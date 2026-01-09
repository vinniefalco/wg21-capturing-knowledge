# Dave Abrahams: Captured Knowledge

**Interview Date**: 2025-12-19
**Interviewer**: Ray Nowosielski
**Duration**: ~3 hours
**Topics Covered**: Boost origins, WG21 process, exception safety standardization, STL impact, BoostCon creation, peer review, Boost license, concepts debacle, governance transitions, library philosophy

## Executive Summary

Dave Abrahams provides a foundational account of Boost's creation, evolution, and philosophical underpinnings. His perspective is uniquely valuable because he was present at Boost's founding, instrumental in establishing its peer review culture, and deeply involved in standardization efforts—most notably bringing exception safety guarantees to the C++ standard library.

Three major themes emerge: First, the power of **consensus-based collaboration** modeled on the WG21 process and Beman Dawes's inclusive leadership style. Second, the critical importance of **existing practice and field experience** before standardization—libraries must prove themselves in real-world use. Third, the insight that **libraries are infrastructure** that enables domain experts to focus on their actual expertise rather than reinventing fundamental components.

Abrahams also provides a cautionary narrative about language/committee evolution: C++'s inability to agree on evolution principles, the concepts debacle, and growing complexity eventually drove him away from the language entirely. His departure to work on Swift represents a judgment that C++ had become too encumbered by legacy to serve his mission of "empowering programmers."

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Standardize Existing Practice

> *"The idea is, let's, let's only make standard the things that are actually out there in use that, that have a track record and who's, you know, that we can evaluate in terms of how they actually worked in the real world."*

**The Principle**: Standardize only components that have demonstrated real-world success through actual use, not theoretical designs that merely "should" work.

**Why It Matters**: The committee strayed from this principle to include STL template features before any compiler implemented them, creating years of lag before compilers caught up. This is "a black eye for the committee"—standardizing unproven features risks discovering they're unimplementable or impractical.

**When to Apply**: Evaluating any library or language proposal for standardization. The proposal should have a track record of actual use, not just an implementation.

**Red Flags**:
- No existing implementation predating the proposal
- Implementation exists but has no users outside the proposers
- Features invented specifically for standardization without prior art
- Compiler/library vendors expressing doubt about implementability

**Supporting Experiences**: E1, E2, E7

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E1, E2, E7]
related-principles: [P2]
-->

---

### P2: Libraries Enable Domain Focus

> *"Programmers that build products are paid to develop the expertise in, in their product domain... every time they have to go on an excursion to build an algorithm that is standard or a data structure... they're doing something that there's economic pressure on them not to give it the attention it deserves."*

**The Principle**: Libraries allow programmers to leverage expert implementations of common components, freeing them to focus their cognitive resources on their actual domain of expertise.

**Why It Matters**: A music notation software expert shouldn't be spending time implementing binary search—they'll likely get it wrong (Dave admits writing it incorrectly multiple times), and even if they get it right, that time is stolen from their actual value-add. Libraries solve this by providing rigorously tested, well-documented components.

**When to Apply**: Evaluating whether something belongs in a standard library. Ask: "Is this something that many programmers across different domains would otherwise implement themselves, likely incorrectly or inefficiently?"

**Red Flags**:
- Library proposal addresses a niche problem that few programmers encounter
- The component is so domain-specific that generic implementation provides little value
- Implementation requires domain knowledge that library authors can't possess

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E2, E3]
related-principles: [P1, P5]
-->

---

### P3: Consensus Achieves Great Things

> *"What the committee demonstrated for me at that time was, was contrary to what a lot of people say about design by committee... you can actually accomplish great things by consensus."*

**The Principle**: Consensus-based processes, when properly facilitated, can produce excellent technical outcomes—not diluted compromises but genuine discoveries of the best approach.

**Why It Matters**: Dave's exception safety work succeeded despite him not being a committee member and having no vote. He achieved it entirely through persuasion, building understanding, and working with people. This demonstrates that formal authority is less important than the ability to help people understand problems clearly.

**When to Apply**: When navigating committee processes or building support for proposals. Focus on education and consensus-building rather than political maneuvering.

**Red Flags**:
- Trying to "win" arguments rather than discover truth
- Treating the process as political rather than collaborative
- Ignoring or dismissing opposing viewpoints rather than addressing them

**Supporting Experiences**: E1, E4

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1, E4]
related-principles: [P4, P8]
-->

---

### P4: Ecumenical Leadership Creates Respect

> *"What really super impressed me was this kind of ecumenical way that Beman ran the meeting where, where everybody's input was valued. He was, he was patient and, um, non-partisan."*

**The Principle**: Effective technical leadership means moderating discussions so all arguments are heard, remaining non-partisan toward solutions, and creating an environment of mutual respect.

**Why It Matters**: Beman Dawes's leadership style at LWG created a level of respect among committee members that Dave "did not experience in my regular job." This environment enabled productive collaboration and attracted high-caliber contributors to Boost. The review manager role in Boost peer review was explicitly modeled on this approach.

**When to Apply**: Running working group sessions, managing peer reviews, or leading any technical collaboration. The leader's job is facilitation and consensus determination, not advocacy.

**Red Flags**:
- Chair advocating for specific technical solutions
- Discussions dominated by a few loud voices
- Newcomers excluded from participation
- Decisions made without hearing all perspectives

**Supporting Experiences**: E4, E5

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E4, E5]
related-principles: [P3, P8]
-->

---

### P5: Libraries Reduce Decision Burden

> *"The benefit of having had the STL take away things I had to consider from me, um, just even, even what kind of design decisions I was gonna make in my own code, if I had an example that completely changed the productivity landscape for me."*

**The Principle**: Good libraries don't just provide implementations—they provide paradigms and conventions that eliminate entire categories of design decisions for users.

**Why It Matters**: Before the STL, every programmer had to decide how to pass data to algorithms, how to structure containers, etc. After the STL, the answer was obvious: use iterators. This removal of decision burden is as valuable as the code itself. It's why consistent conventions and idioms matter so much.

**When to Apply**: Designing library interfaces. Ask: "Does this design establish clear conventions that users can apply to their own code?" A library that requires users to make many arbitrary decisions about how to use it has failed.

**Red Flags**:
- Multiple equally-valid ways to accomplish the same task
- Interface that doesn't suggest how user code should be structured
- Design that conflicts with established idioms without good reason

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P2, P6]
-->

---

### P6: Discovery Over Invention

> *"The valuable things are discovered, not invented... there's a truth that's out there like a mathematical truth or, or a design truth or something, and your job is to discover it."*

**The Principle**: The best technical work uncovers existing truths rather than creating arbitrary constructs. Approach problems as exploration toward the right answer, not competition between proposed solutions.

**Why It Matters**: This mindset shaped Boost's culture. Long debates about naming conventions weren't ego battles—they were collective attempts to discover the genuinely best answer. This framing transforms arguments from adversarial to collaborative and prevents the "meritocracy" trap of focusing on who wins.

**When to Apply**: Any technical debate or design discussion. Frame questions as "What is the right answer?" rather than "Whose proposal should win?"

**Red Flags**:
- Treating technical discussions as competitions
- Attachment to "my solution" rather than "the solution"
- Dismissing alternatives without genuine consideration
- Prioritizing being right over finding right

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P6
source-type: tacit
category: philosophy/coherence
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P3, P4]
-->

---

### P7: Algorithms Are Central

> *"The foundational thing Alex is always gonna come back to is, is it's about the algorithms... nobody had ever focused on the algorithms as, as the core feature."*

**The Principle**: Algorithms—explicit, understandable computations—should be the organizing principle of software design, not webs of loosely-coupled objects passing messages.

**Why It Matters**: Object-oriented programming's "big web of connected components" creates what Sean Parent calls "incidental algorithms"—computations that are spread across the codebase and impossible to reason about locally. The STL's algorithm-centric design made code efficient and comprehensible. This is why generic programming matters.

**When to Apply**: Designing libraries or evaluating designs. Prefer explicit algorithms over implicit message-passing. Code should be readable as a coherent computation, not a configuration of interacting objects.

**Red Flags**:
- Design where behavior emerges from object interactions rather than explicit logic
- "Incidental algorithms" spread across many classes
- Code that can't be understood without tracing message flows
- Over-reliance on inheritance hierarchies and virtual dispatch

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P5, P6]
-->

---

### P8: Minimize Wording Changes

> *"One of the big concerns that the committee had about accepting changes for exception safety is how many actual words would need to change in the standard... Greg was instrumental in working with me to help me find a way to make the wording changes as small as possible."*

**The Principle**: When proposing changes to the standard, minimize the scope of wording changes. Small, focused changes are easier to review, less likely to introduce inconsistencies, and more likely to be accepted.

**Why It Matters**: Large wording changes are hard to evaluate for unintended consequences. The standard is a web of interconnected definitions; changing one part may break consistency elsewhere. Dave's exception safety proposal succeeded partly because Greg Colvin helped minimize the actual text changes.

**When to Apply**: Writing any proposal with wording. Before submitting, ask: "Is there a way to achieve the same semantic change with fewer words modified?"

**Red Flags**:
- Proposals that rewrite large sections of existing text
- Changes that touch many different clauses
- Wording that duplicates concepts already defined elsewhere
- Inability to clearly explain what text changes and why

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: wording/quality
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P3]
-->

---

### P9: Permissive Licensing Maximizes Practice

> *"The license is permissive the way it is because of the fundamental charter to create existing practice for standardization. So the idea is make it as easy as possible for people to use. Don't put any strings on what they do with it, and then it'll get lots of use."*

**The Principle**: If the goal is widespread adoption to establish existing practice, licensing must impose minimal friction. Every restriction reduces adoption.

**Why It Matters**: The Boost Software License's permissiveness directly served Boost's mission. Programs displaying the Boost license at startup became visible evidence of success. More restrictive licenses (like GPL v3) drove companies away from certain open source software entirely.

**When to Apply**: Choosing licensing for libraries intended for standardization or wide adoption. Any requirement that makes lawyers nervous reduces adoption.

**Red Flags**:
- Copyleft provisions that complicate commercial use
- Attribution requirements that create legal review burdens
- Viral licensing that affects downstream code
- Complex license terms requiring legal interpretation

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/navigation
applies-to: library
confidence: high
supported-by: [E6]
related-principles: [P1]
-->

---

### P10: In-Person Collaboration Is Irreplaceable

> *"The relationships that I had developed with people online were meaningful, they were intellectually meaningful... but we wouldn't have personal conversations like you would have over a beer."*

**The Principle**: Online collaboration can accomplish intellectual work, but in-person interaction is necessary for building the deep relationships and trust that sustain long-term collaboration.

**Why It Matters**: Dave created BoostCon specifically because he wanted to meet people like Peter Dimov whom he'd collaborated with for years but never seen. The conference design—long breaks, beautiful setting, planning meetings—was optimized for relationship-building, not just information transfer.

**When to Apply**: Designing conferences, planning working group activities, or building communities. Prioritize unstructured time for conversation. Schedule face-to-face meetings even when online would be "more efficient."

**Red Flags**:
- Conferences packed with back-to-back sessions
- Communities that never meet in person
- Working relationships that remain purely transactional
- Assuming video calls fully substitute for presence

**Supporting Experiences**: E5, E8

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E5, E8]
related-principles: [P4]
-->

---

### P11: Legacy Accumulation Kills Languages

> *"C++ was never gonna get there. It was, it became clear that was over... C++ has become complex and difficult to the point of impracticality... The standard is now thousands of pages long. Nobody can absorb that or even come close."*

**The Principle**: Languages that cannot shed legacy features eventually become too complex for anyone to master, losing their ability to serve their users effectively.

**Why It Matters**: C++'s inability to agree on evolution principles—what old code might break, what features might be deprecated—means it only grows, never simplifies. Dave eventually concluded it could no longer serve his mission of "empowering programmers" and left for Swift. This represents a failure mode the committee should work to avoid.

**When to Apply**: Evaluating proposals that add complexity. Ask: "What is the long-term cost of carrying this feature forever?" Consider deprecation and removal, not just addition.

**Red Flags**:
- Features that can never be removed due to compatibility
- Complexity added without corresponding simplification elsewhere
- Proposals that only add, never subtract
- Committee unable to agree on any evolution principles

**Supporting Experiences**: E7, E9

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E7, E9]
related-principles: [P1]
-->

---

### P12: Infrastructure Is Undervalued

> *"Somehow the business world doesn't appreciate the importance of spending money on infrastructure... the next feature is the thing that everybody's chasing and there's no investment in maintaining the quality of the code."*

**The Principle**: Libraries are infrastructure with no direct financial incentive for creation or maintenance, yet they enable all other development. This structural underinvestment must be addressed through mechanisms like open source volunteer work.

**Why It Matters**: Boost succeeded partly because volunteers built infrastructure outside their day jobs that companies then used commercially. This isn't sustainable long-term—it's a market failure. Understanding this explains why important libraries are often under-maintained and why standardization matters: it's a way to distribute maintenance burden.

**When to Apply**: Advocating for library work within organizations. Evaluating why certain important components lack investment. Understanding the economics of open source.

**Red Flags**:
- Critical libraries maintained by single volunteers
- Companies using libraries without contributing back
- Infrastructure work consistently deprioritized for features
- Assumption that "someone else" will maintain foundational code

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: belongs/ecosystem
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P2]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Exception Safety Standardization

**Context**: Dave discovered that the STL had undefined behavior when exceptions were used—a critical problem for his music notation application. He contacted Alex Stepanov, who warned him the committee was unlikely to accept changes so late in the standardization process.

**What Happened**: Dave developed a theory of exception safety based on programming by contract, popularized it on Usenet, and worked within the committee to build consensus. Greg Colvin became his ally, helping minimize wording changes. The US national body representatives were "extremely conservative" and planned to vote no, but the UK and Germany national bodies said they would reject the standard unless exception safety was included.

**The Outcome**: Success. Exception safety guarantees were added to the C++ standard, despite Dave not being an official committee member with voting rights.

**The Lesson**: Major changes can succeed through consensus-building and education, even without formal authority. Working to minimize wording changes and building allies across national bodies can overcome institutional resistance. International consensus mechanisms can override domestic conservatism.

> *"That was sort of the end of the story... It was a huge accomplishment for me... another piece of evidence that you really can get great things done by consensus. Just by working with people to help them understand."*

**Supports Principles**: P1, P3, P8

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [exception-safety, STL]
supports: [P1, P3, P8]
-->

---

### E2: The STL Revelation

**Context**: Dave was working on music notation software at Mark of the Unicorn in 1997, struggling with the lack of available libraries. His colleague Mark Waxler showed him a magazine with an interview about Alex Stepanov's STL.

**What Happened**: Dave integrated the STL into his application and experienced a transformation in productivity. He could discard unreliable code he'd written (including multiple incorrect implementations of binary search) and its tests, replacing it with rigorously documented, expert-written components. Beyond the code itself, the STL gave him paradigms (like iterators) that eliminated design decisions.

**The Outcome**: Success. The STL "really shifted my programming experience" and taught Dave "what the power, the importance of libraries was."

**The Lesson**: Good libraries provide more than code—they provide paradigms, conventions, and the accumulated expertise of domain specialists. They free application developers to focus on their actual domain rather than reinventing fundamental components.

> *"The ability to get the people who were really best at a thing working on that thing and focused on it... I cannot tell you how many times I wrote binary search incorrectly before."*

**Supports Principles**: P2, P5, P7, P12

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [STL, algorithms, iterators]
supports: [P2, P5, P7, P12]
-->

---

### E3: Building Notation Software Without Libraries

**Context**: Dave's first professional programming job was developing notation software at Mark of the Unicorn starting around 1987. This was before libraries were widely available.

**What Happened**: Dave had to build everything himself: graphics, printing, transcription, user interface. He didn't know professional practices, had no mentor after his initial guide left, and was competing against established products. The software took three years to release while competitors captured the market.

**The Outcome**: Mixed. Dave became a "world class expert" in notation software but learned painful lessons about reinventing wheels. The product was late to market.

**The Lesson**: Without libraries, programmers are forced into time-consuming excursions outside their domain expertise, slowing development and often producing inferior results. This experience directly informed Dave's later appreciation for libraries.

> *"Notation software is complicated... there was a lot to learn. I found it really engaging to do all this stuff. But you had to build all of these parts yourself. There weren't libraries, basically."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/decisions
applies-to: library
outcome: mixed
features: [notation-software]
supports: [P2]
-->

---

### E4: First WG21 Meeting in Nashua

**Context**: Dave was trying to get exception safety changes into the C++ standard but was told by Andy Koenig that he needed to attend a meeting in person to have influence. He was living in Massachusetts; the next meeting happened to be in nearby Nashua, New Hampshire.

**What Happened**: Dave attended as a non-member and sat in a chair along the wall. Beman Dawes, the LWG chair, invited him to join the table despite not being a member. The committee members were generous in helping him understand the process, and he was able to make valuable contributions to issue processing.

**The Outcome**: Success. Dave was welcomed into the process and began building the relationships that would enable his exception safety work and later involvement in Boost.

**The Lesson**: Effective technical communities welcome newcomers and value contributions over credentials. Beman's inclusive leadership style created the respectful environment that made this possible.

> *"Even though I wasn't a committee member and he didn't know me, he asked me to come up and sit with everybody else... the level of respect I saw in the room among the committee members... was something I did not experience in my regular job."*

**Supports Principles**: P3, P4

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [WG21-process]
supports: [P3, P4]
-->

---

### E5: Creating BoostCon

**Context**: Dave wanted to meet the Boost contributors he'd collaborated with online but never seen in person. He consulted Scott Meyers, who advised him to design his "fantasy" conference day and make it happen. Dave's father had been connected to the Aspen Center for Physics, giving Dave a model for collaborative intellectual gatherings.

**What Happened**: Dave designed BoostCon with 30-minute breaks between sessions, long lunches, and a beautiful mountain setting—optimizing for conversation rather than content delivery. The first keynote was Sean Parent. The conference ended with a planning meeting that recruited volunteers for the next year.

**The Outcome**: Success. "I had more fun at that conference than I had ever had at any other conference." BoostCon became an annual event that eventually evolved into C++Now, and inspired the creation of CppCon.

**The Lesson**: Technical conferences should optimize for relationship-building and spontaneous collaboration, not just information transfer. The "hallway track" is often more valuable than sessions. Beautiful, unconventional settings (not Vegas convention centers) support creative thinking.

> *"Part of the way we designed the conference was a half hour between sessions... to really encourage people to talk to each other and have all that stuff that happens in the hallway track."*

**Supports Principles**: P4, P6, P10

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [BoostCon, C++Now]
supports: [P4, P6, P10]
-->

---

### E6: The Boost Software License

**Context**: Boost needed a license permissive enough to maximize adoption for the goal of establishing existing practice. Existing licenses were "all too uncom[plicated]" (transcript unclear, likely "uncomfortable" or "complicated").

**What Happened**: Boost created its own license, intentionally minimizing restrictions. The license became visible evidence of Boost's success when "program after program would display the Boost software license at installation or on startup."

**The Outcome**: Success. The permissive license enabled widespread commercial adoption, achieving the goal of establishing existing practice for standardization.

**The Lesson**: Licensing strategy must align with goals. If the goal is maximum adoption, every restriction is friction that reduces use. The visibility of license notices in shipped software provided feedback on success.

> *"At some point that was like, oh wow, this is really a major force in the world."*

**Supports Principles**: P9

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [Boost-license]
supports: [P9]
-->

---

### E7: STL Template Features Standardized Before Implementation

**Context**: When standardizing the STL, the committee invented template features specifically to make the STL work and put them in the standard before any compiler had implemented them.

**What Happened**: Major compilers took "many years" to support all the features. This violated the "standardize existing practice" principle and represented "a black eye for the committee."

**The Outcome**: Mixed/Failure. The STL was ultimately successful, but the long implementation lag caused problems and demonstrated the risks of standardizing unproven features.

**The Lesson**: Standardizing features without existing implementation practice risks discovering they're unimplementable or that implementations won't converge. Even successful features suffer from the delay between standardization and availability.

> *"If you standardize something that's not in practice, who knows if it can even be produced or whether it's economical for a vendor to produce it."*

**Supports Principles**: P1, P11

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/failures
applies-to: language
outcome: mixed
features: [templates, STL]
supports: [P1, P11]
-->

---

### E8: Doug Gregor Lunch Incident

**Context**: Dave encountered a very young-looking person at a committee meeting lunch who he didn't recognize.

**What Happened**: Dave was "kind of rude" and excluded this person from joining his lunch group because he didn't know who he was. The young person turned out to be Doug Gregor, who would become a "powerhouse computer scientist" and one of Dave's closest collaborators.

**The Outcome**: Mixed. Dave later apologized, and he and Doug became close allies working on concepts, move semantics, and other fundamental C++ features.

**The Lesson**: Don't judge contributors by appearance or credentials. Invest in getting to know people—today's unknown newcomer may become tomorrow's most important collaborator. In-person meetings create opportunities for these connections that online interaction doesn't.

> *"He was this really unassuming looking, very, very young guy... later I apologized to him."*

**Supports Principles**: P10

<!-- METADATA
kind: experience
id: E8
source-type: explicit
category: history/decisions
applies-to: both
outcome: mixed
features: [community]
supports: [P10]
-->

---

### E9: The Concepts Debacle

**Context**: Doug Gregor had done "massive work" implementing concepts for C++ to support generic programming. Dave was peripherally involved as an ally of the Indiana group.

**What Happened**: The concepts proposal was "torpedoed at the last minute" in a way that made clear Bjarne Stroustrup would never support what Dave considered the right design. The version eventually adopted "doesn't make life better for people who are doing generic programming"—it only helps consumers of generic components, not authors.

**The Outcome**: Failure (from Dave's perspective). This became one of the factors that drove Dave to leave C++ for Swift. He concluded "C++ was never gonna get there" for supporting generic programming properly.

**The Lesson**: Technical quality doesn't guarantee acceptance; political dynamics can override technical merit. Major features with deep design disagreements may never resolve properly within the committee process. Sometimes the right response is to pursue the vision in a different language.

> *"Doug had done a massive amount of work... and it got torpedoed at the last minute and in such a way that it was clear that Bjarne was never gonna support what I considered to be the right design."*

**Supports Principles**: P11

<!-- METADATA
kind: experience
id: E9
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [concepts, generic-programming]
supports: [P11]
-->

---

### E10: The Sonda Domain Incident

**Context**: After Beman Dawes passed away, his widow Sonda held the boost.org domain. The Boost Foundation wanted to acquire it.

**What Happened**: When Dave called Sonda, she mentioned she was about to finalize an arrangement with "other folks" who had been trying to buy the domain—people associated with the C++ Alliance. Sonda said she didn't want money, just wanted it "in the right place," but they "really insisted on wanting to try to pay" with lawyers involved.

**The Outcome**: Dave convinced Sonda to transfer the domain to the Boost Software Foundation instead.

**The Lesson**: Governance matters. Attempts to acquire assets outside official channels, even with good intentions, undermine trust and legitimacy. "Nobody outside the official governing body should have been trying to buy the domain, especially not... without negotiating it with the Boost Software Foundation."

> *"Stuff should be above board. It worries me to see Boost in the hands of an organization that would go around the official governing bodies to acquire the domain."*

**Supports Principles**: P4

<!-- METADATA
kind: experience
id: E10
source-type: explicit
category: process/politics
applies-to: both
outcome: mixed
features: [governance, Boost-Foundation]
supports: [P4]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Does the library have existing implementations with real-world use? (P1)
- [ ] Is there field experience from users outside the proposer's organization? (P1)
- [ ] Does the library enable domain experts to avoid reimplementing standard components? (P2)
- [ ] Does the interface establish clear conventions users can apply to their own code? (P5)
- [ ] Are algorithms explicit and locally comprehensible, not hidden in object interactions? (P7)
- [ ] Is the licensing permissive enough for broad commercial adoption? (P9)
- [ ] What is the long-term maintenance burden being added to the standard? (P11)

**Questions to Ask**:
1. "What has been the field experience with this implementation?" (P1)
2. "Who outside your organization has used this, and what was their feedback?" (P1)
3. "What design decisions does this library eliminate for users?" (P5)
4. "Show me where the algorithms are—can I read them as coherent computations?" (P7)
5. "If we add this, what can we remove or simplify?" (P11)

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P5, P7, P9, P11]
-->

---

### When Reviewing Language Proposals

- [ ] Is there existing practice with this feature (implementations, use in other languages)? (P1)
- [ ] Have implementers confirmed this is feasible and economical to implement? (P1, E7)
- [ ] Does the proposal minimize wording changes to the standard? (P8)
- [ ] What legacy burden does this add that can never be removed? (P11)
- [ ] Does this enable removing or simplifying existing features? (P11)

**Questions to Ask**:
1. "What existing implementations or language precedents support this design?" (P1)
2. "What's the smallest wording change that achieves this semantic goal?" (P8)
3. "In 20 years, will we wish we hadn't added this?" (P11)
4. "What becomes possible to deprecate if we add this?" (P11)

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P1, P8, P11]
-->

---

### When Navigating Committee Process

- [ ] Am I building understanding or trying to win? (P3, P6)
- [ ] Have I sought allies who can help refine and advocate for the proposal? (P3, E1)
- [ ] Is the proposal presented in a way that minimizes required changes? (P8)
- [ ] Have I engaged with all stakeholders, including international bodies? (P3, E1)
- [ ] Am I attending in-person meetings where relationships form? (P10)

**Questions to Ask**:
1. "Who are the natural allies for this proposal, and have I engaged them?" (P3)
2. "What concerns do opponents have, and have I genuinely addressed them?" (P3, P6)
3. "Is there a smaller, more focused version of this proposal that could succeed first?" (P8)

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P3, P6, P8, P10]
-->

---

### When Running Working Group Sessions or Reviews

- [ ] Is the environment welcoming to newcomers? (P4, E4)
- [ ] Are all arguments being heard, not just the loudest voices? (P4)
- [ ] Am I remaining non-partisan toward solutions? (P4)
- [ ] Is there adequate unstructured time for discussion? (P10)
- [ ] Am I framing discussions as discovery, not competition? (P6)

**Questions to Ask**:
1. "Has everyone who wants to speak had the opportunity?" (P4)
2. "What would change my mind about this?" (P6)
3. "What's the underlying truth we're trying to discover here?" (P6)

<!-- METADATA
kind: checklist
category: groups/lwg
applies-to: both
proposal-type: process
derived-from: [P4, P6, P10]
-->

---

## Open Questions

1. **What specific libraries does Dave consider failures of the "existing practice" principle?** He mentions "a list of libraries where this strategy has failed us" but doesn't enumerate them.

2. **What were the specific evolution principles Google proposed that the committee rejected?** Dave mentions this as evidence of committee dysfunction but doesn't detail the proposals.

3. **What were the specific design differences between the Indiana concepts and Bjarne's concepts?** Dave says the adopted version "doesn't make life better for generic programming authors" but doesn't explain the technical differences.

4. **What happened with the board Dave set up before leaving?** He calls it "a failure" that contributed to recent governance changes but doesn't explain what went wrong.

5. **What were the "other stories" about C++ Alliance interactions that concerned Dave?** He mentions secondhand stories but won't relay them without firsthand knowledge.

6. **What was the specific conflict between Dave and Beman about build systems?** Dave describes it as "very unlike" Beman's normal behavior but doesn't explain the technical substance.

7. **What constitutes sufficient "existing practice"?** Is there a threshold of time, users, or deployment contexts?

8. **What is Dave's current assessment of Swift?** Did it fulfill his hopes for "empowering programmers" better than C++?

---

## Raw Transcript Reference

`inputs/dave-abrahams.md` - Full interview transcript, filmed 2025-12-19 in San Jose, CA.
