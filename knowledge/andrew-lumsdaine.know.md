# Andrew Lumsdaine: Captured Knowledge

**Interview Date**: 2026-01-15
**Interviewer**: Ray Nowosielski
**Source**: BOOST_ANDREW_LUMSDAINE_STRINGOUT_v00.md
**Topics Covered**: Boost history, generic programming, concepts saga, standardization philosophy, peer review process, community dynamics, diversity, Boost decline

## Executive Summary

Andrew Lumsdaine led the Open Systems Lab at Indiana University, which contributed foundational Boost libraries including the Boost Graph Library, Lambda, and MultiArray. His perspective spans both the technical (generic programming, template metaprogramming) and the institutional (university research funding enabling open source contributions, committee politics).

His most valuable insights concern the "virtuous circle" of standardization: features need substantial real-world experience before standardization because "standards are forever." Boost served this function by allowing programmers to "kick the tires" on both libraries and language extensions implemented via template metaprogramming. The tragic story of C++11 concepts—two competing proposals (Indiana vs. Texas A&M), a compromise brokered by Stepanov, then both sides getting "cold feet" leading to removal at Frankfurt—illustrates what happens when this virtuous circle is short-circuited.

Lumsdaine also provides frank observations about community dynamics: the competitive "hubris aspect" of proving yourself through code created environments that correlated with gender exclusion, and Boost eventually became "a victim of its own success" as standardized libraries created dependency fragmentation.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Standardization Requires Extensive Prior Experience

> *"Standardization really needs to emerge after there's a lot of experience with whatever's being standardized."*

**The Principle**: Features should only be standardized after substantial real-world usage has validated their design; premature standardization creates permanent mistakes.

**Why It Matters**: "Standards are forever." Unlike library code that can be revised, standardized features become permanent API contracts. The concepts failure in C++11 illustrates the cost of attempting to standardize before sufficient experience existed.

**When to Apply**: When evaluating any proposal for standardization, especially language features.

**Red Flags**:
- Proposals without implementations that have been used in production
- "We'll figure out the details during standardization"
- Features that haven't been tested outside the proposer's team
- Rushing to meet a standard deadline

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P2]
-->

---

### P2: Boost as a Proving Ground for Language Extensions

> *"Boost gave the ability for other people to evaluate it, both in just being able to access the library, play with it, as well as through the peer review process... it also allowed people to play with new language features, kick the tires on new language features."*

**The Principle**: Template metaprogramming allows library-level experimentation with language-like features, providing a safer proving ground than direct language changes.

**Why It Matters**: Boost.Lambda, Boost.Bind, and similar libraries demonstrated language features (lambdas, better binding) at the library level before they became C++11 language features. This allowed real-world validation without committing the standard.

**When to Apply**: When evaluating whether a feature should be a library or language feature, and when designing experiments to validate language feature proposals.

**Red Flags**:
- Language feature proposals without library-level prototypes
- Assuming library experimentation is unnecessary for language features
- Skipping the "tire-kicking" phase

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: belongs/language
applies-to: language
confidence: high
supported-by: [E1]
related-principles: [P1]
-->

---

### P3: Template Flexibility Was Deliberate, Not Accidental

> *"When the template system was being developed... they deliberately made design decisions to open up the possibility of new things to make it flexible and composable, extensible. I don't think they knew in particular would end up with this thing, but they knew that if they made it sufficiently flexible that something could happen, something would happen."*

**The Principle**: C++ templates' metaprogramming capabilities were not an accident but the result of deliberate design decisions to enable unforeseen extensions.

**Why It Matters**: This reframes template metaprogramming from "exploitation of a bug" to "intended use of designed flexibility." Language designers should consider building in similar deliberate extensibility.

**When to Apply**: When evaluating language design decisions and understanding the philosophy behind C++ features.

**Red Flags**:
- Dismissing template metaprogramming as a hack or accident
- Language designs that close off unforeseen uses
- Over-specifying features to prevent "misuse"

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: history/decisions
applies-to: language
confidence: high
supported-by: [E3]
related-principles: []
-->

---

### P4: Peer Review for Open Source Was Pioneering

> *"That kind of process didn't really exist, certainly in the open source community. And I think Boost was one of the first examples of this peer review process of open source software... some ideas borrowed from the science typical research world of doing peer review."*

**The Principle**: Boost pioneered applying academic-style peer review to open source software, predating modern code review practices.

**Why It Matters**: Before GitHub pull requests and CI/CD review steps became standard, Boost established that open source quality required formal review. This model influenced the broader open source ecosystem.

**When to Apply**: When establishing quality processes for library collections or standards track.

**Red Flags**:
- Open source projects without any review process
- Assuming "open source" automatically means quality
- Review processes that are purely mechanical (CI only)

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/formal
applies-to: library
confidence: high
supported-by: [E4]
related-principles: []
-->

---

### P5: Competitive Hubris Excludes Diverse Contributors

> *"A lot of it had to do just with the vibe of the communities... this interest in trying to prove yourself to other programmers, to make sure... your code would be held in high regard, sometimes did result in explicit competition and maybe not an environment that was really conducive to certain other ways of interacting and learning and promoting your work."*

**The Principle**: Competitive, prove-yourself cultures in technical communities create environments that systematically exclude contributors who prefer collaborative over competitive interaction styles.

**Why It Matters**: Lumsdaine observed only ~2-3% women representation across Boost and committee meetings. Research he cites links this to competitive "vibe" that correlates with gender exclusion. This represents lost talent and perspectives.

**When to Apply**: When designing community norms, evaluating contribution processes, or assessing why certain groups are underrepresented.

**Red Flags**:
- "Survival of the fittest" attitudes toward contributions
- Public code criticism without constructive purpose
- Celebrating "takedowns" or harsh reviews
- Homogeneous contributor demographics

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/actual
applies-to: both
confidence: medium
supported-by: [E5]
related-principles: []
-->

---

### P6: Compromise Proposals Can Fail When Either Side Gets Cold Feet

> *"Between the first vote and the next vote... essentially Indiana and Texas A&M got cold feet about the compromise proposal. We really decided that, no, this feature we thought was important and we compromised on really was important and we can't compromise on it after all."*

**The Principle**: Brokered compromises between competing proposals can collapse if either party later decides their concessions were too costly.

**Why It Matters**: The concepts saga shows that even a compromise blessed by a respected arbiter (Stepanov) can fail if parties later reconsider. Compromises need genuine buy-in, not just tactical agreement.

**When to Apply**: When evaluating proposals that emerged from compromise, or when attempting to broker compromises between competing approaches.

**Red Flags**:
- Parties agreeing to compromise under time pressure
- Compromises where both sides still advocate for their original position
- No mechanism to prevent later defection
- Parties who "agree to disagree" on fundamental issues

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P1]
-->

---

### P7: Success Can Create Dependency Fragmentation

> *"Because boost as it was evolving also was interdependent. Libraries that were in Boost were dependent on other libraries that were in Boost. But as some of those libraries moved from Boost to becoming standardized, the code that was dependent on the original libraries still stayed the same. People didn't go back... In some sense, Boost was a victim of its own success."*

**The Principle**: When foundational libraries are standardized, dependent code that doesn't migrate creates fragmentation between the original and standardized versions.

**Why It Matters**: Boost's internal dependencies meant that standardizing core libraries (smart pointers, bind, function) left remaining Boost libraries dependent on pre-standard versions. Migrating would have been a "huge effort."

**When to Apply**: When planning standardization of libraries with many dependents, or when evaluating the health of library ecosystems.

**Red Flags**:
- Standardizing libraries without migration plans for dependents
- Ecosystem where foundational libraries have many dependents
- No resources allocated for post-standardization migration
- Assuming standardization is "done" once the vote passes

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/evolution
applies-to: library
confidence: high
supported-by: [E6]
related-principles: []
-->

---

### P8: Innovation Requires Going Beyond the Edge

> *"We do new things by going to the edge of what's possible and going a little further. And so I think that's what Boost did in a lot of ways, was it went to the edge of what was possible in the language, and then went a little bit further. And I think in the case of concepts, it was at the time, just a little bit too far."*

**The Principle**: Meaningful innovation requires pushing past known limits, but this inherently risks going too far.

**Why It Matters**: Boost's value came from pushing boundaries—but the concepts effort pushed past what could be standardized at the time. This is not a failure of ambition but an inherent risk of innovation.

**When to Apply**: When evaluating ambitious proposals or understanding why some efforts fail despite being technically sound.

**Red Flags**:
- Dismissing ambitious proposals as "too far out"
- Equally: assuming all ambitious proposals will succeed
- Not distinguishing "too early" from "wrong direction"
- Risk aversion that prevents any boundary-pushing

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P8
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E2]
related-principles: [P1]
-->

---

### P9: Research Funding Enables Open Source Contribution

> *"Thanks to support we got from the National Science Foundation, I was able to hire these students and hire these postdocs and it just was... templates weren't an accident in C++."*

**The Principle**: University research funding (NSF, endowments) can enable sustained open source contribution that commercial entities may not fund.

**Why It Matters**: Indiana's Boost contributions (BGL, Lambda, MultiArray, concepts work) were possible because of research funding that paid graduate students and postdocs. This model enabled work that was too speculative or foundational for commercial sponsorship.

**When to Apply**: When considering how to fund long-term open source or standards work.

**Red Flags**:
- Assuming volunteers can sustain major library development
- No funding model for foundational/speculative work
- Over-reliance on commercial sponsors with short-term interests

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E7]
related-principles: []
-->

---

### P10: STL Revealed the Power of Generic Programming

> *"I ran across the standard template library and the scales just kind of fell from my eyes and I realized, yes, this is the way to write a program once and be able to reuse it in all of these different situations."*

**The Principle**: STL demonstrated that generic programming could achieve both flexibility and performance, fundamentally changing how C++ should be written.

**Why It Matters**: Before STL, C++ was "really all about objects and creating object hierarchies and inheritance." STL showed an alternative paradigm that Boost then propagated to mainstream programming.

**When to Apply**: When evaluating library design approaches or understanding C++ design philosophy.

**Red Flags**:
- Library designs that ignore STL idioms
- Over-reliance on inheritance hierarchies
- Coupling algorithms to specific data structures

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E3]
related-principles: [P3]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Boost as Language Feature Proving Ground

**Context**: Boost libraries like Lambda and Bind implemented language-like features (anonymous functions, partial application) purely through template metaprogramming.

**What Happened**: These library implementations allowed programmers to "kick the tires" on what would become C++11 language features. Users gained real experience with the concepts (anonymous functions, better binding) before they were baked into the language standard.

**The Outcome**: Success. C++11 included language-level lambdas and std::bind informed by years of Boost experience. The library-level prototypes validated the designs.

**The Lesson**: Template metaprogramming provides a safe proving ground for language features—real usage without permanent commitment.

> *"It also allowed people to play with new language features, kick the tires on new language features."*

**Supports Principles**: P1, P2

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [boost-lambda, boost-bind, cpp11-lambda]
supports: [P1, P2]
-->

---

### E2: The Concepts Saga—Frankfurt Failure

**Context**: Both Indiana (Lumsdaine, Siek, Gregor) and Texas A&M (Stroustrup, Dos Reis) developed concepts proposals for C++11 with "fundamental incompatibilities" around conformance checking (structural vs. nominal).

**What Happened**: The two groups asked Alex Stepanov to referee. A meeting at Adobe produced a compromise proposal that passed an initial committee vote. However, between that vote and the final Frankfurt meeting, "both sides got cold feet" and decided their compromised features were actually essential. At Frankfurt, the decision was to remove concepts entirely from C++11.

**The Outcome**: Failure (at the time). Lumsdaine was "so upset that I walked down the street... went to a music store, and bought a guitar." The first song: "Comfortably Numb." Concepts wouldn't be standardized until C++20, nearly a decade later.

**The Lesson**: Compromise proposals can collapse when parties later reconsider their concessions. Additionally, concepts may have been "a little bit too far"—insufficiently validated before standardization was attempted.

> *"Maybe that's what happened because part of what Boost was doing... was it went to the edge of what was possible in the language, and then went a little bit further. And I think in the case of concepts, it was at the time, just a little bit too far."*

**Supports Principles**: P1, P6, P8

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [concepts, cpp11, cpp20]
supports: [P1, P6, P8]
-->

---

### E3: Templates' Deliberate Flexibility

**Context**: Template metaprogramming was sometimes characterized as an "accidental side effect" of the template system.

**What Happened**: Lumsdaine disputes this characterization. While Bjarne and others developing templates "didn't know in particular would end up with this thing," they "deliberately made design decisions to open up the possibility of new things"—making templates "flexible and composable, extensible."

**The Outcome**: This design decision enabled STL, Boost, and the entire generic programming paradigm in C++.

**The Lesson**: The flexibility that enabled template metaprogramming was intentional, even if the specific applications weren't foreseen.

> *"They knew that if they made it sufficiently flexible that something could happen, something would happen."*

**Supports Principles**: P3, P10

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/decisions
applies-to: language
outcome: success
features: [templates, generic-programming]
supports: [P3, P10]
-->

---

### E4: Boost Pioneered Open Source Peer Review

**Context**: Before GitHub and modern CI/CD, open source projects typically lacked formal review processes.

**What Happened**: Boost established a formal peer review process, borrowing concepts from academic scientific review. This was "one of the first examples of this peer review process of open source software."

**The Outcome**: Success. Boost's review process became a model. Today, "typical continuous integration and continuous development process, particularly with Git... there's a step for doing review"—but Boost helped establish this norm.

**The Lesson**: Applying academic peer review concepts to open source software was a pioneering contribution that influenced the broader ecosystem.

> *"That kind of process didn't really exist, certainly in the open source community."*

**Supports Principles**: P4

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [boost-review-process, peer-review]
supports: [P4]
-->

---

### E5: Gender Representation in C++ Community

**Context**: Lumsdaine observed representation across Boost meetings and committee meetings over many years.

**What Happened**: He recalls meeting only ~2-3% women across these events. Research he references suggests this correlates with the competitive "vibe"—the "interest in trying to prove yourself to other programmers" and "explicit competition" that created environments "not really conducive to certain other ways of interacting and learning."

**The Outcome**: Mixed/ongoing. The low representation represents lost perspectives and talent.

**The Lesson**: Competitive prove-yourself cultures systematically exclude contributors who prefer collaborative interaction styles, which correlates with gender.

> *"One of the reasons that women are so unrepresented... a lot of it had to do just with the vibe of the communities."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: process/actual
applies-to: both
outcome: mixed
features: [community-diversity]
supports: [P5]
-->

---

### E6: Boost as Victim of Its Own Success

**Context**: Many foundational Boost libraries were standardized in C++11 (smart pointers, bind, function, etc.).

**What Happened**: Remaining Boost libraries depended on original Boost versions of these standardized components. Migrating to use the standardized versions "would've been a huge effort." So Boost libraries continued depending on pre-standard Boost components even as users adopted standard versions.

**The Outcome**: Decline. "A lot of the libraries that really addressed specific gaps in C++... did become part of C++ 11. So there were less obvious gaps to fill." Combined with dependency fragmentation, Boost's momentum slowed.

**The Lesson**: Success (standardization) can create fragmentation when dependents don't migrate, and filling the most important gaps leaves less compelling work.

> *"In some sense, Boost was a victim of its own success."*

**Supports Principles**: P7

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/successes
applies-to: library
outcome: mixed
features: [boost-decline, cpp11-standardization]
supports: [P7]
-->

---

### E7: NSF Funding Enabled Indiana Contributions

**Context**: Indiana University's Open Systems Lab contributed multiple foundational Boost libraries.

**What Happened**: National Science Foundation grants and the Lily endowment funded graduate students (Jeremy Siek) and postdocs (Jaakko Jarvi, Doug Gregor, Ron Garcia) who developed Boost Graph Library, Lambda, MultiArray, and the concepts proposal.

**The Outcome**: Success. This research-funded model produced libraries that became part of C++ and influenced language design (concepts eventually in C++20).

**The Lesson**: Research funding enables sustained, speculative open source work that commercial entities typically won't fund.

> *"Thanks to support we got from the National Science Foundation, I was able to hire these students and hire these postdocs."*

**Supports Principles**: P9

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: process/actual
applies-to: both
outcome: success
features: [nsf-funding, indiana-university, boost-graph-library]
supports: [P9]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Evaluating Language Feature Proposals

- [ ] Has there been substantial real-world experience with this feature (not just prototypes)?
- [ ] Has a library-level implementation been used to "kick the tires"?
- [ ] Is the proposal attempting to standardize before sufficient validation?
- [ ] If this is a compromise between competing proposals, do all parties genuinely accept it?
- [ ] Are there fundamental incompatibilities being papered over?

**Questions to Ask**:
1. "What real-world usage validates this design?"
2. "Has this been prototyped at the library level?"
3. "If this is a compromise, what did each side give up, and are they truly okay with it?"
4. "Is this being rushed to meet a standard deadline?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P1, P2, P6]
-->

---

### When Planning Library Standardization

- [ ] What libraries depend on the library being standardized?
- [ ] Is there a migration plan for dependents?
- [ ] Are resources allocated for post-standardization migration?
- [ ] Will standardization create version fragmentation?

**Questions to Ask**:
1. "What depends on this, and how will those dependents migrate?"
2. "Who will do the migration work, and is it funded?"
3. "What happens to code that doesn't migrate?"

<!-- METADATA
kind: checklist
category: philosophy/evolution
applies-to: library
proposal-type: feature
derived-from: [P7]
-->

---

### When Assessing Community Health

- [ ] Is the community culture competitive or collaborative?
- [ ] What is the demographic composition of contributors?
- [ ] Are there interaction styles that are implicitly discouraged?
- [ ] Does the "vibe" welcome diverse approaches to contribution?

**Questions to Ask**:
1. "What does 'proving yourself' look like in this community?"
2. "Who succeeds here, and who doesn't—and why?"
3. "Are there contribution paths that don't require competitive displays?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: feature
derived-from: [P5]
-->

---

## Notable People Mentioned

- **Jeremy Siek**: Graduate student at Notre Dame, math major, co-author of Boost Graph Library, co-developer of concepts
- **Doug Gregor**: "Very few people like Doug"—able to grasp all three C++ paradigms, brilliant and highly productive, contributed to C++11 including concepts
- **Jaakko Jarvi**: Author of Boost Lambda, variadic templates, "many things in C++11"
- **Ron Garcia**: Author of Boost MultiArray
- **Alex Stepanov**: Creator of STL, "one of my best friends," brokered concepts compromise, "at the peak of his powers" when Lumsdaine met him
- **Beman Dawes**: "Progenitor" of Boost
- **Dave Abrahams**: "Very active person in both Boost and the C++ committee"
- **Bjarne Stroustrup**: Designed templates with deliberate flexibility, led Texas A&M concepts proposal
- **Gabriel Dos Reis**: Co-author of Texas A&M concepts proposal

---

## Open Questions

1. What were the specific technical details of structural vs. nominal conformance in the concepts debate?
2. What was the exact timeline between the compromise and Frankfurt—how long did parties have to reconsider?
3. How did the Indiana/Texas A&M concepts experience influence the eventual C++20 concepts design?
4. What specific interventions could address the competitive culture's exclusionary effects?
5. Did any Boost libraries successfully migrate to use standardized components, and if so, how?

---

## Raw Transcript Reference

Source: `inputs/andrew-lumsdaine.md`
Original: `BOOST_ANDREW_LUMSDAINE_STRINGOUT_v00.md`
