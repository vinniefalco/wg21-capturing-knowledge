# Billy O'Neal: Captured Knowledge

**Interview Date**: January 21, 2026
**Interviewer**: Vinnie Falco
**Duration**: ~72 minutes
**Topics Covered**: ABI stability, vcpkg, networking TS, parallel algorithms, task-based concurrency vs message pumps, C++20 coroutines, C++20 modules, package management coordination failures, CMake ecosystem

## Executive Summary

Billy O'Neal brings a unique perspective as someone who worked on both the MSVC STL implementation and vcpkg package management. His experience reveals critical tensions between what can be standardized and what should be left to the ecosystem. A central theme is that ABI stability requirements fundamentally constrain what the standard library can deliver—features that work well in Boost (which breaks ABI regularly) may become permanently suboptimal once frozen in `std::`.

His transition from the STL libraries team to vcpkg was motivated by the networking TS: he saw no path to implement TLS with ABI stability guarantees, leading him to conclude that getting users "real ASIO" through package management was more valuable than a potentially unshippable standard component. This pragmatic assessment—that some problems are better solved outside the standard—recurs throughout the interview.

O'Neal also provides deep insight into coordination failures plaguing C++: the modules build system interoperability problem, the executor/concurrency vocabulary type problem, and why C++ can't easily adopt NPM-style dependency management (ODR violations, non-semantic versioning). His parallel algorithms implementation philosophy of "minimize badness when people use it incorrectly" reflects hard-won understanding that `std::` features reach users who don't know what they're doing.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: ABI Stability Freezes Suboptimality

> *"I implemented the Boyer-Moore Searcher paper, and then my implementation that I shipped is worse than what you can get from Boost, like less than a year after shipping it."*

**The Principle**: Once a feature enters the standard library with ABI stability requirements, implementation bugs and suboptimal designs become permanently frozen, while ecosystem alternatives continue to improve.

**Why It Matters**: The standard library's ABI stability guarantee means that even straightforward algorithm implementations can become permanently inferior to ecosystem alternatives. This creates a paradox where standardization—intended to provide the best default—may lock users into worse solutions.

**When to Apply**: When evaluating library proposals, especially those where the ecosystem has actively-maintained alternatives that can break ABI freely.

**Red Flags**:
- Proposal is for an algorithm or data structure where performance tuning is ongoing
- Reference implementation has known limitations the author plans to fix "later"
- Boost/ecosystem version has broken ABI to fix issues since initial release
- No discussion of what happens when better approaches are discovered post-standardization

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: philosophy/evolution
applies-to: library
confidence: high
supported-by: [E1]
related-principles: [P2, P3]
-->

---

### P2: TLS Disqualifies Networking from Standard Library

> *"I do not think it is responsible to put networking in the standard without TLS and I don't know of any TLS implementation that will ever meet std ABI requirements."*

**The Principle**: Features requiring integration with components that cannot meet ABI stability requirements should not be standardized, even if the core feature itself could be stabilized.

**Why It Matters**: Networking without TLS is incomplete for modern use. But TLS implementations (OpenSSL, WolfSSL, etc.) break ABI regularly. This creates an irreconcilable tension: either ship incomplete networking, or ship networking that can never integrate with real-world TLS.

**When to Apply**: When evaluating proposals that have hard dependencies on external ecosystems that don't follow ABI stability conventions.

**Red Flags**:
- Proposal requires integration with security libraries (TLS, crypto)
- Core functionality incomplete without rapidly-evolving external components
- "We'll add TLS support later" without addressing ABI implications
- Proposal assumes ecosystem components will stabilize their ABIs

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P3]
-->

---

### P3: Ecosystem Delivery Over Incomplete Standardization

> *"It doesn't matter that it's in std. Like, it's important to get people the things that actually solve the problems because there's a whole universe of problems that have good solutions that won't necessarily meet the requirements to be in std."*

**The Principle**: Package management that delivers current ecosystem solutions is more valuable than standardization that delivers frozen, potentially incomplete solutions.

**Why It Matters**: The advantage of `std::` is ubiquity ("it's everywhere"), but the corollary is everything in `std::` must work everywhere. For features that can't meet this bar, package managers like vcpkg provide a better delivery mechanism than compromised standardization.

**When to Apply**: When a proposal seems motivated primarily by "we need this in std" rather than "std can uniquely solve this problem."

**Red Flags**:
- Proposal motivated by "C++ doesn't have X, other languages do"
- Feature works well in ecosystem but requires compromises for standardization
- Platform-specific functionality being forced into portable abstraction
- "GPGPU library that doesn't need to fit on a PIC"

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: belongs/ecosystem
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P2]
-->

---

### P4: IO Concurrency and Parallel Computation Are Distinct Domains

> *"The networking TS and similar concurrency models... is I have a small amount of compute resources... and the majority of what I am doing is waiting for IO. [Parallel algorithms] I am only doing this pure computational problem, and it only lives inside CPU land."*

**The Principle**: IO-bound concurrency (networking, async file IO) and CPU-bound parallelism (parallel algorithms) are fundamentally different problem domains with different optimal solutions; attempts to unify them have not seen broad adoption.

**Why It Matters**: Proposals that try to create unified concurrency abstractions must acknowledge these domains have competing goals. IO concurrency optimizes for not blocking while waiting; parallel computation optimizes for saturating CPU resources.

**When to Apply**: When evaluating concurrency/parallelism proposals, or proposals claiming to unify async/parallel execution.

**Red Flags**:
- Proposal claims to solve both IO waiting and CPU parallelism with one abstraction
- No acknowledgment of the IO-vs-compute distinction
- Examples only show one domain while claiming generality
- "Executors will solve everything"

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: philosophy/coherence
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P5, P6]
-->

---

### P5: Explicit Message Pumps Fail Fast; Task-Based Concurrency Hides Bugs

> *"It's really easy when you have explicit message pumps to not write things that block incorrectly because you can run the message pump with one thread. And if you write something that blocks, your program will deadlock immediately."*

**The Principle**: Concurrency models where you explicitly pass in the execution context (IO context, message pump) expose blocking bugs immediately with single-threaded testing. Task-based models that hide execution context allow bugs to lurk until production load.

**Why It Matters**: The networking TS model is harder to write, but "if it works, it's probably correct." Task-based concurrency is easier to write incorrectly in ways that only manifest under load (the "513th thread" problem).

**When to Apply**: When evaluating async/concurrency API designs, especially proposals influenced by task-based systems from other languages.

**Red Flags**:
- Concurrency proposal has implicit/ambient execution context
- "Where does `.then()` run?" is not clearly answered
- No discussion of testing strategies for concurrent code
- Examples only work because thread pool has enough threads

**Supporting Experiences**: E3, E4

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [E3, E4]
related-principles: [P4, P6]
-->

---

### P6: Task-Based Concurrency's Thread Exhaustion Trap

> *"It's really, really, really, really easy to write a program with task-based concurrency that looks like it works great until you run the system in production and you need the 513th thread."*

**The Principle**: Task-based concurrency models make it trivially easy to accidentally write blocking code that exhausts thread pools under production load, and there is no good mitigation except auditing all code.

**Why It Matters**: When the Windows Concurrency Runtime was deployed, users wrote web servers that "worked fine until their most important client hit it with meaningful load and it died." The only remedy was telling them to audit all their code for accidental blocking—an unacceptable outcome.

**When to Apply**: When evaluating task-based concurrency proposals, especially those coming from languages where this pattern is common.

**Red Flags**:
- Proposal encourages blocking on futures/tasks within async code
- No discussion of thread pool exhaustion scenarios
- "Just use monadic unwrapping" (nobody actually does this)
- Testing shows success with small loads only

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [E4]
related-principles: [P4, P5]
-->

---

### P7: Language Features Without Library Vocabulary Types Languish

> *"Coroutines, the big problem was coroutines need a library component, and nobody has agreed yet on what the library component is."*

**The Principle**: Core language features that require library vocabulary types to be useful (coroutines, modules) see limited adoption until that vocabulary is standardized; the language-only feature is insufficient.

**Why It Matters**: C++20 shipped coroutines (the language bits) but not the library types needed to use them interoperably. Result: five years later, people use coroutines internally but "not in a way that interops with anyone else."

**When to Apply**: When evaluating language proposals that assume library support will follow, or library proposals that seem to be "vocabulary types for feature X."

**Red Flags**:
- Language proposal with no concrete library design
- "Library component can be designed later"
- Existing implementations use incompatible vocabulary types
- Core feature standardized years before library support

**Supporting Experiences**: E5, E6

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/coherence
applies-to: both
confidence: high
supported-by: [E5, E6]
related-principles: [P8]
-->

---

### P8: Build System Coordination Failures Block Feature Adoption

> *"It is 2026, and we have nothing [in vcpkg] that uses C++ modules. Because to get modules to work, everybody has to agree on what the build system does and in practice nobody agrees on a build system."*

**The Principle**: Features requiring coordination between multiple independent actors (different build systems, different package managers) fail to achieve adoption even when technically complete in the standard.

**Why It Matters**: C++20 modules require build systems to communicate about textual module dependencies. Since no standard exists for this communication, modules only work within a single build system. Cross-build-system dependencies remain impossible.

**When to Apply**: When evaluating features that require tooling ecosystem coordination beyond compiler vendors.

**Red Flags**:
- Feature requires build system support with no agreed protocol
- "CMake/Meson/Bazel will figure it out"
- Only works when entire dependency graph uses same build system
- Proposal assumes tooling coordination that doesn't exist

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P7]
-->

---

### P9: Minimize Badness When Users Use It Wrong

> *"My design goal with that was always minimize badness when people use it incorrectly. Like, I don't care if HPX wins on Summit on your massive supercomputer. I care that somebody throws parallel for_each with like 5 elements that doesn't bring their program to its knees."*

**The Principle**: Standard library features should prioritize graceful behavior when misused over maximum performance in optimal conditions, because `std::` features are reached for by users who don't know what they're doing.

**Why It Matters**: Benchmark-driven optimization often makes the common case (small N, accidental misuse) much worse. For standard library features, "training wheels" matter more than winning benchmarks.

**When to Apply**: When evaluating library proposals that show impressive benchmarks, or when reviewing performance-focused design decisions.

**Red Flags**:
- Benchmarks only show large-N / optimal-use cases
- "User's fault if they call it with small N"
- Implementation degrades severely outside optimal parameters
- No discussion of what happens when users misuse the API

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E7]
related-principles: [P3]
-->

---

### P10: ODR Prevents NPM-Style Dependency Management in C++

> *"Node.js has no problem loading multiple versions of something at the same time... Whereas like the most common feature request we get on vcpkg, people want alternatives... And we have to say sorry, but we can't model that in our system because we can't build them simultaneously, like that won't link. They'll want the same symbol names."*

**The Principle**: The One Definition Rule fundamentally prevents C++ from having NPM-style dependency resolution where multiple versions of a library coexist; this is a permanent limitation of the language.

**Why It Matters**: C++ cannot adopt patterns that work in JavaScript/Python ecosystems. Proposals that assume "the package manager will handle versioning" must account for ODR constraints.

**When to Apply**: When evaluating proposals that assume ecosystem will provide alternatives/versions, or when comparing C++ to other language ecosystems.

**Red Flags**:
- Proposal assumes users can choose between alternative implementations
- "Like NPM does it" comparisons
- Multiple backends selected at build time without link compatibility
- Features that conflict at link time presented as "alternatives"

**Supporting Experiences**: E8

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: belongs/ecosystem
applies-to: library
confidence: high
supported-by: [E8]
related-principles: [P3]
-->

---

### P11: Features Are Additive, Not Alternative

> *"Turning on features is always assumed to be safe. So like B depends on A with feature one and C depends on A with feature two. We assume we can give you A with feature 1 and 2, and B and C have to be OK with that."*

**The Principle**: Package manager features must be additive (enabling more features is always safe), not alternative (mutually exclusive options). Library designs must accommodate this constraint.

**Why It Matters**: The most common request vcpkg cannot fulfill is "alternative backends" (OpenSSL vs WolfSSL). Library authors who use `#ifdef` to select one backend create unresolvable dependency graphs.

**When to Apply**: When evaluating library designs that offer configuration options, or proposals with "pluggable backends."

**Red Flags**:
- Library has mutually exclusive build-time options
- `#ifdef` selects between implementations
- "Enable OpenSSL OR WolfSSL" rather than "AND"
- Breaking build when all options enabled simultaneously

**Supporting Experiences**: E8

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E8]
related-principles: [P10]
-->

---

### P12: CMake Has Trees Documentation, Not Forest Documentation

> *"CMake has really good docs for the trees and no docs for the forest. Like what each individual CMake function call does is documented to an extreme degree. But how packages are expected to communicate with each other... there's no hello world example for that."*

**The Principle**: Technical documentation often covers individual components exhaustively while failing to explain how they compose; this gap causes practitioners to invent incompatible patterns.

**Why It Matters**: Without "hello world" examples of inter-package communication, every library author invents their own approach. The vcpkg maintainer's job is "mostly about whacking library maintainers over the head" to enforce undocumented conventions.

**When to Apply**: When evaluating standardese or design documents, especially for features that require multi-component integration.

**Red Flags**:
- Specification describes individual components without integration examples
- No "hello world" for the full workflow
- Each implementer has invented different patterns
- Reference documentation without tutorial documentation

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: wording/quality
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P8]
-->

---

### P13: Windows ABI Model Differs Fundamentally from POSIX

> *"On Windows... each DLL is an island. So like you can have one process with 5 different CRTs in it... which sucks cause we have multiple copies of things, but it's great in that you could get brand new C++20 features back on Windows XP."*

**The Principle**: Windows and POSIX platforms have fundamentally different ABI models; proposals must account for both rather than assuming one model.

**Why It Matters**: Windows applications bundle dependencies (DLL versioning), while POSIX expects system-wide shared libraries. This affects what ABI breaks are tolerable—Windows can bump DLL versions; POSIX platforms need system-wide coordination.

**When to Apply**: When evaluating proposals with ABI implications, or proposals that make assumptions about dynamic linking behavior.

**Red Flags**:
- Proposal assumes single system-wide library version
- ABI break analysis considers only one platform model
- "Just update the shared library" without considering platform differences
- Assumes applications don't bundle dependencies

**Supporting Experiences**: E9

<!-- METADATA
kind: principle
id: P13
source-type: explicit
category: philosophy/tradeoffs
applies-to: library
confidence: high
supported-by: [E9]
related-principles: [P1, P2]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: The Boyer-Moore Searcher ABI Trap

**Context**: Boyer-Moore Searcher was proposed with Marshall Clow's Boost reference implementation. Billy implemented it for MSVC STL.

**What Happened**: Billy made a mistake in detecting when the table lookup optimization could be used vs. falling back to unordered_map lookup. Boost fixed this bug about a month after MSVC shipped. But because MSVC maintains ABI stability and Boost breaks ABI every 6 months, MSVC is "stuck with that suboptimal implementation for the foreseeable future."

**The Outcome**: Failure. A straightforward algorithm implementation from the 1970s/80s, with a reference implementation, still resulted in a standard library version permanently worse than the ecosystem version.

**The Lesson**: ABI stability transforms fixable bugs into permanent limitations. Even "easy" standardization (implement known algorithm with reference impl) can create worse outcomes than leaving it to the ecosystem.

> *"Even that, that is a basic 'implement this algorithm from the 70s or maybe 80s,' and it, and the paper came with reference implementation... and my implementation that I shipped is worse than what you can get from Boost, like less than a year after shipping it."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [boyer_moore_searcher]
supports: [P1]
-->

---

### E2: Why Billy Left STL for vcpkg

**Context**: Billy was on the MSVC libraries team responsible for standard library implementation. The networking TS was under consideration for standardization.

**What Happened**: Billy assessed networking TS as "effectively unimplementable" because ASIO breaks ABI every 6 months, and networking without TLS is irresponsible to ship, but no TLS implementation can meet ABI requirements. He concluded: "I want to get you real ASIO, not out-of-date ASIO 3 months after I ship it."

**The Outcome**: Billy changed teams to work on vcpkg, reasoning that package management delivering current ecosystem libraries provides more value than standardizing a frozen, incomplete networking solution.

**The Lesson**: When ABI requirements make a feature unshippable in a useful form, the principled response is to solve the problem through the ecosystem rather than compromising the standard.

> *"The whole reason why I left the libraries team and joined vcpkg was the networking TS because I saw the networking TS as effectively unimplementable."*

**Supports Principles**: P2, P3

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/decisions
applies-to: library
outcome: mixed
features: [networking_ts, asio]
supports: [P2, P3]
-->

---

### E3: IO Concurrency vs Parallel Computation—Two Different Problems

**Context**: Billy explaining why no unified concurrency model has achieved broad adoption.

**What Happened**: He drew a clear distinction: networking TS / LibUV / IOCP solve "I have one thread and I'm waiting for IO most of the time." Parallel algorithms solve "I have a pure computational problem that lives entirely in CPU land." These have "competing goals"—one wants to not block while waiting, the other wants to saturate CPUs.

**The Outcome**: Mixed. Executors represent an attempt to bridge these, modeling CPU work as "IO if you squint," but "no attempt to mesh these together has seen broad adoption to prove that it works."

**The Lesson**: Unified concurrency abstractions sound elegant but must prove real-world viability. The domains have different enough requirements that bridging them may not be practical.

> *"I am scared to touch anything with that with standardization because no attempt to mesh these together has seen broad adoption."*

**Supports Principles**: P4, P5

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
outcome: mixed
features: [executors, parallel_algorithms, networking_ts]
supports: [P4, P5]
-->

---

### E4: The 513th Thread Problem

**Context**: Microsoft's Concurrency Runtime provided task-based concurrency with futures that supported `.then()`.

**What Happened**: Users deployed web servers that worked fine in testing. Under production load, they exhausted the 512-thread limit because they accidentally wrote blocking code—tasks that blocked waiting for other tasks in the queue. "We had no answer for them other than go audit all of the code you have ever written for blocking on the results of tasks."

**The Outcome**: Failure. Task-based concurrency made it easy to write subtly broken code that only failed under real load.

**The Lesson**: Concurrency models that make blocking easy to write accidentally will see blocking bugs escape to production. Explicit message pump models, though harder to write, fail immediately in single-threaded testing if you block incorrectly.

> *"It's really, really, really, really easy to write a program with task-based concurrency that looks like it works great until you run the system in production and you need the 513th thread."*

**Supports Principles**: P5, P6

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [concurrency_runtime, futures]
supports: [P5, P6]
-->

---

### E5: Coroutines Without Vocabulary Types

**Context**: C++20 shipped coroutines as a language feature in 2020.

**What Happened**: Six years later (2026), Billy reports coroutines are "deployed successfully in languages that are not C++" but in C++ "they just kind of haven't been adopted very much because they don't actually do anything on their own." People use them internally (like IIS HTTP stack) but "not in a way that interops with anyone else."

**The Outcome**: Partial failure. The language feature exists but ecosystem adoption is limited by lack of agreed vocabulary types.

**The Lesson**: Language features that require library vocabulary types to be useful should not be standardized without a plan for those types.

> *"Without the library vocabulary type for people to talk about what do coroutines return, they just kind of haven't been adopted very much because they don't actually do anything on their own."*

**Supports Principles**: P7

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/failures
applies-to: both
outcome: failure
features: [coroutines]
supports: [P7]
-->

---

### E6: Modules and the Build System Coordination Failure

**Context**: C++20 standardized modules. vcpkg is the largest C++ package registry.

**What Happened**: As of 2026, vcpkg has "nothing that uses C++ modules" because modules require coordination between build systems about textual module dependencies, and "in practice nobody agrees on a build system." Individual build systems (CMake, Meson, Buck2) have internal support, but cross-build-system dependencies fail because "the different build systems don't agree on how bindings to modules actually work."

**The Outcome**: Failure at ecosystem level despite technical success at language level.

**The Lesson**: Features requiring tooling coordination beyond compiler vendors face adoption barriers the standard cannot address.

> *"It is 2026, and we have nothing that uses C++ modules. Because to get modules to work, everybody has to agree on what the build system does and in practice nobody agrees on a build system."*

**Supports Principles**: P7, P8, P12

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/failures
applies-to: both
outcome: failure
features: [modules]
supports: [P7, P8, P12]
-->

---

### E7: Racing Foreground Against Background Thread Pool

**Context**: Billy designed MSVC's parallel algorithms implementation with a philosophy of "minimize badness when people use it incorrectly."

**What Happened**: Instead of optimizing for huge benchmarks, he focused on the common case of small N. The implementation races the foreground thread against the background thread pool—if the foreground wins (as it will for small N), it just cancels the background work. "The maximum possible overhead of a parallel algorithms call is just allocating the threadpool task."

**The Outcome**: Success. MSVC's implementation "beats the crap out of concurrency runtime" for realistic workloads because sorting 2000 elements with parallelism "probably loses" versus serial (if it fits in L2, parallelism loses).

**The Lesson**: Standard library features should be optimized for how users will actually use them, including misuse, not for benchmarks that show optimal conditions.

> *"No, this is std, this is a thing that people who don't know what they're doing are going to reach for. It needs to have training wheels."*

**Supports Principles**: P9

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [parallel_algorithms]
supports: [P9]
-->

---

### E8: The TLS Alternatives Problem in vcpkg

**Context**: Users frequently request that vcpkg support "alternative" TLS backends (OpenSSL vs WolfSSL).

**What Happened**: vcpkg cannot model alternatives because features must be additive—if B wants feature 1 and C wants feature 2, vcpkg gives you features 1+2. But OpenSSL and WolfSSL features are mutually exclusive in most libraries (they use `#ifdef` to pick one). The only library that works is Curl, because it does runtime TLS discovery rather than compile-time selection.

**The Outcome**: vcpkg tells users "sorry, we can't model that" and advises using overlays. The registry hardcodes a canonical choice (OpenSSL).

**The Lesson**: Library designs that offer mutually exclusive build-time options break package manager assumptions. Link-compatible additive features work; `#ifdef`-selected alternatives don't.

> *"Our acid test for them is, can I turn on both features... if we have two things that depend on a shared dependency and like this one wants feature one and this one wants feature two. We assume we can give you shared dependency with both features turned on."*

**Supports Principles**: P10, P11

<!-- METADATA
kind: experience
id: E8
source-type: explicit
category: process/actual
applies-to: library
outcome: mixed
features: [vcpkg, tls]
supports: [P10, P11]
-->

---

### E9: Why Windows ABI Breaks Are Easier

**Context**: Discussion of ABI stability requirements across platforms.

**What Happened**: Billy explained that Windows was "designed to allow ABI instability"—applications bundle dependencies, DLLs are islands, one process can have 5 different CRTs. Breaking ABI means bumping the DLL version number. MSVC broke ABI for C++17 because "all we have to do is bump the version number." But enterprise customers complained that updating compilers simultaneously is painful, so 5-10 year ABI lifespans are reasonable.

**The Outcome**: Windows platform characteristics make ABI breaks more feasible than on POSIX platforms where system-wide shared libraries are expected.

**The Lesson**: ABI stability discussions must account for platform differences. What's manageable on Windows (DLL versioning) may be catastrophic on Linux (system library updates).

> *"You could get brand new C++20 features back on Windows XP because you're not stuck with whatever Windows XP shipped with."*

**Supports Principles**: P13

<!-- METADATA
kind: experience
id: E9
source-type: explicit
category: process/actual
applies-to: library
outcome: mixed
features: [abi_stability]
supports: [P13]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] If ABI stability is required, what happens when better implementations are discovered post-standardization?
- [ ] Does the feature depend on components (TLS, crypto) that break ABI regularly?
- [ ] Is this feature better delivered through package management than standardization?
- [ ] Can the feature be implemented correctly on all target platforms?
- [ ] What happens when users call this with pathologically small/simple inputs?
- [ ] Does the design allow additive features (no mutually exclusive options)?
- [ ] Are benchmark results representative of realistic use, including misuse?

**Questions to Ask**:
1. "What does Boost/ecosystem do that this proposal cannot due to ABI constraints?"
2. "If this is the wrong design, how do we fix it after standardization?"
3. "What's the behavior when a user who doesn't know what they're doing reaches for this?"
4. "Can I enable all configuration options simultaneously and still link?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P3, P9, P11]
-->

---

### When Reviewing Concurrency/Async Proposals

- [ ] Does this solve IO-bound waiting, CPU-bound parallelism, or claim to solve both?
- [ ] Where do continuations/completions execute? Is this explicit or ambient?
- [ ] Can I test this with a single thread and detect blocking bugs immediately?
- [ ] What happens if users accidentally write blocking code?
- [ ] Is there a "513th thread" failure mode under load?
- [ ] Does this require vocabulary types that don't exist yet?

**Questions to Ask**:
1. "Is this IO concurrency or parallel computation? If both, show me real-world adoption of this unified model."
2. "Where does `.then()` / continuation run? What context?"
3. "Can I detect blocking bugs in single-threaded unit tests?"
4. "What happens when the thread pool is exhausted?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P4, P5, P6, P7]
-->

---

### When Reviewing Language Feature Proposals

- [ ] Does this feature require library vocabulary types to be useful?
- [ ] Are those vocabulary types being co-designed, or "to be done later"?
- [ ] Does this require tooling (build systems, package managers) to coordinate?
- [ ] Is there an agreed protocol for that tooling coordination, or is it assumed?
- [ ] Can this feature work across different build systems in a dependency graph?

**Questions to Ask**:
1. "What library component makes this feature usable in practice?"
2. "How do CMake, Meson, and Bazel coordinate to support this?"
3. "What happens in a project with mixed build systems in the dependency graph?"
4. "Five years after standardization, why might this not be widely adopted?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P7, P8, P12]
-->

---

## Open Questions

1. What is the specific history of `future::then()`? Billy mentions argument about "where does dot then run" but wasn't in those discussions. Who was? What were the specific technical disagreements?

2. What are the other libraries where "this strategy has failed us"—where lack of field experience led to standardizing suboptimal designs?

3. What would a unified IO/parallel concurrency model need to demonstrate to prove it's ready for standardization? What's the bar for "broad adoption"?

4. Is there a path forward for modules interoperability across build systems? What would CPS or similar need to achieve?

5. Billy mentions Gore's "negative overhead abstraction" talk about coroutines. What were the specific IIS/SQL Server results? Is there public data?

6. What is the status of `std::execution` (P2300) from Billy's perspective? Does it address the IO/parallel split?

7. How do MSVC's parallel algorithms compare to libstdc++ and libc++ implementations? Are the others also "training wheels" focused?

---

## Raw Transcript Reference

Source: `inputs/billy-o-neal-vinnie-falco.md`
