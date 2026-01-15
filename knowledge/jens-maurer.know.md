# Jens Maurer: Captured Knowledge

**Interview Date**: 2025-11-04
**Interviewer**: Ray Nowosielski
**Duration**: ~84 minutes
**Topics Covered**: Boost Random development, WG21 process since 2000, Core Working Group chairing, proposal quality, chair selection dynamics, Hawaii meeting location, corporate influence (Google), favoritism and socialization, Nat Goodspeed's fiber proposal

## Executive Summary

Jens Maurer, longtime Core Working Group chair and author of Boost.Random (now std::random), provides the most detailed insider account of WG21's actual operational mechanics. As a Core WG participant since 2000 and chair since Steve's retirement, he offers unique perspective on how the committee really works—including candid observations about chair selection, scheduling power, and the value of socialization.

His most striking contribution is the careful admission about favoritism: "being good friends with a chair is helpful" when chairs have more papers than they can schedule. His observation that Nat Goodspeed "should have been a little bit more aggressive in marketing his paper" reveals that technical merit alone doesn't determine progress—social engagement matters.

Most actionable is his account of the Boost→TS→Standard pathway for Boost.Random: the rigorous Boost review established credibility, the library fundamentals TS provided a trial balloon, and his well-written proposal paper became the exemplar others were told to follow. This demonstrates the concrete value of Boost's quality culture for standardization success.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: The Convener Appoints All Chairs

> *"Herb Sutter has been convener for ages and Herb Sutter essentially appoints those chair roles... he usually asks the outgoing chairperson who could be the successor."*

**The Principle**: The WG21 convener (Herb Sutter since 2002) holds ultimate authority over chair appointments. Selection is by invitation, not application, typically consulting outgoing chairs for successor recommendations.

**Why It Matters**: This concentrates significant power in the convener. Chair positions aren't competed for—they're "you get the call." The convener's preferences shape committee leadership for decades. Understanding this power structure is essential for navigating WG21.

**When to Apply**:
- When understanding committee power dynamics
- When evaluating chair behavior
- When planning long-term committee engagement

**Red Flags**:
- Assuming chairs are elected or selected by merit alone
- Ignoring the convener's role in shaping committee direction
- Not understanding how leadership succession works

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P2]
-->

---

### P2: Chair Scheduling Power Creates Implicit Favoritism

> *"Chairs of subgroups get the power to select certain papers that they schedule and others that they don't... being good friends with a chair is helpful in these situations."*

**The Principle**: With more papers than meeting time, chairs must prioritize. This creates implicit favoritism—papers from acquaintances or well-socialized authors get scheduled; others "fall through the cracks."

**Why It Matters**: This is Maurer's most candid admission: technical merit isn't the only factor. Authors who don't "market" their papers or socialize with chairs may see their proposals delayed indefinitely. Nat Goodspeed's fiber proposal exemplifies this: "maybe sometimes he should have been a little bit more aggressive."

**When to Apply**:
- When navigating the standardization process
- When understanding why some proposals advance and others stall
- When advising proposal authors on strategy

**Red Flags**:
- Assuming pure meritocracy in scheduling
- Not investing in committee relationships
- Being "very, very quiet and calm" like Goodspeed

**Supporting Experiences**: E3, E4

<!-- METADATA
kind: principle
id: P2
source-type: tacit
category: process/politics
applies-to: both
confidence: high
supported-by: [E3, E4]
related-principles: [P1]
-->

---

### P3: The Boost→TS→Standard Pathway Works

> *"I made a proposal first to integrate that library into the C++ fundamentals technical specification... it was not directly proposed for integration into C++ 11, but we were doing something like a trial balloon."*

**The Principle**: The effective pathway for library standardization: Boost review → Technical Specification → Standard. The TS provides a "trial balloon" with less commitment than direct standardization.

**Why It Matters**: This pathway provides multiple validation stages. Boost review establishes implementation quality; TS provides committee review and broader feedback; final standardization refines based on experience. Very little from library fundamentals TS1 was not eventually standardized.

**When to Apply**:
- When planning library standardization strategy
- When deciding between direct standardization vs. TS approach
- When evaluating library readiness

**Red Flags**:
- Skipping Boost review when standardization is the goal
- Proposing directly for standard without trial balloon
- Ignoring the maturity that staged approach provides

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E1, E2]
related-principles: [P4]
-->

---

### P4: Paper Quality Matters—Write Like Boost.Random

> *"Future library authors were pointed to my proposal paper as when they asked, how should a proposal look like, make it look like this."*

**The Principle**: Well-written proposals with clear design rationale accelerate standardization. Maurer's Boost.Random proposal became the exemplar for library proposals because of its depth of analysis and clear presentation.

**Why It Matters**: Writing down "design criteria and design decisions is materially different from what the Boost review checked." The committee wants rationale beyond implementation—why these abstractions, why these interfaces, what alternatives were considered. Quality proposals get approved faster.

**When to Apply**:
- When writing standardization proposals
- When preparing for library evolution review
- When advising proposal authors

**Red Flags**:
- Proposals without design rationale
- Implementation-focused without abstraction analysis
- Five-minute presentations (which "wouldn't fly anymore")

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/navigation
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P3]
-->

---

### P5: Hawaii Meetings Repeat Because the Convener Likes Hawaii

> *"The sponsor for the Hawaii meeting, himself likes to be here as far as I've understood. And the meeting location is surprisingly not as expensive."*

**The Principle**: WG21 meeting locations are determined by sponsors paying for venues. Hawaii repeats because Herb Sutter's C++ Foundation sponsors it and Herb likes Hawaii.

**Why It Matters**: This reveals how practical logistics shape committee operations. The convener's foundation controls meeting funding; the convener's personal preferences affect location frequency. This is neither sinister nor ideal—it's just how volunteer organizations work.

**When to Apply**:
- When understanding committee logistics
- When planning meeting attendance
- When evaluating claims about committee neutrality

**Red Flags**:
- Assuming meeting locations are purely practical
- Ignoring the foundation's role in committee operations
- Conflating convenience with corruption

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P1]
-->

---

### P6: Google's Departure Coincided With Carbon's Release

> *"Google had a much, much bigger presence in the C++ committee... some of their proposals took flight. A non-trivial number did not. And now Google has substantially cut down on their presence... the release of carbon coincided temporarily with Google no longer being present."*

**The Principle**: Google sent many people and proposals to WG21, but couldn't always get their way due to ISO's diverse representation. Their departure and Carbon's announcement were temporally correlated.

**Why It Matters**: This is a cautionary tale about corporate influence limits. Even large presence (10+ attendees) doesn't guarantee outcomes. The committee's international representation prevents single-company capture. But when frustrated, companies may "take their ball and go home."

**When to Apply**:
- When evaluating corporate influence in standards
- When understanding why companies create alternative languages
- When assessing ISO process resilience

**Red Flags**:
- Assuming corporate presence equals control
- Ignoring the value of diverse representation
- Missing the connection between committee frustration and language forks

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P6
source-type: tacit
category: process/politics
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: [P2]
-->

---

### P7: Boost Peer Review Was Novel Quality Control

> *"Back then GitHub was not a thing... putting in the time for rigorous quality control—that was the novel thing about Boost."*

**The Principle**: Boost's innovation wasn't just collecting libraries—it was applying peer review before publication. Before GitHub and modern open source, software was "use it or don't use it" without quality vetting.

**Why It Matters**: This frames Boost's historical contribution. The formal review process was genuinely novel—importing scientific peer review to software development. This quality control is what gave Boost libraries credibility that translated to standardization success.

**When to Apply**:
- When understanding Boost's historical value
- When evaluating library quality processes
- When comparing to modern alternatives

**Red Flags**:
- Dismissing Boost review as merely bureaucratic
- Ignoring the pre-GitHub context
- Assuming modern open source provides equivalent vetting

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E1]
related-principles: [P3]
-->

---

### P8: Being Criticized Is Awkward But Necessary

> *"Being criticized is always a process that feels a bit awkward... but I think it's the only way people have discovered so far how you can make progress."*

**The Principle**: Peer review is uncomfortable—your "next best thing since sliced bread" gets "scaled down a bit"—but it's the best mechanism known for quality improvement.

**Why It Matters**: This frames the emotional reality of review. Whether in Boost or standardization, criticism is inherent. Authors must develop psychological resilience. The end result is always better than what goes in.

**When to Apply**:
- When preparing for review
- When receiving criticism
- When designing review processes

**Red Flags**:
- Avoiding review to escape criticism
- Taking criticism personally vs. technically
- Expecting comfortable reviews

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P7]
-->

---

### P9: ISO Process Is Designed to Avoid Surprises

> *"The entire process in ISO is geared towards not having surprises, in particular not having surprises at the late stages... the final vote is sort of the anti-climactic moment."*

**The Principle**: ISO standardization is deliberately incremental, with multiple approval stages, specifically to prevent late surprises. Final votes are anti-climactic because issues are resolved earlier.

**Why It Matters**: This explains why the process feels slow—it's intentionally staged. Each step (paper publication, design approval, wording review, plenary vote) reduces risk. Understanding this design reduces frustration with seemingly bureaucratic steps.

**When to Apply**:
- When navigating standardization timing
- When planning proposal strategy
- When explaining process to newcomers

**Red Flags**:
- Expecting fast standardization
- Viewing baby steps as bureaucracy
- Being surprised at late stage votes

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P3, P4]
-->

---

### P10: Core Working Group Is Like a Quaker Meeting

> *"Core working group has been compared to a Quaker meeting—very calm, except when someone has something to say."*

**The Principle**: The Core Working Group operates calmly compared to Library groups, where more contentious debates occur. Core focuses on precise language specification rather than design disputes.

**Why It Matters**: This explains different subgroup cultures. Library evolution involves more design debates and potential conflicts; Core is more technical and detail-oriented. Understanding subgroup personalities helps navigate committee dynamics.

**When to Apply**:
- When choosing which groups to engage with
- When understanding committee conflict patterns
- When interpreting reports from different subgroups

**Red Flags**:
- Assuming all subgroups operate similarly
- Expecting Library Evolution to be calm
- Preparing for Core debates that won't happen

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/actual
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: []
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Boost.Random Development and Review

**Context**: Maurer developed Boost.Random during accumulated overtime between jobs, driven by frustration with C's global-state random number support.

**What Happened**: He went to Frankfurt University Library to read current research on random numbers, designed a framework separating engines from distributions with minimal interface surface, implemented it, and submitted it to Boost review. The review was "awkward"—being criticized always is—but "as usual with any peer review process, the end result is better than what goes in."

**The Outcome**: Success. Boost.Random was accepted and later became the exemplar for standardization proposals.

**The Lesson**: Quality libraries come from first understanding the problem domain deeply (library research), finding the right abstractions, and accepting peer criticism. Pre-GitHub, this rigorous quality control was Boost's novel contribution.

> *"What would not fly anymore these days... a five minute presentation... 'look, here's the two fundamental abstraction concepts... for details, read my paper.'"*

**Supports Principles**: P7, P8

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: process/actual
applies-to: library
outcome: success
features: [Boost-Random, peer-review, quality]
supports: [P7, P8]
-->

---

### E2: Boost.Random Standardization Journey

**Context**: Moving Boost.Random from Boost library to C++ standard library.

**What Happened**: Rather than proposing directly for C++11, Maurer first proposed for the "library fundamentals technical specification"—a trial balloon. He wrote an HTML paper with design goals, alternatives analysis, and rationale (materially different from Boost documentation which focused on implementation). Bill Blogger, with PhD in mathematics, validated the design. About three meetings to get into the TS, then further refinement before C++11. His paper became the exemplar: "future library authors were pointed to my proposal paper."

**The Outcome**: Success. Boost.Random became std::random in C++11. Very little from library fundamentals TS1 wasn't eventually standardized.

**The Lesson**: The staged pathway (Boost→TS→Standard) provides multiple validation opportunities. Quality proposals with clear rationale accelerate the process. The TS trial balloon reduces risk for both author and committee.

> *"Having a Boost library helps quite a bit. Boost had quite a few credentials of being a high quality library conveyance vehicle."*

**Supports Principles**: P3, P4, P9

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: process/navigation
applies-to: library
outcome: success
features: [standardization, library-fundamentals-TS, proposals]
supports: [P3, P4, P9]
-->

---

### E3: Chair Selection and Meeting Locations

**Context**: Maurer's observations from 25 years in WG21, now as Core Working Group chair.

**What Happened**: Herb Sutter has been convener since approximately 2002, appointing all chairs. "You don't apply for this job, you're being just chosen." When chairs leave, they recommend successors; the convener appoints. Hawaii meetings repeat because the C++ Foundation (chaired by Herb) sponsors them and "Herb likes Hawaii." Google sent 10+ people at peak but couldn't always get proposals approved; they've since cut presence, temporally coinciding with Carbon's release.

**The Outcome**: Insight. The convener's long tenure concentrates power over leadership selection and meeting logistics. ISO's diverse representation prevents single-company capture, but frustrated companies may leave.

**The Lesson**: Understanding power structures is essential for committee navigation. Chair appointments, meeting locations, and scheduling all reflect convener preferences. Corporate influence has limits in ISO's international structure.

> *"The question of whether there's favoritism towards certain proposals regarding personal acquaintances certainly needs careful choice of words in the response."*

**Supports Principles**: P1, P2, P5, P6, P10

<!-- METADATA
kind: experience
id: E3
source-type: tacit
category: process/politics
applies-to: both
outcome: insight
features: [chair-selection, meeting-locations, corporate-influence]
supports: [P1, P2, P5, P6, P10]
-->

---

### E4: Nat Goodspeed's Fiber Proposal

**Context**: Maurer's observations about why Nat Goodspeed's fiber proposal has progressed slowly.

**What Happened**: Goodspeed is "very, very quiet and calm"—his turnaround on papers "wasn't always very quick," and he "fell through the cracks" in scheduling. "Maybe sometimes he should have been a little bit more aggressive in marketing his paper." The proposal barely missed C++26 because Core prioritized "big ticket items"—contracts and reflection—leaving ~15 papers in queue.

**The Outcome**: Ongoing. Fiber is likely targeted for C++29 now. Goodspeed's approach of diligent maintenance without social engagement wasn't sufficient.

**The Lesson**: Technical merit alone doesn't determine progress. Socialization matters: "there's certainly overall value in socializing with other participants... you want acquaintances that can review your papers ahead of time." Authors need to actively advocate, not just wait for scheduling.

> *"If you are dropped from the schedule two or three meetings in a row, that would certainly be reason to make a stink with either the subgroup chair or with the convener."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: process/navigation
applies-to: both
outcome: mixed
features: [fiber, scheduling, socialization]
supports: [P2]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Writing Standardization Proposals

- [ ] Is there clear design rationale, not just implementation? (P4)
- [ ] Are design alternatives discussed and rejected with reasons? (P4)
- [ ] Does the paper follow exemplar style (like Boost.Random)? (P4)
- [ ] Has the library been through Boost or equivalent review? (P3, P7)
- [ ] Is there a staged pathway (TS before standard)? (P3)

**Questions to Ask**:
1. "What are the fundamental abstraction concepts?"
2. "What alternatives were considered and why rejected?"
3. "Would someone point to this paper as an exemplar?"
4. "Has implementation maturity been established?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: library
proposal-type: any
derived-from: [P3, P4, P7]
-->

---

### When Navigating Committee Politics

- [ ] Have relationships been built with relevant chairs? (P2)
- [ ] Is the author actively marketing their paper? (P2)
- [ ] If dropped from schedule repeatedly, has complaint been made? (P2)
- [ ] Is the convener's role understood? (P1)
- [ ] Are meeting logistics (location, timing) being considered? (P5)

**Questions to Ask**:
1. "Who are the relevant chairs and do they know this work?"
2. "Is the author 'very quiet and calm' or actively advocating?"
3. "How long has this been in queue without scheduling?"
4. "What are the big ticket items competing for attention?"

<!-- METADATA
kind: checklist
category: process/politics
applies-to: both
proposal-type: any
derived-from: [P1, P2, P5]
-->

---

### When Evaluating Corporate Influence

- [ ] Is the proposal getting through on merit or presence? (P6)
- [ ] Are diverse stakeholders represented in discussion? (P6)
- [ ] Has a single company been dominating discussion? (P6)
- [ ] Are there signs of frustration leading to exit? (P6)

**Questions to Ask**:
1. "How many people from one company are pushing this?"
2. "Are other stakeholders engaging?"
3. "Has this company threatened to 'take their ball and go home'?"
4. "Is there a competing project being developed privately?"

<!-- METADATA
kind: checklist
category: process/politics
applies-to: both
proposal-type: any
derived-from: [P6]
-->

---

## Open Questions

1. What specific design issues led to Google proposals being rejected?

2. Who recommended Maurer for Core Working Group chair?

3. What is the current status of co-chair succession planning?

4. How has the Code of Conduct changed committee dynamics since implementation?

5. What were the specific "delay moments" that pushed C++11 from 08 to 11?

6. What made Bill Blogger's endorsement significant for Boost.Random approval?

7. How does Core WG "Quaker meeting" culture differ from Library Evolution?

8. What is Nat Goodspeed doing to improve his proposal's chances for C++29?

9. What happened to other proposals from library fundamentals TS1 that didn't make it?

10. How has meeting frequency (2→3 per year) affected committee dynamics?

---

## Raw Transcript Reference

Source: `inputs/jens-maurer.md`
Video: https://vimeo.com/1140852773/f4f135ef24?fl=pl&fe=sh
Filmed: 2025-11-04, Kona, HI
