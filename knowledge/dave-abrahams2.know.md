# Dave Abrahams & Doug Gregor: Captured Knowledge (Dinner Reunion)

**Interview Date**: 2025-12-10
**Location**: San Jose, CA
**Participants**: Dave Abrahams, Doug Gregor, LuAnne Abrahams, Amy Gregor
**Duration**: ~1hr 25min
**Topics Covered**: Boost origins and growth, C++ committee dynamics, concepts proposal and failure, Bjarne Stroustrup politics, transition to Swift, field experience requirements, community-driven design

## Executive Summary

This dinner conversation between two central figures in C++ and Swift history provides extraordinary insight into how Boost transformed C++ library development, why the original concepts proposal failed after years of work, and what lessons were carried forward to Swift.

The core insight is that **committee processes cannot invent—they can only standardize existing practice**. Boost succeeded because it created a rapid feedback loop outside the committee: build something, let people use it, iterate based on real feedback, then propose for standardization once patterns were proven. The concepts debacle illustrates what happens when this is violated: years of work can be undone by a single person's change of heart when there's no field-proven consensus to anchor the design.

Perhaps most striking is the candid discussion of how Bjarne Stroustrup's last-minute withdrawal of support killed the concepts proposal, and how this experience drove both Dave and Doug away from C++ language work and toward Swift, where they deliberately built in instability periods to allow experimentation before committing to stability.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Standards Committees Must Standardize Existing Practice, Not Invent

> *"Standards committees should not invent per se, they should take what is known to work well and enshrine it so everyone can build on it."*

**The Principle**: A standards body should only standardize designs that have been proven through extensive real-world use; invention and experimentation must happen outside the standardization process.

**Why It Matters**: When committees try to invent, they lack the feedback loop that validates designs. The concepts failure demonstrates this—despite brilliant people working for years, the design was rejected because it hadn't been battle-tested with real users. In contrast, Boost libraries that went through extensive field use before standardization (like function, tuple, smart pointers) succeeded.

**When to Apply**: 
- Evaluating any proposal for language or library standardization
- Deciding whether a feature is "ready" for standardization
- Assessing whether field experience claims are sufficient

**Red Flags**:
- "We'll figure out the edge cases after standardization"
- Proposal authors haven't shipped to external users
- Design is still actively changing during standardization process
- Implementation was created specifically for the proposal vote

**Supporting Experiences**: E1, E2, E5

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: belongs/library, belongs/language
applies-to: both
confidence: high
supported-by: [E1, E2, E5]
related-principles: [P2, P3]
-->

---

### P2: Implementation Proves Implementability—Field Experience Proves Usability

> *"The Boost ethos, I would say, is very much build it. And hand it out for people to try it and give you feedback. 'Cause that's the only way we knew how to make things better."*

**The Principle**: Having an implementation proves something *can* work; having extensive field experience from independent users proves it *does* work in practice. Both are necessary, but field experience is the harder and more important bar.

**Why It Matters**: Doug's concepts implementation in GCC proved the design was implementable, which was crucial for committee credibility. But the proposal still failed because there wasn't broad real-world validation. Implementation is necessary but not sufficient.

**When to Apply**:
- Evaluating claims of "implementation experience"
- Distinguishing between prototype implementations and production-ready ones
- Assessing whether a design has been validated by real use

**Red Flags**:
- Implementation created in the months before a vote
- "Implementation" is really a prototype/hack
- No users outside the proposer's organization
- Users are limited to the implementation authors

**Supporting Experiences**: E1, E4

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E1, E4]
related-principles: [P1, P3]
-->

---

### P3: Design Feedback Loops Require Real Users, Not Committee Review

> *"You have to get that feedback. 'Cause without that feedback loop, you can design yourself into something that doesn't make sense. Either it doesn't make sense for the user you better to build it for, or you can't actually do that."*

**The Principle**: Meaningful design feedback comes from people actually using your code in their own projects, not from committee members reviewing proposals in 15-minute slots. The feedback loop must include implementation, deployment, user iteration, and refinement.

**Why It Matters**: Committee meetings allocate limited time per proposal, and reviewers cannot deeply evaluate designs without using them. Boost succeeded because it created rapid iteration cycles outside the committee. The concepts proposal, despite extensive committee review, failed because it lacked this real-world feedback loop.

**When to Apply**:
- Designing the process for developing new features
- Evaluating whether a proposal has had adequate review
- Deciding when something is ready for standardization

**Red Flags**:
- Feedback limited to mailing list discussion
- No evidence of iteration based on user experience
- Design changes happening in response to committee comments rather than usage
- Proposers defensive about suggested changes

**Supporting Experiences**: E1, E2, E5

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E1, E2, E5]
related-principles: [P1, P2]
-->

---

### P4: One Person Can Derail Years of Collaborative Work

> *"I knew how much effort it took to get there. And I knew it could disappear on the whim of one person. One bad email chain. And it's hard to personally invest in something that can go away like that."*

**The Principle**: In committee processes, even after years of collaborative work and formal approval, a single influential person withdrawing support can kill a proposal. This risk makes it difficult to sustain the massive personal investment required for significant language changes.

**Why It Matters**: The concepts proposal was formally accepted and merged into the draft standard. Then Bjarne sent an email withdrawing his support, and years of work were undone. This experience drove both Dave and Doug away from C++ language work. Understanding this dynamic is essential for anyone considering major standardization efforts.

**When to Apply**:
- Assessing political risk for major proposals
- Deciding whether to invest in large standardization efforts
- Building coalitions for controversial features

**Red Flags**:
- Key stakeholders expressing private reservations while publicly supporting
- Proposal depends on continued support from a single influential person
- Co-authors with fundamentally different visions "agreeing to disagree"
- Last-minute concerns from people who had been silent

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P5, P8]
-->

---

### P5: Simplicity Is Essential for Committee Acceptance

> *"Jeremy correctly read the room as going sort of against Yako's proposal and said, don't worry everyone, it's okay. It's just a typo. He actually meant to write it like this and wrote down something that was very boring and simple."*

**The Principle**: When presenting to a committee, complex or unfamiliar techniques will cause resistance, even if they're sound. Reframing proposals in simple, familiar terms—even if the underlying complexity remains—is often necessary for acceptance.

**Why It Matters**: Jaakko's tuple proposal was technically correct but relied on template metaprogramming that made committee members nervous. Jeremy's intervention—reframing a scary-looking interface as something "boring and simple"—saved the proposal. This pattern applies broadly: the committee's risk aversion means you must make the unfamiliar feel familiar.

**When to Apply**:
- Presenting proposals that use advanced techniques
- Responding to committee resistance
- Designing how to expose functionality to reviewers

**Red Flags**:
- Committee members' eyes glazing over during presentation
- Questions focused on implementation complexity rather than interface
- Resistance framed as "we don't understand this" rather than technical objections
- Proposal relies on techniques unfamiliar to most committee members

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P5
source-type: tacit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P3, P8]
-->

---

### P6: Backward Compatibility Is a Sacred Constraint in C++

> *"One of the big things about C++ is backward compatibility. Existing code needs to work even if you change the language."*

**The Principle**: Any C++ proposal must preserve backward compatibility with existing code. This is not negotiable—breaking existing code is almost never acceptable, even for significant improvements.

**Why It Matters**: The concepts team spent enormous effort making their design "mostly backward compatible." This constraint shapes what's possible in C++ evolution and must be considered from the start of any design. Features that would require breaking changes are effectively impossible.

**When to Apply**:
- Designing any language or library feature
- Evaluating proposals for compatibility impact
- Choosing between design alternatives

**Red Flags**:
- Proposal changes meaning of existing valid code
- "Migration path" requires code changes for existing users
- Feature interactions could change behavior of existing templates
- Deprecation without a backwards-compatible alternative

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P1]
-->

---

### P7: Community Collaboration Beats Solo Design

> *"I think we did an amazing job on it though. I mean, we found ways to take the system that we built that we thought would work pretty well and actually make it work on existing code... [because] a whole bunch of smart people are helping you make your ideas work better."*

**The Principle**: Software design, especially for standards, benefits enormously from collaborative community effort. Individual brilliance is insufficient; you need diverse perspectives finding weaknesses and suggesting improvements.

**Why It Matters**: Boost's success came from its community culture—people freely contributed improvements to each other's work. Doug describes the excitement of someone finding a new technique and everyone rebuilding their libraries to use it. This collaborative dynamic produced designs that no individual could have achieved.

**When to Apply**:
- Setting up processes for developing new features
- Evaluating whether a design has had adequate review
- Deciding whether to work alone or seek collaboration

**Red Flags**:
- Single-author proposals with no evidence of community input
- Defensive responses to suggested improvements
- Design produced in isolation then "announced"
- Proposer unwilling to incorporate feedback

**Supporting Experiences**: E1, E5

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E1, E5]
related-principles: [P3]
-->

---

### P8: Political Sensitivity Is Required for Technical Success

> *"We ended up having a huddle with Andrew to try and figure out how to deal with this very, very serious political problem. Because Bjarne is the leader of C++... I thought we hadn't done anything disrespectful. But I sort of came up with the idea, you know, maybe we could apologize anyway."*

**The Principle**: Technical excellence alone is insufficient for standardization success. Major proposals require political navigation—understanding stakeholder concerns, managing egos, and sometimes apologizing even when you've done nothing wrong.

**Why It Matters**: The Indiana team's concepts implementation was technically superior, but its presentation made Bjarne feel disrespected. Success required years of subsequent political work: Doug traveling to Texas A&M repeatedly, careful negotiation, and diplomatic handling of disagreements. The ultimate failure came from a political failure, not a technical one.

**When to Apply**:
- Presenting competing proposals
- Working with influential committee members
- Responding to resistance from key stakeholders
- Navigating disagreements about design direction

**Red Flags**:
- Presenting a competing proposal without acknowledging prior work
- Making someone feel their ideas were dismissed
- Demonstrating technical superiority in a way that embarrasses others
- Assuming technical correctness will win arguments

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P8
source-type: tacit
category: process/politics
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P4, P5]
-->

---

### P9: Deliberate Instability Periods Enable Better Designs

> *"One of the great things, Chris was brilliant in setting the direction for Swift to be unstable for a few years. So that we could discover what was working and what wasn't."*

**The Principle**: New languages or major features benefit from an explicit instability period where breaking changes are expected. This allows real-world learning before committing to permanent decisions.

**Why It Matters**: Swift's deliberate instability period allowed the team to iterate based on real usage before committing to ABI stability. This is the opposite of the C++ approach where features are locked in immediately upon standardization. The concepts failure might have been avoided if there had been a way to try the design at scale before committing.

**When to Apply**:
- Designing new languages or major subsystems
- Setting expectations for early adopters
- Deciding when to commit to stability guarantees

**Red Flags**:
- Pressure to stabilize before adequate field experience
- Users expecting stability from experimental features
- No clear plan for when stability will be guaranteed
- Treating "shipped" as equivalent to "stable"

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: philosophy/evolution
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P1, P3]
-->

---

### P10: Proving Grounds Are Essential for Language Evolution

> *"Boost served as an experimental sandbox... proving concepts before standardization... it was a way to go and prove a concept."*

**The Principle**: Languages need external proving grounds where ideas can be tested extensively before standardization. These proving grounds must be disconnected from the standards process to allow rapid iteration.

**Why It Matters**: Boost provided C++ with a proving ground that the committee structure couldn't offer. Ideas could be tried, found wanting, revised, and tried again—all before anyone proposed them for standardization. Doug notes that C++ now lacks this: "They're missing the experimentation to build up what is the best practice before we get into the language."

**When to Apply**:
- Evaluating whether a feature is ready for standardization
- Setting up processes for language evolution
- Deciding where experimentation should happen

**Red Flags**:
- Proposals going directly to committee without external proving
- No ecosystem of experimental implementations
- Committee itself trying to do design iteration
- Pressure to standardize before patterns are proven

**Supporting Experiences**: E1, E5

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E1, E5]
related-principles: [P1, P3, P9]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Boost's Feedback-Driven Success

**Context**: Late 1990s to early 2000s. Boost was founded by Beman Dawes and others as an external project to incubate libraries that might eventually become part of the C++ standard.

**What Happened**: Boost established a culture of collaborative development unlike anything in the C++ world. Developers would propose libraries, receive extensive peer feedback, iterate based on real-world usage, and refine designs over time. Doug describes finding the Boost community: "Here's an online community that gets generic programming. These are my people." The process involved submitting work, getting "good suggestions on how to make it improve it. And like, that's the fun part, when a whole bunch of smart people are helping you make your ideas work better." Every few months, someone would discover a new technique, and everyone would rebuild their libraries to use it.

**The Outcome**: Success. Multiple Boost libraries were standardized in C++11 (shared_ptr, function, tuple, regex, etc.). The Boost Software License became ubiquitous—Dave started noticing it "showing up in startup screens everywhere." Doug notes that Boost is now "in the base system of every operating system out there."

**The Lesson**: A community focused on collaborative improvement, with rapid feedback cycles and willingness to iterate, produces designs that standards committees can confidently adopt because they've been proven in real-world use.

> *"What is the secret sauce? I think a lot of it comes down to people, very smart people collaborating. And it was a fun time for C++ the language because we were discovering ways to use it that hadn't been intended and hadn't been known before."*

**Supports Principles**: P1, P2, P3, P7, P10

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [boost, shared_ptr, function, tuple, type_traits]
supports: [P1, P2, P3, P7, P10]
-->

---

### E2: The Concepts Proposal Journey and Collapse

**Context**: 2005-2009. Multiple groups wanted to add "concepts" to C++ to better support generic programming. Bjarne Stroustrup and Gabriel Dos Reis at Texas had one vision; Doug Gregor and the Indiana University team (including Jeremy Siek, Jaakko Järvi, and others) had a different, more theoretically grounded approach.

**What Happened**: At Lillehammer (2005), Bjarne presented his concepts proposal. Dave and others felt it lacked theoretical rigor: "That whole proposal seemed to start with... let's figure out the most sugary and palatable way to express these ideas. And to a lot of us it seemed like the fundamentals aren't there."

The Indiana team developed a competing proposal and Doug implemented it in GCC in six months. At Mont-Tremblant (2006), Doug gave a live coding demo that "just opened their eyes to, wow, this could be something better." But this made Bjarne "extremely upset"—he felt disrespected.

The teams negotiated. Doug traveled to Texas A&M repeatedly over years to merge the proposals. "I traveled to Texas A&M many times over the next couple of years, sat in Bjarne's office with him and just talked through the design, trying to hear his concerns about it, make sure that his ideas got incorporated in a way that I didn't feel compromised the fundamental model."

By 2008, the merged proposal was accepted and merged into the draft standard—hundreds of pages across a dozen proposals touching much of the standard library.

Then, about a week before the Frankfurt meeting (2009), Bjarne sent an email withdrawing his support unless incompatible changes were made. Doug: "I remember giving a half-hearted attempt to describe why the change he wanted was unsuitable. But there was no saving it at that point."

**The Outcome**: Failure. Years of work undone. Pete Becker (editor) had to unmerge all the changes. Related features like range-based for had to be redesigned without concepts. Dave: "This was a heartbreaking thing for me. I think it was for Doug too."

**The Lesson**: Even formal committee approval cannot protect against political collapse. A single influential person's change of heart can invalidate years of collaborative work. Technical excellence and political consensus must both be maintained.

> *"I knew how much effort it took to get there. And I knew it could disappear on the whim of one person. One bad email chain. And it's hard to personally invest in something that can go away like that."*

**Supports Principles**: P1, P2, P3, P4, P6, P8

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [concepts]
supports: [P1, P2, P3, P4, P6, P8]
-->

---

### E3: The Apology That Wasn't Owed

**Context**: Mont-Tremblant meeting, 2006. Doug had just given his concepts live demo, which was extremely well-received by the committee but had made Bjarne upset.

**What Happened**: After Doug's successful demo, Bjarne was visibly upset—he felt his own proposal had been disrespected. The Indiana team (Doug, Dave, and others) had a huddle with Andrew Lumsdaine to figure out how to handle "this very serious political problem."

Dave describes the decision: "I thought we hadn't done anything disrespectful. But I sort of came up with the idea, you know, maybe we could apologize anyway. And whether he deserves an apology or not, let's think about apologizing and try to make this better. And we did. And things were patched up."

**The Outcome**: Mixed. The apology repaired the relationship enough to enable years of collaboration on a merged proposal. But the underlying tension was never fully resolved, and it resurfaced at Frankfurt when Bjarne withdrew support.

**The Lesson**: Sometimes you must apologize even when you've done nothing wrong, because the relationship is more important than being right. But an apology doesn't resolve fundamental disagreements—it only buys time.

> *"Bjarne is the leader of C++... maybe we could apologize anyway. Whether he deserves an apology or not, let's think about apologizing and try to make this better."*

**Supports Principles**: P4, P8

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: process/politics
applies-to: language
outcome: mixed
features: [concepts]
supports: [P4, P8]
-->

---

### E4: Clang Compiles Boost in 18 Months

**Context**: Late 2000s. After the concepts failure, Doug shifted focus to building Clang's C++ frontend.

**What Happened**: Doug and the Clang team took Clang "from, it doesn't do any C++ to it compiles Boost in 18 months." Compiling Boost was deliberately chosen as the benchmark because "that was the gold standard benchmark" for C++ compiler correctness—Boost used every weird template trick in the language.

Doug describes the pride of announcing this milestone: "I was very excited to get up on stage and say, this compiles Boost. It is real now. Because that was, and in many ways still is, the benchmark for [compiler correctness]."

**The Outcome**: Success. Clang became a production-quality C++ compiler that Dave describes as having impact "easily as big as Boost itself." The Boost compilation benchmark became a standard test for C++ implementations.

**The Lesson**: The best test for implementation correctness is compiling code that pushes the language to its limits. Boost's extensive use of advanced techniques made it the perfect benchmark—if your compiler could handle Boost, it could handle anything.

> *"Boost, like, stretches the language. All those weird tricks that came from the weird machine. Boost uses every single one of them and only a faithful implementation of the standard would build it."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [clang, boost]
supports: [P2]
-->

---

### E5: From C++ to Swift—Carrying Lessons Forward

**Context**: Early 2010s. After the concepts failure, both Dave and Doug eventually left C++ committee work. Doug built Clang at Apple; Dave joined later to work on Swift.

**What Happened**: The concepts experience taught both of them that investing in major C++ language changes was too risky. Doug: "I no longer felt like it was possible to make big improvements to C++ because the bar for change is so high... and I knew it could disappear on the whim of one person."

They brought lessons to Swift:
1. **Deliberate instability**: "Chris was brilliant in setting the direction for Swift to be unstable for a few years. So that we could discover what was working and what wasn't."
2. **Boost-style review process**: When Dave was asked about Swift's process, "I was like, Boost did it. Let's just do it again. The process is almost exactly the same."
3. **Concepts done right**: "A lot [of what we learned] ended up in Swift."

Doug notes that C++ now lacks what Boost provided: "With Boost not being the driving entity for the C++ standard, now they're missing that. They're missing the experimentation to build up what is the best practice before we get into the language."

**The Outcome**: Success (for Swift). The lessons from Boost and the concepts failure informed Swift's design process, allowing it to iterate successfully during its instability period.

**The Lesson**: Failure can be valuable if you learn from it. The concepts experience, while heartbreaking, provided crucial insights about language evolution that made Swift's process more successful.

> *"We learned a lot. Go build the next thing."*

**Supports Principles**: P1, P3, P9, P10

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [swift, concepts]
supports: [P1, P3, P9, P10]
-->

---

### E6: "It's Just a Typo"—Jeremy Saves Tuple

**Context**: Early 2000s, Santa Cruz committee meeting. The first Boost libraries (function, tuple) were being proposed for the Technical Report—a test of whether Boost could influence the standard.

**What Happened**: Jaakko Järvi's tuple proposal relied on template metaprogramming techniques that committee members found scary. "The way he had specified it sort of implied a whole lot of strange template meta programming tricks that us Boost people were totally comfortable with. And the rest of the committee being folks that had responsible for the implementations... were very nervous."

Jaakko tried to explain the metaprogramming, which made things worse: "Everyone's eyes glazed over."

Jeremy Siek "correctly read the room as going sort of against Yako's proposal" and intervened: "Don't worry everyone, it's okay. It's just a typo. He actually meant to write it like this." He wrote down something "very boring and simple" that expressed the same interface without the scary implementation details.

**The Outcome**: Success. The tuple proposal was accepted. "It got the conversation back." This success helped establish Boost's credibility with the committee.

**The Lesson**: Committee members will resist what they don't understand, even if it's technically sound. Presenting the same functionality in familiar terms can transform rejection into acceptance. Reading the room and adapting your presentation in real-time is crucial.

> *"It was something that turned this like very scary, very, you know, boost thing into something normal that everyone understood."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: process/navigation
applies-to: library
outcome: success
features: [tuple]
supports: [P5]
-->

---

### E7: Bjarne's Turing Award and Academic Hostility

**Context**: Ongoing. Dave sets context for understanding Bjarne's behavior during the concepts debate.

**What Happened**: Dave explains that Bjarne has faced hostility throughout his career: "One of the things that was pointed out to me not long ago is Bjarne doesn't have a Turing award... Nicholas Wirth has a Turing award for Pascal... people that have written influential languages have been awarded Turing awards. And it's ridiculous to think that C++ isn't as influential as any of those."

Additionally, "academia hates C++. They hate it with a passion." C++ is seen as "unclean and inelegant"—it "started with C and was grown organically" and there's "no underlying theory that you can base C++ on."

Dave concludes: "I think Bjarne for a lot of his career has felt like under assault from all sides. And not recognized for his contribution. And sometimes I think he doesn't realize who his allies are. And feels under assault from them too."

**The Outcome**: Context. This helps explain why Bjarne might have felt threatened by a competing concepts proposal from academics.

**The Lesson**: Understanding someone's broader context—the slights and disrespect they've experienced—is essential for navigating politically sensitive situations. What looks like overreaction may have deeper causes.

> *"Bjarne for a lot of his career has felt like under assault from all sides. And not recognized for his contribution. And sometimes I think he doesn't realize who his allies are."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E7
source-type: tacit
category: process/politics
applies-to: both
outcome: mixed
features: []
supports: [P8]
-->

---

### E8: Alex Stepanov's Legacy and Regrets

**Context**: Recent visit. Dave, Sean Parent, David Sankel, and Nick DeMarco visited Alex Stepanov (creator of the STL).

**What Happened**: For years, there was a "standing agreement: don't talk about programming" when visiting Alex, because "when he retired, he wanted to get out of it." But during walks with his Corgi, Alex would inevitably bring up "programming and his legacy."

Dave describes Alex's disappointment: "He feels like his experiment was a failure. His vision was large catalogs of reusable, well-documented generic components." Despite influencing so many people who've "made an impact on the industry," Alex feels the vision wasn't realized.

Dave notes the constraints: "I couldn't even begin to approach that with the Swift Standard Library... because it was too big. No, no, it was 'cause we couldn't ship that." (Binary size constraints prevented a large standard library.)

Surprisingly, when David Sankel asked if Alex would consider giving a talk again, "actually there's an opening." Dave found this "really surprising because Alex had been pretty adamant about being out of it."

**The Outcome**: Mixed. Alex's vision hasn't been fully realized, but he may be re-engaging with the community.

**The Lesson**: Even the most influential work can feel like failure to its creator if it didn't achieve their full vision. External success metrics (widespread use, industry impact) don't always align with the creator's internal goals.

> *"He's influenced so many of us that have made an impact on the industry, but he feels like his experiment was a failure."*

**Supports Principles**: P1, P7

<!-- METADATA
kind: experience
id: E8
source-type: tacit
category: history/regrets
applies-to: library
outcome: mixed
features: [stl, generic-programming]
supports: [P1, P7]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Any Major Proposal

- [ ] Has this design been proven through extensive real-world use, or is it being invented in committee?
- [ ] Is there an implementation that predates the proposal by significant time?
- [ ] Have independent users (outside the proposer's organization) used this and provided feedback?
- [ ] Has the design iterated based on that feedback?
- [ ] Is there a proving ground where this was tested before standardization?
- [ ] Does the proposal preserve backward compatibility with existing code?

**Questions to Ask**:
1. "What has been the field experience with this implementation?"
2. "How has the design changed based on user feedback?"
3. "Who outside your organization has used this, and what problems did they encounter?"
4. "What alternatives were tried and rejected based on real usage?"

<!-- METADATA
kind: checklist
category: evaluation/library, evaluation/language
applies-to: both
proposal-type: feature
derived-from: [P1, P2, P3, P6, P10]
-->

---

### When Navigating Committee Politics

- [ ] Have you identified all key stakeholders and their concerns?
- [ ] Are there influential people whose support is essential but fragile?
- [ ] Have you acknowledged prior work and avoided making others feel disrespected?
- [ ] If presenting a competing proposal, have you been diplomatic about differences?
- [ ] Is there tension being papered over that could resurface later?
- [ ] Have you built relationships before you need them?

**Questions to Ask**:
1. "Who might feel threatened by this proposal, and how can we address their concerns?"
2. "Are there unresolved disagreements among co-authors?"
3. "What's the worst-case political scenario, and how would we handle it?"
4. "Have we invested in relationships with key decision-makers?"

<!-- METADATA
kind: checklist
category: process/politics
applies-to: both
proposal-type: feature
derived-from: [P4, P5, P8]
-->

---

### When Presenting Complex Technical Content

- [ ] Can the proposal be explained in simple, familiar terms?
- [ ] Have you tested the explanation on people unfamiliar with the techniques?
- [ ] Are you prepared to simplify on the fly if eyes start glazing over?
- [ ] Is the interface simple even if the implementation is complex?
- [ ] Have you separated "what it does" from "how it's implemented"?

**Questions to Ask**:
1. "Can I explain this without referencing advanced techniques?"
2. "What's the simplest way to present this functionality?"
3. "What will committee members find scary, and how can I defuse that?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P5]
-->

---

### When Assessing Whether to Invest in Major Standardization Effort

- [ ] Is there an external proving ground where this can be developed outside committee?
- [ ] Can we afford an instability period before committing to the design?
- [ ] Are key stakeholders genuinely aligned, or just agreeing to disagree?
- [ ] What's the political risk, and can one person derail this?
- [ ] Is the personal investment worth the risk that it could be rejected?
- [ ] Do we have the community support to sustain multi-year effort?

**Questions to Ask**:
1. "If this takes 5 years and then fails, will it have been worth it anyway?"
2. "What would cause key supporters to withdraw support?"
3. "Where can we build real-world experience before standardization?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P4, P9, P10]
-->

---

## Open Questions

1. **What specific change did Bjarne request at Frankfurt?** Dave and Doug discuss Bjarne's withdrawal of support but don't detail exactly what change he demanded. Understanding this could illuminate what kinds of design disputes are irresolvable.

2. **Why did Boost stop being the driving force for C++ standardization?** Doug notes this absence but doesn't explain why. Was it the concepts failure? Changes in committee structure? The rise of other proposals sources?

3. **What libraries "failed us in the past" due to inadequate field experience?** Dave references Howard Hinnant's list of failures from the first interview but doesn't enumerate them here.

4. **What was the "is edible" / SFINAE technique?** Doug mentions Dave and Jeremy inventing this at ACCU in a hot tub, but the technical details aren't explained.

5. **How has the committee changed since 2009?** The committee has grown from ~50 to ~200 people. How has this affected the dynamics described here?

6. **What happened to the concepts that C++ eventually got?** C++20 includes concepts, but they're different from the original proposal. How do they compare?

---

## Raw Transcript Reference

Source: `inputs/dave-abrahams2.md`
Video: https://vimeo.com/1152624358/b5b24d2896?fl=tl&fe=ec
Filmed: 2025-12-10, San Jose CA
Type: Verite dinner conversation
