# Nat Goodspeed: Captured Knowledge

**Interview Date**: 2025-10-27
**Interviewer**: Ray Nowosielski
**Location**: Rochester, NH
**Duration**: ~85 minutes
**Topics Covered**: Fiber proposal 12-year odyssey, Boost.Context/Boost.Fiber, Oliver Kowalke, Microsoft opposition, WG21 process critique, Christopher Kohlhoff/Asio, senders/receivers complexity, Second Life viewer development, async event handling, generic programming

## Executive Summary

Nat Goodspeed provides the most detailed insider account of a WG21 proposal's journey, chronicling the 12-year (and counting) effort to standardize fiber technology—from its 2013 introduction through ping-ponging between study groups, design committees, and core working groups, facing determined opposition from Microsoft while narrowly missing the C++26 deadline. His narrative reads like a procedural thriller, complete with corporate antagonists, anonymous informants revealing implementation secrets, and a protagonist's unwavering belief in his cause.

The fiber proposal's history reveals structural problems in WG21: proposals requiring both library and core wording must traverse dual tracks (LEWG→LWG and EWG→CWG), creating multiplicative delays; the three-year release cycle leaves proposals stranded when time runs out; and determined opposition from well-resourced companies can delay but not kill technically sound proposals. Goodspeed's observation that "WG21 makes the Catholic Church look impulsive" captures decades of frustration.

Most striking is Goodspeed's account of Microsoft's campaign against fiber technology, including "papers bashing fiber technology" and strategic delays (taking months to answer implementability questions that could have been resolved in weeks). His candid assessment that coawait coroutines have specific weaknesses (viral markup, allocation per invocation) versus fibers' strengths (separate stack, no per-call allocation) provides technical grounding for the political conflict.

The interview also captures Goodspeed's deep appreciation for C++'s evolution from his 1989 C programming epiphany about reference counting to his discovery of Boost libraries at Linden Lab, providing a human context for why standardization matters to practitioners.

---

## Principles

### P-NG-001: Standardize What Cannot Be Written in Portable C++

**Statement**: Features requiring platform-specific assembly code (like stack switching) have the strongest case for standardization because vendors are already targeting those platforms.

**Category**: Standardization Criteria / Technical Justification

**Source Type**: Explicit

**Supporting Quote**:
> "The important thing to know about boost context is that it introduces functionality that you cannot write in portable C++. It uses assembly operations... assembly code is necessarily specific to a particular target machine... Whereas if it became part of the standard, then any vendor claiming to support C++ would have this feature as part of their standard library. They are already writing a compiler that targets a specific machine and a specific operating system."

**Context**: Boost.Context requires separate assembly implementations for each platform/OS combination. Standardization transfers that burden to compiler vendors who already have platform-specific expertise.

**Actionable Guidance**:
- Prioritize standardization for features impossible in portable C++
- Leverage existing vendor expertise in platform-specific code
- Recognize the scalability problem of maintaining assembly for many platforms
- Treat "requires assembly" as strong standardization justification

---

### P-NG-002: Proposals Require Determined Champions

**Statement**: Getting a library into the standard requires a specifically determined person willing to persist through years of iteration; WG21 does not proactively seek out the best libraries.

**Category**: Standardization Process / Human Dynamics

**Source Type**: Explicit

**Supporting Quote**:
> "Getting any library into the standard takes a champion... it takes someone specifically determined to bring that library into the standard and it takes a fair amount of persistence. It usually doesn't take 12 years, but it does take persistence... It isn't WG21 reaching out to pluck the best available libraries from the universe of C++ libraries. It is interested parties coming forward with a library that they think should be part of the standard... and persisting until it gets in."

**Context**: Goodspeed's 12-year fiber odyssey demonstrates the extreme case, but all proposals require sustained effort from advocates who believe in them.

**Actionable Guidance**:
- Identify a committed long-term champion before starting standardization
- Budget years, not months, for the standardization process
- Recognize that giving up is the most common failure mode
- Understand WG21 is reactive, not proactive, in selecting features

---

### P-NG-003: Dual-Track Proposals Face Multiplicative Delays

**Statement**: Proposals touching both core language and library wording must traverse two approval tracks, creating compounding delays and opportunities for procedural stalls.

**Category**: WG21 Governance / Process Structure

**Source Type**: Explicit

**Supporting Quote**:
> "To our dismay, the committee concluded that our proposal touches both the library and the core wording and that it therefore needs to go through both tracks before being admitted to plenary. So the pinball bumpers were SG1 for a long time, and then LEWG, EWG, and then get to LWG and CWG."

**Context**: The fiber proposal bounced between study groups and working groups for over a decade, with each group able to send it back to another for design changes.

**Actionable Guidance**:
- Clearly categorize proposals as library-only or core-only when possible
- If dual-track, plan for significantly longer timelines
- Secure parallel progress in both tracks when feasible
- Document track assignment rationale to avoid mid-process reclassification

---

### P-NG-004: Competing Corporate Interests Create Procedural Opposition

**Statement**: When a proposal competes with a vendor's existing investment, that vendor may use procedural tactics (delay, documentation requests, negative papers) rather than direct rejection.

**Category**: WG21 Governance / Politics

**Source Type**: Explicit

**Supporting Quote**:
> "Microsoft perceived the fiber proposal as a threat, a competitor, and Microsoft, in addition to spending time and energy in effect marketing coawait coroutines, posted a number of papers bashing fiber technology... That was around the time that Microsoft began proposing coawait coroutines."

**Context**: Microsoft championed co_await coroutines while opposing fibers. When asked about implementability, "the answer came back late in the week of the winter 2025 meeting"—months after the question was posed, conveniently leaving no time for review.

**Actionable Guidance**:
- Identify potential corporate competitors early
- Build coalitions beyond a single company's sphere of influence
- Document delays and their impact on the standardization timeline
- Prepare technically rigorous responses to criticism papers
- Seek implementation experience from multiple vendors

---

### P-NG-005: Coawait vs Fibers: Fundamental Architectural Differences

**Statement**: Stackless coroutines (co_await) and stackful fibers have incompatible architectures—"suspend by return" vs "suspend by call"—and suit different use cases despite superficial similarity.

**Category**: Technical Architecture / Design Philosophy

**Source Type**: Explicit

**Supporting Quote**:
> "Despite a similarity of use cases, these technologies are incompatible at a very fundamental level. Fiber technology can be characterized as suspend by call, where coawait technology can be characterized as suspend by return. Very different things happen under the hood."

**Context**: WG21 asked the fiber and coawait teams to unify their proposals, but they produced a paper explaining fundamental incompatibility instead.

**Actionable Guidance**:
- Evaluate coroutine vs fiber based on specific use case requirements
- Fibers excel for layered abstractions with async at the bottom
- Coawait excels for shallow call chains visible to the compiler
- Don't assume similar syntax means similar implementation characteristics

---

### P-NG-006: Viral Markup Is a Design Tax

**Statement**: When every caller of an async function must also be marked async (as with co_await), the markup "pervades your code base" and creates a design tax on abstraction.

**Category**: Technical Architecture / API Design

**Source Type**: Explicit

**Supporting Quote**:
> "Every caller of a coawait coroutine must itself be a coawait coroutine. Every one of their callers must be a coawait coroutine up to the topmost level where you launch and manage such things. And so the markup is viral. It pervades your code base."

**Context**: Second Life viewer's use case—layered abstractions with async I/O at the bottom—would require async markers throughout the call stack with co_await, but fibers allow sync-appearing code.

**Actionable Guidance**:
- Consider markup virality when choosing async models
- Fibers hide async nature from intermediate callers
- Coawait requires explicit async at every level
- Viral markup inhibits refactoring and abstraction

---

### P-NG-007: Per-Invocation Allocation Has Costs

**Statement**: Every coawait coroutine invocation requires a heap allocation; fibers amortize allocation by maintaining a persistent stack.

**Category**: Technical Architecture / Performance

**Source Type**: Explicit

**Supporting Quote**:
> "Every invocation of a coawait coroutine requires a new allocation. And every final return from a coawait coroutine requires a free... There are suggestions that you could maybe reduce the memory thrashing by having a pool of coroutine activation frames. And our answer to that was, yes, the term for a pool of activation frames is a stack, and what you get with fibers is a whole separate stack that doesn't need allocating and deallocating on every call."

**Context**: The fiber proposal's technical argument centers on avoiding per-call allocation overhead in high-frequency async scenarios.

**Actionable Guidance**:
- Profile allocation costs in async-heavy code paths
- Fiber technology amortizes allocation via persistent stacks
- Coawait allocation pools recreate stack semantics
- Choose based on actual invocation patterns

---

### P-NG-008: Priority Starvation Should Be Addressed

**Statement**: Long-pending proposals should receive priority bumps, similar to operating system schedulers preventing task starvation.

**Category**: WG21 Governance / Process Reform

**Source Type**: Explicit

**Supporting Quote**:
> "In a good scheduler for operating system threads or for tasks in general, if some particular task has been ready but has been starved for cycles for a long enough time, its priority gets bumped up so that it will catch some cycles in the near future. I think the committee could borrow a lesson from that kind of implementation."

**Context**: The fiber proposal, ready for final approval, couldn't get "a few minutes of committee time" from LWG and CWG because national body comments had priority.

**Actionable Guidance**:
- Track proposal age as factor in scheduling
- Implement aging priority for long-pending proposals
- Reserve time slots for near-complete proposals
- Prevent perpetual deferral of mature work

---

### P-NG-009: Study Groups Were Created to Streamline, Added Hurdles

**Statement**: Incubator study groups were introduced to filter immature proposals, but they added procedural layers rather than reducing time to standardization.

**Category**: WG21 Governance / Unintended Consequences

**Source Type**: Explicit

**Supporting Quote**:
> "The incubator groups were introduced though because proposals were being introduced that were considered to be wasting the time of the design groups that were immature... It was an attempt by the committee to make better use of scarce committee attention for proposals that were ready. And the result is that you have more hurdles to jump through."

**Context**: The fiber proposal spent years in SG1 before even reaching LEWG and EWG.

**Actionable Guidance**:
- Evaluate whether study group time is productive or gatekeeping
- Monitor total time-to-standardization, not just working group time
- Recognize that "filtering" creates additional stages to pass
- Consider fast-tracking mature proposals from proven sources

---

### P-NG-010: Attending WG21 Requires Scurrying Between Rooms

**Statement**: With 20+ study groups meeting concurrently, interested parties must physically race between rooms and may miss discussions affecting their proposals.

**Category**: WG21 Governance / Participation Barriers

**Source Type**: Explicit

**Supporting Quote**:
> "There are some 20 plus study groups. There are six sort of main track groups. Not all of those groups meet all week at every meeting, but an interested party may find that they have to scurry around between different rooms to attend discussions of proposals that concern them. They may have a conflict."

**Context**: With over 200 attendees and simultaneous sessions, no individual can track all relevant discussions.

**Actionable Guidance**:
- Recruit allies to monitor parallel sessions
- Coordinate with co-authors on room coverage
- Request schedule coordination for related proposals
- Accept that perfect coverage is impossible

---

### P-NG-011: The Review Process Improves Proposals

**Statement**: Despite process frustrations, WG21 review genuinely improves proposal quality—designs that survive are stronger and safer than their original forms.

**Category**: Standardization Process / Value Proposition

**Source Type**: Explicit

**Supporting Quote**:
> "I believe that proposals targeting the standard go through a process of review, critique, improvement. I think that it is typically true that a proposal that arrives at WG21 that gets introduced into the standard is a stronger design, more robust, safer to use than the form in which it originally arrived."

**Context**: Despite 12 years of frustration, Goodspeed acknowledges the fiber proposal has been refined through the process.

**Actionable Guidance**:
- Expect and welcome substantive criticism
- Track how the design evolved through review
- Document lessons learned from committee feedback
- View iteration as value creation, not just delay

---

## Experiences

### E-NG-001: The 1989 Reference Counting Revelation

**Narrative**: In 1989, Nat Goodspeed completed a large C program with manual reference counting using macros. The compiler couldn't detect forgotten increments (dangling pointers) or decrements (memory leaks). When he read about C++ classes, he had a two-phase revelation: first, the compiler would detect reference counting errors; second, it would automate the counting entirely. This insight made him "strongly desire to start coding in C++" though it took another decade to land a C++ job.

**Key Quote**:
> "The compiler will do that automatically for me. And that was enough to make me strongly desire to start coding in C++. And unfortunately it was another 10 years before I landed in a job where C++ was the project language."

**Lesson**: C++'s value proposition to practitioners is error prevention through compiler enforcement, not just abstraction.

**Linked Principles**: P-NG-011 (Quality through review)

---

### E-NG-002: Second Life's 1800-Line Giant Switch Statement

**Narrative**: The Second Life viewer's login function was an 1800-line "giant switch statement"—code that any programmer recognizes as bad design but was necessitated by async event handling without proper coroutine support. Goodspeed's manager extracted portions into Boost.StateChart classes. Armed with coroutine technology from the Google Summer of Code library, Goodspeed reverse-engineered it as "a triply nested loop with an if statement in the middle wrapping an asynchronous operation."

**Key Quote**:
> "Armed with this coroutine technology, I took an embarrassingly long time to figure out what actually was going on in this flow of control between these different classes, and was able to reverse engineer it as a triply nested loop with an if statement in the middle."

**Lesson**: Appropriate language features dramatically reduce complexity; what took 1800 lines could be expressed clearly once coroutines were available.

**Linked Principles**: P-NG-006 (Viral markup), P-NG-007 (Per-invocation allocation)

---

### E-NG-003: The Deep Throat Implementation Secret

**Narrative**: When EWG demanded implementation experience, Goodspeed—not being a compiler implementer—"had to do some scurrying." An anonymous informant who "wasn't even one of the implementers" revealed that one standard library implementation exposed an internal entry point enabling exactly what was needed. This allowed Goodspeed to produce the required proof.

**Key Quote**:
> "Discussions with other interested parties pointed me in the direction of that entry point. And once I knew about it, I was able with that implementation of the standard library to write code that would have the required behavior."

**Lesson**: Informal networks and shared interest in a technology can overcome official barriers; implementation details matter for standardization.

**Linked Principles**: P-NG-002 (Champion persistence)

---

### E-NG-004: Microsoft's Strategic Delay

**Narrative**: When Goodspeed presented implementation experience to EWG in fall 2024, Microsoft responded that they needed to "consult with our backend people in Redmond" about implementability. The answer—that yes, it was implementable—"came back late in the week of the winter 2025 meeting," leaving no time for LWG or CWG review. The pattern of delay prevented fiber from making C++26.

**Key Quote**:
> "It would seem plausible that they might have been able to produce an answer to that question within the next few weeks, let's say, but in fact, the answer came back late in the week of the winter 2025 meeting."

**Lesson**: Procedural questions can be weaponized through delay; timing of responses can be as consequential as their content.

**Linked Principles**: P-NG-004 (Corporate opposition)

---

### E-NG-005: Oliver Kowalke's Emotional Withdrawal

**Narrative**: Oliver Kowalke, the actual creator of Boost.Context and the fiber proposal, eventually "threw up his hands" and told Goodspeed: "If you want to pursue this, go ahead. But I can't emotionally depend on this anymore." As Goodspeed became "the face of the fiber proposal" despite Oliver's technical primacy, he expressed hope that the documentary might "get Oliver's name attached to the fiber technology."

**Key Quote**:
> "I think that if this documentary does one bit of good, it might be to get Oliver's name attached to the fiber technology. He deserves way more credit than I think people in WG21 usually realize."

**Lesson**: Long standardization timelines exact emotional costs; original authors may withdraw while champions persist.

**Linked Principles**: P-NG-002 (Champion persistence)

---

### E-NG-006: Christopher Kohlhoff's Mistreatment

**Narrative**: Goodspeed views the Asio/networking saga as "many of us in WG21 feel [Christopher Kohlhoff] was very badly treated." Kohlhoff traveled from Australia repeatedly to advance networking, only to see the committee pivot to sender/receiver abstractions. Goodspeed attended a meeting where someone presented "Hello World in senders and receivers" over an hour with three pages of code, prompting one participant to call it "the most complicated way of doing Hello World that I could possibly ever have imagined."

**Key Quote**:
> "I think there was this collective turning away from Chris and Asio to this whole other set of ideas and the networking proposal just stalled and Chris went away. Kind of disgusted with the whole thing."

**Lesson**: Pivoting away from a mature proposal to pursue theoretical alternatives can alienate dedicated contributors while delivering nothing.

**Linked Principles**: P-NG-009 (Study groups as hurdles)

---

### E-NG-007: Boost Steering Committee Recognition

**Narrative**: Jeff Garland informed Goodspeed that the Boost Steering Committee "has been apprised of this 12 year odyssey and they think that it points up some problems with the committee process."

**Key Quote**:
> "They think that it points up some problems with the committee process. And I think that it's not only likely, but has happened that authors who bring a proposal and have to wait this long, give up and go away."

**Lesson**: Extreme cases can serve as evidence for process reform; external recognition may amplify internal concerns.

**Linked Principles**: P-NG-008 (Priority starvation)

---

## Evaluation Checklists

### For Proposals Requiring Platform-Specific Implementation

1. **Portability Analysis**
   - [ ] Can the feature be written in portable C++?
   - [ ] If not, what platform-specific code is required?
   - [ ] How many platform variants need separate implementation?
   - [ ] Do compiler vendors already have this platform expertise?

2. **Standardization Justification**
   - [ ] Does standardization eliminate duplication across vendors?
   - [ ] Is there existing practice (e.g., Boost implementation)?
   - [ ] Are there competing proprietary approaches?
   - [ ] What happens to users if standardization fails?

3. **Track Classification**
   - [ ] Is this purely library, purely core, or both?
   - [ ] Has track classification been confirmed with WG21?
   - [ ] If dual-track, are timelines doubled in planning?
   - [ ] Can the proposal be restructured to simplify tracking?

### For Long-Running Proposals

1. **Progress Monitoring**
   - [ ] How many meetings has the proposal attended?
   - [ ] Which groups have approved/rejected/requested changes?
   - [ ] What is the total calendar time since introduction?
   - [ ] Is there a pattern of repeated sends-back?

2. **Opposition Analysis**
   - [ ] Are there competing proposals from well-resourced organizations?
   - [ ] Have negative papers been published? What do they claim?
   - [ ] Are procedural objections serving substantive purposes?
   - [ ] What would satisfy the opposition?

3. **Champion Health**
   - [ ] Is the original author still engaged?
   - [ ] Has champion burnout occurred or threatened?
   - [ ] Are there backup champions if needed?
   - [ ] What institutional support exists?

---

## Open Questions

1. **Starvation Prevention**: Should WG21 implement formal priority aging for long-pending proposals, and what would the threshold be (e.g., 5 years ready-but-unscheduled)?

2. **Corporate Conflict of Interest**: When a company has a competing proposal, should they be required to disclose this when raising objections or requesting delays?

3. **Dual-Track Reform**: Could proposals be allowed to progress through library and core tracks in parallel rather than sequentially?

4. **Remote Participation Equity**: How can WG21 better serve contributors who cannot attend multiple meetings per year due to geography?

5. **Champion Succession**: Should there be formal mechanisms for transferring proposal championship when original authors withdraw?

---

## Raw Transcript Reference

**Source**: Documentary interview footage
**Date**: October 27, 2025
**Location**: Rochester, New Hampshire
**Format**: Video interview with audio transcription

The transcript covers:
- Personal background and entry to programming (0:00-15:00)
- Linden Lab/Second Life context (15:00-33:00)
- Discovery of coroutine need and Boost libraries (33:00-48:00)
- Introduction of fiber proposal to WG21 (48:00-60:00)
- Microsoft opposition and coawait competition (54:00-70:00)
- 12-year odyssey through committee process (60:00-80:00)
- Christopher Kohlhoff/Asio reflection (80:00-85:00)
