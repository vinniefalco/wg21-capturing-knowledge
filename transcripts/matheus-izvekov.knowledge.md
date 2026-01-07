# Matheus Izvekov: Captured Knowledge

**Interview Date**: January 7, 2026  
**Interviewer**: Vinnie  
**Duration**: ~71 minutes (9:51 AM – 11:02 AM Pacific)  
**Topics Covered**: Committee process, template implementation expertise, paper navigation, P3310 (template template parameters), overload resolution complexity, library vs language features, trivial relocation, linear algebra standardization, vocabulary types, knowledge preservation

## Executive Summary

Matheus Izvekov brings a rare perspective to WG21: deep compiler implementation expertise in templates, overload resolution, and partial ordering—areas where most original experts have retired or become inactive. His experience reveals a critical gap between how papers pass through EWG (often without deep technical understanding from voters) and the hard realities discovered later in CWG or during implementation.

His central insight is that **high vote counts in EWG do not indicate understanding**. His first paper achieved near-consensus, yet later revealed that voters hadn't truly grasped the implications—a pattern he believes is systemic. This disconnect stems from the separation of experts (concentrated in CWG) from the design phase (EWG), compounded by simultaneous scheduling that prevents cross-pollination.

Matheus also articulates a tension between library and language features: foundational operations like `std::move` pay unnecessary compile-time costs as templates when they could be cheaper and better-diagnosed as language primitives. He warns that the committee's preference for library solutions may be counterproductive when language features would provide a more polished user experience.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: Editorial vs Design Bugs Require Different Processes

> *"There's like what do you mean like when you say like a wording bug, there's two classes or two kinds of major bugs... editorial bugs... and then like problems in the wording where like it looks obviously wrong, but like you can't exactly make the case like people didn't want to say that."*

**The Principle**: Distinguish between editorial bugs (wording doesn't match clear intent—fixable via CWG directly) and design bugs (unclear or unconsidered intent—requires full EWG paper process).

**Why It Matters**: Misclassifying a design bug as editorial can lead to inadequate review. Misclassifying an editorial bug as design creates unnecessary process overhead. Getting this right determines whether a fix takes weeks or years.

**When to Apply**: When evaluating defect reports or proposed fixes to existing standard wording.

**Red Flags**:
- Claiming something is "obviously wrong" without evidence of original intent
- Rushing a design change through as an editorial fix
- Treating clear typos/transcription errors as requiring full EWG review

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: process/formal
applies-to: both
confidence: high
supported-by: [E1]
related-principles: [P2]
-->

---

### P2: Papers That Skip EWG Risk Incomplete Specification

> *"His paper basically somehow... didn't go through EWG, right? It went straight to court and got merged... they realized, oh, like this specification is really lacking here because we allow this extension, then like a bunch of code relies on partial ordering... but then like the paper completely lacked any wording explaining how partial ordering works with that."*

**The Principle**: Features that bypass EWG review risk having incomplete specifications that only surface during implementation, potentially years later.

**Why It Matters**: The P2579/P3310 template template parameter matching saga demonstrates how skipping evolution review led to years of implementation divergence and workarounds. What seemed like a straightforward extension lacked critical partial ordering wording.

**When to Apply**: When evaluating whether a paper needs EWG review, even if it seems like "just a bug fix."

**Red Flags**:
- Paper going directly to CWG without EWG review
- "Type-theoretically correct extension" claims without implementation analysis
- No discussion of interaction with partial ordering, overload resolution, or other complex subsystems
- Retroactive DR application without implementation experience

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: process/navigation
applies-to: language
confidence: high
supported-by: [E2]
related-principles: [P1, P3]
-->

---

### P3: Expertise Is Siloed Between CWG and EWG

> *"CWG have some people that are like fully dedicated to CWG, you know, they like almost never in all the rooms, but they have like evolutionary concerns... a lot of papers, you know, maybe they go through EWG too quickly, you know, they wouldn't have gone, they would have gone like in a better shape to core if some of these people were able to attend EWG sessions."*

**The Principle**: The simultaneous scheduling of CWG and EWG prevents experts from contributing to evolution discussions, causing papers to arrive at CWG in suboptimal shape.

**Why It Matters**: Papers that pass EWG with near-consensus may still have fundamental issues that CWG experts would have caught earlier. The structural separation creates systematic quality gaps.

**When to Apply**: When scheduling paper reviews or when papers receive unanimous EWG approval but authors lack deep implementation expertise.

**Red Flags**:
- Paper author unfamiliar with CWG-style concerns
- No CWG expert feedback before EWG vote
- Complex template/overload resolution interactions not analyzed
- "Everyone voted for it" used as quality evidence

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: explicit
category: groups/ewg
applies-to: language
confidence: high
supported-by: [E3]
related-principles: [P4]
-->

---

### P4: High Vote Counts Do Not Indicate Understanding

> *"My first ever paper to the committee and like there was almost basically unanimous consensus, right? And but but like that didn't mean that like people really, you know, understood what what was going on there and they had some difficulty later because of that."*

**The Principle**: Near-unanimous EWG votes can mask widespread misunderstanding of a paper's implications; consensus indicates political alignment, not technical comprehension.

**Why It Matters**: Authors may overestimate how well their paper was understood based on vote counts. Problems surface later in CWG or during implementation when actual experts engage with the details.

**When to Apply**: After receiving favorable EWG votes on technically complex papers, especially those involving templates, overload resolution, or specification gaps.

**Red Flags**:
- Large vote counts on papers with few questions asked
- Paper title that doesn't fully convey scope of changes
- Voters who couldn't explain the paper's mechanism if asked
- Author surprised by CWG feedback

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P4
source-type: tacit
category: process/politics
applies-to: language
confidence: high
supported-by: [E3]
related-principles: [P3]
-->

---

### P5: Templates Lack Meaningful Type Checking

> *"How easily, you know, like you can write a template, you know, like that's not really correct, you know, like for all, you know, inputs... and how, you know like not really feasible, or like really would be like really a challenge to like really improve the language to the point where, you know, that that's not an issue anymore... concepts don't really give you that."*

**The Principle**: The compiler cannot verify template correctness for all instantiations; concepts help at call sites but don't provide definition-side checking. Users should minimize template usage accordingly.

**Why It Matters**: Templates are expensive to compile, hard to debug, and can silently be incorrect for untested type arguments. The language fundamentally cannot provide the safety guarantees users might expect.

**When to Apply**: When designing APIs or evaluating proposals that rely heavily on templates.

**Red Flags**:
- Templates used where non-template solutions exist
- Assumption that "it compiles" means "it's correct for all types"
- Over-reliance on concepts as a correctness guarantee
- Heavy template usage without compile-time cost analysis

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: philosophy/language
applies-to: language
confidence: high
supported-by: [E3]
related-principles: [P6]
-->

---

### P6: Overload Resolution Is Too Complex for Safe Reliance

> *"The rules for overall resolution, they really complicated and no one like really understands them fully, right? Like not even in the committee... people are avoiding, you know, like overload resolution, they, you know, like making the cases where they are at least making where they allowed more restricted."*

**The Principle**: Overload resolution rules are so complex that no one—including committee experts—fully understands all implications. Users should avoid relying on subtle overload resolution behaviors.

**Why It Matters**: Code that depends on overload resolution edge cases may break in surprising ways or behave differently across compilers. Successor languages are deliberately restricting overload resolution scope.

**When to Apply**: When designing APIs with multiple overloads, or evaluating proposals that interact with overload resolution.

**Red Flags**:
- APIs relying on subtle overload distinctions
- Code correctness depending on specific overload being chosen
- Proposals adding new overload resolution rules or exceptions
- "SFINAE tricks" as core API mechanism

**Supporting Experiences**: None directly stated (implicit from expertise)

<!-- METADATA
kind: principle
id: P6
source-type: tacit
category: philosophy/language
applies-to: language
confidence: medium
supported-by: []
related-principles: [P5]
-->

---

### P7: Foundational Operations Should Be Language Features

> *"A lot of basic language things, like for example, STD move... they cause a lot of overhead, you know, like in code bays because templates are expensive, right? But a lot of these things... probably be more efficient to make that a language feature instead of library feature... I think like atomic probably would have been better as a language thing."*

**The Principle**: Ubiquitous foundational operations (std::move, std::forward, potentially atomics) pay unnecessary compile-time costs as library templates; they should be language features for better performance and diagnostics.

**Why It Matters**: Language features can provide better error messages, faster compilation, and more optimized codegen. The committee's historical preference for library solutions may be counterproductive for truly foundational operations.

**When to Apply**: When evaluating whether a new foundational capability should be library or language.

**Red Flags**:
- Foundational operation implemented as template when it could be intrinsic
- Error messages exposing library implementation details
- Compile-time overhead for operations used in every translation unit
- Library feature requiring compiler magic anyway

**Supporting Experiences**: None directly stated

<!-- METADATA
kind: principle
id: P7
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: []
related-principles: [P5]
-->

---

### P8: Implementation Capacity Must Constrain Feature Adoption

> *"We have approved like the linear algebra, you know, feature into the C++ standard library, but like I know from my work, my personal relationships, that there's barely anyone right now working on the C++, right?... you're probably only gonna get them done in like 5 years."*

**The Principle**: The committee should throttle feature adoption based on available implementation capacity; approving features faster than they can be implemented wastes committee resources and creates user expectations that can't be met.

**Why It Matters**: Standardizing features that won't be implemented for years provides no user value while consuming limited committee bandwidth. The gap between "standardized" and "available" undermines trust.

**When to Apply**: When prioritizing which papers to advance, especially large library additions.

**Red Flags**:
- Major library feature with no identified implementer
- Feature approved during implementation backlog
- "We can standardize now and implement later" reasoning
- No implementation timeline discussed

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: process/timing
applies-to: library
confidence: high
supported-by: [E5]
related-principles: [P9]
-->

---

### P9: Vocabulary Types Justify Standardization

> *"They should be more about the idea of building a vocabulary, right?... STD vector being in the standard library helped because like people are still gonna want to implement their own vectors because they're going to be specialized... but if they don't have any reason to be different, you know, from STD vector in some aspect... they shouldn't be."*

**The Principle**: Standard library additions are justified when they establish vocabulary types that enable interoperability between libraries; mere usefulness is insufficient justification.

**Why It Matters**: Without standard vocabulary types, libraries develop incompatible representations of the same concepts (as in C). Standardization's value is coordination, not just provision of implementation.

**When to Apply**: When evaluating whether a library proposal belongs in the standard vs. ecosystem.

**Red Flags**:
- "This is useful" as primary justification
- No evidence of interoperability friction being solved
- No discussion of existing ecosystem solutions
- Types unlikely to appear at API boundaries

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P9
source-type: explicit
category: belongs/vocabulary-types
applies-to: library
confidence: high
supported-by: [E5]
related-principles: [P8]
-->

---

### P10: Knowledge Is Lost in Committee Transitions

> *"A lot of times I need to figure out, you know, like why like something in the paper, or some idea was considered, you know, and you cannot find that on the paper, right?... there is also before that a transition between the mathematics study group and EWG, right?... a lot of discussions about that were probably lost in the transition."*

**The Principle**: Rationale and evidence discussed orally in study groups and EWG sessions is systematically lost because it's not recorded in papers; this makes retrospective analysis of decisions nearly impossible.

**Why It Matters**: Without recorded rationale, the committee cannot learn from past decisions, cannot evaluate whether features achieved their goals, and cannot understand why alternatives were rejected.

**When to Apply**: When authoring papers (include rationale), when reviewing (ask for rationale to be documented), when doing retrospectives.

**Red Flags**:
- Paper lacks "alternatives considered" section
- Rationale only exists in meeting minutes (if at all)
- Author says "we discussed this in SG-X" without documenting outcome
- Unable to determine why a design choice was made

**Supporting Experiences**: E5

<!-- METADATA
kind: principle
id: P10
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E5]
related-principles: [P4]
-->

---

### P11: Implementation Experience Reveals Design Flaws

> *"Louis, who is the libc++ maintainer, he came up and made a little showing tale about his experience implementing it in libc++, and he had like a lot of negative, you know, impressions... his presentation had an impact on my vote against Pablo's paper."*

**The Principle**: Testimony from library implementers about actual implementation experience should heavily influence votes; negative implementation experience is strong evidence of design problems.

**Why It Matters**: Implementers discover practical issues that paper authors and reviewers miss. Their experience represents ground truth about whether a design works in practice.

**When to Apply**: When evaluating proposals, especially those with competing designs or controversy.

**Red Flags**:
- No implementer feedback sought or provided
- Implementer concerns dismissed as "implementation details"
- Voting on proposals without implementation experience
- Paper author has not implemented their own proposal

**Supporting Experiences**: E4

<!-- METADATA
kind: principle
id: P11
source-type: explicit
category: evaluation/field-experience
applies-to: both
confidence: high
supported-by: [E4]
related-principles: [P8]
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: N4148 — The Trivially Copyable Bug Fix (2014)

**Context**: Matheus was working on wrapper types that needed to preserve trivial copyability from their wrapped type. During research for an argument on std-proposals, he discovered that types with deleted or inaccessible copy operations could still be trivially copyable.

**What Happened**: Matheus wrote paper N4148 proposing to fix this flaw. However, he couldn't attend meetings at the time, so he had to hand off the paper to someone else to carry it through the process. The fix was eventually merged by building on his work.

**The Outcome**: Success (eventually). The fix was incorporated into C++17, but the process took years and required someone else to shepherd it through.

**The Lesson**: Important bug fixes can stall without someone present to advocate for them. The distinction between editorial fixes (quick) and design bugs (slow) determines the timeline. Even "obvious" fixes require navigating significant process overhead.

> *"That kind of issue... it wasn't something that could be fixed very efficiently within the bureaucracy, right? So that's why I didn't, you know, carry it over the finish line myself, and I relied on someone else."*

**Supports Principles**: P1

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: history/successes
applies-to: language
outcome: success
features: [trivially-copyable, special-member-functions]
supports: [P1]
-->

---

### E2: P3310 — The Template Template Parameter Matching Disaster

**Context**: James Touton proposed relaxing template template parameter matching rules (P0522) so that a template template parameter would accept any template argument that would work for all uses within the template body—a type-theoretically sound extension.

**What Happened**: The paper went straight to CWG without EWG review and was applied as a defect report, retroactively changing the language. When compilers began implementing it, they discovered the specification completely lacked wording for how partial ordering should work with the new matching rules. Compilers implemented incompatible workarounds. Clang couldn't claim C++17 conformance for years because they implemented no workarounds and kept the feature behind a disabled-by-default flag.

**The Outcome**: Failure. Matheus eventually developed a proper solution while at Bloomberg, implemented it in Clang, and wrote P3310 to standardize the fix. James Touton joined as co-author for the wording. The saga became a cautionary tale cited when arguing that papers must go through EWG.

**The Lesson**: Features that seem like clean theoretical extensions can have devastating practical consequences when they interact with complex subsystems like partial ordering. Skipping EWG review doesn't save time—it defers and multiplies the cost.

> *"That was something actually that was holding Clang for a long time from advertising C++17 conformance... we couldn't consider that we had implemented that."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: history/failures
applies-to: language
outcome: failure
features: [template-template-parameters, partial-ordering]
supports: [P2]
-->

---

### E3: The Saint Louis Consensus That Wasn't

**Context**: Matheus presented his first paper defending a template-related fix at the Saint Louis meeting in 2024. He had written a long, well-explained paper and had been interacting primarily with Richard Smith—one of the foremost C++ language experts.

**What Happened**: The paper received near-unanimous consensus in EWG. But when it reached CWG, reviewers found issues. The paper title didn't fully convey all the changes, and CWG questioned whether EWG voters had really understood what they approved. Matheus had to return to confirm the intent. He also discovered that some voters had initially misunderstood parts of his presentation, only realizing this during CWG discussion.

**The Outcome**: Mixed. The paper eventually progressed, but required additional rounds. More importantly, Matheus learned that his interactions with Richard Smith had "colored his view" and made him "severely overestimate how much people understood about templates, even in the committee."

**The Lesson**: A unanimous vote does not indicate understanding. Authors must not assume that vote counts reflect comprehension, especially on technically complex topics. Expert-level collaborators can create a skewed perception of baseline committee knowledge.

> *"My first ever paper to the committee and there was almost basically unanimous consensus, right? And but that didn't mean that people really understood what was going on there."*

**Supports Principles**: P3, P4, P5

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: process/politics
applies-to: language
outcome: mixed
features: [templates, partial-ordering, deduction]
supports: [P3, P4, P5]
-->

---

### E4: Trivial Relocation — Implementation Experience Decides

**Context**: Two competing trivial relocation proposals were under consideration: Arthur O'Dwyer's (aligned with existing industry practice but requiring explicit opt-in) and Pablo Halpern's (more radical, attempting automatic deduction).

**What Happened**: Matheus wouldn't have voted for Arthur's proposal because it lacked automatic deduction ("the language figure out if a type should be trivially relocatable"). He saw Pablo's proposal as having "a lot of weird things and unanswered things." Then Louis Dionne, the libc++ maintainer, presented his negative implementation experience with Pablo's design.

**The Outcome**: Pablo's proposal was pulled from C++26. Louis Dionne's testimony significantly influenced Matheus's vote and others'. The controversy demonstrated how implementation experience can overturn theoretical preferences.

**The Lesson**: Implementer testimony is decisive. Matheus explicitly states he "trusts [Louis's] opinion a lot on that stuff" and that the presentation "had an impact on my vote." When experts who've actually implemented something report problems, that evidence outweighs theoretical arguments.

> *"Louis, who is the libc++ maintainer, he came up and made a little showing tale about his experience implementing it in libc++, and he had a lot of negative impressions... his presentation had an impact on my vote."*

**Supports Principles**: P11

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: evaluation/field-experience
applies-to: library
outcome: mixed
features: [trivial-relocation]
supports: [P11]
-->

---

### E5: Linear Algebra — Approved Without Implementers

**Context**: The linear algebra proposal went through the mathematics study group and eventually was approved for C++26's standard library.

**What Happened**: Matheus observes that "there's barely anyone right now working on [libc++]" and the feature represents "a crazy amount of work for not having anyone to do it." He estimates implementations may not arrive for 5 years. When pressed on the evidence of need (coordination problems, interoperability friction), he couldn't recall specific evidence being presented—only that "from my personal perspective" such vocabulary types are valuable.

**The Outcome**: The feature was approved, but without clear implementation timeline or documented evidence of the specific coordination problems it solves. Rationale discussed in the mathematics study group was not preserved in the paper.

**The Lesson**: Features can be approved faster than they can be implemented, creating a backlog. Rationale established in study groups may not survive the transition to EWG/LEWG papers. "Useful" is accepted as sufficient justification even when evidence of specific coordination failures is lacking.

> *"We have approved the linear algebra feature into the C++ standard library, but I know from my personal relationships that there's barely anyone right now working on [libc++]... you're probably only gonna get them done in like 5 years."*

**Supports Principles**: P8, P9, P10

<!-- METADATA
kind: experience
id: E5
source-type: explicit
category: process/timing
applies-to: library
outcome: mixed
features: [linear-algebra, mdspan]
supports: [P8, P9, P10]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Reviewing Language Proposals (Especially Template-Related)

- [ ] Has this paper been reviewed by someone with deep implementation expertise in the affected area?
- [ ] Does the paper address interactions with partial ordering, overload resolution, and template argument deduction?
- [ ] If this is labeled a "bug fix," is it actually editorial (clear intent) or design (unclear intent)?
- [ ] Has the paper received implementation experience beyond "it compiles"?
- [ ] Are there CWG-affiliated experts who should review before EWG vote?
- [ ] Does the paper title accurately reflect all changes being proposed?

**Questions to Ask**:
1. "What happens when this interacts with partial ordering?"
2. "Has anyone from CWG reviewed this for wording feasibility?"
3. "If I asked 5 random EWG voters to explain this paper's mechanism, could they?"
4. "What compilers have implemented this, and what did they discover?"

<!-- METADATA
kind: checklist
category: evaluation/language
applies-to: language
proposal-type: feature
derived-from: [P2, P3, P4, P5, P6]
-->

---

### When Reviewing Library Proposals

- [ ] Is this establishing a vocabulary type that enables library interoperability?
- [ ] Is there documented evidence of coordination failures this solves (not just "this is useful")?
- [ ] Are there identified implementers with capacity to implement this?
- [ ] Has an implementer provided testimony about implementation experience?
- [ ] What is the realistic implementation timeline given current backlog?
- [ ] Is the rationale from study group discussions captured in the paper?

**Questions to Ask**:
1. "What specific interoperability problem does this solve that third-party libraries cannot?"
2. "Who is going to implement this, and when?"
3. "What evidence do we have that users are blocked by lack of this in the standard?"
4. "What was discussed in the study group that isn't in this paper?"

<!-- METADATA
kind: checklist
category: evaluation/library
applies-to: library
proposal-type: feature
derived-from: [P8, P9, P10, P11]
-->

---

### When Evaluating Papers Claiming Near-Consensus in EWG

- [ ] Can voters articulate why they voted in favor?
- [ ] Were questions asked during presentation, or did it "fly over heads"?
- [ ] Does the author have calibrated expectations about committee template/language expertise?
- [ ] Has CWG been consulted about wording feasibility?
- [ ] Does the paper fully disclose all behavioral changes (not just the headline feature)?

**Questions to Ask**:
1. "What concerns were raised during discussion?"
2. "Did anyone ask for clarification on the technical mechanism?"
3. "What would CWG experts say about this if they had been in the room?"

<!-- METADATA
kind: checklist
category: process/politics
applies-to: language
proposal-type: feature
derived-from: [P3, P4]
-->

---

## Open Questions

1. **What specific papers does Matheus believe should have been language features instead of library features?** He mentions std::move, std::forward, and atomics, but are there others? What's the full list of "foundational operations that pay unnecessary template cost"?

2. **What are the specific C++0x concepts that would have provided definition-side checking?** Matheus mentions "the C++11 ones maybe, but that ship has sailed"—what was the mechanism and why can't we return to it?

3. **Which libraries "where this strategy has failed us"?** Matheus mentions a pattern of standardizing without field experience leading to failures, but doesn't enumerate specific examples beyond the template template parameter case.

4. **What were the specific "weird things and unanswered things" in Pablo's trivial relocation paper?** Understanding these would help identify what to look for in future proposals.

5. **What happened to niebloids?** Matheus mentions Eric Niebler "dropped or is not trying to standardize them anymore"—what caused this change and what replaced them?

6. **What is the actual evidence that was presented for linear algebra standardization?** Matheus couldn't recall it. Was there documented evidence of interoperability friction, or was "useful for games/physics" the extent of the justification?

7. **Which template-related areas have "retired or inactive" experts?** Matheus mentions partial ordering, template argument deduction, and partial template specialization. Who were these experts, and is there documented knowledge from them?

---

## Raw Transcript Reference

See: `transcripts/matheus-izvekov.md`

Interview conducted January 7, 2026, covering Matheus's journey from his first paper (N4148, 2014) through his current work on template-related defect reports, with extensive discussion of committee process, expertise gaps, and standardization philosophy.
