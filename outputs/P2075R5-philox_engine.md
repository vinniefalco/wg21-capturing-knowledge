# Evaluation: P2075R5 — Philox as an extension of the C++ RNG engines

**Paper:** P2075R5  
**Title:** Philox as an extension of the C++ RNG engines  
**Authors:** Ilya Burylov (Nvidia), Ruslan Arutyunyan (Intel), Andrey Nikolaev, Alina Elizarova (Intel), Pavel Dyakov (Intel)  
**Link:** [https://wg21.link/P2075R5](https://wg21.link/P2075R5)  
**Revision Date:** 2024-04-01  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ❌ FAIL  
Paper cites "wide usage" and lists multiple existing implementations (Intel MKL, cuRAND, rocRAND, numpy, etc.) as justification—this is evidence the ecosystem works, not evidence of coordination failure. No documented interoperability incidents, bug reports, or integration failures cited.

**G1. Why not third-party?** ❌ FAIL  
Paper does not address why existing third-party implementations are insufficient. Philox is already available via Intel MKL, cuRAND, rocRAND, numpy, and other libraries. No explanation of why these solutions create coordination problems requiring standardization.

**G2. Perpetual costs acknowledged?** ❌ FAIL  
Paper states only "This is a library-only extension" without analyzing implementation burden across vendors, interaction surface with existing `<random>` components, teaching burden, or defect resolution commitment.

**Gate Result:** ❌ AUTOMATIC FAIL — No documented coordination failure; existing ecosystem implementations demonstrate the problem is solved without standardization

---

## Guidance for Authors

This evaluation is not a judgment on whether Philox is a useful or well-designed random number engine—the extensive field experience and vendor adoption demonstrate it clearly is. The gate failure indicates that the proposal, as written, has not yet made the case for why this functionality must be in the C++ standard library rather than distributed through the ecosystem.

### What Was Missing

**G0 failed** because the paper's Section 4 (General Description) lists multiple vendors providing Philox implementations (Intel MKL, Nvidia cuRAND, AMD rocRAND, MathWorks, Microsoft DirectML, numpy, cuPy) as evidence *for* standardization. Under the evaluation framework, this proves the ecosystem works—not that standardization is needed. No specific incidents where incompatible Philox implementations caused bugs, build failures, or wasted engineering are documented.

**G1 failed** because the paper assumes standardization value without justification. The existence of high-quality, widely-deployed implementations in major vendor libraries demonstrates this functionality is available without standardization. The paper does not explain what coordination problem these existing solutions create.

**G2 failed** because Section 10 ("Impact on the Standard") states only that this is "a library-only extension" that "adds one or two new class templates." There is no analysis of:
- Implementation complexity for each major standard library vendor
- Interaction with existing `<random>` components, `<ranges>`, or future parallel algorithms
- Who will address defects discovered post-standardization
- Teaching and documentation burden

### How to Strengthen a Revision

To pass G0 (What coordination failure does this solve?), consider adding:
- **Documented interop failures**: Cite specific issues where libraries using Intel MKL's Philox could not interoperate with libraries using cuRAND's Philox
- **Vocabulary type argument**: Demonstrate that Monte Carlo libraries need to exchange Philox engines at API boundaries (not just use them internally)
- **Quantified harm**: Estimate hours wasted or projects blocked due to Philox fragmentation across vendors
- **Why ecosystem convergence failed**: If Boost or another ecosystem standard was attempted and failed, document why

**Key question to answer**: If a library needs Philox internally, it can use Intel MKL, cuRAND, or any other implementation. What specific scenario requires standardization?

To pass G1 (Why not third-party?), consider:
- **Cross-library exchange scenarios**: Demonstrate that libraries need to pass `philox_engine` objects across API boundaries, not just use them internally
- **Package manager insufficiency**: Document why vcpkg/conan distribution of a common header-only Philox library wouldn't solve the problem
- **Portable seeding/state concerns**: If the issue is reproducibility across platforms, explain why a third-party library with specified behavior wouldn't suffice

To pass G2 (Perpetual costs), consider adding:
- **Implementation analysis**: Estimate complexity for libc++, libstdc++, and MSVC STL maintainers
- **Interaction surface**: Document how `philox_engine` interacts with `std::seed_seq`, `std::random_device`, distribution types, and future parallel random facilities
- **Maintenance commitment**: State which authors or organizations will address LWG issues post-standardization
- **Teaching burden**: Acknowledge that users must now choose between `mt19937`, `minstd_rand`, and `philox4x64`

### Alternative Paths

If coordination failures are difficult to document, consider:
- **Portable ecosystem library**: Publish a header-only Philox implementation via vcpkg/conan that provides a consistent API across platforms
- **Return with evidence**: After 2-3 years, document actual coordination problems users encountered
- **Focus on vocabulary types first**: If the goal is parallel RNG standardization, consider whether `std::random_device` improvements or a `std::parallel_rng` concept would address the underlying need

### Strengths to Preserve

- **Excellent field experience**: Multiple vendor implementations with years of production use (Section 4)
- **Clean API design**: The `set_counter()` interface for parallel simulations is well-motivated (Section 8.2)
- **Rigorous statistical validation**: TestU01 BigCrush results cited with independent confirmation (Section 4)
- **Thoughtful design evolution**: R0-R5 revisions show careful consideration of API alternatives (Section 8)

---

*This feedback is generated to help improve proposals. The committee values your contribution to C++ and encourages resubmission once the standardization justification is strengthened.*

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal failed the standardization justification gate.** The detailed evaluation below is provided for reference. The primary action items are in Guidance for Authors above.

🔴 GATE FAIL: Proposal documents ecosystem success (multiple implementations) but interprets this as justification for standardization rather than evidence that standardization is unnecessary.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 1 | ⚠️ |
| 2. Economic Analysis | 0 | ❌ |
| 3. Vocabulary Necessity | 0 | ❌ |
| 4. External Validation | 1 | ⚠️ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 1 | ⚠️ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 0 | ❌ |
| 12. Ecosystem Consideration | 0 | ❌ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **13/26** | Below library threshold (14) |

**Required category minimums for library proposals (≥1):**
- Category 1 (Use-Case): 1 ✅
- Category 2 (Economic): 0 ❌
- Category 3 (Vocabulary): 0 ❌
- Category 4 (External): 1 ✅
- Category 5 (Implementation): 2 ✅
- Category 6 (Completeness): 2 ✅
- Category 10 (Usability): 2 ✅

---

## Summary Exposition

P2075R5 proposes adding the Philox counter-based random number engine to the C++ standard library. Philox is a well-established algorithm with excellent statistical properties, small state size, and strong parallelization characteristics. The paper demonstrates extensive field experience through implementations in Intel MKL, Nvidia cuRAND, AMD rocRAND, numpy, and other major libraries.

The critical gap is the absence of standardization justification. The paper's Section 4 lists seven vendors providing Philox implementations as evidence for standardization, but this actually demonstrates that the ecosystem successfully delivers this functionality without standardization. No coordination failures—bug reports where incompatible implementations caused problems, libraries that failed to interoperate, or engineering hours wasted on integration—are documented. The "vocabulary necessity" argument is implicit but unsubstantiated: if Monte Carlo libraries use Philox internally, they can depend on any ecosystem implementation.

The proposal would benefit from documenting specific scenarios where standardization provides value that ecosystem distribution cannot. If the goal is cross-platform reproducibility, a well-specified third-party library achieves this. If the goal is reducing dependencies, package managers address this. The paper should identify the specific coordination failure that only standardization can resolve.

---

## Red Flags Identified

🚩 **Multiple implementations as justification** — Section 4 cites Intel MKL, Nvidia cuRAND, AMD rocRAND, MathWorks, Microsoft DirectML, numpy, and cuPy implementations as evidence FOR standardization without documenting interoperability harm (GATE FAIL)

🚩 **No standardization justification** — Paper treats usefulness and wide adoption as sufficient justification; no cost analysis or coordination failure documented (GATE FAIL)

🚩 **Vocabulary assertion without evidence** — Implicit claim that Philox should be a vocabulary type without documenting why libraries need to exchange Philox objects at API boundaries (GATE FAIL)

🚩 **Cost blindness** — No acknowledgment of perpetual implementation/maintenance burden for three major standard library implementations (GATE FAIL)

🚩 **No retrospective plan** — No success criteria defined, no plan to evaluate adoption

🚩 **ABI silence** — No discussion of ABI implications or long-term maintenance

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ⚠️

**Score: 1/2**

Section 8.2 provides a concrete Monte Carlo simulation example showing `set_counter()` usage for parallel atom/timestep simulation. Section 3 (Motivation) discusses application domains. However, the paper opens with algorithm description rather than user-facing code examples. The use-case section is buried in "Design considerations" rather than leading the proposal.

**Evidence cited:** "The following example shows the typical flow for a Monte Carlo simulation of a large number of 'atoms' for a large number of timesteps" (Section 8.2)

---

### 2. Economic Analysis — ❌

**Score: 0/2**

No economic analysis of standardization costs. Section 10 ("Impact on the Standard") states only "This is a library-only extension" without quantifying implementation burden, interaction complexity, teaching burden, or defect resolution costs. No comparison to ecosystem distribution alternatives.

**Evidence cited:** None found

---

### 3. Vocabulary Necessity — ❌

**Score: 0/2**

No documented coordination failures. The paper lists multiple existing implementations as justification, which under the evaluation framework is evidence AGAINST standardization. No bug reports, integration failures, or interoperability incidents cited. No explanation of why libraries need to exchange Philox objects at API boundaries.

**Evidence cited:** None found—paper cites ecosystem success as justification: "The value of the Philox engine is widely recognized by various vendors, to name a few: Intel*, Nvidia*, AMD*, MathWorks*, Microsoft*..."

---

### 4. External Validation — ⚠️

**Score: 1/2**

Paper names specific application domains (Monte Carlo, financial simulations, physics) and cites academic papers demonstrating usage. However, no specific user testimonials or quantified demand ("N users requested this"). No developer survey data or StackOverflow question frequency cited.

**Evidence cited:** "Philox is broadly used in Monte-Carlo simulations... financial simulations [6], simulation of non-deterministic finite automata [7]" (Section 4)

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

Excellent implementation coverage. Multiple vendor implementations with years of production use (Intel MKL, cuRAND, rocRAND). Independent statistical validation (TestU01 BigCrush). Reference implementations on GitHub. The 10000th-value requirements demonstrate cross-implementation agreement.

**Evidence cited:** "Intel® MKL, rocRAND, cuRAND, MATLAB, etc." (Section 8.7); "TestU01 batteries for Philox4x32-10 and Philox4x32-7 were tested in [4]" (Section 4)

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal is self-contained. Predefined aliases (`philox4x32`, `philox4x64`) are usable immediately without additional ecosystem support. The engine integrates with existing `<random>` distributions. No "machinery now, types later" pattern.

**Evidence cited:** Complete class template specification with constructors, seeding, `set_counter()`, and streaming operators provided

---

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

Authors from Intel and Nvidia transparently disclosed. Corporate interests aligned with proposal (both companies ship Philox implementations). However, no explicit succession plan or post-acceptance stewardship commitment documented.

**Evidence cited:** Author affiliations clearly listed: "Ilya Burylov (Nvidia)", "Ruslan Arutyunyan (Intel)", etc.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria defined. No adoption targets specified. No retrospective analysis planned. No mechanism for gathering post-standardization usage data.

**Evidence cited:** None found

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Clear revision history (R0→R5) with documented LEWG feedback integration. Polls recorded (Section 9). Competing approaches resolved (counter_based_engine removed per LEWG 2023-11-28 poll). Design authority clear through consistent author team across revisions.

**Evidence cited:** "Based on the poll at LEWG Telecon on 2023-11-28 the second approach was removed from the paper starting from R4" (Section 8.1)

---

### 10. Practical Usability — ✅

**Score: 2/2**

API follows existing `<random>` engine patterns. `set_counter()` genuinely simplifies parallel Monte Carlo simulations. Predefined aliases eliminate template parameter complexity. Error messages would reference familiar random engine concepts.

**Evidence cited:** Section 8.2 example demonstrates simplified parallel simulation code compared to alternatives

---

### 11. Safety & Stability — ❌

**Score: 0/2**

No safety analysis. No discussion of how this contributes to C++ safety roadmap. ABI implications not mentioned. No analysis of whether design permits future optimization.

**Evidence cited:** None found

---

### 12. Ecosystem Consideration — ❌

**Score: 0/2**

No rationale for standard inclusion vs package manager distribution. Paper lists extensive ecosystem solutions (Intel MKL, cuRAND, rocRAND, numpy) without explaining why these are insufficient. Assumes standardization is better than ecosystem without justification.

**Evidence cited:** None—paper lists ecosystem success as motivation rather than analyzing why ecosystem is insufficient

---

### 13. Expert Weighting — ✅

**Score: 2/2**

John Salmon (original Philox algorithm author) listed as contributor. Authors include implementers from Intel and Nvidia who ship production Philox code. Original academic papers cited. Design informed by years of vendor deployment.

**Evidence cited:** "Contributors: John Salmon" (paper header); authors from Intel MKL and cuRAND teams
