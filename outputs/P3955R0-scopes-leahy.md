# D3004 Evaluation: P3955R0 — It's Scopes All the Way Down

**Paper:** P3955R0  
**Title:** It's Scopes All the Way Down  
**Authors:** Robert Leahy  
**Link:** [https://wg21.link/P3955R0](https://wg21.link/P3955R0)  
**Revision Date:** 2026-01-14  
**Evaluation Date:** 2026-01-24

---

## Gate: Principled Design Foundation

**G0. Status quo included as baseline?** ❌ FAIL  
The paper discusses the limitations of synchronous RAII and prior work (P2849R0) but does not explicitly include "status quo (no change)" as a candidate solution scored against enumerated principles.

**G1. Imperative principles identified and enforced?** ❌ FAIL  
The paper presents design goals implicitly through discussion but does not characterize any principles by importance level (@, 9, 5, 1, -) and does not identify imperative constraints that filter solutions.

**Gate Result:** ❌ NOT PRINCIPLED DESIGN — Missing status quo baseline and imperative principle identification

---

## Guidance for Authors

This evaluation assesses whether your proposal follows D3004R0 principled design methodology. The gate failure indicates the proposal's analysis methodology needs strengthening, not necessarily that your conclusions are wrong.

### What Was Missing

**G0 Failure:** The paper motivates asynchronous RAII by showing limitations of current C++ (synchronous constructors/destructors) and discusses issues with P2849R0's prior design, but neither "do nothing" nor "use existing patterns (e.g., manual cleanup)" is explicitly enumerated as Solution A and scored against principles. The `simple_counting_scope` example demonstrates problems with the status quo but doesn't position it as a competing solution.

**G1 Failure:** The paper contains implicit design principles (e.g., "avoid object primacy," "support rvalue qualification," "follow currying model") but these are not:
- Extracted into an explicit list
- Characterized by importance (imperative vs. high vs. medium)
- Used to systematically filter candidate solutions

### How to Apply Principled Design

**To pass G0 (Status quo as baseline):**
- Add "Solution A: Status Quo — Manual cleanup patterns with synchronous destructors"
- Add "Solution B: Prior Design (P2849R0) — async_object concept with storage"
- Add "Solution C: Proposed Design — Scopes with enter/exit senders"
- Score all three against enumerated principles

**To pass G1 (Imperative principles identified):**
- Extract principles from motivating discussion, such as:
  - "Must not require copied captures from const-qualified objects" (from reference qualification issue)
  - "Must support rvalue qualification of factory invocation"
  - "Must not couple scope entry/exit to object storage"
  - "Must integrate with std::execution currying model"
- Assign importance: At least one should be imperative (@) — perhaps "must not require objects to be movable for placement in operation states"
- Eliminate solutions failing imperatives before considering other criteria

### D3004R0 Reference

For detailed methodology, see D3004R0 "Principled Design for WG21" by John Lakos et al.:
- Section 5: Writing a Principled-Design-Based Standards Proposal
- Section 6: Example 2 (Erroneous Behavior) demonstrates full methodology
- Table format and scoring scales in Section 5.5-5.6

### Strengths to Preserve

The paper demonstrates several aspects that align with principled design philosophy:

1. **Prior art acknowledgment:** The paper explicitly builds on P2849R0 and credits Kirk Shoop's exploration
2. **Issue identification:** Clear enumeration of problems with prior design (reference qualification, curried-or-not ambiguity, object primacy)
3. **Evolutionary design:** Shows how new design addresses each identified issue
4. **Extensive examples:** Practical examples (let_async_scope, async_mutex, io_uring) demonstrate the design's capabilities
5. **Implementation experience:** Author has implemented the design on stdexec

These elements could form the foundation of a principled design analysis if restructured into the formal methodology.

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal did not follow principled design methodology.** The scores below indicate how close the analysis comes to D3004 requirements.

🔴 GATE FAIL: Paper presents well-motivated design evolution but does not follow principled design methodology for solution comparison and selection.

| # | Category | Score | |
|---|----------|-------|---|
| 1 | Solution Completeness | 0 | ❌ |
| 2 | Principle Extraction | 1 | ⚠️ |
| 3 | Principle Formulation | 0 | ❌ |
| 4 | Importance & Objectivity | 0 | ❌ |
| 5 | Ranking & Ordering | 0 | ❌ |
| 6 | Compliance Table | 0 | ❌ |
| 7 | Row-by-Row Analysis | 0 | ❌ |
| 8 | Hybrid Exploration | 1 | ⚠️ |
| 9 | Evolution & Compatibility | 1 | ⚠️ |
| 10 | Transparency & Auditability | 1 | ⚠️ |
| **TOTAL** | | **4/20** | Below threshold |

---

## Summary Exposition

P3955R0 presents a thoughtful evolution of asynchronous RAII design for C++, building explicitly on Kirk Shoop's P2849R0. The paper identifies concrete technical issues with the prior design—reference qualification problems, the curried-vs-uncurried ambiguity, and unnecessary coupling to object storage—and proposes a cleaner design based on scope entry/exit senders. The technical content is substantial and the examples demonstrate practical value.

However, the paper does not follow D3004 principled design methodology. Rather than enumerating candidate solutions (including status quo), extracting principles with importance characterization, and systematically scoring solutions against ranked principles, the paper presents a narrative evolution from problem identification to proposed solution. This approach, while readable, does not provide the auditable decision trail that principled design enables.

The paper would benefit from restructuring its analysis to: (1) explicitly include status quo and P2849R0 as scored alternatives, (2) extract the implicit principles into an explicit ranked list with importance levels, and (3) present a compliance table showing how each solution performs against each principle. This would strengthen the argument for the proposed design by making the selection criteria transparent and reproducible.

---

## Red Flags Identified

🚩 **No status quo** — Status quo not included as Solution A; paper motivates change but doesn't formally score "do nothing"

🚩 **No imperatives** — No principles marked as imperative importance; design goals are implicit

🚩 **Vague principles** — Principles embedded in prose cannot be objectively scored by independent evaluators

🚩 **Missing compliance table** — No tabular solution-vs-principle comparison

🚩 **Arbitrary ranking** — Principles not ordered by importance/objectivity rationale

🚩 **Hidden derivation** — Final design principles not explicitly mapped from raw motivating reasons

---

## Category-by-Category Analysis

### 1. Solution Completeness — ❌

**Score: 0/2**

**D3004 Principle:** P1 (Status Quo Is Always a Candidate Solution), P9 (Motivating Principles Come From All Solutions)

The paper discusses three implicit solution categories: (1) synchronous RAII status quo, (2) P2849R0's async_object design, and (3) the newly proposed scope-based design. However, these are not enumerated as Solutions A, B, C with formal analysis. The status quo is presented only as motivation for why change is needed, not as a candidate being evaluated. P2849R0 is analyzed for its flaws but not scored against principles that would also apply to the new design.

**Evidence cited:** "Kirk Shoop has previously explored this space [2]. With his permission the author of this paper is continuing that exploration." — acknowledges prior work but doesn't position it as a competing solution.

---

### 2. Principle Extraction — ⚠️

**Score: 1/2**

**D3004 Principle:** P9 (Motivating Principles Come From All Solutions)

The paper does extract several implicit principles from the prior design's failures: the need to avoid const-qualification problems, support consumptive capture, avoid coupling scopes to storage, and support single-responsibility decomposition. These motivating reasons are discussed in the "Issues With the Prior Design" section. However, they are not formalized into an explicit principle list, and principles from status quo advocates are not captured.

**Evidence cited:** "Reference Qualification: The most serious issue with the previous design is that it requires that async_construct and async_destruct be invocable on const lvalue async objects."

---

### 3. Principle Formulation — ❌

**Score: 0/2**

**D3004 Principle:** P4 (Principles Must Be Actionable and Measurable)

No explicit principles are formulated. Design goals are embedded in prose discussion (e.g., "should support rvalue qualification," "should decouple scopes from storage") but are not stated as binary predicates or quantitative metrics that could be objectively scored. Two independent evaluators reading this paper could not produce consistent scores for solutions because there is no scoring framework.

**Evidence cited:** None found — no explicit principle statements with measurable criteria.

---

### 4. Importance & Objectivity Characterization — ❌

**Score: 0/2**

**D3004 Principle:** P3 (Coarse Scoring Enables Consensus), P5 (Objectivity Determines Reliability)

The paper does not use D3004's importance scale (@, 9, 5, 1, -) or objectivity scale (@, 5, -). No principles are characterized by importance level, and no imperative constraints are identified. All design considerations are presented with equal implicit weight.

**Evidence cited:** None found — no importance or objectivity characterization present.

---

### 5. Ranking & Ordering — ❌

**Score: 0/2**

**D3004 Principle:** P3 (Coarse Scoring Enables Consensus), P5 (Objectivity Determines Reliability)

Design considerations are presented in narrative order rather than ranked by importance and objectivity. There is no principle table showing rank numbers, and no documentation of how ties would be broken. The ordering appears to follow the structure of the discussion (prior art → issues → new design) rather than priority-based ranking.

**Evidence cited:** None found — no ranked principle list.

---

### 6. Compliance Table — ❌

**Score: 0/2**

**D3004 Principle:** P6 (Row-by-Row Analysis Eliminates Nonviable Solutions)

No compliance table is present. Solutions are not scored against principles in tabular format. The reader cannot quickly see how each candidate solution (status quo, P2849R0 design, proposed design) performs against each design criterion.

**Evidence cited:** None found — no tabular comparison.

---

### 7. Row-by-Row Analysis — ❌

**Score: 0/2**

**D3004 Principle:** P2 (Imperative Principles Are Absolute Filters), P6 (Row-by-Row Analysis)

Without a compliance table, there is no row-by-row analysis. The paper does not proceed from highest-priority principles to lowest, eliminating solutions that fail imperative constraints. The prior design (P2849R0) is effectively eliminated through narrative discussion of its flaws, but this elimination is not documented as failing specific imperative principles.

**Evidence cited:** None found — no systematic elimination process.

---

### 8. Hybrid Exploration — ⚠️

**Score: 1/2**

**D3004 Principle:** P7 (Hybrid Solutions Often Emerge from Analysis)

The paper does show evolutionary design: the new proposal addresses specific issues identified in P2849R0 while preserving its core insight (asynchronous construction/destruction). The scope-based design can be seen as a hybrid that keeps the async object concept while decoupling it from storage management. However, this evolution is not framed as formal hybrid exploration with re-scoring.

**Evidence cited:** "Note that none of the names in this paper, unlike the previous one [2], feature the async_ prefix." — shows conscious evolution from prior design while departing from some conventions.

---

### 9. Evolution & Compatibility — ⚠️

**Score: 1/2**

**D3004 Principle:** P8 (Bidirectional Compatibility), P13 (Deprecation Before Ill-Formed), P14 (QoI Independence), P15 (Diagnosability Preservation)

The paper considers how the proposed design fits within the existing std::execution ecosystem, explicitly extending the currying model. The `sync_object` utility shows how to wrap synchronous objects, preserving compatibility with existing code patterns. However, there is no explicit analysis of whether this proposal closes design space for future evolution, and diagnosability considerations are not discussed.

**Evidence cited:** "The above design also reflects and extends the currying model of std::execution."

---

### 10. Transparency & Auditability — ⚠️

**Score: 1/2**

**D3004 Principle:** P12 (Show Your Work—Don't Rewrite the Lab Notebook)

The paper does show evolution from P2849R0 to the new design, documenting three specific issues with the prior design and how each is addressed. The development from "async_object with storage" to "scopes that yield exit senders" is traceable. However, the paper presents polished conclusions rather than showing the full principle extraction and refinement process that would make the analysis independently reproducible.

**Evidence cited:** "Issues With the Prior Design" section documents three categories of problems: reference qualification, curried-or-not ambiguity, and object primacy.

---

*This feedback helps improve proposal methodology. A revised paper with proper principled design analysis will receive a fresh evaluation.*
