# Howard Hinnant: Captured Knowledge (Documentary Interview)

**Interview Date**: 2025-10-26  
**Interviewer**: Ray Nowosielski  
**Location**: Sturbridge, MA  
**Duration**: ~87 minutes  
**Topics Covered**: Personal history, Boost origins, move semantics decade-long journey, Chrono library development, LWG chair experience, Peter Dimov's influence, C++11 standardization, field experience requirements, Ripple/cryptocurrency, Vinnie Falco, C++ Alliance

## Executive Summary

This documentary interview with Howard Hinnant provides a personal narrative of his journey from aerospace engineer to C++ standard library implementer, and his perspective on Boost's role in the C++11 transformation. Unlike his technical interview, this conversation emphasizes stories and relationships—particularly his mentorship by Beman Dawes and his observations of how Boost functioned as a proving ground.

Howard's most powerful insight is about **sustained effort over ignorance of difficulty**: he explicitly states that if he had known move semantics would take a decade to standardize, "I probably never would've started the effort." This ignorance was actually an advantage, allowing him to "sprint forward with it and work on it for the love of working on it." The principle generalizes: major standardization efforts require champions who don't fully appreciate how hard it will be.

He also articulates the dual nature of standardization difficulty: "It's both a good thing and a bad thing. It's bad because it's hard to get something standardized... On the other hand, everybody thinks they've got a great idea and not everybody does." The high bar prevents garbage accumulation but also discourages potentially valuable contributions. His experience chairing LWG from 2005-2010 through C++11's development gives him authority on this balance.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Boost Was Created to Solve the Field Experience Problem

> *"Beman would be the protagonist, I guess. He saw a need. We need libraries with field experience before they get standardized. 'Cause standardizing a library without field experience is a huge risk."*

**The Principle**: Beman Dawes created Boost specifically to address the gap between proposed libraries and field-tested libraries; standardizing without real-world validation is gambling with the standard's quality.

**Why It Matters**: Before Boost, there was no ecosystem for creating widely-used, peer-reviewed C++ libraries that could become standardization candidates. Beman foresaw that the standards committee needed a proving ground.

**When to Apply**: When evaluating any library proposal's field experience claims; when understanding Boost's historical purpose.

**Red Flags**:
- Proposal has no public implementation for users to try
- "Field experience" limited to proposer's organization
- Library created specifically for standardization without prior use

**Supporting Experiences**: E1, E2

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: evaluation/field-experience
applies-to: library
confidence: high
supported-by: [E1, E2]
related-principles: [P2]
-->

---

### P2: C++11 Was Boost's Validation Moment

> *"The 2011 standard incorporated a lot of things from Boost. And so that's approximately a decade after Boost was created... that's a point where you could say, this was worth it. This was a success."*

**The Principle**: C++11's extensive incorporation of Boost libraries validated the entire Boost experiment; the decade between Boost's founding and C++11 was the maturation period required to produce standardization-ready libraries.

**Why It Matters**: Success took a decade. Expectations of faster standardization pathways may be unrealistic. The Boost model worked, but on a timeline that required sustained commitment.

**When to Apply**: When setting expectations for library standardization timelines; when evaluating claims about faster paths to standardization.

**Red Flags**:
- Expectation that new proving ground will produce standardization candidates quickly
- Impatience with multi-year development cycles
- Assuming technical quality alone determines standardization timeline

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: history/successes
applies-to: library
confidence: high
supported-by: [E2]
related-principles: [P1, P3]
-->

---

### P3: Major Standardization Efforts Require Naive Champions

> *"It took a decade to get it standardized. And I'm glad I didn't know that going into it. If I'd known how much work it would be to standardize it, I probably never would've started the effort."*

**The Principle**: Champions of major standardization efforts often succeed precisely because they underestimate the difficulty; full awareness of the challenge might prevent valuable contributions from ever beginning.

**Why It Matters**: Move semantics transformed C++ and Howard was "25 years younger" when he started. The combination of youth, energy, and blissful ignorance enabled a decade of sustained effort. Experienced people who "know better" might not even try.

**When to Apply**: When mentoring potential proposal authors; when evaluating why certain proposals get championed and others don't.

**Red Flags**:
- Champion accurately assessing 10-year timeline upfront (may give up)
- Only experienced committee members proposing features (survivor bias)
- Young/naive champions being discouraged by timeline warnings

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: tacit
category: process/navigation
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: [P4]
-->

---

### P4: The High Standardization Bar Is Both Bug and Feature

> *"It's very difficult to get something standardized, and that is a double-edged sword. It's both a good thing and a bad thing... the bar should be very high to get a library or a language standardized."*

**The Principle**: Standardization difficulty filters out bad proposals but also discourages good ones; this tradeoff is inherent and cannot be fully optimized.

**Why It Matters**: Howard experienced both sides: about half his attempts to standardize features failed. The filter is imperfect but necessary—"everybody thinks they've got a great idea and not everybody does."

**When to Apply**: When evaluating process reform proposals; when consoling failed proposal authors.

**Red Flags**:
- Proposals to dramatically lower standardization bar
- Assuming failed proposals were all bad (some good ones fail too)
- Assuming successful proposals were all good (committee makes mistakes)

**Supporting Experiences**: E3, E4

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E3, E4]
related-principles: [P3]
-->

---

### P5: Peter Dimov's Remote Standardization Is Anomalous

> *"Peter Dimov is one of the only person I can think of who has succeeded in standardizing things without ever showing up to a meeting... I have no clue because I could not do it."*

**The Principle**: Remote standardization success (without meeting attendance) is extremely rare; most successful proposals require years of in-person advocacy and argument.

**Why It Matters**: Shared pointer was "a shoe in for standardization" partly because Peter Dimov made it "better than everybody else's" and then "even better than that" through Boost field experience. But even Howard, an LWG chair, says "about half the times I tried to do that, I did not succeed" despite attending meetings regularly.

**When to Apply**: When advising potential proposal authors on required commitment; when understanding Peter Dimov's unique contribution.

**Red Flags**:
- Assuming technical quality alone will drive standardization
- Expecting remote participation to be sufficient
- Underestimating in-person advocacy requirements

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/navigation
applies-to: library
confidence: high
supported-by: [E5]
related-principles: [P3, P4]
-->

---

### P6: LWG Chair Is a Burnout Position

> *"Five, the reason five years was a good suggestion for the term of chair of library chair is because it's a position that at least in my experience, will burn you out. And it did."*

**The Principle**: The Library Working Group chair position is demanding enough to cause burnout; five-year terms exist to protect chairs from themselves.

**Why It Matters**: Beman told Howard "this is a five year term. You need to give it up after five years." This institutional knowledge (if still followed) explains chair transitions and should inform expectations of chair availability.

**When to Apply**: When interacting with LWG chairs; when considering chair succession; when evaluating governance structures.

**Red Flags**:
- Chairs serving much longer than 5 years (burnout risk)
- Expectations of unlimited chair availability
- Lack of succession planning

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: groups/lwg
applies-to: library
confidence: high
supported-by: [E4]
related-principles: []
-->

---

### P7: Boost's Review Process Rivals Standardization Difficulty

> *"I would not be surprised if somebody told me that it's just as hard to get a library into Boost as it is to get one standardized. There's a high bar there as well."*

**The Principle**: Boost's acceptance process is rigorous enough to be comparable to standardization; this is known to the standards committee and increases trust in Boost libraries.

**Why It Matters**: "The standards committee is inclined to look favorably on Boost libraries" precisely because of this rigor. The Boost review process is not merely a stepping stone but a significant achievement in itself.

**When to Apply**: When evaluating Boost library proposals for standardization; when setting expectations for Boost acceptance.

**Red Flags**:
- Treating Boost acceptance as merely preliminary
- Expecting easy Boost acceptance for novel libraries
- Assuming standardization is the only meaningful bar

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: evaluation/field-experience
applies-to: library
confidence: medium
supported-by: [E2]
related-principles: [P1, P4]
-->

---

### P8: Companies Use Boost as Compliance Proxy

> *"On so many Stack Overflow questions I see people will say, if I offer them, say my library to solve a problem, I often get responses like, sorry, but I have to use only Boost."*

**The Principle**: Many organizations permit only Boost as external C++ library source; Boost's reputation serves as compliance proxy for quality and legal review.

**Why It Matters**: This corporate trust explains Boost's continued relevance even as GitHub made library distribution trivial. Companies trust Boost's process more than individual library quality assessment.

**When to Apply**: When understanding Boost's value proposition; when evaluating alternative library distribution approaches.

**Red Flags**:
- Alternative library ecosystems without comparable review rigor
- Assuming individual library quality will overcome corporate restrictions
- Underestimating legal/compliance barriers to library adoption

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P8
source-type: tacit
category: belongs/ecosystem
applies-to: library
confidence: medium
supported-by: [E6]
related-principles: [P7]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: First Hearing About Boost from Beman

**Context**: Howard was attending C++ standards meetings in the late 1990s, having just become MetroWorks' standard library implementer.

**What Happened**: "Beman had an after hour session at one of the standards committee meetings to let people know about his project. And that's when I first heard about Boost." Howard was "thrilled to meet him and be mentored by him" as Beman was "recognized expert, very well respected by everyone."

**The Outcome**: Howard became "Boost adjacent," contributing to Type Traits and later Chrono, even though he wasn't a core Boost contributor.

**The Lesson**: Boost's founding was intimately connected to the standards community; Beman recruited from within WG21 attendees who understood the standardization gap.

> *"I agreed with his premise that we needed someplace to field test C++ libraries before standardization. And this seemed ideal."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/decisions
applies-to: library
outcome: success
features: [boost-founding]
supports: [P1]
-->

---

### E2: C++11 as Boost Validation

**Context**: Boost was created around 1998-1999. The first major C++ standard revision was 2011—approximately a decade later.

**What Happened**: "Several Boost libraries were standardized at that time. And I think that's a point where you could say, this was worth it. This was a success." Howard credits shared pointer, regex, unordered containers, and other libraries as coming from Boost.

**The Outcome**: Success. "I would say that Boost was a giant success for the 2011 standard."

**The Lesson**: Boost's model required a decade to mature. The long gap between C++03 and C++11 (8 years) may have actually helped by allowing more Boost libraries to accumulate field experience.

> *"There was an extremely long time between standards between 2003, 2011, that's what, eight years... that's one of the reasons so many libraries were standardized."*

**Supports Principles**: P1, P2, P7

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [C++11, shared_ptr, regex, unordered-containers]
supports: [P1, P2, P7]
-->

---

### E3: Move Semantics Decade

**Context**: Howard started working on move semantics in 2001 because "Vector was too slow" and he wanted his MetroWorks implementation to be competitive.

**What Happened**: "It took a decade to get it standardized. And I'm glad I didn't know that going into it." He was "20 years younger... 25, 25 years younger" and could "sprint forward with it and work on it for the love of working on it without worrying so much about how long it was going to take."

**The Outcome**: Success. Move semantics "made code 10 times faster, even a hundred times faster" in specific cases and became one of C++11's defining features.

**The Lesson**: Youth, energy, and ignorance of difficulty enabled the sustained effort required. Accurate forecasting might have prevented the attempt.

> *"The fact that I didn't know how hard it would be was an advantage to myself."*

**Supports Principles**: P3, P4

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [move-semantics, unique_ptr]
supports: [P3, P4]
-->

---

### E4: LWG Chair Burnout

**Context**: Howard became LWG chair in 2005 and served through 2010, handing off to Alisdair Meredith before C++11's final publication.

**What Happened**: "I was thrilled to give Alisdair or anyone the chair in 2010 or starting in 2011. And I was not disappointed at all that I was not chair when the 2011 standard was shipped." Beman had advised the 5-year term limit "because it's a position that will burn you out. And it did."

**The Outcome**: Successful transition. Howard remained involved but at reduced intensity, contributing to move semantics advocacy even while no longer chairing.

**The Lesson**: Leadership burnout is predictable and should be planned for. The 5-year convention protects both the individual and the organization.

> *"I was very excited to see a lot of my personal pet projects go in, such as Move Semantics, Unique Pointer, Chrono."*

**Supports Principles**: P4, P6

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: groups/lwg
applies-to: library
outcome: success
features: [LWG-chair, C++11]
supports: [P4, P6]
-->

---

### E5: Peter Dimov's Remote Standardization

**Context**: Peter Dimov authored Boost.SharedPtr and contributed significantly to Boost, but never attended standards meetings.

**What Happened**: "Peter Dimov is one of the only person I can think of who has succeeded in standardizing things without ever showing up to a meeting." His shared pointer "was just better than everybody else's. It was harder for it to have errors with runtime errors. It could do more things than everybody else's shared pointer. It was just bulletproof."

**The Outcome**: Success. Shared pointer was "a shoe in for standardization in 2011. I'm not sure, but I think we may have taken that one without any changes at all besides wordsmithing."

**The Lesson**: Exceptional technical quality can sometimes substitute for in-person advocacy, but this is rare. Howard explicitly says "I have no clue" how Peter did it and "I could not do it" despite being LWG chair.

> *"I have never met him, but I've talked with him many times on email... Peter, if you're out there, please come on."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [shared_ptr, Peter-Dimov]
supports: [P5]
-->

---

### E6: "Sorry, I Have to Use Only Boost"

**Context**: Howard answers Stack Overflow questions and recommends libraries.

**What Happened**: "On so many Stack Overflow questions I see people will say, if I offer them, say my library to solve a problem, I often get responses like, sorry, but I have to use only Boost."

**The Outcome**: Observation about corporate constraints. Companies use Boost as a compliance proxy.

**The Lesson**: Boost's reputation creates real-world adoption advantages that individual libraries can't easily replicate.

> *"That speaks highly of Boost Libraries."*

**Supports Principles**: P8

<!-- METADATA
kind: experience
id: E6
source-type: tacit
category: belongs/ecosystem
applies-to: library
outcome: mixed
features: [boost-adoption]
supports: [P8]
-->

---

### E7: Chrono's Origin Outside Boost

**Context**: Howard and Jeff Garland were working on threading standardization, which needed timing services.

**What Happened**: "I didn't put Chrono into Boost. I am the author of the Chrono Library along with Jeff Garland and several other people. We worked on it quite extensively, but we worked on it outside of Boost and for the purpose of standardization in C++, and somebody else moved it into Boost with my permission."

**The Outcome**: Success. Chrono was standardized in C++11 with "just durations and time points and a couple of clocks" and has since been "greatly expanded" to include calendars and time zones.

**The Lesson**: Not all successful C++11 libraries came through Boost's standard process. Some were developed specifically for standardization with Boost as a secondary publication venue.

> *"LWG really did not want to standardize something and regret it later. It's much easier to add things later, and it's very difficult to take things out of the standard."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [chrono, threading]
supports: [P1]
-->

---

### E8: Vinnie Falco Recruitment

**Context**: Howard was at Apple in 2013-2014 when Ripple (then a tiny cryptocurrency startup) was looking for C++ expertise.

**What Happened**: "Vinnie Falco first called me probably late in 2013 and asked me if I'd be interested in working for Ripple... I probably told him at the time that I was only available for remote work. And he told me that would not be a problem."

**The Outcome**: Howard joined Ripple and worked there for over 10 years until retirement in 2024. "Ripple was very good to me."

**The Lesson**: Remote work enabled a career-changing opportunity. Vinnie's willingness to accommodate remote work was decisive.

> *"Vinnie is very outgoing, not afraid to say what he thinks... enthusiastic about everything he's doing. He never does anything halfway."*

**Supports Principles**: (No direct principle—provides context on C++ Alliance origins)

<!-- METADATA
kind: experience
id: E8
source-type: explicit
category: history/decisions
applies-to: both
outcome: success
features: [ripple, vinnie-falco]
supports: []
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Evaluating Library Proposals

- [ ] Does the library have field experience from users outside the proposer's organization? (P1)
- [ ] Has the library been available for multiple years? (P2)
- [ ] Is there a champion willing to sustain multi-year effort? (P3)
- [ ] Does the proposal meet the high bar of significance? (P4)

**Questions to Ask**:
1. "Where has this been deployed, and what was user feedback?" (P1)
2. "How long has this implementation been available?" (P2)
3. "Who will champion this through the full process?" (P3)
4. "Is this sufficiently important to justify standardization overhead?" (P4)

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P1, P2, P3, P4]
-->

---

### When Mentoring Proposal Authors

- [ ] Avoid discouraging with accurate timeline warnings (P3)
- [ ] Prepare them for in-person advocacy requirements (P5)
- [ ] Set realistic expectations about success rates (~50% for experienced authors) (P4)
- [ ] Emphasize Boost acceptance as significant achievement (P7)

**Questions to Ask**:
1. "Are you prepared for a multi-year effort?" (P3)
2. "Can you attend meetings regularly?" (P5)
3. "Have you considered Boost submission first?" (P7)

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: feature
derived-from: [P3, P4, P5, P7]
-->

---

## Open Questions

1. **What were the details of the threading cancellation debate?** Howard describes two camps but doesn't name individuals or explain why consensus was impossible.

2. **Why did concepts fail for C++11?** Howard mentions hearing "through the walls" about a saga but wasn't involved and doesn't know details.

3. **What is Peter Dimov's perspective?** Howard has never met him and explicitly requests his participation: "Peter, if you're out there, please come on."

4. **What specific Boost libraries has Howard used at Ripple?** He mentions Beast but notes confusion about which utilities were in Beast vs. other Ripple code.

5. **What is Howard's view on the current LWG structure?** He mentions that LWG has split into multiple groups (Evolution, Wording, Incubation) but hasn't followed closely.

---

## Raw Transcript Reference

Source: `inputs/howard-hinnant-2.md`  
Video: https://vimeo.com/1158488358/9e7c53922b
