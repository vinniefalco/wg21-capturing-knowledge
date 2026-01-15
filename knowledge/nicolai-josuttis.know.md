# Nicolai Josuttis: Captured Knowledge

**Interview Date**: 2025-09-17
**Interviewer**: Ray Nowosielski
**Location**: Aurora, CO
**Duration**: ~72 minutes
**Topics Covered**: Boost founding, Beman Dawes, std::array history, WG21 early years, C++11 impact, standardization process, Java competition, Boost license, declining Boost influence, "inventing while standardizing" critique, std::thread to std::jthread story

## Executive Summary

Nicolai Josuttis provides a unique perspective as both a witness to Boost's founding moment in 1998 and a long-serving C++ author and committee member. His narrative connects Boost's creation directly to the completion of C++98, describing how Beman Dawes approached him about "a website for peer-reviewed C++ libraries" just as the first standard was being finalized.

Most striking is Josuttis's candid frustration with the committee's recent departure from the "existing practice first" model that made Boost successful. He argues that WG21 has lost "the general view of C++" and now "invents while standardizing"—a fundamental break from the philosophy that libraries should mature through years of real-world use before becoming standards. His assessment that "200 cooks spoil the meal" reflects deep concern about specialization replacing the generalist perspective that characterized early Boost contributors.

Josuttis's account of the std::thread design flaw provides a concrete example of his concerns: the committee knew before C++11 that the type violated RAII principles, but "there was not enough political support to fix the flaw." Years of community workarounds eventually forced std::jthread's creation—a pattern he sees repeating with other prematurely standardized features.

The interview also captures the human side of C++ history: his first encounter with Beman and Sandra Dawes in a hotel lobby, the cultural diversity of early committee meetings, and his observation that programmers are "pirates of the universe"—independent thinkers who resist traditional career structures.

---

## Principles

### P-NJ-001: Take Time to Establish Before Standardizing

**Statement**: Libraries should be established at Boost for 3-7 years before standardization to ensure robustness; inventing during standardization leads to mistakes.

**Category**: Standardization Process / Quality Assurance

**Source Type**: Explicit

**Supporting Quote**:
> "We don't take our time to say, let's establish things at Boost, take 3, 5, 7 years, and then we know how it should be, and then we standardize. No. More and more we invent libraries while we standardize, and that's a huge mistake we have."

**Context**: Josuttis contrasts the original Boost model (mature libraries becoming standards) with current practice (designing during committee process), expressing frustration at the resulting quality issues.

**Actionable Guidance**:
- Require multi-year deployment before proposing standardization
- Use Boost or similar incubators for design iteration
- Distinguish "proposing" from "inventing" in committee
- Measure design stability over time before final votes

**Corroborating Sources**: Multiple interviewees on existing practice principle

---

### P-NJ-002: Reviewer Quality Determines Library Quality

**Statement**: No formal process can guarantee library quality; what matters is having experienced generalists with broad vision who can evaluate across diverse use cases.

**Category**: Review Process / Quality Assurance

**Source Type**: Explicit

**Supporting Quote**:
> "My experience is whatever your process is, if those who review are idiots, crap falls out... the biggest benefit was that Beman was able to bring together the right people and also himself to say, no, that's not good enough."

**Context**: When asked about what made Boost's review process successful, Josuttis emphasizes people over procedures.

**Actionable Guidance**:
- Invest in cultivating experienced reviewers
- Prioritize generalists who understand multiple domains
- Empower reviewers to reject inadequate submissions
- Recognize that processes are necessary but not sufficient

---

### P-NJ-003: C++ Standard Libraries Must Be Domain-Agnostic

**Statement**: Standard library components must work across fundamentally different domains (embedded, finance, medical, mainframe), requiring exceptional generalist thinking from reviewers.

**Category**: Library Design / Scope Appropriateness

**Source Type**: Explicit

**Supporting Quote**:
> "What is so special about C++ standard libraries is they don't fulfill a purpose of a specific domain. They are the basics for a lot of general data processing in very different domains under very different circumstances... Is this usable by a mainframe? Is it usable in an embedded system? Is it usable by medical software? Is it usable by finance software?"

**Context**: Josuttis explains why Boost reviewer selection was critical—standard library components face requirements unlike any single-purpose library.

**Actionable Guidance**:
- Test library designs against diverse domain requirements
- Include reviewers from multiple industry verticals
- Question domain-specific assumptions in proposals
- Recognize that "general purpose" is harder than "specific purpose"

---

### P-NJ-004: Standardization Provides Second Chance for Design

**Statement**: Moving from Boost to the standard provides an opportunity to fix known flaws because backward compatibility constraints reset at the namespace boundary.

**Category**: Standardization Process / Evolution Strategy

**Source Type**: Explicit

**Supporting Quote**:
> "When we take the existing backward-compatible Boost library and put it to the C++ standard, that's now something kind of new because it's the filesystem library of the C++ standard, which is kind of different than the filesystem library of Boost. We could, to some extent, make fixes we always wanted, but we would not break existing code because it's new code. Because it's not in the namespaces, in the areas of the existing code."

**Context**: Describing how the filesystem library was improved during standardization, catching Windows portability issues that Boost's Linux-focused community had missed.

**Actionable Guidance**:
- View standardization as "version 2.0" opportunity
- Don't blindly copy Boost implementations into the standard
- Re-examine designs against broader platform requirements
- Use namespace transition to break from accumulated quirks

---

### P-NJ-005: The Committee Has Lost the General View

**Statement**: Modern WG21 has too many specialists caring for "a specific part of C++" and too few generalists who can evaluate the whole language coherently.

**Category**: WG21 Governance / Expertise Distribution

**Source Type**: Explicit

**Supporting Quote**:
> "We lost the general view of C++. So we have too many people caring for a specific part of it, a specific way to use it... This programming language has a problem that 200 cooks spoil the meal. We have 200 different interests and we do no longer take our time to make it really a robust, good, well-established library."

**Context**: Josuttis's explanation for why Boost's influence has declined and why recent standardization has made "a lot of mistakes."

**Actionable Guidance**:
- Actively cultivate generalist reviewers
- Require cross-domain review for all proposals
- Create mechanisms for holistic language evaluation
- Recognize specialization as both strength and risk

---

### P-NJ-006: Java's Rise Enabled Community-Driven Standardization

**Statement**: When Java captured industry attention in the late 1990s, corporate political games in C++ ended, allowing community-driven standardization to flourish.

**Category**: Historical Context / Governance Dynamics

**Source Type**: Explicit

**Supporting Quote**:
> "Java suddenly had all the focus and a lot of companies went there and said, oh, that's the game. We have to spend time there. So immediately when Java came up, there was less interest in C++, which helped us a lot because the political games ended and we could just work."

**Context**: Josuttis explains why early C++ standardization was unusually free of corporate interference.

**Actionable Guidance**:
- Recognize that reduced corporate attention can enable good work
- Don't assume high interest always produces good outcomes
- Use periods of reduced pressure to establish strong precedents
- Understand historical context when interpreting current dynamics

---

### P-NJ-007: C++ Is an Outlaw Language

**Statement**: C++ succeeds by ignoring conventional wisdom (e.g., "you must do OOP") and being proven right later; this outlaw identity is part of its character.

**Category**: Language Philosophy / Cultural Identity

**Source Type**: Explicit

**Supporting Quote**:
> "C++ has an interesting role in the world, and the role is, it's kind of an outlaw. We don't follow rules as they are established and it turns out to be right... We came up with templates and everybody said, no, you have to do object-oriented programming. And you have to do it that way. But we did it differently and it turned out to be the right decision."

**Context**: Opening observation about C++'s cultural position, contrasting with conventional programming language evolution.

**Actionable Guidance**:
- Don't assume industry consensus determines correct direction
- Be willing to diverge from trends when justified
- Evaluate results, not just conformity to current fashion
- Maintain independent technical judgment

---

### P-NJ-008: Programmers Are Pirates of the Universe

**Statement**: The people who build critical software systems are often independent thinkers who resist traditional career paths, making them hard to corrupt with promotions but also hard to manage.

**Category**: Community Character / Cultural Observation

**Source Type**: Explicit

**Supporting Quote**:
> "Most of these people are not interested in the usual way to have a good career, go up and up becoming a boss... They finally want to program... They just are free persons. And that's what I would say is to some extent a category of these people. They're all pirates of the universe."

**Context**: Josuttis's characterization of the C++ community's personality, noting both strengths (independence) and implications (resistance to hierarchy).

**Actionable Guidance**:
- Design governance around intrinsic motivation
- Provide technical challenges, not just career ladders
- Accept that traditional management doesn't apply
- Value independence while finding coordination mechanisms

---

### P-NJ-009: Performance Is the Ultimate Arbiter

**Statement**: Despite complexity complaints, C++ survives because performance (speed and memory efficiency) matters—Google's sites would need 10x more energy in Java.

**Category**: Language Value Proposition / Technical Justification

**Source Type**: Explicit

**Supporting Quote**:
> "At the end, the performance was so great and performance is key in this world. Performance is both. It's speed and memory resources. What you have to know is the Google websites, if they would be driven in Java, they would need 10 times more energy."

**Context**: Josuttis's response to the common criticism that C++ is too complex, arguing that performance justifies the complexity.

**Actionable Guidance**:
- Use performance as evaluation criterion for proposals
- Consider resource consumption (energy, memory) not just speed
- Recognize C++ fills a specific niche: "fast enough, abstract enough"
- Don't sacrifice performance for convenience

---

## Experiences

### E-NJ-001: First Meeting with Beman Dawes

**Narrative**: At his first WG21 meeting (London, ~1996), Josuttis was standing in the hotel lobby when Beman Dawes came down an elevator with distinctive red hair. A woman followed, looked around, went to Beman, kissed him, and introduced herself: "I'm his wife." Josuttis was charmed by this playful relationship and "fell in love to some extent with this way of entertaining serious work."

**Key Quote**:
> "They were great people, but together they were an incredible couple and supporting each other and you could really see how they did enjoy life... kind of an enrichment instead of ownership, which is sometimes having relationships."

**Lesson**: The early C++ community was characterized by deep personal relationships that made technical work enjoyable; culture matters for sustained volunteer effort.

**Linked Principles**: P-NJ-008 (Pirates of the Universe)

---

### E-NJ-002: The "Die C++" Book Cover Incident

**Narrative**: At his first international standards meeting, Josuttis brought his German book "DIE C++ Standardbibliothek" (where "Die" is the German article "The"). The book was half-covered on a table, and Bjarne Stroustrup walked by, saw only "Die C++", and immediately approached Josuttis. After clarification, they became acquainted—a memorable first contact.

**Key Quote**:
> "All he read was die, C++. And that was how we got in contact. So he immediately knew me, that was for sure. 'What the hell is that?'"

**Lesson**: Cultural and language differences create memorable moments in international collaboration; first impressions can be accidental but impactful.

**Linked Principles**: P-NJ-006 (Cultural diversity in standardization)

---

### E-NJ-003: Beman's Booth Founding Conversation

**Narrative**: Just after the C++98 standard was finalized (auto_ptr was the last decision), Beman Dawes approached Josuttis and said: "I'm going to be retired. And I have an idea... maybe I start to create a website where we can peer-review C++ libraries." Josuttis encouraged him and asked to mention it in his C++ Standard Library book. Beman later emailed that he had reserved the website.

**Key Quote**:
> "Nico, I'm going to be retired. And I'm, I have an idea. And the idea is maybe I start to create a website where we can peer-review C++ libraries.' And that was a moment where I said, 'Yeah. Yeah. Great, do it.'"

**Lesson**: Boost emerged from a specific moment of personal transition (retirement) combined with recognition of a specific need (existing practice for standardization).

**Linked Principles**: P-NJ-001 (Take time to establish)

---

### E-NJ-004: The std::thread RAII Failure

**Narrative**: Before C++11 was finalized, the committee knew std::thread violated the RAII principle (it didn't clean up automatically on destruction). Despite agreement that this was wrong, "there was not enough political support to fix the flaw." The community responded by creating wrappers, which were "really bad." Eventually, the committee had to introduce std::jthread—a type that could have been std::thread from the beginning.

**Key Quote**:
> "We all agreed even before C++11 about that. So it should be a type that cleans up better... And we shipped that finally, and then we found out that the community is starting to wrap it because we didn't solve the cleanup problem correctly."

**Lesson**: Known design flaws standardized due to political deadlock create long-term ecosystem costs; backward compatibility prevents fixes once shipped.

**Linked Principles**: P-NJ-001 (Take time to establish)

---

### E-NJ-005: std::array's Journey from Bjarne to Standard

**Narrative**: Bjarne Stroustrup had an example of a fixed-size array wrapper in his book. Josuttis took that idea, implemented it, and submitted to early Boost with minimal review (Boost was just starting, processes weren't formalized). Years later, Alistair Meredith contacted him about proposing it for C++11. Josuttis said "do it" and Meredith did the actual standardization work.

**Key Quote**:
> "I never coined any idea. I just discuss it and bring it further. So the idea actually came from Bjarne Stroustrup... I took it and said, 'Let me prepare for Boost.'"

**Lesson**: Ideas flow through multiple hands; Boost served as the crucial bridge between conceptual examples in books and standardized components.

**Linked Principles**: P-NJ-003 (Domain-agnostic design)

---

### E-NJ-006: The Filesystem Library Windows Problem

**Narrative**: When the Boost.Filesystem library was being standardized for C++17, a small group (including Beman) discovered multiple problems, particularly around Windows support. The Boost community "was more on open source and that was more in the Linux area"—they hadn't caught issues that Windows users would face. Standardization provided the "second chance" to fix these flaws.

**Key Quote**:
> "We double-checked what we have there. And surprisingly, even for a library that existed for five to 10 years and was maintained at Boost, we thought, 'No, we cannot make it that way. That's not good. Let's make it more robust. Let's make it more portable.'"

**Lesson**: Boost community composition affects what gets caught in review; standardization review can catch what Boost missed.

**Linked Principles**: P-NJ-004 (Standardization as second chance)

---

## Evaluation Checklists

### For Boost Library Proposals

1. **Domain Independence**
   - [ ] Works on embedded systems (resource constraints)?
   - [ ] Works on mainframes (different architecture)?
   - [ ] Works for financial applications (reliability, precision)?
   - [ ] Works for medical software (safety, certification)?
   - [ ] Works on all major platforms (Windows, Linux, macOS)?

2. **Maturity Indicators**
   - [ ] How many years in production use?
   - [ ] How many distinct organizations using it?
   - [ ] What bugs were found and fixed through use?
   - [ ] Has the API stabilized or is it still changing?

3. **Reviewer Qualifications**
   - [ ] Do reviewers have cross-domain experience?
   - [ ] Have reviewers seen similar designs succeed/fail?
   - [ ] Is there at least one generalist reviewer?
   - [ ] Are platform specialists included?

### For Standardization Readiness

1. **Existing Practice Verification**
   - [ ] Multi-year Boost or equivalent deployment?
   - [ ] Multiple independent implementations?
   - [ ] Real user feedback incorporated?
   - [ ] Design stability demonstrated?

2. **Second-Chance Review**
   - [ ] Have Boost's accumulated quirks been examined?
   - [ ] Are there known issues that can be fixed at namespace transition?
   - [ ] Has the design been tested against current language features?
   - [ ] Are backward-compatible hacks still necessary?

3. **Generalist Evaluation**
   - [ ] Does the committee have sufficient generalists to evaluate?
   - [ ] Is the proposal being invented during standardization?
   - [ ] What would 3-5 more years of incubation reveal?
   - [ ] Are specialist interests overriding holistic judgment?

---

## Open Questions

1. **Generalist Cultivation**: How can WG21 deliberately cultivate generalist reviewers when the natural tendency is toward specialization?

2. **Invention Detection**: What signals indicate a proposal is being "invented during standardization" rather than codifying existing practice?

3. **Boost Revitalization**: Can Boost regain its role as the primary standardization incubator, or has that model been permanently displaced?

4. **200 Cooks Problem**: Is there an optimal committee size, and how would reducing participation be managed politically?

5. **Performance Justification**: How should energy consumption and resource efficiency be weighted in proposal evaluation?

---

## Raw Transcript Reference

**Source**: Documentary interview footage
**Date**: September 17, 2025
**Location**: Aurora, Colorado
**Format**: Video interview with audio transcription

The transcript covers:
- Personal background and philosophy (0:00-12:00)
- Boost founding and Beman Dawes (12:00-30:00)
- std::array and early Boost (30:00-43:00)
- Review process and quality (43:00-50:00)
- Boost libraries standardized in C++11 (50:00-58:00)
- std::thread RAII failure story (58:00-64:00)
- Declining Boost influence critique (64:00-72:00)
