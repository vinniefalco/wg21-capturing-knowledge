# Khalil Estell & Vinnie Falco: Captured Knowledge

**Interview Date**: 2025-01-13
**Participants**: Khalil Estell (kammce), Vinnie Falco
**Duration**: ~83 minutes
**Topics Covered**: C++ coroutines, executor affinity, dispatcher design, JUCB (Just Use Coroutines Bro), frame allocation, thread-local storage, type erasure, senders/receivers critique, embedded coroutines, WG21 standardization critique, framework-first vs use-case-first design, knowledge capture workflow, paper evaluation tools

## Executive Summary

This technical discussion between Khalil Estell and Vinnie Falco represents a deep dive into competing coroutine design philosophies for C++, contrasting networking-focused approaches with embedded systems requirements. The conversation reveals fundamental insights about why different domains require different solutions and why the C++ standardization process struggles with framework-oriented proposals.

Vinnie Falco presents his "JUCB" (Just Use Coroutines, Bro) philosophy, demonstrating how coroutines can outperform callback-based composition at sufficient depth due to the fixed overhead of a coroutine handle versus growing callback state. His key technical contribution is the "affinity awaitable" protocol—a mechanism for propagating executor context through coroutine chains using zero-cost type erasure, achieved by exploiting the guaranteed lifetime extension of parameters passed to promise functions.

Khalil Estell counters with an embedded-first approach where coroutine frames are allocated on a pre-sized stack, schedulers are injected from above rather than specified by coroutines, and the system optimizes for deterministic behavior over flexibility. His insight that "the person at the top level sets the policy" represents a fundamental inversion of the senders/receivers model.

Most striking is their shared critique of WG21's framework-first standardization approach. Both agree that senders/receivers (P2300) optimizes for GPU/heterogeneous computing at the expense of networking and embedded use cases, and that the committee's rush to standardize frameworks before they have real-world scars leads to poor outcomes. Falco's knowledge capture workflow and paper evaluation tools represent an attempt to inject empirical rigor into WG21's decision-making process.

---

## Principles

### P-KV-001: Allocation Pays for Type Erasure

**Statement**: The allocation that cannot be avoided in asynchronous IO can pay for the type erasure needed for clean APIs.

**Category**: Design Philosophy / Technical Architecture

**Source Type**: Explicit

**Supporting Quote**:
> "The allocation that we can't avoid pays for the type erasure that we need. That's principle number one of this whole philosophy."

**Context**: When a coroutine suspends to call into the operating system, memory must be allocated to preserve state. This mandatory allocation can also store type-erased function pointers for the dispatcher, enabling clean task types that don't leak executor types into template parameters.

**Actionable Guidance**:
- Accept that OS-level async IO requires allocation; don't fight it
- Use that allocation to store type-erased dispatch functions
- Keep task types clean by not propagating executor types through templates
- Fixed cost (two pointers: object + function) supports stateful allocators

**Corroborating Sources**: Peter Dimov's coroutine advocacy, ASIO design patterns

---

### P-KV-002: Promise Parameter Lifetime Extension

**Statement**: Parameters passed into promise functions from calling coroutines have a lifetime that extends beyond the coroutine frame, enabling zero-cost type erasure.

**Category**: Technical Architecture / Language Mechanics

**Source Type**: Explicit

**Supporting Quote**:
> "Parameters passed into the promise functions from the calling coroutine have a lifetime that extends beyond your frame. That is the key insight. So once you internalize that, now you can have type erasure that's for free."

**Context**: This C++ language guarantee means that when a coroutine receives a dispatcher parameter, it can safely store a pointer to the type-erased version without additional allocation, because the caller's frame (and thus the original dispatcher) outlives the callee.

**Actionable Guidance**:
- Store pointers to caller-provided parameters rather than copying
- Use this for type-erased dispatchers, allocators, and stop tokens
- Enables O(1) overhead for passing context through coroutine chains
- Requires all coroutines in chain to opt into the protocol

---

### P-KV-003: IO Objects Should Not Specify Executors

**Statement**: IO objects (sockets, files) should not be bound to specific executors; execution context is the client's responsibility.

**Category**: Design Philosophy / API Design

**Source Type**: Explicit

**Supporting Quote**:
> "IO objects don't care about where they run. Like they run at the operating system level... You shouldn't bake the executor into the IO object. The executor is actually the responsibility... in the client code because only you know if you're doing multi-threading."

**Context**: A socket knows how to connect, read, and write. It doesn't know whether the application needs strand-based serialization, priority scheduling, or single-threaded operation. Baking executor affinity into IO objects creates inflexible designs.

**Actionable Guidance**:
- Design IO objects with minimal responsibilities (just the IO operations)
- Let client code specify execution context at the call site
- Pass dispatcher/executor through the coroutine chain, not through IO objects
- Enables the same IO code to work with different threading models

---

### P-KV-004: Halo Optimization Cannot Save IO

**Statement**: Heap allocation elision (HALO) cannot work for operating-system-level asynchronous IO because the calling thread must be released.

**Category**: Technical Reality / Language Limitations

**Source Type**: Explicit

**Supporting Quote**:
> "Here's the reality of it. It can never work for IO. Because at the end of the day, if you're calling into the operating system to do something, and then your coroutine suspends, you have to allocate memory. Because otherwise you can never get back control of the thread that launched the operation."

**Context**: HALO works by proving at compile time that a coroutine's lifetime is bounded by its caller. For IO, the thread must return to the reactor to service other operations, breaking this assumption.

**Actionable Guidance**:
- Don't rely on HALO for networking/IO code
- Design allocation strategies that assume allocation will happen
- Use frame recyclers or custom allocators for performance-critical paths
- Accept allocation and optimize within that constraint

---

### P-KV-005: Senders/Receivers Connect Template Problem

**Statement**: The `connect` function in senders/receivers being a template forces all types in the chain to be visible at the call site, preventing ABI stability and type erasure.

**Category**: Technical Architecture / Standardization Critique

**Source Type**: Explicit

**Supporting Quote**:
> "Connect... is the fundamental operation in senders and receivers... and this function is a template... The implications, Khalil, is that every type in the entire chain has to be visible at the call site of the co_await. That means you can't have any... you can't hide any of your implementation. You can never be ABI stable."

**Context**: P2300 (senders/receivers) requires template instantiation through the entire composition chain. This is acceptable for GPU kernels compiled together but problematic for networking where you want to link against different SSL libraries without recompilation.

**Actionable Guidance**:
- Recognize that senders/receivers trades ABI stability for compile-time optimization
- For networking, prefer designs that enable type erasure at API boundaries
- Allow switching implementations (e.g., OpenSSL to WolfSSL) via linking
- Accept that different domains have different optimal designs

---

### P-KV-006: Domain-Specific Solutions Over Universal Frameworks

**Statement**: There is no single coroutine/async model that works for all domains; networking, GPU computing, and embedded systems each require different designs.

**Category**: Design Philosophy / Standardization Critique

**Source Type**: Explicit

**Supporting Quote**:
> "What I've learned from this, Khalil... is that there is not one model that works for everyone. Like senders and receivers works for Nvidia. Great. OK, nice. Cool, cool story, bro. What I've done, the thing that I make is amazing for networking, but... my library is not suitable for you."

**Context**: Vinnie's affinity-awaitable protocol optimizes for multi-threaded reactor-based networking. Khalil's stack-allocated approach optimizes for deterministic embedded systems. P2300 optimizes for GPU kernel composition. None is universally superior.

**Actionable Guidance**:
- Resist pressure to standardize "one true framework"
- Allow library-level solutions to coexist
- Standardize vocabulary types and primitives, not complete frameworks
- Evaluate proposals against specific domain requirements

**Corroborating Sources**: Michael Wong's comment about pulling back on standardizing frameworks

---

### P-KV-007: Top-Level Policy Injection

**Statement**: In embedded systems, execution policy (scheduling, time management, power modes) should be controlled from the top level, not specified by individual coroutines.

**Category**: Design Philosophy / Domain-Specific

**Source Type**: Explicit (Khalil)

**Supporting Quote**:
> "In your design, you have your coroutine make the choice of I want this executor to execute this thing... it just seems odd because it needs a certain resource to exist before the function gets called... The person who created the context, who passes it to the first top level coroutine, that is what sets the policy of how time is managed."

**Context**: Khalil's embedded design inverts the typical approach: instead of coroutines requesting execution on specific executors, coroutines report their blocked state and the top-level scheduler decides how to handle it.

**Actionable Guidance**:
- For embedded: inject schedulers from above, not from within coroutines
- Allow the same coroutine code to work with different scheduling policies
- Expose "blocked by" states (time, IO, synchronization, external)
- Let the integrator (not the library) decide sleep strategies

---

### P-KV-008: Use-Case-First Versus Framework-First Design

**Statement**: Libraries that start with real use cases develop "scars" that make them harder to standardize but more useful; framework-first designs pass committee review more easily but serve users poorly.

**Category**: Standardization Process / Design Philosophy

**Source Type**: Explicit

**Supporting Quote**:
> "When you do use case first, when you have a library that's 5, 10, 15, 20 years old, it has scars... from having to satisfy actual real world needs, it deviates from the theoretically pure foundation and the reality is that these big framework first designs, they're more easily able to pass through the committee because people can look at it and... they don't have any real world thing to compare it to."

**Context**: Peter Dimov's philosophy of starting from what the user writes and designing backwards. Committee members can more easily critique scarred, battle-tested APIs against their real-world experience than evaluate pristine frameworks with no deployment history.

**Actionable Guidance**:
- Start library design from user-facing code, not abstract concepts
- Accumulate real usage before proposing standardization
- View API "scars" as evidence of real-world fitness
- Be skeptical of pristine frameworks without deployment history

**Corroborating Sources**: Peter Dimov, Boost review process philosophy

---

### P-KV-009: Excessive In-Flight Papers Signal Immaturity

**Statement**: When a proposal requires many concurrent papers to fix or extend it, the underlying design is not mature enough for standardization.

**Category**: Standardization Process / Evaluation Criteria

**Source Type**: Explicit

**Supporting Quote**:
> "The fact that he has like 10 papers in flight related to std::execution tells you that the design is not mature."

**Context**: A proliferation of papers addressing gaps, fixes, and extensions to a recently standardized feature suggests it was standardized prematurely. Mature designs should be relatively stable before standardization.

**Actionable Guidance**:
- Track the number of follow-up papers a proposal generates
- Treat high paper counts as a signal of design instability
- Delay standardization until the core design settles
- Use paper count as an evaluation criterion in paper review

---

### P-KV-010: Coroutine Composition Efficiency Crossover

**Statement**: Callback-based async composition outperforms coroutines for shallow chains but loses at deeper composition due to growing state sizes versus fixed coroutine handles.

**Category**: Technical Architecture / Performance

**Source Type**: Explicit

**Supporting Quote**:
> "Every layer you have to do a move... into a bigger and bigger struct, and that shit starts adding up... there's a point where the coroutines become better. Because the coroutine callback... it's only a pointer... if you have 5 layers of composition in ASIO, that could be 500 bytes, whereas if you have 5 layers of composition with coroutines, it's only 40 bytes."

**Context**: ASIO-style composition grows the handler state at each layer. Coroutine composition maintains a fixed-size handle (pointer). At sufficient depth, the memory and copy overhead of callback composition exceeds coroutine overhead.

**Actionable Guidance**:
- For shallow composition (1-2 layers), callbacks may be more efficient
- For deep composition (5+ layers), coroutines likely win
- Measure actual composition depth in real applications
- Don't dismiss coroutines based on single-layer overhead

---

### P-KV-011: Thread-Local Allocation Window

**Statement**: C++17's evaluation order guarantees create a safe window for using thread-local storage to pass allocators to coroutine frames.

**Category**: Technical Architecture / Language Mechanics

**Source Type**: Explicit

**Supporting Quote**:
> "A little thing happened in C++17, it guarantees that this gets evaluated first... The question is how does the allocator propagate through to the... if my task awaits another coroutine, how does it propagate? ... we use a thread-local."

**Context**: The challenge is getting a custom allocator into operator new for coroutine frames without polluting the API. C++17's left-to-right function argument evaluation allows setting a thread-local before the coroutine frame is allocated.

**Actionable Guidance**:
- Use functor syntax `async_run(ex)(my_task)` to ensure evaluation order
- Set thread-local allocator in the functor's constructor
- Clear thread-local after frame allocation completes
- Restore thread-local when coroutine resumes (for nested launches)

---

### P-KV-012: AI-Assisted Knowledge Capture for Standards

**Statement**: Interviewing committee members and using AI to extract generating principles can provide an empirical basis for evaluating standardization proposals.

**Category**: Process Innovation / Standardization

**Source Type**: Explicit

**Supporting Quote**:
> "It's called knowledge capture... it's about interviewing people and then using AI to distill what are called the generating principles... if you interview like multiple people, you can get... confidence... what I did was I used my knowledge capture prompt to capture the knowledge. And then... another algorithm which correlates what are the things that... is everybody saying that's the same?"

**Context**: WG21 lacks codified principles beyond broad guidelines. By interviewing experienced committee members, extracting principles, and correlating across interviews, a more rigorous evaluation framework emerges.

**Actionable Guidance**:
- Interview diverse committee members about their evaluation criteria
- Use AI to extract and correlate principles across interviews
- Create automated paper evaluation against extracted principles
- Provide signal to authors and reviewers before meetings

---

### P-KV-013: AI Enables Voice for Implementation-Focused Developers

**Statement**: AI tools enable developers who prefer writing code to writing prose to contribute to the standards process through well-articulated papers.

**Category**: Process Innovation / Accessibility

**Source Type**: Explicit

**Supporting Quote**:
> "AI gave me a voice because previously, you know... I want to write code. I don't want to write papers. And I had all these ideas and the AI lets me bring them to life."

**Context**: The standards process historically advantages those who write well in committee-style prose. AI can translate implementation insights into formal papers, lowering the barrier for practitioners.

**Actionable Guidance**:
- Use AI to draft papers from working implementations
- Have AI generate documentation from code comments and structure
- Focus human effort on ideas and code; let AI handle prose
- Review AI output carefully to ensure it captures your voice

---

## Experiences

### E-KV-001: Converting from Callback Skeptic to Coroutine Advocate

**Narrative**: Vinnie Falco spent three years disagreeing with Peter Dimov's "just use coroutines" advice, preferring C++11-style callbacks for broader audience reach. When designing an Express.js-like C++ server, API pressure pushed him toward coroutines for cleaner syntax. Investigating coroutine performance, he discovered that callbacks aren't superior—at sufficient composition depth, coroutines win on both clarity and efficiency.

**Key Quote**:
> "For the last 3 years I've been disagreeing and I've had to hear Peter Dimov like... it's so irritating he's saying this shit all over again... But a funny thing happens. I found out that they actually don't suck. In fact, they're rather good at some point."

**Lesson**: Initial resistance to new paradigms may be based on incomplete analysis. Performance characteristics can invert at different scales of usage.

**Linked Principles**: P-KV-010 (Composition Efficiency Crossover)

---

### E-KV-002: AI Writing Coroutine Boilerplate

**Narrative**: Vinnie found coroutine machinery (await_suspend, final_suspend, etc.) "incredibly laborious" and avoided coroutines partly because of implementation complexity. When AI became capable of writing this boilerplate correctly, he could finally express his design ideas without getting lost in the mechanical details.

**Key Quote**:
> "I let the AI write all this... I find all of this incredibly laborious. It's why I've avoided coroutines, you know, but it's what we have... But now that AI can do it... I can finally, I have a voice now."

**Lesson**: AI can lower the barrier to exploring complex language features by handling mechanical details while humans focus on design.

**Linked Principles**: P-KV-013 (AI Enables Voice)

---

### E-KV-003: Embedded Stack-Based Coroutine Design

**Narrative**: Khalil designed an embedded coroutine library with fundamentally different assumptions than networking libraries: a pre-sized stack for frame allocation, scheduler injection from above, and block-state reporting instead of executor specification. This emerged from embedded-specific needs: deterministic memory usage, low-power sleep modes, and hardware interrupt-driven completion.

**Key Quote**:
> "What do you do when you run out of memory or... your stack depth, that means you chose the wrong stack depth. Same thing that we do in all of embedded software, which is you map out how much you're going to need upfront."

**Lesson**: Domain constraints (embedded vs. networking vs. GPU) lead to fundamentally different optimal designs. One-size-fits-all frameworks will underserve specialized domains.

**Linked Principles**: P-KV-006 (Domain-Specific Solutions), P-KV-007 (Top-Level Policy Injection)

---

### E-KV-004: Senders/Receivers Learning Curve Concern

**Narrative**: Khalil, despite actively contributing to WG21 as a minute-taker for LEWG, found senders/receivers (P2300) difficult to understand. He eventually stopped minute-taking partly because the deep technical discussions exceeded his ability to compress them. David Sankel expressed similar concerns, suggesting that if engaged committee members struggle, newcomers will fare worse.

**Key Quote**:
> "Senders receivers is... me and David... agree on the fact that we are both afraid of senders and receivers. He doesn't, he has a hard time wrapping his head around it, and I do too... if Khalil, the person who's been minuting all this stuff, is having a hard time... then what hope do we have for like new people."

**Lesson**: Complexity that challenges experienced committee members signals potential adoption problems. The committee should weight learnability more heavily.

**Linked Principles**: P-KV-005 (Connect Template Problem), P-KV-006 (Domain-Specific Solutions)

---

### E-KV-005: Paper Tester Reception Concern

**Narrative**: When Vinnie described his AI-powered paper evaluation tool, both he and Khalil acknowledged the political risk of publishing it to WG21. Previous AI-generated content on the mailing received hostile reception. Vinnie's CEO advised against publishing. Khalil suggested continuing to show it to individuals rather than formally proposing it.

**Key Quote**:
> "The moment you put something like this on the mailing, you'll... people will collectively try to curb stomp you... I like the idea. I think you should continue to bring it up to other people."

**Lesson**: Process innovations face political resistance even when technically sound. Informal adoption may precede formal acceptance.

**Linked Principles**: P-KV-012 (AI-Assisted Knowledge Capture)

---

### E-KV-006: The co_await Duration Syntax Discovery

**Narrative**: Khalil implemented a syntax where `co_await std::chrono::duration` directly suspends for that time period, using `await_transform` to convert durations into blocked-by-time states. This emerged from embedded needs for sleep/delay without specifying implementation details.

**Key Quote**:
> "I have `await_transform` on chrono duration, and that passes a blocked by time... this just passes the 100 milliseconds into the scheduler, and the scheduler can then... it's one of the block states that the scheduler has to... wait that duration of time before it resumes your coroutine."

**Lesson**: Domain-specific syntactic sugar can dramatically improve API ergonomics. User-facing syntax should drive implementation, not vice versa.

**Linked Principles**: P-KV-007 (Top-Level Policy Injection), P-KV-008 (Use-Case-First Design)

---

## Evaluation Checklists

### For Async/Coroutine Library Proposals

1. **Allocation Strategy**
   - [ ] Does the proposal acknowledge where allocation is unavoidable?
   - [ ] Can custom allocators be provided without polluting API signatures?
   - [ ] Is frame memory management documented?

2. **Executor/Scheduler Model**
   - [ ] Can IO objects be used independently of execution context?
   - [ ] Is execution policy specified at launch or by each coroutine?
   - [ ] Does the model support both single-threaded and multi-threaded use?

3. **Type Erasure and ABI**
   - [ ] Can implementations be changed without recompilation?
   - [ ] Are template instantiation chains bounded?
   - [ ] Is the type-erased overhead documented?

4. **Domain Fit**
   - [ ] Is the primary domain (networking, GPU, embedded) clearly stated?
   - [ ] Are tradeoffs for other domains acknowledged?
   - [ ] Are domain-specific requirements (real-time, deterministic, low-power) addressed?

5. **Complexity**
   - [ ] Can an engaged committee member explain the core model?
   - [ ] Is the "hello world" equivalent shown and simple?
   - [ ] Are advanced features layered, not required?

### For Framework Standardization Proposals

1. **Maturity Signals**
   - [ ] How many years of production use exist?
   - [ ] How many follow-up papers are in flight?
   - [ ] What real applications use it?

2. **Design Origin**
   - [ ] Did the design start from user code (use-case-first)?
   - [ ] Or from abstract architecture (framework-first)?
   - [ ] What "scars" from real usage are visible?

3. **Scope Appropriateness**
   - [ ] Could this be a library rather than standard?
   - [ ] Does standardization enable something impossible otherwise?
   - [ ] Is the vocabulary-type portion separable from the framework?

---

## Open Questions

1. **Optimal Composition Depth Threshold**: At what depth of async composition do coroutines definitively outperform callbacks? Is this measurable across diverse workloads?

2. **Embedded Coroutine Standardization**: Should there be a minimal embedded-compatible coroutine vocabulary in the standard, separate from full frameworks?

3. **AI Paper Evaluation Acceptance**: What would it take for WG21 to formally adopt AI-assisted paper evaluation? What safeguards would be required?

4. **Frame Size Static Analysis**: Can coroutine frame sizes be reliably determined at compile time across all major compilers? Is standardization of this metadata feasible?

5. **Senders/Receivers Networking Story**: Given the ABI concerns raised, will P2300 ever be suitable for networking, or should networking remain with ASIO-style approaches?

---

## Raw Transcript Reference

**Source**: Huddle recording transcript, January 13, 2025
**Participants**: Vinnie Falco (@Vinnie), Khalil Estell (@kammce)
**Duration**: 11:00 AM - 12:23 PM Pacific Time
**Format**: Auto-generated transcript with speaker attribution

The transcript covers:
- Technical walkthrough of affinity-awaitable protocol (0:00-30:00)
- Frame allocation and thread-local strategy (30:00-45:00)
- Khalil's embedded coroutine design presentation (45:00-60:00)
- WG21 critique and framework-first problems (60:00-75:00)
- Knowledge capture and paper tester demonstration (75:00-83:00)
