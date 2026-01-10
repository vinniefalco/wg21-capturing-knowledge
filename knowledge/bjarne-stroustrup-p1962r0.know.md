# Bjarne Stroustrup (P1962R0): Captured Knowledge

**Document Date**: 2019-11-18
**Audience**: EWG and LEWG
**Document Type**: Position Paper
**Topics Covered**: Design philosophy, committee process, intellectual humility, feature evaluation, stability, field experience

## Executive Summary

This position paper from C++'s creator argues for greater intellectual humility and rigor in WG21's decision-making processes. Stroustrup contends that the committee has become excellent at technical implementation details but has grown somewhat superficial in evaluating fundamental design questions. He warns against fashion-driven design, union-of-all-needs bloat, and the insufficiency of common arguments used to justify features ("my company does it," "all modern languages have it").

The paper advocates for a "cut until nothing left to cut" design philosophy, emphasizing minimal initial designs that grow based on feedback rather than anticipating every need upfront. Stroustrup stresses that stability is a feature, that feature interactions are among the hardest problems, and that neither arguments nor data alone are conclusive—both require careful interpretation. The paper serves as a meta-level critique of committee process, urging members to distinguish fashion from long-term value and to approach design decisions with the humility appropriate to defining a language for decades of use.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Non-Technical Arguments Are Insufficient

> *"'I think so' is not a technical argument. 'My company does it' is not a conclusive argument. 'I badly need it' is not a conclusive argument. 'All modern languages have it' is not a conclusive argument. 'We can implement it' is a necessary but not sufficient reason to accept a feature."*

**The Principle**: Reject proposals whose justification relies primarily on personal opinion, company practice, urgency, industry trends, or implementation feasibility alone—require genuine technical merit and broader applicability.

**Why It Matters**: These arguments appeal to authority, fashion, or narrow interests rather than demonstrating that a feature solves an important problem well for the broader C++ community. A feature that "all modern languages have" may not fit C++'s design constraints; a feature one company badly needs may be a poor fit for others.

**When to Apply**: When evaluating the motivation section of any proposal; when assessing arguments made in committee discussions; when writing a proposal's justification.

**Red Flags**:
- Motivation section dominated by "Other languages do this"
- Justification relies heavily on a single company's use case
- "Implementability" presented as the primary argument for acceptance
- Appeals to what's fashionable rather than what's fundamental

**Supporting Experiences**: E1, E4

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: evaluation/motivation
applies-to: both
confidence: high
supported-by: [E1, E4]
related-principles: [P2, P8]
-->

---

### P2: Voting Majorities Are Necessary But Not Sufficient

> *"I think that simply adding up votes and seeing if there is a 3-1 majority is a mistake. We need such a majority and preferably more for consensus, but it is not sufficient, especially not when there are relatively few people in the room, when it's late in the week and people are tired, and when key and/or long-serving members are elsewhere."*

**The Principle**: A vote clearing the threshold does not establish consensus—consider who voted, who was absent, who strongly opposed and why, the timing of the vote, and whether the room was representative.

**Why It Matters**: Rooms are self-selected; proponents are typically more motivated and articulate than defenders of the status quo. Votes taken late in a meeting week, with few attendees, or without key experts present may not reflect true committee sentiment.

**When to Apply**: Interpreting any committee vote; deciding whether to advance a proposal after a close vote; assessing whether a feature has genuine consensus.

**Red Flags**:
- Vote taken late Friday with sparse attendance
- Strong opposition from long-serving members dismissed as "they always oppose things"
- Vote margin just clears threshold
- Key domain experts absent during the vote
- Proponents significantly outnumber opponents in the room

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P1, P8]
-->

---

### P3: Distinguish Fashion From Long-Term Value

> *"Today, we have different fashions, but it is still difficult to determine what's long-term useful and what's 'just fashion.' It is easy to get swept up in what is currently fashionable. Which problems are worth-while solving and how are both subject to fashions."*

**The Principle**: Before accepting a feature, critically examine whether it addresses a genuinely enduring problem or merely reflects current programming trends that may pass.

**Why It Matters**: Standards define a language for decades. Fashions in programming come and go—features standardized during a fad become permanent legacy. The committee has nearly followed several fashions that later proved misguided.

**When to Apply**: Evaluating any proposal that aligns with current industry trends; when a feature is justified by what "modern" languages do; when something feels like it's "obviously" needed.

**Red Flags**:
- Feature justified primarily by current industry buzz
- "Every modern language does this" as primary motivation
- No consideration of whether the trend will persist
- Feature addresses a problem that only recently became popular to discuss
- Lack of historical perspective on similar past proposals

**Supporting Experiences**: E1, E4

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E1, E4]
related-principles: [P1, P6]
-->

---

### P4: Focus on "What" and "Why" Before "How"

> *"I suggest we should look more at use patterns and interfaces, at least initially, and less on implementation details. Implementations tend to improve over years (and decades) provided the user interfaces and models of use are clean. We need to focus on 'what?' and 'why?' more than 'how?'"*

**The Principle**: Prioritize clean user interfaces and usage models over implementation details; a good interface can accommodate improving implementations, but a poor interface cannot be fixed post-standardization.

**Why It Matters**: Implementation techniques improve over time, but standardized interfaces are permanent. Over-focusing on implementation details can lock in suboptimal designs that prevent future optimization. The standard differs from products by requiring stability over decades.

**When to Apply**: Early proposal evaluation; design discussions; choosing between alternative designs; when a proposal spends more pages on implementation than motivation and interface.

**Red Flags**:
- Proposal dominated by implementation discussion with minimal interface analysis
- Design choices driven by what's easiest to implement today
- Over-specification that constrains future implementations
- No discussion of usage patterns or user mental models
- "Detailed controls" that force programmers to be overly specific about "how"

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: philosophy/library
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P6, P10]
-->

---

### P5: Feature Interaction Is Among the Hardest Problems

> *"No language feature (or library) exists in isolation (or at least it shouldn't). Feature interaction is among the hardest of problems, and often underestimated both as a problem and as something useful."*

**The Principle**: Always analyze how a proposed feature interacts with existing language features and standard library components, including features still under development.

**Why It Matters**: Poorly considered interactions lead to surprising corner cases, teachability problems, and the need for endless patches. Conversely, well-designed interactions create emergent power. Post-major-improvement cleanup is inevitable because we cannot anticipate all interactions.

**When to Apply**: Evaluating any proposal; design review; when a proposal claims to be "orthogonal" to existing features; when assessing completeness of a proposal.

**Red Flags**:
- Proposal doesn't discuss interaction with related features
- "This is orthogonal to X" claimed without analysis
- Proposal creates new special cases or exceptions to general rules
- No consideration of interaction with features under concurrent development
- Feature requires special handling that doesn't generalize

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: philosophy/coherence
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P6, P7]
-->

---

### P6: Start Minimal, Grow Based on Feedback

> *"There are two fundamental ways of approaching the unavoidable uncertainty in a design: add 'improvements' until everybody feels well served [or] cut until there is nothing left to cut and all there is left is principled and fundamental."*

**The Principle**: Prefer minimal initial designs focused on what's fundamental, clean, and essential; grow features through generalization based on real feedback rather than trying to anticipate every need upfront.

**Why It Matters**: The committee process naturally converges on unions of all stated needs—this is bloat. Not all stated needs are real or important for most C++ programmers. Trying to anticipate every need generates permanent bloat. Growth should be generalization, not patches adding special cases.

**When to Apply**: Initial feature design; evaluating feature scope; when a proposal keeps growing with "last-minute improvements"; revision strategy decisions.

**Red Flags**:
- Feature scope keeps expanding to satisfy everyone
- "Last-minute improvements" added before votes
- Design accommodates every stated use case
- Patches upon patches adding special cases
- No clear "nucleus" or fundamental core to the design

**Supporting Experiences**: E4, E5

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E4, E5]
related-principles: [P4, P5, P7]
-->

---

### P7: Articulate Who Benefits and Who Suffers

> *"When considering a problem, we should always try to articulate 'who benefits?' 'how do they benefit?' 'how significant are the benefits?' ... Also, 'who might suffer new problems?' Be specific and concrete; 'average users can't …' is neither."*

**The Principle**: Proposals must specifically and concretely identify beneficiaries, the nature and significance of benefits, and potential negative impacts on others—vague appeals to "average users" are insufficient.

**Why It Matters**: Every proposal carries costs: committee time, implementation, documentation, teaching, dealing with older implementations. Benefits must be weighed against these costs with specificity. Serving one group's needs perfectly might harm the broader community.

**When to Apply**: Evaluating motivation sections; writing proposals; assessing cost/benefit tradeoffs; when proposals claim broad benefit without evidence.

**Red Flags**:
- Vague beneficiary claims ("users will benefit")
- No discussion of who might be negatively affected
- Benefits claimed without quantification or concrete examples
- Costs dismissed or not enumerated
- "Average programmer" invoked without definition or evidence

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: evaluation/motivation
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P1, P6]
-->

---

### P8: Neither Arguments Nor Data Are Conclusive Alone

> *"Neither arguments nor data are by themselves conclusive. We are far too good at fooling ourselves with clever arguments and data always require interpretation."*

**The Principle**: Require both logical arguments and empirical data, and subject both to critical interpretation—clever arguments can mislead, and data without proper analysis proves nothing.

**Why It Matters**: Technical communities excel at constructing persuasive arguments that may not withstand scrutiny. Data from experiments or field use requires proper methodology to interpret. The academic literature's strength is rigorous interpretation of experimental data.

**When to Apply**: Evaluating any evidence presented for a proposal; when arguments seem "too clever"; when data is presented without analysis methodology; when reviewing field experience claims.

**Red Flags**:
- Proposal relies solely on logical argument without empirical support
- Data presented without methodology or interpretation
- "Obvious" conclusions drawn from limited data
- Arguments that sound compelling but resist verification
- No consideration of alternative interpretations of evidence

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P1, P12]
-->

---

### P9: Individual Experience Is Narrow and Incomplete

> *"Our experiences are necessarily narrow and incomplete. The C++ world is too large and diverse for anyone to know all, and anyway, problems and styles of solutions change over time. Your perception of your company's or industry's needs may not be correct and even when they are, they may not be conclusive for the whole C++ community."*

**The Principle**: No individual's or company's experience is representative of the entire C++ community; serving narrow needs perfectly might harm the broader community.

**Why It Matters**: C++ is used across extraordinarily diverse domains—embedded, games, finance, scientific computing, systems programming. What works for one domain may be wrong for others. Even correct perceptions of local needs don't generalize.

**When to Apply**: Evaluating proposals from single-company or single-domain origins; weighing expert testimony; considering one's own strong opinions; when proposals claim universal benefit.

**Red Flags**:
- All evidence from a single company or domain
- "In my experience" without acknowledgment of limitations
- No consideration of other usage domains
- Assumption that one domain's problems are universal
- Proposal shaped entirely by one group's workflow

**Supporting Experiences**: E1, E4

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: evaluation/scope
applies-to: both
confidence: high
supported-by: [E1, E4]
related-principles: [P1, P7, P12]
-->

---

### P10: Stability Is a Feature

> *"Stability is a feature as well as a serious design constraint. It is always frustrating when old code and old design approaches stand in the way of 'progress' but people really hate it when their code is broken."*

**The Principle**: Treat backward compatibility as a valuable feature, not merely a constraint; C++ programs from 20 years ago still run, and this durability is a key argument for C++ adoption.

**Why It Matters**: Billions of lines of code exist. Millions of textbooks, blogs, and programmer mental models depend on current behavior. The promise that today's code will run in 20 years is a competitive advantage for C++. Deprecation has never really worked in practice.

**When to Apply**: Evaluating breaking changes; considering deprecation; assessing migration cost of new features; when "progress" arguments conflict with compatibility.

**Red Flags**:
- Proposal breaks existing valid code
- "Just deprecate the old way" without realistic migration plan
- Assumption that users will happily rewrite working code
- Underestimation of existing code volume affected
- Changes that silently change meaning of valid programs

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P4, P5]
-->

---

### P11: Implementation Experience Can Prematurely Freeze Design

> *"Implementation experience is usually beneficial for improving a design, but implementation work tends to freeze a design so that alternatives and improvements might be ignored. It is generally unwise to implement before the fundamental requirements and principles have been articulated (preferably in writing) and the key use cases have been chosen."*

**The Principle**: Articulate requirements, principles, and key use cases in writing before implementing—implementation investment creates inertia that resists design changes.

**Why It Matters**: Once significant implementation effort exists, psychological and practical pressures resist revisiting fundamental design questions. Alternatives may go unexplored not because they're inferior but because switching costs seem too high.

**When to Apply**: Early proposal development; deciding when to begin implementation; evaluating proposals with heavy implementation investment; when implementation details drive design discussions.

**Red Flags**:
- Implementation begun before requirements documented
- "We've already implemented it" used to resist design changes
- Design alternatives dismissed due to implementation switching costs
- Implementation details constraining interface design
- Sunk cost fallacy affecting design decisions

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P4, P12]
-->

---

### P12: Usage Experience Is Valuable But Limited

> *"Usage experience reports are most valuable, but they are hard to get and impossible to get at scale. Usually, we have to make do with the experiences of a small group of self-selected, usually way-above-averagely-capable enthusiasts."*

**The Principle**: Value usage experience highly but interpret it cautiously—early adopters are self-selected enthusiasts who are not representative of typical users, and reports from small coherent groups don't predict behavior at scale.

**Why It Matters**: Self-selected early adopters are typically far more capable than average users. A feature that works well for experts may fail when deployed broadly. Small, coherent teams may not encounter problems that arise in diverse, large-scale deployment.

**When to Apply**: Evaluating field experience claims; assessing readiness for standardization; interpreting user feedback; when "our users love it" is claimed.

**Red Flags**:
- All feedback from expert early adopters
- Experience limited to a single small team
- No usage data from "ordinary" programmers
- Enthusiast bias in positive reports
- No feedback from users who tried and abandoned the feature

**Supporting Experiences**: E2, E5

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E2, E5]
related-principles: [P8, P9, P11]
-->

---

### P13: Present Disadvantages and Alternatives Honestly

> *"Every design has advantages, disadvantages, and limitations. We should never present a design without a serious and honest discussion of possible problems and alternatives. It is part of a proposer's job to examine problems; 'pure sales jobs' are not intellectually honest."*

**The Principle**: Proposals must include honest discussion of disadvantages, limitations, and alternative approaches—omitting these makes a proposal a "sales job" rather than a serious technical document.

**Why It Matters**: Committee members cannot make informed decisions without understanding tradeoffs. Hidden problems surface post-standardization when they're impossible to fix. Joint pro-and-con papers (like the coroutines papers) provide immense value.

**When to Apply**: Writing proposals; reviewing proposals; when a proposal seems "too good"; when alternatives are dismissed too quickly.

**Red Flags**:
- No "Alternatives Considered" section
- Disadvantages minimized or omitted
- Alternative designs strawmanned or dismissed without analysis
- Proposal reads like marketing material
- No acknowledgment of limitations or failure modes

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P13
source-type: explicit
category: evaluation/red-flags
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P7, P8]
-->

---

### P14: Ground Major Proposals in Theory and Literature

> *"The ideal proposal reflects both some theory and some practical experience. We should also be more careful considering related (often academic) literature. For major proposals, there is always some related literature."*

**The Principle**: Major proposals should engage with relevant academic literature and theoretical foundations—there is always prior art for significant features.

**Why It Matters**: Academic literature provides peer-reviewed analysis, empirical studies, and theoretical frameworks that can inform design. Ignoring existing research risks repeating known mistakes or missing known solutions.

**When to Apply**: Writing major proposals; evaluating novel features; when a proposal claims to solve a problem "for the first time"; when assessing theoretical soundness.

**Red Flags**:
- No references to academic literature
- Claims of novelty without literature survey
- Ignoring known theoretical results
- Reinventing solutions without acknowledging prior art
- No theoretical framework for design decisions

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P14
source-type: explicit
category: evaluation/motivation
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P8, P13]
-->

---

### P15: No Single Principle Is Absolute

> *"Design involves balancing different concerns and principles. There is never a single absolute and unbreakable principle that we can blindly follow. This is the reason that D&E lists a couple of dozen 'rules of thumb.'"*

**The Principle**: Apply design principles as heuristics to be balanced against each other—no principle should be followed blindly or elevated above all others.

**Why It Matters**: Real design involves tradeoffs between competing concerns. Dogmatic application of any single principle leads to suboptimal designs. Good judgment requires weighing multiple principles in context.

**When to Apply**: When principles conflict; when someone argues for an absolute rule; when a design decision seems to violate a principle but feels right.

**Red Flags**:
- "We must always X" without nuance
- Single principle invoked to override all others
- No consideration of competing concerns
- Dogmatic adherence to one approach
- Inability to articulate tradeoffs

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P15
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P6, P8]
-->

---

### P16: Committee Size Amplifies Feature Pressure

> *"We have a committee with 300+ members. It seems that essentially every member has a feature or two that they'd like to get into the language, and many have several. I have not changed my opinion that adding too many features could 'sink C++.'"*

**The Principle**: The large committee size creates structural pressure toward feature bloat—be aware that the union of all members' wishes would overwhelm the language.

**Why It Matters**: With 300+ members each wanting 1-2 features, the pressure to add is enormous. The committee can do much, or do things fast, but not both while maintaining quality and coherence. Restraint and selectivity are essential.

**When to Apply**: Assessing overall committee direction; prioritizing proposals; when "just one more feature" is argued; when evaluating workload.

**Red Flags**:
- Treating all proposals as equally deserving of time
- "We can do everything" attitude
- Lack of prioritization mechanism
- Features advanced primarily because they have a champion
- Volume of proposals overwhelming review capacity

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P16
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P6, P7]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: The Fashions That Nearly Were

**Context**: The C++ committee has existed through multiple programming paradigm fashions, each with enthusiastic proponents.

**What Happened**: At various times in C++ history, there were strong movements advocating:
- All functions should be members
- Every function should be virtual
- All data members should be protected (public data was "old school")
- Garbage collectors were essential

Stroustrup notes: "I suspect that a committee with the composition of today's committee would have followed these fashions."

**The Outcome**: Mixed. These fashions passed without being standardized as mandatory. However, the pressure was real, and the current committee faces similar pressures with different fashions.

**The Lesson**: What seems "obviously correct" at any given time may simply be fashion. The committee must distinguish genuine long-term value from transient trends, recognizing that current "obvious" needs may look as dated as these examples in 20 years.

> *"Today, we have different fashions, but it is still difficult to determine what's long-term useful and what's 'just fashion.'"*

**Supports Principles**: P1, P2, P3, P8, P9

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/decisions
applies-to: both
outcome: mixed
features: [virtual-functions, member-functions, protected-data, garbage-collection]
supports: [P1, P2, P3, P8, P9]
-->

---

### E2: Concepts—Decades to Maturity

**Context**: Stroustrup wanted to specify constraints on template arguments from the inception of templates.

**What Happened**: The journey to C++20 concepts spanned decades:
- Mid-1980s: Began looking at ways to specify generic arguments
- Earlier: Discovered that macro-based techniques didn't scale
- Followed literature for more than a decade
- 2003: Published foundational work
- Work involved "experimentation, implementation, academic publishing, committee papers, use, teaching"
- User-visible design essentially stable by ~2015
- Post-2015 changes were "expert/implementer details" not user improvements

**The Outcome**: Success—concepts became part of C++20, considered "a necessary completion of the design of templates and an essential part of the support of generic programming."

**The Lesson**: Major features require decades of development, theory, implementation, and practical experience. The right design emerges from sustained engagement with theory, practice, and feedback—not from rushing to implementation.

> *"I consider concepts a necessary completion of the design of templates and an essential part of the support of generic programming."*

**Supports Principles**: P4, P5, P8, P11, P12, P14, P15

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [concepts, templates, generic-programming]
supports: [P4, P5, P8, P11, P12, P14, P15]
-->

---

### E3: RAII—Deep Roots in Practice

**Context**: Constructor/destructor pairs and RAII are now considered foundational to C++.

**What Happened**: In 1979, these features "seemed to come out of nowhere" to many observers. But they had "deep roots in operating systems practice" and reflected Stroustrup's "inability to express those established practices directly in the languages of the time."

**The Outcome**: Success. Stroustrup considers this "the real foundation of C++."

**The Lesson**: The most valuable features often formalize established practices that lack direct expression. Theory and prior practice provided the foundation; implementation followed principled understanding of the problem.

> *"I consider this the real foundation of C++."*

**Supports Principles**: P4, P5, P10, P14, P15

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [RAII, constructors, destructors, resource-management]
supports: [P4, P5, P10, P14, P15]
-->

---

### E4: Remember the Vasa

**Context**: The Vasa was a Swedish warship that sank on its maiden voyage in 1628, overloaded with features (guns, ornate decorations) that made it unstable.

**What Happened**: Stroustrup references his earlier paper P0977 "Remember the Vasa!" as a warning about feature bloat. He notes that "the flood of new proposals has increased" since that paper, and observes: "I think we are trying to do too much too fast. We can do much or do less fast. We cannot do both and maintain quality and coherence."

**The Outcome**: Ongoing concern. The warning remains unheeded—feature proposals continue to accelerate.

**The Lesson**: Adding too many features can "sink C++." The committee must become more restrained and selective. Quality and coherence require either doing less, or doing things more slowly.

> *"I have not changed my opinion that adding too many features could 'sink C++.' Remember the Vasa!"*

**Supports Principles**: P1, P3, P6, P9, P16

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/failures
applies-to: both
outcome: mixed
features: [committee-process, feature-bloat]
supports: [P1, P3, P6, P9, P16]
-->

---

### E5: The Coroutines Pro-Con Papers

**Context**: Coroutines were a contentious proposal with competing camps holding different views on design tradeoffs.

**What Happened**: People from "opposing camps" collaborated to produce joint papers examining both use cases and tradeoffs ([Use] P1493) and implementation impact ([Impact] P1492). These papers presented balanced analysis rather than advocacy.

**The Outcome**: Success. Stroustrup describes these papers as "immensely useful."

**The Lesson**: Joint pro-and-con papers from people with opposing views provide far more value than single-perspective advocacy papers. This collaborative, honest approach to examining tradeoffs should be a model for other contentious proposals.

> *"The joint 'pro- and con-papers' on coroutines written by people from 'opposing camps' were immensely useful."*

**Supports Principles**: P6, P7, P12, P13

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [coroutines, collaborative-papers]
supports: [P6, P7, P12, P13]
-->

---

### E6: Operator Dot—Four Decades of Incompleteness

**Context**: One of Stroustrup's fundamental aims since 1979 is providing "equally good support for user-defined and built-in types."

**What Happened**: The very first extension proposal in 1980 was for operator dot. Without it, users cannot build "a simple and general smart reference, a proxy" or types that fully match built-in behavior for types with public members. Multiple attempts to add this feature have failed.

**The Outcome**: Failure to date. C++ remains incomplete without `operator.()` or equivalent.

**The Lesson**: Some gaps in the language design remain unfilled for decades, even when the need was identified at the very beginning. Long-standing gaps may indicate genuinely hard problems, but they don't become less important with time.

> *"The very first extension proposal in 1980 was for an operator dot. C++ is not complete without operator.() or equivalent."*

**Supports Principles**: P4, P5

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/regrets
applies-to: language
outcome: failure
features: [operator-dot, proxy-types, smart-references]
supports: [P4, P5]
-->

---

### E7: Contracts—Three Failures

**Context**: Contracts (invariants, preconditions, postconditions) have deep theoretical roots going back to Peter Naur (mid-1970s) and Bertrand Meyer's Eiffel.

**What Happened**: Before the C++20 failure, there were two previous failed attempts to add contracts to C++. The proposal for C++20 also failed. Stroustrup notes that the "continuation" aspect of contracts is "relatively novel, backed mostly by logical arguments and experience at Bloomberg."

**The Outcome**: Failure (three times). Stroustrup urges: "We should consider why."

**The Lesson**: Repeated failures on the same feature indicate deep unresolved issues. The novel aspects of proposals (like continuation semantics) may lack sufficient field experience compared to established aspects. Understanding why past attempts failed is essential before trying again.

> *"Note that before the failure of the proposals for C++20, two previous attempts had also failed. We should consider why."*

**Supports Principles**: P8, P11, P12, P14

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/failures
applies-to: both
outcome: failure
features: [contracts, invariants, preconditions, postconditions]
supports: [P8, P11, P12, P14]
-->

---

### E8: Spaceship and Concepts—Timing Judgments

**Context**: Stroustrup offers his assessment of the committee's timing on recent major features.

**What Happened**: "I think we were far too slow for concepts and far too fast for <=>" (the spaceship operator).

**The Outcome**: Mixed. Both features were standardized, but the process could have been better paced.

**The Lesson**: The committee doesn't have a consistent calibration for feature readiness. Some features are over-deliberated while others are rushed. Being "systematic, careful, and consistent in our reasoning" requires developing better judgment about appropriate pace.

> *"I am not arguing that we should slow down or speed up decisions. For example, I think we were far too slow for concepts and far too fast for <=>."*

**Supports Principles**: P2, P11, P12

<!-- METADATA
kind: experience
id: E8
source-type: tacit
category: process/timing
applies-to: both
outcome: mixed
features: [concepts, spaceship-operator]
supports: [P2, P11, P12]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Any Proposal

- [ ] Does the motivation rely on non-technical arguments ("my company does it," "modern languages have it")?
- [ ] Has the proposal distinguished fashion from long-term value?
- [ ] Does it focus on "what" and "why" more than "how"?
- [ ] Are feature interactions with existing language/library analyzed?
- [ ] Is the design minimal and principled, or a union of all stated needs?
- [ ] Are beneficiaries and potential harm specifically identified?
- [ ] Are disadvantages and alternatives honestly discussed?
- [ ] Is there engagement with relevant literature and theory?
- [ ] Is there evidence beyond clever arguments?

**Questions to Ask**:
1. "Who specifically benefits from this, and how?"
2. "Who might be harmed, and how?"
3. "What are the disadvantages and limitations?"
4. "What alternatives were considered and why were they rejected?"
5. "Is this solving an enduring problem or a current fashion?"
6. "How does this interact with feature X/Y/Z?"

<!-- METADATA
kind: checklist
category: evaluation/red-flags
applies-to: both
proposal-type: feature
derived-from: [P1, P3, P4, P5, P6, P7, P13, P14]
-->

---

### When Evaluating Field Experience Claims

- [ ] Is there experience from users outside the proposer's organization?
- [ ] How long has the implementation been in use?
- [ ] Are the users representative or self-selected enthusiasts?
- [ ] Has it been used at scale or only in small coherent teams?
- [ ] Were requirements and principles articulated before implementation?
- [ ] Is the implementation investment creating resistance to design changes?

**Questions to Ask**:
1. "Who outside your organization has used this?"
2. "How capable were the users compared to typical C++ programmers?"
3. "Were the requirements written down before implementation began?"
4. "What problems did users encounter?"
5. "Have any users tried and abandoned the feature?"

<!-- METADATA
kind: checklist
category: evaluation/field-experience
applies-to: both
proposal-type: feature
derived-from: [P8, P9, P11, P12]
-->

---

### When Interpreting Committee Votes

- [ ] Was attendance representative of the full committee?
- [ ] Were relevant domain experts present?
- [ ] What time of day/week was the vote?
- [ ] Who strongly opposed, and why?
- [ ] Were proponents overrepresented in the room?
- [ ] Was this a self-selected audience?

**Questions to Ask**:
1. "Who was absent that should have been consulted?"
2. "Why did the opponents oppose this?"
3. "Was the room self-selected toward proponents?"
4. "Should this be re-confirmed with broader attendance?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: feature
derived-from: [P2, P9]
-->

---

### When Assessing Backward Compatibility

- [ ] Does this break existing valid code?
- [ ] What is the volume of code affected?
- [ ] Is migration realistic at scale?
- [ ] Does this silently change the meaning of valid programs?
- [ ] Can existing idioms coexist with the new approach?

**Questions to Ask**:
1. "How much existing code would this break?"
2. "What is the migration path for affected code?"
3. "Does this preserve the promise that today's code works in 20 years?"

<!-- METADATA
kind: checklist
category: philosophy/evolution
applies-to: both
proposal-type: feature
derived-from: [P10]
-->

---

## Open Questions

1. **Specific features criticized**: What specific features does Stroustrup consider to have been "far too fast" (besides <=>)? What specific fashions is the current committee following?

2. **Quality metrics**: Is there a way to measure "quality and coherence" of the language to track whether the Vasa problem is manifesting?

3. **Successful minimal designs**: What are examples of features that successfully followed the "cut until nothing left" approach and grew well?

4. **Failed union-of-needs designs**: What are specific examples of features that became "union-of-all-needs" bloat?

5. **Fashion detection**: Is there a process or framework for identifying when something is fashion vs. long-term value?

6. **Committee composition**: Has the committee's composition changed in ways that affect its susceptibility to fashions?

7. **Operator dot history**: What specifically caused the three previous operator dot attempts to fail?

8. **Contracts analysis**: What does Stroustrup believe are the reasons contracts have failed three times?

---

## Key Quotes for Reference

> "We are defining a language for decades of use. A bit of humility is necessary."

> "Cut until there is nothing left to cut and all there is left is principled and fundamental."

> "Implementations tend to improve over years (and decades) provided the user interfaces and models of use are clean."

> "Every design has advantages, disadvantages, and limitations. We should never present a design without a serious and honest discussion of possible problems and alternatives."

> "We can do much or do less fast. We cannot do both and maintain quality and coherence."

> "Say not 'This is the truth' but 'So it seems to me to be as I now see the things I think I see.'"

---

## Raw Document Reference

P1962R0 "How can you be so certain?" by Bjarne Stroustrup, 2019-11-18
