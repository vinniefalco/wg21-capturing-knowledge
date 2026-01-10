# P0559R0 Operating Principles for Evolving C++: Captured Knowledge

**Document Date**: 2017-01-31
**Authors**: JC van Winkel, Jose Daniel Garcia, Ville Voutilainen, Roger Orr, Michael Wong, Sylvain Bonnal
**Document Number**: P0559R0
**Topics Covered**: Committee operating principles, language evolution philosophy, process guidelines, cultural norms, design ground rules

## Executive Summary

P0559R0 is a foundational meta-document that attempts to codify the implicit operating principles of WG21 into explicit guidance. Written in response to concerns about C++ appearing "dead" and the influx of new committee members lacking institutional context, this paper synthesizes Bjarne Stroustrup's original design philosophy with post-C++11 committee evolution practices.

The document establishes three layers of guidance: (1) philosophical principles about change and risk management, (2) procedural norms for the train model and TS handling, and (3) cultural expectations for respectful collaboration. The key tension it addresses is balancing the need for rapid evolution (to keep C++ "alive") against maintaining coherence and consistency with fundamental C++ principles.

Notably, the document explicitly articulates that *inaction is itself risky*—a counterweight to the committee's natural conservatism. It also provides concrete guidance on plenary dynamics, TS prioritization, and conflict resolution between features.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Inaction Carries Risk Equal to Action

> *"Any change carries risk. Doing nothing is also risky."*

**The Principle**: When evaluating whether to accept a proposal, recognize that rejecting or deferring it carries its own risks—the risk of stagnation, missed opportunities, and perceived language death.

**Why It Matters**: Committees naturally favor the status quo. This principle counterbalances that bias by forcing explicit consideration of the cost of *not* acting. A language perceived as "dead" loses developers and investment.

**When to Apply**: Every proposal evaluation, especially when the default instinct is to defer or reject.

**Red Flags**:
- Rejection rationale focuses only on risks of acceptance, never risks of rejection
- "Let's wait and see" without articulating what waiting costs
- Accumulated deferrals creating a perception of stagnation

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P2, P3]
-->

---

### P2: Early Errors Enable Early Fixes

> *"We will make errors. Make them early so that we can fix them."*

**The Principle**: Accept that mistakes will happen and prefer making them early in the process (when correction is cheaper) over attempting to achieve perfection before shipping.

**Why It Matters**: The pursuit of perfection delays progress and often fails anyway. Early integration exposes problems when they can still be addressed, rather than discovering them after standardization when fixes require breaking changes.

**When to Apply**: When debating whether a feature is "ready enough" for integration into a TS or working draft.

**Red Flags**:
- Indefinite deferral seeking "more experience" without concrete criteria
- Refusal to integrate because edge cases aren't fully resolved
- Features that linger in study groups for multiple standard cycles

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P1, P3]
-->

---

### P3: Integrate Early, Back Out If Wrong

> *"Integrate early. And be willing to back out if wrong."*

**The Principle**: Prefer integrating features into the working paper sooner rather than later, with the explicit commitment to remove them if they prove problematic.

**Why It Matters**: Integration enables the committee to build on features (e.g., concepts enabling library improvements) and prevents bikeshedding near release deadlines. The willingness to back out provides a safety net.

**When to Apply**: When deciding whether an "almost ready" grand feature should wait for the next IS or be integrated now.

**Red Flags**:
- "Grand" features repeatedly missing trains due to last-minute bikeshedding
- Dependent features blocked because their prerequisite keeps slipping
- Reluctance to remove problematic features after integration

**Supporting Experiences**: E3, E4

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/timing
applies-to: both
confidence: high
supported-by: [E3, E4]
related-principles: [P1, P2]
-->

---

### P4: Familiarity Is Not Simplicity

> *"Don't confuse familiarity and simplicity. Such confusion hinders and delays major improvements."*

**The Principle**: Evaluate proposals based on actual complexity, not on how unfamiliar they feel. Unfamiliarity with a concept does not mean it is complex; familiarity with a concept does not mean it is simple.

**Why It Matters**: The committee is biased toward familiar patterns even when they are objectively more complex. This principle forces explicit separation of "I don't know this" from "this is complicated."

**When to Apply**: When evaluating novel proposals that feel "too different" or when defending status quo solutions because "everyone knows how to do it this way."

**Red Flags**:
- Rejection because something "feels" complicated without concrete complexity analysis
- Defense of verbose/error-prone patterns because they're "what people know"
- Assuming teaching burden equals inherent complexity

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P10]
-->

---

### P5: Grand Features Take Priority Over Small Ones

> *"Grand project ideas have priority over smaller ones when it comes to conflicts. To prevent small items being a road block for large features."*

**The Principle**: When a small feature conflicts with a larger, more important feature, the large feature should generally win. Small features should not block grand projects.

**Why It Matters**: Without this principle, the accumulation of small decisions can foreclose important future directions. Coordination costs increase when large features must work around many small obstacles.

**When to Apply**: When scheduling work, resolving design conflicts, or when a small proposal would constrain future design space.

**Red Flags**:
- Small features approved without considering impact on pending grand features
- Large features repeatedly redesigned to accommodate small prior decisions
- "We can't do X because we already shipped Y" where Y is minor

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3]
-->

---

### P6: Trust the Subgroup

> *"If a working group (LWG or CWG) had a strong consensus, the motion is put forward and WG21 should generally trust the subgroup."*

**The Principle**: Plenary should defer to subgroup expertise when the subgroup reached strong consensus. Absent members should not reopen settled technical debates in plenary.

**Why It Matters**: Subgroups have the time and expertise for deep technical discussion. Relitigating in plenary wastes time and undermines the subgroup process. Plenary is for coordination, not technical debate.

**When to Apply**: When voting in plenary on subgroup recommendations; when deciding whether to raise objections.

**Red Flags**:
- Extended technical debates in plenary
- "Did you consider X?" questions that reopen settled subgroup discussions
- Absent members blocking progress with concerns not raised in subgroup
- Individual objections presented as national body concerns

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P7]
-->

---

### P7: Dead-Body Votes Require Papers

> *"'Over-my-dead-body' votes on WG21 level need to be followed by a paper describing the concerns in the post-meeting mailing so they can be talked about and weighed just like new proposals are."*

**The Principle**: Strong objections in plenary must be documented in writing so they can be evaluated on technical merit, not just rhetorical force.

**Why It Matters**: Verbal objections can be emotionally compelling but technically weak. Written documentation enables systematic evaluation and prevents repeated re-raising of the same concerns.

**When to Apply**: When someone votes strongly against a proposal in plenary; when evaluating whether objections have been adequately addressed.

**Red Flags**:
- Repeated strong objections without supporting documentation
- Objections that remain vague or shift between meetings
- Inability to point to a paper that documents the concern

**Supporting Experiences**: None documented (procedural norm)

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: []
related-principles: [P6]
-->

---

### P8: TSes Must Have Exit Criteria

> *"When putting out a TS, a list of questions should be prepared that need to be answered before merging the TS into the C++ working paper."*

**The Principle**: Every TS should have explicit criteria for success/failure and clear conditions for when it should be merged into the IS.

**Why It Matters**: Without exit criteria, TSes linger indefinitely—neither providing clarity nor advancing the language. The committee should default to high-priority merging once questions are answered.

**When to Apply**: When proposing a TS; when evaluating whether a TS is ready for merger.

**Red Flags**:
- TSes without documented questions to answer
- TSes that have been active for multiple cycles without evaluation
- Vague "more experience needed" without concrete metrics
- TS proponents who can't articulate success criteria

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: [E7]
related-principles: [P3]
-->

---

### P9: Zero-Overhead Abstraction

> *"What you don't use, you don't pay for (zero-overhead rule)."*

**The Principle**: Features should not impose runtime or compile-time costs on code that doesn't use them.

**Why It Matters**: This is a foundational C++ design principle. Violating it breaks the implicit contract with users who chose C++ for performance predictability.

**When to Apply**: Evaluating any proposal that adds runtime machinery, vtables, type information, or other costs.

**Red Flags**:
- Features that add overhead even when not used
- "Small" costs that accumulate across the codebase
- Hidden allocations or indirections
- Mandatory runtime support structures

**Supporting Experiences**: E8

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: [E8]
related-principles: [P10, P11]
-->

---

### P10: Prefer Library Over Language

> *"Prefer library solutions over language changes if feasible."*

**The Principle**: If a problem can be solved adequately with a library, prefer that over a language change.

**Why It Matters**: Language changes are permanent and affect all users. Libraries can be versioned, replaced, or avoided. Language complexity accumulates permanently.

**When to Apply**: When evaluating whether something should be a core language feature versus a library facility.

**Red Flags**:
- Language proposals that could be libraries with minor inconvenience
- "Compiler magic" when library solutions exist
- Features justified by "nicer syntax" alone

**Supporting Experiences**: None documented (design principle)

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: []
related-principles: [P9, P12]
-->

---

### P11: User-Defined Types Equal to Built-ins

> *"Provide as good support for user-defined types as for built-in types."*

**The Principle**: The language should not privilege built-in types with capabilities unavailable to user-defined types.

**Why It Matters**: This enables abstraction without penalty and allows library authors to create types that feel native. Asymmetry between built-in and user types creates artificial limitations.

**When to Apply**: Evaluating any language feature that affects type behavior; reviewing libraries that define vocabulary types.

**Red Flags**:
- Features that only work with built-in types
- Syntax reserved for language primitives
- Performance differences between built-in and user-defined types doing the same thing

**Supporting Experiences**: E9

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: philosophy/language
applies-to: language
confidence: high
supported-by: [E9]
related-principles: [P9]
-->

---

### P12: Prefer Generality Over Specificity

> *"Prefer generality over specificity: prefer standardizing general building blocks on top of which domain-specific semantics can be layered, as opposed to domain-specific facilities on top of which other domain-specific semantics can't be layered."*

**The Principle**: Standardize composable, general-purpose building blocks rather than domain-specific solutions that can't be extended.

**Why It Matters**: General building blocks enable unforeseen uses and can serve multiple domains. Domain-specific solutions often become obsolete or insufficient as requirements evolve.

**When to Apply**: Evaluating library proposals; deciding the scope of language features.

**Red Flags**:
- Proposals that solve one specific use case
- Designs that can't compose with other features
- Facilities that bake in specific domain assumptions
- "Sealed" abstractions that can't be extended

**Supporting Experiences**: E10

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [E10]
related-principles: [P10, P11]
-->

---

### P13: Teachability as Tiebreaker

> *"If in doubt, pick the variant of a feature that is easiest to teach."*

**The Principle**: When choosing between otherwise equivalent design alternatives, prefer the one that is easier to explain and learn.

**Why It Matters**: Teaching difficulty correlates with cognitive load during use. Features that are hard to teach are hard to use correctly, leading to bugs and frustration.

**When to Apply**: When there are multiple viable designs and technical merit is similar.

**Red Flags**:
- Designs requiring extensive special-case explanations
- Features where experts disagree on the "right" mental model
- Documentation that requires extensive caveats

**Supporting Experiences**: None documented (design heuristic)

<!-- METADATA
kind: principle
id: P13
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: []
related-principles: [P4]
-->

---

### P14: Always Provide a Transition Path

> *"Always provide a transition path."*

**The Principle**: Changes should include a viable migration strategy from existing code. Don't strand users with working code that can't evolve.

**Why It Matters**: C++ codebases are long-lived. Features without transition paths create permanent fragmentation or force expensive rewrites.

**When to Apply**: Any deprecation, breaking change, or feature that supersedes existing practice.

**Red Flags**:
- Deprecations without replacement guidance
- New features that can't interoperate with existing code
- "Just rewrite it" as the migration strategy

**Supporting Experiences**: None documented (design principle)

<!-- METADATA
kind: principle
id: P14
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: []
related-principles: [P1]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: The Perception of Language Death

**Context**: Large companies with significant C++ investment were expressing concerns about the language's trajectory.

**What Happened**: Hiring became difficult because prospective employees perceived C++ as a "dead" or stagnating language. National bodies expressed worry that C++ was not making significant progress.

**The Outcome**: Mixed. This paper itself is a response to these concerns, attempting to articulate principles that would prevent stagnation.

**The Lesson**: The perception of language vitality directly affects its ecosystem health. A language that appears to be "at the end of its development" loses contributors and users.

> *"It is very hard to hire good designers and programmers and hiring is almost impossible if the language of choice is perceived to be at the end of its development ('dead')."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: philosophy/evolution
applies-to: both
outcome: mixed
features: [committee-process]
supports: [P1]
-->

---

### E2: Death by Paralysis and Paper Cuts

**Context**: The committee was observing patterns in how C++ could decline.

**What Happened**: The authors identified two modes of potential failure: (1) "paralysis" from inability to make progress on major features, and (2) "death by a thousand cuts" from accumulating small, incoherent features without a grand vision.

**The Outcome**: This experience motivated the creation of explicit operating principles.

**The Lesson**: Both inaction (paralysis) and unfocused action (small isolated features) are threats. Coherent progress on major features is the path to language health.

> *"...heading towards an accelerated death by paralysis, lack of innovations that tackle modern challenges, and by thousands cuts of small isolated features."*

**Supports Principles**: P1, P5

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: philosophy/evolution
applies-to: both
outcome: mixed
features: [committee-process]
supports: [P1, P5]
-->

---

### E3: The Missing Train Problem

**Context**: The committee operates on a "train model" where features are added when ready.

**What Happened**: "Grand" features that were almost ready would miss the IS deadline, then face renewed bikeshedding in the next cycle, potentially missing yet another train.

**The Outcome**: Repeated delays compounded—each cycle of delay risked additional changes and further delay.

**The Lesson**: Near-ready features should be integrated early so dependent work can proceed and bikeshedding doesn't compound across cycles.

> *"If an almost ready 'grand' feature doesn't make it for an IS, integrate it in the next Working Paper as soon as possible... do not risk bikeshedding near the end of the cycle and thus missing yet another train."*

**Supports Principles**: P2, P3

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: process/timing
applies-to: both
outcome: failure
features: [committee-process]
supports: [P2, P3]
-->

---

### E4: Concepts Enabling Library Work

**Context**: Concepts was a long-awaited language feature that would enable significant library improvements.

**What Happened**: The document notes that integrating concepts early would allow "the committee to build on it in the next version" and enable "the library to use concepts."

**The Outcome**: This illustrates the dependency principle—delayed grand features block dependent work.

**The Lesson**: Grand features unlock subsequent work. Their delay has multiplicative costs.

> *"...the committee can build on it in the next version—e.g. concepts will allow support for the library to use concepts."*

**Supports Principles**: P3, P5

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: process/timing
applies-to: both
outcome: mixed
features: [concepts]
supports: [P3, P5]
-->

---

### E5: Familiarity Bias in Evaluation

**Context**: The committee evaluates proposals from diverse paradigms and approaches.

**What Happened**: Major improvements were being "hindered and delayed" because unfamiliar approaches were conflated with complex or bad approaches.

**The Outcome**: This pattern was recognized as a systematic bias requiring explicit counteraction.

**The Lesson**: Novelty and complexity are orthogonal. Evaluate proposals on actual merits, not gut reactions to unfamiliarity.

> *"Don't confuse familiarity and simplicity. Such confusion hinders and delays major improvements."*

**Supports Principles**: P4

<!-- METADATA
kind: experience
id: E5
source-type: implicit
category: philosophy/tradeoffs
applies-to: both
outcome: mixed
features: [committee-process]
supports: [P4]
-->

---

### E6: Plenary Technical Debates

**Context**: WG21 plenary sessions involve the full committee voting on subgroup recommendations.

**What Happened**: People who were not present during subgroup discussions would raise concerns in plenary, leading to extended technical debates. People who were in the minority in subgroups would attempt to relitigate in plenary.

**The Outcome**: This led to explicit guidance about plenary behavior and the distinction between subgroup and plenary functions.

**The Lesson**: Plenary is for coordination, not technical discussion. Trust the subgroup process.

> *"Plenary is not a forum for extended technical discussion, and there is no provision for 'hold up the feature until I have time to weigh in.'"*

**Supports Principles**: P6

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: process/actual
applies-to: both
outcome: mixed
features: [committee-process]
supports: [P6]
-->

---

### E7: Lingering TSes

**Context**: Technical Specifications were intended as experimental proving grounds for features.

**What Happened**: TSes would be published but then linger indefinitely, never being merged into the working paper nor explicitly abandoned.

**The Outcome**: This motivated the requirement for explicit exit criteria on TS creation.

**The Lesson**: Without explicit success criteria, experiments never conclude.

> *"This prevents TSes from lingering on forever and never making it into the C++ working paper."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: process/formal
applies-to: both
outcome: failure
features: [technical-specifications]
supports: [P8]
-->

---

### E8: The Zero-Overhead Principle Origins

**Context**: C++ has always positioned itself as a systems programming language suitable for performance-critical code.

**What Happened**: The "zero-overhead" principle was established early in C++'s design: features should not impose costs on code that doesn't use them.

**The Outcome**: This became a foundational design constraint for all C++ evolution.

**The Lesson**: Performance predictability is a core C++ value that proposals must respect.

> *"What you don't use, you don't pay for (zero-overhead rule)."*

**Supports Principles**: P9

<!-- METADATA
kind: experience
id: E8
source-type: explicit
category: philosophy/language
applies-to: both
outcome: success
features: [language-design]
supports: [P9]
-->

---

### E9: User-Defined Type Parity

**Context**: Early C++ allowed built-in types to do things user-defined types could not.

**What Happened**: Features like operator overloading, copy constructors, and move semantics were added specifically to allow user-defined types to behave like built-ins.

**The Outcome**: Success—C++ abstractions can achieve performance parity with primitives.

**The Lesson**: Asymmetry between built-in and user-defined types creates artificial limitations on abstraction.

> *"Provide as good support for user-defined types as for built-in types."*

**Supports Principles**: P11

<!-- METADATA
kind: experience
id: E9
source-type: explicit
category: philosophy/language
applies-to: language
outcome: success
features: [operator-overloading, move-semantics]
supports: [P11]
-->

---

### E10: Transactional Memory as Special Case

**Context**: When deciding whether a feature should be a normal proposal or TS.

**What Happened**: Transactional Memory was identified as "special because of hardware support still being in flux"—an example of when the TS route is appropriate.

**The Outcome**: TM went through the TS process to allow experimentation while hardware matured.

**The Lesson**: TSes are appropriate when external factors (hardware, ecosystem) are still uncertain. General building blocks should not be so constrained.

> *"An indication can be if you say something like 'Feature X is special because…'. Example: Transactional Memory is special because of hardware support still being in flux."*

**Supports Principles**: P12, P8

<!-- METADATA
kind: experience
id: E10
source-type: explicit
category: process/navigation
applies-to: both
outcome: mixed
features: [transactional-memory]
supports: [P12, P8]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Any Proposal

- [ ] Does the proposal respect the zero-overhead principle?
- [ ] Could this be a library instead of a language feature?
- [ ] Does it treat user-defined types equally to built-in types?
- [ ] Is there a clear transition path from existing code?
- [ ] Is this the most general solution, or is it domain-specific?
- [ ] What are the risks of *not* accepting this proposal?

**Questions to Ask**:
1. "What does existing code do today, and how does it migrate?"
2. "Can this be implemented without compiler magic?"
3. "Does this impose any cost on code that doesn't use it?"
4. "What other features does this block or enable?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: both
proposal-type: feature
derived-from: [P9, P10, P11, P12, P14]
-->

---

### When Evaluating Timing/Priority

- [ ] Is this a "grand" feature that would unblock other work?
- [ ] Has this been deferred before? What was the cost of delay?
- [ ] Does waiting actually provide more information, or is it procrastination?
- [ ] If this is a TS, what are the explicit exit criteria?

**Questions to Ask**:
1. "What work is blocked waiting for this?"
2. "What happens to C++ if we don't do this?"
3. "What would sufficient experience look like?"

<!-- METADATA
kind: checklist
category: process/timing
applies-to: both
proposal-type: feature
derived-from: [P1, P2, P3, P5, P8]
-->

---

### When Participating in Plenary

- [ ] Was I present in the subgroup discussion?
- [ ] If not, have I consulted with subgroup participants?
- [ ] Is my concern a national body position or personal opinion?
- [ ] If I vote strongly against, am I prepared to write a paper?
- [ ] Am I asking clarifying questions or reopening technical debate?

**Questions to Ask**:
1. "Did the subgroup consider [my concern]?" (answerable Yes/No)
2. "What was the consensus level in subgroup?"

<!-- METADATA
kind: checklist
category: process/formal
applies-to: both
proposal-type: feature
derived-from: [P6, P7]
-->

---

### When Evaluating Design Alternatives

- [ ] Am I conflating unfamiliarity with complexity?
- [ ] Which variant is easiest to teach?
- [ ] Which enables the most future possibilities?
- [ ] Does one option compose better with existing features?

**Questions to Ask**:
1. "How would I explain this to a competent C++ programmer?"
2. "What does this prevent us from doing later?"

<!-- METADATA
kind: checklist
category: philosophy/tradeoffs
applies-to: both
proposal-type: feature
derived-from: [P4, P12, P13]
-->

---

## Design Ground Rules Reference

From Bjarne Stroustrup's D&E and subsequent writings, as endorsed by this paper:

### Core Expression Goals
1. Express ideas directly in code
2. Express relations among ideas directly in code
3. Express independent ideas in independent code
4. Compose code representing ideas freely wherever composition makes sense

### C++ Design Aims
- C++ makes programming more enjoyable for serious programmers
- General-purpose language that is: a better C, supports data abstraction, supports OOP, supports generic programming

### Language-Technical Rules
- No implicit violations of the static type system
- User-defined types equal to built-in types
- Locality is good
- Avoid order dependencies
- Teachability as tiebreaker
- Syntax matters (often perversely)
- Eliminate preprocessor usage

### Low-Level Support Rules
- No gratuitous C incompatibilities (as close as possible, not closer)
- No room for lower-level language below C++ (except assembler)
- Zero-overhead rule
- When in doubt, provide manual control

---

## Open Questions

1. What specific historical examples motivated the "death by paralysis" and "thousand cuts" concerns? The paper alludes to patterns but doesn't enumerate instances.

2. What constitutes "strong consensus" vs "weak consensus" in a subgroup? Is there a quantitative threshold?

3. The paper mentions TSes "may be active at the same time" when conflicting—what happens when both want to merge? Is there a resolution process?

4. How do these principles interact with national body objections, which can block progress regardless of committee consensus?

5. The paper mentions this should be "kept up to date"—were there subsequent revisions addressing post-C++17 evolution?

6. What are the specific "list of libraries where this strategy has failed us" mentioned implicitly through the "maximize successes rather than minimize failures" framing?

---

## Raw Transcript Reference

Source document: P0559R0 "Operating principles for evolving C++"
- Document number: P0559R0
- Date: 2017-01-31
- Available from WG21 paper archive
- Authors: JC van Winkel, Jose Daniel Garcia, Ville Voutilainen, Roger Orr, Michael Wong, Sylvain Bonnal
- Acknowledgments cite Gabriel Dos Reis for assistance
