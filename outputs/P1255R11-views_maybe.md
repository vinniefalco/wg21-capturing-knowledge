# Evaluation: P1255R11 — A view of 0 or 1 elements: views::maybe

**Paper:** P1255R11  
**Title:** A view of 0 or 1 elements: views::maybe  
**Authors:** Steve Downey (sdowney@gmail.com)  
**Link:** [https://wg21.link/P1255R11](https://wg21.link/P1255R11)  
**Revision Date:** 2024-01-12  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ❌ FAIL  
No coordination failure documented. The before/after examples show existing solutions work (filter + transform pipelines). The primary value is convenience and safety improvements for already-solvable problems—the "before" code compiles and runs correctly today.

**G1. Why not third-party?** ❌ FAIL  
Paper explicitly states implementation exists at GitHub with "no particular implementation difficulties." No documented coordination failures, no explanation of why ecosystem distribution (vcpkg/conan) is insufficient. Functionality is purely header-only compatible.

**G2. Perpetual costs acknowledged?** ❌ FAIL  
Section 11 states only "A pure library extension, affecting no other parts of the library or language." No analysis of vendor implementation burden, interaction surface with existing ranges components, teaching burden, or maintenance commitment.

**Gate Result:** ❌ AUTOMATIC FAIL — Standardization not justified. Proposal provides convenience improvements for problems already solvable with existing range adaptors.

---

## Guidance for Authors

This evaluation is not a judgment on whether `views::maybe` and `views::nullable` are useful or well-designed—the excellent use-case examples suggest they may well be both. The gate failure indicates that the proposal, as written, has not yet made the case for why this functionality must be in the C++ standard library rather than distributed through the ecosystem.

### What Was Missing

**G0 failed** because the paper demonstrates that the problem is already solvable. The before/after table in Section 1 shows:

```cpp
// Before (works today)
auto&& r = v | ranges::views::transform(test) |
           ranges::views::filter([](auto x) { return bool(x); }) |
           ranges::views::transform([](auto x) { return *x; }) | ...

// After (proposed)  
auto&& r = v | ranges::views::transform(test) |
           ranges::views::transform(views::nullable) |
           ranges::views::join | ...
```

Both produce the same result. The proposal makes code more elegant but doesn't enable anything previously impossible. Per Howard Hinnant's threshold: "Making the easy easier, I find very uninteresting and not worthwhile to standardize."

The safety argument (Section 2) is compelling for library design but insufficient for standardization justification—users can achieve safety today by immediately binding the dereferenced optional to a named variable.

**G1 failed** because the paper acknowledges a working GitHub implementation exists. No documented interoperability failures between this implementation and any other ranges code are presented. No attempt to explain why Boost submission, vcpkg distribution, or header-only inclusion would be insufficient.

**G2 failed** because the paper's only acknowledgment of standardization costs is that it's "a pure library extension." This ignores:
- Implementation burden on libstdc++, libc++, MSVC STL
- Interaction with `<ranges>`, `<optional>`, `<algorithm>` headers
- Teaching burden: another view type to explain alongside `single`, `empty`, `filter`, `transform`
- Monadic interface (`and_then`, `transform`, `or_else`) creates interaction surface with `std::optional`'s monadic operations

### How to Strengthen a Revision

To pass G0 (What coordination failure does this solve?), consider:
- **Documenting harm from current patterns**: Cite specific bug reports where the filter+transform pattern led to bugs that `views::nullable` would prevent
- **Show library boundary friction**: Document cases where libraries needed to exchange "0 or 1 element" ranges and couldn't interoperate
- **Quantify safety incidents**: If the unsafe nullable protocol has caused documented CVEs or bugs in production code, cite them
- **Demonstrate the impossible made possible**: Show use cases that genuinely cannot be achieved with existing range adaptors

To pass G1 (Why not third-party?), consider:
- **Document vcpkg/conan distribution attempts**: If the GitHub implementation has been published through package managers, report adoption and any friction
- **Vocabulary type evidence**: If other libraries have attempted to define similar "0 or 1" range types and couldn't interoperate, document those failures
- **Boost submission**: Consider submitting to Boost.Range to gather multi-year field experience and establish ecosystem standard

To pass G2 (Perpetual costs), consider adding:
- **Implementation complexity analysis**: The monadic interface (`and_then`, `transform`, `or_else`) requires specification review against `std::optional`'s P0798R8 monadic operations for consistency
- **Interaction surface**: Document how `maybe_view` interacts with `views::join`, `views::filter`, `views::transform`, and other range adaptors
- **Teaching burden**: `maybe_view` vs `optional` vs `single` vs `empty`—when should users choose each?
- **Maintenance commitment**: State who will address defects post-standardization

### Alternative Paths

If coordination failures are difficult to document, consider:

1. **Boost submission**: Establish `views::maybe` in Boost.Range or a standalone Boost library. Gather 2-3 years of field experience from independent users. Document adoption metrics.

2. **Standalone distribution**: Publish via vcpkg/conan and track:
   - Download counts
   - GitHub issues/feedback
   - Real-world usage examples from adopters (not just the author)

3. **Return with evidence**: After ecosystem deployment, return to committee with:
   - Named projects using the library
   - User testimonials
   - Any documented cases where standardization would have helped

4. **Narrow scope**: Consider proposing only `views::nullable` (which has stronger safety motivation) and leaving `views::maybe` to the ecosystem, reducing standardization burden.

### Strengths to Preserve

- **Excellent before/after examples**: Section 1's comparison table immediately communicates the value proposition—preserve this in any revision
- **Complete wording**: The proposal includes full wording with all member functions specified—this is production-ready
- **Pythagorean triples example**: Section 3 shows the monadic/list-comprehension pattern elegantly—strong motivating example
- **Safety analysis**: The discussion of moving dereference into the for-loop to avoid distant use/*opt bugs is genuinely valuable
- **Reference specialization rationale**: Section 5.3's discussion of `maybe_view<T&>` ergonomics shows thoughtful API design

---

*This feedback is generated to help improve proposals. The committee values your contribution to C++ and encourages resubmission once the standardization justification is strengthened.*

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal failed the standardization justification gate.** The detailed evaluation below is provided for reference. The primary action items are in Guidance for Authors above.

🔴 GATE FAIL: Proposal does not justify why this cannot remain a third-party library; primary value is convenience for already-solvable problems.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 0 | ❌ |
| 3. Vocabulary Necessity | 1 | ⚠️ |
| 4. External Validation | 0 | ❌ |
| 5. Implementation | 1 | ⚠️ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 1 | ⚠️ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 1 | ⚠️ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 0 | ❌ |
| 13. Expert Weighting | 1 | ⚠️ |
| **TOTAL** | **12/26** | Below threshold (14) |

### Summary Exposition

P1255R11 proposes `views::maybe` (an owning 0-or-1 element view) and `views::nullable` (a range adaptor over nullable types like `std::optional` and pointers). The paper is well-written with clear before/after examples and complete wording through R11. The design is thoughtful, including reference specializations for ergonomic mutation and monadic operations (`and_then`, `transform`, `or_else`) paralleling `std::optional`.

However, the proposal fails the standardization threshold. The before/after examples demonstrate that existing range adaptors (`filter` + `transform`) already solve these problems—just less elegantly. The paper's value proposition is convenience and marginal safety improvement, not enabling previously impossible capabilities. Howard Hinnant's principle applies: "Making the easy easier, I find very uninteresting and not worthwhile to standardize."

The recommendation is to deploy through the ecosystem (vcpkg, conan, or Boost), gather field experience from independent users, document any coordination failures that emerge, and return with evidence of actual standardization necessity.

### Red Flags Identified

🚩 **No named users** — Paper mentions no specific organizations or projects that have requested or deployed this functionality

🚩 **No demand signal** — No evidence of user surveys, StackOverflow questions, or ecosystem demand for this specific abstraction

🚩 **No standardization justification** — Treats "useful" and "safer" as sufficient; no cost analysis of perpetual standardization burden

🚩 **Convenience without threshold** — Primary value is more elegant syntax for already-solvable problems; fails "make impossible possible, not easy easier" test

🚩 **Decade-long development** — R11 over multiple years without shipping; while thorough, suggests lack of urgency or ecosystem-blocking need

---

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with an excellent before/after comparison table (Section 1) showing concrete user-facing code. Section 2 provides multiple motivating examples including range-based for loops with nullable types, `reference_wrapper` mutation patterns, and integration with lookup operations. Section 3's Pythagorean triples example demonstrates the monadic programming pattern clearly. Design was clearly built to serve use-cases.

**Evidence cited:** Section 1 before/after table; Section 2 motivation examples; Section 3 Pythagorean triples

---

### 2. Economic Analysis — ❌

**Score: 0/2**

No economic analysis present. Section 11 states only "A pure library extension, affecting no other parts of the library or language." No acknowledgment of:
- Implementation burden on three major standard library implementations
- Interaction complexity with existing `<ranges>` components
- Teaching burden (yet another view type)
- Defect resolution commitment

**Evidence cited:** Section 11: "A pure library extension"—no cost analysis

---

### 3. Vocabulary Necessity — ⚠️

**Score: 1/2**

Section 5.1 argues for vocabulary type status: "there are use cases for returning near primitive ranges as explicit types" and "Explicit types are much easier for compilers to generate good code." However, no documented coordination failures are presented—no bug reports, no interoperability issues, no quantified harm from fragmentation. The vocabulary argument is theoretical, not evidence-based.

**Evidence cited:** Section 5.1 "The Argument for a Vocabulary Type"—argument made but not substantiated with evidence

---

### 4. External Validation — ❌

**Score: 0/2**

No external validation present. No specific organizations cited. No user testimonials. No quantitative problem statement. No survey data. No endorsements from domain experts. The paper targets "SG9, LEWG" but provides no evidence of user demand outside the committee process.

**Evidence cited:** None found

---

### 5. Implementation — ⚠️

**Score: 1/2**

Implementation publicly available at https://github.com/steve-downey/view_maybe. Section 8 states "no particular implementation difficulties or tricks." However:
- No positive feedback from independent users documented
- Single implementation only
- No evidence of multi-year deployment
- No implementation differences revealing design ambiguities

R11 indicates iteration, but field experience from users outside the author's team is not documented.

**Evidence cited:** Section 8 references GitHub implementation; no independent user feedback cited

---

### 6. Completeness — ✅

**Score: 2/2**

Proposal is complete and usable out-of-the-box. Section 10 provides full wording for `maybe_view`, `nullable_view`, and all member functions. Both view types are fully specified with constructors, iterators, comparison operators, and monadic operations. No "machinery now, types later" pattern. Feature-test macro included.

**Evidence cited:** Section 10 complete wording; Section 7 Freestanding analysis

---

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

Single author (Steve Downey) with clear technical investment (R11 iterations). No explicit stewardship commitment post-acceptance. No succession plan. No corporate interests disclosed or potential conflicts identified. Author appears to be genuinely community-motivated but no accountability mechanism is specified.

**Evidence cited:** Single author listed; no maintenance commitment statement

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria defined. No adoption targets. No measurable outcomes. No retrospective analysis planned. No mechanisms for gathering post-adoption usage data. Classic "ship and forget" pattern.

**Evidence cited:** None found

---

### 9. Process & Timeline — ⚠️

**Score: 1/2**

R11 indicates sustained development with tracked changes (Document history section). Clear audience targeting (SG9, LEWG). However, development over many years without shipping could indicate either thoroughness or stalled progress. No explicit timeline or milestones for completion. No competing proposals mentioned or resolved.

**Evidence cited:** Document history section shows progression R0→R11

---

### 10. Practical Usability — ✅

**Score: 2/2**

Before/after examples clearly show simplification. The feature makes user code more readable:
- Eliminates filter+transform+transform pattern
- Moves dereference into for-loop (safer)
- Enables monadic composition with `and_then`/`transform`

Reference specialization (`maybe_view<T&>`) shows attention to practical mutation patterns. Gradual adoption possible—new code uses views::nullable, old code continues working.

**Evidence cited:** Section 1 before/after table; Section 5.3 reference specialization rationale

---

### 11. Safety & Stability — ⚠️

**Score: 1/2**

Safety explicitly addressed in Section 2: "The nullable protocol that views::nullable adapts is inherently unsafe because it models unsafe pointer semantics... The allowed operations of views::nullable are all, in themselves, safe." This is a genuine safety improvement.

However:
- ABI implications not discussed
- No analysis of defect correction mechanisms
- No evolution/optimization path documented

**Evidence cited:** Section 2: "all of the operations on maybe_view and nullable_view are directly safe"

---

### 12. Ecosystem Consideration — ❌

**Score: 0/2**

No ecosystem analysis. Paper acknowledges GitHub implementation exists but doesn't analyze:
- Why ecosystem distribution is insufficient
- Comparison to similar ecosystem solutions
- Whether vcpkg/conan publication would solve the problem
- What specifically requires standardization vs third-party distribution

**Evidence cited:** Section 8 mentions GitHub implementation; no ecosystem comparison

---

### 13. Expert Weighting — ⚠️

**Score: 1/2**

Paper targets SG9 and LEWG. Author Steve Downey appears to have ranges expertise (implementation exists, wording is detailed). However:
- No mention of consultation with major ranges authors (Eric Niebler cited only for example inspiration)
- No validation from standard library implementers
- No production deployment history documented

**Evidence cited:** Section 3 mentions Eric Niebler's Pythagorean example; no implementer validation cited
