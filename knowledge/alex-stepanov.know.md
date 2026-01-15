# Alexander Stepanov: Captured Knowledge

**Interview Date**: 2025-12-10
**Interviewer**: Ray Nowosielski
**Duration**: ~92 minutes
**Topics Covered**: STL origins, generic programming, Bjarne Stroustrup, Doug McIlroy, WG21 politics, Concepts conflict, meta-programming critique, academic-industry dynamics, open source philosophy

## Executive Summary

Alexander Stepanov, the creator of the Standard Template Library (STL), provides a foundational perspective on the intellectual origins of generic programming and its path into the C++ standard. His interview reveals the profound debt modern C++ owes to Doug McIlroy's vision of "industrial-scale software component catalogs" and the insight that algorithms are grounded in mathematical abstractions—a revelation Stepanov traces to a literal fever dream.

Most striking is Stepanov's critique of how the C++ ecosystem evolved away from his original focus on algorithms and data structures toward template meta-programming—a technique he views as a necessary implementation detail that incorrectly became "the thing." His candid assessment of WG21 politics, including his complete withdrawal after 1995 and his blunt criticisms of specific committee participants, reveals deep frustration with institutional processes that favor political maneuvering over technical competence.

Stepanov's prescription for the future—that software components should be "open like mathematics" and that standards governance should involve rigorous selection of competent contributors—challenges current community practices and points toward a more academically rigorous model for language evolution.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Keep the Language Close to the Machine

> *"He stuck to one fundamental principle, keep the language close to the machine."*

**The Principle**: A systems programming language must maintain direct correspondence between language constructs and machine operations; abstraction should not obscure the hardware reality.

**Why It Matters**: This is what Stepanov identifies as Bjarne Stroustrup's "fundamental principle" that enabled STL. Generic programming requires predictable performance characteristics, which is only possible when you can reason about machine-level behavior. Languages that abstract away the machine lose the ability to write high-performance generic code.

**When to Apply**: 
- When evaluating language features: do they preserve machine-level reasoning?
- When designing abstractions: can users predict performance from the abstraction?
- When choosing between languages for systems programming

**Red Flags**:
- Abstractions that hide memory allocation patterns
- Features that prevent reasoning about cache behavior
- Language semantics that vary by implementation in performance-critical areas
- "Zero-cost" claims that aren't actually zero-cost

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P4]
-->

---

### P2: Algorithms Are Founded on Mathematical Abstractions

> *"And I realized that behind every algorithm there is a mathematical abstraction on which it is based."*

**The Principle**: Every algorithm depends on underlying mathematical structures (groups, rings, partial orders, etc.); identifying these structures enables generic implementation across any type that satisfies the mathematical requirements.

**Why It Matters**: This insight is the intellectual foundation of generic programming and STL. By identifying the mathematical concept behind an algorithm (e.g., "sort requires a strict weak ordering"), you can implement the algorithm once and have it work on any type that provides that concept. This is why concepts matter—they formalize the mathematical requirements.

**When to Apply**:
- When designing generic algorithms: identify the minimal mathematical requirements
- When reviewing library proposals: are the concept requirements precisely specified?
- When teaching generic programming: start with the mathematics, not the syntax

**Red Flags**:
- Generic code that requires more than mathematically necessary
- Concept definitions that mix mathematical requirements with incidental type requirements
- Algorithms that work for some types but fail for others that should mathematically qualify

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P6]
-->

---

### P3: Software Components Should Be Like Mathematical Knowledge—Openly Available

> *"It has to be not just open source, but really open completely. It's like mathematics. You cannot have proprietary mathematics."*

**The Principle**: Foundational software components (algorithms, data structures, generic libraries) should be treated like mathematical theorems—publicly available, freely usable, and part of shared human knowledge.

**Why It Matters**: Stepanov couldn't find continued funding for STL-style work after its initial success because companies wanted proprietary, obfuscated code. This frustrates cumulative progress. Mathematics advances because results are published and built upon; software component engineering should work the same way.

**When to Apply**:
- When deciding what should be open source vs. proprietary
- When evaluating corporate open source strategies
- When considering the long-term health of software ecosystems

**Red Flags**:
- Companies that obfuscate generic utility code
- Unwillingness to contribute foundational components back to the community
- Treating algorithms and data structures as competitive advantages rather than shared infrastructure

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E5]
related-principles: []
-->

---

### P4: Industrial-Scale Component Catalogs Are the Goal

> *"There should be massive catalogs of algorithms and data structures, which provide different trade-offs, solve different problems, and they should be produced in industrial way."*

**The Principle**: The software industry should produce comprehensive, standardized catalogs of reusable components—algorithms and data structures with well-documented trade-offs—manufactured at industrial scale, not ad hoc.

**Why It Matters**: This was Doug McIlroy's original vision that inspired STL. Software engineering remains immature compared to other engineering disciplines precisely because we lack these catalogs. Every project reinvents basic components. STL was a step toward this vision, but the vision remains largely unrealized.

**When to Apply**:
- When evaluating the strategic direction of standard libraries
- When designing library ecosystems
- When prioritizing standardization efforts

**Red Flags**:
- Standard libraries that are incomplete or inconsistent
- Ecosystems that encourage reinvention over reuse
- Lack of standardized interfaces between components from different sources

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P2]
-->

---

### P5: Technical Work Requires a Champion Who Understands Politics

> *"He pushed STL into the standard. It was his doing. It wasn't my doing for sure... He could manipulate the standard committee."*

**The Principle**: Technically excellent work requires a politically skilled champion to navigate institutional adoption; the technical creator is often not the right person to shepherd standardization.

**Why It Matters**: Stepanov created STL but explicitly credits Bjarne Stroustrup with getting it standardized. Stepanov withdrew from WG21 entirely after 1995, while Bjarne devoted himself to the political work of building consensus. Without this division of labor, STL might never have been standardized despite its technical excellence.

**When to Apply**:
- When planning standardization strategy: identify both the technical expert and the political champion
- When evaluating why technically sound proposals fail
- When advising technical contributors on standards work

**Red Flags**:
- Technical authors without political champions
- Assuming technical excellence alone ensures adoption
- Brilliant contributors who refuse to engage with political realities

**Supporting Experiences**: E3, E6

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E3, E6]
related-principles: [P7]
-->

---

### P6: Meta-Programming Was a Necessary Hack, Not a Goal

> *"Boost migrated away from dealing with algorithms and data structures, which was my concentration, to what they call template meta-programming, which I had to do."*

**The Principle**: Template meta-programming should be understood as implementation machinery required to achieve generic programming, not as a programming paradigm to be celebrated or taught as primary.

**Why It Matters**: Stepanov views meta-programming as something he "had to do" to implement his ideas, not as an end in itself. Boost's focus on meta-programming distracted from the actual goal—algorithms and data structures. This echoes Sean Parent's critique and explains why Stepanov views his relationship with Boost as "tangential."

**When to Apply**:
- When teaching C++: focus on algorithms and generic programming, not template tricks
- When designing libraries: hide meta-programming behind clean interfaces
- When evaluating library contributions: is the goal algorithms and data structures, or showing off techniques?

**Red Flags**:
- Libraries that showcase meta-programming rather than solve problems
- Educational materials that emphasize TMP over generic algorithms
- Community celebration of cleverness over utility

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E4]
related-principles: [P2]
-->

---

### P7: Standards Bodies Need Competence-Based Selection

> *"The mechanism of standard committee doesn't work. It's not a viable mechanism. There has to be done by competent people... There should be some selection. There should be like, you know, French Academy."*

**The Principle**: Standards governance should involve rigorous selection of technically competent participants, similar to academic bodies; open participation without quality filters produces dysfunctional outcomes.

**Why It Matters**: Stepanov's complete withdrawal from WG21 after 1995 reflects his assessment that the process rewards political maneuvering over technical competence. His prescription—an academy model with selection—challenges the open participation model but addresses real concerns about decision quality.

**When to Apply**:
- When designing governance structures for technical standards bodies
- When evaluating why standards processes produce suboptimal outcomes
- When considering reforms to participation models

**Red Flags**:
- Standards bodies where travel budget determines participation
- Technical decisions made by consensus of non-experts
- No mechanism for distinguishing expert opinion from amateur opinion
- Participation driven by employer funding rather than expertise

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/actual
applies-to: both
confidence: medium
supported-by: [E6]
related-principles: [P5]
-->

---

### P8: First Collaborators Who Understand Are Invaluable

> *"The first person who understood, and he became very important collaborator, is Dave Musser."*

**The Principle**: Foundational technical work requires early collaborators who genuinely understand the vision; these first believers amplify and validate ideas that would otherwise remain isolated.

**Why It Matters**: Stepanov names specific individuals—Dave Musser, Andrew Koenig, Meng Lee—as people who understood his vision early and made STL possible. Ideas, no matter how good, need advocates who comprehend them deeply enough to contribute meaningfully and champion them to others.

**When to Apply**:
- When developing new technical ideas: seek out first believers who truly understand
- When evaluating nascent projects: who are the early collaborators, and do they understand the vision?
- When building technical communities: create pathways for deep understanding, not just superficial adoption

**Red Flags**:
- Projects where the lead has no collaborators who deeply understand
- "Followers" who adopt without comprehension
- Isolation of technical visionaries without intellectual community

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P5]
-->

---

### P9: Resistance to Fashionable Ideas Enables Innovation

> *"Part of it is because I am propaganda resistant. Growing up in Soviet Union helped since I figured out that if everybody says something, it doesn't make it true."*

**The Principle**: Innovative technical work often requires resistance to dominant paradigms; skepticism of "what everyone knows" creates space for genuinely new approaches.

**Why It Matters**: Stepanov describes himself as a "professed enemy of object-orientedness" at a time when OOP was the dominant paradigm. This position cost him jobs but enabled STL's value-semantic, generic approach. Propaganda resistance—the ability to question consensus—is essential for paradigm-shifting work.

**When to Apply**:
- When evaluating heterodox technical proposals: is the dissent informed and principled?
- When doing technical work: maintain skepticism of fashionable approaches
- When assessing contributors: value principled disagreement over conformity

**Red Flags**:
- Technical communities that punish dissent
- Proposals justified primarily by appeal to consensus or fashion
- Careers derailed for disagreeing with popular approaches
- Echo chambers where everyone agrees

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P9
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E4]
related-principles: [P6]
-->

---

### P10: Persistent Dedication Over Decades Is Irreplaceable

> *"He is absolutely unique in one fundamental aspect. He started working on C++ in 1978 and he's still working on it... I don't know anyone who could."*

**The Principle**: Language evolution requires sustained individual dedication over decades; there is no substitute for a single person who maintains continuity of vision and investment.

**Why It Matters**: Stepanov identifies Bjarne's multi-decade commitment as "absolutely unique" and essential to C++'s existence. Languages without such stewardship fragment or stagnate. This kind of dedication cannot be institutionalized or distributed—it's inherently personal.

**When to Apply**:
- When assessing language health: is there sustained individual stewardship?
- When planning succession: recognize what cannot be replaced by process
- When evaluating language choices: consider the dedication of the steward

**Red Flags**:
- Languages without clear individual stewardship
- Assumption that committees can replace individual vision
- Stewards who lose interest or move on
- Fragmentation of vision among competing factions

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: history/successes
applies-to: language
confidence: high
supported-by: [E1]
related-principles: [P5]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Bjarne's Unique Dedication to C++

**Context**: Stepanov reflecting on what made C++ successful and enabled his own work.

**What Happened**: Bjarne Stroustrup started working on C++ in 1978 and, at the time of the interview, continues working on it—nearly 50 years of sustained dedication. He travels to give talks everywhere, including community colleges, and maintains a consistent philosophy of keeping the language close to the machine.

**The Outcome**: Success. C++ became and remains a dominant systems programming language. Stepanov explicitly credits this dedication as enabling his own work: "I owe him a great deal because he enabled my work to materialize."

**The Lesson**: Language success requires irreplaceable individual dedication spanning decades. Bjarne's consistent vision and tireless advocacy created the stable foundation on which STL could be built.

> *"He is absolutely unique in one fundamental aspect. He started working on C++ in 1978 and he's still working on it... He would go, he will get invited to some community college to give a talk. He goes."*

**Supports Principles**: P1, P10

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [C++, language-stewardship]
supports: [P1, P10]
-->

---

### E2: Doug McIlroy's Vision and STL's Origins

**Context**: Stepanov tracing the intellectual origins of STL to a talk he heard decades before he could implement it.

**What Happened**: Doug McIlroy, whom Stepanov calls "a forgotten great computer scientist," gave a talk proposing that software should have "massive catalogs of algorithms and data structures" produced in an industrial way. McIlroy was behind Bell Labs computer science and, in Stepanov's view, neither Unix nor C nor C++ would have existed without him. Later, while delirious with fever, Stepanov realized that algorithms are grounded in mathematical abstractions—the insight that enabled generic programming.

**The Outcome**: Success. The vision materialized as STL, which brought industrial-scale component catalogs to reality (at least partially). The mathematical foundation enabled truly generic algorithms.

**The Lesson**: Foundational technical ideas often have long gestation periods. McIlroy's vision preceded its realization by decades. The insight connecting algorithms to mathematics enabled the practical implementation.

> *"That was a talk by Doug McIlroy... There should be massive catalogs of algorithms and data structures, which provide different trade-offs, solve different problems, and they should be produced in industrial way."*

**Supports Principles**: P2, P4

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/decisions
applies-to: library
outcome: success
features: [STL, generic-programming, component-catalogs]
supports: [P2, P4]
-->

---

### E3: The Collaborators Who Made STL Happen

**Context**: Stepanov describing the people who understood his vision and helped realize it.

**What Happened**: Dave Musser was the first person who understood Stepanov's ideas and became an important collaborator. Andrew Koenig "understood what I was trying to do much faster than anybody else in the C++ community" and suggested submitting STL to the standard library. Meng Lee "literally forced me to start"—she "fired up FrameMaker, put me in front of the computer, and fed me papaya" to keep him working. Bjarne, while initially not understanding, became "a hundred percent supportive" once he did and spent "literally all his time pushing STL."

**The Outcome**: Success. Through these collaborators—an early believer (Musser), a connector (Koenig), an implementer (Lee), and a political champion (Bjarne)—STL went from vision to standard.

**The Lesson**: Technical innovation requires different kinds of collaborators: those who understand deeply, those who connect to communities, those who force practical progress, and those who navigate politics. No single person can fill all these roles.

> *"The person who actually helped me start is Meng Lee... She literally forced me to start. Andrew is a remarkable guy... he understood what I was trying to do much faster than anybody else. He pushed STL into the standard. It was his doing."*

**Supports Principles**: P5, P8

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [STL, standardization, collaboration]
supports: [P5, P8]
-->

---

### E4: Stepanov's Anti-OOP Stance and Career Consequences

**Context**: Stepanov explaining his opposition to object-oriented programming and its effects on his career.

**What Happened**: Stepanov describes himself as "the professed enemy of object-orientedness" at a time when OOP was the dominant paradigm. He attributes his resistance to growing up in the Soviet Union, where he learned that "if everybody says something, it doesn't make it true." HP Labs hired him, then "discovered that I'm not object oriented." He was "forced out of multiple jobs" because of his stated position against OOP.

**The Outcome**: Mixed. Professionally costly (job losses), but technically vindicated—STL's value-semantic, generic approach has proven more influential than many OOP designs.

**The Lesson**: Resistance to fashionable paradigms can cost careers but enable innovation. Stepanov's skepticism of OOP was essential to creating the generic programming approach that became STL.

> *"I'm the professed enemy of object-orientedness... I have been forced out of multiple jobs because of my stated position. Growing up in Soviet Union helped since I figured out that if everybody says something, it doesn't make it true."*

**Supports Principles**: P6, P9

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/decisions
applies-to: both
outcome: mixed
features: [OOP, generic-programming, career]
supports: [P6, P9]
-->

---

### E5: The Failure to Fund Post-STL Work

**Context**: Stepanov describing his inability to continue STL-style work after its initial success.

**What Happened**: After STL was standardized, Stepanov could not find any company that would fund continued development of algorithmic libraries. Companies like Google, Adobe, and Microsoft "want to obfuscate code and make it ugly." The work that should have continued—extending the component catalog—had no institutional home because corporations treat such work as either non-proprietary (thus not worth funding) or competitive advantage (thus requiring obfuscation).

**The Outcome**: Failure. The vision of comprehensive, industrial-scale component catalogs remains largely unrealized because the funding model for such work doesn't exist outside academia, and academia is "totally enthralled with Google, Amazon, Meta."

**The Lesson**: Foundational software component work has a funding gap—it's too generic for proprietary investment, too practical for pure academia. This is why Stepanov advocates for treating such work like mathematics: openly available and publicly funded.

> *"Right after I did STL, I couldn't ever find a place which would fund development of further work... Every place wants to obfuscate code and make it ugly. Google, Adobe, Microsoft."*

**Supports Principles**: P3

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [STL, funding, open-source]
supports: [P3]
-->

---

### E6: Stepanov's Complete Withdrawal from WG21

**Context**: Stepanov explaining why he never attended WG21 meetings after STL's standardization.

**What Happened**: After 1995 and STL's passage into the standard, Stepanov "did not attend a single meeting." He describes WG21 as "one of the most unpleasant things" and observes that "people who join the committee are people who like travel, because you go to Europe once a year." He acknowledges some competent participants (Andrew Koenig "did know what he was talking about") but expresses broad skepticism about the mechanism. He proposes instead a "French Academy" model with rigorous selection of competent participants.

**The Outcome**: Mixed. Stepanov preserved his sanity and productive capacity by withdrawing, but lost direct influence over C++ evolution. The Concepts debacle (which he references obliquely) might have unfolded differently with his involvement.

**The Lesson**: Standards processes that reward political skill over technical competence drive away technical contributors. This creates a filtering effect where the people making decisions are not necessarily the most technically qualified.

> *"I did not attend a single meeting. I stayed totally out of all this politics. It's highly, I mean, the standard committees one of the most unpleasant things... The mechanism of standard committee doesn't work."*

**Supports Principles**: P5, P7

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/decisions
applies-to: both
outcome: mixed
features: [WG21, standards-politics, governance]
supports: [P5, P7]
-->

---

### E7: The Concepts Political Failure

**Context**: Stepanov commenting on the Concepts debacle from the outside.

**What Happened**: Doug Gregor (from Andrew Lumsdaine's Indiana team) implemented a working version of Concepts. Bjarne Stroustrup worked with Gabriel Dos Reis on a competing approach but, in Stepanov's blunt assessment, "Gabby doesn't know how to program" so no implementation materialized. "Bjarne was not prepared to make compromises" and "was determined not to let Indiana guys push the thing even if it was ready." The result was neither version being adopted.

**The Outcome**: Failure. Technically sound, implemented work was rejected due to political conflict. Concepts eventually entered C++20, a decade later.

**The Lesson**: When prominent figures entrench on competing proposals, political dynamics can override technical merit. Implementation doesn't guarantee adoption if politics intervene.

> *"Bjarne was not prepared to make compromises... was determined not to let Indiana guys push the thing even if it was ready. Doug Gregor did do an implementation. This is true of fact."*

**Supports Principles**: P5, P7

<!-- METADATA
kind: experience
id: E7
source-type: tacit
category: history/failures
applies-to: language
outcome: failure
features: [concepts, C++11, politics]
supports: [P5, P7]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Does the design identify the mathematical abstractions underlying the algorithms? (P2)
- [ ] Are concept requirements minimal and mathematically grounded? (P2)
- [ ] Does the abstraction preserve reasoning about machine-level behavior? (P1)
- [ ] Is meta-programming confined to implementation, not exposed in API? (P6)
- [ ] Would this fit in a comprehensive catalog of components with documented trade-offs? (P4)
- [ ] Is the proposal suitable for open, public knowledge sharing? (P3)

**Questions to Ask**:
1. "What is the mathematical concept this algorithm requires?"
2. "Can users predict the performance characteristics from the interface?"
3. "Is template meta-programming visible to users, or hidden in implementation?"
4. "How does this fit with other components in the library—are interfaces consistent?"
5. "Is this something that should be open, shared infrastructure?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P3, P4, P6]
-->

---

### When Reviewing Language Proposals

- [ ] Does this feature maintain direct correspondence with machine operations? (P1)
- [ ] Does it enable better expression of mathematical abstractions in algorithms? (P2)
- [ ] Will it simplify or complicate generic programming? (P2, P6)
- [ ] Is there a technical champion AND a political champion? (P5)
- [ ] Has this been rejected before? If so, what's different politically? (P7)

**Questions to Ask**:
1. "Can users still reason about machine-level behavior with this feature?"
2. "Does this help express algorithmic requirements more clearly?"
3. "Who will shepherd this through the political process?"
4. "What is the political landscape for this proposal?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P1, P2, P5, P6, P7]
-->

---

### When Assessing Standards Process Health

- [ ] Are technically competent contributors participating or withdrawing? (P7)
- [ ] Is travel budget or employer funding determining participation? (P7)
- [ ] Are there political deadlocks between prominent figures? (P5, P7)
- [ ] Is there rigorous selection of participants, or open participation without filtering? (P7)
- [ ] Are decisions documented with technical rationale? (P7)

**Questions to Ask**:
1. "Who has withdrawn from the process, and why?"
2. "What determines who participates—expertise or logistics?"
3. "Are competing proposals being synthesized or fought over?"
4. "Is this decision being made by people who deeply understand the technical issues?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P5, P7]
-->

---

## Open Questions

1. What specific algorithms and data structures did Stepanov want to develop after STL but couldn't find funding for?

2. What is Stepanov's view on C++ Concepts as finally standardized in C++20—does it resemble what he envisioned?

3. What would Stepanov's "French Academy" model for standards governance look like concretely?

4. What specific critique does Stepanov have of Herb Sutter's advice to "always use deque"?

5. What is Stepanov's current view on the state of generic programming in C++ and other languages?

6. What mathematical abstractions does Stepanov believe are still missing from STL/standard library?

7. What is Stepanov's assessment of Rust, Swift, and other languages that have adopted generic programming ideas?

8. Who does Stepanov consider the most competent current WG21 participants?

9. What was Stepanov's relationship with Dave Abrahams and the early Boost community?

10. What is Stepanov's view on the future of the "component catalog" vision—is it being realized anywhere?

---

## Raw Transcript Reference

Source: `inputs/alex-stepanov.md`
Original: `BOOST_ALEXANDER_STEPANOV_STRINGOUT_v00.md`
