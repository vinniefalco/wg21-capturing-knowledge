# Evaluation: P0214R9 — Data-Parallel Vector Types & Operations

**Paper:** P0214R9  
**Title:** Data-Parallel Vector Types & Operations  
**Authors:** Matthias Kretz  
**Link:** [https://wg21.link/P0214R9](https://wg21.link/P0214R9)  
**Revision Date:** 2018-03-16  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
The paper addresses a fundamental coordination failure: "C++ has no means to use SIMD operations directly." All vendor-provided SIMD intrinsics are "inherently not portable." This makes portable SIMD programming currently *impossible* without standardization—a clear "make the impossible possible" case.

**G1. Why not third-party?** ✅ PASS  
While the author's Vc library exists as a third-party solution, the paper documents that vendor intrinsics are "very directly bound to a specific instruction" and non-portable. A third-party library cannot guarantee cross-vendor ABI compatibility or integrate with compiler optimization pipelines the way a standard type can. The ABI tag design (Section 5.1.2.1) specifically addresses cross-TU portability that third parties cannot ensure.

**G2. Perpetual costs acknowledged?** ⚠️ PARTIAL  
The paper extensively discusses implementation-relevant concerns (ABI tags, conversion semantics, alignment requirements) and acknowledges vendor implementation differences. However, explicit quantification of perpetual costs to implementers is limited. The extensive LEWG/SG1 review history and multiple revisions suggest ongoing committee investment awareness.

**Gate Result:** ✅ PROCEED TO EVALUATION

---

🟢 PASS: Well-justified vocabulary type for portable SIMD with extensive field experience and committee review through 9 revisions.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 1 | ⚠️ |
| 3. Vocabulary Necessity | 2 | ✅ |
| 4. External Validation | 1 | ⚠️ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 2 | ✅ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 2 | ✅ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **22/26** | Library threshold: 14 ✅ |

## Summary Exposition

P0214R9 is a mature, well-designed proposal that addresses a genuine gap in C++: portable access to SIMD operations. The paper correctly identifies that without standardization, developers must choose between (1) non-portable vendor intrinsics tied to specific instruction sets, (2) hoping the compiler auto-vectorizes correctly, or (3) writing assembly. This is a textbook "make the impossible possible" case—portable SIMD abstraction *cannot* be achieved through third-party libraries because ABI compatibility and compiler integration require standardization.

The proposal's strengths are substantial: nine revisions incorporating extensive LEWG and SG1 feedback, a production-quality reference implementation (the Vc library backed by the author's PhD research), comprehensive wording, and careful attention to real-world concerns like ABI compatibility across translation units. The changelog documents hundreds of design decisions refined through committee review, demonstrating exemplary process discipline. The inclusion of concrete code examples (Section 4) and thorough discussion of design tradeoffs (Section 7) shows mature, use-case-driven development.

The primary gap is the absence of explicit retrospective commitments—no success criteria or post-adoption measurement plan is defined. Additionally, while external validation through committee process is strong, named external users beyond the author's institution would strengthen the case. These are minor concerns for a proposal at R9 targeting a TS, where the TS itself serves as a validation mechanism.

## Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption review mechanism defined

No other red flags identified.

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with motivation (Section 3) explaining the problem space before presenting concrete usage examples. Section 4 provides a complete, compilable loop vectorization example demonstrating SIMD loads, operations, write-masking, and stores. The design clearly emerged from use-cases—the extensive changelog shows refinements driven by practical concerns (e.g., "Removed immutable masked load. Requested in LWG review session because it's too clever").

**Evidence cited:** Section 4 example shows idiomatic usage:
```cpp
using floatv = native_simd<float>;
floatv v(&data[i], vector_aligned);
where(v > 100.f, v) = 100.f + (v - 100.f) * 0.1f;
v.copy_to(&data[i], vector_aligned);
```

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper acknowledges implementation complexity through detailed discussion of ABI tag semantics, conversion rules, and vendor-specific considerations. The discussion of `max_fixed_size` (Section 7.11) shows awareness of implementer burden. However, explicit quantification of perpetual costs—implementation burden estimates, interaction surface analysis, or defect resolution commitments—is not present. The targeting of Parallelism TS 2 (rather than the IS) provides a validation buffer.

**Evidence cited:** "An implementation can choose to forego ABI compatibility between differently compiled translation units for simd and simd_mask specializations" ([simd.abi] para 4 note) acknowledges implementer flexibility needs.

---

### 3. Vocabulary Necessity — ✅

**Score: 2/2**

SIMD types are genuinely vocabulary types—they must cross library boundaries for any meaningful SIMD ecosystem to develop. The paper correctly identifies that vendor intrinsics are "inherently not portable" and that "different SIMD register sizes" and "different microarchitectures" require a standard abstraction. The ABI tag system is specifically designed to enable safe cross-TU communication of SIMD types.

**Evidence cited:** Section 3.2: "Thus, a data-parallel type (SIMD type) can provide the necessary interface for writing software that can utilize data-parallel hardware efficiently. Higher-level abstractions can be built on top of these types." This explicitly positions `simd` as foundation vocabulary for the ecosystem.

---

### 4. External Validation — ⚠️

**Score: 1/2**

Extensive committee validation through SG1 and LEWG straw polls is documented (Section 2), showing strong internal demand. The acknowledgements cite GSI Helmholtzzentrum für Schwerionenforschung as the institutional supporter. However, named external users beyond the author's institution are not cited. The paper would benefit from testimonials from production deployments outside academia.

**Evidence cited:** Section 2 documents 20+ straw polls from Chicago 2013 through Jacksonville 2018, showing sustained committee interest. LEWG Toronto 2017: "Poll: Forward to LWG for TS — SF:11 F:2 N:0 A:0 SA:0"

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

The author has developed the Vc library over many years, backed by a PhD thesis ([1] in bibliography). The changelog references "my reference implementation" multiple times, and design decisions are informed by implementation experience. The thesis citation indicates academic rigor. Multiple years of development and nine paper revisions demonstrate iterative refinement based on real usage.

**Evidence cited:** Bibliography [1]: "Matthias Kretz. 'Extending C++ for Explicit Data-Parallel Programming via SIMD Vector Types.' Frankfurt (Main), Univ. PhD thesis. 2015." Also: "I verified the change in my implementation" (R8 changelog).

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal is comprehensive and usable out-of-box: `simd` and `simd_mask` class templates, load/store operations, arithmetic operators, comparison operators, reductions (`reduce`, `hmin`, `hmax`), algorithms (`min`, `max`, `clamp`), casts (`simd_cast`, `split`, `concat`), and math library integration. No "ecosystem will provide" dependencies exist.

**Evidence cited:** Section 5.1.2 synopsis spans 4 pages covering all operations needed for practical SIMD programming. "The header `<experimental/simd>` defines class templates, tag types, trait types, and function templates for element-wise operations on data-parallel objects."

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

The author (academic researcher at GSI) has demonstrated multi-year commitment through PhD research, the Vc library, and nine paper revisions spanning 2016-2018. The proposal serves broad community needs (any developer wanting portable SIMD), not narrow corporate interests. Committee co-evolution through LEWG/SG1 ensures diverse stakeholder input.

**Evidence cited:** Acknowledgements: "This work was supported by GSI Helmholtzzentrum für Schwerionenforschung and the Hessian LOEWE initiative." The academic context and public library development indicate community-oriented incentives.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria, adoption targets, or retrospective analysis plans are defined. The paper does not specify how adoption will be measured or what would constitute success. For a TS-targeted proposal, the TS feedback mechanism provides implicit validation, but explicit metrics would strengthen confidence.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Exemplary process discipline: nine revisions from R0 (2016) to R9 (2018), clear target (Parallelism TS 2), extensive changelog documenting every design decision, multiple committee reviews with recorded straw polls. The paper moves steadily toward completion rather than churning indefinitely.

**Evidence cited:** Section 1 changelog spans 13 pages documenting evolution. Section 2 documents straw polls from Chicago 2013 through Jacksonville 2018. Paper explicitly states "Target: Parallelism TS 2" in header.

---

### 10. Practical Usability — ✅

**Score: 2/2**

User code is demonstrably simpler than alternatives. The Section 4 example shows clean, readable SIMD code versus the alternative (vendor intrinsics or manual loop management). The `where()` syntax for masking is intuitive. Type aliases (`native_simd<T>`, `fixed_size_simd<T, N>`) provide progressive complexity.

**Evidence cited:** Section 4 example compiles and is readable. Discussion in 7.6 shows user-centric thinking: "Consider that write-masked assignment is used as a replacement for if-statements. Using void as return type therefore is a more fitting choice because if-statements have no return value."

---

### 11. Safety & Stability — ✅

**Score: 2/2**

Extensive ABI analysis throughout—the ABI tag system is a central design feature enabling safe cross-TU communication. The paper explicitly addresses what happens with unsupported template combinations (deleted constructors), alignment requirements, and conversion safety. Future evolution is enabled through extended ABI tags.

**Evidence cited:** [simd.overview]: "If simd<T, Abi> is not supported, the specialization shall have a deleted default constructor, deleted destructor, deleted copy constructor, and deleted copy assignment." Section 7.7 extensively discusses ABI implications and future-proofing.

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

The paper directly addresses why ecosystem solutions are insufficient: "All compiler vendors... add intrinsics support... These intrinsics are inherently not portable." The proposal solves a coordination failure that cannot be solved by third parties because portable ABI requires standard agreement. Section 7.8 discusses compatibility with implementation-defined SIMD extensions.

**Evidence cited:** Section 3.3: "C++ has no means to use SIMD operations directly. There are indirect uses through automatic loop vectorization or optimized algorithms... All compiler vendors add intrinsics support... These intrinsics are inherently not portable and most of the time very directly bound to a specific instruction."

---

### 13. Expert Weighting — ✅

**Score: 2/2**

The author has a PhD specifically on this topic and has implemented a production library. The proposal has been reviewed by LEWG and SG1 over five years. Named reviewers include Jens Maurer (extensive standards experience), Geoffrey Romer (wording review), and multiple LWG members (Alisdair Meredith, Benjamin Craig, et al.). Design authority is clear (Matthias Kretz).

**Evidence cited:** Acknowledgements list domain experts. Bibliography [1] is author's PhD thesis on the topic. Changelog shows Jens Maurer presented in Kona 2017 and Toronto 2017, indicating deep expert engagement.

---

## Conclusion

P0214R9 represents a model library proposal: it addresses a genuine capability gap (portable SIMD), provides extensive field experience through the Vc library and PhD research, demonstrates exemplary process discipline through nine revisions, and carefully considers implementation concerns. The only notable gap is the absence of explicit retrospective commitments, which is mitigated by the TS feedback mechanism. This proposal clears the standardization bar convincingly.
