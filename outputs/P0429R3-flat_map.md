# Evaluation: P0429R3 — A Standard flat_map

**Paper:** P0429R3  
**Title:** A Standard flat_map  
**Authors:** Zach Laine  
**Link:** [https://wg21.link/P0429R3](https://wg21.link/P0429R3)  
**Revision Date:** 2016-08-31  
**Evaluation Date:** 2026-01-07

---

## Gate: Standardization Justification

**G0. What coordination failure does this solve?** ❌ FAIL  
Paper cites "virtually everyone who makes games, embedded, or system software in C++ uses the Boost implementation or one that they rolled themselves" — this is evidence the ecosystem works, not evidence of coordination failure. No documented interoperability harm, bug reports, or integration failures cited.

**G1. Why not third-party?** ❌ FAIL  
Boost.FlatMap has been available since 2011 (Boost 1.48) and the paper acknowledges widespread use. No explanation of why Boost distribution is insufficient; primary motivation appears to be convenience of having it "in the standard."

**G2. Perpetual costs acknowledged?** ❌ FAIL  
No discussion of implementation burden across vendors, interaction surface with existing standard library, teaching burden, or maintenance commitment post-standardization.

**Gate Result:** ❌ AUTOMATIC FAIL — Standardization not justified; paper relies on "widespread existing implementations" which proves ecosystem works, not that standardization is necessary

---

## Guidance for Authors

This evaluation is not a judgment on whether `flat_map` is useful or well-designed—the extensive field experience via Boost.FlatMap since 2011 strongly suggests it is both. The gate failure indicates that the proposal, as written, has not yet made the case for why this functionality must be in the C++ standard library rather than distributed through the ecosystem.

### What Was Missing

**G0 failed** because the paper's primary justification is that "virtually everyone" uses Boost or their own implementation. Per the evaluation framework, this proves the ecosystem successfully distributes this functionality. No specific coordination failures are documented—no bug reports where `boost::container::flat_map` was incompatible with another `flat_map`, no GitHub issues showing integration pain, no quantified engineering costs from fragmentation.

**G1 failed** because Boost.FlatMap has been stable and widely used since 2011. The paper does not explain what specific problems users face that Boost cannot solve. The mention of SG14 discussions (P0038R0) indicates interest, but interest is not the same as documented coordination failure.

**G2 failed** because the paper contains no analysis of:
- Which vendors would implement this and the estimated complexity
- How `flat_map` interacts with `<algorithm>`, `<ranges>`, and iterator requirements
- Who commits to resolving defects post-standardization
- The teaching burden of adding another map variant to the standard library

### How to Strengthen a Revision

To pass G0 (What coordination failure does this solve?), consider adding:
- **Vocabulary type argument with evidence**: Document specific cases where libraries needed to exchange `flat_map` objects at API boundaries and failed due to incompatible types (e.g., game engine A uses Boost.flat_map, middleware B uses Folly's sorted_vector_map, integration failed)
- **Quantified fragmentation harm**: Survey major game/embedded projects to quantify hours spent wrapping or converting between incompatible flat map implementations
- **Named victims**: Identify specific open-source or commercial projects that encountered interoperability problems

To pass G1 (Why not third-party?), consider adding:
- **Why Boost is insufficient**: Boost.FlatMap exists—explain why standardization adds value beyond what Boost provides. Is it that Boost's specific design decisions don't satisfy all users? That Boost is not universally available in constrained environments?
- **Cross-library exchange requirement**: If the argument is that libraries need to agree on this type at boundaries (like `std::optional` or `std::string_view`), provide concrete evidence of API boundaries where this matters

To pass G2 (Perpetual costs), consider adding:
- **Implementation analysis**: Acknowledge that libstdc++, libc++, and MSVC STL would all need to implement, test, and maintain this indefinitely
- **Interaction surface**: Document interactions with ranges, algorithms, and the complexity of proxy iterators (the paper notes dependence on Ranges TS—this has implementation implications)
- **Maintenance commitment**: State whether the author or sponsoring organizations commit to addressing defects discovered post-standardization

### Alternative Paths

If standardization justification remains difficult to establish, consider:
- **Documenting real integration failures**: Return to SG14 and survey actual projects for interoperability incidents
- **Proposing ecosystem coordination**: Work with Boost and other implementers to establish a common interface that could later become a candidate for standardization
- **Waiting for vocabulary evidence**: As more libraries adopt flat maps at API boundaries, coordination failures may naturally emerge and become documentable

### Strengths to Preserve

- **Extensive field experience**: Boost.FlatMap since 2011 is exactly the kind of prior art the committee values
- **Responsive to feedback**: Three revisions incorporating LEWG direction (proxy iterators, split storage, etc.) demonstrates good process
- **Clear design rationale**: The tradeoffs section (from Boost.Container docs) honestly presents both benefits and drawbacks
- **Complete API specification**: The synopsis is thorough and usable

---

*This feedback is generated to help improve proposals. The committee values your contribution to C++ and encourages resubmission once the standardization justification is strengthened.*

---

## Detailed Evaluation (For Reference)

> ⚠️ **This proposal failed the standardization justification gate.** The detailed evaluation below is provided for reference. The primary action items are in Guidance for Authors above.

🔴 GATE FAIL: Proposal does not justify why this cannot remain a third-party library; "widespread use of Boost.FlatMap" proves ecosystem distribution works.

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
| 11. Safety & Stability | 1 | ⚠️ |
| 12. Ecosystem Consideration | 0 | ❌ |
| 13. Expert Weighting | 2 | ✅ |
| **TOTAL** | **14/26** | Library threshold: 14 ✅ |

The paper meets the minimum library threshold score but fails the gate questions, which take precedence.

## Summary Exposition

**Key Strengths:** P0429R3 represents genuine, battle-tested existing practice. Boost.FlatMap has been in production since 2011, giving it over 5 years of field experience at time of writing. The proposal is responsive to committee feedback—R3 incorporates significant design changes based on LEWG direction regarding proxy iterators and split storage. The API is thoroughly specified and designed as a drop-in replacement for `std::map` with different performance characteristics. The involvement of SG14 (game/embedded developers) provides some domain expert validation.

**Critical Gaps:** The proposal fails to make the case for *why* standardization is necessary. The primary motivation appears to be "many people use this" and "it would be convenient to have in the standard"—but these are precisely the arguments the evaluation framework identifies as insufficient. Boost.FlatMap works. The ecosystem distributes it effectively. No coordination failures are documented. The paper also contains no analysis of the perpetual costs that standardization imposes on implementers, the committee, and educators.

**Recommendation:** Revise and resubmit with documented evidence of coordination failures. The underlying functionality is clearly valuable—the question is whether standardization (vs. ecosystem distribution via Boost) is the right solution. A revision should answer: "What specific harm has occurred because `flat_map` is not in the standard?" If the answer is "none documented," the proposal may need to mature further in the ecosystem until such evidence emerges.

## Red Flags Identified

🚩 **"Multiple implementations exist" as justification** — The paper cites widespread Boost use and rolled-own implementations as motivation. Per the framework, this proves the ecosystem works, not that standardization is needed.

🚩 **No standardization justification** — Paper treats "useful and widely wanted" as sufficient justification without cost/benefit analysis.

🚩 **ABI silence** — No discussion of ABI implications or long-term maintenance burden.

🚩 **No retrospective plan** — No success criteria or measurement plan defined.

🚩 **Cost blindness** — No acknowledgment of perpetual implementation/maintenance burden across vendors.

---

## Category-by-Category Analysis

### 1. Use-Case Validation — ⚠️

**Score: 1/2**

The paper presents the API thoroughly but does not open with concrete user-facing code examples demonstrating typical usage patterns. The design goals section discusses tradeoffs in abstract terms (faster lookup, better cache performance, non-stable iterators) rather than showing "before and after" code comparisons. The synopsis is comprehensive but serves as reference documentation rather than use-case-driven motivation.

**Evidence cited:** "Overall, flat_map is meant to be a drop-in replacement for map, just with different time- and space-efficiency properties." — This states intent but doesn't demonstrate it with code.

### 2. Economic Analysis — ❌

**Score: 0/2**

The paper contains no economic analysis of standardization costs. There is no comparison of standardization vs. continued ecosystem distribution via Boost. No estimate of implementation burden, interaction complexity, teaching burden, or long-term committee maintenance commitment. The paper assumes that being "useful" is sufficient justification.

**Evidence cited:** None found.

### 3. Vocabulary Necessity — ❌

**Score: 0/2**

The paper does not make a vocabulary type argument with evidence. While `flat_map` could theoretically serve as a vocabulary type at API boundaries (like `std::map`), the paper provides no documentation of coordination failures—no bug reports, no GitHub issues, no quantified harm from the existence of multiple incompatible implementations. The "multiple implementations exist" argument is explicitly identified by the framework as evidence AGAINST standardization.

**Evidence cited:** "Virtually everyone who makes games, embedded, or system software in C++ uses the Boost implementation or one that they rolled themselves." — This proves ecosystem success, not coordination failure.

### 4. External Validation — ⚠️

**Score: 1/2**

The paper references SG14 (game/embedded developers) and mentions a related paper P0038R0. It claims widespread use in games, embedded, and system software. However, no specific organizations are named with their use cases, no user testimonials are provided, and no quantitative problem statement is given. The validation is categorical ("game developers use this") rather than specific ("Company X reports Y% performance improvement").

**Evidence cited:** "This has motivated discussions among the members of SG14 resulting in a paper" — references P0038R0 but doesn't cite specific organizations or testimonials.

### 5. Implementation & Field Experience — ✅

**Score: 2/2**

This is the proposal's strongest category. Boost.FlatMap has been available since Boost 1.48 (2011), providing 5+ years of field experience at time of writing. The implementation is publicly available, has gone through multiple Boost release cycles, and has been refined based on user feedback. The proposal notes that "As of Boost 1.65, the Boost implementation will optionally act as an adapter," showing ongoing evolution.

**Evidence cited:** "This proposal represents existing practice in widespread use – Boost.FlatMap has been available since 2011 (Boost 1.48)."

### 6. Completeness — ✅

**Score: 2/2**

The proposal provides a complete, usable API. Users can construct a `flat_map` with default containers (`vector<Key>`, `vector<T>`), perform standard map operations, and start using it immediately. No ecosystem completion is required. The synopsis is thorough and includes all necessary member functions, type aliases, deduction guides, and comparison operators.

**Evidence cited:** The complete 10-page synopsis with all member functions specified.

### 7. Incentive Alignment — ⚠️

**Score: 1/2**

The author (Zach Laine) is a known WG21 contributor with library experience. The proposal acknowledges Ion Gaztañaga (Boost.FlatMap author) and Sean Middleditch for design contributions. However, there is no explicit stewardship commitment post-acceptance, no succession plan, and no statement about who would address defects discovered after standardization.

**Evidence cited:** "Thanks to Ion Gaztañaga for writing Boost.FlatMap. Thanks to Sean Middleditch for suggesting the use of split containers for keys and values."

### 8. Retrospective Commitment — ❌

**Score: 0/2**

The paper defines no success criteria, no adoption targets, and no plan for retrospective analysis. There is no mechanism proposed for gathering usage data or evaluating whether standardization was worthwhile. This follows a "ship and forget" pattern.

**Evidence cited:** None found.

### 9. Process & Timeline — ✅

**Score: 2/2**

The paper is at R3, demonstrating iterative refinement based on committee feedback. The revision history shows clear progression: R0→R1 (deduction guides, proxy iterators, split storage), R1→R2 (allocator changes, extract() return type, contains()), R2→R3 (value_type changes, sorted_unique_t uniformity). The author serves as clear design authority responding to LEWG direction.

**Evidence cited:** Detailed revision history showing responsive iteration: "LEWG was strongly against a flat map value_type with a non-const key. LEWG was also strongly against presenting values from the underlying storage container..."

### 10. Practical Usability — ✅

**Score: 2/2**

The design prioritizes practical usability. `flat_map` is explicitly designed as a drop-in replacement for `std::map`. The `sorted_unique_t` overloads provide optimization opportunities without requiring them. The `extract()`/`replace()` API enables batch operations. Deduction guides reduce boilerplate. The proxy iterator approach (while complex internally) preserves the expected user-facing `pair<const Key, T>` interface.

**Evidence cited:** "Overall, flat_map is meant to be a drop-in replacement for map, just with different time- and space-efficiency properties. Functionally it is not meant to do anything other than what we do with map now."

### 11. Safety & Stability — ⚠️

**Score: 1/2**

The paper honestly documents safety implications: "Weaker exception safety than standard associative containers (copy/move constructors can throw when shifting values in erasures and insertions)." It notes iterator invalidation differences. However, there is no discussion of ABI implications or whether the design permits future optimization without ABI breaks. The reliance on proxy iterators (and Ranges TS) is mentioned but ABI implications are not analyzed.

**Evidence cited:** "The exception safety guarantees for associative containers (§26.2.4.1) do not apply."

### 12. Ecosystem Consideration — ❌

**Score: 0/2**

The paper does not justify standard inclusion over ecosystem distribution. Boost.FlatMap has been successful for 5+ years. The paper provides no analysis of why ecosystem distribution is insufficient, no comparison of standardization benefits vs. costs, and no response to the obvious question: "Why not just use Boost?" The existence of a working ecosystem solution is treated as motivation for standardization rather than evidence against it.

**Evidence cited:** None found. The paper assumes standardization is desirable without comparing to the ecosystem alternative.

### 13. Expert Weighting — ✅

**Score: 2/2**

The proposal is grounded in expert input. It builds on Boost.FlatMap by Ion Gaztañaga, a major Boost contributor. SG14 (which includes practitioners from game development, embedded systems, and high-performance computing) provided input. The split storage suggestion came from Sean Middleditch, a game industry practitioner. The design reflects production experience rather than theoretical design.

**Evidence cited:** References to SG14 discussions, P0038R0, Boost.Container documentation, and named contributors with implementation experience.

---

## Historical Note

*For context: `flat_map` was eventually standardized in C++23 (P0429 continued through many more revisions). This evaluation assesses R3 as written in 2016, not the final accepted version. The eventual standardization suggests the committee ultimately found the justification compelling, though likely through evidence gathered in subsequent revisions.*
