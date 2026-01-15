# Daisy Hollman: Captured Knowledge

**Interview Date**: 2025-09-16
**Interviewer**: Ray Nowosielski
**Duration**: ~100 minutes
**Topics Covered**: Boost history, meritocracy critique, diversity in C++, WG21 committee experience, MDSpan standardization, CPP Con leadership, Google's committee exit, Carbon language, AI's impact on programming languages, community conflicts

## Executive Summary

Daisy Hollman, former C++ committee member, Study Group 9 (Ranges) chair, and CPP Con program chair, provides a candid perspective on diversity challenges in C++ and Boost communities. As a trans woman who transitioned publicly within the committee, she offers unique insights into how "meritocracy" framing has become politically charged and how it intersects with inclusion efforts.

Her most striking contribution is the analysis of why Boost's imagined meritocracy is vulnerable to exploitation: code quality is subjective (30 ways to write the same thing), participation requires free time that disadvantages caregivers, and reviewers favor code written in familiar styles—creating self-reinforcing homogeneity. She argues that the Include C++ vs. Boost dinner scheduling at the same time reflected a real split: those who wanted diversity and those who resisted it.

Most actionable is her framework for understanding code quality subjectivity: the purpose of code is communicating with humans, not machines. This undermines pure meritocracy claims because "better code" depends on who's reading it. Her prediction that AI may create a "programming language singularity" where training data quantity matters more than language quality raises important questions about Boost's future relevance.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Boost Delayed C++ Package Management

> *"Boost was this kind of lightweight version of a package manager for C++. And to some extent it put off the development of package management ecosystems in C++ because of Boost."*

**The Principle**: Boost's success as a library collection obviated the need for proper package management, delaying C++'s development of that infrastructure compared to other languages.

**Why It Matters**: This is the flip side of Boost's value proposition—by solving the "where do I find quality libraries" problem through curation, Boost removed pressure to build distribution infrastructure. When Boost declined, C++ was behind on package management.

**When to Apply**:
- When analyzing why C++ lacks strong package management
- When understanding Boost's historical role and limitations
- When designing library ecosystems

**Red Flags**:
- Assuming curated collections can substitute for proper distribution
- Not investing in package management because existing solutions "work"
- Single-point-of-failure library ecosystems

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: history/regrets
applies-to: library
confidence: medium
supported-by: [E1]
related-principles: [P2]
-->

---

### P2: Boost's Quality Bar Made It Harder to Prototype

> *"Boost had gotten to be so big and such a big deal that their quality standards were at the point where you couldn't—it was harder to prototype something into the Boost Libraries directly."*

**The Principle**: As Boost's reputation grew, its quality bar became prohibitively high for prototyping, pushing experimentation elsewhere and breaking the Boost→Standard pipeline.

**Why It Matters**: This explains why post-2016 proposals increasingly bypassed Boost. The high bar that created Boost's reputation became a barrier to the experimentation that fed the standard. Quality standards optimized for mature libraries don't serve prototyping.

**When to Apply**:
- When designing library acceptance processes
- When balancing quality with accessibility
- When understanding why new features bypass Boost

**Red Flags**:
- Quality processes that prevent prototyping
- Reputation-driven bars that exclude newcomers
- No pathway for experimental libraries

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E1]
related-principles: [P1]
-->

---

### P3: Code Quality Is Subjective—Meritocracy Is Illusory

> *"There are 30 different ways you can say the same thing in code... The purpose of code is not to communicate with a computer, it's to communicate with another human... There is a very subjective element to this meritocracy."*

**The Principle**: Because code's primary purpose is human communication (not machine execution), and multiple implementations can be functionally identical, "code quality" is inherently subjective—undermining claims of pure meritocracy.

**Why It Matters**: This challenges the foundational assumption of "best code wins." Reviewers favor code that matches their mental models, creating self-reinforcing homogeneity. "The person thinks the best code objectively is the one that they understand the best, but that's because they're in the same industry."

**When to Apply**:
- When evaluating code review processes
- When understanding why "meritocracy" produces homogeneous communities
- When designing inclusive contribution processes

**Red Flags**:
- Claims that code quality is purely objective
- Review processes where all reviewers share similar backgrounds
- Assuming consensus on "quality" reflects truth rather than shared bias

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/tradeoffs
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P4]
-->

---

### P4: Participation Requires Time That Disadvantages Many

> *"A single mother with two children is not getting a library into Boost regardless of how good they are at coding. You don't have time to sit around mailing lists and argue that your library is the best."*

**The Principle**: Open source "meritocracy" rewards those with discretionary time to advocate for their contributions; this systematically disadvantages caregivers and others with constrained time, regardless of technical ability.

**Why It Matters**: This identifies a structural bias in open source processes that goes beyond code quality. Getting a library accepted requires sustained advocacy—attending meetings, responding to emails, defending design decisions. Time availability, not just skill, determines success.

**When to Apply**:
- When designing contribution processes
- When analyzing why certain demographics are underrepresented
- When evaluating claims of meritocracy

**Red Flags**:
- Processes requiring sustained, unpaid engagement
- No accommodation for asynchronous participation
- Interpreting lack of advocacy as lack of merit

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P3]
-->

---

### P5: The Committee Requires Building Consensus Across Industries

> *"You actually do have to make everyone happy to some extent, and so you do actually have to kind of walk in their shoes... I had to learn all kinds of things about the games industry that I had no idea, and it influenced the design significantly."*

**The Principle**: Successful standardization requires understanding and accommodating use cases from multiple industries; this forced perspective-taking produces better designs than single-industry development.

**Why It Matters**: Hollman contrasts this with Boost's process, where designs can succeed by satisfying a narrower constituency. MDSpan's design improved because she had to understand game development needs alongside scientific computing. The committee's breadth requirement is a feature, not a bug.

**When to Apply**:
- When designing features intended for standardization
- When evaluating whether a design has sufficient industry coverage
- When understanding the committee's value over private development

**Red Flags**:
- Designs that only work for one industry
- Proposals that haven't consulted multiple use cases
- Assuming one domain's needs are universal

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E3]
related-principles: []
-->

---

### P6: Large Companies Have Better Implementation Experience

> *"The reason why proposals from Microsoft, from Google, from Apple see a lot of attention is because they are good... A large company gives you a lot of usage experience internally and makes you have to balance the needs of a more diverse set of stakeholders."*

**The Principle**: Proposals from large companies tend to succeed not because of political favoritism but because internal deployment across diverse teams provides natural vetting and forces design compromises.

**Why It Matters**: This counters conspiracy theories about corporate capture. Large company proposals arrive already tested across multiple use cases with conflicts resolved. This is similar to field experience but happens internally. The advantage is structural, not corrupt.

**When to Apply**:
- When evaluating why certain proposals succeed
- When advising smaller organizations on standardization strategy
- When understanding committee dynamics

**Red Flags**:
- Assuming corporate proposals succeed due to politics alone
- Small-org proposals that haven't sought diverse testing
- Ignoring the vetting that internal deployment provides

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P6
source-type: tacit
category: process/politics
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: [P5]
-->

---

### P7: Dyslexia Paradoxically Improves Language Design Intuition

> *"Dyslexic programmers make the same mistakes as normal programmers. We just make them a lot more often. And because of that... I was able to see the places where people would make mistakes much more readily."*

**The Principle**: Conditions that cause more errors in a domain can develop better intuition for error patterns; Hollman's dyslexia gave her exceptional insight into where developers would stumble.

**Why It Matters**: This challenges assumptions about what makes a good language designer. Hollman's senior committee members recognized her mistake-pattern intuition and brought her onto papers because of it. Diversity in cognitive processing produces design insights unavailable to typical contributors.

**When to Apply**:
- When valuing diverse perspectives in design
- When understanding why certain contributors have unusual insights
- When evaluating who should contribute to language/API design

**Red Flags**:
- Assuming technical excellence requires neurotypical processing
- Dismissing contributors who make frequent errors
- Undervaluing error-pattern recognition as a skill

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P7
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E2]
related-principles: [P3]
-->

---

### P8: AI May Create a "Programming Language Singularity"

> *"We may have passed some sort of programming language singularity where the quality of language features gets kind of balanced out by the quantity or size of the training data available."*

**The Principle**: AI coding assistants may shift value from language quality to training data quantity; languages with more code in training data may become more useful regardless of design quality.

**Why It Matters**: This suggests Boost's extensive legacy codebases might become valuable precisely because they're in training data, not because of superior design. It also suggests that "better designed" libraries without training data presence may be less useful in an AI-assisted world.

**When to Apply**:
- When planning library strategy in an AI-assisted future
- When evaluating whether to maintain vs. replace legacy code
- When understanding potential shifts in language popularity

**Red Flags**:
- Assuming better design always wins
- Ignoring training data presence as a factor
- Planning for a non-AI future

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P8
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E4]
related-principles: []
-->

---

### P9: Visible Representation Matters for Retention

> *"I felt like I had a responsibility to women coming to the committee meetings to be able to find role models... The impact that I'm having by just being there and being visible is the most meaningful thing to me by far."*

**The Principle**: Visible representation of underrepresented groups creates role models that enable retention; absence of representation signals unwelcome and drives away potential contributors.

**Why It Matters**: Hollman stayed on the committee partly because leaving would remove 20% of regular women attendees. Her keynotes matter most when women approach afterward saying "this changed my perspective." Representation is not just recruitment—it's retention infrastructure.

**When to Apply**:
- When evaluating community health
- When deciding whether to stay in unwelcoming environments
- When understanding why representation matters beyond fairness

**Red Flags**:
- Communities with single-digit representation of major demographics
- Dismissing representation as merely symbolic
- Not creating pathways for underrepresented contributors

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P4]
-->

---

### P10: Features Take 10+ Years From Inception to Standard

> *"That was a 11, 12 year long process total. I think the first paper was 2014, maybe 2013 even. And the first parts of it went into 23, and then the last part of it's going into 26."*

**The Principle**: Major library features (like MDSpan) take a decade or more from first paper to final standardization, confirming the 10-year rule applies broadly.

**Why It Matters**: This independently confirms Bryce Lelbach's observation about 10-year timelines. MDSpan took 11-12 years. This calibrates expectations and explains why waiting for "more baking time" is resisted—authors have already invested a decade.

**When to Apply**:
- When planning standardization efforts
- When understanding author frustration with delays
- When evaluating whether to start a standardization effort

**Red Flags**:
- Expecting faster timelines without precedent
- Not accounting for multi-cycle incremental standardization
- Assuming first version will be complete

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/timing
applies-to: both
confidence: high
supported-by: [E3]
related-principles: []
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Boost as Proto-Package Manager

**Context**: Hollman's early career in quantum chemistry, using Boost in the early 2000s.

**What Happened**: Boost served as "a lightweight version of a package manager for C++." If something was needed, the question was "Is there something in Boost that does this?" The convenience of having everything in one ecosystem—where Boost libraries could depend on other Boost libraries without additional setup—delayed investment in proper package management.

**The Outcome**: Mixed. Boost provided value during C++'s "dark period" but may have delayed ecosystem infrastructure development. C++ now lags other languages in package management.

**The Lesson**: Convenient solutions that work can prevent investment in better infrastructure. Boost's success as a curated collection was also a form of technical debt at the ecosystem level.

> *"It was almost like a package manager in that sense... whoever used your library wouldn't have to go get another Boost Library. They would've just had all of Boost."*

**Supports Principles**: P1, P2

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/evolution
applies-to: library
outcome: mixed
features: [boost, package-management]
supports: [P1, P2]
-->

---

### E2: First Committee Meeting as Stealth Trans Woman

**Context**: Hollman's first WG21 meeting in 2016, not yet publicly identifying as a woman.

**What Happened**: She walked into a room with one other woman present (the second regular woman had missed her flight). A male committee member told her—not knowing she was trans—that "the reason why there are so many more men here than women is because the men are smarter." This was presented as scientific fact (the "flatter bell curve" argument). She was told she'd have to choose between C++ and "living my life as a woman."

**The Outcome**: Mixed. Despite the hostile environment, Hollman became deeply involved, eventually chairing Study Group 9 and CPP Con. She credits the other women on the committee with being "absolutely lovely" and supportive of her transition.

**The Lesson**: Toxic environments drive away diverse talent. Those who stay despite toxicity often do so because they find supportive subgroups. Representation matters—Hollman worried about the impact of leaving when she was "20% of the women on the committee."

> *"Every woman in this community has been through some version of that."*

**Supports Principles**: P3, P4, P7, P9

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/failures
applies-to: both
outcome: mixed
features: [diversity, WG21, committee-culture]
supports: [P3, P4, P7, P9]
-->

---

### E3: MDSpan Standardization Journey

**Context**: Hollman's work on multidimensional array abstractions for scientific computing, starting at Sandia National Labs.

**What Happened**: First papers appeared around 2013-2014. The design required understanding use cases across scientific computing and game development—industries with very different needs. The team considered putting it in Boost but decided it "wasn't worth it" given time and the risk that scientific computing users wouldn't be well-represented in Boost reviews. It took 11-12 years total, with parts landing in C++23 and final pieces in C++26.

**The Outcome**: Success. MDSpan shipped, and the cross-industry consultation improved the design. The experience demonstrated that committee breadth requirements, while slow, produce better designs.

**The Lesson**: Cross-industry consensus takes time but produces better results. The decision to bypass Boost was rational given the time investment and stakeholder coverage concerns. Large features can ship incrementally across multiple standards.

> *"I had to learn all kinds of things about the games industry that I had no idea, and it influenced the design significantly and I think for the better."*

**Supports Principles**: P5, P6, P10

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: process/navigation
applies-to: library
outcome: success
features: [MDSpan, standardization, C++23]
supports: [P5, P6, P10]
-->

---

### E4: AI and the Future of Libraries

**Context**: Hollman's current work at Anthropic on Claude Code, reflecting on C++ and Boost's future.

**What Happened**: After leaving Google (with 30 minutes notice, the day before CPP Con), Hollman joined Anthropic in a Rust role but gravitated to Claude Code. She now writes mostly in TypeScript but "very rarely writes actual TypeScript"—she writes ideas and the agent writes code. She observed that Boost's legacy support (C++03 compatibility) might paradoxically become valuable because that code is in AI training data.

**The Outcome**: Ongoing. Hollman predicts that "programming language singularity" may make training data quantity more important than language quality, potentially preserving relevance for legacy-focused libraries like Boost.

**The Lesson**: AI may invert traditional assumptions about library value. Boost's extensive legacy codebase could become an asset in training data terms even as its design philosophy becomes less relevant. The future of software engineering is changing faster than any prior period.

> *"Models can write code just as happily in C++ as any other language... I literally went from my last C++ committee meeting to my first day at Anthropic."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E4
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
outcome: pending
features: [AI, claude-code, future-of-programming]
supports: [P8]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Evaluating Library Design Processes

- [ ] Does the process allow prototyping or only mature submissions? (P2)
- [ ] Is code quality evaluation based on shared assumptions or diverse perspectives? (P3)
- [ ] Does participation require sustained time investment that disadvantages some groups? (P4)
- [ ] Are multiple industries represented in review? (P5)
- [ ] Is there visible representation of diverse contributors? (P9)

**Questions to Ask**:
1. "How would a caregiver with limited time participate in this process?"
2. "Have we consulted use cases from industries different than ours?"
3. "What assumptions about 'good code' might we be taking for granted?"
4. "Who is missing from our reviewer pool, and why?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: library
proposal-type: any
derived-from: [P2, P3, P4, P5, P9]
-->

---

### When Assessing Community Health

- [ ] Is representation of major demographics above single digits? (P9)
- [ ] Do participation structures require time disadvantaged groups don't have? (P4)
- [ ] Are "meritocracy" claims accompanied by diversity metrics? (P3)
- [ ] Do multiple industries feel their needs are heard? (P5)

**Questions to Ask**:
1. "What does our demographic data actually show?"
2. "Who has stopped participating, and why?"
3. "Do people from different backgrounds agree on what 'quality' means?"
4. "Is there a pathway for contributors with limited time?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P3, P4, P5, P9]
-->

---

### When Planning for AI-Assisted Future

- [ ] Is the library well-represented in AI training data? (P8)
- [ ] Does legacy support matter more or less with AI assistance? (P8)
- [ ] Would AI-generated code follow this library's patterns? (P8)
- [ ] How much does language/library design quality matter vs. ubiquity? (P8)

**Questions to Ask**:
1. "Is our code in AI training data?"
2. "Would an AI-assisted developer produce code in our style?"
3. "Does our legacy support become an asset or liability with AI?"
4. "How does AI change the value proposition of curated libraries?"

<!-- METADATA
kind: checklist
category: philosophy/tradeoffs
applies-to: library
proposal-type: any
derived-from: [P8]
-->

---

## Open Questions

1. What specifically were Google's demands that the committee rejected, leading to Google's exit?

2. What is the current status of Carbon language, and how does it relate to C++ standardization?

3. What happened with the CPP Con leadership changes around the sex offender disclosure?

4. What were the details of the "diversity panel incident" referenced in the transcript?

5. What is the current state of Include C++ vs. Boost community relations?

6. How has the committee's gender composition changed since 2016?

7. What is Hollman's assessment of Herb Sutter's diversity efforts and their effectiveness?

8. What led to Hollman's sudden departure from Google the day before CPP Con?

9. How does Rust's intentional inclusivity compare to C++'s in outcomes?

10. What would a more inclusive Boost review process look like specifically?

---

## Raw Transcript Reference

Source: `inputs/daisy-hollman.md`
Video: https://vimeo.com/1141523385/9843033d39?fl=pl&fe=sh
Filmed: 2025-09-16, Aurora, CO
