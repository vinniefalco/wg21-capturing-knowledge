# Evaluation: P0843R10 — `inplace_vector`

**Paper:** P0843R10  
**Title:** `inplace_vector` — A dynamically-resizable vector with fixed capacity and embedded storage  
**Authors:** Gonzalo Brito Gadeschi, Timur Doumler, Nevin Liber, David Sankel  
**Link:** [https://wg21.link/P0843R10](https://wg21.link/P0843R10)  
**Revision Date:** 2024-02-12  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ⚠️ WEAK PASS  
The paper explicitly cites "prior art in boost::static_vector and EASTL" as justification—which is the "multiple implementations exist" pattern that signals ecosystem success, not failure. However, a stronger argument exists: the C++ standard provides **no dynamically-sized sequence container for environments without dynamic allocation**. `std::array` is fixed-size; `std::vector` requires allocation. Freestanding/embedded users have no standard solution.

**G1. Why not third-party?** ⚠️ WEAK PASS  
The paper states "we believe it will be very useful to expose it as part of the C++ standard library, which will enable it to be used as a vocabulary type." This asserts vocabulary necessity without documenting specific interoperability harm. Third-party solutions (Boost.Container) work. However, for cross-library API boundaries in embedded/safety-critical domains where allocation is prohibited, incompatible types create genuine friction.

**G2. Perpetual costs acknowledged?** ✅ PASS  
Extensive design analysis across 10 revisions covering exception safety, move semantics, allocator awareness, triviality requirements, fallible APIs, and iterator invalidation. The changelog documents LEWG feedback incorporation. Implementation based on battle-tested Boost.Container and libc++ code.

**Gate Result:** ✅ PROCEED TO EVALUATION (with reservations on G0/G1)

---

🟡 CONCERNS: Useful container with extensive field experience, but standardization justification relies on "vocabulary type" assertion without documented coordination failures. The stronger argument (no standard container for freestanding) is underemphasized.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 1 | ⚠️ |
| 3. Vocabulary Necessity | 1 | ⚠️ |
| 4. External Validation | 2 | ✅ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 2 | ✅ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 2 | ✅ |
| 12. Ecosystem Consideration | 1 | ⚠️ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **21/26** | Library threshold: 14 ✅ |

## Summary Exposition

P0843R10 proposes `inplace_vector`, a container that fills a genuine gap in the standard library: there is currently no dynamically-sized sequence container that works without dynamic memory allocation. For embedded systems, real-time applications, and safety-critical software where allocation is prohibited or undesirable, users must resort to third-party implementations (Boost.Container, EASTL) or roll their own. The proposal has strong technical merit—10 revisions of careful design work, extensive exception safety analysis, and implementation based on battle-tested Boost code.

The proposal's weakness is in its standardization justification. The paper explicitly argues that "prior art in boost::static_vector and EASTL" demonstrates the need for standardization—but per the evaluation framework, multiple implementations existing is evidence the ecosystem *works*, not evidence of coordination failure. The paper asserts vocabulary type necessity ("enable it to be used as a vocabulary type") without documenting specific integration failures, bug reports, or quantified engineering costs from fragmentation. A stronger argument exists but is underemphasized: the C++ standard library provides zero dynamically-sized sequence containers for freestanding implementations.

The technical quality is high. The API mirrors `std::vector` for teachability, fallible APIs (`try_push_back`, `try_emplace_back`) address the capacity-exceeded case cleanly, and careful attention to triviality ensures the type can be used in contexts requiring trivial copyability. The acknowledgments cite Howard Hinnant (libc++), Walter Brown, Casey Carter, and Daniel Krügler—indicating serious expert review. This is a well-designed container; the question is whether the standardization bar is cleared.

## Red Flags Identified

🚩 Multiple implementations as justification — Paper cites Boost.Container and EASTL as evidence FOR standardization without documenting interoperability harm

🚩 Vocabulary assertion without evidence — "Enable it to be used as a vocabulary type" stated without documented coordination failures

🚩 No retrospective plan — No success criteria or post-adoption review mechanism defined

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The Motivation section provides clear, concrete use cases: embedded environments without free store, performance-critical code avoiding allocation overhead, real-time systems requiring deterministic latency, and cache-friendly stack allocation. The API deliberately mirrors `std::vector` for learnability. Design discussions show use-case driven refinement (e.g., fallible APIs for capacity-exceeded handling).

**Evidence cited:** "The `inplace_vector` container is useful when: memory allocation is not possible, e.g., embedded environments without a free store; memory allocation imposes an unacceptable performance penalty; deterministic latency is required, e.g., in real-time contexts."

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper extensively discusses implementation trade-offs (exception safety, triviality, allocator awareness) but does not explicitly quantify standardization costs vs. continued ecosystem distribution via Boost. The 10-revision history and detailed changelog demonstrate significant committee investment. However, explicit acknowledgment of perpetual maintenance burden is limited.

**Evidence cited:** Changelog documents LEWG feedback: "Should not be allocator aware. Should throw `bad_alloc` on exceeding capacity. Should be in a separate header." This shows implementation cost awareness through committee iteration.

---

### 3. Vocabulary Necessity — ⚠️

**Score: 1/2**

The paper asserts vocabulary type status without documenting specific coordination failures. The statement "enable it to be used as a vocabulary type" is aspirational rather than evidence-based. No bug reports, integration failures, or engineering costs from Boost/EASTL incompatibility are cited. The implicit argument—freestanding needs a standard container—is stronger but underemphasized.

**Evidence cited:** "This container is widely-used in the standard practice of C++, with prior art in, e.g., boost::static_vector<T, Capacity> or the EASTL, and therefore we believe it will be very useful to expose it as part of the C++ standard library, which will enable it to be used as a vocabulary type."

---

### 4. External Validation — ✅

**Score: 2/2**

Strong prior art: Boost.Container's `static_vector` has multi-year production deployment. EASTL (Electronic Arts STL) represents game industry validation. The extensive acknowledgments list domain experts who provided feedback. 10 revisions through LEWG/LWG demonstrate sustained committee validation.

**Evidence cited:** "This proposal is based on Boost.Container's `boost::container::static_vector`, mainly authored by Adam Wulkiewicz, Andrew Hundt, and Ion Gaztanaga." Acknowledgments cite Walter Brown, Zach Laine, Rein Halbersma, Casey Carter, Daniel Krügler.

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

Implementation is based on two production-quality sources: Boost.Container's `static_vector` (years of deployment) and Howard Hinnant's libc++ `vector` implementation. The test suite is also derived from libc++. This is not speculative design—it's standardizing proven code.

**Evidence cited:** "The reference implementation is based on Howard Hinnant `std::vector` implementation in libc++ and its test-suite."

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal is comprehensive: full container requirements compliance, range construction/assignment, fallible APIs (`try_push_back`, `try_emplace_back`), unchecked APIs for performance, erasure functions, zero-sized specialization behavior, and feature test macro. Users can immediately use this as a drop-in where `std::vector` was previously used.

**Evidence cited:** Technical specification covers all standard container sections: constructors, capacity, data access, modifiers, erasure, comparisons, specializations, and version.syn integration.

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

Authors represent diverse organizations: David Sankel (Adobe), Timur Doumler (audio industry), Gonzalo Brito Gadeschi (NVIDIA, per other papers), Nevin Liber (Argonne National Laboratory). This cross-industry authorship suggests broad community benefit rather than narrow corporate interest. The container serves genuinely universal needs (embedded, real-time, games).

**Evidence cited:** Author affiliations span multiple industries. The use cases (embedded, real-time, games) are domain-agnostic.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria, adoption targets, or retrospective analysis plans are defined. The paper does not specify how success will be measured or who will evaluate adoption post-standardization.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Exemplary process discipline: 10 revisions from R0 through R10 with detailed changelog documenting every design decision. Clear progression through LEWG to LWG. The naming evolution (`fixed_capacity_vector` → `static_vector` → `inplace_vector`) shows responsive iteration to feedback.

**Evidence cited:** Changelog documents revision history from R1 through R10 with specific LEWG guidance incorporated at each stage (Kona 2022, Varna 2023, etc.).

---

### 10. Practical Usability — ✅

**Score: 2/2**

The API deliberately mirrors `std::vector` for immediate familiarity. Users already know how to use this container. The addition of fallible APIs (`try_push_back` returning `T*`) provides clean handling of the capacity-exceeded case that `std::vector` doesn't face. Gradual adoption is trivial—replace `std::vector<T>` with `inplace_vector<T, N>` where appropriate.

**Evidence cited:** Design section "Summary of semantic differences with vector" explicitly documents the minimal delta from familiar `std::vector` semantics.

---

### 11. Safety & Stability — ✅

**Score: 2/2**

Exception safety is analyzed in depth with dedicated subsections. The decision to throw `bad_alloc` on capacity exceeded (rather than UB) prioritizes safety. Fallible APIs (`try_push_back`) provide non-throwing alternatives. Triviality requirements are carefully specified. The design explicitly addresses move semantics and iterator invalidation.

**Evidence cited:** "Exception Safety guarantees of Mutating Operations" and "Exception thrown by mutating operations exceeding capacity" sections. LEWG polls recorded on exception behavior.

---

### 12. Ecosystem Consideration — ⚠️

**Score: 1/2**

The paper acknowledges Boost.Container as prior art but does not analyze why continued ecosystem distribution is insufficient. The implicit argument is "vocabulary type," but this isn't substantiated with coordination failure evidence. The freestanding argument (no standard container for allocation-free environments) is more compelling but less emphasized.

**Evidence cited:** Prior art acknowledged: "boost::static_vector<T, Capacity> [1] or the EASTL [2]." Analysis of why standardization specifically (vs. continued Boost use) is necessary is limited.

---

### 13. Expert Weighting — ✅

**Score: 2/2**

Implementation based on Howard Hinnant's libc++ code. Acknowledgments cite major library experts: Walter Brown, Casey Carter, Daniel Krügler (wording review). Original Boost.Container authors (Adam Wulkiewicz, Andrew Hundt, Ion Gaztanaga) provided the foundation. Extensive LEWG/LWG review over 10 revisions.

**Evidence cited:** "The reference implementation is based on Howard Hinnant `std::vector` implementation in libc++ and its test-suite... Many thanks to Daniel Krügler for reviewing the wording."

---

## Conclusion

P0843R10 is a technically excellent proposal standardizing a well-understood, widely-deployed container. The primary concern is not the container itself—it's the standardization justification. The paper relies on the "multiple implementations exist, therefore standardize for vocabulary" argument, which the evaluation framework explicitly flags as insufficient without documented coordination harm. The stronger argument—that the C++ standard provides no dynamically-sized sequence container for freestanding/embedded environments—exists but is underemphasized. Given the 10 revisions of committee review and the clear utility of the container, this will likely proceed, but future vocabulary type proposals should document specific interoperability failures rather than asserting vocabulary necessity.
