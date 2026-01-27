# Evaluation: P3724R2 — Integer division

**Paper:** P3724R2  
**Title:** Integer division  
**Authors:** Jan Schultke  
**Link:** [https://wg21.link/P3724R2](https://wg21.link/P3724R2)  
**Revision Date:** 2025-12-14  
**Evaluation Date:** 2026-01-26

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ⚠️ BORDERLINE PASS  
Paper documents that correct implementations are genuinely hard—users consistently produce buggy code (§3.1 cites multiple Stack Overflow answers with incorrect implementations). This meets the "genuinely hard to solve" criterion, though no inter-library coordination failure is documented.

**G1. Why not third-party?** ❌ FAIL  
Paper provides a complete reference implementation (Appendix A) that would work as a header-only library. No discussion of why ecosystem distribution (Boost, vcpkg, conan) is insufficient. The functions don't require compiler integration and are not vocabulary types exchanged at API boundaries.

**G2. Perpetual costs acknowledged?** ❌ FAIL  
No discussion of implementation burden on vendors, interaction surface with existing library components, teaching/documentation burden, or long-term maintenance commitment.

**Gate Result:** ❌ AUTOMATIC FAIL — G1 and G2 not addressed

---

## Guidance for Authors

This evaluation is not a judgment on whether your library is useful or well-designed—the excellent use-case examples and comprehensive reference implementation demonstrate it is both. The gate failure indicates that the proposal, as written, has not yet made the case for why this functionality must be in the C++ standard library rather than distributed through the ecosystem.

### What Was Missing

**G1 failed** because the paper does not address why third-party distribution is insufficient. The complete reference implementation in Appendix A demonstrates this functionality can be distributed as a header-only library. The functions don't require compiler/language integration unavailable to third parties, and they are not vocabulary types that libraries need to exchange at API boundaries.

**G2 failed** because the paper contains no discussion of:
- Implementation burden across compiler vendors (GCC, Clang, MSVC, others)
- Interaction surface with existing `<numeric>` facilities, `<bit>`, and `<cmath>`
- Who will address defects discovered post-standardization
- Teaching and documentation requirements

### How to Strengthen a Revision

To pass G1 (Why not third-party?), consider adding:
- **Cross-library exchange analysis**: Do libraries need to pass `div_result<T>` across API boundaries? If so, document why incompatible types would cause problems.
- **Ecosystem survey**: Are there existing third-party implementations? If multiple exist, have they caused integration issues?
- **Portability argument**: While the functions can be header-only, is there value in guaranteed cross-platform availability that ecosystem distribution cannot provide?
- **Alternative consideration**: Add a section explicitly analyzing "Why not a header-only library distributed via vcpkg/conan?" and answering it.

To pass G2 (Perpetual costs), consider adding:
- **Implementation analysis**: The reference implementation is ~150 lines for `int` only. Estimate complexity for full template implementation across all integer types including extended and bit-precise integers.
- **Interaction surface**: Document how these functions interact with `<numeric>` (saturation arithmetic), `<bit>` (bit manipulation), and future SIMD overloads.
- **Maintenance commitment**: State who will address defects. Given SG6 review history, consider noting ongoing engagement.
- **Teaching burden**: These are 21 new function templates + `div_result<T>`. Estimate documentation requirements.

**Alternative argument path**: Howard Hinnant's principle includes "make the hard easy." The paper excellently documents that correct implementations ARE hard. Consider strengthening this angle:
- Quantify: How many buggy implementations exist? How much time do developers waste?
- Show: The Stack Overflow evidence is compelling—expand it with GitHub search data showing incorrect implementations in production code.
- Argue: Unlike simple utilities, these functions have non-obvious correctness requirements (overflow, signed/unsigned edge cases) that justify standardization even without coordination failures.

### Alternative Paths

If standardization justification remains difficult:
- **Boost submission**: Submit to Boost.Integer or as standalone Boost.IntDiv to establish multi-year field experience and gather adoption data.
- **GitHub distribution**: The reference implementation on GitHub could be published to vcpkg/conan to demonstrate demand via download metrics.
- **Safety angle**: Given C++ safety focus, emphasize that incorrect user implementations are a safety hazard—buggy division functions have caused real security vulnerabilities in the wild.

### Strengths to Preserve

- **Excellent motivating examples**: §3 "Motivation" with bucket counting and bucket assignment is exactly the right way to open a proposal
- **Thorough existing practice survey**: §2.1 tables showing language and hardware support demonstrate deep domain knowledge
- **Complete, tested reference implementation**: Appendix A provides production-quality code that proves the design works
- **Responsive to review**: Changes from R1 based on SG6 feedback show good committee engagement

---

*This feedback is generated to help improve proposals. The committee values your contribution to C++ and encourages resubmission once the standardization justification is strengthened.*

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal failed the standardization justification gate.** The detailed evaluation below is provided for reference. The primary action items are in Guidance for Authors above.

🔴 GATE FAIL: Proposal does not justify why this cannot remain a third-party library or acknowledge perpetual costs.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 0 | ❌ |
| 3. Vocabulary Necessity | 0 | ❌ |
| 4. External Validation | 1 | ⚠️ |
| 5. Implementation | 1 | ⚠️ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 1 | ⚠️ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 0 | ❌ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **14/26** | Meets library threshold, but gate failed |

## Summary Exposition

P3724R2 is a technically excellent proposal with clear motivation, comprehensive design rationale, and a complete reference implementation. The author demonstrates deep domain knowledge through extensive surveys of language support (§2.1.1) and hardware support (§2.1.2), and provides compelling evidence that correct implementations are surprisingly difficult (§3.1, §3.2).

The proposal's primary weakness is insufficient justification for standardization over ecosystem distribution. The paper implicitly treats "users get this wrong" as sufficient justification, but the evaluation framework requires explicit analysis of coordination failures, vocabulary type necessity, or ecosystem inadequacy. The reference implementation itself proves this can be a header-only library—the paper must explain why that's insufficient.

**Recommendation:** Revise to address G1 and G2 before resubmission. The technical content is strong; what's needed is a standardization justification section. Consider emphasizing the "make the hard easy" argument more explicitly, with quantified evidence of harm from incorrect user implementations.

## Red Flags Identified

🚩 **No standardization justification** — Treats "useful and hard to get right" as sufficient; no analysis of why ecosystem distribution fails

🚩 **No retrospective plan** — No success criteria, adoption targets, or post-adoption evaluation commitment

🚩 **Convenience threshold concern** — Primary value is providing correct implementations users could write themselves (albeit incorrectly); borderline on "make hard easy" vs "make easy easier"

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with concrete, motivating code examples showing bucket counting (`div_to_pos_inf`) and bucket assignment (`div_to_neg_inf`). §3.1 provides extensive real-world examples of buggy implementations from Stack Overflow, demonstrating the design addresses genuine user pain points. The interactive demonstration in §6 "Try it yourself" allows hands-on validation.

**Evidence cited:** "A common problem is to compute how many chunks/buckets/blocks of a fixed size are needed to fit a certain amount of elements" (§3)

### 2. Economic Analysis — ❌

**Score: 0/2**

No analysis of perpetual costs, implementation burden, or why standardization is necessary versus third-party distribution. The paper mentions "implementation effort for all of these functions is close to zero" (§5) but this refers to implementation difficulty, not ongoing maintenance costs borne by vendors and the committee.

**Evidence cited:** None found

### 3. Vocabulary Necessity — ❌

**Score: 0/2**

These are utility functions, not vocabulary types. There's no evidence that libraries need to exchange `div_result<T>` at API boundaries. No documentation of coordination failures between incompatible implementations. The functions work in isolation without cross-library agreement.

**Evidence cited:** None found

### 4. External Validation — ⚠️

**Score: 1/2**

The paper cites Stack Overflow questions showing genuine user demand ([StackOverflowCeil], [StackOverflowRound]). However, no specific organizations are named as wanting this, no testimonials from production deployments, and no survey data showing this ranks highly among C++ developer needs.

**Evidence cited:** "At the time of writing, the first Google search result for 'c++ ceiling integer division' yields [StackOverflowCeil]" (§3.1)

### 5. Implementation & Field Experience — ⚠️

**Score: 1/2**

Reference implementation is publicly available on GitHub ([GitHub]). Paper has undergone SG6 review with responsive changes (div_to_even removed per poll). However, no evidence of positive feedback from independent users outside the proposal process. No multi-year deployment history.

**Evidence cited:** "A reference implementation can be found on [GitHub]" (§5)

### 6. Completeness — ✅

**Score: 2/2**

The proposal is fully self-contained. All 21 function templates are specified with complete wording. Users can immediately use the feature without additional ecosystem support. No "machinery now, types later" pattern—everything ships together.

**Evidence cited:** Complete wording in §7 and reference implementation in Appendix A

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

Single author with clear engagement (three revisions, responsive to SG6 feedback). No corporate interests apparent. However, no explicit stewardship commitment or succession plan. Author acknowledges in §8 Lawrence Crowl's review.

**Evidence cited:** "I sincerely thank Lawrence Crowl... for reviewing this paper in great detail" (§8)

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria defined. No adoption targets specified. No retrospective analysis planned. No mechanisms for gathering usage data post-standardization.

**Evidence cited:** None found

### 9. Process & Timeline — ✅

**Score: 2/2**

Clear progression through revisions with explicit change logs. SG6 review completed with documented polls and consensus outcomes. Single author provides clear design authority. Non-goals explicitly stated (SIMD overloads deferred to follow-up proposal §4.6).

**Evidence cited:** "R1 of this paper was seen by SG6. Several polls were taken" (§1.1)

### 10. Practical Usability — ✅

**Score: 2/2**

Functions clearly simplify user code versus writing correct implementations manually. Self-documenting names (`div_to_neg_inf` vs `floor`). Designed as "drop-in replacement for the various bad implementations that users have written themselves" (§4). Error messages will be straightforward (template instantiation failures for invalid types).

**Evidence cited:** "the proposed functionality should be a drop-in replacement for the various bad implementations that users have written themselves" (§4)

### 11. Safety & Stability — ⚠️

**Score: 1/2**

Functions have same undefined behavior as existing division (division by zero, `INT_MIN / -1`). Constant-checked preconditions prevent UB during constant evaluation. No ABI concerns (function templates). However, no explicit safety roadmap analysis or contribution to C++ safety goals.

**Evidence cited:** "These functions are not noexcept because they could not have a wide contract" (§4.3.1)

### 12. Ecosystem Consideration — ❌

**Score: 0/2**

No analysis of whether this should be in the standard versus ecosystem. No consideration of third-party alternatives. No explanation of why a header-only library distributed via vcpkg/conan would be insufficient.

**Evidence cited:** None found

### 13. Expert Weighting — ✅

**Score: 2/2**

Lawrence Crowl (original P0105R1 author, decades of WG21 experience) reviewed the paper in detail. SG6 (Numerics study group) has reviewed with polls. Design builds on prior proposals ([P0105R1], [P1889R1]) with acknowledged improvements.

**Evidence cited:** "I sincerely thank Lawrence Crowl (the author of the predecessor paper [P0105R1]) for reviewing this paper in great detail, providing detailed feedback" (§8)
