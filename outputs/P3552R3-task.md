# Evaluation: P3552R3 — Add a Coroutine Task Type

**Paper:** P3552R3  
**Title:** Add a Coroutine Task Type  
**Authors:** Dietmar Kühl (Bloomberg), Maikel Nadolski  
**Link:** [https://wg21.link/P3552R3](https://wg21.link/P3552R3)  
**Revision Date:** 2025-06-20  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ✅ PASS  
C++26 shipped `std::execution` (sender/receiver) without a usable coroutine type—users cannot ergonomically use the framework without `task<T>`. This is framework completion, not ecosystem fragmentation.

**G1. Why not third-party?** ✅ PASS  
Requires tight integration with `std::execution` semantics (schedulers, stop tokens, environments). A third-party task type cannot be the canonical way to use a standard library framework.

**G2. Perpetual costs acknowledged?** ⚠️ PARTIAL  
Paper provides extensive wording and implementation analysis but does not explicitly quantify vendor implementation burden or long-term maintenance costs.

**Gate Result:** ✅ PROCEED TO EVALUATION

---

🟢 PASS: Framework-completing proposal that makes std::execution usable; strong implementation heritage and clear use-cases.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 1 | ⚠️ |
| 3. Vocabulary Necessity | 2 | ✅ |
| 4. External Validation | 2 | ✅ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 1 | ⚠️ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 2 | ✅ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **21/26** | Library threshold: 14 ✅ |

## Summary

P3552R3 is a well-justified, framework-completing proposal. C++26 standardized `std::execution` with the sender/receiver model, but without a coroutine task type, users face a significant usability gap—they must write custom coroutine machinery or adopt non-standard implementations to use the framework idiomatically. This proposal fills that gap with `std::execution::task<T>`.

The proposal demonstrates strong prior art: it builds on P1056, P2506, cppcoro, libunifex, and stdexec implementations. The design has been refined through multiple revisions incorporating SG1, LEWG, and LWG feedback. The Hello World example demonstrates immediate usability, and the integration with `std::execution` primitives (`sync_wait`, `just`, schedulers) is seamless.

**Key strengths:** Framework completion for std::execution; extensive prior implementation experience; clear progression through working groups; practical examples demonstrating usability.

**Areas for improvement:** The paper could benefit from explicit acknowledgment of perpetual costs (vendor implementation burden) and a retrospective commitment defining success criteria for adoption measurement.

## Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption review commitment defined.

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper opens with a concrete Hello World example showing `task<int>` usage with `sync_wait` and `co_await`. The design is clearly driven by the need to make `std::execution` usable for coroutine authors. Examples demonstrate real user-facing code, not abstract framework machinery.

**Evidence cited:** Section 1 provides immediate code example; prior work section explains why existing designs informed this one.

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper acknowledges implementation complexity through detailed wording and design discussion but does not explicitly quantify perpetual costs. There is no section discussing vendor implementation burden, interaction complexity with existing components, or long-term maintenance commitments.

**Evidence cited:** Extensive wording provided; no explicit cost analysis section.

---

### 3. Vocabulary Necessity — ✅

**Score: 2/2**

`task<T>` must be standardized because it is the idiomatic way to use `std::execution`. Libraries exchanging asynchronous operations via sender/receiver need a common coroutine type. Without standardization, every library would define its own task type, creating the fragmentation that sender/receiver was designed to avoid.

**Evidence cited:** "The expectation is that users would use the framework using some coroutine type. To support that, a suitable class needs to be defined."

---

### 4. External Validation — ✅

**Score: 2/2**

Extensive prior work validates demand: P1056, P2506, cppcoro (in active use), libunifex (Meta), stdexec (NVIDIA). Bloomberg's involvement demonstrates industrial need. Multiple implementations in production prove the design space is well-understood.

**Evidence cited:** Section 2 "Prior Work" documents cppcoro, libunifex, stdexec, folly::coro implementations and their deployment.

---

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

Multiple implementations exist with years of field experience. cppcoro, libunifex, and stdexec have all shipped task types with similar semantics. The proposal synthesizes lessons learned from these implementations, including symmetric transfer, allocator support, and scheduler integration.

**Evidence cited:** "There are also implementations of coroutine types based on a sender/receiver model in active use."

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal ships a complete, immediately usable `task<T>`. Users can write coroutines on day one without ecosystem scaffolding. The type integrates with existing `std::execution` primitives (`sync_wait`, `just`, schedulers, stop tokens).

**Evidence cited:** Hello World example compiles and runs; no external dependencies required beyond `<execution>` and `<task>`.

---

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

Bloomberg authorship is transparently disclosed. However, there is no explicit commitment to long-term stewardship or succession planning. Bloomberg has a strong track record with library proposals, but the paper doesn't address post-acceptance maintenance.

**Evidence cited:** Author affiliations disclosed; no maintenance commitment stated.

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

No success criteria defined. No adoption targets specified. No retrospective analysis planned. The paper does not address how to measure whether standardization was successful.

**Evidence cited:** None found.

---

### 9. Process & Timeline — ✅

**Score: 2/2**

Clear progression from R0 through R3 with documented feedback incorporation. SG1, LEWG, and LWG have all provided feedback reflected in revisions. The paper has explicit milestones and a named audience progression.

**Evidence cited:** Change history documents R1 (Hagenberg/SG1), R2 (LEWG), R3 (LWG) feedback.

---

### 10. Practical Usability — ✅

**Score: 2/2**

The task type is simple to use: declare return type as `task<T>`, use `co_await` and `co_return`. The Hello World example is 8 lines including headers. Error handling integrates with standard exception mechanisms. Gradual adoption is possible—users can use `task<T>` without adopting all of `std::execution`.

**Evidence cited:** Hello World example demonstrates simplicity; `co_await` on senders works naturally.

---

### 11. Safety & Stability — ⚠️

**Score: 1/2**

The paper addresses exception handling (`uncaught_exception`, `with_error`) and stop token integration. However, there is no explicit safety analysis or discussion of ABI implications. The design permits future optimization through allocator customization.

**Evidence cited:** Stop token integration documented; exception propagation specified; no explicit safety roadmap discussion.

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

The paper explicitly positions `task<T>` as completing `std::execution`, not competing with ecosystem solutions. It builds on cppcoro, libunifex, and stdexec experience rather than ignoring them. The proposal unifies fragmented approaches into a standard vocabulary type.

**Evidence cited:** Extensive prior work analysis; design informed by ecosystem implementations.

---

### 13. Expert Weighting — ✅

**Score: 2/2**

Authors have implementation experience (Bloomberg). Prior work from major library authors (Lewis Baker/cppcoro, Eric Niebler/libunifex) explicitly cited. Design incorporates lessons from production deployments at Meta, NVIDIA, and Bloomberg.

**Evidence cited:** Prior work section credits implementation experience; authors' affiliations demonstrate domain expertise.
