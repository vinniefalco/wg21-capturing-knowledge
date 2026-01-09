# Sean Parent: Captured Knowledge

**Interview Date**: 2025-12-10
**Interviewer**: Ray Nowosielski
**Duration**: ~46 minutes
**Topics Covered**: Boost history, C++ standardization, library licensing, Adobe's use of Boost, generic programming, meta-programming critique, C++ complexity crisis, memory safety, standards committee dysfunction, university-industry collaboration

## Executive Summary

Sean Parent, a senior principal scientist at Adobe with deep roots in both Apple and Adobe's foundational C++ work, provides a sweeping historical perspective on Boost's role in sustaining C++ during its "lost decade" (1998-2011) and its influence on modern standardization. His most striking contribution is framing C++ as a "Shakespearean tragedy" where the language's virtues (performance, expressiveness) have been undermined by accumulated complexity and institutional failures.

Parent offers crucial insider knowledge on how Boost achieved commercial adoption through licensing reform, the political dynamics that can derail even technically sound proposals (the Concepts C++ debacle), and the standards committee's systemic failure to document rationale for decisions. His perspective is particularly valuable because he bridges academia (through connections to Stepanov, Lumsdaine's team) and industry (Adobe, Google, Apple), and has directly witnessed how libraries succeed or fail in production environments.

Most actionable is his diagnosis of the standards committee's dysfunction: decisions made in isolation without documented rationale lead to inconsistency and complexity. His prescription—that Boost could again catalyze language evolution by demonstrating what libraries could achieve with safety features—offers a concrete path forward.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Libraries Preserve Languages During Standardization Stagnation

> *"Boost... Kept the language alive, uh, and then turned into the foundation for features for C++ 11... I think C++ in some sense, you know, would've greatly diminished during that time period. Just from stagnation."*

**The Principle**: When language standardization stalls, high-quality open-source libraries can sustain a language ecosystem and seed future language evolution.

**Why It Matters**: The 13-year gap between C++98 and C++11 could have killed C++. Boost filled that gap by providing modern facilities (smart pointers, function objects, lambdas via library) that kept practitioners productive and demonstrated what the language could become. This pattern can repeat.

**When to Apply**: 
- When evaluating whether to invest in library development vs. waiting for language features
- When assessing the strategic value of library ecosystems to language health
- When a language appears stagnant but has an active library community

**Red Flags**:
- Dismissing library efforts as "workarounds" rather than recognizing their strategic value
- Assuming language features will arrive in time to meet practitioner needs
- Undervaluing the feedback loop from library experience to language design

**Supporting Experiences**: E1, E3

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: history/successes
applies-to: both
confidence: high
supported-by: [E1, E3]
related-principles: [P7]
-->

---

### P2: Commercial Adoption Requires License Simplification

> *"In the early days of Boost, Boost didn't have a single license. So contributors to Boost were putting their code under their own license... there were over a hundred licenses inside of the Boost Libraries. So I had to get that all vetted by our legal department here before we could get sign off."*

**The Principle**: Open source projects targeting commercial adoption must consolidate to a single, commercially-friendly license; fragmented licensing creates prohibitive friction for legal review.

**Why It Matters**: Even technically excellent libraries won't achieve broad industry adoption if legal teams must review hundreds of individual licenses. Adobe was an early Boost adopter specifically because Parent drove license consolidation. The Boost Software License became a model for other projects.

**When to Apply**:
- When starting a new open source project intended for commercial use
- When evaluating why adoption of a technically sound library is lagging
- When advising projects on governance and contribution policies

**Red Flags**:
- Multiple licenses within a single project
- Licenses requiring attribution in product UI ("scrolling credits")
- Viral licenses that require derivative works to be open-sourced
- Licenses without clear origin/indemnification language
- "No guarantees" language without IP warranty

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: process/navigation
applies-to: library
confidence: high
supported-by: [E2]
related-principles: []
-->

---

### P3: The Standard Library Should Exemplify Good Practice

> *"The standard library, in my opinion, should be an example of how developers should write their code. And so if your example for how to write a pair of two values is 2000 lines of code, uh, the complexity is more than most reasonable developers can digest."*

**The Principle**: Standard library implementations should be readable exemplars of good practice, not baroque monuments to optimization; when the canonical implementation of a trivial type requires 2000 lines, the language has failed pedagogically.

**Why It Matters**: Developers learn idioms from standard library code. When `std::pair`—conceptually the simplest possible composite type—requires thousands of lines of template machinery, it signals that "proper" C++ is inaccessible to ordinary practitioners. This drives talent away and entrenches complexity.

**When to Apply**:
- When evaluating library proposals: will the implementation be comprehensible?
- When designing vocabulary types: can the implementation fit in a developer's head?
- When assessing language feature proposals: will they simplify or complicate library implementations?

**Red Flags**:
- Proposals where the "reference implementation" is incomprehensible
- Vocabulary types requiring extensive metaprogramming
- Optimizations that obscure the fundamental design
- Implementations that require deep template expertise to understand

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E4]
related-principles: [P5]
-->

---

### P4: Document Decision Rationale to Ensure Consistency

> *"The biggest problem with the standards committee is an unwillingness to specify what the goals are and basically what the rules are... every decision that the standards committee tends to make tends to almost be made in isolation. And they don't then document the rationale for that decision. And so when a similar decision is made, they may come up with a different answer."*

**The Principle**: Standards bodies must document the rationale for each decision and maintain explicit design principles; without this, similar questions get inconsistent answers, creating incoherent languages.

**Why It Matters**: C++'s accumulated "warts" stem not from individual bad decisions but from the lack of a framework ensuring consistency across decisions. When each proposal is evaluated ad hoc, the language accretes contradictions. This is the root cause of C++'s complexity crisis.

**When to Apply**:
- When proposing features: explicitly reference relevant precedents and principles
- When evaluating proposals: ask what precedent this sets and whether it's consistent with prior decisions
- When participating in standards work: push for documented design rationale

**Red Flags**:
- Proposals justified purely on technical merit without reference to design principles
- Decisions that contradict prior committee positions without explicit rationale
- New types that don't follow established patterns (e.g., non-regular types without justification)
- "We'll make an exception this time" reasoning

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P6]
-->

---

### P5: Meta-Programming Is Implementation Detail, Not Interface

> *"He's the person who started this notion of meta programming in order to implement STL. But he will tell you, generic programming has nothing to do with meta programming. It was a hack so he could implement generic programming, and it kind of became the thing in boost."*

**The Principle**: Meta-programming should be an implementation technique for library authors, not an exposed interface or programming paradigm promoted to users; it was always a workaround, not a goal.

**Why It Matters**: Boost's emphasis on meta-programming (MPL, type traits, SFINAE tricks) impressed experts but alienated practitioners. The original intent—enabling generic programming—got lost when the scaffolding became the showcase. This contributed to C++'s reputation for impenetrability.

**When to Apply**:
- When designing libraries: hide metaprogramming behind clean interfaces
- When evaluating library proposals: is the user-facing API clean, regardless of implementation complexity?
- When assessing Boost's historical impact: distinguish the elegant results (boost::function, boost::any) from the complex machinery

**Red Flags**:
- Libraries that expose metaprogramming concepts in their public API
- Proposals whose usage examples require template metaprogramming knowledge
- Documentation that emphasizes implementation techniques over use cases
- "Look how clever this is" design motivation

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P5
source-type: tacit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E3]
related-principles: [P3]
-->

---

### P6: Require Regularity for New Types

> *"Even what I would consider basic things like saying, you know, all new types within the language should be regular, uh, doesn't happen and doesn't get held up."*

**The Principle**: All new standard types should be regular (copyable, equality-comparable, with copies being equal) unless there is explicit, documented justification for deviation.

**Why It Matters**: Regular types compose predictably; irregular types require special handling that propagates complexity through all code that touches them. Without a regularity requirement, the standard accumulates types with inconsistent semantics, making generic programming harder.

**When to Apply**:
- When designing new types: start with regularity as the default
- When evaluating type proposals: demand explicit justification for non-regular semantics
- When reviewing library designs: check that types follow consistent semantic patterns

**Red Flags**:
- Types that are movable but not copyable without clear resource semantics
- Types where copies aren't equal
- Types with implicit/surprising special member behavior
- Proposals that don't address regularity explicitly

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/library
applies-to: library
confidence: high
supported-by: [E5]
related-principles: [P4]
-->

---

### P7: Libraries Can Demonstrate Language Feature Viability

> *"I think if there was more effort in Boost to say this is what a standard SIMD library should look like... Boost could look at what would a common C++ standard language support look like for GPUs... If they could demonstrate that and then come up with language proposals... I think that could have huge influence."*

**The Principle**: Libraries that demonstrate what's achievable with hypothetical language features can drive language evolution; showing "if we had X, we could do Y" is more persuasive than abstract proposals.

**Why It Matters**: The committee responds better to demonstrated capability than theoretical arguments. Boost proved this with C++11 (lambdas, variadic templates, smart pointers all had Boost precursors). The same approach could work for safety features, SIMD, and GPU support.

**When to Apply**:
- When advocating for language features: build a library that shows the benefit
- When Boost/similar organizations consider strategic direction: identify high-impact gaps
- When evaluating the feasibility of language extensions: look for library-based existence proofs

**Red Flags**:
- Language proposals without implementation experience
- Features justified purely theoretically
- Libraries that can't articulate what language support would improve them
- Dismissing library workarounds without proposing better alternatives

**Supporting Experiences**: E1, E3

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1, E3]
related-principles: [P1]
-->

---

### P8: University Partnerships Drive Innovation

> *"A lot of what I see that was driven in the early days of Boost came out of universities. A lot of it came out of Andrew Lumsdaine's team at Indiana University... Boost establishing strong connections with one or more universities could play a pivotal role."*

**The Principle**: Foundational library and language innovations often emerge from university research groups; open source projects should cultivate academic partnerships to access "young research focused DNA."

**Why It Matters**: The Boost Graph Library, Concept C++, and much foundational generic programming work came from Indiana University's team. Universities provide researchers with time for deep problems and students with fresh perspectives. Industry alone tends toward incremental improvement.

**When to Apply**:
- When Boost/similar projects consider governance: ensure academic representation
- When identifying future contributors: look at research groups
- When planning ambitious library projects: consider academic partnerships

**Red Flags**:
- Open source projects entirely driven by industry practitioners
- Lack of connection to academic programming languages/SE research
- Dismissing academic work as "impractical"
- No pathway for research ideas to enter the library ecosystem

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/navigation
applies-to: both
confidence: medium
supported-by: [E6]
related-principles: []
-->

---

### P9: Political Deadlock Kills Good Proposals

> *"It was a very political decision. There was a competing proposal... from Stroustrup's team, and they couldn't reach consensus on the two. The end result was both of them got pulled from the standards and neither went in."*

**The Principle**: When competing proposals from prominent figures reach deadlock, the committee often rejects both rather than choosing; technical merit alone doesn't determine outcomes.

**Why It Matters**: Doug Gregor's Concepts C++ was technically sound and implemented, but political dynamics with a competing proposal led to total rejection. Contributors must understand that technical quality is necessary but not sufficient; coalition building and timing matter.

**When to Apply**:
- When multiple proposals address the same problem: seek synthesis early
- When prominent figures are involved: be attentive to political dynamics
- When a proposal faces competition: don't assume technical superiority wins

**Red Flags**:
- Competing proposals from different "camps" with entrenched positions
- Unwillingness to merge or synthesize competing approaches
- Technical debates that become proxies for personal/institutional rivalries
- Votes scheduled while fundamental disagreements remain unresolved

**Supporting Experiences**: E6

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: process/politics
applies-to: both
confidence: high
supported-by: [E6]
related-principles: [P4]
-->

---

### P10: C++ Is Leaving Performance on the Table

> *"If you're looking at just single threaded C++ running on a CPU, you're only able to use about 0.25% of the machine because most of the performance of the machine is locked up in the GPU and in the SIMD units. And C++ doesn't have a standard way to access those."*

**The Principle**: The standards committee has over-focused on micro-optimizations (squeeze cycles from function calls) while ignoring macro-optimizations (GPU, SIMD, proper threading); this leaves 99%+ of modern hardware performance inaccessible through standard C++.

**Why It Matters**: C++ justifies its complexity through performance, but standard C++ can't access the majority of modern hardware capability. This undermines the language's core value proposition and creates an existential threat as other languages (with better hardware abstractions) mature.

**When to Apply**:
- When evaluating the strategic direction of C++ standardization
- When prioritizing library/language work: hardware access > micro-optimization
- When assessing C++ vs. alternatives for new projects

**Red Flags**:
- Proposals focused on saving cycles in sequential code
- Language features adding complexity for marginal single-threaded gains
- Ignoring GPU/SIMD/heterogeneous computing in standards roadmaps
- Threading primitives that encourage oversubscription

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P3]
-->

---

### P11: Standardized Components Become Migration Burdens

> *"If you talk to a lot of companies right now, they will say one issue that they have is now that large portions of boost have been standardized, they would like to be able to migrate to the standard versions. And in some cases that can be very hard."*

**The Principle**: When library components are standardized, migration from the original library to the standard version creates significant organizational burden; standardization success creates legacy problems.

**Why It Matters**: Boost's success means organizations now face "boost removal" as a project—the library became synonymous with "legacy stuff that must be removed." This is an ironic consequence of success, but it affects how organizations perceive Boost's ongoing value.

**When to Apply**:
- When designing libraries intended for standardization: consider migration paths
- When standardizing existing library functionality: ensure compatibility or clear migration
- When evaluating Boost's current reputation: distinguish legacy standardized parts from ongoing value

**Red Flags**:
- Standardized versions with gratuitously different interfaces
- No migration tooling or guidance when standardizing
- Organizations conflating "standardized Boost components" with "all of Boost"

**Supporting Experiences**: E7

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: history/evolution
applies-to: library
confidence: medium
supported-by: [E7]
related-principles: [P1]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Boost Bridged the Lost Decade

**Context**: C++ had C++98, then only a minor defect fix (C++03), with no major release until C++11—a 13-year gap during which the language risked obsolescence through stagnation.

**What Happened**: The Boost Libraries emerged during this period, building on Stepanov's STL ideas. Contributors found ways to exploit template mechanisms to create useful facilities (smart pointers, function wrappers, lambdas-via-library). These libraries kept practitioners productive and demonstrated what C++ could become.

**The Outcome**: Success. Boost kept C++ relevant during stagnation, and many Boost innovations (variadic templates, lambdas, smart pointers, threading) became C++11 features. The language emerged from its lost decade stronger.

**The Lesson**: Library ecosystems can sustain languages through standardization gaps and seed future evolution. Boost's role was existential, not merely convenient.

> *"Boost... Kept the language alive, uh, and then turned into the foundation for features for C++ 11 and beyond... I think C++ in some sense would've greatly diminished during that time period just from stagnation."*

**Supports Principles**: P1, P7

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: both
outcome: success
features: [boost, C++11, variadic-templates, lambdas]
supports: [P1, P7]
-->

---

### E2: The Hundred-License Problem

**Context**: Early Boost had no unified license. Each contributor used their own license terms, resulting in over 100 different licenses within the library collection.

**What Happened**: Parent wanted Adobe to adopt Boost as its first approved open-source dependency. He had to get every single license reviewed by Adobe Legal. This was enormously time-consuming. Parent then pushed Dave Abrahams to establish a single Boost license. Abrahams worked with lawyers to draft what became the Boost Software License, with Parent providing feedback from Adobe Legal to ensure commercial acceptability.

**The Outcome**: Success. The Boost Software License enabled broad commercial adoption. Adobe became an early adopter, legitimizing Boost for enterprise use. The license became a model for other projects.

**The Lesson**: License fragmentation kills commercial adoption even for technically excellent libraries. A single, commercially-friendly license removes friction that legal departments otherwise use to say "no."

> *"In the early days of Boost, Boost didn't have a single license... there were over a hundred licenses inside of the Boost Libraries. So I had to get that all vetted by our legal department."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [boost-license, open-source-licensing]
supports: [P2]
-->

---

### E3: The Boost Graph Library as Existence Proof

**Context**: Stepanov created STL as an example of generic programming, hoping others would extend the approach to different domains. The Boost Graph Library (BGL), by Jeremy Siek, Doug Gregor, and Andrew Lumsdaine, applied these ideas to graph algorithms.

**What Happened**: The BGL team took STL's approach—separating algorithms from data structures through concepts—and applied it to graphs. This required sophisticated template machinery but produced an elegant, reusable graph algorithm library. It proved that generic programming could extend beyond sequences.

**The Outcome**: Success. BGL became a "stellar example" of taking generic programming into new domains, validating Stepanov's vision. However, its implementation complexity also exemplified the metaprogramming that would become both Boost's strength and its criticism.

**The Lesson**: Libraries can demonstrate that programming paradigms work in new domains, but the implementation complexity required to achieve this may become the public face of the paradigm.

> *"The boost graph library is just a phenomenal piece of work... the one example that we have of using what Alex did with STL and generic programming as an example of doing something in a different domain."*

**Supports Principles**: P1, P5, P7

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: history/successes
applies-to: library
outcome: success
features: [boost-graph-library, generic-programming]
supports: [P1, P5, P7]
-->

---

### E4: The 2000-Line std::pair

**Context**: Parent was preparing his "Tragedy of C++" keynote and examining the complexity of the C++ standard library.

**What Happened**: He examined the implementation of `std::pair`—conceptually, just two values together. The standard library implementation was approximately 2000 lines of code, filled with template machinery for optimization and special cases.

**The Outcome**: Failure (pedagogically). The implementation that should exemplify "how to write a pair" is incomprehensible to ordinary developers. This became Parent's central example of C++ complexity crisis.

**The Lesson**: When the canonical implementation of the simplest possible composite type requires thousands of lines, the language has made "correct" code inaccessible. The complexity tax accumulated in "simple" library components makes the entire ecosystem feel hostile.

> *"std::pair within the standard library is something close to 2000 lines of code. It's ridiculous... if your example for how to write a pair of two values is 2000 lines of code, the complexity is more than most reasonable developers can digest."*

**Supports Principles**: P3, P10

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: history/failures
applies-to: library
outcome: failure
features: [std-pair, complexity]
supports: [P3, P10]
-->

---

### E5: The Missing Design Principles

**Context**: Parent was analyzing why C++ has accumulated so many inconsistencies and "warts" over its evolution.

**What Happened**: He observed that the standards committee makes decisions in isolation without documenting rationale. When similar questions arise later, there's no record of why previous decisions were made, leading to different (often contradictory) answers. Even basic principles like "new types should be regular" aren't consistently applied because they aren't formally established.

**The Outcome**: Failure (ongoing). C++ has accumulated inconsistent semantics across types, surprising special cases, and design contradictions that can't be unwound without breaking compatibility.

**The Lesson**: Institutional knowledge requires explicit documentation. Without recorded rationale and design principles, standards bodies make inconsistent decisions that compound into language incoherence.

> *"Every decision that the standards committee tends to make tends to almost be made in isolation. And they don't then document the rationale for that decision. And so when a similar decision is made, they may come up with a different answer."*

**Supports Principles**: P4, P6

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: history/failures
applies-to: both
outcome: failure
features: [standards-committee, design-principles]
supports: [P4, P6]
-->

---

### E6: The Concepts C++ Rejection

**Context**: Doug Gregor, from Andrew Lumsdaine's team at Indiana University, developed Concepts C++—a major language feature for constrained templates. He built both the design and a working implementation.

**What Happened**: A competing proposal came from Stroustrup's team. The two camps couldn't reach consensus. Rather than choose between them or force synthesis, the standards committee rejected both proposals. Neither went into C++11.

**The Outcome**: Failure. Doug Gregor, having invested enormous personal effort, was devastated. He left C++ work and channeled his ideas into Swift's protocol system, where they proved highly successful. C++ eventually got concepts in C++20, a decade later, after much additional effort.

**The Lesson**: Political deadlock between prominent figures can kill technically sound proposals. The committee's conflict-avoidance culture produces outcomes worse than choosing either alternative. Brilliant contributors can be lost to other languages when their work is rejected for political rather than technical reasons.

> *"It was a very political decision... they couldn't reach consensus on the two. The end result was both of them got pulled from the standards and neither went in... I think he wanted to go prove that his work was of high value. And I think he did that in Swift."*

**Supports Principles**: P8, P9

<!-- METADATA
kind: experience
id: E6
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [concepts, swift-protocols, C++11]
supports: [P8, P9]
-->

---

### E7: Boost as "Legacy to Remove"

**Context**: Many Boost libraries were standardized into C++11/14/17/20. Organizations that had adopted Boost now had two implementations of the same functionality.

**What Happened**: Companies wanted to migrate from Boost versions to standard versions, but migration proved difficult in many cases. Boost became associated with "legacy code that must be removed" in organizational discourse, even though significant non-standardized Boost functionality remains valuable.

**The Outcome**: Mixed. Standardization succeeded (Boost's goal), but created perception problems. Boost's reputation became entangled with its standardized (now "legacy") components, obscuring its ongoing value.

**The Lesson**: Successful standardization creates migration burdens. Organizations may conflate "parts we need to migrate away from" with "the entire project." Standardization success can paradoxically harm the originating project's reputation.

> *"Boost becomes almost synonymous in some organizations as legacy stuff that must be removed. But that's not completely true—there are large portions of Boost that are not standardized and are incredibly useful."*

**Supports Principles**: P11

<!-- METADATA
kind: experience
id: E7
source-type: explicit
category: history/evolution
applies-to: library
outcome: mixed
features: [boost, standardization, migration]
supports: [P11]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Library Proposals

- [ ] Is the implementation comprehensible to a skilled but non-expert developer? (P3)
- [ ] Do all new types satisfy regularity requirements? If not, is the deviation explicitly justified? (P6)
- [ ] Is metaprogramming confined to implementation, not exposed in the user API? (P5)
- [ ] Has this approach been prototyped in a library with real users? (P7)
- [ ] Is there a migration path for existing similar libraries? (P11)
- [ ] Does this address macro-level performance (SIMD, GPU, parallelism) rather than micro-optimizations? (P10)

**Questions to Ask**:
1. "Can you show me a usage example that doesn't require template metaprogramming expertise?"
2. "What types does this introduce, and are they all regular? If not, why?"
3. "Is there a Boost/library precursor with field experience?"
4. "How does this fit with prior committee decisions on similar questions? What's the design rationale?"
5. "Will the standard library implementation be readable as an exemplar?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P3, P5, P6, P7, P10, P11]
-->

---

### When Reviewing Language Proposals

- [ ] Is the rationale documented so future decisions can be consistent? (P4)
- [ ] Does this enable simpler library implementations, or does it add complexity? (P3)
- [ ] Is there library-based experience demonstrating the need for this feature? (P7)
- [ ] Does this address hardware access (SIMD, GPU, threading) or just syntax sugar? (P10)
- [ ] Are there competing proposals? If so, has synthesis been attempted? (P9)
- [ ] Does this support or undermine type regularity as a default? (P6)

**Questions to Ask**:
1. "What precedent does this set, and is it consistent with prior committee decisions?"
2. "Is there a library workaround today? What does this feature enable that the library can't achieve?"
3. "Will this simplify or complicate the implementation of std::pair (or equivalent simple types)?"
4. "Are there competing approaches? What would synthesis look like?"
5. "Does this help C++ access modern hardware, or is it micro-optimization?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P3, P4, P6, P7, P9, P10]
-->

---

### When Evaluating Open Source Library Projects for Adoption

- [ ] Is there a single, commercially-friendly license? (P2)
- [ ] Is the license clearly authored with indemnification language? (P2)
- [ ] Are there viral/copyleft provisions that would affect your product? (P2)
- [ ] Are there attribution requirements that would be onerous (UI credits, etc.)? (P2)
- [ ] If components have been standardized, are migration paths clear? (P11)

**Questions to Ask**:
1. "How many distinct licenses exist in this project?"
2. "Does the license require attribution visible to end users?"
3. "Are there viral provisions that affect code using this library?"
4. "What components of this are now in the standard, and how hard is migration?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: adoption
derived-from: [P2, P11]
-->

---

### When Assessing Standards Committee Proposals for Procedural Health

- [ ] Is the design rationale documented, not just the specification? (P4)
- [ ] Does the proposal reference relevant precedents and explain consistency or deviation? (P4)
- [ ] Are competing proposals being synthesized rather than fought? (P9)
- [ ] Is there academic/research input, not just industry practitioners? (P8)
- [ ] Is there field experience from independent users? (P7)

**Questions to Ask**:
1. "What precedent does this create, and where is that documented?"
2. "Are there competing proposals? What's the plan for synthesis?"
3. "Who outside the proposer's organization has used this?"
4. "Is there academic research supporting this approach?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P4, P7, P8, P9]
-->

---

## Open Questions

1. What specific libraries does Parent believe failed due to insufficient field experience? He mentions a "list of libraries where this strategy has failed us" but doesn't enumerate.

2. What happened with the memory safety proposal that was "shot down"? Who proposed it, what did it contain, and what were the objections?

3. What specific "gaps" does Parent see in Rust that prevent it from proving itself "at scale"?

4. What concrete language features would be needed to make library implementations readable again (reversing the 2000-line std::pair problem)?

5. What is Parent's view on Beman vs. Boost governance—should Boost adopt Beman's "start from standards proposal" approach?

6. What are the specific inconsistencies in type regularity across the standard library that Parent finds most problematic?

7. What would "standard GPU support" look like concretely? What has prevented proposals in this area?

8. Why was Dave Sankel a "hard no" regarding something (the interviewer's question that Parent declined to answer on camera)?

9. What was the specific content of Parent's involvement with Adobe Source Libraries, and why did it "bear some resemblance to boost"?

10. What are the "significant gaps" Parent sees in Rust for commercial products?

---

## Raw Transcript Reference

Source: `inputs/sean-parent.md`
Video: https://vimeo.com/1152633745/2a73805542?fl=tl&fe=ec
Filmed: 2025-12-10, San Jose CA
