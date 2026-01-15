# Glen Fernandes: Captured Knowledge

**Interview Date**: 2025-10-28
**Interviewer**: Ray Nowosielski
**Duration**: ~124 minutes
**Topics Covered**: Boost history since 2011, Peter Dimov, formal review process, Microsoft-era contributions, John Kalb resignation, Boost Foundation vs C++ Alliance, FSC review, Beman Project, standardization process critique, flat_map controversy, networking TS failure

## Executive Summary

Glen Fernandes, longtime Boost contributor, co-maintainer of Smart Pointers, Release Manager, and former Boost Foundation director, provides the most comprehensive insider account of Boost's governance evolution from 2011 to present. His perspective is unique: he saw Boost from inside Microsoft (where teams preferred Boost over Microsoft's own standard library), navigated the Foundation's internal politics, managed the pivotal FSC review, and observed the Alliance/Foundation conflict firsthand.

His most striking contribution is documenting how Microsoft teams in 2011 trusted Boost more than Visual C++'s own STL implementation—and would rather wait for Boost's 3-month release cycle than Microsoft's 2-year compiler cycle for bug fixes. This speaks to Boost's extraordinary reputation for quality and responsiveness.

Most actionable is his account of the FSC review process: when the community decided via formal review (not governance fiat) to transfer Boost assets to C++ Alliance management, the vote was roughly 95-5% in favor—including Boost users "coming out of the woodwork" to support Alliance. This demonstrates that Boost's formal review process can handle governance decisions, not just libraries.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Boost Was the Original Library Evolution Working Group

> *"Boost was the original library evolution working group before there was a library evolution working group. When there were just core and library, Boost was the place where ideas took form."*

**The Principle**: Before WG21 had a Library Evolution Working Group (LEWG), Boost served that function—a place where library ideas matured through review and real-world use before standardization.

**Why It Matters**: This frames Boost's historical role: not just a library collection but the C++ ecosystem's R&D lab. Understanding this explains why Boost libraries dominated early standardization and why creating LEWG changed the dynamics.

**When to Apply**:
- When understanding Boost's historical role
- When evaluating the Beman Project's positioning
- When discussing where new library ideas should mature

**Red Flags**:
- Ignoring Boost's role as the original proving ground
- Assuming LEWG replaced Boost's function entirely
- Treating Boost as merely a library collection

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: history/origins
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P2]
-->

---

### P2: Production Users Trust Boost More Than Vendor Implementations

> *"Microsoft... groups of developers within Microsoft preferred Boost over the product that the company develops... they were using Boost because they trusted Boost more than the standard library implementation."*

**The Principle**: At least as of 2011, professional C++ teams at major companies (including Microsoft itself) trusted Boost implementations over vendor standard library implementations for quality and bug-fix responsiveness.

**Why It Matters**: This is extraordinary social proof: Microsoft's own developers preferred Boost over MSVC's STL. The reasons cited were: faster bug fixes (3-month vs 2-year release cycles), fewer defects, and better handling of edge cases. This validates Boost's quality culture.

**When to Apply**:
- When evaluating library quality claims
- When justifying Boost adoption decisions
- When understanding release cycle importance

**Red Flags**:
- Assuming vendor implementations are always superior
- Ignoring release cycle as a quality factor
- Dismissing community libraries as less professional

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [E1]
related-principles: [P1]
-->

---

### P3: Boost's Formal Review Creates Intense but Valuable Feedback

> *"I would log on, check my email at two in the morning just to see if someone else posted a comment... it was very intense... people who made very useful suggestions. And I realized, oh, you know, yes, I should have..."*

**The Principle**: The Boost formal review process, while emotionally intense for library authors, generates high-quality feedback that materially improves libraries—even (especially) heated discussions.

**Why It Matters**: This validates the review process from an author's perspective. The intensity comes from investment, not dysfunction. Authors lose sleep but gain insights they wouldn't get elsewhere. "Battles and arguments can be a good thing."

**When to Apply**:
- When preparing for formal review
- When evaluating whether to participate in reviews
- When designing feedback processes

**Red Flags**:
- Avoiding reviews due to anticipated intensity
- Dismissing heated feedback as unproductive
- Expecting reviews to be comfortable

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P4]
-->

---

### P4: Review Managers Have Final Authority Despite Non-Voting

> *"It's not a counting votes thing necessarily. The review manager has the final decision and has to exercise their best judgment."*

**The Principle**: Boost review managers exercise judgment, not vote counting. They synthesize feedback quality, not just quantity, to make acceptance decisions.

**Why It Matters**: This prevents gaming the review process through vote mobilization. A thoughtful reject review from an expert can outweigh multiple superficial accepts. This maintains quality by trusting human judgment over pure democracy.

**When to Apply**:
- When interpreting review outcomes
- When writing meaningful reviews
- When selecting review managers

**Red Flags**:
- Treating reviews as vote counts
- Dismissing review manager judgment
- Mobilizing low-quality accept votes

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P3]
-->

---

### P5: Things Get Done When One Person Takes Responsibility

> *"A lot of things just happened because one or two people say, let's do the work... the steering committee declared, oh, Boost is moving to CMake without any plan... Boost has CMake now because one person, Peter Dimov said, I'm gonna start adding CMake support."*

**The Principle**: In Boost, progress happens when individuals commit to doing the work, not when committees issue declarations. Announcements without implementation fail; implementation without announcements succeeds.

**Why It Matters**: This explains why Boost can seem chaotic yet productive. Governance declarations are theater; individual commitment is reality. The CMake transition failed by announcement, succeeded by implementation. The website happened because Vinnie built it.

**When to Apply**:
- When evaluating Boost governance proposals
- When deciding whether to wait for consensus or act
- When understanding why some initiatives succeed and others fail

**Red Flags**:
- Committees declaring changes without implementation plans
- Waiting for governance approval before starting work
- Assuming announcements equal progress

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E3]
related-principles: []
-->

---

### P6: Boost Is Merit-Based, Neutral to Social/Political Issues

> *"Boost is merit based... everyone is welcome here... ideally we could keep all this stuff out of Boost... we would never [ban someone] just by virtue of them being from Russia... it doesn't affect your contributing C++ code."*

**The Principle**: Boost maintains strict meritocracy and neutrality on social/political issues—code quality determines acceptance, not contributor backgrounds or politics.

**Why It Matters**: This explains both Boost's inclusivity (anyone can contribute) and its resistance to activist governance. The Outreachy rejection and Arthur O'Dwyer debates both reflect this: technical contribution matters, other factors don't.

**When to Apply**:
- When evaluating contribution policies
- When navigating controversial situations
- When designing inclusive but neutral processes

**Red Flags**:
- Policies that filter contributors by non-technical criteria
- Code of conduct overreach into political/social enforcement
- Discrimination in any direction

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/community
applies-to: both
confidence: high
supported-by: [E4]
related-principles: []
-->

---

### P7: Boost's License Enables Adoption

> *"Lawyers at various companies have looked at it and have found it to be more permissive and better... than almost every other license... you don't have to publish the boost license along with your release."*

**The Principle**: The Boost Software License is uniquely adoption-friendly—more permissive than MIT, requiring no binary attribution, enabling corporate use without legal friction.

**Why It Matters**: This removes a major barrier to adoption. Unlike MIT/Apache, Boost license requires no license file in binary distributions. Corporate lawyers approve it readily. This is infrastructure for Boost's widespread adoption.

**When to Apply**:
- When choosing licenses for new projects
- When evaluating libraries for commercial use
- When understanding Boost's adoption success

**Red Flags**:
- Using more restrictive licenses without reason
- Ignoring license implications for adoption
- Assuming all permissive licenses are equivalent

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/community
applies-to: library
confidence: high
supported-by: [E1]
related-principles: []
-->

---

### P8: Standardization Can Produce Inferior Designs Through Committee

> *"Through the standardization process... feedback shaped that proposal into a design where rather than vector of pair of key and value, it became two sequence containers... I still question what we put into the C++ standard."*

**The Principle**: The WG21 standardization process can transform proven, widely-used designs (like Boost.Container's flat_map) into inferior alternatives through committee feedback—"design by committee" despite intentions otherwise.

**Why It Matters**: This warns that standardization doesn't guarantee quality. flat_map's standard version uses double allocation where Boost uses single allocation; users now avoid the standard version. The committee's desire for generality produced a design nobody wanted.

**When to Apply**:
- When evaluating standard library designs
- When navigating standardization feedback
- When deciding whether to use standard or Boost versions

**Red Flags**:
- Assuming standard versions are automatically better
- Committee feedback that changes proven designs
- Generality demands that sacrifice real-world utility

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: evaluation/library
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P9]
-->

---

### P9: Networking TS Failed By Seeking Perfection Over Progress

> *"It's now 2025, 2026, and C++ won't have networking... you need to find a third party library to connect to the internet. Which isn't great."*

**The Principle**: The Networking TS (based on ASIO) failed standardization because the committee wanted a more generic abstraction than "just networking"—sacrificing the practical library that the industry was already using.

**Why It Matters**: This is a cautionary tale. ASIO has decades of production use; the Networking TS had vendor implementations; yet committee desire for theoretical generality killed standardization. C++ still has no standard networking in 2026.

**When to Apply**:
- When navigating standardization strategy
- When evaluating generality vs. practicality tradeoffs
- When understanding why certain proposals fail

**Red Flags**:
- Rejecting proven designs for theoretical improvements
- Perfectionism that prevents any progress
- Ignoring industry adoption in favor of committee preferences

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P8]
-->

---

### P10: Peter Dimov Is the Rock Boost Stands Upon

> *"He's the rock that Boost stands upon... he's contributed to almost 80% or more of the Boost Libraries... I've never met anyone like him in my life."*

**The Principle**: Peter Dimov is Boost's most essential contributor—author of Smart Pointers and MP11, contributor to most Boost libraries, responsible for CMake support, and technically brilliant beyond comparison.

**Why It Matters**: This identifies a key-person risk and also explains why certain Boost libraries (Smart Pointers, Core, MP11) have exceptional quality. Beman Dawes speaking "at length about Peter" to other contributors demonstrates his recognized importance.

**When to Apply**:
- When understanding Boost's quality culture
- When evaluating key-person dependencies
- When seeking Boost expertise

**Red Flags**:
- Ignoring Peter Dimov's contributions
- Underestimating key-person risk
- Assuming Boost quality is uniform across libraries

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: history/evolution
applies-to: library
confidence: high
supported-by: [E3]
related-principles: []
-->

---

### P11: The FSC Review Demonstrated Community Preference for Alliance

> *"It was something like 90% to 10% or even 95% to 5%... what was very surprising was Boost users coming out of the woodwork to vote in favor of the C++ Alliance."*

**The Principle**: When given a formal choice via the Boost review process, the community overwhelmingly (95-5%) chose C++ Alliance management over Boost Foundation for asset custody—including users, not just developers.

**Why It Matters**: This resolved the Foundation/Alliance governance dispute through Boost's own mechanisms. The community spoke clearly. The formal review process proved capable of handling governance decisions, not just library acceptance.

**When to Apply**:
- When understanding current Boost governance
- When evaluating community sentiment
- When designing governance decision processes

**Red Flags**:
- Ignoring the FSC review outcome
- Claiming Foundation vs. Alliance is unresolved
- Dismissing user voices in governance decisions

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P5]
-->

---

### P12: The Beman Project May Become the New Standardization Vehicle

> *"The Beman Project is being pitched as the next sort of vehicle for entry into the standard, what Boost was originally... I wouldn't call it a competitor."*

**The Principle**: The Beman Project, led by WG21 working group chairs (Inbal Levi, Jeff Garland), positions itself as the new proving ground for standardization proposals—the role Boost once filled.

**Why It Matters**: This represents a potential fork in the Boost→Standard pipeline. Libraries targeting standardization may go through Beman instead of Boost. This shifts Boost's role toward production-quality libraries rather than standardization prototypes.

**When to Apply**:
- When planning library development strategy
- When understanding standardization pathways
- When evaluating Boost's future role

**Red Flags**:
- Assuming Boost remains the standardization pathway
- Ignoring Beman Project as alternative
- Conflating Boost's production quality role with prototyping role

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: process/actual
applies-to: both
confidence: medium
supported-by: [E6]
related-principles: [P1]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Microsoft Teams Preferred Boost Over MSVC STL

**Context**: Glen joined Microsoft in 2009 and worked in Online Services Division (Bing backend, Bond serialization).

**What Happened**: In 2011, Glen's team was using Boost instead of Visual C++ 10's standard library, even though MSVC was implementing C++11 features. The reasons: (1) Boost had fewer defects in edge cases, (2) bug fixes came in 3 months vs. 2 years for compiler releases, (3) Boost handled certain cases (like nullptr) better. "This is Microsoft, the people that make the compiler and groups of developers within Microsoft preferred Boost."

**The Outcome**: Success. Glen contributed back to Boost while at Microsoft, though this required legal approval due to Microsoft's open source aversion at the time. His manager Chad Walters navigated the approval process to enable Glen's contributions.

**The Lesson**: Trust is earned through quality and responsiveness. Boost's 3-month release cycle and community responsiveness created trust that even vendor implementations couldn't match. This speaks to Boost's production-grade quality culture.

> *"If there's a bug in Boost, we know we can upgrade within three months 'cause that's their release cycle. Whereas to get an upgrade in Visual C++, we might have to wait two years."*

**Supports Principles**: P1, P2, P7

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/evolution
applies-to: library
outcome: success
features: [Microsoft, quality, release-cycles]
supports: [P1, P2, P7]
-->

---

### E2: Glen's Boost.Align Formal Review

**Context**: Glen submitted Boost.Align for formal review in 2013-2014, during a period of low Boost activity.

**What Happened**: The review was "very intense." Glen would check email at 2 AM to see if new criticism had arrived. He had to defend design decisions, accept valid criticism, and make changes during the review period. He struggled to find a review manager because activity was so low. He personally emailed people asking them to submit reviews. The library was accepted with 5 yeses and 1 conditional yes.

**The Outcome**: Success. Boost.Align was accepted on first review. The process, though stressful, improved the library through feedback Glen wouldn't have gotten otherwise.

**The Lesson**: The review process is emotionally demanding but valuable. Authors must actively recruit reviewers. The review manager's judgment matters more than vote counting. Rejection doesn't mean the end—libraries can return for re-review.

> *"Battles and arguments can be a good thing... libraries can get rejected and people take that as a sign to work on it and come back for a second round of review."*

**Supports Principles**: P3, P4

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: process/actual
applies-to: library
outcome: success
features: [formal-review, review-process]
supports: [P3, P4]
-->

---

### E3: CMake Support and Website Development

**Context**: Boost needed CMake support and a modern website for years, but progress was stalled.

**What Happened**: The Boost Steering Committee once "declared" Boost was moving to CMake without any implementation plan—this caused Rene to threaten to leave (and temporarily leave). Years passed with no progress. Then Peter Dimov simply started adding CMake support himself, and it happened. Similarly, the website needed modernization for over a decade (looked "2000 era" in 2013), but the Foundation never funded it. Vinnie Falco built the new website through the C++ Alliance, just doing the work.

**The Outcome**: Success (eventually). CMake support and the new website both exist because individuals committed to doing the work, not because committees declared it would happen.

**The Lesson**: Governance declarations without implementation are empty. Progress comes from individuals taking responsibility. "Nobody owns anything... things organically work because people are willing to put in the effort."

> *"You can't shut that down... a lot of things just happened because one or two people say, let's do the work."*

**Supports Principles**: P5, P10

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: process/actual
applies-to: both
outcome: success
features: [CMake, website, governance]
supports: [P5, P10]
-->

---

### E4: John Kalb's Resignation Over Arthur O'Dwyer

**Context**: John Kalb, Boost Foundation chair and C++ Now organizer, knew Arthur O'Dwyer had a criminal record but included him in conference activities without disclosure.

**What Happened**: When this came to light, David Sankel called a Foundation meeting to discuss John's handling. John was supposed to present his side, but the meeting was rescheduled and John wasn't informed—so he couldn't defend himself. The meeting "painted a picture of John being derelict in his duty." John resigned (or was effectively forced out). Glen later talked to John and learned the sequence of events differed from what was presented.

**The Outcome**: Mixed. John felt "given the short end of the stick." Glen now thinks "too many things happened too quickly without people getting a chance to speak." But the Foundation's position remained: contributor background shouldn't affect code contributions, though conferences are "a different ball game."

**The Lesson**: Due process matters even in volunteer organizations. Quick action without hearing all sides creates injustice. The technical/code side of Boost should remain neutral ("everyone should be able to contribute"), but events require different considerations.

> *"Maybe if we had given John the opportunity to present his case to the whole board, we might've taken a different turn."*

**Supports Principles**: P6

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/failures
applies-to: both
outcome: mixed
features: [John-Kalb, governance, due-process]
supports: [P6]
-->

---

### E5: flat_map and Networking TS Design Degradation

**Context**: Zach Laine's flat_map proposal and the ASIO-based Networking TS both went through WG21 standardization.

**What Happened**: flat_map started as the typical Boost design (vector of pair<key, value>, single allocation). Through standardization feedback, it became two separate containers (vector of keys, vector of values, double allocation). Now users "don't want to adopt the standard version because they want the single allocation." The Networking TS was based on ASIO with decades of production use, but the committee wanted something "more generic"—it could back "both networking and other kinds of IO." As of 2026, C++ still has no standard networking.

**The Outcome**: Failure. flat_map got standardized in a form users don't want. Networking didn't get standardized at all. Both represent committee processes overriding proven designs.

**The Lesson**: Standardization can make things worse. Committee desires for generality can destroy practical utility. Proven, widely-deployed designs (Boost flat_map, ASIO) may be better left as external libraries than committee-modified.

> *"When you hear things like that, you question whether the right thing got into the standard."*

**Supports Principles**: P8, P9

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/failures
applies-to: both
outcome: failure
features: [flat_map, networking, design-by-committee]
supports: [P8, P9]
-->

---

### E6: The FSC Review

**Context**: The Boost Foundation and C++ Alliance were in conflict over asset management, particularly the boost.org domain (which had once lapsed).

**What Happened**: Rather than a governance fight, both sides agreed to let the community decide via formal review. Glen was elected review manager despite being a Foundation director—a testament to community trust. The review was "intense for non-technical reasons." The result: roughly 95-5% in favor of C++ Alliance's FSC taking over Boost assets. "What was very surprising was Boost users coming out of the woodwork to vote in favor of the C++ Alliance."

**The Outcome**: Success. The FSC review resolved the governance dispute through Boost's own mechanisms. The community spoke clearly. Foundation members accepted the outcome.

**The Lesson**: The formal review process can handle governance decisions, not just library acceptance. Community voice matters. When given a clear choice, the community rewarded visible contribution over institutional position.

> *"The community sort of felt like they wanted an end to it. They didn't want to be in between two sides."*

**Supports Principles**: P11, P12

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: process/politics
applies-to: both
outcome: success
features: [FSC-review, governance, Alliance-Foundation]
supports: [P11, P12]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Evaluating Library Quality

- [ ] Does the library have a faster release cycle than vendor alternatives? (P2)
- [ ] Is the library trusted by production users at major companies? (P2)
- [ ] Has it been through Boost formal review or equivalent? (P3)
- [ ] Is there an identifiable maintainer committed to quality? (P10)
- [ ] Does the license enable adoption (Boost license or equivalent)? (P7)

**Questions to Ask**:
1. "Would a team at a major company trust this over vendor alternatives?"
2. "How quickly are bugs fixed?"
3. "Who is responsible for maintenance?"
4. "What license barriers exist for adoption?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: any
derived-from: [P2, P3, P7, P10]
-->

---

### When Navigating Standardization

- [ ] Is the design proven in production, or theoretical? (P8, P9)
- [ ] Will committee feedback improve or degrade the design? (P8)
- [ ] Is there risk of "perfection prevents progress"? (P9)
- [ ] Should this remain an external library instead? (P8)
- [ ] Is Beman Project a better path than Boost for this? (P12)

**Questions to Ask**:
1. "Has this design been used in production for years?"
2. "Will generality requirements destroy utility?"
3. "Is the committee changing proven designs?"
4. "Would users prefer the external version over the standard version?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P8, P9, P12]
-->

---

### When Evaluating Boost Governance Proposals

- [ ] Is there a specific person committed to implementation? (P5)
- [ ] Does it respect Boost's merit-based, neutral culture? (P6)
- [ ] Has the community been given voice through proper process? (P11)
- [ ] Does it address proven problems, not theoretical ones? (P5)

**Questions to Ask**:
1. "Who specifically will do the work to implement this?"
2. "Is this a declaration without a plan?"
3. "Has the community been consulted?"
4. "Does this maintain technical meritocracy?"

<!-- METADATA
kind: checklist
category: process/politics
applies-to: both
proposal-type: any
derived-from: [P5, P6, P11]
-->

---

## Open Questions

1. What is the current status of Boost Fiber in standardization?

2. How has the Beman Project's adoption progressed since 2024?

3. What specific changes did WG21 request that transformed flat_map's design?

4. What were the technical arguments for networking generalization over ASIO?

5. What happened to David Sankel's involvement after the FSC review?

6. How has Peter Dimov's involvement changed over time?

7. What was Microsoft's specific legal process for approving open source contributions?

8. What is the current relationship between C++ Alliance and Boost Foundation?

9. How did the MP11 vs. reflection plenary session in 2018 affect Walter Brown?

10. What is the status of libraries that bypassed Boost review (like Hive)?

---

## Raw Transcript Reference

Source: `inputs/glen-fernandes.md`
Video: https://vimeo.com/1140474568/a6c8392c2d
Filmed: 2025-10-28, Darien, NY
