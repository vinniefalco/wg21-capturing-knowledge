# Combined Evaluation: BOOST1000 — IoAwaitables: A Coroutines-First Execution Model

**Paper:** BOOST1000  
**Title:** IoAwaitables: A Coroutines-First Execution Model  
**Authors:** Vinnie Falco, Steve Gerbino, Amlal El Mahrouss  
**Link:** N/A (Boost proposal, not WG21)  
**Revision Date:** 2026-01-21  
**Evaluation Date:** 2026-01-25

> **Note:** This document is labeled BOOST1000, indicating a Boost proposal rather than a WG21 paper. The evaluation frameworks below are designed for WG21 papers. The evaluations are provided for analytical purposes and to help authors understand how the proposal would fare under WG21 scrutiny if submitted for standardization.

---

# Part 1: WG21 Paper Evaluation

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ⚠️ CONDITIONAL PASS  
The paper argues that `std::execution` (P2300) is architecturally unsuited for networking due to backward query flow conflicting with coroutine allocation timing. However, it does not document specific coordination failures (bug reports, integration issues) in the ecosystem. The argument is design-theoretical rather than evidence-based.

**G1. Why not third-party?** ✅ PASS (as third-party)  
Section 10 explicitly acknowledges: "A reference implementation of this protocol exists as a complete library: Boost.Capy." The paper positions this as a Boost library, not claiming standardization is required. This actually demonstrates the ecosystem working as intended.

**G2. Perpetual costs acknowledged?** ⚠️ PARTIAL  
Section 11 provides proposed wording, implicitly acknowledging implementation burden. However, there is no explicit analysis of vendor implementation costs, interaction complexity with existing standard library components, or maintenance commitments.

**Gate Result:** ⚠️ CONDITIONAL — Paper is structured as ecosystem proposal (Boost), not standardization request. If submitted to WG21, G0 and G2 would need strengthening with documented coordination failures and explicit cost analysis.

---

## Guidance for Authors (If Targeting WG21)

This evaluation is not a judgment on whether your library is useful or well-designed—the extensive implementation (Boost.Capy, Boost.Corosio) suggests it is both. The current paper is appropriately positioned as a Boost proposal. If you later seek WG21 standardization, consider the following:

### What Would Need Strengthening for WG21

**G0 gaps:** The paper argues P2300 is architecturally unsuited for networking, but does not document:
- Specific bug reports where P2300's query model caused real networking problems
- Named projects that attempted to use P2300 for networking and failed
- Quantified engineering costs from the architectural mismatch

The argument is compelling design theory but lacks the evidence WG21 expects for coordination failure claims.

**G2 gaps:** For standardization, add:
- Implementation burden analysis across major vendors (libstdc++, libc++, MSVC STL)
- Interaction surface with `<coroutine>`, `<stop_token>`, `<memory_resource>`
- Commitment to long-term maintenance and defect resolution

### Current Strengths

The paper excels at:
- Use-case-driven design with concrete networking examples
- Clear articulation of why P2300's backward flow conflicts with coroutine allocation
- Working implementation with field experience (Boost.Capy)
- Complete specification (Section 11) demonstrating implementability

### Recommended Path

The current Boost trajectory is appropriate. After gathering multi-year field experience in Boost with documented user adoption, the case for standardization could be built with concrete evidence of:
1. Wide adoption metrics
2. User testimonials from production deployments
3. Evidence of ecosystem convergence on the IoAwaitable protocol
4. Documented interoperability benefits or coordination failures the standard type would solve

---

## Detailed Evaluation

🟡 CONCERNS: Strong technical proposal positioned correctly as ecosystem library; would need evidence-based justification for WG21 submission.

| Category | Score | |
|----------|-------|---|
| 1. Use-Case Validation | 2 | ✅ |
| 2. Economic Analysis | 1 | ⚠️ |
| 3. Vocabulary Necessity | 1 | ⚠️ |
| 4. External Validation | 1 | ⚠️ |
| 5. Implementation | 2 | ✅ |
| 6. Completeness | 2 | ✅ |
| 7. Incentive Alignment | 2 | ✅ |
| 8. Retrospective Commitment | 0 | ❌ |
| 9. Process & Timeline | 1 | ⚠️ |
| 10. Practical Usability | 2 | ✅ |
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 2 | ✅ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **19/26** | Library threshold: 14 ✅ |

### Summary Exposition

The IoAwaitables paper presents a well-reasoned argument that networking deserves purpose-built abstractions rather than adaptation to `std::execution`. The core technical insight—that coroutine frame allocation happens before `connect()`, making backward query flow incompatible with allocator propagation—is compelling. The paper demonstrates sophisticated understanding of both coroutine mechanics and networking requirements.

The proposal's greatest strength is its use-case-first methodology. Sections 2-3 systematically derive requirements from networking patterns (strand serialization, I/O completion contexts, thread affinity) before presenting solutions. The resulting design (executor, stop token, allocator propagation via forward flow) emerges naturally from these requirements rather than being retrofitted to them.

The paper appropriately positions itself as a Boost proposal rather than demanding immediate standardization. This demonstrates the kind of ecosystem-first development WG21 experts recommend. The path to standardization would involve gathering multi-year field experience and documenting concrete coordination failures that only standardization could resolve.

### Red Flags Identified

🚩 No retrospective plan — No success criteria or post-adoption metrics defined for measuring whether the design achieves its goals.

🚩 No documented coordination failures — The argument against P2300 is design-theoretical; no specific bug reports or failed integrations cited.

---

### 1. Use-Case Validation — ✅

**Score: 2/2**

The paper exemplifies use-case-driven design. Section 2 opens with concrete networking requirements (strand serialization, I/O completion contexts, thread affinity) before introducing any abstractions. Code examples throughout demonstrate user-facing usage patterns. The design emerges from use-cases rather than use-cases being found to justify an existing design.

**Evidence cited:** "Strip these requirements down to their essence. What primitive do they all depend on? Something that runs work. An executor." (§2.1)

---

### 2. Economic Analysis — ⚠️

**Score: 1/2**

The paper argues that P2300's machinery imposes complexity costs on networking without proportionate benefits (§6). However, it does not quantify the perpetual costs of standardizing the IoAwaitable protocol itself. Section 9 lists benefits but not costs. The comparison is asymmetric—P2300's costs are analyzed, but IoAwaitable's are assumed to be low without evidence.

**Evidence cited:** "The question is not whether P2300/P3826 break networking code. They don't—defaults work. The question is whether networking should pay for abstractions it doesn't use." (§6.3) — This analyzes P2300 costs but not IoAwaitable costs.

---

### 3. Vocabulary Necessity — ⚠️

**Score: 1/2**

The paper argues for forward context propagation as a vocabulary pattern but does not document specific coordination failures in the current ecosystem. The existence of Boost.Asio (decades of production use) actually demonstrates the ecosystem works. The paper does not show that Boost.Asio's model is insufficient or that fragmentation has caused documented harm.

**Evidence cited:** "This design borrows heavily from Boost.Asio." (§4.3) — Acknowledges ecosystem success rather than failure.

---

### 4. External Validation — ⚠️

**Score: 1/2**

The paper references Boost.Asio's success and cites Chris Kohlhoff's pioneering work. However, it does not cite specific organizations using IoAwaitable, user testimonials from production deployments, or developer surveys requesting this specific protocol. The validation is architectural (based on design analysis) rather than market-based.

**Evidence cited:** "These libraries arose from use-case-first driven development with a simple mandate: produce a networking library built only for coroutines." (§10) — Internal development mandate, not external user demand.

---

### 5. Implementation — ✅

**Score: 2/2**

Section 10 confirms: "A reference implementation of this protocol exists as a complete library: Boost.Capy. It is also the foundation for the Boost.Corosio library which offers sockets, timers, signals, DNS resolution, and integration on multiple platforms." This demonstrates working code beyond proof-of-concept, with platform integration.

**Evidence cited:** "Every design decision: forward context propagation, type-erased executors, the thread-local allocation window, emerged from solving real problems in production I/O code." (§10)

---

### 6. Completeness — ✅

**Score: 2/2**

The proposal is immediately usable. Section 11 provides complete wording with concepts (`io_awaitable`, `io_awaitable_task`, `io_launchable_task`, `executor`), types (`executor_ref`, `execution_context`), and launch functions (`run_async`, `run_on`). The `this_coro` namespace provides context accessors. No essential components are deferred to "the ecosystem."

**Evidence cited:** Section 11 wording provides complete specification including class definitions, concept requirements, and launch function semantics.

---

### 7. Incentive Alignment — ✅

**Score: 2/2**

The authors demonstrate clear commitment through existing library development (Boost.Capy, Boost.Corosio). The paper explicitly positions this as ecosystem-first development: "Standards should follow implementations, not the reverse." Corporate interests (if any) are not disclosed, but the Boost positioning suggests community-oriented development.

**Evidence cited:** "The future of C++ depends less on papers and more on practitioners who ship working code. Open source library authors are the true pioneers." (§10)

---

### 8. Retrospective Commitment — ❌

**Score: 0/2**

The paper defines no success criteria, adoption targets, or retrospective analysis plan. There is no mechanism for measuring whether the protocol achieves its goals or for documenting if adoption is lower than expected. This is a notable gap for a proposal that criticizes P2300's complexity—how will we know if IoAwaitable's simplicity delivers promised benefits?

**Evidence cited:** None found.

---

### 9. Process & Timeline — ⚠️

**Score: 1/2**

The paper positions itself as a Boost proposal with implicit timeline (Boost acceptance → field experience → potential standardization). However, explicit milestones and decision points are not documented. The relationship to ongoing P2300/P3826 evolution is observational rather than defining a concrete competing proposal timeline.

**Evidence cited:** "Our goal is not to replace std::execution for GPU workloads—it is to demonstrate that networking deserves a purpose-built abstraction." (§1) — Positions as parallel effort, not direct competitor with resolution timeline.

---

### 10. Practical Usability — ✅

**Score: 2/2**

The paper demonstrates that user code is simpler with IoAwaitable than without. Examples show clean coroutine chains without ceremony. The `co_await this_coro::executor` pattern provides intuitive context access. Error messages would reference user-understandable concepts (task, executor) rather than framework internals.

**Evidence cited:** §3 examples show straightforward coroutine patterns without the "template tax" the paper criticizes in P2300.

---

### 11. Safety & Stability — ⚠️

**Score: 1/2**

The paper discusses safety in terms of correct executor usage (§2.1 dispatch vs post for deadlock avoidance) and cooperative cancellation (§2.2). However, explicit contribution to C++'s safety roadmap is not documented. ABI implications are acknowledged implicitly through type erasure discussion but not analyzed explicitly.

**Evidence cited:** "Using dispatch while holding a mutex invites deadlock. Using post for every continuation wastes cycles bouncing through queues." (§1) — Safety as correctness, not security.

---

### 12. Ecosystem Consideration — ✅

**Score: 2/2**

The paper explicitly positions itself as an ecosystem proposal, not demanding immediate standardization. It acknowledges Boost.Asio's success and positions IoAwaitable as evolution within that ecosystem. The comparison to P2300 analyzes whether standardization would serve networking better than ecosystem development—and concludes ecosystem is the right path.

**Evidence cited:** "The future of asynchronous C++ need not be a single universal abstraction—it may be purpose-built frameworks that excel at their primary use cases while remaining interoperable at the boundaries." (§9)

---

### 13. Expert Weighting — ✅

**Score: 2/2**

The acknowledgements cite Chris Kohlhoff (Boost.Asio), Lewis Baker (coroutine expertise), and Dietmar Kühl (P2762, P3552). The design explicitly builds on decades of Boost.Asio production experience. The authors have implementation track records with Boost libraries.

**Evidence cited:** Acknowledgements section explicitly cites domain experts and their contributions, with the design informed by their work.

---

---

# Part 2: D3004 Principled Design Evaluation

## Gate: Principled Design Foundation

**G0. Status quo included as baseline?** ❌ FAIL  
The paper does not include "Status Quo / No Change" as an explicitly scored solution. While P2300 is analyzed as an alternative, the comparison is narrative rather than tabular, and the option of "use P2300 as-is for networking" is not formally scored against principles alongside IoAwaitable.

**G1. Imperative principles identified and enforced?** ❌ FAIL  
The paper does not characterize any requirements as imperative (@), high (9), medium (5), or low (1). Design goals are stated (forward propagation, minimal executor, allocator at invocation time) but not ranked by importance. No principle is identified as an absolute filter that would eliminate solutions.

**Gate Result:** ❌ NOT PRINCIPLED DESIGN — Paper uses traditional technical argument structure, not D3004 methodology

---

## Guidance for Authors

This evaluation assesses whether your proposal follows D3004R0 principled design methodology. The gate failure indicates the paper uses traditional technical argument structure rather than principled design methodology. This is not a judgment on design quality—the paper may reach correct conclusions through traditional analysis.

### What Was Missing

**G0 failed** because the paper compares IoAwaitable against P2300 in prose form without including "do nothing / status quo" as a formally scored option. D3004 requires status quo as Solution A, scored against all principles to demonstrate why change is necessary.

**G1 failed** because the paper does not use the D3004 importance scale (@/9/5/1/-) or identify imperative constraints. Requirements like "allocator must be present at invocation" are stated but not characterized as imperative vs. desirable.

### How to Apply Principled Design

**To convert this paper to principled design:**

1. **Define candidate solutions:**
   - Solution A: Status Quo (use existing approaches without new protocol)
   - Solution B: Adapt P2300 for networking (sender/receiver model)
   - Solution C: IoAwaitable protocol (forward propagation)
   - Solution D: Hybrid (IoAwaitable concepts with P2300 interop layer)

2. **Extract principles from all solutions' motivations:**
   - From P2300 advocates: composability, structured concurrency, heterogeneous dispatch
   - From IoAwaitable: allocation timing, forward flow, minimal surface area
   - From status quo advocates: stability, no new learning curve

3. **Characterize importance:**
   - @ (Imperative): "Allocator discoverable before coroutine frame allocation"
   - 9 (High): "Minimal executor abstraction (dispatch/post only)"
   - 5 (Medium): "Type erasure at API boundaries"
   - 1 (Low): "Syntax convenience"

4. **Create compliance table** scoring each solution against each principle

5. **Perform row-by-row elimination** starting from highest-priority principles

### D3004R0 Reference

For detailed methodology, see D3004R0 "Principled Design for WG21":
- Section 5: Writing a Principled-Design-Based Standards Proposal
- Section 6: Example 2 (Erroneous Behavior) demonstrates full methodology

### Strengths to Preserve

The paper's strengths that align with principled design spirit:
- Clear articulation of motivating principles (§2: what networking needs)
- Fair representation of alternative (P2300) with its motivating reasons
- Evidence-based comparison (allocation timing, type leakage)
- Transparent reasoning that readers can audit

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal did not follow principled design methodology.** The scores below indicate how close the analysis comes to D3004 requirements.

🟠 PARTIAL: Paper has strong design rationale but presented in traditional argument form, not D3004 tabular methodology.

| # | Category | Score | |
|---|----------|-------|---|
| 1 | Solution Completeness | 1 | ⚠️ |
| 2 | Principle Extraction | 2 | ✅ |
| 3 | Principle Formulation | 1 | ⚠️ |
| 4 | Importance & Objectivity | 0 | ❌ |
| 5 | Ranking & Ordering | 0 | ❌ |
| 6 | Compliance Table | 0 | ❌ |
| 7 | Row-by-Row Analysis | 0 | ❌ |
| 8 | Hybrid Exploration | 1 | ⚠️ |
| 9 | Evolution & Compatibility | 1 | ⚠️ |
| 10 | Transparency & Auditability | 2 | ✅ |
| **TOTAL** | **8/20** | Below threshold |

### Summary Exposition

The IoAwaitables paper demonstrates strong technical analysis but does not employ D3004 principled design methodology. The comparison between IoAwaitable and P2300 is presented through traditional argumentative structure: stating requirements (§2), presenting the proposed solution (§3-5), and arguing against alternatives (§6). This is effective technical writing but does not provide the auditable, tabular analysis that D3004 methodology requires.

The paper's greatest methodological strength is its fair representation of P2300's motivating principles. Section 6 acknowledges that P2300's query model works well for GPU workloads and that defaults function correctly for networking. This intellectual honesty is aligned with D3004's requirement to extract principles from all solutions, not just the preferred one.

The primary gaps are structural: no compliance table, no formal importance ranking, no row-by-row elimination analysis. Converting to D3004 format would strengthen the case by making the design tradeoffs explicit and auditable, particularly the claim that allocator timing is an imperative constraint rather than a preference.

### Red Flags Identified

🚩 No status quo — "Do nothing" is not included as a formally scored solution
🚩 No imperatives — No principles marked with imperative (@) importance
🚩 Missing compliance table — No tabular solution-vs-principle comparison
🚩 Arbitrary ranking — Principles presented without importance/objectivity characterization
🚩 Hidden derivation — Final design principles appear without formal extraction from competing solutions

---

### 1. Solution Completeness — ⚠️

**Score: 1/2**

**D3004 Principle:** P1 (Status Quo Is Always a Candidate Solution), P9 (Motivating Principles Come From All Solutions)

The paper considers IoAwaitable (proposed) and P2300 (alternative) but does not include status quo as a formally scored option. Boost.Asio is mentioned as existing practice but not analyzed as a candidate solution. The comparison is IoAwaitable vs P2300, not a multi-solution analysis including "change nothing."

**Evidence cited:** "Our goal is not to replace std::execution for GPU workloads—it is to demonstrate that networking deserves a purpose-built abstraction." (§1) — Binary comparison, not multi-solution with status quo.

---

### 2. Principle Extraction — ✅

**Score: 2/2**

**D3004 Principle:** P9 (Motivating Principles Come From All Solutions)

The paper fairly extracts motivating principles from both IoAwaitable and P2300. Section 6.3's table explicitly lists what each approach needs vs. provides. P2300's design goals (domain-based dispatch, heterogeneous computing, typed operation state for optimization) are acknowledged and respected, even while arguing they don't serve networking.

**Evidence cited:** Table in §6.3 showing "Abstraction | Networking Need | GPU/Parallel Need" demonstrates fair extraction from competing solutions.

---

### 3. Principle Formulation — ⚠️

**Score: 1/2**

**D3004 Principle:** P4 (Principles Must Be Actionable and Measurable)

Some principles are well-formulated as binary predicates ("allocator must be present at invocation"—testable: either it is or isn't). Others are vaguer ("simpler design," "minimal surface area"). The paper does not consistently use D3004's binary/metric formulation style that enables objective scoring.

**Evidence cited:** "Coroutine frame allocation happens before connect()—the allocator must be known at invocation" (§3.5) — Clear binary principle. But "minimal executor abstraction" lacks precise measure.

---

### 4. Importance & Objectivity Characterization — ❌

**Score: 0/2**

**D3004 Principle:** P3 (Coarse Scoring Enables Consensus), P5 (Objectivity Determines Reliability)

The paper does not use D3004's importance scale (@/9/5/1/-) or objectivity scale (@/5/-). Requirements are stated without characterizing whether they are imperative constraints or preferences. This makes it impossible to know which principles would eliminate solutions vs. merely influence preference.

**Evidence cited:** None found. Requirements in §2 are stated without importance ranking.

---

### 5. Ranking & Ordering — ❌

**Score: 0/2**

**D3004 Principle:** P3, P5

Principles are presented in narrative order (what networking needs → executor → stop token → allocator) rather than importance-ranked order. No explicit ranking table with importance and objectivity columns. Readers cannot determine which principles take precedence in case of conflicts.

**Evidence cited:** None found.

---

### 6. Compliance Table — ❌

**Score: 0/2**

**D3004 Principle:** P6 (Row-by-Row Analysis Eliminates Nonviable Solutions)

No compliance table exists. Section 6.3 has a comparison table, but it shows "need vs. need" by domain, not "solution vs. principle" scores. A D3004 compliance table would score IoAwaitable, P2300, and status quo against each ranked principle using the @/9/7/5/3/1/- scale.

**Evidence cited:** §6.3 table is domain comparison, not compliance scoring.

---

### 7. Row-by-Row Analysis — ❌

**Score: 0/2**

**D3004 Principle:** P2 (Imperative Principles Are Absolute Filters), P6

No row-by-row elimination analysis is present. The paper argues that P2300's backward flow is fundamentally incompatible with coroutine allocation timing, which could be formulated as an imperative failure—but this is presented as narrative argument, not formal elimination at a specific principle row.

**Evidence cited:** §3.5 argues P2300 fails allocation timing but does not formally eliminate it using D3004 methodology.

---

### 8. Hybrid Exploration — ⚠️

**Score: 1/2**

**D3004 Principle:** P7 (Hybrid Solutions Often Emerge from Analysis)

The paper does not explicitly explore hybrid solutions combining IoAwaitable with P2300 interop. However, the design itself shows hybrid thinking: type-erased `executor_ref` (similar to P2300's any_scheduler concept) combined with forward propagation. This suggests implicit hybrid exploration even without formal documentation.

**Evidence cited:** `executor_ref` design borrows type-erasure concept while rejecting query-based discovery—a form of selective hybrid.

---

### 9. Evolution & Compatibility — ⚠️

**Score: 1/2**

**D3004 Principle:** P8 (Bidirectional Compatibility), P13-P15

The paper considers forward compatibility (§4.4 discusses ABI stability through type erasure) but does not analyze whether adopting IoAwaitable would close design space for future evolution. Interoperability with P2300 at boundaries is mentioned as a goal but not detailed. No deprecation analysis since this is new functionality.

**Evidence cited:** "purpose-built frameworks that excel at their primary use cases while remaining interoperable at the boundaries" (§9) — Acknowledges interop need without detailing mechanism.

---

### 10. Transparency & Auditability — ✅

**Score: 2/2**

**D3004 Principle:** P12 (Show Your Work—Don't Rewrite the Lab Notebook)

The paper extensively shows its reasoning. The evolution from networking requirements (§2) to design decisions (§3-5) is transparent. Readers can follow the logical chain and disagree at specific points. The paper does not hide unfavorable comparisons—it acknowledges P2300 works for GPU workloads.

**Evidence cited:** §6 provides detailed analysis of P2300's design choices and why they don't serve networking, enabling readers to audit the reasoning.

---

---

# Summary: Both Evaluations

| Framework | Gate Result | Score | Threshold | Verdict |
|-----------|-------------|-------|-----------|---------|
| WG21 Paper Tester | ⚠️ Conditional | 19/26 | 14/26 | 🟡 CONCERNS |
| D3004 Principled Design | ❌ Fail | 8/20 | 14/20 | 🟠 PARTIAL |

**Overall Assessment:**

This is a well-crafted technical proposal that makes a compelling case for purpose-built networking abstractions. As a Boost proposal (its stated positioning), it is appropriately scoped and demonstrates mature ecosystem thinking.

For WG21 standardization (if pursued later), the paper would need to document specific coordination failures and acknowledge perpetual standardization costs.

For D3004 principled design compliance, the paper would need restructuring into tabular format with explicit status quo baseline, importance-ranked principles, and row-by-row elimination analysis. The underlying technical reasoning is strong—converting to D3004 format would make the design tradeoffs more auditable without requiring new analysis.

---

*Evaluations generated using WG21_PAPER_TESTER.md and D3004_TESTER.md frameworks. These are experimental methodologies; evaluations should be reviewed by humans before being acted upon.*
