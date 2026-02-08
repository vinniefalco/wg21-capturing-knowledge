# Stephan T. Lavavej: Captured Knowledge — VC Libraries Open Code Reviews

**Source**: 19 VC Libraries Open Code Review sessions (2021-09-09 through 2023-03-16)
**Expert**: Stephan T. Lavavej (STL), MSVC STL maintainer
**Co-reviewers**: Casey Carter, Nicole Mazzuca/Minkovsky/Melnichenko, Charlie Barto
**Format**: Live public code reviews of PRs to the microsoft/STL repository
**Topics Covered**: Standard library implementation, template metaprogramming, SIMD optimization, ranges, expected, format/print, vector<bool>, ASan annotations, iterator concepts, conditional triviality, ABI stability, modules export, feature test macros, compiler bugs and workarounds

## Executive Summary

These 19 code review sessions contain an extraordinary density of institutional knowledge about maintaining a production C++ standard library implementation — knowledge directly applicable to maintaining a C++ compiler front end. STL reviews with extreme rigor: every standard paragraph citation is verified, every noexcept specification is traced through call chains, every naming convention is enforced, every feature test macro value is cross-checked against the working draft.

**For compiler front-end maintenance**, the most directly transferable knowledge includes:

1. **Template instantiation discipline** — Understanding when `decltype(auto)` vs `decltype(expr)` triggers hard errors vs SFINAE (S9P1), how `if constexpr` converts tag dispatch without changing semantics (S6P3), and why `always_false<T>` exists for delayed `static_assert` evaluation.

2. **Concept and constraint correctness** — De Morgan errors in constraint negation (S3P1), the distinction between `sized_sentinel_for` and `sized_range` (S1P7), checking both C++17 categories and C++20 concepts (S6P1), and how `requires` clauses should serve overload resolution not replace mandates (S17P6).

3. **ABI and cross-TU consistency** — Mode-dependent base classes as ODR violations (S9P2), `[[no_unique_address]]` deployment timing (S5P7), `detect_mismatch` for configuration consistency (S14P4), and C interfaces at ABI boundaries (S19P2).

4. **Compiler bug patterns** — `[[nodiscard]]` lost through C++20 operator rewriting (S11P4), Clang ignoring constraints on multiple destructors (S3P5), centralized built-in usage to work around front-end bugs (S4P3), and the TRANSITION comment convention for tracking workarounds (S4P5, S16P4).

5. **Code review as systematic verification** — Exhaustive boundary testing for bit manipulation (S18P1), escalating paranoia after finding one error (S15P1), verifying code movements by diffing (S7P1), and tracing noexcept through all call layers (S13P4).

The evaluation framework that emerges is: **correctness first (standard conformance, boundary cases, exception safety), then clarity (naming, comments, structure), then performance (only with evidence)**. Every principle below was extracted from real code review of real PRs to a shipping standard library.

1. **S1P1** Naming Must Not Shadow Standard Terminology
2. **S1P2** Comments Must Track Code Mutations
3. **S1P3** Avoid Identifier Quasi-Shadowing Across Scopes
4. **S1P4** Guard Against ADL Even When Technically Safe
5. **S1P5** Match Algorithm Semantics Precisely, Not Mechanically
6. **S1P6** Exploit the Type System for Static Optimization
7. **S1P7** Sized Sentinel vs Sized Range — Know the Difference
8. **S2P1** Convert Leaf TMP to constexpr Functions First
9. **S2P2** Incremental Changes to Widely-Used Infrastructure
10. **S2P4** constexpr Error Enforcement via Non-constexpr Function Calls
11. **S3P1** De Morgan's Law in Constraint Negation Is Non-Negotiable
12. **S3P2** Don't Implement Unaccepted Papers Preemptively
13. **S3P5** Document Compiler Bugs with Transition Comments
14. **S4P1** Use Byte/Element Distinction Religiously in Naming
15. **S4P2** Magic Numbers at Algorithm Boundaries Demand Targeted Tests
16. **S4P3** Centralize Built-in Usage to Avoid Compiler Bugs
17. **S4P5** Comment TRANSITION Workarounds with PR/Version
18. **S5P1** Ranges Algorithms Must Be Niebloids, Not Functions
19. **S5P5** Defend Against Overloaded Operator Comma in STL Algorithms
20. **S6P1** C++20 Iterator Concepts May Be Stronger Than C++17 Categories — Check Both
21. **S6P3** Tag Dispatch to if-constexpr: Test Most Specific First
22. **S7P1** Verify Code Movements by Diffing Old and New Locations
23. **S8P1** Assertion Messages Must Match the Function They're In
24. **S9P1** Use decltype(expr) Return Types for SFINAE, Not decltype(auto)
25. **S9P2** ABI Mix-and-Match Is the Highest Concern for Mode-Dependent Base Classes
26. **S10P3** Guard O(N) Precondition Checks With Constant-Time Feasibility
27. **S11P4** [[nodiscard]] Warnings Are Lost Through C++20 Operator Rewriting
28. **S12P1** Functional-Style Casts in Generic Code Are Dangerous C-Style Casts
29. **S13P1** Header Inclusion Throughput Discipline
30. **S13P2** Feature Test Macros Only for Complete, Usable Features
31. **S13P4** Strengthen Noexcept Specifications Consistently Through All Layers
32. **S13P7** Don't Const Local Variables Returned by Value
33. **S14P1** New Headers Must Follow the Full Incantation Checklist
34. **S14P4** Use detect_mismatch for Cross-TU Consistency
35. **S15P1** When You Find One Typo, Increase Paranoia
36. **S15P2** Iterator Rewrapping Must Preserve Parent Provenance
37. **S15P6** Same Names for Same Things, Different Names for Different Things
38. **S16P4** Report Compiler Bugs and Mark Workarounds as Transitions
39. **S17P4** Fix Obviously Bogus Standard Wording and File DR Simultaneously
40. **S17P6** Constraints Should Serve Overload Resolution, Not Replace Mandates
41. **S17P7** Prefer Direct Standard Translation Over Clever Extraction
42. **S18P1** Exhaustively Test All Boundary Combinations for Bit Manipulation
43. **S18P3** Runtime Optimizations Carry High Regression Risk
44. **S19P1** Import Lib Code Must Not Depend on Non-Core Headers
45. **S19P2** Use C Interfaces at ABI Boundaries
46. **S19P3** Prefer Simpler Implementation Now, Optimize Later With Evidence

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

---

### S1P1: Naming Must Not Shadow Standard Terminology

> *"When something says `_Trivially_constructible` and it's doing something different, then it's an opportunity to get confused... the only thing that makes this whole metaprogramming thing bearable is that our names are generally pretty precise."*

**The Principle**: Internal type trait names must not mirror standard trait names when they have additional or different semantics.

**Why It Matters**: In deeply layered template metaprogramming, developers rely on names to avoid re-reading definitions. If `_Trivially_constructible` adds `_Same_size_and_compatible` beyond what `is_trivially_constructible_v` tests, someone will eventually use the standard trait where they needed the internal one, or vice versa.

**When to Apply**: Any time you introduce an internal type trait, concept, or constexpr predicate that overlaps with — but is not identical to — a standard library trait.

**Red Flags**:
- Internal trait name is a subset/superset of a `std::is_*` name
- No comment documenting the delta from the standard trait
- Usage sites that could plausibly confuse the two

**Supporting Experiences**: S1E1

<!-- METADATA
kind: principle
id: S1P1
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S1E1]
related-principles: [S15P6]
-->

---

### S1P2: Comments Must Track Code Mutations

> *"One of the things I look for when code is significantly changing is that if there are any comments around, it is quite possible to change the code such that the comments become inaccurate."*

**The Principle**: When refactoring moves a check to a different layer, update all comments that described or depended on the original location of that check.

**Why It Matters**: Stale comments about preconditions become actively misleading when the enforcement moves elsewhere. In template metaprogramming there is no debugger — comments are the only documentation of layer contracts.

**When to Apply**: Every PR that moves, removes, or reorders checks across abstraction layers.

**Red Flags**:
- Comment says "X is guaranteed" but the guarantee was moved
- Precondition comments that reference checks no longer in the same function

<!-- METADATA
kind: principle
id: S1P2
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: []
related-principles: []
-->

---

### S1P3: Avoid Identifier Quasi-Shadowing Across Scopes

> *"I'm really uncomfortable whenever I see the same name reused in the STL, even if there's no actual shadowing. I would prefer any other name."*

**The Principle**: When a template parameter and a nested type share the same identifier, rename one to eliminate confusion — even when C++ scoping rules disambiguate.

**Why It Matters**: Human readers scanning dense metaprogramming will misread `_Lex_compare_memcmp_classify<MEOW, _Pred>::_Pred` as recursive or self-referential.

**When to Apply**: Any template that has both a parameter name and a nested name that collide.

**Red Flags**:
- `typename Foo<..., _X>::_X` patterns
- Same identifier used in both template parameter list and body/nested type

**Supporting Experiences**: S16E1

<!-- METADATA
kind: principle
id: S1P3
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S16E1]
related-principles: [S16P1]
-->

---

### S1P4: Guard Against ADL Even When Technically Safe

> *"That's influenced by how much I hate and fear ADL... When I see the qualification, I'm like, oh, no ADL, this is fun and happy."*

**The Principle**: Qualify calls to standard library entities with `_STD` (or `std::`) even when they are technically immune to ADL.

**Why It Matters**: Consistency prevents accidental ADL in future refactors. When a reader sees an unqualified call in STL internals, they must stop and verify whether ADL could hijack it.

**When to Apply**: All internal calls to standard function objects, CPOs, or anything that looks like a function call in library implementation code.

**Red Flags**:
- Unqualified calls to `strong_order`, `weak_order`, etc.
- Inconsistency between files

**Supporting Experiences**: S5E1

<!-- METADATA
kind: principle
id: S1P4
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S5E1]
related-principles: [S5P5, S18P5]
-->

---

### S1P5: Match Algorithm Semantics Precisely, Not Mechanically

> *"For the classic impl, this is critical, as the metaprogrammed machinery is capable of reversing the ordering, which we don't want to do for the lengths of equal prefix sequences."*

**The Principle**: When implementing a standard algorithm optimization, verify that every sub-expression matches the semantic intent of the standard, not just the mechanical pattern of nearby code.

**Why It Matters**: Pattern consistency across similar algorithms can mask semantic divergence. Always re-derive from the standard for each algorithm independently.

**When to Apply**: Any time an optimization wraps a standard algorithm with metaprogrammed dispatch.

**Red Flags**:
- Optimization path uses the user predicate in a context the standard doesn't
- Pattern from one algorithm copy-pasted to a related but subtly different algorithm

<!-- METADATA
kind: principle
id: S1P5
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S1E1]
related-principles: []
-->

---

### S1P6: Exploit the Type System for Static Optimization

> *"We can do this thanks to `nullptr_t` being in the type system. When things are in the type system, that's good. When things like 0 is a null pointer constant are rules that exist outside the type system, that leads to misery."*

**The Principle**: Prefer optimizations keyed off types over optimizations that inspect values at runtime, because type-based dispatch is resolved at compile time with zero runtime cost.

**Why It Matters**: The `_Is_all_bits_zero` optimization for `nullptr_t` avoids runtime `memcmp` entirely via `if constexpr`. Any type whose representation is statically known can skip runtime analysis.

**When to Apply**: Fill, comparison, and copy optimizations where a type's bit representation is compile-time deterministic.

**Red Flags**:
- Runtime `memcmp` against a `constexpr`-constructible value when a type check would suffice
- Missing `if constexpr` branches for types with statically-known representations

<!-- METADATA
kind: principle
id: S1P6
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: []
related-principles: []
-->

---

### S1P7: Sized Sentinel vs Sized Range — Know the Difference

> *"Sized_sentinel_for means that the iterator and sentinel can tell you the distance between them. List is an example of a range that's a sized range. It knows its own size, but the iterators and sentinels don't know the distance between them."* — Casey

**The Principle**: Distinguish `sized_sentinel_for` (iterator+sentinel can compute distance) from `sized_range` (range knows its size) and use the correct concept.

**Why It Matters**: Using the wrong concept leads to overly restrictive constraints or unsound assumptions about O(1) distance computation.

**When to Apply**: Any algorithm optimization that needs to know the size of a range or distance between iterators.

**Red Flags**:
- Using `sized_range` when you only have an iterator and sentinel
- Using `sized_sentinel_for` when you need the range's own size

<!-- METADATA
kind: principle
id: S1P7
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: []
related-principles: [S10P3]
-->

---

### S2P1: Convert Leaf TMP to constexpr Functions First

> *"I think that doing sort of a limited conversion of ABS, sign_of, and GCD is a good start and then later we could continue converting. It's sort of doing it from the leaf nodes up."*

**The Principle**: When modernizing template metaprogramming to `constexpr` functions, start with leaf computations that have no error-handling or SFINAE concerns.

**Why It Matters**: Leaf functions like `abs`, `sign_of`, `gcd` are pure computations. Converting error-handling layers requires different techniques (e.g., calling a non-`constexpr` function for compile-time errors).

**When to Apply**: Any modernization effort converting struct-based TMP to `constexpr` functions.

**Red Flags**:
- Trying to convert error-handling and pure-computation TMP in the same PR
- Converting a middle layer before its leaf dependencies

<!-- METADATA
kind: principle
id: S2P1
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S2E1]
related-principles: [S2P4]
-->

---

### S2P2: Incremental Changes to Widely-Used Infrastructure

> *"This is changing code that is used by ratio and Chrono. I'm a little more hesitant to just go wild and change a whole bunch of stuff."*

**The Principle**: When modifying code that is unconditionally included across many features, prefer small, self-contained PRs over sweeping refactors.

**Why It Matters**: `ratio` is used by `chrono`, which is used everywhere. A bug propagates widely. Small PRs are easier to review, bisect, and don't block other work.

**When to Apply**: Any change to foundational headers like `<ratio>`, `<type_traits>`, `<utility>`, `<xutility>`.

**Red Flags**:
- PR touches both pure-computation and error-handling layers
- PR changes behavior in C++14 mode without targeted test coverage

<!-- METADATA
kind: principle
id: S2P2
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S2E1]
related-principles: []
-->

---

### S2P4: constexpr Error Enforcement via Non-constexpr Function Calls

> *"I believe that the overflow enforcement would be best expressed with 'if would overflow, call a non-constexpr function,' which is a technique that we've used elsewhere."*

**The Principle**: To trigger a compile-time error from within a `constexpr` function, call a non-`constexpr` function. The compiler will reject the call during constant evaluation, and the function name serves as the error message.

**Why It Matters**: `static_assert(false)` in a template is evaluated eagerly. `static_assert(always_false<T>)` requires a template parameter. The non-`constexpr` call technique works in plain `constexpr` functions.

**When to Apply**: Converting `static_assert`-based error handling from TMP structs to `constexpr` functions.

**Red Flags**:
- `static_assert(false)` in a constexpr function
- Missing error enforcement after TMP-to-constexpr conversion

<!-- METADATA
kind: principle
id: S2P4
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S2E1]
related-principles: [S2P1]
-->

---

### S3P1: De Morgan's Law in Constraint Negation Is Non-Negotiable

> *"The requirements on the non-trivial copy constructor are incorrect because what it says is not trivially copy constructible T and not trivially copy constructible E. And what we want is... either."* — Casey/Nicole

**The Principle**: When negating a conjunction of constraints for the "else" overload (the non-trivial path), apply De Morgan's law correctly: `!(A && B)` becomes `(!A || !B)`, not `(!A && !B)`.

**Why It Matters**: The incorrect `(!A && !B)` leaves a gap: types where exactly one of T or E is trivially copy constructible match neither the trivial overload nor the non-trivial overload.

**When to Apply**: Every conditionally-trivial special member function pattern in any wrapper type (expected, optional, variant, pair, tuple).

**Red Flags**:
- Non-trivial overload constrained with `!A && !B` instead of `!A || !B`
- Copy-pasted constraints from the trivial overload with naive negation
- Missing test for the case where exactly one inner type is trivial

**Supporting Experiences**: S3E1

<!-- METADATA
kind: principle
id: S3P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S3E1]
related-principles: []
-->

---

### S3P2: Don't Implement Unaccepted Papers Preemptively

> *"So many times in the past, we have tried to implement things in advance of them being voted into the working paper, and if they get changed, or in the worst case rejected... we've just shipped something nonstandard."*

**The Principle**: Only implement features that are in the C++ working paper. Separate "likely future" features into their own PRs gated on actual acceptance.

**Why It Matters**: The STL was burned by `std::future`'s blocking destructor — implemented in anticipation of a paper never accepted.

**When to Apply**: Any request to implement a paper not yet voted into the working draft.

**Red Flags**:
- PR bundles a voted-in feature with an "anticipated" feature
- Feature depends on a paper still in LEWG review

<!-- METADATA
kind: principle
id: S3P2
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [S3E2]
related-principles: []
-->

---

### S3P5: Document Compiler Bugs with Transition Comments

> *"The destructor order is significant... we should have the same comment here as this code pattern is equally affected."*

**The Principle**: When code structure is dictated by a compiler bug, add a `// TRANSITION, <version>` comment naming the bug and a searchable marker so the workaround can be removed.

**Why It Matters**: Without the comment, future maintainers will reorder the code and reintroduce the bug. Without the transition marker, workarounds accumulate indefinitely.

**When to Apply**: Any code whose structure is dictated by a compiler bug rather than logical necessity.

**Red Flags**:
- Constrained special member functions in a specific order without explanation
- Workaround code without transition marker or bug reference
- Decade-old workarounds nobody remembers the reason for

<!-- METADATA
kind: principle
id: S3P5
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: []
related-principles: [S4P5, S16P4]
-->

---

### S4P1: Use Byte/Element Distinction Religiously in Naming

> *"There's a very strong assumption in the STL that when we see size, we're counting elements. If anybody's talking about bytes, they really need to say bytes up front."*

**The Principle**: Names involving counts must unambiguously indicate whether they measure bytes or elements.

**Why It Matters**: The Mars Climate Orbiter crashed because of a units mismatch; the same principle applies to naming in low-level code. Confusing bytes and elements in vectorized code causes buffer overruns.

**When to Apply**: Any code that converts between byte offsets and element indices.

**Red Flags**:
- `portion_size` could mean bytes or elements
- No comment explaining the unit of a numeric constant

**Supporting Experiences**: S4E2

<!-- METADATA
kind: principle
id: S4P1
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S4E2]
related-principles: [S7P4]
-->

---

### S4P2: Magic Numbers at Algorithm Boundaries Demand Targeted Tests

> *"Whenever we see a constant in the code, we need to test on the side... We were bit by this before."*

**The Principle**: Every magic number that creates a control-flow boundary must have test cases that exercise both sides and the exact boundary value.

**Why It Matters**: Randomized testing with small inputs often fails to hit the exact transitions where bugs lurk.

**When to Apply**: Any algorithm with hard-coded thresholds that trigger different code paths.

**Red Flags**:
- Only random testing, no boundary-value testing
- Test inputs are all smaller than internal constants

**Supporting Experiences**: S4E1

<!-- METADATA
kind: principle
id: S4P2
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S4E1]
related-principles: [S18P1]
-->

---

### S4P3: Centralize Built-in Usage to Avoid Compiler Bugs

> *"We have traditionally centralized our usage of builtins and intrinsics into helper functions... Those built-ins appearing at different strange places... the compiler was not always prepared to handle."*

**The Principle**: Wrap compiler built-ins in a single helper rather than scattering raw built-in calls throughout the codebase.

**Why It Matters**: Compiler built-ins are special-cased by the front end and historically had bugs in unexpected contexts. Centralizing means only one call site needs to be correct.

**When to Apply**: All uses of compiler intrinsics and built-ins in standard library or compiler-adjacent code.

**Red Flags**:
- Raw `__builtin_*` calls scattered throughout headers
- Built-in used in a novel context without checking for compiler bugs
- Different files using different wrappers for the same built-in

<!-- METADATA
kind: principle
id: S4P3
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: []
related-principles: [S3P5]
-->

---

### S4P5: Comment TRANSITION Workarounds with PR/Version

> *"Recommend... make the comment just say '17.3 Preview 2.' That's all we need in the source code."*

**The Principle**: Compiler bug workarounds should have a `// TRANSITION, <version>` comment with the VS version and a reference to the fixing PR. This enables automated cleanup.

**Why It Matters**: The MSVC STL has a `grep`-able convention that marks every workaround. When a new toolset ships, maintainers search for removable transitions.

**When to Apply**: Every compiler workaround, every deviation from the standard caused by a compiler limitation.

**Red Flags**:
- Workaround code with no transition marker
- Workarounds older than two VS release cycles

<!-- METADATA
kind: principle
id: S4P5
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: []
related-principles: [S3P5, S16P4]
-->

---

### S5P1: Ranges Algorithms Must Be Niebloids, Not Functions

> *"ranges algorithms are not functions or function templates. But are currently implemented as niebloids — those are objects with the call operator."*

**The Principle**: All ranges algorithms must be implemented as function objects (niebloids) deriving from `_Not_quite_object` to inhibit ADL.

**Why It Matters**: Without ADL inhibition, unqualified calls with two iterators would find `std::` algorithm overloads.

**When to Apply**: Any time a new ranges algorithm is added.

**Red Flags**:
- Ranges algorithm implemented as a plain function template
- Missing `_Not_quite_object` derivation

**Supporting Experiences**: S5E1

<!-- METADATA
kind: principle
id: S5P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S5E1]
related-principles: [S1P4]
-->

---

### S5P5: Defend Against Overloaded Operator Comma in STL Algorithms

> *"as always in the STL, we have to defend against hijacking of operators that we use by strange ADL overloads"* — Casey

**The Principle**: Cast subexpressions to `void` to prevent user-defined `operator,` from being found by ADL in comma-separated expressions.

**Why It Matters**: Users can define `operator,` that ADL could find. The algorithm specification doesn't permit calling user-defined comma operators.

**When to Apply**: Every `for` loop increment expression in an algorithm implementation where both operands involve user types. Pattern: `(void)++_First, (void)++_Val`.

**Red Flags**:
- Missing `(void)` casts around comma-separated increment expressions

<!-- METADATA
kind: principle
id: S5P5
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: []
related-principles: [S1P4]
-->

---

### S6P1: C++20 Iterator Concepts May Be Stronger Than C++17 Categories — Check Both

> *"There are iterators that meet the forward iterator concept that do not that aren't marked with the forward iterator category."*

**The Principle**: When dispatching on iterator strength, check both the C++17 category tag AND the C++20 concept. An iterator may satisfy `forward_iterator` without being tagged as one.

**Why It Matters**: C++20 ranges views produce iterators that satisfy concepts but report weaker categories. This caused vector to fall back to the inefficient input-iterator code path.

**When to Apply**: Any container code that dispatches on iterator strength.

**Red Flags**:
- Only checking `_Is_fwd_iter_v` without also checking `forward_iterator<Iter>`
- Removing the old code path instead of adding the new one alongside

**Supporting Experiences**: S6E1

<!-- METADATA
kind: principle
id: S6P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S6E1]
related-principles: [S6P3]
-->

---

### S6P3: Tag Dispatch to if-constexpr: Test Most Specific First

> *"we have always been very careful when transforming old tag dispatch to new if constexpr... to test things in the correct order."*

**The Principle**: When converting tag dispatch to `if constexpr`, always test conditions from most specific to most general. Tag dispatch selects "best match" automatically; `if constexpr` selects first-true.

**Why It Matters**: Reversing the test order causes random-access iterators to be handled by the bidirectional branch.

**When to Apply**: Any modernization of tag-dispatch to `if constexpr`, especially iterator strength hierarchies.

**Red Flags**:
- `if constexpr (forward)` tested before `if constexpr (random_access)`
- Missing the hierarchy: contiguous > random_access > bidirectional > forward > input

**Supporting Experiences**: S6E3

<!-- METADATA
kind: principle
id: S6P3
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S6E3]
related-principles: [S6P1]
-->

---

### S7P1: Verify Code Movements by Diffing Old and New Locations

> *"I love to double check code movements because that is a wonderful time for things like merge conflicts and other bugs to be introduced."*

**The Principle**: When code is moved between files, copy both versions into an editor and diff them character-by-character. Code movement is a prime vector for accidental modifications.

**Why It Matters**: Merge conflicts during code movement silently introduce bugs. GitHub's diff doesn't show that removed code equals added code.

**When to Apply**: Any PR that moves functions between headers.

**Red Flags**:
- Code "moved" that has subtle logic differences
- Large code movements without explicit reviewer verification

**Supporting Experiences**: S7E1

<!-- METADATA
kind: principle
id: S7P1
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S7E1]
related-principles: []
-->

---

### S8P1: Assertion Messages Must Match the Function They're In

> *"This function is insert after. But the STL verify message says erase after."*

**The Principle**: Every `_STL_VERIFY` message must be audited to ensure it names the correct function. Assertion messages are the most common source of copy-paste errors.

**Why It Matters**: Incorrect diagnostic messages waste debugging time.

**When to Apply**: Every PR that adds or modifies functions containing assertion messages.

**Red Flags**:
- Assertion message mentioning a different function name
- Same error message across unrelated functions

**Supporting Experiences**: S8E1

<!-- METADATA
kind: principle
id: S8P1
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S8E1]
related-principles: [S15P1]
-->

---

### S9P1: Use decltype(expr) Return Types for SFINAE, Not decltype(auto)

> *"If you say decltype auto that will need to instantiate the body of the function. If you say decltype of spam out the expression again, you get SFINAE."*

**The Principle**: Use explicit `decltype(expr)` return types instead of `decltype(auto)` when the function must participate in SFINAE / overload resolution.

**Why It Matters**: `decltype(auto)` requires instantiating the function body, producing a hard error if instantiation fails. `decltype(expression)` triggers substitution failure (soft error).

**When to Apply**: Any function template whose compilability must be detectable by SFINAE, concepts, or type traits — especially `operator()` in callable wrappers.

**Red Flags**:
- A callable wrapper using `decltype(auto)` return type
- `is_invocable` returning incorrect results
- Hard errors during overload resolution instead of graceful removal

<!-- METADATA
kind: principle
id: S9P1
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: [S9E1]
related-principles: [S3P3]
-->

---

### S9P2: ABI Mix-and-Match Is the Highest Concern for Mode-Dependent Base Classes

> *"anytime you have a base class whose pruning changes, that is an ODR violation. We certainly do a lot of that... how to violate the ODR properly is one of the hardest parts of our job."*

**The Principle**: Never change the base class layout or identity of a type based on standard mode when that type already exists in an earlier mode.

**Why It Matters**: Different TUs compiled with different standard modes can be linked together. Changed base classes create ODR violations.

**When to Apply**: Any time a library introduces types that reuse or replace existing internal machinery across standard modes.

**Red Flags**:
- Conditional inheritance that changes based on `__cplusplus`
- "It works in my mode" testing without cross-mode linking tests

<!-- METADATA
kind: principle
id: S9P2
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [S9E2]
related-principles: [S5P7, S14P4]
-->

---

### S10P3: Guard O(N) Precondition Checks With Constant-Time Feasibility

> *"computing the distance from current to the sentinel end might not be an order one operation... because this is just a precondition check, we should guard this with sized_sentinel_for."*

**The Principle**: Debug checks that compute distances must be guarded by `sized_sentinel_for` — never sneak O(N) work into a debug check.

**Why It Matters**: A random access iterator can have a non-sized sentinel. An O(N) strlen-like operation hidden in a debug check would destroy performance.

**When to Apply**: Any iterator debug check that computes distance or range size.

**Red Flags**:
- `ranges::distance(current, end)` in a debug check without `sized_sentinel_for` guard
- Precondition checks more expensive than the operation they guard

**Supporting Experiences**: S10E1

<!-- METADATA
kind: principle
id: S10P3
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S10E1]
related-principles: [S1P7]
-->

---

### S11P4: [[nodiscard]] Warnings Are Lost Through C++20 Operator Rewriting

> *"When the compiler does that rewriting, it is not carrying along the [[nodiscard]]."*

**The Principle**: In C++20, when `!=` is rewritten to `!(==)`, the `[[nodiscard]]` attribute on the underlying operator may not propagate. This is a compiler bug (confirmed in MSVC and GCC, not Clang).

**Why It Matters**: The most important use case for `[[nodiscard]]` — catching the comma-vs-&& bug on iterator comparisons — was silently broken in C++20 mode.

**When to Apply**: Testing `[[nodiscard]]` behavior across standard modes; debugging missing warnings.

**Red Flags**:
- `[[nodiscard]]` on `operator==` not triggering warnings when user writes `!=`
- C++20 operator rewriting silently consuming attributes

**Supporting Experiences**: S11E1

<!-- METADATA
kind: principle
id: S11P4
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: [S11E1]
related-principles: []
-->

---

### S12P1: Functional-Style Casts in Generic Code Are Dangerous C-Style Casts

> *"A functional style cast... is equivalent to the corresponding cast expression. Which is a C cast... it tries const_cast, followed by static_cast, followed by reinterpret_cast."*

**The Principle**: Never use functional-style casts (`Type(expr)`) in generic code where types are user-specifiable. Use `static_cast<Type>(expr)` explicitly.

**Why It Matters**: `U(std::move(init))` is syntactic sugar for a C-style cast. With user-controlled types, this can silently perform `const_cast` or `reinterpret_cast`.

**When to Apply**: Any standard library implementation where the return type is computed from user-provided types.

**Red Flags**:
- `U(std::move(init))` in generic code
- Standard wording that says "direct-non-list-initialized" mapping to functional-style casts

**Supporting Experiences**: S12E1

<!-- METADATA
kind: principle
id: S12P1
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S12E1]
related-principles: [S17P1]
-->

---

### S13P1: Header Inclusion Throughput Discipline

> *"Dragging in algorithm is not awesome for throughput."*

**The Principle**: When a large header is included solely for a tiny piece of functionality, investigate promoting that piece to a lighter-weight internal header.

**Why It Matters**: `<algorithm>` is ~200+ KB. `<ranges>` already has poor throughput, so adding `<algorithm>` on top compounds the problem.

**When to Apply**: Any time a new feature header includes a heavy header for only a few utilities.

**Red Flags**:
- Including `<algorithm>` for `std::min`/`std::max` only
- Not checking whether the needed utility lives in a lighter internal header

**Supporting Experiences**: S13E1

<!-- METADATA
kind: principle
id: S13P1
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S13E1]
related-principles: [S19P1]
-->

---

### S13P2: Feature Test Macros Only for Complete, Usable Features

> *"Our policy is that we only define a feature test macro when a feature is complete and non-buggy enough to actually be usable."*

**The Principle**: Never define a feature test macro for a partially implemented feature. The macro is a promise to users.

**Why It Matters**: Users rely on feature test macros to conditionally compile code. A macro that lies about completeness causes silent breakage.

**When to Apply**: When implementing a paper spanning multiple PRs, or when compiler bugs block full functionality.

**Red Flags**:
- Macro defined in a PR that says "partial implementation"
- Macro defined when known compiler bugs prevent use

**Supporting Experiences**: S13E2

<!-- METADATA
kind: principle
id: S13P2
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S13E2]
related-principles: [S10P4]
-->

---

### S13P4: Strengthen Noexcept Specifications Consistently Through All Layers

> *"operator- is strengthened to be noexcept... but _Zip_get_smallest_distance is never marked. So this is identical to noexcept(false)."*

**The Principle**: When strengthening a public function's noexcept, all internal helpers it calls must also be strengthened; otherwise the public strengthening evaluates to `noexcept(false)`.

**Why It Matters**: A noexcept specification referencing a non-noexcept helper silently becomes `noexcept(false)`. The code compiles, tests pass, but the specification is dead code.

**When to Apply**: Reviewing any noexcept strengthening. Trace the call chain through all helpers.

**Red Flags**:
- `noexcept(noexcept(helper()))` where `helper` has no noexcept
- Strengthened public functions calling unstrengthened private helpers

**Supporting Experiences**: S13E3

<!-- METADATA
kind: principle
id: S13P4
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [S13E3]
related-principles: [S13P5, S16P5]
-->

---

### S13P7: Don't Const Local Variables Returned by Value

> *"Although const is one of our favorite keywords... this is a rare exception — when returning a local variable. This can inhibit automatic moving."*

**The Principle**: Never apply `const` to local variables that will be returned by value, because `const` inhibits implicit move on return when NRVO doesn't activate.

**Why It Matters**: A `const` local cannot be moved from — it will be copied instead. If NRVO doesn't activate (e.g., because of branching), you pay a full copy.

**When to Apply**: Post-increment patterns, or any function that stores a result in a local and returns it.

**Red Flags**:
- `const auto temp = *this;` followed by `return temp;`
- Local variables declared const that are subsequently returned

<!-- METADATA
kind: principle
id: S13P7
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S13E4]
related-principles: [S5P3]
-->

---

### S14P1: New Headers Must Follow the Full Incantation Checklist

> *"When adding a new header, I like to look at an existing header for precedent, because here we don't exactly have a checklist, but there is a certain dance."*

**The Principle**: Every new header must include the full set of preprocessor defenses: include guard, `#pragma once`, `_STL_COMPILER_PREPROCESSOR` defense, packing/warning push-pop, and the `new` macroization defense.

**Why It Matters**: Headers grow over time. A header that starts as "just macros" will eventually gain declarations. Defenses prevent future problems.

**When to Apply**: Every time a new header file is created.

**Red Flags**:
- New header with only `#pragma once`
- Author says "it's just macros, we don't need defenses"

**Supporting Experiences**: S14E1

<!-- METADATA
kind: principle
id: S14P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S14E1]
related-principles: [S14P2]
-->

---

### S14P4: Use detect_mismatch for Cross-TU Consistency

> *"This is a sort of generic way, extensible way for us to ensure that inconsistent things are not linked into a single binary."*

**The Principle**: Use `#pragma detect_mismatch` to enforce that all TUs linked into a single binary agree on critical configuration settings.

**Why It Matters**: Mixing TUs with different annotation or debug settings causes silent corruption. `detect_mismatch` catches this at link time.

**When to Apply**: Any library compile-time configuration option that must be consistent across all TUs.

**Red Flags**:
- Configuration-dependent behavior without detect_mismatch
- Relying on runtime checks instead of link-time checks

**Supporting Experiences**: S14E3

<!-- METADATA
kind: principle
id: S14P4
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S14E3]
related-principles: [S9P2]
-->

---

### S15P1: When You Find One Typo, Increase Paranoia

> *"The guiding principle here... when I find something like a typo, my level of caution immediately goes up a notch. I start looking for — are there other typos or copy paste errors?"*

**The Principle**: Finding one error in repetitive code should immediately escalate review thoroughness. Where there's one, there's usually more.

**Why It Matters**: A single found error is evidence of a systemic copy-paste process failure.

**When to Apply**: Any time you find a typo, wrong value, or copy-paste remnant during review.

**Red Flags**:
- Feature test macro value that doesn't match other occurrences
- One of N similar overloads missing `[[nodiscard]]`

**Supporting Experiences**: S15E1

<!-- METADATA
kind: principle
id: S15P1
source-type: tacit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S15E1]
related-principles: [S8P1]
-->

---

### S15P2: Iterator Rewrapping Must Preserve Parent Provenance

> *"Nicole noticed a major problem — the parameter first is a wrapped iterator with a parent. But the freshly value-initialized last has no parent."*

**The Principle**: When returning iterators from a ranges algorithm, never value-initialize an iterator and seek it to an unwrapped position — it will lack parent provenance. Use `_Rewrap_subrange`.

**Why It Matters**: A value-initialized iterator has no parent. Comparing parentless with parented iterators violates iterator requirements.

**When to Apply**: Every ranges algorithm that returns iterators.

**Red Flags**:
- `_It last{};` followed by `_Seek_wrapped(last, ...)`
- Not using `_Rewrap_subrange`

**Supporting Experiences**: S15E2

<!-- METADATA
kind: principle
id: S15P2
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [S15E2]
related-principles: [S15P3]
-->

---

### S15P6: Same Names for Same Things, Different Names for Different Things

> *"In templated code, we kind of have no type system."*

**The Principle**: In heavily templated code, template parameter names are the closest thing to a type system. If a parameter represents an unwrapped iterator, name it `_UIt`; if wrapped, name it `_It`.

**Why It Matters**: Without concepts doing full definition checking, template parameter names are the primary guard against passing the wrong kind of type.

**When to Apply**: Helper functions in a chain where types transform (unwrapping, adding constness, etc.).

**Red Flags**:
- Public and private helpers both use `_It` for semantically different iterators
- Type transformations that don't change the parameter name

**Supporting Experiences**: S15E2

<!-- METADATA
kind: principle
id: S15P6
source-type: tacit
category: philosophy/library
applies-to: both
confidence: medium
supported-by: [S15E2]
related-principles: [S1P1, S1P3]
-->

---

### S16P4: Report Compiler Bugs and Mark Workarounds as Transitions

> *"This should be reported as an MSVC bug. And then this code should be marked as transition citing the bug number. We conventionally avoid literally saying 'bug' in the product code."*

**The Principle**: When a compiler bug forces a workaround: (1) file a bug report, (2) mark with `// TRANSITION` citing the bug number, (3) don't literally write "bug", (4) don't guard with `#ifdef` if the workaround is harmless.

**Why It Matters**: Without a filed bug and TRANSITION comment, workarounds become permanent.

**When to Apply**: Any compiler limitation that forces non-obvious code in the library.

**Red Flags**:
- Comments saying "this is a compiler bug" without a filed issue
- Complex `#ifdef` guards around harmless workarounds

<!-- METADATA
kind: principle
id: S16P4
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S16E3]
related-principles: [S3P5, S4P5]
-->

---

### S17P4: Fix Obviously Bogus Standard Wording and File DR Simultaneously

> *"This is a case where the standard is clearly bogus, and the right thing to do is obvious."*

**The Principle**: When standard wording is clearly incorrect and the fix is obvious, implement the correct behavior immediately and file an LWG defect report simultaneously.

**Why It Matters**: Waiting for DR resolution can take years. A working implementation with tests serves as evidence for the resolution.

**When to Apply**: When standard wording is unambiguously wrong and no reasonable design alternative exists.

**Red Flags**:
- Implementing clearly wrong behavior "because the standard says so"
- Fixing without filing a DR

**Supporting Experiences**: S17E2

<!-- METADATA
kind: principle
id: S17P4
source-type: explicit
category: wording/pitfalls
applies-to: library
confidence: high
supported-by: [S17E2]
related-principles: [S12P3]
-->

---

### S17P6: Constraints Should Serve Overload Resolution, Not Replace Mandates

> *"Frankly, I don't even think this needs to be a constraint at all... what are you doing that you need that SFINAE constraint?"*

**The Principle**: Use `requires` clauses only when they genuinely improve overload resolution. If no realistic overload set benefits, use `static_assert` — it produces better diagnostics.

**Why It Matters**: Over-constraining adds complexity for no benefit. The whole point of constraints is to participate in overload resolution.

**When to Apply**: Evaluating whether a `requires` clause is actually necessary.

**Red Flags**:
- `requires` clauses on member functions where SFINAE is meaningless
- Standard wording using "Constraints:" where "Mandates:" would be more appropriate

**Supporting Experiences**: S17E2

<!-- METADATA
kind: principle
id: S17P6
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [S17E2]
related-principles: [S17P5]
-->

---

### S17P7: Prefer Direct Standard Translation Over Clever Extraction

> *"I'd rather have basically more code that more directly aligns with the standard, and I have to think less whenever I see something that needs a big transformation."*

**The Principle**: Standard library implementations should directly mirror standardese structure, even if this means repetition. Extracting common code into helpers makes conformance verification harder.

**Why It Matters**: The primary correctness criterion is conformance. If each function body maps directly to its specification paragraph, verification is straightforward.

**When to Apply**: Implementing standard library functions with multiple similar-but-not-identical overloads.

**Red Flags**:
- Helper functions that don't map to any standard paragraph
- "Clever" implementations where cleverness obscures standard conformance

**Supporting Experiences**: S17E1, S17E3

<!-- METADATA
kind: principle
id: S17P7
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S17E1, S17E3]
related-principles: [S17P2]
-->

---

### S18P1: Exhaustively Test All Boundary Combinations for Bit Manipulation

> *"When I see that many special cases, then I sort of want to see really exhaustive testing... 32 offsets times 32 offsets times 32 possible lengths, that's only 32Ki test cases."*

**The Principle**: Bit manipulation algorithms must be tested exhaustively across all relevant parameter combinations — source offset, destination offset, copy length.

**Why It Matters**: Bit manipulation has an exponential number of edge cases at boundaries. Only exhaustive testing provides confidence.

**When to Apply**: Any low-level algorithm operating on sub-word data.

**Red Flags**:
- Tests with only a handful of hand-picked sizes
- No testing around word boundaries
- No testing of misaligned source-destination combinations

**Supporting Experiences**: S18E2

<!-- METADATA
kind: principle
id: S18P1
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [S18E2]
related-principles: [S4P2, S18P2]
-->

---

### S18P3: Runtime Optimizations Carry High Regression Risk

> *"we just got done dealing with fixing a bunch of regressions caused by performance optimizations... if it breaks at runtime, it's always bad."*

**The Principle**: Performance optimizations to runtime algorithms are inherently higher risk. The testing bar must be proportionally higher.

**Why It Matters**: Compile-time errors are caught before shipping. Runtime errors silently produce wrong results in production.

**When to Apply**: Reviewing any PR that optimizes runtime behavior.

**Red Flags**:
- Performance optimization PRs with minimal test coverage
- "This optimization is simple, it can't be wrong"
- No before/after behavioral comparison tests

**Supporting Experiences**: S18E2, S18E3

<!-- METADATA
kind: principle
id: S18P3
source-type: tacit
category: evaluation/red-flags
applies-to: both
confidence: high
supported-by: [S18E2, S18E3]
related-principles: [S18P1]
-->

---

### S19P1: Import Lib Code Must Not Depend on Non-Core Headers

> *"What I really need to do here is make it so that we cannot include anything noncore in the import lib."*

**The Principle**: Code compiled into the import library must depend only on "core" headers free of iterator debug level dependencies and complex template machinery.

**Why It Matters**: The import lib is the ABI boundary. Non-core headers create hidden ABI dependencies.

**When to Apply**: Any code compiled into the STL's import library.

**Red Flags**:
- New import lib code that `#include`s non-core headers
- Transitive includes through generated files

**Supporting Experiences**: S19E1

<!-- METADATA
kind: principle
id: S19P1
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [S19E1]
related-principles: [S13P1, S19P2]
-->

---

### S19P2: Use C Interfaces at ABI Boundaries

> *"While we are the providers of awesome tech, like std::expected, we throw it all away and we go down to the simplest C stuff for our ABI."*

**The Principle**: ABI-stable boundaries should use C-style interfaces (plain enums, integral types, raw pointers) rather than C++ types.

**Why It Matters**: C++ introduces many ways to break ABI. C interfaces are maximally stable and compatible.

**When to Apply**: Any function crossing a DLL/import-lib boundary.

**Red Flags**:
- C++ types crossing DLL boundaries
- Templates in import lib function signatures

**Supporting Experiences**: S19E1

<!-- METADATA
kind: principle
id: S19P2
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [S19E1]
related-principles: [S19P1, S9P2]
-->

---

### S19P3: Prefer Simpler Implementation Now, Optimize Later With Evidence

> *"Going with something simpler seems even if it's a bigger code change, it's gonna result a lot simpler code."*

**The Principle**: Choose simplicity unless profiling proves the optimization is necessary. Ensure the ABI allows future optimization.

**Why It Matters**: Complex code has more bugs. For I/O, the bottleneck is external, not CPU.

**When to Apply**: Any performance-sensitive implementation where the dominant cost is external.

**Red Flags**:
- Premature optimization that adds significant complexity
- ABI-visible optimization decisions that can't be revised

**Supporting Experiences**: S19E2, S19E3

<!-- METADATA
kind: principle
id: S19P3
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [S19E2, S19E3]
related-principles: [S2P2]
-->

---

## Experiences

### S1E1: Catching a Subtle Standardese Mismatch in Three-Way Lexicographic Compare

**Context**: Reviewing optimized `lexicographical_compare_three_way` using `memcmp` + metaprogrammed predicate dispatch.

**What Happened**: STL noticed code used `_Memcmp_pred` to compare sequence lengths when elements were equivalent. This was consistent with the element comparison dispatch, but the standard says to directly `<=>` the lengths.

**Outcome**: Comment requesting direct `<=>` on lengths for clarity and correctness alignment.

**Lesson**: Pattern consistency across similar algorithms can mask semantic divergence.

> *"Even though it does look like it's consistent here... that difference in pattern is what clued me in."*

**Supports Principles**: S1P1, S1P5

<!-- METADATA
kind: experience
id: S1E1
source-type: explicit
category: evaluation/library
applies-to: library
outcome: success
features: [lexicographic-compare, three-way-comparison, memcmp]
supports: [S1P1, S1P5]
-->

---

### S3E1: Nicole Catches De Morgan Bug in Copy Constructor Constraints

**Context**: `std::expected`'s non-trivial copy constructor constrained with `!trivial<T> && !trivial<E>` instead of `!trivial<T> || !trivial<E>`.

**What Happened**: The incorrect conjunction left a gap for types where exactly one is trivially copy constructible. Same error was on the move constructor.

**Outcome**: Bug caught before merge.

**Lesson**: Constraint negation is one of the most common sources of bugs in conditionally-trivial types.

> *"This is an excellent example of how code review can catch bugs."*

**Supports Principles**: S3P1

<!-- METADATA
kind: experience
id: S3E1
source-type: explicit
category: history/failures
applies-to: library
outcome: success
features: [expected, conditional-triviality, De-Morgan]
supports: [S3P1]
-->

---

### S6E1: Vector Range Constructor — Lost Iterator Category

**Context**: GitHub issue #1709 — passing C++20 ranges to vector's range constructor fell back to the input-iterator path.

**What Happened**: Vector checked C++17 tags only. C++20 view iterators satisfy concepts but report weaker tags. Adam Bucior added an `else if constexpr` for concepts. Team preserved both paths for backward compatibility.

**Outcome**: Success — conservative, noninvasive approach.

**Lesson**: In central containers, add new code paths alongside old ones rather than replacing them.

> *"Being noninvasive is probably the right approach here."*

**Supports Principles**: S6P1

<!-- METADATA
kind: experience
id: S6E1
source-type: explicit
category: history/decisions
applies-to: library
outcome: success
features: [vector, iterator-concepts, ranges]
supports: [S6P1]
-->

---

### S11E1: Discovering a C++20 Compiler Bug Live During Code Review

**Context**: STL was demonstrating the comma-vs-&& bug that `[[nodiscard]]` catches. He switched to C++20 mode.

**What Happened**: The `[[nodiscard]]` warning disappeared. C++20's operator rewriting (`!=` → `!(==)`) wasn't carrying `[[nodiscard]]`. Both MSVC and GCC exhibited the bug; Clang did not.

**Outcome**: Compiler dev Cameron DaCamara had a fix PR within the hour.

**Lesson**: Live code review with cross-functional team members discovers and fixes compiler bugs in real time.

> *"Cameron's already got a PR out fixing the bug, so that's awesome."*

**Supports Principles**: S11P4

<!-- METADATA
kind: experience
id: S11E1
source-type: explicit
category: history/failures
applies-to: both
outcome: success
features: [nodiscard, operator-rewriting, C++20]
supports: [S11P4]
-->

---

### S12E1: Functional-Style Cast Enables const_cast in fold_right

**Context**: `fold_right` returns `U(std::move(init))` where `U` is computed from user types.

**What Happened**: With a function returning its second argument, `fold_right` over an empty `char*` range with `const char*` init silently `const_cast`s the pointer.

**Outcome**: LWG issue filed proposing `static_cast`.

**Lesson**: Functional-style casts in generic specs are ticking time bombs.

> *"Functional style cast doing a const_cast is absolutely bat**** behavior."*

**Supports Principles**: S12P1

<!-- METADATA
kind: experience
id: S12E1
source-type: explicit
category: wording/pitfalls
applies-to: both
outcome: failure
features: [fold-algorithms, functional-cast, const_cast]
supports: [S12P1]
-->

---

### S15E2: The Parentless Iterator Bug

**Context**: `find_last` helper value-initialized `_It last{}` then used `_Seek_wrapped(last, ...)`.

**What Happened**: Nicole noticed value-initialized `last` has no parent container. The forward non-common case compared `result == _It{}` which is UB per the standard.

**Outcome**: Major bug found. Casey filed an issue to add parent-checking to ranges test iterator machinery.

**Lesson**: Always use existing helpers (`_Rewrap_subrange`) rather than manual unwrap-seek patterns.

> *"This indicates a massive hole in our test coverage."*

**Supports Principles**: S15P2

<!-- METADATA
kind: experience
id: S15E2
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [find_last, iterator-rewrapping, ranges]
supports: [S15P2]
-->

---

### S17E2: Discovering Bogus Constraints on Const Rvalue Overloads

**Context**: `and_then` const rvalue overload required `is_move_constructible_v<E>` — semantically meaningless for const rvalue.

**What Happened**: Deep discussion about correct constraint. Casey argued constraints weren't needed at all — no realistic scenario benefits from SFINAE on these overloads.

**Outcome**: LWG issue filed.

**Lesson**: What looks like a simple typo can reveal deep design questions.

> *"Frankly, I don't even think this needs to be a constraint at all."*

**Supports Principles**: S17P4, S17P6

<!-- METADATA
kind: experience
id: S17E2
source-type: explicit
category: wording/pitfalls
applies-to: library
outcome: mixed
features: [expected, constraints, LWG-issues]
supports: [S17P4, S17P6]
-->

---

### S18E2: The 32x32x100 Exhaustive Testing Demand

**Context**: Optimized `vector<bool>` copy used hand-picked test cases with only 67 elements.

**What Happened**: STL counted special cases in the implementation and demanded exhaustive testing: every bit offset (0-31) × every bit offset (0-31) × range of copy lengths. "32x32x100 = ~100K cases. That's nothing."

**Outcome**: Team agreed to implement exhaustive testing with `vector<unsigned char>` as reference.

**Lesson**: For bit-manipulation, the number of edge cases is multiplicative. Only exhaustive testing provides confidence.

> *"Let's just test everything. Just go nuts and then see how fast it is."*

**Supports Principles**: S18P1

<!-- METADATA
kind: experience
id: S18E2
source-type: explicit
category: evaluation/field-experience
applies-to: library
outcome: mixed
features: [vector-bool, testing, bit-manipulation]
supports: [S18P1]
-->

---

### S19E1: The Grapheme Break Iterator Header Dependency Disaster

**Context**: `std::print` used a grapheme break property iterator. That iterator's UCD tables included `<xutility>` for `lower_bound`.

**What Happened**: This dragged a massive non-core header into the import lib, creating a hidden ABI dependency.

**Outcome**: Team eliminated the grapheme break iterator entirely. Verified through live experiment that `WriteConsoleW` handles split grapheme clusters correctly.

**Lesson**: Transitive include dependencies can silently violate architectural boundaries. Generated files are particularly dangerous.

> *"What are we even using—oh, lower_bound... I would rather extract and hand-write something here."*

**Supports Principles**: S19P1, S19P2

<!-- METADATA
kind: experience
id: S19E1
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [std-print, unicode, import-lib]
supports: [S19P1, S19P2]
-->

---

## Evaluation Checklists

### When Reviewing Pull Requests to a C++ Standard Library

- [ ] Are all standard paragraph citations verified against the current working draft? (S17P2)
- [ ] Are `static_assert` messages using user-facing names? (S17P8)
- [ ] Are mandates staged for better diagnostics? (S17P5)
- [ ] Are `requires` clauses needed for overload resolution, or should they be mandates? (S17P6)
- [ ] Does implementation directly mirror standard structure? (S17P7)
- [ ] Are functional-style casts replaced with `static_cast`? (S12P1, S17P1)
- [ ] Are all feature test macro values verified against the working draft? (S10P4, S12P2)
- [ ] Is De Morgan's law correctly applied in constraint negation? (S3P1)
- [ ] Are noexcept specifications traced through all call layers? (S13P4)
- [ ] Is noexcept strengthening consistent with the requires clause? (S13P5)
- [ ] Are all assertion messages verified for copy-paste errors? (S8P1)
- [ ] Are all `[[nodiscard]]` annotations present on all overloads? (S16P7)
- [ ] Are code movements verified by diffing old and new locations? (S7P1)
- [ ] Are entries added to sorted lists in the correct position? (S10P5)
- [ ] Is every new public identifier marked for module export? (S13P3)

**Questions to Ask**:
1. "What has been the field experience with this implementation?"
2. "Does this optimization match the semantic intent of the standard?"
3. "Have we checked both C++17 tags and C++20 concepts?"
4. "Is there a compiler bug we need to work around? If so, filed?"
5. "Would a staff engineer approve this?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [S1P5, S3P1, S6P1, S7P1, S8P1, S10P4, S12P1, S13P4, S16P7, S17P2, S17P5, S17P6, S17P7]
-->

---

### When Reviewing Pull Requests to a C++ Compiler Front End

- [ ] Are template parameter names distinct from nested/member names? (S1P1, S1P3)
- [ ] Is `decltype(auto)` vs `decltype(expr)` chosen correctly for SFINAE? (S9P1)
- [ ] Are `if constexpr` chains ordered most-specific-first? (S6P3)
- [ ] Are compiler built-ins centralized in helper functions? (S4P3)
- [ ] Do `[[nodiscard]]` attributes propagate through operator rewriting? (S11P4)
- [ ] Are ABI-sensitive changes guarded against cross-mode ODR violations? (S9P2)
- [ ] Are workarounds marked with `// TRANSITION, <version>`? (S4P5, S16P4)
- [ ] Do concepts and constraints distinguish library vs language intent? (S17P6)
- [ ] Are O(N) precondition checks guarded by constant-time feasibility? (S10P3)
- [ ] Has exhaustive boundary testing been performed for bit-level operations? (S18P1)
- [ ] Are functional-style casts avoided in generic/template contexts? (S12P1)
- [ ] Is ADL considered and either used intentionally or suppressed? (S1P4, S5P5)

**Questions to Ask**:
1. "Does this change affect how templates are instantiated across TUs?"
2. "Could this break ABI when different TUs use different standard modes?"
3. "What happens when this interacts with concept checking?"
4. "Is this a known compiler limitation that we should file and track?"
5. "Are there edge cases at boundaries (word boundaries, type boundaries) that need exhaustive testing?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: both
proposal-type: feature
derived-from: [S1P1, S1P3, S1P4, S4P3, S4P5, S6P3, S9P1, S9P2, S10P3, S11P4, S12P1, S16P4, S17P6, S18P1]
-->

---

### When Reviewing Performance Optimization PRs

- [ ] Is there exhaustive testing across all boundary-relevant parameter combinations? (S18P1)
- [ ] Is there a reference implementation for correctness comparison? (S18P2)
- [ ] Have all special cases in the implementation been covered by tests? (S4P2)
- [ ] Are overlapping range cases tested for copy/move algorithms? (S18P1)
- [ ] Is testing proportional to the runtime regression risk? (S18P3)
- [ ] Is the optimization actually needed, or would simpler code suffice? (S19P3)
- [ ] Have byte/element distinctions been maintained in naming? (S4P1)
- [ ] Is stack buffer usage conservative? (S19P5)

**Questions to Ask**:
1. "What is the worst-case stack usage?"
2. "Can we verify this against the standard paragraph by paragraph?"
3. "What happens if we simplified and optimized later with evidence?"
4. "Is the test coverage proportional to the number of special cases?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: both
proposal-type: feature
derived-from: [S4P1, S4P2, S18P1, S18P2, S18P3, S19P3, S19P5]
-->

---

## Key Compiler/Library Implementation Insights

### Template Instantiation & SFINAE

- `if constexpr (is_constant_evaluated())` is always true — the compiler warns. Use plain `if`, not `if constexpr`.
- `decltype(auto)` return requires body instantiation (hard error); `decltype(expr)` gives SFINAE.
- `always_false<T>` variable template delays `static_assert(false)` until instantiation.
- `void_t<decltype(expression)>` partial specialization is the conventional detection idiom.
- `is_base_of` ignores access control and ambiguity; `derived_from` requires public unambiguous inheritance.
- Template argument deduction for base class detection works only with public unambiguous inheritance — not conversion operators.

### Concepts & Constraints

- C++20 concepts may be stronger than C++17 categories — always check both.
- `sized_sentinel_for` ≠ `sized_range`. Use the right concept for the abstraction level.
- Concepts-satisfying test types should `static_assert(false)` in unused bodies to catch accidental calls.
- Constraints should serve overload resolution, not replace mandates.
- De Morgan errors in constraint negation are extremely common.

### ABI & Cross-TU

- `[[no_unique_address]]` is a no-op in MSVC until the next ABI break.
- `detect_mismatch` enforces cross-TU configuration consistency at link time.
- C interfaces at ABI boundaries; C++ types must not cross DLL boundaries.
- Mode-dependent base classes are ODR violations across standard-mode TU linking.

### Naming & Style

- `_Ugly_snake_case` for types/functions; `_UglyCamelCase` for template parameters.
- Same names for same things, different names for different things.
- `// TRANSITION, <version>` marks every compiler workaround.
- `#endif` comments are mandatory in dense preprocessor code.

### Testing

- 32×32×100 exhaustive testing for bit manipulation.
- Reference implementations (`vector<unsigned char>` for `vector<bool>`) as truth source.
- Empty ranges, boundary values, and cross-type comparisons in every test.
- Don't define `NOMINMAX` in tests — test code should face the same hostile macro environment.

---

## Open Questions

1. What is the complete list of "core" vs "non-core" headers in the MSVC STL?
2. Has the import lib core-header validation been automated?
3. What is the full list of libraries "where this strategy has failed us in the past" (field experience requirement)?
4. What was the resolution of the `and_then`/`or_else` constraint LWG issue?
5. Has `noexcept(auto)` been proposed for standardization?
6. When will `deducing this` be usable in module-exported code?

---

## Raw Transcript References

All transcripts from VC Libraries Open Code Review sessions:

| Session | Date | Topic | Source |
|---------|------|-------|--------|
| 1 | 2021-09-09 | memcpy/memmove/memcmp optimizations | `inputs/stl/2021-09-09.md` |
| 2 | 2022-01-13 | Ratio: constexpr functions | `inputs/stl/2022-01-13.md` |
| 3 | 2022-04-28 | std::expected (part 2) | `inputs/stl/2022-04-28.md` |
| 4 | 2022-05-12 | Vectorized min/max/minmax_element | `inputs/stl/2022-05-12.md` |
| 5 | 2022-05-26 | ranges::iota, shift_left, shift_right | `inputs/stl/2022-05-26.md` |
| 6 | 2022-06-09 | Vector range constructor concepts | `inputs/stl/2022-06-09.md` |
| 7 | 2022-06-23 | P1206R7 ranges::to (part 1) | `inputs/stl/2022-06-23.md` |
| 8 | 2022-07-07 | P1206R7 ranges::to (parts 2 & 3) | `inputs/stl/2022-07-07.md` |
| 9 | 2022-07-14 | P2387R3 pipe support, bind_back | `inputs/stl/2022-07-14.md` |
| 10 | 2022-08-04 | P1899R3 views::stride | `inputs/stl/2022-08-04.md` |
| 11 | 2022-08-25 | [[nodiscard]] messages | `inputs/stl/2022-08-25.md` |
| 12 | 2022-09-15 | Ranges fold algorithms | `inputs/stl/2022-09-15.md` |
| 13 | 2022-10-13 | views::zip | `inputs/stl/2022-10-13.md` |
| 14 | 2022-11-03 | ASan string annotations | `inputs/stl/2022-11-03.md` |
| 15 | 2022-12-08 | find_last algorithms | `inputs/stl/2022-12-08.md` |
| 16 | 2023-01-12 | zip_transform_view | `inputs/stl/2023-01-12.md` |
| 17 | 2023-02-07 | Monadic expected functions | `inputs/stl/2023-02-07.md` |
| 18 | 2023-02-23 | vector\<bool\> optimization | `inputs/stl/2023-02-23.md` |
| 19 | 2023-03-16 | std::print | `inputs/stl/2023-03-16.md` |
