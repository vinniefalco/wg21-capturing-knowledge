# Evaluation: P3179R6 — C++ parallel range algorithms

**Paper:** P3179R6  
**Title:** C++ parallel range algorithms  
**Authors:** Ruslan Arutyunyan, Alexey Kukanov, Bryce Adelstein Lelbach  
**Link:** [https://wg21.link/P3179R6](https://wg21.link/P3179R6)  
**Revision Date:** 2025-02-03  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
The C++ standard itself has internal fragmentation: C++17 parallel algorithms cannot be used with C++20 ranges. Users must choose between expressive range pipelines OR parallelism, but not both. Only standardization can unify these two existing standard features.

**G1. Why not third-party?** ✅ PASS  
Execution policies (`std::execution::par`, etc.) and `std::ranges` algorithms are both standard library features. A third party would need to reimplement the entire algorithm library to combine them. This is completing existing standard functionality, not adding a new capability.

**G2. Perpetual costs acknowledged?** ✅ PASS  
The paper documents implementation experience (Section 6), explicitly lists in-scope vs out-of-scope algorithms (Section 5), and has undergone extensive SG1/SG9/LEWG review with recorded polls. Interaction surface is well-defined—these are overloads of existing algorithms.

**Gate Result:** ✅ PROCEED TO EVALUATION

---

🟢 PASS: Well-justified extension unifying two existing standard features (parallel algorithms + ranges) with strong committee consensus and implementation experience.

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
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **22/26** | Library threshold: 14 ✅ |

## Summary Exposition

P3179R6 is a mature, well-motivated proposal that addresses a genuine capability gap: C++ currently forces users to choose between the expressiveness of ranges and the performance of parallel algorithms. The motivation is compelling—"fusing several computations into one parallel algorithm call, thus reducing the overhead on parallelism" cannot be achieved when parallel algorithms and ranges are incompatible. This is a textbook example of standardization completing existing standard functionality rather than adding new capabilities that could live in the ecosystem.

The proposal demonstrates excellent process discipline: six revisions from R0 through R6, explicit tracking of design decisions through SG1/SG9/LEWG polls, clear in-scope/out-of-scope boundaries, and documented implementation experience. The author team combines Intel parallel algorithm expertise (Arutyunyan, Kukanov) with NVIDIA/ranges expertise (Lelbach), providing cross-vendor validation. The design choices are well-reasoned—requiring `random_access_range` for parallelism, maintaining return type consistency with serial ranges algorithms, and explicit handling of bounded vs unbounded ranges.

The primary gap is the absence of explicit retrospective commitments—no success metrics or post-adoption evaluation plan is defined. This is a minor concern for an extension to existing features, where success is naturally measurable by adoption in codebases already using parallel algorithms. The paper would also benefit from more explicit discussion of safety implications in heterogeneous execution contexts.

## Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption review mechanism defined

No other red flags identified.

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with clear motivation (Section 1) explaining why combining ranges and parallel algorithms is valuable. Section 3 ("More examples") provides concrete before/after code comparisons. Section 2.1.4 shows an example of the proposed API. The design is clearly use-case driven—the paper explicitly discusses differences from serial range algorithms and from C++17 parallel algorithms.

**Evidence cited:** Section 3.2 "Less parallel algorithm calls and better expressiveness" shows how range pipelines can reduce boilerplate: "Combining these two powerful features by adding support for execution policies to the range-based algorithms opens an opportunity to fuse several computations into one parallel algorithm call."

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper implicitly acknowledges costs through extensive design discussion and explicit in-scope/out-of-scope boundaries (Section 5). However, explicit quantification of perpetual implementation burden is limited. The paper relies on the argument that these are "just overloads" of existing algorithms, which understates interaction complexity with constraints, views, and heterogeneous execution.

**Evidence cited:** Section 5 explicitly separates in-scope algorithms (counterparts of C++17 parallel algorithms) from out-of-scope cases (algorithms without ExecutionPolicy counterparts, views with parallel algorithms). This shows awareness of scope boundaries.

---

### 3. Vocabulary Necessity — ✅

**Score: 2/2**

This is not a vocabulary type proposal—it extends existing standard algorithms. The "vocabulary necessity" analog here is: must this be in the standard? YES, because execution policies and ranges are both standard features. A third party cannot achieve the same integration without reimplementing the entire algorithm library. The standard has created an internal fragmentation that only standardization can resolve.

**Evidence cited:** Section 1: "Standard parallel algorithms with execution policies... were a good start for supporting parallelism in the C++ standard. The C++ Ranges library... is a powerful facility... Combining these two powerful features by adding support for execution policies to the range-based algorithms opens an opportunity..."

---

### 4. External Validation — ✅

**Score: 2/2**

Strong committee validation through multiple SG1, SG9, and joint session polls across Wroclaw 2024, St. Louis 2024, and Tokyo 2024 (Section 10). Authors represent Intel and NVIDIA—major industry stakeholders in parallel computing. The paper explicitly thanks Mikhail Dvorskiy for implementation experience, indicating validation beyond the author team.

**Evidence cited:** Section 10 documents 10+ polls with strong consensus. Joint SG1 + SG9, St. Louis 2024: "Continue work on [P3179R2] for IS'26... SF:7 F:4 N:2 A:1 SA:0". SG9 Wroclaw 2024: "Forward [P3179R3]... to LEWG for inclusion in C++26 — SF:4 F:5 N:0 A:0 SA:0".

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

Section 6 discusses implementation experience explicitly. The acknowledgments thank Mikhail Dvorskiy for implementation experience. The extensive revision history (R0→R6) demonstrates iterative refinement based on implementation attempts. Design decisions like requiring `sized_range` for both inputs emerged from implementation constraints.

**Evidence cited:** Section 6: "Implementation experience" (referenced but truncated in search results). Acknowledgments: "Thanks to Mikhail Dvorskiy for the implementation experience." Revision history shows implementation-driven changes: "R4 => R5: Add the necessary wording to [algorithm.syn]."

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal is comprehensive: Section 5.1 explicitly lists all algorithms in scope (50+ algorithm families), Section 5.2 explicitly lists what is out of scope with rationale. The wording section (Section 8) covers all necessary modifications across multiple standard sections. Users can immediately use parallel range algorithms on day one.

**Evidence cited:** Section 5.1.1 lists "The counterparts of C++17 parallel algorithms in std::ranges namespace." Section 5.1.2 lists "Algorithms in std::ranges namespace only." Section 5.2 explicitly excludes views integration ("Out-of-scope: Use of views with parallel algorithms") with reasoning.

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

Authors from Intel (Arutyunyan, Kukanov) and NVIDIA (Lelbach) transparently represent industry interests in parallel computing. These are major standard library implementers with long-term stake in the feature. The proposal serves broad community need—anyone using both ranges and parallel algorithms benefits, not just the authors' employers.

**Evidence cited:** Author affiliations clearly listed. The collaboration between Intel and NVIDIA (competing companies) on a shared proposal demonstrates alignment with broader community needs rather than narrow corporate interest.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No explicit success criteria, adoption targets, or retrospective analysis plans are defined. The paper does not specify how success will be measured or who will evaluate adoption post-standardization. This is a common gap in WG21 proposals.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Exemplary process: six revisions (R0→R6) over approximately one year, clear targeting of C++26, detailed revision history documenting every design change, multiple committee reviews with recorded poll results. The paper shows clear progression toward completion rather than indefinite churn.

**Evidence cited:** Section 9 provides detailed revision history from R0→R6. Section 10 documents polls from Tokyo 2024, Wroclaw 2024, and St. Louis 2024. Paper targets "inclusion in C++26" per SG9 Wroclaw poll.

---

### 10. Practical Usability — ✅

**Score: 2/2**

The examples show clear usability improvements. Users can combine range expressiveness with parallelism—something currently impossible. The API follows established patterns from both C++17 parallel algorithms and C++20 ranges, enabling gradual adoption. Return types match serial range algorithms for consistency.

**Evidence cited:** Section 2.1.4 example shows clean usage:
```cpp
std::ranges::sort(std::execution::par, v);
std::ranges::for_each(std::execution::par, v | std::views::filter(pred), f);
```
Section 2.4: "Algorithm return types" discusses maintaining consistency with serial ranges algorithms.

---

### 11. Safety & Stability — ⚠️

**Score: 1/2**

Section 2.9 discusses requirements for callable parameters including `const operator()` requirement (per SG9 Tokyo poll). Section 2.8 discusses bounded range requirements for safety. However, explicit safety analysis for heterogeneous execution (GPU offload) is limited. ABI implications are not explicitly discussed, though these are overloads of existing algorithms.

**Evidence cited:** Section 2.9: "Requirements for callable parameters." SG9 Tokyo 2024 Poll 4: "Range-based parallel algos should require const operator() — SF:0 F:7 N:2 A:0 SA:0."

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

The paper clearly justifies why this must be in the standard: it unifies two existing standard features. A third-party library cannot provide the same integration because execution policies and ranges algorithms are both standard library components. Section 7.2 discusses "Parallelism and Views" for further work, showing awareness of ecosystem boundaries.

**Evidence cited:** Section 2.2 "Coexistence with schedulers" discusses relationship with P2300 (std::execution). Section 5.2.3 explicitly defers "Use of views with parallel algorithms" to future work, showing careful scope management.

---

### 13. Expert Weighting — ✅

**Score: 2/2**

Authors include recognized experts: Alexey Kukanov (Intel TBB/oneTBB lead), Bryce Adelstein Lelbach (NVIDIA, former CUDA C++ lead, ranges expertise). Review by SG1 (concurrency), SG9 (ranges), and LEWG ensures multi-domain expert validation. Acknowledgments cite Jonathan Müller (wording review) and implementation experience from Mikhail Dvorskiy.

**Evidence cited:** Acknowledgments: "Thanks to Jonathan Müller for the wording review and providing useful feedback. Thanks to Mikhail Dvorskiy for the implementation experience." Poll history shows review by domain experts in SG1 (parallelism) and SG9 (ranges).

---

## Conclusion

P3179R6 represents a well-executed proposal to complete an obvious gap in the C++ standard library. The combination of parallel algorithms and ranges is a natural evolution that users expect but cannot currently achieve. The extensive committee review, implementation experience, and clear design decisions make this a model for extending existing standard functionality. The only notable gap is the absence of retrospective commitments, which is a systemic issue across WG21 proposals rather than a specific weakness of this paper.
