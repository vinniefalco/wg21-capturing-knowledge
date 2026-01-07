# Evaluation: D3952R0 — is_pointer_in_range

**Paper:** D3952R0  
**Title:** is_pointer_in_range  
**Authors:** Herb Sutter, Glen Joseph Fernandes  
**Link:** [https://wg21.link/D3952R0](https://wg21.link/D3952R0)  
**Revision Date:** 2025-12-28  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
The paper demonstrates this is literally impossible to implement correctly in portable C++: raw pointer comparison is UB outside the same array, and `std::less` relies on unspecified behavior allowing false positives. This makes the impossible possible.

**G1. Why not third-party?** ✅ PASS  
Requires compiler intrinsics (`__builtin_pointers_related` in Hana Dusíková's implementation) and `if consteval` semantics unavailable to third-party libraries. The paper explicitly shows no conforming implementation is possible without language support.

**G2. Perpetual costs acknowledged?** ⚠️ PARTIAL  
No explicit cost analysis, but the paper demonstrates implementations already exist in libc++, libstdc++, Qt, Boost, BSL, EASTL—costs are de facto already being paid. The proposal is minimal (one function).

**Gate Result:** ✅ PROCEED TO EVALUATION

---

🟢 PASS: Textbook example of "make the impossible possible"—enables correct, portable pointer-in-range checking that currently requires UB or unspecified behavior.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 1 | ⚠️ |
| 3. Vocabulary Necessity | 2 | ✅ |
| 4. External Validation | 2 | ✅ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 2 | ✅ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 2 | ✅ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **21/26** | Library threshold: 14 ✅ |

## Summary

This proposal is an exemplar of justified standardization. It passes the standardization threshold by making the impossible possible: there is currently **no correct portable C++ code** that can determine whether a pointer points into a buffer. Raw pointer comparison is undefined behavior outside the same array, and `std::less` relies on unspecified behavior that permits false positives due to pointer interleaving.

The paper documents extensive existing practice (libc++, libstdc++, Qt, Boost, BSL, EASTL) where implementations **must** solve this problem but currently rely on non-conforming or unspecified behavior. This is not "multiple implementations as justification"—this is "multiple implementations are all broken because the language doesn't provide the necessary primitive." The coordination failure is the language itself.

The proposal is minimal (one function), addresses a real safety concern (bounds checking for CWE Top 25 vulnerabilities), has broad expert review, and enables implementations to become conforming. The only weaknesses are lack of explicit cost analysis (mitigated by the trivial scope) and no retrospective commitment.

**Recommendation:** Proceed. This is exactly what standardization is for.

---

🚩 No retrospective plan — No success criteria defined

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with concrete motivation: checking whether data is already governed by a container, pointer bounds checking for security, and the existing requirement for `std::string::insert`. Section 1.1 provides clear use cases, and Section 1.6 documents existing implementations that need this functionality.

**Evidence cited:** "it enables more use cases that cannot tolerate false positive answers, such as checks for whether a data item is already governed by this container or is some new data that should be added/adopted, and pointer bounds checking"

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper does not explicitly quantify perpetual costs. However, it implicitly addresses this by showing implementations already exist across major standard libraries. The scope is minimal (one function), reducing the burden analysis requirement.

**Evidence cited:** None explicit. Implicit in Section 1.6 showing existing implementations.

---

### 3. Vocabulary Necessity — ✅

**Score: 2/2**

This is a rare case of genuine vocabulary necessity: standard library implementations **require** this functionality to be conforming (string insert must detect self-referencing ranges). The paper documents that current implementations "formally rely on unspecified behavior which can potentially generate false positives." The harm is not theoretical—it's that existing implementations are technically non-conforming.

**Evidence cited:** "This is already an implicit conformance requirement since C++98. As mentioned in [Core 2025], it's needed to implement std::string"

---

### 4. External Validation — ✅

**Score: 2/2**

Named implementations: libc++ (`__is_pointer_in_range`), Qt (`q_points_into_range`), Boost (`pointer_in_range`), libstdc++ (`basic_string::_M_disjunct`), BSL, EASTL. Named requesters include WG21 members (P3234R1, P3852R0) and CWG mailing list discussions. CBMC static analysis tool also implements this.

**Evidence cited:** Section 1.6 lists implementations with links. Section 1.1 references P3234R1, P3852R0, and [Core 2025].

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

Multiple production implementations exist (libc++, libstdc++, Qt, Boost). Hana Dusíková has a working Clang prototype with compiler intrinsic. Years of deployment in major standard library implementations. The implementations have revealed the design requirement: compiler support is necessary for correctness.

**Evidence cited:** Section 1.6 lists implementations. Section 2.3 shows Dusíková's Clang implementation with `__builtin_pointers_related`.

---

### 6. Completeness — ✅

**Score: 2/2**

This is a single, self-contained function. No ecosystem completion required. Usable immediately upon standardization.

**Evidence cited:** Section 3 shows the complete wording—one function signature, one paragraph of specification.

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

Authors are Herb Sutter (long-term WG21 leadership) and Glen Joseph Fernandes (Boost contributor, original Boost implementation author). No apparent corporate agenda. The proposal consolidates work from multiple independent contributors (Fernandes P3234R1, Dusíková P3852R0).

**Evidence cited:** Section 4 acknowledgments. "The parallel proposal [P3234R1] by Glen Fernandes is merged into this paper."

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria defined. No adoption targets. No retrospective plan. No mechanism for gathering usage data post-standardization.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Clear, focused proposal. Design decisions documented (§2.1 on span vs. raw pointers, §2.2 on naming). Merges parallel proposals (P3234R1, P3852R0) rather than competing indefinitely. Targeted audience specified (LEWG, EWG).

**Evidence cited:** Section 2 "Discussion" covers design decisions with rationale.

---

### 10. Practical Usability — ✅

**Score: 2/2**

Simple API: `is_pointer_in_range(ptr, span)`. The span signature is type-safe and prevents argument ordering errors (explicitly discussed in §2.1). Gradual adoption possible. Makes user code correct where it was previously relying on UB.

**Evidence cited:** "Call sites that have three pointers can conveniently write is_pointer_in_range(ptr, {begin, end})"

---

### 11. Safety & Stability — ✅

**Score: 2/2**

Explicitly addresses safety: enables bounds checking for CWE Top 25 vulnerabilities (out-of-bounds read/write). The function is `constexpr` and `noexcept`. No ABI concerns (new function). Replaces UB-reliant code with defined behavior.

**Evidence cited:** "pointer bounds checking which helps improve two vulnerability root causes perennially in the 'Top 10 most dangerous software weaknesses' lists"

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

Clear rationale: this **cannot** be an ecosystem solution because it requires compiler intrinsics for correctness. The paper explicitly shows that all current ecosystem implementations rely on unspecified behavior. Standardization is the only path to correct implementation.

**Evidence cited:** Section 2.3 shows implementation requires `__builtin_pointers_related`. "The current implementations rely on techniques such as §1.5 that rely on unspecified behavior"

---

### 13. Expert Weighting — ✅

**Score: 2/2**

Extensive expert acknowledgments: Howard Hinnant, Peter Dimov, Daveed Vandevoorde, Jonathan Wakely, Tim Song, Jens Maurer, Richard Smith, Tony Van Eerd, Ville Voutilainen, and others. Implementation by Hana Dusíková with Clang prototype. CWG mailing list discussion involvement.

**Evidence cited:** Section 4 lists 20+ acknowledged experts including major library implementers.
