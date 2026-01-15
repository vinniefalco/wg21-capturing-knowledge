# Robert Ramey: Captured Knowledge

**Interview Date**: 2025-12-16
**Interviewer**: Ray Nowosielski
**Duration**: ~124 minutes
**Topics Covered**: Boost Serialization library, formal peer review process, Dave Abrahams, Peter Dimov, Andrei Alexandrescu, MPL (Meta Programming Language), template metaprogramming, BoostCon, Boost Build (B2) vs CMake, Boost Library Incubator, networking standardization, Vinnie Falco, C++ Alliance, software licensing (BSL), open source philosophy, AI and future of software development.

## Executive Summary

Robert Ramey, author of the Boost Serialization library, provides a deeply personal and historically rich account of his journey through the Boost ecosystem, offering unique insights into the peer review process, the dynamics of technical collaboration, and the evolution of open-source software development. His narrative is characterized by a self-described "pathologically stubborn" approach to problem-solving, which led him from building his own house to creating one of Boost's most complex libraries.

Ramey's most profound contribution is his detailed exposition of the Boost formal review process as a crucible for personal and technical growth. He recounts his library's initial rejection, his explicit response to every criticism raised, and the subsequent acceptance—a testament to the process's rigor and transformative power. His story of a reviewer's graceful concession ("I've done my best. I'm sorry I failed to convince you") causing him to reconsider and ultimately change his design is a masterclass in how humility and persistence can lead to superior technical outcomes.

The interview reveals Ramey's complex relationships with key Boost figures, particularly Dave Abrahams, whom he characterizes as initially intimidating and dismissive but who later acknowledged Ramey's abilities ("Ramey surprised me again"). He credits Abrahams' MPL library (with Aleksey Gurtovoy) as foundational to his serialization work, describing it as bringing template metaprogramming "from outer space just into the stratosphere." His observations on Peter Dimov's shared_ptr as solving "a common problem for which there was no good solution" and getting "accepted or included into the standard library with no change at all" highlight the impact of well-designed Boost libraries.

Ramey offers a provocative perspective on Boost's post-C++11 identity crisis, arguing that "70% of Boost got incorporated into the standard" and Boost subsequently "lost its way." His critique of Vinnie Falco's vision as "delusional" (a term he explicitly stands by) while simultaneously acknowledging "more power to you" reflects the tension between old-guard skepticism and new leadership initiatives. His failed Boost Library Incubator project and ongoing frustrations with the B2 vs CMake debate illustrate the organizational challenges of evolving established open-source communities.

Most philosophically, Ramey's reflections on software licensing and the future of development—from "all software development was proprietary" to open source to "AI generated code"—frame Boost contributors as "dinosaurs" in an evolutionary sense, while emphasizing the enduring importance of individual genius: "We should river it more... some guy coding the zip format... We use it every day. Do you know his name?"

---

## Principles

### PRINCIPLE-RR-01: The Graceful Concession Pattern

**Principle**: When trying to convince someone of a technical point, gracefully acknowledging failure to convince—rather than escalating conflict—can paradoxically trigger deeper reconsideration than persistent argumentation.

**Source Type**: Explicit

**Category**: Working Group Dynamics / Interpersonal Effectiveness

**Direct Quote**:
> "His final sentence is, 'Well, okay, I've done my best. I'm sorry I failed to convince you.' And then for some reason, that one sentence... made me take it seriously as opposed to just spitballing. And I stepped back and I said, son of a bitch, the guy is actually right."

**Elaboration**: Ramey describes this moment as "character building" and credits it with teaching him when to switch from "they can't be right" to "they are right" mode. The pattern suggests that ego defense mechanisms are disarmed not by persistent attack but by graceful withdrawal, creating psychological space for genuine reflection.

**Application to WG21**: When advocating for design positions in working groups, strategic retreat with grace can be more effective than escalation. Acknowledging "I've made my case, the committee disagrees" may open minds that sustained argumentation closes.

---

### PRINCIPLE-RR-02: Explicit Response to Every Criticism

**Principle**: When a proposal is rejected, systematically enumerate every criticism raised and explicitly address each one in the revision—document this mapping publicly.

**Source Type**: Explicit

**Category**: Proposal Development / Revision Strategy

**Direct Quote**:
> "I explicitly went through the list of all the points that were brought up in the first review and made sure that the second version of the library addressed every single one. And at that point, when the thing went through review, it actually pretty much just coasted through because I did the work."

**Elaboration**: Ramey's serialization library was initially rejected. Rather than disputing the rejection or making selective improvements, he created a systematic response document addressing every point. This demonstrated respect for reviewers' time and signaled genuine engagement with feedback.

**Application to WG21**: Proposals that stall should be revised with explicit point-by-point response to committee feedback. Papers that say "we addressed concerns about X, Y, and Z as follows..." signal seriousness and increase likelihood of forward progress.

---

### PRINCIPLE-RR-03: The Two-Week Pressure Cooker

**Principle**: Compressing expert review into a defined time window forces focused attention and generates more actionable feedback than open-ended review periods.

**Source Type**: Explicit

**Category**: Process / Review Methodology

**Direct Quote**:
> "The formal review... is a period lasting two weeks... you get these reports, you answer questions, and of course when you answer questions, it becomes totally apparent that the documentation you wrote isn't sufficient... All this feedback you get gives you fodder to make it better or to address it or to convince you that it's a lost cause or both."

**Elaboration**: Ramey describes approximately 30 capable reviewers investing "one or two days trying to use your library" during the compressed window. The time-boxing creates urgency while the concentration of feedback makes deficiencies unmistakably clear.

**Application to WG21**: The formal review model suggests that concentrated, time-boxed review periods may yield better results than the diffuse review that occurs across multiple committee meetings spread over years.

---

### PRINCIPLE-RR-04: Rejection as Feature Selection

**Principle**: A rigorous consensus process, while frustrating in its slowness, acts as a "brake against really bad ideas" and is preferable to premature standardization.

**Source Type**: Explicit

**Category**: Process / Proposal Evaluation

**Direct Quote**:
> "The funny thing is, and great thing is, that the consensus process, since they can't reach consensus, we're not stuck with something that doesn't work. So, although I criticize the whole concept of consensus, it does act as a brake against really bad ideas."

**Elaboration**: Ramey uses networking standardization's 20-year stalemate as paradoxical evidence of the process working: "I laugh because 20 years people have been talking about it and 20 years as far as I'm concerned, there's zero progress." Yet he sees this as preferable to a bad standard.

**Application to WG21**: Proposals that fail to achieve consensus may be correctly identified as not yet ready. Extended deliberation, while painful, can prevent "std::auto_ptr"-style mistakes that burden the language for decades.

---

### PRINCIPLE-RR-05: Abstraction vs. Practicality Tension

**Principle**: The hardest library design problems involve balancing abstract generality with practical equipment constraints—solving one side creates "a mess" without the other.

**Source Type**: Explicit

**Category**: Design Philosophy / Library Design

**Direct Quote**:
> "On one hand you have an abstract problem, on the other hand, you're working with real equipment and you, if you try and meld them, you end up with something that's really a mess... The trick is to find a way to address both of those issues without turning into something that's so complicated no one can understand."

**Elaboration**: Ramey identifies this as the fundamental challenge of networking standardization: "Networking is worse than serialization as far as that's concerned." The tension explains both why certain libraries succeed (shared_ptr solved both cleanly) and why others stall indefinitely.

**Application to WG21**: Proposals should demonstrate they've grappled with both the abstract interface design and the practical implementation constraints. Papers that feel "too abstract" or "too hardware-specific" may be correctly identified as unbalanced.

---

### PRINCIPLE-RR-06: Canonical Solutions to Common Problems

**Principle**: The highest-impact libraries solve problems "for which there was no good solution at the time" with designs so definitive that "nobody's come up with a better solution since."

**Source Type**: Implicit

**Category**: What Belongs in the Standard / Impact Criteria

**Direct Quote**:
> "[shared_ptr] was like the canonical solution to a common problem... it did address a lot of the most difficult aspects of multi-threaded programming... Almost everybody was getting it wrong. And then within the Boost framework... his shared pointer library pretty much got accepted or included into the standard library with no change at all."

**Elaboration**: Ramey describes both serialization and shared_ptr as "canonical solutions"—libraries that define the correct approach so thoroughly that variants become unnecessary. This stands in contrast to "framework" libraries that provide mechanisms but not answers.

**Application to WG21**: Standard library additions should aspire to be canonical solutions, not just useful utilities. "Could someone reasonably do this better?" is a key evaluation question.

---

### PRINCIPLE-RR-07: Enable Tools for Meta-Work

**Principle**: Libraries that enable other libraries (like MPL enabling serialization) have multiplicative impact and justify their abstraction overhead through downstream productivity.

**Source Type**: Explicit

**Category**: What Belongs in the Standard / Library Ecosystem

**Direct Quote**:
> "David Abraham's used this meta programming facility to generate a library of useful things that meta programming can do. At that point, he brought it back from outer space just into the stratosphere. And so it became more usable to, for the rest of us. And I depended upon it to make the serialization library."

**Elaboration**: Ramey credits MPL as essential to serialization: "I don't know that I could have done it without MPL." This highlights a category of "meta" libraries whose value lies not in direct use but in enabling other work.

**Application to WG21**: Evaluation criteria for "foundational" libraries (type traits, concepts, metaprogramming facilities) should consider downstream enablement, not just direct utility.

---

### PRINCIPLE-RR-08: Descriptive Names Over Branding

**Principle**: Library names should be descriptive rather than branded, because branding signals ego and marketing rather than technical merit.

**Source Type**: Explicit

**Category**: Design Philosophy / API Design

**Direct Quote**:
> "I was very put off by the name Beast because I always wanted libraries whose names were descriptive... to make a name that's like Beast... it's very egocentric. And it's kind of like branding, which is off-putting to me."

**Elaboration**: Ramey contrasts branded names with his preference for "something so fundamentally obviously a good idea that it takes off on its own." This reflects a broader philosophy that technical merit should speak for itself.

**Application to WG21**: While not directly applicable to standardese, this principle suggests that proposal naming and marketing should emphasize clarity over cleverness. Names like `std::optional` succeed where clever names might alienate.

---

### PRINCIPLE-RR-09: Grand Gestures in Community Building

**Principle**: Outsized community investments—sponsoring events, providing resources, visible generosity—build social capital that enables technical leadership.

**Source Type**: Implicit

**Category**: Working Group Dynamics / Leadership

**Direct Quote**:
> "Vinnie is the master of the grand gesture... he sponsored free drink tickets for everybody in the room... The way he promoted his library was far, far more extensive than anybody has ever promoted their library. My view on that... I said, hey, it's a thing. Doesn't hurt. See how it goes. And apparently it's gone well."

**Elaboration**: Despite his skepticism of Vinnie's broader vision ("delusional"), Ramey acknowledges the effectiveness of grand gestures in community building. This represents a shift from purely technical meritocracy to recognizing social dynamics.

**Application to WG21**: Technical excellence is necessary but not sufficient for influence. Investing in community—hosting dinners, sponsoring events, mentoring newcomers—builds the relationships that enable proposals to advance.

---

### PRINCIPLE-RR-10: Dinosaurs and Disruption

**Principle**: Recognize when established paradigms are being disrupted, and acknowledge that current expertise may become obsolete even while that expertise remains valuable for its historical period.

**Source Type**: Explicit

**Category**: Historical Knowledge / Ecosystem Context

**Direct Quote**:
> "Those of us in Boost, myself included, we're all dinosaurs. It's an epic... this is not gonna really repeat itself in the same way... I don't know what worlds are gonna have to conquer, but I don't think it's gonna be these worlds now."

**Elaboration**: Ramey's framing of Boost contributors as "dinosaurs" acknowledges both their historical importance and their potential irrelevance to future paradigms. This humility about expertise expiration is rare in technical communities.

**Application to WG21**: Long-serving committee members bring invaluable historical knowledge but should remain open to paradigm shifts (AI-generated code, new safety models) that may invalidate assumptions built over decades.

---

## Experiences

### EXPERIENCE-RR-01: The Rejected Serialization Library

**Experience Type**: Personal Anecdote

**Narrative**:
Ramey's Boost Serialization library was rejected on its first formal review submission. Rather than dispute the rejection or abandon the project, he systematically addressed every criticism:

> "I got a lot of feedback from the first go round when the library was rejected and I recognized that the rejection was totally appropriate and valid. I doubled down and I explicitly went through the list of all the points that were brought up in the first review and made sure that the second version of the library addressed every single one."

The result was transformative: "At that point, when the thing went through review, it actually pretty much just coasted through because I did the work. I took a hint and doubled down instead of putting on my hat and saying, 'hell with you guys.'"

**Key Insight**: The rejection was not an obstacle but a gift—it provided the roadmap for improvement.

**Category**: Process / Proposal Development

---

### EXPERIENCE-RR-02: The Raw Pointer Serialization Debate

**Experience Type**: Technical Dispute Resolution

**Narrative**:
During the serialization review, a reviewer challenged Ramey's approach to serializing raw pointers. Ramey initially "blew it off" and "argued against it" because of his investment in the existing approach:

> "We had a back and forth and he said, 'Well, gee, I guess I just failed to convince you.' And which was true. And the way he did that... I remember that to this day. It was sometime later, maybe a day or maybe just later the same day or maybe a couple days later, I'm thinking, son of a bitch. Actually that guy is right and I was wrong."

The graceful concession triggered genuine reconsideration: "That's something that doesn't happen very often for somebody to say that. And... the way he gracefully acknowledged that I had the final say motivated me to look more carefully."

**Key Insight**: Graceful retreat can be more persuasive than persistent argument.

**Category**: Working Group Dynamics

---

### EXPERIENCE-RR-03: Dave Abrahams' Evolving Assessment

**Experience Type**: Interpersonal Dynamics

**Narrative**:
Ramey describes a complex relationship with Dave Abrahams that evolved from dismissive to respectful. Initially:

> "My C++ skills when I started the serialization library were not particularly great... David Abrahams would dispute it, knowing much more than I about the subject. And I would then also dispute his argument. And so we, and his way of handling a dispute with a person like me revealed his own personality weaknesses."

Ramey recounts a numerical analysis dispute where Abrahams lectured him despite Ramey's graduate-level training under William Kahan, "the inventor of the floating point library for C++." But over time:

> "He did come to respect me and which was totally contrary to our initial interaction. Our interaction improved a lot... he did say to somebody at one point, he considered me his friend."

A collaborator (Mattias Troyer) reported Abrahams saying: "This guy, he surprised me again"—suggesting grudging acknowledgment of Ramey's abilities.

**Key Insight**: Initial dismissiveness from senior figures can evolve into respect through persistent, quality work.

**Category**: Working Group Dynamics

---

### EXPERIENCE-RR-04: Mattias Troyer and Design Purity

**Experience Type**: Design Compromise

**Narrative**:
Ramey resisted changes to the serialization library proposed by Mattias Troyer (now at Microsoft on quantum computing) to improve floating-point performance because it would "pollute the pristine structure" of his design:

> "My motivation for working on a piece of computer code is artistic perfection. And sometimes that will get in the way of actually finishing something."

Troyer came to Ramey's house in Santa Barbara, and after a hike overlooking the city, they discussed the changes. Despite Ramey's resistance:

> "In the end, he did manage to convince me and he was working closely with David Abrahams... they were right to destroy the purity of the library for a practical end."

**Key Insight**: "Artistic perfection" in design can be an impediment; practical improvements may require accepting impurity.

**Category**: Design Philosophy

---

### EXPERIENCE-RR-05: The First BoostCon and Dave Abrahams' Neck

**Experience Type**: Community Formation

**Narrative**:
Ramey attended the first BoostCon in Aspen with vivid recollection:

> "I was sitting in tourist class and tourist class on one of these commuter planes is like super cramped. The guy is probably six and a half feet tall and he's got a neck that looks like it's about a foot long. And I knew it was him right away 'cause I was about 10 rows back and that was his head sticking up. And that was the first time I actually saw him in the flesh. I didn't approach him 'cause I knew I'd be running into him eventually. And I didn't want to start that now."

The conference itself was transformative: "The Boost Conference I really loved... you're not just at a conference, it was Boost... I would get a chance to meet the people... rub elbows with a group of peer people that I would like to consider my peers."

**Key Insight**: Face-to-face community gatherings create bonds that mailing lists cannot.

**Category**: Historical Knowledge / Community

---

### EXPERIENCE-RR-06: Peter Dimov—Acerbic Genius

**Experience Type**: Character Study

**Narrative**:
Ramey provides a nuanced portrait of Peter Dimov:

> "Peter Dimov and I dispute stuff all the time. I actually asked him for once, I asked him for a letter of recommendation, 'cause I wanted to attend a particular course, and he refused to give it. So we have... he's kind of a little bit of an acerbic kind of guy."

Yet Ramey acknowledges Dimov's immense contributions: shared_ptr "solved a problem for which there was no good solution at the time... pretty much got accepted or included into the standard library with no change at all."

On Dimov's absence from conferences: "Somebody said, well, his English accent is so bad, he's embarrassed about it. And I just laugh my ass off on that because... if you read the way he writes, English is perfect."

**Key Insight**: Technical genius often comes with personality quirks; the community learns to work around them.

**Category**: Historical Knowledge / Key Figures

---

### EXPERIENCE-RR-07: The Boost Library Incubator

**Experience Type**: Failed Initiative

**Narrative**:
Ramey created the "Boost Library Incubator" (theblinkabator.com) to improve the submission process:

> "I wanted people to be able to submit a Boost library and get feedback on it before the review so they wouldn't have to do what I did, which is to suffer all that goes with making something that's not up to snuff and have it rejected and then go back and try and do it again."

The system allowed posting reviews without waiting for formal review periods. It achieved partial success: "It did get a number of submissions... it would shortcut the whole process in case of failure. And if your idea didn't get much traction, well at least you didn't get any public humiliation."

But maintaining the WordPress-based system proved too burdensome: "The level of effort and maintenance that would be required... was really more than I wanted to dedicate. So I let it, I cast it aside."

**Key Insight**: Good process improvements require sustained maintenance investment; without dedicated resources, they fail.

**Category**: Process / Community Infrastructure

---

### EXPERIENCE-RR-08: The B2 vs CMake Wars

**Experience Type**: Organizational Conflict

**Narrative**:
Ramey has been "unhappy with the Boost building process for many years." The conflict between Boost Build (B2) and CMake remains unresolved:

> "It's still not done. It's never gonna be done because the enthusiasts of Boost Build are hanging in there doing everything they can to keep the transition from CMake to CMake from happening. And they've been pretty successful at it."

He offers a diplomatic solution: "Rene [Rivera] is an enthusiast... I think that he should think of that or manage that not as a boost thing, but as a separate project, which is promoted independently as a competitor to CMake or something like that. And then Boost would be an example of its use."

**Key Insight**: Tool loyalties within communities create entrenchment that prevents practical evolution.

**Category**: Process / Technical Infrastructure

---

### EXPERIENCE-RR-09: "Delusional" but "More Power to You"

**Experience Type**: Leadership Critique

**Narrative**:
Ramey provides a characteristically blunt assessment of Vinnie Falco's leadership of the C++ Alliance:

> "Vinnie's vision is aspirational and I'm not really sure what it is. And then there's money being invested. I can't help but think that there's hope that at some point this generates some sort of return on investment. And I just don't see things coming together for that to happen."

When asked about his "delusional" characterization: "I'll stand by that... he did talk about once, he articulated a future for the vision of Boost, and I thought that it just wasn't in accordance with my reality. And so I used the word delusional and I never felt the word was ill chosen."

Yet simultaneously: "I didn't have any real objection to what I call a change in direction because I felt that we were rudderless... I wish him well. I disagree with him about a lot of stuff, but hey, it's a free country still... he can take a shot and he's doing it. And I say, more power to you."

**Key Insight**: Skepticism of vision need not preclude support for action; rudderless organizations need leadership even if the direction is disputed.

**Category**: Working Group Dynamics / Leadership

---

### EXPERIENCE-RR-10: The Whole Computer World Is Built on Stolen Code

**Experience Type**: Philosophical Reflection

**Narrative**:
Ramey offers a provocative perspective on intellectual property in software:

> "The whole computer world is built on stolen code. And just look up Steve Jobs, for example... He's quoted saying, 'Whenever possible, steal code.'... If somebody makes a serialization library, they're gonna look at the Boost serialization library and steal what they can from it, and then think they made it. And they will have, because where did I get it? I basically got it from looking at the Microsoft Foundation Classes."

He traces the evolution: "I started out in the era where all software development was proprietary... And then we moved to an area where a lot of stuff was open source... And of course now we're into AI generated code."

The Boost Software License represents a philosophical choice: "Hey, we're changing the world here. Here it is. It's Michelangelo. You're free to photograph."

**Key Insight**: Open source is not altruism but recognition of how software actually evolves—through absorption, adaptation, and iteration.

**Category**: Historical Knowledge / Ecosystem Context

---

## Evaluation Checklists

### Checklist: Proposal Revision Strategy
Based on PRINCIPLE-RR-02 and EXPERIENCE-RR-01

- [ ] Have all criticisms from previous reviews been explicitly enumerated?
- [ ] Does the revision document how each criticism was addressed?
- [ ] Were criticisms that weren't addressed explicitly explained?
- [ ] Has the author demonstrated genuine engagement (not just rebuttals)?
- [ ] Would a reviewer from the previous round say their concerns were heard?

### Checklist: Library Design Balance
Based on PRINCIPLE-RR-05 and PRINCIPLE-RR-06

- [ ] Does the proposal address both abstract interface design AND practical implementation?
- [ ] Is the abstraction level appropriate for the problem domain?
- [ ] Would this be the "canonical solution" or just another option?
- [ ] Has the "nobody's come up with better since" test been considered?
- [ ] Are hardware/platform constraints adequately addressed?

### Checklist: Review Process Effectiveness
Based on PRINCIPLE-RR-03 and EXPERIENCE-RR-07

- [ ] Is there a defined, time-bounded review period?
- [ ] Are reviewers expected to actually USE the proposal, not just read it?
- [ ] Is there a mechanism for pre-review feedback?
- [ ] Does the process surface documentation inadequacies?
- [ ] Can the process identify "lost causes" early?

### Checklist: Interpersonal Dynamics in Technical Debates
Based on PRINCIPLE-RR-01 and EXPERIENCE-RR-02

- [ ] Has escalation been avoided when consensus isn't reached?
- [ ] Have graceful concessions been attempted before persistent argumentation?
- [ ] Is there psychological space for opponents to reconsider?
- [ ] Has the "surprise me again" possibility been left open?
- [ ] Has mutual respect been maintained despite technical disagreement?

---

## Open Questions

### QUESTION-RR-01: Incubator Revival
Ramey's Boost Library Incubator addressed real process problems. Should a well-resourced version be created? What would it take to sustain it?

### QUESTION-RR-02: Networking Deadlock Resolution
The 20-year networking standardization stalemate demonstrates consensus as "brake on bad ideas" but also represents enormous opportunity cost. Is there a middle path?

### QUESTION-RR-03: AI-Generated Code and Standards
Ramey identifies Boost contributors as "dinosaurs" in an AI-generated future. How should WG21 adapt to a world where code is generated rather than authored?

### QUESTION-RR-04: Canonical Solutions vs. Framework Libraries
When should the standard provide "canonical solutions" (like shared_ptr) versus "framework libraries" (like executors)? What criteria distinguish them?

---

## Raw Transcript Reference

Key timestamps for referenced material:

- **01:04:56-01:05:30**: Boost formal review process as "work of genius"
- **01:07:30-01:10:30**: Raw pointer serialization debate and graceful concession
- **01:11:37-01:12:30**: Rejection, doubling down, and subsequent acceptance
- **01:17:00-01:18:30**: MPL as enabling technology ("outer space to stratosphere")
- **01:19:30-01:22:00**: Peter Dimov and shared_ptr's impact
- **01:23:47-01:28:30**: Dave Abrahams relationship evolution
- **01:34:30-01:36:00**: Boost post-C++11 identity crisis
- **01:43:20-01:44:10**: "Delusional" characterization of Vinnie's vision
- **01:46:00-01:49:00**: Networking standardization 20-year stalemate
- **01:55:30-01:58:00**: Boost contributors as "dinosaurs"
- **02:00:30-02:01:00**: Individual genius and zip format anonymous contributor
- **02:04:30-02:05:30**: Boost Software License as "Michelangelo, free to photograph"
