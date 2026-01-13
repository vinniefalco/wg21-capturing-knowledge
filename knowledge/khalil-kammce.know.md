# Khalil (kammce): Captured Knowledge

**Interview Date**: January 13, 2026
**Interviewer**: Vinnie Falco
**Duration**: ~83 minutes
**Topics Covered**: Embedded coroutines, stack-based allocation, scheduling philosophy, block states, WG21 framework concerns, static stack analysis

## Executive Summary

Khalil brings deep embedded systems expertise to coroutine design, with a radically different philosophy from desktop/server approaches. His central insight is that embedded systems can use stack-based coroutine allocation with predetermined sizes, avoiding the complexity of dynamic allocation entirely. This requires static analysis to determine maximum stack usage—a problem he's actively solving with tooling that extracts coroutine frame sizes from debug symbols.

His scheduling philosophy inverts the typical model: instead of coroutines specifying their executor at launch, the top-level scheduler dictates policy to blocked coroutines. This enables embedded-specific concerns like low-power modes and hardware timer integration. His "block states" taxonomy (time, IO, synchronization, external) provides a clean abstraction for different blocking reasons.

Khalil shares concerns about WG21's direction on framework standardization, agreeing with Michael Wong that the committee should "pull back on standardizing frameworks." His experience as LEWG minute-taker gave him direct exposure to the complexity explosion around senders/receivers—complexity he found difficult even to document accurately.

---

## Principles

### P1: Stack-Based Coroutine Allocation for Embedded

> *"In this whole framework that I'm building up... the design is around block states... I just need a place to allocate my co-routine frames. I need to put them somewhere so that they can be executed and resumed."*

**The Principle**: Embedded coroutine systems can use predetermined stack-based allocation rather than dynamic heap allocation, eliminating allocator complexity entirely.

**Why It Matters**: This sidesteps HALO concerns, custom allocator propagation, and heap fragmentation—all problems that simply don't exist when frames are stack-allocated with known maximum sizes.

**When to Apply**:
- Embedded systems with deterministic memory requirements
- Systems where maximum coroutine depth is known at design time
- Environments without dynamic allocation support

**Red Flags**:
- Assuming desktop allocation strategies apply to embedded
- Over-engineering allocator propagation for systems that don't need it
- Ignoring static analysis opportunities for size determination

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E1]
related-principles: [P2]
-->

---

### P2: Static Analysis for Stack Size Determination

> *"I'm working on a tool to search through your debug information afterwards to kind of pull out the information... you can get the max stack usage of any function."*

**The Principle**: Coroutine frame sizes can be extracted from debug symbols (Clang's "Coro-something-Ty") and summed along call chains to determine maximum stack requirements at compile/link time.

**Why It Matters**: This transforms "how big should my stack be?" from a runtime mystery into a build-time answer. Combined with stack-based allocation, it enables deterministic memory budgeting.

**When to Apply**:
- Embedded systems with fixed memory budgets
- Safety-critical systems requiring worst-case analysis
- Any system where stack overflow is unacceptable

**Red Flags**:
- Guessing stack sizes through trial and error
- Assuming runtime stack probing is sufficient
- Ignoring compiler debug information capabilities

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: philosophy/library
applies-to: library
confidence: medium
supported-by: [E2]
related-principles: [P1]
-->

---

### P3: Top-Down Scheduler Policy, Not Bottom-Up Executor Binding

> *"I let the top level do it. I don't let my co-routines specify that... In your design, you have your coroutine make the choice of I want this executor to execute this thing... it just seems odd."*

**The Principle**: The top-level scheduler should dictate execution policy to blocked coroutines, rather than coroutines specifying their executor at launch.

**Why It Matters**: Embedded systems have concerns invisible to individual coroutines: power management, hardware timer availability, multi-core delegation. Only the top-level scheduler has this context.

**When to Apply**:
- Embedded systems with power management requirements
- Systems with heterogeneous execution resources
- Designs where coroutines shouldn't know about hardware details

**Red Flags**:
- Coroutines specifying execution resources they can't verify exist
- Bottom-up executor binding in resource-constrained environments
- Ignoring system-level scheduling concerns

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E3]
related-principles: [P4]
-->

---

### P4: Block States as Scheduling Abstraction

> *"The design is around block states... blocked by nothing, blocked by time, blocked by IO, blocked by synchronization, and blocked by external."*

**The Principle**: Categorizing blocking reasons into distinct states (time, IO, synchronization, external) provides clean abstraction for scheduler implementation.

**Why It Matters**: Different block states require different handling: time-blocked coroutines can use hardware timers and low-power modes; IO-blocked coroutines need interrupt handlers; synchronization-blocked coroutines need mutex/semaphore awareness.

**When to Apply**:
- Designing coroutine schedulers for embedded systems
- Implementing power-aware scheduling
- Creating portable abstractions over hardware-specific blocking mechanisms

**Red Flags**:
- Treating all blocking as equivalent
- Ignoring low-power opportunities for time-based blocking
- Coupling blocking semantics to specific hardware mechanisms

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E4]
related-principles: [P3]
-->

---

### P5: co_await on Duration as Syntactic Sugar

> *"I have await_transform on chrono::duration, and that passes a blocked_by_time. This is a shorthand for saying blocked by time."*

**The Principle**: Enabling `co_await` directly on `std::chrono::duration` provides elegant syntax for time-based blocking without explicit API calls.

**Why It Matters**: `co_await 100ms` is immediately readable and communicates intent clearly. The scheduler receives a `blocked_by_time` state with the duration, enabling appropriate handling (busy-wait, sleep, or hardware timer).

**When to Apply**:
- Designing coroutine primitives for timing operations
- Creating ergonomic async APIs
- Implementing await_transform customization points

**Red Flags**:
- Requiring explicit timer objects for simple delays
- Hardcoding sleep implementation in the await mechanism
- Ignoring scheduler flexibility in delay implementation

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E5]
related-principles: [P3, P4]
-->

---

### P6: Futures as Return Value Containers

> *"When you get that return object, that is the container for your return value. The promise keeps a pointer to that container so it can update it with your value."*

**The Principle**: The "future" object returned from a coroutine should be the final destination for the return value, with the promise holding only a pointer to it, enabling emplacement without intermediate moves.

**Why It Matters**: This avoids copying/moving the return value from promise storage to caller storage. The value is constructed directly in its final location.

**When to Apply**:
- Designing coroutine task types where return value copy cost matters
- Systems where the promise should be destroyable immediately after completion
- Minimizing coroutine promise size

**Red Flags**:
- Storing return values in the promise and then moving to caller
- Large promise types that include return value storage
- Assumptions about promise lifetime extending beyond value delivery

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/library
applies-to: library
confidence: medium
supported-by: [E6]
related-principles: [P1]
-->

---

### P7: Framework Standardization Is Dangerous

> *"Michael Wong said something along the lines of we should pull back on standardizing frameworks. And I agree with that. I'm very concerned about standardizing frameworks."*

**The Principle**: WG21 should avoid standardizing large frameworks, preferring smaller, composable primitives that enable diverse approaches.

**Why It Matters**: Frameworks encode specific design philosophies that may not fit all use cases. Senders/receivers works for NVIDIA but may be wrong for networking or embedded. Primitives allow ecosystem diversity.

**When to Apply**:
- Evaluating large standardization proposals
- Assessing whether proposals are frameworks vs. primitives
- Predicting long-term ecosystem effects

**Red Flags**:
- Proposals that require adopting an entire execution model
- "One size fits all" claims for diverse problem domains
- Frameworks without extensive field experience in varied contexts

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E7]
related-principles: [P8]
-->

---

### P8: Coroutines Are a Hodgepodge—And That's Good

> *"After a long time, I realized, especially working with coroutines over and over again... it's this hodgepodge of trying to make everything work for everyone. At first, I really hated it... then I started realizing, oh, but I get to have all of the control."*

**The Principle**: C++ coroutines' apparent complexity provides maximum customization; the "hodgepodge" of customization points enables radically different usage patterns.

**Why It Matters**: Vinnie's networking approach and Khalil's embedded approach both use C++ coroutines but in fundamentally different ways. This flexibility comes from the coroutine machinery's many customization points.

**When to Apply**:
- Teaching coroutines (acknowledge the complexity serves a purpose)
- Designing coroutine primitives (use the customization points)
- Evaluating coroutine library designs (check if they leverage flexibility)

**Red Flags**:
- Proposals that remove coroutine customization points for "simplicity"
- Assuming one coroutine usage pattern is canonical
- Teaching coroutines as if they have one right way

**Supporting Experiences**: E8

<!-- METADATA
kind: principle
id: P8
source-type: tacit
category: philosophy/library
applies-to: library
confidence: medium
supported-by: [E8]
related-principles: [P7]
-->

---

### P9: Senders/Receivers Complexity Is a Documentation Problem

> *"So many papers were about sends and receivers... once you get into someone's weird, like... they're at some other level and they've already passed me trying to figure out even how to write stuff down."*

**The Principle**: If an LEWG minute-taker struggles to document discussions about a feature, that feature may be too complex for widespread adoption.

**Why It Matters**: Khalil's experience as minute-taker provides a calibration point: if someone actively trying to understand and document the discussions can't keep up, ordinary users have little hope.

**When to Apply**:
- Evaluating proposal complexity
- Assessing whether a feature is teachable
- Gauging whether "implementation complexity" will translate to "user complexity"

**Red Flags**:
- Experts discussing features in terms newcomers can't follow
- Rapid-fire papers adjusting complex designs
- Minute-takers struggling to summarize discussions

**Supporting Experiences**: E9

<!-- METADATA
kind: principle
id: P9
source-type: tacit
category: evaluation/red-flags
applies-to: library
confidence: medium
supported-by: [E9]
related-principles: [P7]
-->

---

### P10: Thread-Local Is Acceptable for Embedded

> *"I'm almost at levels on the exceptions guy... I'm fine with thread-local."*

**The Principle**: Thread-local storage is implementable and acceptable in embedded systems, contrary to assumptions that it's desktop-only.

**Why It Matters**: This challenges the assumption that TLS is "heavyweight" or "not embedded-friendly." Khalil has implemented TLS for ARM and other embedded targets.

**When to Apply**:
- Evaluating embedded compatibility of designs using TLS
- Deciding whether to avoid TLS for "portability"
- Implementing coroutine context propagation on embedded

**Red Flags**:
- Assuming TLS is unavailable on embedded platforms
- Over-engineering alternatives to avoid TLS
- Not checking actual embedded TLS support

**Supporting Experiences**: E10

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: philosophy/library
applies-to: library
confidence: medium
supported-by: [E10]
related-principles: [P1]
-->

---

## Experiences

### E1: Stack-Based Coroutine Context Design

**Context**: Khalil designed a coroutine library for embedded systems.

**What Happened**: Instead of using dynamic allocation or complex allocator propagation, he designed around a fixed stack buffer per "context" that holds all coroutine frames for a chain.

**The Outcome**: Success—"If you're curious, like, oh, what do you do when you run out of memory... that means you chose the wrong stack depth. Same thing that we do in all of embedded software."

**The Lesson**: Embedded constraints enable simpler solutions when you accept them as design inputs.

> *"I just need a place to allocate my co-routine frames. I need to put them somewhere so that they can be executed and resumed."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: philosophy/library
applies-to: library
outcome: success
features: [coroutines, embedded, allocation]
supports: [P1]
-->

---

### E2: Debug Symbol Stack Analysis

**Context**: Determining coroutine stack requirements statically.

**What Happened**: Khalil discovered that Clang emits coroutine frame size information in debug symbols (similar to GCC's `-fstack-usage`). He's building tooling to extract this and sum along call chains.

**The Outcome**: In progress—"I probably can just get myself or something to do that"—but the approach is sound for deterministic stack budgeting.

**The Lesson**: Compiler debug information can solve problems that seem to require runtime inspection.

> *"The information about how big the stack frames are is in a debug symbol that clang dumps into your debug objects."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: philosophy/library
applies-to: library
outcome: mixed
features: [coroutines, static-analysis, debug-info]
supports: [P2]
-->

---

### E3: Scheduler-Driven vs Launch-Driven Execution

**Context**: Comparing Khalil's top-down scheduler approach with Vinnie's launch-site executor binding.

**What Happened**: Khalil questioned why coroutines should specify their executor when only the top-level scheduler knows about power management, hardware timers, and multi-core delegation.

**The Outcome**: Two valid but different models—Vinnie's for networking (where strand/thread affinity matters), Khalil's for embedded (where system-level concerns dominate).

**The Lesson**: Execution model should match domain requirements; neither approach is universally correct.

> *"I let the top level do it. I don't let my co-routines specify that."*

**Supports Principles**: P3

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: philosophy/library
applies-to: library
outcome: mixed
features: [coroutines, scheduling, embedded]
supports: [P3]
-->

---

### E4: Block States Taxonomy

**Context**: Designing the scheduling abstraction for embedded coroutines.

**What Happened**: Khalil categorized all blocking reasons into five states: nothing, time, IO, synchronization, and external. Each state enables different scheduler optimizations.

**The Outcome**: Success—clean abstraction that enables power-aware scheduling and hardware-specific optimizations.

**The Lesson**: Categorizing blocking reasons at the type level enables scheduler specialization.

> *"Blocked by nothing, blocked by time, blocked by IO, blocked by synchronization, and blocked by external."*

**Supports Principles**: P4

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: philosophy/library
applies-to: library
outcome: success
features: [coroutines, scheduling, embedded]
supports: [P4]
-->

---

### E5: The co_await Duration Syntax

**Context**: Creating ergonomic time-based blocking.

**What Happened**: Khalil implemented `await_transform` for `std::chrono::duration`, allowing `co_await 100ms` to produce a `blocked_by_time` state.

**The Outcome**: Success—Vinnie loved it: "I love that syntax. Is that anyone, anyone else done that?" 

**The Lesson**: `await_transform` customization enables domain-specific ergonomics.

> *"I have await_transform on chrono::duration, and that passes a blocked_by_time."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: philosophy/library
applies-to: library
outcome: success
features: [coroutines, chrono, await_transform]
supports: [P5]
-->

---

### E6: Promise-to-Future Pointer Design

**Context**: Avoiding return value copies in coroutine completion.

**What Happened**: Khalil designed his "future" type to be the final container for return values, with the promise holding only a pointer. Values are emplaced directly into the future.

**The Outcome**: Success—"I want when the value is finished being created for it to be put into its container and then for the promise to be able to be destroyed at any point in time."

**The Lesson**: Inverting the typical ownership model eliminates a copy.

> *"The promise keeps a pointer to that container so it can update it with your value."*

**Supports Principles**: P6

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: philosophy/library
applies-to: library
outcome: success
features: [coroutines, promise, return-values]
supports: [P6]
-->

---

### E7: LEWG Senders/Receivers Fatigue

**Context**: Khalil's experience as LEWG minute-taker during senders/receivers development.

**What Happened**: So many papers were about senders/receivers that Khalil eventually stopped being minute-taker. The discussions were too complex to summarize—"they're at some other level and they've already passed me."

**The Outcome**: Mixed—senders/receivers was standardized, but the complexity drove away a contributor. David Sankel shared Khalil's concerns.

**The Lesson**: Volume and complexity of papers on a feature may indicate insufficient maturity or over-engineering.

> *"I stopped being a minute taker for LEWG. It's because so many papers were about sends and receivers."*

**Supports Principles**: P7, P9

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: groups/lewg
applies-to: library
outcome: mixed
features: [senders-receivers, P2300, WG21-process]
supports: [P7, P9]
-->

---

### E8: Learning to Love Coroutine Complexity

**Context**: Khalil's journey from hating coroutine complexity to appreciating it.

**What Happened**: Initially, Khalil (and his students) hated C++ coroutines' apparent complexity. Over time, he realized the customization points gave him complete control for embedded use cases.

**The Outcome**: Success—embracing the flexibility enabled his stack-based, scheduler-driven design.

**The Lesson**: Apparent complexity may be necessary flexibility in disguise.

> *"At first, I really hated it... then I started realizing, oh, but I get to have all of the control, every single knob I can tune."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E8
source-type: tacit
category: philosophy/library
applies-to: library
outcome: success
features: [coroutines, customization-points]
supports: [P8]
-->

---

### E9: The Minute-Taking Complexity Test

**Context**: Using minute-taking difficulty as a complexity metric.

**What Happened**: Khalil's struggle to document senders/receivers discussions, combined with David Sankel's similar difficulty understanding the feature, suggests the complexity is inherent, not incidental.

**The Outcome**: Both Khalil and Sankel concluded: "If Khalil, the person who's been minute-taking all this stuff, is having a hard time... what hope do we have for new people?"

**The Lesson**: If experts struggle to follow, users will struggle more.

> *"Me and him agree on the fact that we are both afraid of senders and receivers. He doesn't, he has a hard time wrapping his head around it, and I do too."*

**Supports Principles**: P9

<!-- METADATA
kind: experience
id: E9
source-type: tacit
category: evaluation/red-flags
applies-to: library
outcome: failure
features: [senders-receivers, complexity]
supports: [P9]
-->

---

### E10: TLS on Embedded Platforms

**Context**: Discussing whether TLS is embedded-hostile.

**What Happened**: Khalil noted he's "finished my demos of showing like how you can use TLS... how to implement it yourself with ARM and other devices."

**The Outcome**: Success—TLS works on embedded, contradicting assumptions about its heavyweight nature.

**The Lesson**: Don't assume desktop features are unavailable on embedded without checking.

> *"Thread-local is not that bad. I've actually at some point want to finish my implementation."*

**Supports Principles**: P10

<!-- METADATA
kind: experience
id: E10
source-type: explicit
category: philosophy/library
applies-to: library
outcome: success
features: [TLS, embedded, ARM]
supports: [P10]
-->

---

## Evaluation Checklists

### When Reviewing Proposals for Embedded Compatibility

- [ ] Does the design assume dynamic allocation is available?
- [ ] Can frame/buffer sizes be determined statically?
- [ ] Does the scheduler model allow top-down policy enforcement?
- [ ] Are blocking reasons categorized in a way that enables power-aware scheduling?
- [ ] Can it work without TLS, or is TLS support checked on target platforms?

**Questions to Ask**:
1. "What's the maximum stack/memory usage, and can it be computed at build time?"
2. "How does a system-level scheduler influence execution policy?"
3. "What happens when the block is due to time—can I use a hardware timer and sleep?"
4. "Does this require heap allocation, and if so, can I provide a fixed-size pool?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P3, P4]
-->

---

### When Reviewing Framework Proposals

- [ ] Does this proposal encode a single execution model?
- [ ] Are there field experience reports from diverse domains (not just the proposer's)?
- [ ] Can an LEWG minute-taker summarize discussions accurately?
- [ ] Is the paper count for this feature growing faster than understanding?
- [ ] Does this proposal enable or constrain ecosystem diversity?

**Questions to Ask**:
1. "Would this framework work for embedded? For networking? For GPU?"
2. "How many papers have been written to adjust this design?"
3. "Can experts outside the proposal team explain how it works?"
4. "What would be lost if we standardized primitives instead of this framework?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P7, P8, P9]
-->

---

## Open Questions

1. What exactly is the Clang debug symbol type that contains coroutine frame sizes? ("Coro something Ty")
2. How does the `blocked_by_external` state work—what triggers resumption?
3. How does Khalil's scheduler handle the case where multiple coroutines are blocked_by_time with different deadlines?
4. What's the full interface of the "context" class that provides stack memory?
5. How are synchronization primitives (mutexes, semaphores) integrated with `blocked_by_synchronization`?
6. What's the exact promise size target for embedded? ("I probably have like 4 words, 4 pointers in total size")

---

## Raw Transcript Reference

See: `inputs/khalil.md` (Khalil's contributions)
