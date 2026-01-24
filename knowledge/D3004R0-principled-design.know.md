# D3004R0: Principled Design for WG21 — Captured Knowledge

**Document**: D3004R0
**Authors**: John Lakos, Harold Bott, Mungo Gill, Lori Hughes, Alisdair Meredith, Bill Chapman, Mike Giroux, Oleg Subbotin (Bloomberg)
**Date**: 2024-02-13
**Audience**: EWG, LEWG
**Topics Covered**: Design methodology, proposal evaluation, committee process, decision-making framework, consensus building

## Executive Summary

This paper presents a formal, systematic design selection methodology called *principled design* for WG21. The methodology transforms subjective design debates into objective, auditable decision-making by: (1) explicitly enumerating all candidate solutions including status quo, (2) extracting and refining motivating principles from each solution, (3) characterizing each principle's importance and objectivity, (4) ranking principles systematically, and (5) scoring each solution against each principle in a compliance table. The methodology has been successfully applied in SG21 for Contracts MVP decisions and in EWG for erroneous behavior adoption. The paper provides detailed worked examples demonstrating how principled design can rapidly eliminate nonviable solutions, guide discovery of superior hybrid solutions, and achieve consensus where traditional voting methods fail.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Status Quo Is Always a Candidate Solution

> *"The first solution is always the status quo, representing no consensus for change."*

**The Principle**: Every principled design analysis must include the status quo (no change) as solution A, establishing the baseline that any proposed change must beat.

**Why It Matters**: The status quo provides an objective baseline for comparison. Any solution that fails to beat the status quo on high-priority principles is automatically nonviable. This prevents adopting changes that are worse than doing nothing.

**When to Apply**: 
- Beginning any design analysis
- Evaluating any proposal
- When tempted to skip comparison with current behavior

**Red Flags**:
- Analysis that omits "do nothing" as an option
- Proposals that don't demonstrate superiority over status quo
- Solutions adopted without explicit comparison to current behavior

**Supporting Experiences**: E1, E2, E3

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E1, E2, E3]
related-principles: [P2, P7]
-->

---

### P2: Imperative Principles Are Absolute Filters

> *"If a principle has imperative importance, any solution that fails to satisfy the principle is rejected over the status quo."*

**The Principle**: Principles scored as "imperative" (@) act as hard filters—any solution failing them is immediately eliminated, regardless of how well it scores on other criteria.

**Why It Matters**: Imperative principles represent inviolable constraints (e.g., backward compatibility of defined behavior, implementability). A solution that excels on 20 criteria but fails one imperative is worse than status quo.

**When to Apply**: 
- When evaluating any solution against principles
- When ranking principles (imperative always comes first)
- When a solution scores perfectly everywhere except one imperative

**Red Flags**:
- Rationalizing acceptance of solutions that fail imperatives
- Treating imperative principles as "negotiable"
- Allowing non-imperative concerns to override imperative failures

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P1, P3]
-->

---

### P3: Coarse Scoring Enables Consensus

> *"This restriction is the result of practicing the methodology and discovering that consensus is better served when the precision with which an answer can be expressed is not allowed to exceed the accuracy with which the number expressed represents the true value."*

**The Principle**: Use deliberately coarse scoring scales (@ 9 5 1 - for importance; @ 5 - for objectivity) to minimize debate over false precision and maximize consensus on relative rankings.

**Why It Matters**: Fine-grained scoring invites endless debate about whether something is 73% or 77% important. Coarse categories (imperative, high, medium, low, irrelevant) capture meaningful distinctions without spurious precision.

**When to Apply**: 
- Scoring importance: only @ 9 5 1 -
- Scoring objectivity: only @ 5 -
- Compliance: primarily @ 9 7 5 3 1 - with 8 6 4 2 reserved

**Red Flags**:
- Debates about whether something is 6 vs 7 in importance
- Over-precise numeric scores that don't reflect actual certainty
- Spending excessive time on fine gradations

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P4, P5]
-->

---

### P4: Principles Must Be Actionable and Measurable

> *"Write each principle as a clear, one-sentence rule/guideline... Prefer a binary property to a metric one where the former is more accurate... Prefer a metric property to a binary one when that property is not binary."*

**The Principle**: Refine raw motivating reasons into principles that are either binary predicates (yes/no) or quantitative metrics (minimize/maximize), with clear conditions for scoring.

**Why It Matters**: Vague principles like "be good" cannot be objectively scored. Binary predicates ("does not exceed budget") allow @ or - scores. Metrics ("maximize interpersonal interaction") enable graduated scoring.

**When to Apply**: 
- Transforming motivating reasons into principles
- When a principle seems impossible to score objectively
- When different scorers would give wildly different results

**Red Flags**:
- Principles that can't be scored consistently
- Mixing binary and metric language in one principle
- Principles where "true" and "false" aren't clearly distinguishable

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3, P5]
-->

---

### P5: Objectivity Determines Reliability of Scoring

> *"Provably objective principles score @ for objectivity... The wording of a principle can affect its objectivity, and the principle should be written to be as objective as possible."*

**The Principle**: Classify each principle's objectivity as provably objective (@), largely objective (5), or subjective (-) to indicate how reliably different scorers will agree.

**Why It Matters**: A principle like "does not change defined behavior" is provably objective—all scorers should agree. "Maximizes user satisfaction" is subjective—scores will vary. This meta-information helps weight tie-breaking.

**When to Apply**: 
- After writing each principle statement
- When principles of equal importance need ordering
- When group scoring shows wide disagreement

**Red Flags**:
- Claiming high objectivity for inherently subjective principles
- Ignoring objectivity when breaking ties
- Treating all principles as equally reliable

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3, P4]
-->

---

### P6: Row-by-Row Analysis Eliminates Nonviable Solutions

> *"As the author analyzes each row, they must document in the paper which candidate solutions remain, which have been rejected, and which are maybes, stating clearly our thought processes and reasons behind the decision to reject or retain."*

**The Principle**: Analyze the compliance table row by row from highest-priority principle to lowest, eliminating solutions that fail badly on each row before considering subsequent rows.

**Why It Matters**: This creates an efficient pruning process. A solution eliminated at row 3 doesn't need to be scored against rows 4-20. The resulting analysis is transparent and auditable.

**When to Apply**: 
- After completing the compliance table
- When presenting analysis to others
- When documenting rationale for decisions

**Red Flags**:
- Keeping clearly nonviable solutions in consideration too long
- Not documenting elimination decisions
- Jumping ahead to lower-priority principles before resolving higher ones

**Supporting Experiences**: E1, E2, E3

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1, E2, E3]
related-principles: [P1, P2]
-->

---

### P7: Hybrid Solutions Often Emerge from Analysis

> *"Combining the knowledge from another principle into a hybrid solution or creating a new derivative solution that removes the failure to comply to that important early principle can often result in a clear winner."*

**The Principle**: When a promising solution fails a single important principle but excels elsewhere, look for a hybrid solution that preserves its strengths while addressing the failure.

**Why It Matters**: The Italian restaurant emerged when the expensive steak restaurant exceeded budget but excelled on other criteria. Erroneous behavior emerged when zero-initialization failed to preserve diagnosability.

**When to Apply**: 
- When a promising solution fails one early principle
- When two solutions have complementary strengths and weaknesses
- When no single original solution clearly wins

**Red Flags**:
- Accepting a flawed solution without exploring hybrids
- Combining solutions that address unrelated concerns
- Creating Frankenstein solutions that violate coherence

**Supporting Experiences**: E1, E2, E5

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E1, E2, E5]
related-principles: [P1, P6]
-->

---

### P8: Preserve Bidirectional Compatibility Where Possible

> *"The change to C++ behavior is purely additive with no change to fully defined behavior, ensuring complete bidirectional semantic compatibility."*

**The Principle**: Prefer solutions that allow backward-compatible migration to future improvements over solutions that close off evolution paths.

**Why It Matters**: A solution that defines previously undefined behavior becomes the new baseline and may prevent future improvements. A solution that leaves room for future refinement enables ongoing evolution.

**When to Apply**: 
- When choosing between two otherwise comparable solutions
- When a solution would make currently undefined behavior defined
- When evaluating long-term implications

**Red Flags**:
- Solutions that permanently close design space
- Trading diagnosability of defects for deterministic behavior
- Adopting solutions that preclude known better alternatives

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P2, P7]
-->

---

### P9: Motivating Principles Come From All Solutions

> *"The goal is to provide any principles — beyond those listed with the preferred solution and regardless of perceived objectivity and relative importance as long as they are supportive, somewhat plausible, and relevant — that favor this alternative solution."*

**The Principle**: Extract motivating principles from every proposed solution, not just the author's preferred one, then apply all principles to all solutions uniformly.

**Why It Matters**: Each solution was proposed for a reason. That reason represents a principle someone considers important. Fair evaluation requires gathering principles from all perspectives, then letting the scoring determine outcomes.

**When to Apply**: 
- When collecting principles from multiple papers
- When the author has a preferred solution
- When ensuring fair evaluation of alternatives

**Red Flags**:
- Ignoring principles that favor competing solutions
- Rigging principle selection to favor a predetermined outcome
- Dismissing principles as "irrelevant" without scoring them

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P1, P4]
-->

---

### P10: Five-Way Polls Map to RICO Data Collection

> *"By taking a single five-way poll, we can typically derive the relevance, importance, and consensus from the poll."*

**The Principle**: Use standard WG21 five-way polls (SF/F/N/A/SA) mapped to (@/9/5/1/-) to efficiently collect Relevance, Importance, Consensus, and Objectivity data from groups.

**Why It Matters**: The existing poll mechanism can be repurposed to gather principled-design data without new tooling. SF means imperative, F means high importance, etc. This enables real-time group characterization.

**When to Apply**: 
- During committee meetings characterizing principles
- When gauging group consensus on principle importance
- When limited time requires efficient data collection

**Red Flags**:
- Using polls without mapping to RICO categories
- Ignoring SA votes without checking for "reversed" interpretation
- Assuming a single poll captures all needed information

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3, P5]
-->

---

### P11: Low Consensus + High Importance Requires Discussion

> *"The worst case occurs when a few people feel the principle is extremely important and all the others think it's of no importance at all... significantly more discussion is mandatory."*

**The Principle**: When polling reveals high importance scores from a minority and irrelevance from the majority, pause for deeper discussion—the minority may see something critical others miss.

**Why It Matters**: Implementers or advanced users may understand constraints that retail users don't experience. Per Stroustrup: supporting a useful feature fully is better than preventing all misuses. The minority view deserves exploration.

**When to Apply**: 
- When poll results show bimodal distribution
- When experts and non-experts strongly disagree
- When safety-critical concerns are raised by a few

**Red Flags**:
- Dismissing minority high-importance votes
- Assuming majority irrelevance votes end discussion
- Not investigating why the split exists

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3, P10]
-->

---

### P12: Show Your Work—Don't Rewrite the Lab Notebook

> *"The work invested to arrive at the new solution should be shown; i.e., don't rewrite the lab notebook."*

**The Principle**: Document the evolution from raw motivating reasons to refined principles, showing which were combined, split, or removed—don't just present final polished results.

**Why It Matters**: Transparency enables auditing. Showing evolution helps readers understand why certain principles exist and how they connect to original concerns. It prevents accusations of cherry-picking.

**When to Apply**: 
- When refining raw principles
- When presenting principled-design analysis
- When hybrid solutions emerge from analysis

**Red Flags**:
- Presenting only final refined principles
- Removing traces of eliminated alternatives
- Hiding how hybrid solutions were derived

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P6, P9]
-->

---

### P13: Deprecation Before Ill-Formed

> *"Avoid making well-formed nondeprecated code become ill formed."*

**The Principle**: When removing capability from the language, first deprecate the construct (warning) before making it ill-formed (error) in a subsequent standard.

**Why It Matters**: Users need migration time. Immediate ill-formedness breaks working code without warning. Deprecation signals intent, allows adaptation, and respects the upgrade burden.

**When to Apply**: 
- When proposing to make well-formed code ill-formed
- When removing language features
- When changing parsing rules that affect valid code

**Red Flags**:
- Making code ill-formed without prior deprecation
- Skipping deprecation for "obviously bad" code
- Ignoring the existence of working code using deprecated patterns

**Supporting Experiences**: E3, E5

<!-- METADATA
kind: principle
id: P13
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E3, E5]
related-principles: [P8, P14]
-->

---

### P14: QoI Should Not Determine Portability

> *"Whether a program will compile is guaranteed to be portable; that is, the notion of what makes a TU ill formed is not tied to the QoI of a particular compiler."*

**The Principle**: Avoid solutions where whether code compiles depends on compiler quality—the standard should specify consistent behavior across implementations.

**Why It Matters**: If compiler A diagnoses and rejects code that compiler B accepts, programs lose portability. Users shouldn't have to worry about which compiler's static analysis is better.

**When to Apply**: 
- When solutions involve "diagnose or else" behavior
- When considering implementation-defined compilation outcomes
- When QoI determines error vs. warning

**Red Flags**:
- Solutions that make ill-formedness depend on analysis depth
- Proposals where smarter compilers reject more code
- Inconsistent compilation across toolchains for same source

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P14
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P2, P8]
-->

---

### P15: Don't Trade Diagnosability for Determinism

> *"By making previously undefined behavior well defined, we are no longer able to automatically diagnose such errors of omission."*

**The Principle**: Be cautious of solutions that eliminate security vulnerabilities by making defective behavior defined—this may permanently hide correctness bugs.

**Why It Matters**: Zero-initializing uninitialized variables eliminates the security vulnerability but makes "forgot to initialize" impossible to diagnose. Erroneous behavior preserves diagnosability while eliminating the security hole.

**When to Apply**: 
- When defining previously undefined behavior
- When security fixes might mask correctness bugs
- When choosing between safety and diagnosability

**Red Flags**:
- Solutions that trade diagnosability for safety
- Making "works by accident" behavior permanent
- Closing future debugging capabilities

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P15
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P7, P8]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: The Italian Restaurant Discovery

**Context**: A team of eight people was selecting a venue for a company outing using principled design. One team member proposed a fancy steak restaurant.

**What Happened**: The steak restaurant was everyone's subjective favorite but cost over $200 per person when the budget was $125 (imperative principle). Rather than abandon the concept, the team derived a new solution: an elegant Italian restaurant that satisfied all the steak restaurant's strengths while staying within budget.

**The Outcome**: Success. The Italian restaurant emerged as a clear winner by preserving the best aspects of the failed proposal while complying with the imperative constraint.

**The Lesson**: When a promising solution fails a single imperative principle, look for a hybrid that preserves its strengths. Don't abandon good ideas—evolve them.

> *"The author should append the new solution — the Italian restaurant that derived from the original (steak) restaurant proposal — with its motivation being that the cost is not prohibitive."*

**Supports Principles**: P1, P2, P6, P7, P12

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [principled-design, hybrid-solutions]
supports: [P1, P2, P6, P7, P12]
-->

---

### E2: Erroneous Behavior Beats Zero-Initialization

**Context**: JF Bastien proposed [P2723R0] to zero-initialize uninitialized automatic variables to plug a major security vulnerability affecting ~10% of C++ security issues.

**What Happened**: Jake Fevold applied principled design [P2754R0] comparing Bastien's "always zero-initialize" to Thomas Köppe's "erroneous behavior" alternative. Zero-initialization failed the "doesNotMaskDefects" principle—it would make correctness bugs permanently undiagnosable. Erroneous behavior (EB) scored perfectly on the first seven high-priority principles while zero-initialization failed row 5.

**The Outcome**: Success. Köppe's EB-based solution was adopted by EWG in Varna (June 2023) because principled design proved it was "just as good or better in each individual dimension of interest."

**The Lesson**: Principled design can resolve polarized debates by revealing that one solution dominates another across all relevant criteria. The analysis was "dispositive."

> *"Fevold's comparison paper, using early principled-design concepts, proved dispositive."*

**Supports Principles**: P1, P2, P6, P7, P8, P12, P14, P15

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [erroneous-behavior, uninitialized-variables, security]
supports: [P1, P2, P6, P7, P8, P12, P14, P15]
-->

---

### E3: SG21 Contracts MVP Breakthrough

**Context**: At the SG21 telecon on February 1, 2024, polarized subgroups were proposing incompatible contract solutions with no hope of consensus, risking the Contracts MVP's inclusion in C++26.

**What Happened**: Timur Doumler (assistant SG21 Chair) walked attendees through requirements using principled design [P3113R0]. Lisa Lippincott resurrected a previously discarded solution that wasn't anyone's first or second choice.

**The Outcome**: Success. The solution achieved strong consensus (SF=7, F=5, N=1, A=1, SA=0) because it: (1) provided what was needed for MVP, (2) didn't violate anyone's principles, and (3) allowed space for backward-compatible future improvements.

**The Lesson**: Principled design can break deadlocks by finding solutions that satisfy all imperative constraints even if they're not anyone's favorite. Consensus-building focuses on principles, not solutions.

> *"This solution was no one's first or even second choice but achieved strong consensus."*

**Supports Principles**: P1, P6, P9, P13

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [contracts, SG21, consensus-building]
supports: [P1, P6, P9, P13]
-->

---

### E4: The RICO Poll Discovery

**Context**: The authors needed to collect characterization data from groups efficiently during committee meetings without specialized tooling.

**What Happened**: They discovered that the standard WG21 five-way poll (SF/F/N/A/SA) maps naturally to importance scores (@/9/5/1/-). A single poll captures Relevance (is anything non-SA?), Importance (median excluding SA), and Consensus (fraction non-SA). A follow-up show of hands determines if SA votes mean "irrelevant" or "reversed."

**The Outcome**: Success. Groups can now characterize principles using familiar mechanisms. The coarse granularity was validated through practice—finer gradations caused more debate without improving decisions.

**The Lesson**: Leverage existing committee mechanisms rather than inventing new ones. Coarse scales work better than precise ones for achieving consensus.

> *"This restriction is the result of practicing the methodology and discovering that consensus is better served when the precision with which an answer can be expressed is not allowed to exceed the accuracy."*

**Supports Principles**: P3, P4, P5, P10, P11

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: process/actual
applies-to: both
outcome: success
features: [polling, RICO, committee-process]
supports: [P3, P4, P5, P10, P11]
-->

---

### E5: Most Vexing Parse Solution Evolution

**Context**: The paper analyzes competing solutions for addressing the "most vexing parse" problem where declarations are ambiguously interpreted as functions instead of variables.

**What Happened**: Initial analysis showed deprecation (Solution B) as a clear winner, but solution E (disambiguate for predeclared objects) had complementary strengths. The authors created hybrid Solution F combining B and E, which scored better on lower-priority principles while preserving B's strengths.

**The Outcome**: Mixed. Both B and F emerged as reasonable choices with slightly different tradeoffs—B favors never disambiguating, F allows disambiguation where obvious to humans.

**The Lesson**: When two solutions have complementary strengths, consider combining them. The analysis process naturally reveals combination opportunities.

> *"After preliminary analysis, we saw that our original proposed solution B could benefit from our alternate solution E. Hence, we created a new solution, F, that combines the benefits of both."*

**Supports Principles**: P7, P13

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/mixed
applies-to: language
outcome: mixed
features: [most-vexing-parse, grammar-ambiguity]
supports: [P7, P13]
-->

---

### E6: noexcept Specifier Evolution Without Principled Design

**Context**: The paper references the evolution of `noexcept` specifier behavior on defaulted special member functions across C++11, C++14, and C++17.

**What Happened**: Without principled design, the committee chose option 3 in C++11, changed to option 4 in C++14, and finally settled on option 5 in C++17. Each change reflected late recognition of problems with the previous approach.

**The Outcome**: Failure. Multiple standard revisions were required to reach a stable design. Users experienced churn across three standards.

**The Lesson**: Principled design applied upfront could have identified the optimal solution before C++11 shipped, avoiding years of instability.

> *"One might think the answer is obvious, and it would have been had principled design been applied. Sadly, principled design was not well known when the feature was conceived."*

**Supports Principles**: P2, P6

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [noexcept, defaulted-functions]
supports: [P2, P6]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Writing a Principled-Design Proposal

- [ ] Include status quo (no change) as Solution A
- [ ] Extract motivating principles from every solution, including alternates
- [ ] For each principle, determine if it's binary (predicate) or metric
- [ ] Score each principle's importance: @ (imperative), 9 (high), 5 (medium), 1 (low), - (irrelevant)
- [ ] Score each principle's objectivity: @ (provably), 5 (largely), - (subjective)
- [ ] Rank principles by importance, then objectivity, then subjective pairwise
- [ ] Create compliance table with solutions as columns, ranked principles as rows
- [ ] Analyze row-by-row, documenting elimination decisions
- [ ] Look for hybrid solutions when promising options fail single principles
- [ ] Show evolution from raw motivating reasons to refined principles

**Questions to Ask**:
1. "Does my proposed solution beat status quo on all imperative principles?"
2. "Have I captured the motivating principles of competing proposals fairly?"
3. "Are my principles specific enough to score consistently?"
4. "Have I considered hybrid solutions combining strengths of multiple proposals?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: both
proposal-type: feature
derived-from: [P1, P2, P4, P6, P7, P9, P12]
-->

---

### When Evaluating Proposals in Committee

- [ ] Verify status quo is included as a baseline solution
- [ ] Check that all known alternative solutions are represented
- [ ] Audit principle characterizations (importance, objectivity)
- [ ] Verify principles are actionable and measurable
- [ ] Look for imperative principles that eliminate solutions early
- [ ] Check for solutions that might enable better future evolution (bidirectional compatibility)
- [ ] Watch for QoI-dependent compilation outcomes
- [ ] Consider whether security fixes might mask diagnosability
- [ ] If making code ill-formed, verify prior deprecation occurred

**Questions to Ask**:
1. "Which solutions are eliminated by imperative principles?"
2. "Are there hybrid solutions we haven't considered?"
3. "Does this solution preserve room for future improvement?"
4. "Is well-formed code becoming ill-formed without prior deprecation?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: both
proposal-type: feature
derived-from: [P1, P2, P8, P13, P14, P15]
-->

---

### When Conducting Group Polling on Principles

- [ ] Map SF/F/N/A/SA to @/9/5/1/- importance scores
- [ ] Calculate Relevance: is anything besides SA non-zero?
- [ ] Calculate Importance: median of scores excluding SA votes
- [ ] Calculate Consensus: fraction of non-SA votes
- [ ] For SA votes, ask for show of hands: "irrelevant" or "reversed"?
- [ ] For provable objectivity, require near-unanimous agreement (>80%)
- [ ] For High Consensus + High Importance: brief discussion to confirm
- [ ] For Low Consensus + High Importance: extensive discussion required

**Questions to Ask**:
1. "Did anyone voting SA mean the opposite of this principle?"
2. "Why do some feel this is imperative while others find it irrelevant?"
3. "Is there hidden context that explains the split?"

<!-- METADATA
kind: checklist
category: process/formal
applies-to: both
proposal-type: feature
derived-from: [P3, P10, P11]
-->

---

## Open Questions

1. How should principled design be formally integrated into WG21 procedures beyond SG21?
2. What electronic polling tools would accelerate compliance table construction?
3. How many worked examples are needed before the methodology becomes self-sustaining?
4. Should RICO data be captured in formal minutes for historical record?
5. How to handle principles that experts consider imperative but others don't even understand?

---

## Raw Transcript Reference

Source: D3004R0 "Principled Design for WG21" by John Lakos et al., February 2024 pre-Tokyo mailing
https://wg21.link/d3004r0
