# Marshall Clow: Captured Knowledge

**Interview Date**: 2025-12-16
**Interviewer**: Ray Nowosielski
**Location**: Poway, CA
**Duration**: ~76 minutes
**Topics Covered**: Boost history, maintainership, generic programming, Alex Stepanov influence, WG21 experience, LWG chair (2015-2020), Herb Sutter's role, Networking TS/Asio controversy, Boost license, C++ Alliance, Boost's mission evolution, C++11's impact on Boost

## Executive Summary

Marshall Clow provides a uniquely comprehensive perspective spanning three distinct roles in the C++ ecosystem: Boost library author and maintainer, WG21 Library Working Group chair for five years, and early C++ Alliance employee. His narrative traces the arc from Boost's founding mission ("inventing existing practice for standardization") through its identity crisis after C++11 absorbed its most popular libraries, to its current evolution under C++ Alliance stewardship.

Most striking is Clow's account of how Alex Stepanov's 2003 keynote "The Greatest Common Measure: 2,500 Years" fundamentally redirected his career toward generic programming—a revelation that eventually led him to Boost, WG21, and the LWG chair. His observation that "generic programming lowers your cognitive load" captures the philosophical core that animated early Boost contributors.

Clow's perspective on the Networking TS debate is particularly valuable. As LWG chair during the critical 2017 timeframe, he witnessed Christopher Kohlhoff's discouragement firsthand and concludes: "C++ would have been better off adopting Asio because then we would have some networking built into the standard library, as opposed to nothing." His candid assessment that Boost "fell into doldrums" post-C++11 and his optimism about its current revival under Alliance support provides crucial context for understanding the ecosystem's evolution.

---

## Principles

### P-MC-001: Maintainership as Distinct Discipline

**Statement**: Maintaining a library is a distinct discipline from authoring it, requiring different skills focused on adaptation to evolving environments rather than original design.

**Category**: Library Development / Project Management

**Source Type**: Explicit

**Supporting Quote**:
> "A maintainer is someone who is responsible for a library... their job is to make sure that it continues to build. Even though environments change, new compilers are released, old compilers are retired. New operating systems, new versions of the C++ standard are released. Bugs are reported, that those bugs get fixed or get at least triaged."

**Context**: Clow distinguishes between the creative act of authoring and the sustaining act of maintenance, noting that these roles often separate as projects mature when original authors move on to new interests.

**Actionable Guidance**:
- Plan for maintainer succession from project inception
- Document not just code but evolution strategies
- Value maintenance skills equally with design skills
- Enable graceful handoffs when interests diverge

---

### P-MC-002: Generic Programming Reduces Cognitive Load

**Statement**: Generic programming's primary value is reducing cognitive load by eliminating the need to understand multiple similar-but-different implementations for different types.

**Category**: Design Philosophy / Technical Architecture

**Source Type**: Explicit

**Supporting Quote**:
> "One of the things that generic programming does is it lowers your cognitive load. You don't need to know that... this implementation of dynamic array of complex numbers has these special cases as opposed to this dynamic array of floating point numbers. You don't need to worry about that. You say it's a vector. Okay, I understand a vector."

**Context**: Clow traces this insight to Stepanov's influence, explaining how the STL transformed his understanding of programming by providing unified abstractions with documented requirements and performance guarantees.

**Actionable Guidance**:
- Design containers and algorithms generically by default
- Document requirements and performance guarantees
- Prefer unified interfaces over type-specific variants
- Measure cognitive impact when evaluating APIs

**Corroborating Sources**: Alex Stepanov's work, STL design principles

---

### P-MC-003: Standardize Existing Practice Through Incubation

**Statement**: Standardization should follow demonstrated existing practice, and organizations like Boost exist to "invent existing practice"—to create and mature implementations before proposing them for standards.

**Category**: Standardization Process / Ecosystem Role

**Source Type**: Explicit

**Supporting Quote**:
> "The impetus for Boost was... to invent existing practice to bring it into existence so that it could become existing practice so that it could be standardized."

**Context**: This was Boost's founding mission, distinct from merely providing useful libraries. The formal review process and implementation experience served the ultimate goal of feeding battle-tested components into the standard.

**Actionable Guidance**:
- Treat incubation as distinct from final standardization
- Require years of implementation and usage experience
- Use review processes to validate designs before proposing
- Recognize that "existing practice" must be created deliberately

**Corroborating Sources**: Beman Dawes's Boost founding documents, WG21 historical practice

---

### P-MC-004: Good Libraries Are Easy to Use Correctly, Hard to Use Wrong

**Statement**: Quality libraries are characterized by being easy to use, general, extensible, and hard to use incorrectly.

**Category**: Library Design / API Principles

**Source Type**: Explicit

**Supporting Quote**:
> "What makes a good library? Wow. It's easy to use. It's general and it's extensible and it's hard to use wrong... for the standard library, we lean really hard into generic, usable in many contexts."

**Context**: Clow references Liskov's open-closed principle as foundational, using `std::vector` as the exemplar of a good library: minimal knobs, understandable behavior, applicable to 90% of container needs.

**Actionable Guidance**:
- Optimize for the common case (vector handles 90%)
- Provide few but meaningful customization points
- Document behavior, not just interface
- Measure misuse patterns in real deployments

---

### P-MC-005: The Train Schedule Creates Artificial Urgency

**Statement**: The three-year release cycle creates artificial urgency that makes it difficult for the committee to say "not this time," leading to premature standardization.

**Category**: Standardization Process / Governance

**Source Type**: Explicit

**Supporting Quote**:
> "The hardest thing that the committee has to do is say, Nope, this is not going in this time. You know, that train is leaving the station and this is not ready."

**Context**: Clow notes that even with a longer cycle (e.g., five years), the committee would still face end-of-cycle pressure—the problem is structural, not durational.

**Actionable Guidance**:
- Build in explicit "not ready" checkpoints before final votes
- Decouple feature development timelines from release deadlines
- Resist "one more meeting" slippage that compounds into years
- Evaluate readiness independently of schedule pressure

**Corroborating Sources**: C++11's multi-year delay (07→08→09→10→11)

---

### P-MC-006: Adoption Beats Theoretical Purity

**Statement**: Standardizing a proven-but-imperfect design creates more value than holding out for an ideal design that may never materialize.

**Category**: Standardization Process / Pragmatism

**Source Type**: Explicit

**Supporting Quote**:
> "I'm kind of of the opinion that C++ would have been better off adopting Asio because then we would have some networking built into the standard library as opposed to nothing."

**Context**: On the Networking TS debate, Clow argues that rejecting Asio because "this is not how we do things now" led to a decade without standard networking, while theoretical alternatives failed to materialize.

**Actionable Guidance**:
- Weigh "something useful now" against "something perfect never"
- Track the cost of non-adoption (fragmentation, workarounds)
- Set time limits on "waiting for better approaches"
- Accept that any mature library will seem dated by standardization time

**Corroborating Sources**: Christopher Kohlhoff's Asio experience

---

### P-MC-007: Chair Succession Should Be Planned and Mentored

**Statement**: Five-year chair terms with overlap and mentorship ensure continuity while preventing burnout and enabling fresh perspectives.

**Category**: Governance / Leadership Development

**Source Type**: Explicit

**Supporting Quote**:
> "Herb chose Jonathan and the other two as assistant LWG chairs. The idea was to have assistants so that when Jonathan steps down... either Jeff or Dietmar will step up. And so they've been participating in the chairing for five years."

**Context**: When stepping down as LWG chair, Clow recommended three candidates (Jonathan Wakeley, Jeff Garland, Dietmar Kühl), and Herb Sutter chose one as successor with the other two as assistants, creating a leadership pipeline.

**Actionable Guidance**:
- Establish assistant/deputy positions for leadership roles
- Plan succession multiple years before transitions
- Enable candidates to participate in leadership before taking over
- Document chair responsibilities and institutional knowledge

---

### P-MC-008: Boost's Mission Evolved When Standards Absorbed Core Libraries

**Statement**: When C++11 absorbed Boost's most popular libraries (smart pointers, unordered containers, etc.), Boost's raison d'être shifted from "standards incubator" to "useful libraries repository."

**Category**: Ecosystem Evolution / Organizational Purpose

**Source Type**: Explicit

**Supporting Quote**:
> "A lot of the very mainstream value of Boost... were picked up and dropped in for C++11 and Boost became... much less of a 'well, duh, of course you need it.' Boost started doing a bunch of other things, which were good, which were interesting, which were inventive, but they weren't as widely applicable."

**Context**: Clow describes Boost falling into "doldrums" post-C++11 as its identity crisis played out—new libraries like Beast aren't destined for standardization but serve valuable purposes.

**Actionable Guidance**:
- Organizations must explicitly redefine mission after major milestones
- "Standards incubator" and "useful libraries" are different value propositions
- Communicate mission changes to community and contributors
- Measure success against current mission, not historical one

---

### P-MC-009: Licensing Clarity Enables Adoption

**Statement**: Clear, permissive licensing is essential for corporate adoption; organizations will not use unlicensed or ambiguously licensed code regardless of quality.

**Category**: Open Source Governance / Legal

**Source Type**: Explicit

**Supporting Quote**:
> "A lot of places, a lot of corporations, Qualcomm was one of them, would not use any open source if it didn't have some kind of license on it, stating what the responsibilities of the users are and what the rights of the authors are."

**Context**: Clow describes the Boost Software License's development as responding to corporate needs—shorter and more permissive than GPL, clearer than public domain, addressing patent concerns.

**Actionable Guidance**:
- Choose established licenses over custom or unlicensed distribution
- Address patent grants explicitly
- Keep license text short and understandable
- Consult legal expertise for license drafting

---

### P-MC-010: The Convener Sets Direction But Does Not Dictate

**Statement**: The WG21 convener (Herb Sutter) has significant administrative power—setting schedules, appointing chairs—but does not control technical decisions; proposals live or die by community consensus.

**Category**: WG21 Governance / Power Dynamics

**Source Type**: Explicit

**Supporting Quote**:
> "He doesn't get to decide things for the committee. He's an administrator. He also sits in EWG and argues for and against proposals. But as a convener, he does a lot of administrative stuff and tries to keep things moving... he set the schedule for like every three years."

**Context**: Clow clarifies that while Herb wields influence through agenda-setting and chair appointments, technical outcomes emerge from proposal champions and committee consensus.

**Actionable Guidance**:
- Understand the difference between administrative and technical authority
- Build coalitions for proposals; no single person can mandate adoption
- Work with chairs and convener on process, not outcomes
- Recognize schedule-setting as significant indirect power

---

### P-MC-011: Corporate Resources Amplify But Don't Corrupt

**Statement**: Large companies (Google, Microsoft, Bloomberg) have more resources to develop proposals, implement them, and send delegates, but this represents amplified voice rather than undue influence.

**Category**: WG21 Governance / Influence Dynamics

**Source Type**: Explicit

**Supporting Quote**:
> "Is this some secretive kind of underhanded thing? No, it's very, very open... Google has their Abseil libraries. They have proposed several of their Abseil libraries for standardization... That doesn't make it bad. It just means you gotta know where they're coming from."

**Context**: Clow addresses concerns about corporate influence, noting that corporate proposals tend to have implementation experience, which is a feature, not a bug.

**Actionable Guidance**:
- Evaluate proposals on merit, not provenance
- Recognize implementation experience as valuable signal
- Track which organizations champion which proposals
- Create pathways for individual contributors to participate

---

## Experiences

### E-MC-001: Stepanov's Keynote as Career Pivot

**Narrative**: In September 2003, Marshall Clow attended a small software conference in the Santa Cruz mountains where Alex Stepanov delivered "The Greatest Common Measure: 2,500 Years." The talk traced generic programming's roots from ancient mathematics to the STL, and it fundamentally changed Clow's understanding of programming. He went home "with his head spinning," started studying the STL intensively, found Boost, and eventually joined WG21.

**Key Quote**:
> "I went home and started tearing it apart and trying to write all sorts of things and basically that changed my whole outlook on programming and basically sent my career off in a completely different direction."

**Lesson**: Single talks by brilliant communicators can permanently redirect careers. Creating opportunities for such encounters (conferences, keynotes) has multiplicative impact.

**Linked Principles**: P-MC-002 (Cognitive Load)

---

### E-MC-002: Boost Algorithm Library from Library-in-a-Week

**Narrative**: At BoostCon, Jeff Garland runs a "library in a week" session where attendees brainstorm and implement libraries. During an algorithms session, Sean Parent mentioned the lack of a good Boyer-Moore implementation for C++. Clow went home, read the papers, implemented Boyer-Moore and Boyer-Moore-Horspool, then packaged them with other algorithms and submitted for Boost review. Dave Abrahams agreed to review it in exchange for Clow managing another library's review.

**Key Quote**:
> "Sean popped up with, 'you know, it's a real shame that there isn't a good Boyer Moore implementation for C++.' And I said, oh, okay, I can do that."

**Lesson**: Collaborative sessions and casual conversations can spark significant library development. The review quid-pro-quo ("I'll review yours if you manage mine") built community capacity.

**Linked Principles**: P-MC-001 (Maintainership), P-MC-003 (Existing Practice)

---

### E-MC-003: Boost Process Library's Instructive Rejection

**Narrative**: Clow managed the review for a proposed Boost Process library that was not initially accepted. During the interactive review process, fundamental flaws were identified that the author acknowledged. The author went away, worked on the problems for years, and resubmitted—the second time it was accepted.

**Key Quote**:
> "I said to him, I don't think your library's gonna be accepted. And he said, yeah, I know. Because somebody had pointed out a few fundamental flaws... He went away and worked on it for a while and submitted for review again later. Couple, three years later, I believe the second time it was accepted."

**Lesson**: Rejection is part of the process, not failure. Good faith rejection with clear feedback enables improvement. Multi-year development cycles between reviews are normal.

**Linked Principles**: P-MC-003 (Existing Practice)

---

### E-MC-004: Christopher Kohlhoff's Discouragement

**Narrative**: Christopher Kohlhoff, the Asio author living in Australia, attended WG21 meetings to advance the Networking TS. The proposal faced repeated objections that the design was "not how we write C++ today." Kohlhoff became discouraged—not actively blocked, but worn down. Seven years later, C++ still lacks standard networking.

**Key Quote**:
> "Chris came to a couple of standards meetings. It was hard for him, when he's in Australia... He was discouraged... and feeling discouraged, and now it's six or seven years later and we still don't have networking in the standard library, which is unfortunate."

**Lesson**: Procedural exhaustion can defeat proposals as effectively as explicit rejection. Geographic barriers compound the cost of participation. "Perfect is the enemy of good" in standards bodies.

**Linked Principles**: P-MC-006 (Adoption vs Purity)

---

### E-MC-005: Prague Standing Ovation

**Narrative**: At the Prague meeting in February 2020, Clow's final meeting as LWG chair, the committee voted out C++20 after intensive work. When he announced stepping down after five years, he received a standing ovation—an emotional moment of recognition for sustained volunteer leadership.

**Key Quote**:
> "I got a standing ovation... Everybody stood up and made it clear that they appreciated all the work I'd done. And people came up and said thank you and shook my hand and bought me beers. And it was a nice feeling."

**Lesson**: Volunteer leadership in standards work is often taken for granted. Explicit recognition ceremonies validate contributions and encourage future service.

**Linked Principles**: P-MC-007 (Chair Succession)

---

### E-MC-006: Hired by C++ Alliance to Continue Existing Work

**Narrative**: When Qualcomm laid off Clow, Vinnie Falco reached out through the C++ Alliance to hire him to continue exactly what he had been doing: Boost work, libc++ contributions, and WG21 participation. This preserved continuity that might otherwise have been lost to finding unrelated employment.

**Key Quote**:
> "Vinny reached out to me and said, we'd like to hire you to keep doing the things you're doing... He was gonna pay me to do it instead of Qualcomm paying me to do it. He thought it had value. He thought I was providing, helping things along. He didn't wanna see it stop."

**Lesson**: Funding continuity of expert contributions is an efficient intervention. The Alliance model of paying people to do what they'd do unpaid (but might have to stop) preserves ecosystem capacity.

**Linked Principles**: P-MC-008 (Boost Mission Evolution)

---

### E-MC-007: Unified Function Call Syntax Surprise Defeat

**Narrative**: Bjarne Stroustrup's Unified Function Call Syntax proposal went through years of discussion and subgroup votes before reaching plenary in Jacksonville (2016). Despite the usual expectation that plenary is procedural, significant objections were raised at the last minute, and it was voted down—a surprising outcome that frustrated people accustomed to earlier resolution.

**Key Quote**:
> "A lot of people stood up and spoke out against it, and there was a lot of discussion and eventually it was voted down. Which is kind of surprising because usually by the time it gets to the plenary session... everything's cut and dry."

**Lesson**: Even late-stage proposals can fail if fundamental disagreements aren't resolved. Plenary votes are not rubber stamps. Large changes that "simplify for users while complicating for implementers" face particular resistance.

**Linked Principles**: P-MC-005 (Train Schedule)

---

### E-MC-008: lib C++ Global Reach

**Narrative**: Clow estimates his libc++ code runs on "a billion and a half devices every single year"—every iOS device, every Android device, many routers and embedded systems. When visiting SpaceX, he tried to confirm libc++ was in their stack (they declined to confirm, being "a very secretive bunch"), but he's confident it's there.

**Key Quote**:
> "I used to joke that my code went into a billion to a billion and a half devices every single year. Every iOS device, every iPhone, every iPad, every Mac OS device, every Android device... a billion and a half devices a year is probably a low estimate."

**Lesson**: Standard library implementation work has extraordinary reach. The impact of getting foundational code right is multiplied by billions of deployments.

**Linked Principles**: P-MC-004 (Good Libraries)

---

## Evaluation Checklists

### For Library Acceptance (Boost or Standards)

1. **Generic Design**
   - [ ] Works with multiple types through templates
   - [ ] Documents requirements (concepts) for type parameters
   - [ ] Provides performance guarantees (complexity bounds)
   - [ ] Follows open-closed principle (extensible without modification)

2. **Usage Experience**
   - [ ] Implementation exists and is tested
   - [ ] Real users have deployed it in production
   - [ ] Bug reports have been received and addressed
   - [ ] Edge cases discovered through use are documented

3. **Quality Attributes**
   - [ ] Easy to use correctly for common cases
   - [ ] Hard to misuse (compile-time or runtime errors for mistakes)
   - [ ] Minimal but sufficient customization points
   - [ ] Well-documented behavior and rationale

4. **Maintainability**
   - [ ] Author willing to maintain or successor identified
   - [ ] Works with current and near-future compiler versions
   - [ ] Clear licensing (preferably BSL or similar)
   - [ ] Test suite covers documented functionality

### For Standards Proposals

1. **Existing Practice**
   - [ ] Multi-year implementation exists (Boost, vendor, standalone)
   - [ ] Significant user base (not just author's projects)
   - [ ] Bug reports and fixes demonstrate real-world usage
   - [ ] Not already obsoleted by newer techniques

2. **Committee Readiness**
   - [ ] Author willing to attend meetings and respond to feedback
   - [ ] Geographic/time constraints of author considered
   - [ ] Champion coalition exists beyond single author
   - [ ] Multiple implementations feasible (not vendor-locked)

3. **Scope Appropriateness**
   - [ ] Fills genuine gap in standard library
   - [ ] Not duplicating existing facilities
   - [ ] Complexity justified by breadth of applicability
   - [ ] Wording can be completed in reasonable time

---

## Open Questions

1. **Networking Impasse Resolution**: Given Clow's assessment that waiting for theoretical perfection left C++ without networking for a decade, how should the committee balance pragmatic adoption against architectural concerns?

2. **Boost Mission Clarity**: With Boost no longer primarily a standards incubator, how should it communicate its current value proposition to attract contributors and users?

3. **Chair Term Limits**: Is five years optimal for working group chairs? Should there be formal term limits or mandatory mentorship of successors?

4. **Geographic Accessibility**: How can WG21 better accommodate contributors from distant locations (e.g., Australia) to prevent discouragement-through-exhaustion?

5. **Post-Absorption Identity**: What happens to incubation organizations when their flagship components are absorbed into the standard? Is "doldrums" an inevitable transition period?

---

## Raw Transcript Reference

**Source**: Documentary interview footage
**Date**: December 16, 2025
**Location**: Poway, California
**Format**: Video interview with audio transcription

The transcript covers:
- Personal background and career trajectory (0:00-17:00)
- Stepanov influence and generic programming (17:00-29:00)
- Boost involvement and library-in-a-week (29:00-38:00)
- Boost license development (38:00-44:00)
- WG21 entry and LWG chair experience (44:00-57:00)
- Networking TS and Asio debate (57:00-62:00)
- Boost evolution and C++ Alliance (62:00-76:00)
