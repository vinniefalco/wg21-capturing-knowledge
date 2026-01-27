# Bjarne Stroustrup: Captured Knowledge

**Interview Date**: 2025-10-28  
**Interviewer**: Ray Nowosielski  
**Location**: Manhattan, New York  
**Duration**: ~69 minutes  
**Topics Covered**: WG21 governance, Boost history, language/library design interdependence, STL adoption, committee growth and fragmentation, ASIO/networking standardization failure, profiles, Beman Dawes legacy

## Executive Summary

Bjarne Stroustrup, creator of C++, provides a candid assessment of WG21's evolution and limitations. His central concern is the loss of cohesion: the committee has grown from ~100 members to 527, work happens in isolated subcommittees, and the Direction Group's advice is easily ignored. He explicitly states "I would have liked to see some kind of secretariat or core group that could set direction" but acknowledges he lacked the organizational skills to make this happen.

A recurring theme is the **feature interaction problem**—the failure to ensure that features and libraries work together coherently. He cites `variant`, `any`, and `optional` as examples where independently-designed Boost libraries ended up with incompatible interfaces despite solving related problems. This reflects his Bell Labs background where "the feature interaction problem was considered an absolutely essential problem that had to be dealt with."

Stroustrup also reveals significant regret about how standardization began: representatives from IBM, Sun, and HP "twisted my arm" into agreeing to ANSI standardization when he felt it was "too early." The resulting ISO process fragmented decision-making and prevented the unified vision he would have preferred. His proposed solution—profiles—represents an attempt to create coherent subsets that provide guarantees (safety, performance, teaching) without further bloating the language.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Language Design Is Library Design, and Vice Versa

> *"A language design is library design. And the library design is language design. So when you design a library, you basically extend a language that is language design. And when you design language features, you are directing what can be done in terms of library design."*

**The Principle**: Language features and library components must be designed together; separating them leads to suboptimal solutions in both.

**Why It Matters**: When library and language groups work in isolation, libraries compensate for language limitations with complexity (template metaprogramming), while language features miss opportunities to enable better library design. The STL succeeded precisely because Alex Stepanov worked with Bjarne to fix C++ for generic programming before building the library.

**When to Apply**: When evaluating any proposal—ask whether it's solving a problem that should be addressed in the other domain (language vs library).

**Red Flags**:
- Library doing heroic template metaprogramming to work around language limitations
- Language feature designed without considering library implications
- Proposal presented only to EWG or only to LEWG without cross-group discussion
- "We'll fix it in the library" or "we'll fix it in the language" as response to design concerns

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: philosophy/coherence
applies-to: both
confidence: high
supported-by: [E1, E2]
related-principles: [P2, P5]
-->

---

### P2: Committees Tend Toward Union, Not Intersection

> *"There's a tendency for committees to choose the union of everybody's desires... and it is a very common thing and very hard to avoid."*

**The Principle**: Committee decision-making naturally produces bloat by accepting the union of all desired features rather than finding the minimal solution that serves the most important use cases.

**Why It Matters**: Bloat accumulates—each feature seems individually justified but the cumulative effect is a language/library too large to learn, implement correctly, or maintain coherently. Bjarne notes this affected both Boost and WG21.

**When to Apply**: When reviewing proposals, especially those that have grown through the review process; when voting on feature sets.

**Red Flags**:
- Proposal has grown significantly since initial submission
- Multiple competing camps each got their feature included
- "We added X to satisfy group Y and Z to satisfy group W"
- No features were removed during review despite concerns

**Supporting Experiences**: E3, E6

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E3, E6]
related-principles: [P5]
-->

---

### P3: Design for Decades, Not Quarters

> *"A lot of developers are trained to think in terms of quarters. A year's standardization and library design must consider decades because a good library will last for decades. A good language feature will be unchanged for decades, and they will have to be used by people who may not even be born yet."*

**The Principle**: Standardization requires thinking in decades, not product release cycles; proposals driven by immediate needs without considering long-term implications will age poorly.

**Why It Matters**: Unlike product development, standardized features cannot be removed. Decisions made to solve today's problem become permanent constraints on future evolution. Committee members with only product development experience may not naturally think this way.

**When to Apply**: When evaluating any proposal; when assessing a proposer's qualifications and perspective.

**Red Flags**:
- Proposal motivated primarily by current project needs
- "We need this for the next release"
- No discussion of how the feature will interact with future evolution
- Champion lacks experience thinking beyond 3-5 year horizons

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P2, P4]
-->

---

### P4: Expertise Does Not Scale with Voting

> *"Everybody in WG 21 is called experts. I don't think there is 527 language design experts on earth... but everybody has the same vote."*

**The Principle**: WG21's growth has diluted expertise per vote; the shift from "one organization, one vote" to "one person, one vote" combined with 5x membership growth means many voters lack deep language design experience.

**Why It Matters**: Voting outcomes may reflect popularity or lobbying success rather than technical merit. Features that benefit narrow constituencies can pass if proponents mobilize, while broadly needed but boring improvements languish.

**When to Apply**: When interpreting vote results; when planning proposal strategy; when assessing whether consensus reflects actual design quality.

**Red Flags**:
- People "coming into the working group five minutes before the vote and voting the way they've been told to"
- Proposal passes despite objections from known experts
- Vote preceded by significant external lobbying
- "Everybody likes it" without evidence of deep technical review

**Supporting Experiences**: E3, E5

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E3, E5]
related-principles: [P2, P3]
-->

---

### P5: Coherent Design Requires Central Direction

> *"We really would've been better off with some kind of secretariat or core group that could set direction. We have a direction group, but it only gives advice and people can ignore it very easily, and they do."*

**The Principle**: Without enforceable central direction, independent working groups and library authors produce features that don't interact well, have inconsistent naming, and follow different philosophies.

**Why It Matters**: The committee structure inherently fragments responsibility. Individual authors optimize for their specific problem without considering the whole. The result is inconsistent APIs (variant/any/optional), duplicated functionality, and features that don't compose.

**When to Apply**: When evaluating whether a proposal fits with existing standard components; when reviewing API naming and design patterns.

**Red Flags**:
- Proposal introduces new patterns/conventions without justification
- API style differs from related standard components
- No discussion of interaction with existing features
- "This is how we do it in our library" without considering standard conventions

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P1, P2]
-->

---

### P6: Monolithic Distribution Creates Adoption Barriers

> *"The Boost Libraries came as a huge chunk and you couldn't just get one library... if you are in some regulated business like a bank, you actually have to validate that there hasn't been something slipped in... So you had to review the libraries that you bring in."*

**The Principle**: Bundling libraries as a single monolithic distribution creates adoption barriers for organizations that must audit dependencies; the inability to adopt individual components limits uptake.

**Why It Matters**: Bjarne describes "de-boosting" large codebases—removing Boost because audit requirements made the whole-bundle approach untenable. This is a real-world deployment concern that affects whether good libraries actually get used.

**When to Apply**: When designing library distribution strategy; when evaluating claims about library adoption.

**Red Flags**:
- Library can only be obtained as part of larger bundle
- No mechanism to select only needed components
- Dependencies pull in unrelated functionality
- "Just download all of Boost" as adoption path

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: belongs/ecosystem
applies-to: library
confidence: high
supported-by: [E6]
related-principles: []
-->

---

### P7: Mature Libraries Can Fail Standardization Through Politics

> *"ASIO became a massive success. I've used it commercially. It's been used worldwide for at least 15 years more now. And the standards committee couldn't agree on it... This was a success, but it was a success outside the standard and it should have been inside the standard."*

**The Principle**: Even extensively field-tested, widely-deployed libraries can fail standardization if stakeholders with blocking power prefer alternative approaches; technical merit alone is insufficient.

**Why It Matters**: ASIO represents perhaps the strongest case of field experience validating a design, yet it failed to standardize. "Big organizations, important organizations... big enough to block" prevented standardization while not providing equally mature alternatives.

**When to Apply**: When planning proposal strategy for any library with significant existing deployments; when assessing feasibility of standardizing mature external libraries.

**Red Flags**:
- Major vendors express preference for different approach without shipping alternative
- "We'll provide something better" without concrete timeline
- Blocking without providing comparable field experience
- Perfectionism preventing standardization of proven solutions

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/politics
applies-to: library
confidence: high
supported-by: [E7]
related-principles: [P4]
-->

---

### P8: Credits Should Follow Work

> *"I think when people do something like a library, it should get a name on it. I'm all in favor of that."*

**The Principle**: Individual contributors to libraries and standards work should receive attribution; corporate anonymization ("based on a document by...") undermines both recognition and accountability.

**Why It Matters**: Reputation is a key motivator in volunteer-driven work. Attribution creates accountability and allows contributors to build careers on their contributions. Bjarne fought AT&T early on to ensure contributors were credited.

**When to Apply**: When reviewing attribution practices in proposals and libraries.

**Red Flags**:
- Corporate authorship hiding individual contributors
- Credit only going to proposal champions, not implementers
- Historical decisions made anonymously

**Supporting Experiences**: E8

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/actual
applies-to: both
confidence: medium
supported-by: [E8]
related-principles: []
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: The STL's Language-Library Co-Design

**Context**: Alex Stepanov had built the STL concept twice before—in Lisp and Ada—and both failed. Bjarne had been developing C++ and had a list of requirements for a good containers/algorithms library.

**What Happened**: Bjarne and Alex talked for years, "partly agreeing that we needed such a library and partly disagreeing with some of his detailed language designs." Bjarne then "went and fixed C++ to be significantly better at generic programming. And Alex took that and ran with it." The STL matched 11 of Bjarne's 12 criteria despite looking nothing like what anyone expected in the object-oriented era.

**The Outcome**: Success. The STL became one of the most influential library designs in programming history, precisely because language and library design were coordinated.

**The Lesson**: Major library innovations may require language changes first. The STL couldn't exist in C++ before Bjarne's generic programming improvements—the failed Lisp and Ada versions prove this.

> *"So there was this direct connection between language design and library design, which I would have liked to see go further."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [STL, templates, generic-programming]
supports: [P1]
-->

---

### E2: Unique Pointer as Library-Language Success

**Context**: C++98 had `auto_ptr` which "couldn't be done till we'd fixed the language to be able to do it." It was a "unique pointer which we couldn't do."

**What Happened**: When C++ gained move semantics (a language change), `unique_ptr` could be built properly. "The unique pointer is the one place that I can think of where we simply built a drop in replacement for something we had and could yank out the original."

**The Outcome**: Success. `auto_ptr` was deprecated and removed; `unique_ptr` is what `auto_ptr` should have been.

**The Lesson**: Sometimes library improvements must wait for language improvements. Forcing library-only solutions leads to compromised designs like `auto_ptr`.

> *"Unique pointer came out of the Boost effort... unique pointer is what auto pointer should have been had we been able to do it."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [unique_ptr, auto_ptr, move-semantics]
supports: [P1]
-->

---

### E3: Committee Growth and Dilution

**Context**: The C++ committee started with ~100 voting members under "one organization, one vote" rules. By Bjarne's count, it has grown to 527 members under "one person, one vote."

**What Happened**: "Instead of thinking of the committee of about a hundred people, which I already was shockingly large, we are now thinking of five times that." Bjarne observes "people coming into the working group five minutes before the vote and voting the way they've been told to, convinced to do, but they haven't been there in the discussion."

**The Outcome**: Mixed. Increased participation but decreased expertise density per vote. "It's difficult to get things through if they are important... it's actually easier to get fairly irrelevant things through because people can't be bothered to object."

**The Lesson**: Committee growth creates coordination problems and dilutes expertise. The shift to individual voting amplifies this by removing organizational filtering.

> *"Everybody in WG 21 is called experts. I don't think there is 527 language design experts on earth."*

**Supports Principles**: P2, P3, P4

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/evolution
applies-to: both
outcome: mixed
features: [committee-process]
supports: [P2, P3, P4]
-->

---

### E4: Variant/Any/Optional Incoherence

**Context**: Boost developed `variant`, `any`, and `optional` as independent libraries, each providing a set of alternatives with some constraints.

**What Happened**: Because each was "designed in isolation from each other," their interfaces are "totally different. Anything you learn and can use the style for optional doesn't work for variant." This despite the only real difference being "what the set of alternatives are."

**The Outcome**: Failure of coherence. "Any group of people working on a coherent library would have not had that problem."

**The Lesson**: Independent development without coordination produces inconsistent APIs even for closely related functionality.

> *"Boost was encouraging libraries and it was encouraging individuals to do libraries, but they were not working on a, with a coherent philosophy across libraries."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [variant, any, optional]
supports: [P5]
-->

---

### E5: Forced Standardization Beginning

**Context**: In the early days of C++, Bjarne was working at Bell Labs. Representatives from IBM, Sun, and HP wanted C++ standardized.

**What Happened**: "The representatives of IBM, Sun and HP turned up in my office and told me that I wanted to standardize C++ on the ISO or on the ANSI rules... I said, no, it's too early to standardize... So they twisted my arm for about an hour." Their arguments: "Of course we trust you, but we can't trust your employer" and "you might get run over by a bus."

**The Outcome**: Mixed. Standardization happened but under a process Bjarne didn't choose. "The issue of exactly what was the best way of standardizing was never there. I would've had to rebel against the three largest computer manufacturers on earth at the time."

**The Lesson**: External pressures can force standardization timing and process choices that aren't optimal for the technology.

> *"After an hour, I said, yes. Yeah, yes, yes. I really want to help you standardize C++ on the ANSI rules. And, by the way, what's ANSI rules? I had no clue at the time."*

**Supports Principles**: P4

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/decisions
applies-to: both
outcome: mixed
features: [standardization-process]
supports: [P4]
-->

---

### E6: De-Boosting Large Codebases

**Context**: Bjarne was involved in removing Boost libraries from a large codebase, likely in a regulated industry (banking context mentioned earlier).

**What Happened**: "The main reason for that had nothing to do with the quality of a Boost Library. It has to do with the fact that the Boost Libraries came as a huge chunk and you couldn't just get one library." In regulated businesses, "you actually have to validate that there hasn't been something slipped in." Reviewing the whole bundle was impractical: "Once it is there, somebody's going to use it."

**The Outcome**: Failure of adoption. Despite high quality, organizational audit requirements forced removal.

**The Lesson**: Library distribution model matters as much as library quality for enterprise adoption.

> *"You couldn't say, I want just those three libraries. No, no, no, no, no, no."*

**Supports Principles**: P2, P6

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [boost, dependency-management]
supports: [P2, P6]
-->

---

### E7: ASIO's Standardization Failure

**Context**: ASIO (Asynchronous I/O library by Chris Kohlhoff) has been commercially used for 15+ years, including by Bjarne himself, in "high performance stuff" and "high reliability stuff."

**What Happened**: "The standards committee couldn't agree on it." Opponents "came forward with several different solutions to the problems of ASIO" but without comparable maturity. Bjarne argued "we'll just bring in ASIO, it'll help a lot of people. And then you can come up with something better or extensions of ASIO later. And they were not willing to."

**The Outcome**: Failure. "This was a success, but it was a success outside the standard and it should have been inside the standard."

**The Lesson**: Blocking a mature solution while promising better alternatives that never materialize harms users who need networking capabilities now.

> *"They were big organizations, important organizations big enough to be taken serious and big enough to block."*

**Supports Principles**: P7

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [asio, networking]
supports: [P7]
-->

---

### E8: AT&T Attribution Fight

**Context**: Early in C++ development at Bell Labs, AT&T corporate rules prohibited putting individual names on documentation.

**What Happened**: "The corporate rule says I couldn't put the names of individuals on, and I refused to deal with that." After "some negotiations," a compromise was reached: "Every document didn't say who the author was, but every document said 'based on a document by' and then the name of the individual who had done the work."

**The Outcome**: Success. Individual contributors got credit despite corporate resistance.

**The Lesson**: Attribution fights are worth having; they're essential for building contributor reputation in volunteer-driven ecosystems.

> *"I actually fought that battle back in 83, 84... against AT&T, actually the biggest company in the US at the time, and I won."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E8
source-type: explicit
category: history/decisions
applies-to: both
outcome: success
features: [attribution, licensing]
supports: [P8]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Has the proposal been discussed with EWG/language experts for potential language-level solutions? (P1)
- [ ] Does the API style match related standard components (naming, patterns)? (P5)
- [ ] Is the scope minimal, or has it grown to satisfy multiple constituencies? (P2)
- [ ] Will this design still make sense in 20 years? (P3)
- [ ] Can the library be adopted independently without pulling in unrelated dependencies? (P6)

**Questions to Ask**:
1. "Would this be better solved by a language feature?" (P1)
2. "What related standard components exist, and how does this API compare?" (P5)
3. "What features were removed or rejected during review?" (P2)
4. "How will this interact with future language/library evolution?" (P3)

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P3, P5, P6]
-->

---

### When Assessing Committee Process

- [ ] Have relevant experts participated, or mainly enthusiasts? (P4)
- [ ] Was there late lobbying or vote mobilization? (P4)
- [ ] Did blocking occur without provision of mature alternatives? (P7)
- [ ] Are individual contributors properly credited? (P8)

**Questions to Ask**:
1. "Who objected, and what was their expertise?" (P4)
2. "What comparable field experience do blocking alternatives have?" (P7)
3. "Who actually wrote this, and are they credited?" (P8)

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P4, P7, P8]
-->

---

## Open Questions

1. **What exactly caused ASIO to fail standardization?** Bjarne mentions "big organizations" blocking but doesn't name them or specify their alternative proposals.

2. **What are the specific politics around the C++ Alliance and Boost name?** Bjarne mentions "some pretty bad political fights about a year ago" regarding the Boost name but declines to elaborate.

3. **What does Bjarne consider successful profile implementations?** He advocates profiles but doesn't cite existing examples of this pattern working in practice.

4. **What is Bjarne's view on the Beman project?** He doesn't mention it, but it attempts to address some of the library standardization issues he raises.

5. **What was Beman's specific role in mediating between "major egos" in Boost?** Bjarne strongly suspects Beman kept people working together but wasn't in the room to confirm.

---

## Raw Transcript Reference

Source: `inputs/bjarne-stroustrup.md`  
Video: https://vimeo.com/1157576773/c5cad0787a
