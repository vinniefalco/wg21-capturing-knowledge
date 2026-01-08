# Howard Hinnant: Captured Knowledge

**Interview Date**: January 7, 2026  
**Interviewer**: Vinnie Falco  
**Duration**: ~59 minutes (12:05 PM – 1:04 PM Pacific)  
**Topics Covered**: Library standardization criteria, field experience requirements, allocator design, hashing proposals, ABI stability, committee dynamics, exception safety, undefined behavior, API layering, evaluation frameworks

## Executive Summary

Howard Hinnant brings nearly three decades of WG21 experience, beginning as MetroWorks' sole standard library implementer in 1998 and later serving as LWG chair starting in 2005. His perspective is grounded in implementation reality: he has personally shipped standard library code and experienced the consequences of committee decisions at the vendor level.

His most powerful insight is the **standardization threshold principle**: the standard should make the impossible possible or the hard easy, but not the easy easier. This filters out "convenience" proposals that add maintenance burden without solving real problems. He couples this with an unwavering requirement for **positive field experience**—proposals without real-world validation are gambling with the standard's long-term quality.

Howard also articulates the fundamental structural limitation of WG21: it's a volunteer organization lacking executive power. No one can compel work to be done, which means important but contentious proposals (like his hash improvements) can simply be abandoned when participants tire of arguing. This explains why obvious needs sometimes go unaddressed for years.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Make the Impossible Possible, Not the Easy Easier

> *"I prefer to make what was previously impossible or impractical, possible. Or if not that, to make something that is very difficult, to make it easy. But making the easy easier, I find very uninteresting and not worthwhile to standardize."*

**The Principle**: Only standardize features that enable what was previously impossible/impractical, or that significantly reduce difficulty of hard tasks; reject proposals that merely add convenience for already-easy operations.

**Why It Matters**: The standard library is large and every addition incurs maintenance cost, implementation burden, and cognitive load. Convenience features that don't clear a high value bar accumulate as cruft without proportionate benefit.

**When to Apply**: When evaluating any library proposal, especially "utility" functions or thin wrappers.

**Red Flags**:
- Proposal can be trivially implemented by users in a few lines
- Functionality is already achievable with existing standard components
- Primary benefit is "slightly nicer syntax" or "saves a few keystrokes"
- No explanation of what was previously impossible/hard

**Supporting Experiences**: E3 (std::exchange example)

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: belongs/library
applies-to: library
confidence: high
supported-by: [E3]
related-principles: [P2, P8]
-->

---

### P2: Require Positive Field Experience Before Standardization

> *"My personal viewpoint is that nothing should be standardized unless it has some positive field experience under its belt... field experience will bang out use cases."*

**The Principle**: Proposals must demonstrate successful real-world usage with positive feedback from independent users before standardization; implementation alone is insufficient.

**Why It Matters**: Field experience reveals use case gaps, API friction, and design flaws that aren't visible in paper review. Standardizing without it is gambling—sometimes you get lucky, sometimes you don't.

**When to Apply**: When evaluating any proposal, but especially novel APIs, complex features, or significant additions.

**Red Flags**:
- No public implementation available for users to try
- Implementation exists but no evidence of external adoption
- "Field experience" limited to the proposer's team/company
- Theoretical benefits without demonstrated practical value

**Supporting Experiences**: E1, E6

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E1, E6]
related-principles: [P1, P8]
-->

---

### P3: The Committee Lacks Executive Power

> *"With a group of volunteers, although there's working group chairs and there's conveners, different leaders, there's no one who can say, I want you to do this, and if you don't, you're fired."*

**The Principle**: WG21 is a volunteer organization without executive authority; no one can compel work to be done, which means important but contentious proposals may be abandoned when champions lose interest.

**Why It Matters**: Understanding this structural limitation explains why obvious improvements sometimes languish for years. Proposals require sustained champion effort through potentially years of debate; without that persistence, even clearly needed features can fail.

**When to Apply**: When planning proposal strategy, when analyzing why past proposals failed, when setting expectations for timeline.

**Red Flags**:
- Proposal depends on someone else to do significant work
- Champion lacks bandwidth for multi-year effort
- Contentious design with no path to consensus
- Assuming "obvious need" will drive progress without active championing

**Supporting Experiences**: E2, E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E2, E3]
related-principles: [P4]
-->

---

### P4: Consensus Ensures Agreement, Not Alignment with User Needs

> *"To ensure alignment, the committee has to agree by consensus... consensus is more than a majority, it's roughly 2/3."*

**The Principle**: The consensus mechanism ensures committee agreement but provides no guarantee that approved proposals align with actual C++ user needs; there is no formal mechanism for validating market demand.

**Why It Matters**: A proposal can achieve consensus among committee members while failing to address real user problems, or while solving problems users don't actually have. Internal agreement is necessary but not sufficient.

**When to Apply**: When evaluating whether a proposal should proceed despite consensus; when questioning whether unanimous support reflects actual user demand.

**Red Flags**:
- High consensus but no external user feedback cited
- Proposers are committee regulars but not practitioners in the problem domain
- No evidence of users asking for this feature
- "The committee likes it" as primary justification

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P4
source-type: implicit
category: process/politics
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: [P2, P3]
-->

---

### P5: Evaluate ABI Breaks by Cost/Benefit, Not Automatic Veto

> *"If you're really rigid about ABI stability, then you just paint yourself into a corner eventually where you can't improve things. So ultimately you've got to be able to break ABI at least every once in a while."*

**The Principle**: ABI stability concerns should trigger cost/benefit analysis, not automatic rejection; some ABI breaks are worth the transition cost.

**Why It Matters**: Treating ABI concerns as an absolute veto prevents beneficial evolution. The SSO string transition was painful but worthwhile. Claims of "ABI break" should prompt analysis, not shutdown.

**When to Apply**: When proposals are opposed on ABI grounds; when evaluating whether ABI concerns are being used as a veto without analysis.

**Red Flags**:
- "This breaks ABI" stated without quantifying the impact
- No analysis of what the ABI break would actually cost
- No comparison of break cost vs. feature benefit
- Historical ABI accidents used to reject all future changes

**Supporting Experiences**: E4, E5

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: philosophy/evolution
applies-to: library
confidence: high
supported-by: [E4, E5]
related-principles: [P6]
-->

---

### P6: Correctness Over Performance, Always

> *"Performance is the 2nd most important goal when writing code. And the most important goal is correctness. And every once in a while, we seem to reverse those two."*

**The Principle**: Correctness must always take precedence over performance; optimizations that sacrifice correctness (like compilers removing "UB" code that would otherwise work) invert the proper priority.

**Why It Matters**: Performance gains from exploiting undefined behavior can turn working code into broken code. Hardware has defined behavior (e.g., signed overflow wraps); standards saying "undefined" enables dangerous optimizations.

**When to Apply**: When evaluating proposals with performance claims, when reviewing code that relies on UB not being exploited, when considering compiler optimization strategies.

**Red Flags**:
- Performance claims based on exploiting UB
- "The hardware does X but the standard says undefined"
- Optimizations that remove user-written safety checks
- Trading correctness for benchmarks

**Supporting Experiences**: None directly stated

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: []
related-principles: [P7]
-->

---

### P7: Offer Both Checked and Unchecked API Layers

> *"It's often good to have like a two-layer API, a low level layer that is unchecked. And then a safer layer, checked layer built on top of that, so that the mid-level programmer knows whether he's got this adversarial input or not."*

**The Principle**: Design APIs with dual layers—an unchecked low-level layer for trusted contexts and performance-critical paths, and a checked layer for adversarial inputs and safety-critical paths.

**Why It Matters**: Users have different needs: some process trusted internal data and need maximum performance; others face adversarial input and need robust validation. A single API forces one group to pay costs they don't need.

**When to Apply**: When designing parsing APIs, validation APIs, or any API that might process untrusted input.

**Red Flags**:
- API forces validation overhead on all callers
- API lacks validation, forcing all callers to implement checks
- No consideration of adversarial input scenarios
- Performance and safety treated as mutually exclusive

**Supporting Experiences**: None directly stated

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: []
related-principles: [P6]
-->

---

### P8: Every Paper Must Answer "What Problem?" and "What's the Alternative?"

> *"What problem am I solving and if this paper's not accepted, how does the programmer solve this problem without this solution."*

**The Principle**: Every proposal must clearly answer: (1) What specific problem does this solve? (2) Without this proposal, how hard is the problem to solve?

**Why It Matters**: These questions expose proposals that solve non-problems or provide marginal improvements. If the alternative is easy, standardization adds cost without proportionate value.

**When to Apply**: As a first-pass filter for all proposals; when evaluating motivation sections.

**Red Flags**:
- Problem statement is vague or absent
- No discussion of existing solutions
- Existing solution is nearly as good
- "Convenience" is the primary value proposition

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: evaluation/motivation
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P1, P2]
-->

---

### P9: Dangerous Tools Are Fine If Used Correctly

> *"Any good tool is dangerous. I mean, I'm a big fan of pocket knives and kitchen knives... they can really help in the kitchen or they can chop your fingers off. You just have to know how to use them."*

**The Principle**: Features that can be misused are not inherently bad; the standard should provide powerful tools and trust users to learn correct usage, rather than crippling tools to prevent misuse.

**Why It Matters**: Overly "safe" designs often sacrifice power and flexibility. String_view can dangle, but that doesn't make it bad—it makes it a tool requiring skill. C++ is a language of sharp tools.

**When to Apply**: When evaluating proposals that add constraints to prevent misuse; when defending features criticized as "dangerous."

**Red Flags**:
- Proposal cripples functionality to prevent misuse
- "Users will misuse this" as primary objection
- Safety achieved by removing capability rather than providing guidance
- Treating C++ users as unable to learn correct usage patterns

**Supporting Experiences**: None directly stated

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: philosophy/language
applies-to: both
confidence: high
supported-by: []
related-principles: [P7]
-->

---

### P10: Standardization Solves Cross-Platform Availability

> *"It makes it easier to port from platform to platform. If you can grab it from the library, that means you don't have to install a third party library, which is naturally going to be probably a non-portable process."*

**The Principle**: A key benefit of standardization is guaranteed cross-platform availability, eliminating the friction of acquiring and building third-party dependencies.

**Why It Matters**: Even excellent third-party libraries face adoption barriers: build system integration, version management, platform variations. Standardization removes these barriers for features important enough to justify inclusion.

**When to Apply**: When evaluating whether a library belongs in the standard vs. ecosystem; when justifying standardization beyond "it's useful."

**Red Flags**:
- Proposal for something trivially available via package managers
- No evidence that cross-platform availability is a real friction point
- Feature only relevant on one platform
- Claiming portability benefit for highly platform-specific functionality

**Supporting Experiences**: None directly stated

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: belongs/library
applies-to: library
confidence: medium
supported-by: []
related-principles: [P1]
-->

---

### P11: Mentorship Is Informal but Essential

> *"He was definitely a mentor of mine. He guided me along in the library working group. He taught me the ropes of how to work with the standard committee... and advised me the right way of doing things."*

**The Principle**: WG21 knowledge transfer happens through informal mentorship relationships, not formal onboarding; newcomers must seek out mentors or learn through trial and error.

**Why It Matters**: Without deliberate mentorship, institutional knowledge is lost when experienced members retire. The lack of formal mechanisms means knowledge transfer depends on relationship formation.

**When to Apply**: When joining the committee, when experienced members are retiring, when diagnosing why newcomers struggle.

**Red Flags**:
- Newcomers receiving no guidance on unwritten rules
- Experienced members leaving without knowledge transfer
- "Just read the papers" as onboarding strategy
- Criticism of newcomers for violating norms they were never taught

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P3]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Vector<bool> — "I Thought You Guys Knew What You Were Doing"

**Context**: Howard's first WG21 meeting (1998-1999). He had just implemented `vector<bool>` for MetroWorks when C++98 shipped.

**What Happened**: At his first meeting, he encountered a defect report stating that `vector<bool>` was not a proper container. The proposed resolution was essentially to tear it down and start over. Howard was shocked that such a fundamental flaw existed in a just-shipped standard.

**The Outcome**: Howard said out loud what he was thinking: "I thought you guys knew what you were doing." Beman Dawes gently corrected him with what Howard describes as his "first lesson in standardization: don't be an asshole." Beman became Howard's mentor and guided him through his early committee years.

**The Lesson**: Major design flaws can survive the standardization process. Newcomers should approach the standard with appropriate humility—it has bugs—but also with respect for those working to fix them. Mentorship relationships are formed through these interactions.

> *"I was just blown away that such a massive bug appeared in the standard... Beman Dawes taught me my first lesson in standardization: don't be an asshole."*

**Supports Principles**: P2, P11

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [vector-bool]
supports: [P2, P11]
-->

---

### E2: The Failed Allocator Proposal

**Context**: Around 2010, Howard proposed extending the allocator API to support smarter memory management: asking "how much memory did you actually give me?", "can you expand this in place?", and potentially shrinking allocations.

**What Happened**: Howard recognized that for the proposal to succeed, it would need C committee buy-in because C++ allocators ultimately depend on C's `malloc`/`free`. He attempted to engage WG14 (the C committee) but was unsuccessful—he didn't regularly attend C meetings and was essentially a stranger to them.

**The Outcome**: Failure. The proposal was "doomed to fail" because Howard lacked the relationship and credibility with the C committee. The allocator API remains limited to this day.

**The Lesson**: Cross-committee proposals require relationship building with both committees. Being a stranger to a group you need buy-in from is nearly disqualifying. The volunteer nature of committees means you can't compel cooperation—you must earn it through participation.

> *"I was unsuccessful at getting the C committee interested. Which isn't too surprising because I didn't regularly attend the C meeting and so I was kind of a stranger. They didn't know who I was."*

**Supports Principles**: P3

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [allocators]
supports: [P3]
-->

---

### E3: The Hash Proposal Deadlock

**Context**: Howard (with Vinnie as co-author) proposed a hash API allowing multiple objects to be hashed with a single algorithm, preserving hash quality. Google independently became interested in the same problem.

**What Happened**: Howard and Google had "intense disagreement over details on how to accomplish it, what exactly the API should be like." The debate continued until both parties were exhausted. Despite both recognizing the clear need for improved hashing—and hashing being a vocabulary-type problem that clearly belongs in the standard—no progress was made.

**The Outcome**: Both Howard and Google dropped the proposal. "We argued with each other until both Google and myself were tired of arguing, and we both just dropped it."

**The Lesson**: The committee's volunteer nature means even obviously needed improvements can fail if champions lose interest. There's no executive power to force resolution. When two strong parties disagree and neither will compromise, the work simply stops, regardless of how important it is.

> *"There's no one who can say, I want you to do this, and if you don't, you're fired. You can't fire somebody."*

**Supports Principles**: P1, P3, P4, P8

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [hashing, std-hash]
supports: [P1, P3, P4, P8]
-->

---

### E4: GCC's String ABI Break — Worth the Pain

**Context**: The C++ standard library needed to transition from reference-counted strings to short string optimization (SSO).

**What Happened**: This required a massive ABI break. GCC was hit hardest—it took them "years and years to transition users from one design to the other." The cost was "very, very high."

**The Outcome**: Success. Howard states: "The benefit was equally high. Or higher... The community is today better off than when it was before the ABI break."

**The Lesson**: Some ABI breaks are worth the cost. The transition was painful but resulted in a better outcome for everyone. ABI concerns should trigger cost/benefit analysis, not automatic rejection.

> *"It was a huge ABI break. And yet we still did it, and I'm glad we did. It was still worth it."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [basic-string, sso]
supports: [P5]
-->

---

### E5: Apple's Explicit Instantiation Regret

**Context**: While at Apple building libc++, Howard wanted to minimize ABI surface by keeping code in headers as templates rather than explicitly instantiating into the dynamic library.

**What Happened**: Howard's managers disagreed. They wanted explicit instantiation of templates like `vector` into the dylib to achieve faster compile and link times. Despite Howard's objections about the ABI fragility this would create, management overruled him.

**The Outcome**: Mixed/Failure. The decision created permanent ABI fragility in libc++ that "can't be broken" because it's baked into the shipped dylib. Howard considers this a mistake that traded short-term compile performance for long-term flexibility.

**The Lesson**: Baking implementations into shared libraries creates ABI constraints that are extremely difficult to remove later. Short-term benefits (faster builds) can create long-term costs (frozen ABI). Template-heavy headers, while slower to compile, preserve more flexibility.

> *"libc++ has some extra fragility in its ABI that can't be broken because my managers forced me to explicitly instantiate things like vector into the dylib."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/regrets
applies-to: library
outcome: failure
features: [abi, dylib, explicit-instantiation]
supports: [P5]
-->

---

### E6: Variant's Valueless State Controversy

**Context**: During standardization of `std::variant`, a critical design question arose: what state should variant be in if an exception is thrown during move assignment?

**What Happened**: There was major disagreement about the correct design. The debate was intense enough that variant "missed several standard deadlines, got standardized years later than otherwise would have." The compromise was a "valueless" state—similar to floating-point NaN—where the variant holds no value.

**The Outcome**: Mixed. The feature shipped, but with a design that some consider suboptimal. Peter Dimov's later `Boost.Variant2` demonstrated an alternative approach where variant always holds a value (when at least one type is default constructible), and this gained popularity, suggesting the original design left a need unmet.

**The Lesson**: Difficult design decisions can delay standardization for years. Compromises reached under deadline pressure may not be optimal. Field experience with alternative designs (like Variant2) can reveal that the standardized version left user needs unaddressed.

> *"It's almost like a floating point NaN. It's essentially not a value... I believe it missed several standard deadlines."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/failures
applies-to: library
outcome: mixed
features: [variant, exception-safety]
supports: [P2]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Does this make the impossible possible, or the hard easy? (not the easy easier)
- [ ] Is there positive field experience from independent users?
- [ ] What specific problem does this solve?
- [ ] How hard is the problem to solve without this proposal?
- [ ] Is there evidence of real user demand (GitHub usage, Stack Overflow questions, etc.)?
- [ ] Does standardization provide cross-platform availability benefit beyond third-party libraries?
- [ ] What is the implementation burden on standard library vendors?
- [ ] Are there ABI implications? If so, what's the cost/benefit analysis?

**Questions to Ask**:
1. "Without this proposal, how does a programmer solve this problem today?"
2. "Where is this implemented and who is using it successfully?"
3. "If I can write this in 5 lines, why does it belong in the standard?"
4. "What happens if this turns out to be wrong—can we fix it later?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P5, P8, P10]
-->

---

### When Evaluating API Design

- [ ] Does the API support both checked (safe) and unchecked (fast) usage patterns?
- [ ] Is correctness prioritized over performance?
- [ ] For features that can be misused, is guidance provided rather than capability removed?
- [ ] Do dangerous features require explicit opt-in or clear naming?
- [ ] Does the API handle adversarial input appropriately?

**Questions to Ask**:
1. "Can users who know their input is trusted skip unnecessary validation?"
2. "Can users facing adversarial input get robust error handling?"
3. "Is the 'dangerous' version named clearly (e.g., `_unchecked` suffix)?"
4. "What does misuse look like, and how can we guide users away from it?"

<!-- METADATA
kind: checklist
category: philosophy/library
applies-to: library
proposal-type: feature
derived-from: [P6, P7, P9]
-->

---

### When Assessing Proposal Viability

- [ ] Does the champion have bandwidth for potentially years of effort?
- [ ] If this requires cross-committee (WG14) buy-in, does the champion have those relationships?
- [ ] Is there a clear path to consensus, or are there entrenched opposing camps?
- [ ] Has the proposal survived contact with real implementation and real users?
- [ ] Are there alternative proposals that might deadlock progress?

**Questions to Ask**:
1. "Who will shepherd this through if the original champion loses interest?"
2. "Are there competing proposals, and is there a path to resolution?"
3. "What committee relationships does this proposal depend on?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P3, P4, P11]
-->

---

## Open Questions

1. **What is Howard's full list of proposals that were rejected (the other 50%)?** Understanding what was rejected and why would provide additional insight into committee evaluation patterns.

2. **What specific "convenience" APIs does Howard consider mistakes?** He mentions `std::exchange` as an example he didn't vote for—are there others?

3. **What were the details of the Google hash proposal?** Understanding the specific technical disagreements might illuminate patterns in how API design conflicts arise and fail to resolve.

4. **How has the committee's stance on undefined behavior evolved?** Howard mentions "erroneous behavior" as a recent development but isn't familiar with details.

5. **What specific signed integer overflow optimizations has Howard seen cause problems?** He references "infamous cases" without specifics.

6. **What are the specific features that Peter Dimov's Variant2 handles differently?** Understanding the delta between std::variant and Boost.Variant2 could inform future API design.

7. **What metrics does the committee currently track, if any?** Howard mentions email threads about C++ user counts but doesn't know details.

8. **What happened to the mentorship tradition?** Howard describes Beman Dawes as a mentor, but there's no formal mechanism. Has informal mentorship declined as the committee has grown?

---

## Raw Transcript Reference

See: `transcripts/howard-hinnant.md`

Interview conducted January 7, 2026, covering Howard's journey from MetroWorks (1998) through Apple/libc++ to Ripple, with extensive discussion of library design principles, standardization criteria, and committee dynamics.
