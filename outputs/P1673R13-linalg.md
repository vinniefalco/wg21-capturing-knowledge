# Evaluation: P1673R13 — A free function linear algebra interface based on the BLAS

**Paper:** P1673R13  
**Title:** A free function linear algebra interface based on the BLAS  
**Authors:** Mark Hoemmen (NVIDIA), Daisy Hollman, Christian Trott (Sandia), Daniel Sunderland, Nevin Liber (Argonne), Alicia Klinvex (UNNPP), Li-Ta Lo (LANL), Damien Lebrun-Grandie (ORNL), Graham Lopez (NVIDIA), Peter Caday (Intel), Sarah Knepper (Intel), Piotr Luszczek (UTK), Timothy Costa (NVIDIA)  
**Link:** [https://wg21.link/P1673R13](https://wg21.link/P1673R13)  
**Revision Date:** 2023-11-10  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
The BLAS (Basic Linear Algebra Subprograms) is a de facto standard interface from the 1970s-80s that hardware vendors (Intel MKL, NVIDIA cuBLAS, AMD rocBLAS) have optimized for decades. C++ lacks a standard way to access these optimized implementations. Every scientific computing project creates its own wrapper, preventing: (1) portable code across vendors, (2) seamless hardware acceleration, and (3) integration with `mdspan` (now standard). This is not "multiple implementations exist"—this is "a hardware interface standard exists that C++ cannot portably use."

**G1. Why not third-party?** ✅ PASS  
Third-party libraries (Eigen, Blaze, Armadillo) provide linear algebra, but they cannot: (1) integrate with `std::mdspan` as vocabulary type, (2) enable vendor-optimized BLAS implementations through a standard interface, (3) support execution policies for heterogeneous execution (GPU). The paper explicitly builds on `mdspan` (P0009), making this a natural extension of already-standardized infrastructure.

**G2. Perpetual costs acknowledged?** ✅ PASS  
Extensive design analysis across 13 revisions. Section 9 explicitly documents exclusions (LAPACK, tensors, banded matrices, expression templates) to limit scope. Interaction with `mdspan` is thoroughly analyzed. Authors from major implementers (NVIDIA, Intel, national labs) indicate vendor commitment to implementation.

**Gate Result:** ✅ PROCEED TO EVALUATION

---

🟢 PASS: Exceptionally well-justified proposal bringing the 40-year BLAS standard into modern C++, with cross-organizational authorship from major hardware vendors and national laboratories.

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
| **TOTAL** | **23/26** | Library threshold: 14 ✅, Major feature: 22 ✅ |

## Summary Exposition

P1673R13 represents the gold standard for how to propose a major library feature. The BLAS (Basic Linear Algebra Subprograms) is a 40+ year old interface standard that hardware vendors have optimized relentlessly. Intel MKL, NVIDIA cuBLAS, AMD rocBLAS, and other vendor libraries implement this interface with hand-tuned assembly, SIMD intrinsics, and GPU kernels. C++ currently has no portable way to access these implementations—every project creates its own wrapper, every vendor provides its own C++ layer, and interoperability is impossible. This proposal standardizes the interface that the hardware world already agrees on.

The authorship is remarkable: 13 authors from NVIDIA (3), Intel (2), Sandia National Labs (2), Oak Ridge National Lab, Los Alamos National Lab, Argonne National Lab, and the University of Tennessee at Knoxville (home of the original BLAS/LAPACK). This cross-organizational, multi-vendor collaboration provides strong evidence of broad community need and commitment to implementation. The proposal builds on `mdspan` (already standardized), uses execution policies (already standardized), and provides a natural vocabulary type for passing matrices between libraries.

The proposal's discipline is exemplary: 13 revisions with detailed changelogs, explicit exclusions (LAPACK, tensors, expression templates, banded matrices) to limit scope, thorough design justifications (58+ pages of content), and production-quality examples including complete Cholesky factorization and QR algorithms. The only gap is the absence of explicit retrospective commitments—no success metrics are defined. However, for a feature this fundamental to scientific computing, success measurement is straightforward: adoption in scientific libraries and integration with vendor BLAS implementations.

## Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption review mechanism defined

No other red flags identified.

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

Section 29 provides three complete, compilable examples: Cholesky factorization, solving linear systems via Cholesky, and QR factorization of tall-skinny matrices. These are not toy examples—they're production algorithms. The API design clearly serves practical use cases: matrix-vector products, triangular solves, symmetric rank-k updates. Section 7 explicitly discusses criteria for including algorithms.

**Evidence cited:** Section 29.1 Cholesky factorization example: "This example shows how to compute the Cholesky factorization of a real symmetric positive definite matrix A stored as an `mdspan` with a unique non-packed layout. The algorithm imitates `DPOTRF2` in LAPACK 3.9.0."

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper extensively documents design trade-offs and explicit exclusions (Section 9), showing awareness of scope management. However, explicit quantification of perpetual implementation costs is limited. The multi-vendor authorship implicitly suggests vendor commitment, but no explicit implementation burden estimates are provided. The 13-revision history and extensive LEWG review demonstrate substantial committee investment awareness.

**Evidence cited:** Section 9 "What we exclude from the design" documents: LAPACK, Extended-precision BLAS, Arithmetic operators/expression templates, Banded matrix layouts, Tensors, Explicit asynchronous support.

---

### 3. Vocabulary Necessity — ✅

**Score: 2/2**

This builds on `mdspan` (P0009), already standardized as a vocabulary type for multidimensional arrays. Linear algebra operations on `mdspan` are the natural completion of that vocabulary. The BLAS is *already* the vocabulary standard for linear algebra interfaces—hardware vendors, scientific libraries, and numerical software all speak BLAS. C++ is simply adopting this existing vocabulary.

**Evidence cited:** Section 10.2 "Why use mdspan?" discusses: "View of a multidimensional array," "Ease of use," "BLAS and mdspan are low level," "Hook for future expansion," "Generic enough to replace a 'multidimensional array concept'."

---

### 4. External Validation — ✅

**Score: 2/2**

Authorship from NVIDIA, Intel, Sandia National Labs, Oak Ridge National Lab, Los Alamos National Lab, Argonne National Lab, and University of Tennessee (BLAS/LAPACK birthplace) represents extraordinary cross-organizational validation. These are the institutions that *define* high-performance linear algebra. The proposal has been through 13 revisions with LEWG/SG6 review.

**Evidence cited:** Author list includes: Mark Hoemmen (NVIDIA), Christian Trott (Sandia), Nevin Liber (Argonne), Li-Ta Lo (LANL), Damien Lebrun-Grandie (ORNL), Peter Caday (Intel), Sarah Knepper (Intel), Piotr Luszczek (UTK).

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

The BLAS itself has 40+ years of implementation experience. Modern C++ implementations exist in Kokkos Kernels (Sandia), which informed this proposal. The design explicitly supports "hooking in" optimized vendor implementations (Intel MKL, NVIDIA cuBLAS). Section 13 discusses implementation experience (truncated in search results).

**Evidence cited:** Section 10.1: "We do not require using the BLAS library or any particular 'back-end'." This indicates the design supports both portable implementation and vendor-optimized backends.

---

### 6. Completeness — ✅

**Score: 2/2**

Comprehensive coverage of BLAS Level 1 (vector operations), Level 2 (matrix-vector), and Level 3 (matrix-matrix) operations. The proposal is immediately usable for matrix multiplication, triangular solves, symmetric rank updates, and more. Section 9 explicitly documents what's *out* of scope, preventing scope creep while ensuring completeness for the defined mission.

**Evidence cited:** Table of contents shows coverage: vector norms, matrix-vector products, triangular solves, symmetric/Hermitian operations, rank-k updates, matrix-matrix products. Section 29 examples demonstrate complete algorithms.

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

Multi-vendor authorship (NVIDIA, Intel) with national laboratory backing (Sandia, ORNL, LANL, Argonne) represents aligned incentives: hardware vendors want a standard interface for their optimized BLAS implementations, and national labs want portable high-performance code. No single company dominates. The scientific computing community as a whole benefits.

**Evidence cited:** 13 authors from 8+ organizations, including competing hardware vendors (NVIDIA, Intel) cooperating on a shared interface.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No explicit success criteria, adoption targets, or retrospective analysis plans are defined. The paper does not specify how success will be measured or who will evaluate adoption post-standardization. For a feature this major, explicit commitment to post-adoption evaluation would strengthen the proposal.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Exemplary process: 13 revisions (R0→R13) with Section 2 providing detailed revision history. Clear progression through SG6 (numerics), SG1 (concurrency), and LEWG. The paper explicitly addresses feedback from each review cycle. The proposal does not churn indefinitely—it progresses toward completion.

**Evidence cited:** Section 2 "Revision history" documents changes from R0 through R13, including LEWG and SG6 feedback responses.

---

### 10. Practical Usability — ✅

**Score: 2/2**

The API uses `mdspan` for matrices/vectors (already standardized), making it immediately familiar to users of modern C++. The examples in Section 29 demonstrate clean, readable code for complex algorithms (Cholesky, QR). The free function interface follows BLAS conventions that numerical programmers already know.

**Evidence cited:** Section 29 examples show clean usage:
```cpp
symmetric_matrix_rank_k_update(ONE, transposed(A_cur), R, upper_triangle);
triangular_matrix_matrix_left_solve(R, upper_triangle, A);
```

---

### 11. Safety & Stability — ✅

**Score: 2/2**

Section 10.3 discusses function argument aliasing and zero scalar multipliers. Section 10.8 extensively analyzes "Constraining matrix and vector element types and scalars" with subsections on associativity, semirings, and algorithm behavior. Section 10.9 addresses `complex` issues and user-defined complex types. Execution policies enable future GPU/heterogeneous support.

**Evidence cited:** Section 10.8.6 "Properties of textbook algorithm descriptions," Section 10.8.7 "Reordering sums and creating temporaries," Section 10.8.8 "'Textbook' algorithm description in semiring terms."

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

Section 5 "Why include dense linear algebra in the C++ Standard Library?" directly addresses standardization justification. Section 6 "Why base a C++ linear algebra library on the BLAS?" explains the choice of interface. The paper explicitly builds on the existing BLAS ecosystem rather than replacing it—implementations can delegate to vendor BLAS for performance.

**Evidence cited:** Section 10.1: "We do not require using the BLAS library or any particular 'back-end'" enables coexistence with existing optimized implementations.

---

### 13. Expert Weighting — ✅

**Score: 2/2**

Authors include world-leading experts in high-performance linear algebra: Piotr Luszczek (University of Tennessee, home of BLAS/LAPACK), Christian Trott (Kokkos lead, Sandia), Mark Hoemmen (NVIDIA, former Sandia), Sarah Knepper (Intel MKL). These are the people who *write* production linear algebra libraries. SG6 (numerics) review ensures domain expert validation.

**Evidence cited:** Piotr Luszczek (UTK) is from the institution that created BLAS and LAPACK. Christian Trott leads Kokkos. Multiple authors have decades of numerical computing experience at national laboratories.

---

## Conclusion

P1673R13 is a model proposal for bringing established domain standards into C++. The BLAS is not a "new idea"—it's a 40-year-old interface that hardware vendors have optimized relentlessly. This proposal does not ask the committee to validate a novel design; it asks the committee to adopt an interface that the numerical computing world has already validated through decades of production use. The cross-organizational authorship from competing vendors and national laboratories provides extraordinary confidence in both the design and the commitment to implementation. The only gap—lack of explicit retrospective commitment—is a systemic WG21 issue rather than a specific weakness of this proposal.
