# Harry Bott: Captured Knowledge

**Interview Date**: 2025-11-03
**Interviewer**: Ray Nowosielski
**Duration**: ~71 minutes
**Topics Covered**: C++ Alliance mission, Alliance CEO role, compiler writer shortage, WG21 process, C++ future and safety concerns, BSL license promotion, China outreach, contracts standardization, AI and legacy code advantages

## Executive Summary

Harry Bott, the newly appointed CEO of the C++ Alliance, provides a fresh outsider perspective on the C++ ecosystem. His unconventional background—Juilliard music, Columbia classics, Goldman Sachs trading systems, Bear Wagner CIO during NYSE electronic transition—gives him unique insights into high-stakes technology transitions and managing talented people through change.

His most striking contribution is the "compiler writer crisis" revelation: while estimating 5,000 compiler engineers globally, actual investigation revealed perhaps 50 active, with ~25 working daily. This creates existential fragility—"the world runs on C++" but depends on a handful of individuals maintaining GCC and Clang. His thought experiment about a convention attack being catastrophic is darkly illuminating.

Most actionable is his "future focus" philosophy: "the past is done... we're ready to move forward and collaborate." As new Alliance CEO, he attended CPP Con and WG21 Kona on "reconnaissance missions" seeking partnership opportunities, explicitly not relitigating past conflicts. This represents a potential reset in community relations.

---

## Principles

Distilled, actionable knowledge that can be applied agentically.

### P1: The Compiler Writer Crisis Is Real

> *"There's gotta be 5,000 compiler engineers... then I actually sat down and started to try to reach out to compiler engineers... There's like 50. And there's like maybe 25 who are doing it on a day-to-day basis."*

**The Principle**: The global pool of active C++ compiler engineers (GCC, Clang) is shockingly small—perhaps 50, with ~25 working daily. This creates existential risk for infrastructure that "runs the world."

**Why It Matters**: If C++ underlies nuclear reactors, stock exchanges, and aircraft systems, and only 25 people maintain the compilers, the ecosystem is more fragile than anyone realizes. "You could have a plane with all the compiler writers in the world."

**When to Apply**:
- When planning ecosystem investments
- When assessing infrastructure risk
- When recruiting compiler engineers

**Red Flags**:
- Ignoring compiler development as "someone else's problem"
- Not investing in compiler engineer pipeline
- Assuming compiler maintenance is sustainable

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P1
source-type: explicit
category: process/actual
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P2]
-->

---

### P2: Language Surface Area Makes Learning Daunting

> *"Every time something is added to the language, it makes the learning process more daunting... at a certain point, it becomes just a huge topic that no one can really be expert in the entire thing."*

**The Principle**: C++'s 40-year growth, with features added every three years, has made the language impossible for anyone to fully master. Each addition increases "surface area" that newcomers must learn.

**Why It Matters**: This creates a tension: WG21 keeps adding useful features (contracts, reflection), but each addition makes C++ more daunting for new developers. "All the layups were done in 2011."

**When to Apply**:
- When evaluating new feature proposals
- When designing educational materials
- When understanding adoption challenges

**Red Flags**:
- Adding features without considering learning burden
- Assuming new developers will catch up
- Ignoring the complexity tax on the ecosystem

**Supporting Experiences**: E2

<!-- METADATA
kind: principle
id: P2
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E2]
related-principles: [P1]
-->

---

### P3: AI Favors Incumbent Languages

> *"AI revolution... really does favor incumbent languages because there's such a large code base to learn from... there's this huge library to use of C++ out there to learn from."*

**The Principle**: Contrary to intuition that AI might favor new languages, AI coding assistants benefit established languages (like C++) with massive existing codebases for training data.

**Why It Matters**: C++'s billions of lines of existing code become an asset for AI-assisted development. This is a countervailing force against safety-motivated migration to Rust/Swift. Legacy code quantity enables better AI assistance.

**When to Apply**:
- When planning language strategy
- When evaluating AI assistance tools
- When understanding competitive dynamics

**Red Flags**:
- Assuming AI will accelerate migration to new languages
- Ignoring training data as competitive advantage
- Dismissing legacy code as purely a liability

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P3
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E3]
related-principles: []
-->

---

### P4: The Review Process Is a Rite of Passage

> *"Being a Boost library means you've gone past the Boost review process and it's kind of a rite of passage... It's a badge of honor. It's something where you get attention by going through that process, you get the right kind of attention."*

**The Principle**: The Boost review process provides validation that confers reputation on library authors—a "badge of honor" that signals quality to the community.

**Why It Matters**: Beyond technical vetting, the review process creates social capital. Authors who pass review earn recognition that opens doors. This explains why some prefer the difficult Boost path over easier alternatives.

**When to Apply**:
- When advising library authors on strategy
- When understanding motivations for Boost contribution
- When evaluating alternatives to Boost

**Red Flags**:
- Bypassing review for expedience
- Undervaluing the reputational benefits
- Treating review as purely technical gatekeeping

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P4
source-type: explicit
category: process/actual
applies-to: library
confidence: high
supported-by: [E1]
related-principles: []
-->

---

### P5: Move Forward, Don't Relitigate

> *"I'm very much focused on the future... the past is done. It's already, it's done. And we're ready to move forward and collaborate and have a positive working relationship."*

**The Principle**: When joining a community with past conflicts, focus on future collaboration rather than understanding or litigating historical disputes.

**Why It Matters**: As new Alliance CEO, Bott explicitly declined to investigate past conflicts ("willful ignorance"). His CPP Con and WG21 attendance were "reconnaissance missions" to find partners, not assign blame. This enables fresh starts.

**When to Apply**:
- When entering communities with historical conflicts
- When rebuilding damaged relationships
- When deciding how to spend leadership attention

**Red Flags**:
- Demanding resolution of past grievances before collaboration
- Relitigating historical disputes
- Letting past conflicts define current possibilities

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P5
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [E1]
related-principles: []
-->

---

### P6: C++ Is Like Electricity—Invisible Infrastructure

> *"It's kinda like electricity... it's so a part of your life that you don't even realize it until it's... you don't even realize how much of the world runs on C++. Nuclear reactors or seven forty sevens or the world's stock markets."*

**The Principle**: C++ underlies so much critical infrastructure (stock exchanges, aircraft, nuclear reactors) that it's become invisible—people don't realize their dependence until something fails.

**Why It Matters**: This frames the stakes of C++ safety debates and ecosystem health. If C++ is foundational infrastructure, its maintenance is a public good that transcends individual company interests. The compiler writer shortage becomes a civilizational risk.

**When to Apply**:
- When communicating C++ importance to non-technical audiences
- When justifying ecosystem investments
- When understanding why C++ won't simply disappear

**Red Flags**:
- Underestimating C++ criticality
- Treating C++ maintenance as private goods
- Assuming migration away from C++ is feasible

**Supporting Experiences**: E3

<!-- METADATA
kind: principle
id: P6
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [E3]
related-principles: [P1]
-->

---

### P7: Musical Instrument Study Teaches Coding Discipline

> *"Studying an instrument is useful... you have to figure out a way to get better... everyday practice by yourself and making daily incremental progress... I think that's a very direct analogy to coding."*

**The Principle**: Studying a musical instrument teaches the self-directed discipline required for coding: daily solitary practice, incremental progress, weekly review with a mentor.

**Why It Matters**: Unlike most Western education, instrument study teaches how to improve independently—the same skill coding requires. Both involve solitary work followed by feedback cycles. This explains why musical backgrounds correlate with programming ability.

**When to Apply**:
- When understanding programmer development
- When advising young people on skill development
- When valuing non-traditional backgrounds

**Red Flags**:
- Assuming only technical training prepares for coding
- Ignoring discipline development in education
- Missing the analogy between artistic and technical practice

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P7
source-type: tacit
category: philosophy/tradeoffs
applies-to: both
confidence: medium
supported-by: [E1]
related-principles: []
-->

---

### P8: The BSL Is the Cleanest License

> *"BSL is the cleanest way of licensing your software... it's the least intrusive license. It's ideal for open source software."*

**The Principle**: The Boost Software License is the "cleanest" open source license—least intrusive, ideal for corporate adoption, superior to similar alternatives.

**Why It Matters**: This aligns with Glen Fernandes' testimony about BSL's adoption advantages. The Alliance is actively promoting BSL awareness as a strategic initiative. License choice affects library adoption.

**When to Apply**:
- When choosing licenses for new projects
- When advising organizations on open source policy
- When evaluating barriers to library adoption

**Red Flags**:
- Using more restrictive licenses without reason
- Ignoring license as adoption factor
- Missing the BSL's unique properties

**Supporting Experiences**: E1

<!-- METADATA
kind: principle
id: P8
source-type: explicit
category: evaluation/library
applies-to: library
confidence: high
supported-by: [E1]
related-principles: []
-->

---

## Experiences

Relatable stories that illustrate and support the principles.

### E1: Reconnaissance Mission at CPP Con and WG21

**Context**: Harry Bott's first weeks as Alliance CEO, attending CPP Con 2025 and WG21 Kona.

**What Happened**: Bott approached both events as "reconnaissance missions" to understand "the lay of the land"—who was willing to work with the Alliance, who was wary, what the issues were. He met staff engineers, John Kalb, Alan Talbot, Matt Poosh (Polish unit library author being sponsored). He explicitly chose not to investigate past conflicts: "I'm very much focused on the future."

**The Outcome**: Positive. Bott reports "feeling pretty positive about the prospect of partnering up with different members of the community." The Alliance sponsored Matt Poosh's attendance at WG21, demonstrating investment in new contributors.

**The Lesson**: Fresh leadership can reset relationships by refusing to relitigate the past. Reconnaissance before judgment, partnership before position-taking. The "badge of honor" from Boost review remains attractive to new contributors.

> *"The goal I think of the Alliance and of people who want to see C++ thrive is to make it a language that is viable for new projects, for the foreseeable future."*

**Supports Principles**: P4, P5, P8

<!-- METADATA
kind: experience
id: E1
source-type: explicit
category: process/navigation
applies-to: both
outcome: positive
features: [Alliance, reconciliation, partnerships]
supports: [P4, P5, P8]
-->

---

### E2: WG21 Size and Complexity Growth

**Context**: Bott's observations of the WG21 process at the Kona 2025 meeting.

**What Happened**: The standards committee has grown from a small group to "20 something odd study groups" and "hundreds of members." Getting anything done is "a much bigger task." The meeting was processing national body comments on contracts, a feature that's been discussed for years and was removed from C++20 at the last minute. Even trivial relocation requires touching both language and library. "All the layups were done in 2011."

**The Outcome**: Ongoing. C++26 is expected to include contracts, reflection, and trivial relocation—major features—but the process is "down to the last minute" despite appearing slow with a 3-year cadence.

**The Lesson**: WG21's success in attracting participation has created coordination challenges. More participants means more comments to resolve, more conflicts to navigate, and harder consensus-building. The committee's growth is both a strength and a bottleneck.

> *"You've got 150 people attending a meeting, and they're all technically savvy... many of them are super, super bright. And they're coming together trying to come to agreement. The best you can hope for is violent agreement."*

**Supports Principles**: P2

<!-- METADATA
kind: experience
id: E2
source-type: explicit
category: process/actual
applies-to: both
outcome: ongoing
features: [WG21, committee-size, standardization]
supports: [P2]
-->

---

### E3: The Compiler Writer Thought Experiment

**Context**: Bott's experience recruiting compiler engineers for a previous initiative.

**What Happened**: Bott and a colleague estimated there must be 5,000 compiler engineers globally. As a thought experiment, they imagined a "compiler engineering convention in Vegas" attacked by terrorists—"the world would come to a stop." When Bott actually tried to recruit compiler engineers, he discovered the pool was perhaps 50, with ~25 working daily. "Let's not tell anybody," he joked, because the fragility is genuinely alarming.

**The Outcome**: Insight. This drives the Alliance's initiative to "sponsor younger compiler developers, provide them with mentors, and bring along the next generation." Compiler maintenance is an essential but neglected part of the ecosystem.

**The Lesson**: Critical infrastructure depends on small numbers of people. The C++ ecosystem's health requires investing in compiler engineers, not just library developers. AI favoring incumbent languages creates countervailing pressure against migration.

> *"Nuclear reactors or 747s or the world's stock markets—these are things that all run on C++... There's a lot of weight resting on the C++ language."*

**Supports Principles**: P1, P3, P6

<!-- METADATA
kind: experience
id: E3
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
outcome: insight
features: [compiler-engineers, infrastructure, risk]
supports: [P1, P3, P6]
-->

---

### E4: John Lakos Introduction to Vinnie Falco

**Context**: How Bott came to lead the C++ Alliance.

**What Happened**: John Lakos, who was "always talking about Vinnie," introduced Bott via Zoom. Bott found Vinnie "super bright" and "very personable"—"easy to get along with" despite expectations that "coders or programmers" might be difficult. Vinnie was "results oriented, very practical... very interested in getting things done." When the CEO opportunity arose, Bott "jumped at the chance."

**The Outcome**: Success. Bott reports working well with Vinnie and the Alliance team, finding "great team, great collection of minds... really bright people."

**The Lesson**: Strong referrals from respected figures (Lakos) enable trust-building. Bott's background (music, finance, management) complemented Vinnie's technical focus. "Role of a lifetime" suggests successful matching of person to opportunity.

> *"He's got a quick mind and he seems to be always onto the next thing... moves quick."*

**Supports Principles**: P5

<!-- METADATA
kind: experience
id: E4
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [John-Lakos, Vinnie-Falco, Alliance-leadership]
supports: [P5]
-->

---

## Evaluation Checklists

Actionable checklists derived from principles, for evaluating proposals.

### When Assessing Ecosystem Health

- [ ] What is the state of compiler engineer pipeline? (P1)
- [ ] Is language complexity deterring new developers? (P2)
- [ ] Are AI tools available for this language/library? (P3)
- [ ] Is critical infrastructure dependent on few individuals? (P1, P6)

**Questions to Ask**:
1. "How many people are actively maintaining the compilers?"
2. "Can a new developer realistically learn this?"
3. "What happens if key maintainers leave?"
4. "Is training data available for AI assistance?"

<!-- METADATA
kind: checklist
category: process/actual
applies-to: both
proposal-type: any
derived-from: [P1, P2, P3, P6]
-->

---

### When Planning Community Engagement

- [ ] Are we focused on future collaboration, not past grievances? (P5)
- [ ] Have we done reconnaissance before taking positions? (P5)
- [ ] Are we sponsoring new contributors? (P4)
- [ ] Is the BSL license being promoted? (P8)

**Questions to Ask**:
1. "What would partnership look like?"
2. "Who is willing to work with us?"
3. "How can we remove obstacles for bright minds to contribute?"
4. "Are we relitigating or building?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: any
derived-from: [P4, P5, P8]
-->

---

## Open Questions

1. What specific mentorship programs is the Alliance developing for compiler engineers?

2. What is the status of Chinese developer outreach and documentation translation?

3. How did contracts get removed from C++20 at the last minute?

4. What are the Alliance's AI-related initiatives that Bott mentioned but couldn't share?

5. How is the transition from Herb Sutter to Guy Davidson affecting committee dynamics?

6. What happened to Sean Baxter's Safe C++ initiative that "didn't get the traction"?

7. What is the Alliance's relationship with the Standard C++ Foundation now?

8. How many Boost libraries are actively maintained vs. unmaintained?

9. What specific compiler engineer recruitment efforts is the Alliance undertaking?

10. How effective has the China outreach (40% web traffic) been in generating contributions?

---

## Raw Transcript Reference

Source: `inputs/harry-bott.md`
Video: https://vimeo.com/1140473570/bbc46461c8?fl=pl&fe=sh
Filmed: 2025-11-03, Kona, HI
