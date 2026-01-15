# Bryce Lelbach: Captured Knowledge

**Interview Date**: 2025-10-24
**Interviewer**: Ray Nowosielski
**Duration**: ~109 minutes
**Topics Covered**: Boost history, career through Boost, WG21 governance critique, Library Evolution chairing, ISO process critique, what belongs in the standard library, Boost review process, Dave Abrahams' leadership, GitHub's impact on Boost, standards committee reform proposals

## Executive Summary

Bryce Adelstein Lelbach, former Library Evolution Group chair and principal engineer at Nvidia, provides the most comprehensive insider account of both Boost's decline and WG21's governance challenges. His perspective is unique: he entered through Boost's IRC community as a college dropout, rose to chair Library Evolution, ran for convener, and now views Boost as "done"—a successful project that fulfilled its mission.

His most striking contribution is the frank assessment that Boost's decline was not failure but success: once C++11 standardized the most valuable Boost libraries, the motivation to use Boost collapsed. Combined with GitHub's emergence as a distribution channel, Boost's value proposition evaporated. His prescription—that the C++ committee needs a steering council, shared vision, and potentially an exit from ISO—represents the reform wing's agenda.

Most actionable is his framework for what belongs in the standard library: only things that absolutely require compiler integration, platform-specific implementation, or serve as vocabulary types. Everything else should stay outside, because standardization costs are permanent and the ability to distribute via GitHub has eliminated the old rationale.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Boost Saved C++ During Its Dark Period

> *"Boost... kept C++ alive during its long winter period... Before C++11 came out, Boost was where a lot of ideas were being tested and proven. And without Boost, I think you would've seen a much sharper decline in C++ usage."*

**The Principle**: During C++'s decade of stagnation (1998-2011), Boost provided the libraries, community, and innovation pipeline that prevented the language from dying; it was existentially important.

**Why It Matters**: Understanding Boost's historical role explains why it commanded such respect and why its decline is acceptable. Boost wasn't just a library collection—it was the community, the conference (BoostCon/C++ Now), and the proving ground for C++11 features. The language nearly died during the "dark period."

**When to Apply**:
- When evaluating Boost's historical significance
- When understanding C++ culture and gratitude toward Boost
- When analyzing what keeps languages alive during standardization gaps

**Red Flags**:
- Dismissing Boost as "just a library collection"
- Not understanding the 2000-2011 context
- Assuming C++ would have survived without Boost

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: history/successes
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P2]
-->

---

### P2: Boost Is a Victim of Its Own Success

> *"Boost is a victim of its own success. In C++11, some of the most important and highest impact Boost libraries were standardized... Once the most valuable parts of Boost were in the standard, there was less of a motivation to have Boost available."*

**The Principle**: Boost's decline came not from failure but from success—once its most widely-used libraries were standardized, the compelling reason to depend on Boost disappeared.

**Why It Matters**: This reframes Boost's reduced relevance as mission accomplished rather than organizational failure. The goal was always to improve C++, and standardization achieved that. The same dynamic—successful projects losing relevance after achieving their goals—applies broadly.

**When to Apply**:
- When assessing projects that seem to be declining
- When planning library standardization strategies
- When understanding why mature projects lose contributors

**Red Flags**:
- Interpreting declining usage as failure when the mission was achieved
- Not celebrating success because it led to reduced relevance
- Trying to artificially extend a project beyond its natural lifecycle

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: history/evolution
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P3]
-->

---

### P3: GitHub Eliminated Boost's Distribution Value

> *"In the early days... if you needed to go get high quality libraries, you went to Boost... Then GitHub rose to prominence. And then that became the place that people went to look for libraries."*

**The Principle**: Boost's value proposition included distribution—getting a library into Boost meant it would be deployed everywhere Boost was installed. GitHub eliminated this, allowing authors to distribute independently.

**Why It Matters**: This explains why fewer quality libraries come through Boost now. Eric Niebler put Ranges on GitHub instead of Boost because "by that time, the Boost review process had gotten slower... and there was a lot less value to going through" it. The calculus changed.

**When to Apply**:
- When advising library authors on distribution strategies
- When understanding why Boost contributions have declined
- When evaluating the value of curated library collections

**Red Flags**:
- Assuming Boost still offers distribution value
- Not accounting for GitHub/package managers when evaluating Boost's role
- Treating the pre-GitHub era's assumptions as current reality

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: history/evolution
applies-to: library
confidence: high
supported-by: [E2, E3]
related-principles: [P2]
-->

---

### P4: Only What Must Be in the Standard Library Should Be

> *"I only wanna put things in the standard library that absolutely have to be in there... Things that abstract over aspects of different platforms. Things that have to be implemented by the person implementing the C++ compiler."*

**The Principle**: The standard library should contain only: (1) platform abstractions, (2) things requiring compiler integration, and (3) vocabulary types. Everything else should remain external because standardization costs are permanent.

**Why It Matters**: This is Lelbach's framework from his "What Belongs in the C++ Standard Library" talk, developed during his Library Evolution tenure. The C++11 era's "standardize everything" philosophy proved costly because mistakes can't be unwound. The existence of GitHub and package managers eliminates the distribution rationale.

**When to Apply**:
- When evaluating library standardization proposals
- When deciding whether to propose something for standardization
- When assessing the cost/benefit of standard library additions

**Red Flags**:
- "Nice to have" justifications
- Proposals that don't require compiler/platform integration
- Libraries that work fine outside the standard
- Vocabulary types that could be per-project rather than universal

**Supporting Experiences**: E4, E5

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E4, E5]
related-principles: [P5]
-->

---

### P5: The Committee Is Bad at Saying No

> *"One of the problems with the committee is that we're really bad at saying no. We would rather tell somebody 'you go and do some more work on that and come back to us' even when in our hearts we know that we're never gonna ship that feature."*

**The Principle**: WG21 systematically fails to reject proposals that will never succeed, wasting committee time and author effort by avoiding direct rejection.

**Why It Matters**: Lelbach introduced the phrase "knowing that our time and resources are limited" to votes specifically to force acknowledgment of opportunity costs. The backlog problem he inherited partly resulted from inability to definitively close proposals.

**When to Apply**:
- When reviewing proposals that seem unlikely to succeed
- When managing review backlogs
- When deciding how to provide feedback to proposal authors

**Red Flags**:
- "Do more work" guidance when rejection is warranted
- Growing backlogs of dormant proposals
- Authors continuing work on proposals committee members privately consider hopeless

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P4]
-->

---

### P6: Every Feature Takes 10 Years

> *"The average C++ feature, from inception to shipping, takes 10 years... I started corresponding with people about MDSpan in 2014, and we shipped MDSpan in C++23. That's about 10 years."*

**The Principle**: Expect any significant C++ feature to take approximately a decade from initial conception to standardization; faster timelines are exceptional.

**Why It Matters**: This calibrates expectations for both proposal authors and users. After working on a feature for 10 years, there's strong pressure to "ship this, it's good enough" rather than delay another three years. Understanding this dynamic explains committee behavior.

**When to Apply**:
- When planning standardization timelines
- When evaluating whether to start a standardization effort
- When understanding why "wait for more baking time" is resisted

**Red Flags**:
- Expecting features in less than 5 years
- Frustration at "slow" progress on 3-year-old proposals
- Not accounting for the 10-year timeline in planning

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: process/timing
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P5]
-->

---

### P7: Dave Abrahams Was Irreplaceable for Boost

> *"There was only one person that had the willpower and the respect and the authority to be able to make the critical decisions across Boost that needed to be made. And that was Dave... When Dave's focus shifted elsewhere, I think Boost suffered."*

**The Principle**: Boost's functioning depended on Dave Abrahams' unique combination of willpower, respect, and authority to make cross-project decisions; no one could replace him.

**Why It Matters**: Despite Boost's decentralized structure (each library maintainer autonomous), Dave provided the coordination function that kept it coherent. When he left for Apple/Swift, "nobody could replace Dave" and Boost suffered. This explains Boost's organizational challenges.

**When to Apply**:
- When understanding Boost's governance history
- When analyzing why decentralized organizations need coordinating figures
- When planning succession in volunteer organizations

**Red Flags**:
- Assuming decentralized organizations don't need coordinators
- Not identifying who fills the "Dave role" in an organization
- Losing the coordinator without succession planning

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E6]
related-principles: []
-->

---

### P8: ISO Is a Poor Governance Model for Programming Languages

> *"If you look at more modern languages, they tend to not go down the ISO route because there's a lot of overhead and paperwork... The stakeholder model—national bodies—is a terrible stakeholder model for a software project."*

**The Principle**: ISO's national-body voting model is inappropriate for programming language governance; newer languages avoid it, but C++ is trapped within it.

**Why It Matters**: Lelbach identifies ISO governance as a root cause of C++ committee dysfunction. Countries have disproportionate voting power (one company can be an entire national body), the process is closed, and it doesn't reflect the actual stakeholder community.

**When to Apply**:
- When analyzing WG21 dysfunction
- When designing governance for new languages/projects
- When understanding why ISO membership structure matters

**Red Flags**:
- Assuming ISO membership reflects actual stakeholders
- Not accounting for national body dynamics in committee politics
- Applying ISO models to new projects

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P9]
-->

---

### P9: The Committee Needs a Shared Vision

> *"The biggest problem we have with C++ is we have too many cooks in the kitchen. The committee does not have a shared vision, a shared direction. We have 300 individual authors... There's no real attempt to set down a vision."*

**The Principle**: WG21 lacks a consensus vision for C++'s future, leading to incoherent evolution as 300+ individual authors pursue disconnected goals.

**Why It Matters**: Lelbach's reform agenda includes creating a steering council to establish and vote on a shared vision. Without it, the committee is a collection of individual projects rather than a coordinated effort. This explains many inconsistencies.

**When to Apply**:
- When analyzing why committee decisions seem inconsistent
- When proposing governance reforms
- When understanding why "too many cooks" leads to problems

**Red Flags**:
- Treating 300 individual proposals as coherent evolution
- Not attempting to establish shared direction
- Assuming consensus will emerge without deliberate effort

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P8]
-->

---

### P10: Tech Politics Is Unavoidable and Valuable

> *"Everybody would like to think that disagreements in a technical project are always 100% about technical facts. That's not the reality. Sometimes it's that somebody feels like you're on their turf... There's too few people in tech who acknowledge the human side."*

**The Principle**: Technical disagreements often have interpersonal components (territory, respect, inclusion); ignoring this reality makes technical work harder, not purer.

**Why It Matters**: Lelbach self-identifies as a "tech politician" who enjoys building consensus. He argues this skill is undervalued—many technologists pretend politics doesn't exist, which handicaps their ability to navigate it effectively.

**When to Apply**:
- When technical arguments seem disproportionately heated
- When seeking to understand blocked proposals
- When building consensus for controversial changes

**Red Flags**:
- "It's purely technical" when it clearly isn't
- Ignoring interpersonal dynamics in technical discussions
- Treating political skill as unprincipled

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E5]
related-principles: []
-->

---

### P11: Conferences Launched Careers in the Pre-GitHub Era

> *"I got my first job through Boost... almost all of my early connections in the industry were through Boost. For me, somebody who was a college dropout who didn't have any credentials... giving talks at conferences was one of the ways I could build up a reputation."*

**The Principle**: Before GitHub profiles, conference talks were the primary credential-building mechanism for developers without degrees; Boost/C++ Now provided this pathway.

**Why It Matters**: Lelbach's career demonstrates how the Boost community functioned as an alternative credentialing system. The C++ Now student volunteer program he created extended this, producing many current C++ leaders (Michael Park, Louis Dionne, etc.).

**When to Apply**:
- When advising people without traditional credentials
- When understanding the value of conference participation
- When evaluating alternative credentialing systems

**Red Flags**:
- Assuming degrees are the only path
- Undervaluing open source contribution as credentials
- Not creating pathways for non-traditional contributors

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P11
source-type: tacit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1]
related-principles: []
-->

---

### P12: Ship Minimal Viable Products, Defer Additive Changes

> *"When proposals came before me, my first thought would be 'what can I cut out? What parts do we not need to ship in version one?' If we can ship it later, if it's an additive change... great. Give me as little as possible for the first version."*

**The Principle**: Standard library features should ship as minimal viable products; anything that can be added later should be deferred. Only ship what you'd be unable to add later.

**Why It Matters**: This was Lelbach's primary criterion as Library Evolution chair. It reduces risk, accelerates shipping, and reserves flexibility. The key question: "If we don't ship this piece now, can we ship it later?" If yes, defer it.

**When to Apply**:
- When designing library proposals
- When reviewing proposals for scope
- When prioritizing features within a proposal

**Red Flags**:
- "While we're at it" feature additions
- First versions with extensive bells and whistles
- Features that could be additive but are bundled into v1

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P12
source-type: explicit
category: evaluation/scope
applies-to: library
confidence: high
supported-by: [E4]
related-principles: [P4, P5]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Bryce's Path from IRC to Principal Engineer

**Context**: Lelbach as a college dropout with no credentials, living with parents after being kicked out of school.

**What Happened**: Through Boost IRC, he connected with Hartmut Kaiser (just "a handle on a chat room"), who offered him a job at LSU sight unseen. Lelbach bought a one-way ticket to Louisiana, joined Hartmut's research lab, gave his first talk at BoostCon 2010, and built his career through conference talks because "giving talks was one of the ways I could build up a reputation for myself" without credentials.

**The Outcome**: Success. Lelbach became Library Evolution chair, ran for convener, and is now a principal engineer at Nvidia. The C++ Now student volunteer program he created produced many current C++ leaders.

**The Lesson**: Open source communities and conferences can provide alternative credentialing pathways for talented people without traditional qualifications. Boost served this function for an entire generation.

> *"For me, somebody who was a college dropout who didn't have any credentials, the first four years of my career... giving talks at conferences was one of the ways I could build up a reputation."*

**Supports Principles**: P1, P11

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [boost, conferences, career-development]
supports: [P1, P11]
-->

---

### E2: Eric Niebler Bypassing Boost for Ranges

**Context**: Eric Niebler developing the Ranges library that would become a major C++20 feature.

**What Happened**: People suggested Niebler put Ranges into Boost. He declined. "By that time, the Boost review process had gotten a bit slower because there were fewer people involved, and there was a lot less value to going through the Boost review process." Instead, he put it directly on GitHub and used the C++ standards review process for vetting.

**The Outcome**: Success. Ranges shipped in C++20 without ever being a Boost library. This demonstrated that the "Boost → Standard" pipeline was no longer necessary.

**The Lesson**: When distribution value evaporates (GitHub exists) and review costs remain high (fewer Boost reviewers), rational authors bypass Boost entirely. The calculus that made Boost valuable has changed.

> *"Eric's philosophy was, I'm just going to use the C++ standard review process as the way of vetting this thing. He just put his Range implementation on GitHub."*

**Supports Principles**: P2, P3

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/evolution
applies-to: library
outcome: success
features: [ranges, C++20, github]
supports: [P2, P3]
-->

---

### E3: Boost ASIO's Special Status

**Context**: Boost ASIO (async I/O library) was one of the most widely used Boost libraries, developed by Chris Kohlhoff.

**What Happened**: ASIO existed before Boost and had special conditions: Chris wanted to continue distributing it independently. During Boost integration, many libraries accumulated dependencies ("you should use this other Boost library instead of your code"), making them interdependent. Chris resisted this, maintaining standalone and header-only versions.

**The Outcome**: Mixed. ASIO remains valuable, but its standardization (via executors) became "the executors debacle" that Lelbach mentions but won't detail.

**The Lesson**: Pre-existing popular libraries entering Boost had different dynamics than libraries developed within Boost. Maintaining independence required explicit conditions. The dependency accumulation problem made Boost monolithic.

> *"Chris's condition was he wanted to continue to be able to distribute ASIO independent of Boost... he didn't want every Boost library to depend on every other Boost library."*

**Supports Principles**: P3

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/decisions
applies-to: library
outcome: mixed
features: [boost-asio, executors]
supports: [P3]
-->

---

### E4: Lelbach as Library Evolution Chair

**Context**: Lelbach chairing Library Evolution during C++20/23 development, inheriting a massive backlog.

**What Happened**: He introduced "knowing that our time and resources are limited" into vote language, emphasizing opportunity costs. His primary criterion became "what can I cut out?" He pushed for minimal viable products and tried to teach the committee to say no. He decentralized work, built a team, and prepared his successor (Inbal Levi).

**The Outcome**: Success (for his tenure). The backlog was better managed, the committee learned to reject some proposals, and he built a sustainable organization rather than doing everything himself. He stepped down after three years as planned.

**The Lesson**: Committee chairs can shift culture by changing language (opportunity cost acknowledgment), focusing on reduction rather than addition, and building organizations rather than being heroes.

> *"One of the problems with the committee is that we're really bad at saying no. I wanted us to acknowledge verbally that we're committing to spending more time on this thing, knowing that our time and resources are limited."*

**Supports Principles**: P4, P5, P6, P12

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [library-evolution, committee-management]
supports: [P4, P5, P6, P12]
-->

---

### E5: WG21 Governance Critique

**Context**: Lelbach's experience in committee leadership, including his convener run (which he couldn't discuss due to Nvidia restrictions).

**What Happened**: He observed that ISO's national body voting model gives disproportionate power to small countries (one company can be an entire national body), the process is closed and unwelcoming to newcomers, there's no shared vision ("300 individual cooks"), and features take 10 years. He proposed steering and implementer councils to reform governance.

**The Outcome**: Mixed. Reform efforts continue. Lelbach says he's happy he didn't become convener because "presiding over a dying empire" would have been limiting, and the convener can't fix ISO-dictated problems anyway.

**The Lesson**: ISO governance creates structural problems for C++ that individual leaders can't fix. The reform agenda requires either changing ISO or exiting it—neither is easy.

> *"I think we need to find a way to exit ISO and to evolve C++ outside of ISO, which I think would be the best thing for C++."*

**Supports Principles**: P8, P9, P10

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: process/actual
applies-to: both
outcome: mixed
features: [WG21, governance, ISO]
supports: [P8, P9, P10]
-->

---

### E6: Dave Abrahams' Irreplaceable Role

**Context**: Lelbach reflecting on Boost's functioning before and after Dave left for Apple.

**What Happened**: "There was only one person that had the willpower and the respect and the authority" to make cross-Boost decisions—Dave Abrahams. When Dave left for Apple/Swift, "Boost suffered because of that" and "there was nobody who could replace Dave." Lelbach recalls early friction with Dave (having commit access revoked) but later deeply missing his presence.

**The Outcome**: Failure (for Boost post-Dave). Without the coordinating authority, Boost's decentralized model couldn't make collective decisions effectively.

**The Lesson**: Even decentralized organizations need someone who can make cross-cutting decisions. Dave's unique combination of willpower, respect, and authority was irreplaceable. This is a succession planning failure.

> *"I immensely missed Dave's presence in Boost and I did not realize the degree to which Dave was essential to the functioning of Boost."*

**Supports Principles**: P7

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/evolution
applies-to: library
outcome: failure
features: [boost, dave-abrahams, governance]
supports: [P7]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Does this require compiler integration or platform-specific implementation? (P4)
- [ ] Is this a vocabulary type that needs universal definition? (P4)
- [ ] Could this be distributed via GitHub instead? (P3, P4)
- [ ] What is the minimal viable product? What can be deferred? (P12)
- [ ] Are we likely to actually ship this, or should we just say no? (P5)
- [ ] How many years has this already taken? (P6)

**Questions to Ask**:
1. "Why does this need to be in the standard rather than on GitHub?"
2. "What compiler support does this require?"
3. "What can be cut from version one?"
4. "If we defer this piece, can we add it later?"
5. "Are we being honest about whether this will ever ship?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P3, P4, P5, P6, P12]
-->

---

### When Assessing Standards Committee Health

- [ ] Is there a shared vision that proposals can be evaluated against? (P9)
- [ ] Is the committee good at saying no to proposals? (P5)
- [ ] Are interpersonal dynamics being acknowledged? (P10)
- [ ] Is the governance model serving the actual stakeholders? (P8)
- [ ] Are pathways open for non-traditional contributors? (P11)

**Questions to Ask**:
1. "What is the vision this proposal serves?"
2. "When did we last reject a proposal outright?"
3. "What non-technical factors are influencing this discussion?"
4. "Who are the actual stakeholders, and are they represented?"
5. "How do newcomers get involved?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P5, P8, P9, P10, P11]
-->

---

### When Evaluating Boost's Role Today

- [ ] Is this library's value in distribution, or just quality? (P3)
- [ ] Would GitHub distribution serve equally well? (P3)
- [ ] Is the review process cost justified by the benefits? (P2)
- [ ] Has Boost already fulfilled its mission for this domain? (P2)
- [ ] Is there a "Dave" figure who can make cross-cutting decisions? (P7)

**Questions to Ask**:
1. "What does Boost provide that GitHub doesn't?"
2. "Is the Boost review process faster/better than direct standardization?"
3. "Has Boost already proven this concept, making further work unnecessary?"
4. "Who makes collective decisions in Boost today?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: adoption
derived-from: [P2, P3, P7]
-->

---

## Open Questions

1. What specifically happened with the ASIO/executors standardization effort that Lelbach calls "the debacle"?

2. What happened in Lelbach's convener run that he couldn't discuss due to Nvidia restrictions?

3. What are the specific reform proposals for WG21 governance—steering council details, implementer council composition?

4. What was Google's specific ask regarding "breaking changes more frequently" that led to their disengagement?

5. What libraries were rejected during Lelbach's Library Evolution tenure, and what reasons were given?

6. What is Lelbach's view on Beman (the project) versus Boost going forward?

7. What specific cultural/political conflicts in Boost were referenced that he couldn't discuss?

8. How did the convener election work procedurally, and who were the candidates?

9. What would "exiting ISO" look like practically for C++?

10. What is Lelbach's assessment of his predecessors' strengths—Jeffrey Yasskin's "wizard at consensus," Titus Winters' "design sense"?

---

## Raw Transcript Reference

Source: `inputs/bryce-lelbach.md`
Video: https://vimeo.com/1141544290/9d6d3d6e9d?fl=pl&fe=sh
Filmed: 2025-10-24, New York City, NY
