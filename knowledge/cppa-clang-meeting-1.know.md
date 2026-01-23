# CPPA-Clang Meeting 1: Captured Knowledge

**Meeting Date**: January 23, 2026
**Duration**: ~26 minutes (11:41 AM - 12:07 PM Pacific)
**Participants**: Matheus Izvekov, Vinnie Falco, Krystian
**Topics Covered**: AI-assisted Clang development workflow, two-repository structure, review processes, issue prioritization, knowledge capture for compilers

---

## Executive Summary

This meeting captured critical institutional knowledge about deploying AI-assisted development workflows for the LLVM/Clang compiler. The discussion revealed three key themes: (1) the fundamental separation between AI-generated code review and traditional human code review as distinct skills requiring different processes; (2) the importance of human accountability for AI outputs—humans must be able to explain and defend any AI-generated contribution; and (3) implicit knowledge about LLVM issue prioritization that exists only in the minds of senior contributors like Richard Smith. The conversation also validated the concept of expertise scoring and knowledge capture as essential components for scaling AI-assisted development.

---

# Matheus Izvekov: Principles and Experiences

## Principles

### MI-P1: Avoid Splitting Human Review

> *"If we can put like split those domains up, you know, then we're sure that we see like pull requests in the C++ Alliance LVM report... we're not supposed to review this, only AI reviewing. And then when that goes to LLVM project, then everyone reviews."*

**The Principle**: Human review should happen in one consolidated location to avoid duplicated discussion, repeated explanations, and fragmented context.

**Why It Matters**: When review is split across repositories, new reviewers ask questions already discussed elsewhere. This wastes time, creates inconsistent understanding, and makes it harder to maintain coherent decision-making.

**When to Apply**: Designing multi-stage workflows that involve both AI-assisted development and upstream contribution.

**Red Flags**:
- Reviewers asking about issues previously resolved in another venue
- Important context existing only in a non-upstream repository
- Having to repeat rationale explanations across multiple review locations

**Supporting Experiences**: MI-E1

<!-- METADATA
kind: principle
id: MI-P1
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [MI-E1]
related-principles: [VF-P1, VF-P2]
-->

---

### MI-P2: Human Accountability for AI Outputs

> *"The Human like the us, you know, like that we need to be able to respond or account for everything that the bot does, right? So like, for example, if we come up, you know, like go to LLVM review, and they're like someone suddenly we have to ask the bot, you know, like, what's going on here? Why we did things this way. That, that, that, that would be bad, right?"*

**The Principle**: Humans must be able to fully explain and defend any AI-generated contribution without needing to defer to the AI itself.

**Why It Matters**: In code review, you are expected to understand and defend your submission. If you cannot explain why a change was made without asking the AI, you cannot credibly claim ownership or responsibility for the contribution.

**When to Apply**: Any time AI-generated code is submitted for review by humans, especially in upstream/external projects.

**Red Flags**:
- Needing to re-prompt the AI to answer reviewer questions
- Contributors who cannot explain the rationale for their own submission
- Pull request discussions that reveal the submitter doesn't understand the change

**Supporting Experiences**: MI-E2

<!-- METADATA
kind: principle
id: MI-P2
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [MI-E2]
related-principles: [VF-P3, K-P2]
-->

---

### MI-P3: Weight Opinions by Expertise

> *"Like Richard Smith, like you, you should give a lot of weight to his opinions and things like that."*

**The Principle**: Not all feedback is equal—opinions from recognized experts in a domain should carry more weight in decision-making.

**Why It Matters**: In large projects like LLVM, some contributors have decades of experience and deep understanding of design decisions. Their pattern recognition and judgment is informed by history that newer contributors cannot replicate.

**When to Apply**: Evaluating conflicting opinions in code review, issue triage, or design discussions.

**Red Flags**:
- Treating all feedback as equally weighted
- Ignoring input from domain veterans
- Making decisions that contradict expert consensus without strong justification

**Supporting Experiences**: MI-E3

<!-- METADATA
kind: principle
id: MI-P3
source-type: tacit
category: process/politics
applies-to: both
confidence: high
supported-by: [MI-E3]
related-principles: [VF-P5]
-->

---

### MI-P4: LLVM Issue Priority Hierarchy

> *"There's this thing about in LLVM projects about how we like grade importance of issues... crashes that are basically like fuzzy generated. They're like the lowest priority thing for us to fix, right? And above that, like you could say, a light crashes, like yeah, crash on the valid code or especially crash on the valid code after, you know, like an error has already been emitted right like a crash on the error recovery situations."*

**The Principle**: LLVM issues have an implicit priority hierarchy: fuzzer-generated crashes are lowest priority; crashes on valid code are higher priority; crashes during error recovery are in between.

**Why It Matters**: This unwritten prioritization guides where maintainers spend their limited time. Understanding it helps contributors identify high-value issues versus noise.

**When to Apply**: Triaging issues, deciding which bugs to fix, evaluating AI-generated fixes.

**Red Flags**:
- Spending significant effort on fuzzer-generated crashes while higher-priority issues remain
- Not distinguishing between crash types in issue assessment
- Treating all crashes as equally urgent

**Supporting Experiences**: MI-E3

<!-- METADATA
kind: principle
id: MI-P4
source-type: implicit
category: process/actual
applies-to: language
confidence: high
supported-by: [MI-E3]
related-principles: []
-->

---

### MI-P5: Make AI Identity Explicit

> *"Could we have like the bot as a person in the GitHub, you know, like putting these comments in his own name because that would make things clearer, right?"*

**The Principle**: AI-generated contributions and comments should be clearly attributed to the AI itself, not mixed with human identity.

**Why It Matters**: Clarity about authorship prevents confusion about who said what, enables proper accountability, and allows reviewers to calibrate their expectations appropriately.

**When to Apply**: Deploying AI assistants in collaborative development environments.

**Red Flags**:
- Confusion about whether a comment came from a human or AI
- AI content posted under human accounts without clear attribution
- Reviewers treating AI output as if a human wrote it

**Supporting Experiences**: MI-E2

<!-- METADATA
kind: principle
id: MI-P5
source-type: explicit
category: process/navigation
applies-to: both
confidence: medium
supported-by: [MI-E2]
related-principles: [MI-P2]
-->

---

## Experiences

### MI-E1: Avoiding Split Review Domains

**Context**: Discussion of workflow design for AI-assisted Clang development, considering whether to use the C++ Alliance fork for AI review and then submit to upstream LLVM.

**What Happened**: Matheus expressed concern that if human review happened in both the Alliance fork and upstream LLVM, reviewers in each location might ask questions already addressed elsewhere, leading to repetition and fragmentation.

**The Outcome**: Mixed—the concern was acknowledged and the workflow was designed to minimize this, with AI review happening in the fork and human review consolidated at upstream submission time.

**The Lesson**: When designing multi-stage workflows, consider where review happens and ensure context flows through the pipeline without requiring repetition.

> *"If we can put like split those domains up... then we're gonna be repeating ourselves, right, as well. That, that's another problem that that I wanted to like avoid."*

**Supports Principles**: MI-P1

<!-- METADATA
kind: experience
id: MI-E1
source-type: explicit
category: process/navigation
applies-to: both
outcome: mixed
features: [workflow-design, code-review]
supports: [MI-P1]
-->

---

### MI-E2: Accountability Scenario

**Context**: Matheus imagined a scenario where a contributor submits AI-generated code to LLVM and faces questions they cannot answer.

**What Happened**: He described a hypothetical where someone goes to LLVM review and has to "ask the bot" to explain why something was done a certain way—which would be embarrassing and undermine credibility.

**The Outcome**: This concern directly shaped the workflow requirement to generate comprehensive rationale documents before upstream submission.

**The Lesson**: Before submitting AI-generated work, ensure you fully understand it and can defend it without the AI's help.

> *"If we come up, you know, like go to LLVM review, and they're like someone suddenly we have to ask the bot... Why we did things this way. That, that, that, that would be bad."*

**Supports Principles**: MI-P2, MI-P5

<!-- METADATA
kind: experience
id: MI-E2
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
outcome: mixed
features: [ai-workflow, accountability]
supports: [MI-P2, MI-P5]
-->

---

### MI-E3: Richard Smith on Fuzzer Issues

**Context**: Discussing how LLVM prioritizes different types of issues, Matheus recalled a conversation with Richard Smith about fuzzer-generated bugs.

**What Happened**: Richard Smith discouraged people from submitting fuzzer-generated issues because "we need an army of engineers to fix all those kinds of issues." This revealed the implicit prioritization: fuzzer crashes are lowest priority because they're effectively infinite and not user-facing.

**The Outcome**: This insight directly connected to the AI-assisted development concept—Krystian noted "here's your army," suggesting AI could tackle the low-priority-but-numerous fuzzer issues.

**The Lesson**: Understanding implicit project priorities helps identify where AI assistance can add value without distracting from human-priority work.

> *"Richard Smith talking about like fuzzy generated, you know, issues in Clang, you know, like discouraging people to submit them because basically he said, oh, like we need an army of engineers."*

**Supports Principles**: MI-P3, MI-P4

<!-- METADATA
kind: experience
id: MI-E3
source-type: tacit
category: history/decisions
applies-to: language
outcome: mixed
features: [clang, fuzzing, issue-triage]
supports: [MI-P3, MI-P4]
-->

---

# Vinnie Falco: Principles and Experiences

## Principles

### VF-P1: Two-Repository Structure for Cautious AI Deployment

> *"The two repository structure is specifically designed to allow us to move slowly to anticipate problems before they get exposed to the upstream repo."*

**The Principle**: Use a separate staging repository for AI-assisted development to contain risk and allow experimentation without exposing upstream to failures.

**Why It Matters**: AI-generated code has different failure modes than human code. A staging area allows for iteration, correction, and quality assurance before the work is judged by the broader community.

**When to Apply**: Deploying AI-assisted development workflows in open source projects with established upstream communities.

**Red Flags**:
- AI-generated PRs going directly to upstream without internal review
- Experimentation happening in public where failures damage reputation
- No clear separation between "in progress" and "ready for review" states

**Supporting Experiences**: VF-E1

<!-- METADATA
kind: principle
id: VF-P1
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [VF-E1]
related-principles: [MI-P1, VF-P2]
-->

---

### VF-P2: AI Review Is a Distinct Skill

> *"The review of the AI generated code... it's a different skill. It's related, but it's a different skill. So because the AI can hallucinate and also the way that we correct the things in the AI generated pull request is different than how you correct with the human."*

**The Principle**: Reviewing AI-generated code requires different skills and approaches than reviewing human-written code.

**Why It Matters**: AI hallucinations, pattern-matching errors, and context limitations create different error patterns than human mistakes. Reviewers must be trained to spot AI-specific issues.

**When to Apply**: Training reviewers for AI-assisted workflows, designing review checklists, evaluating AI output quality.

**Red Flags**:
- Treating AI output exactly like human code without calibration
- Missing hallucinated function calls or invented APIs
- Assuming code that "looks right" is correct without deeper verification

**Supporting Experiences**: VF-E1, VF-E2

<!-- METADATA
kind: principle
id: VF-P2
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [VF-E1, VF-E2]
related-principles: [MI-P2, K-P1]
-->

---

### VF-P3: Generate Comprehensive Rationale Documentation

> *"Part of the workflow is that when our pull request is ready, we have the AI generate a big description, a full explanation of the change, why it's safe, the deep analysis of all the code that gets touched, you know, how it proves that it's correct."*

**The Principle**: AI-assisted contributions should include comprehensive rationale documentation that humans review and can use to defend the change.

**Why It Matters**: This documentation serves multiple purposes: verification by the submitter, understanding by reviewers, and historical record for future maintainers.

**When to Apply**: Preparing any AI-assisted contribution for upstream submission.

**Red Flags**:
- Submitting AI patches without explanation of the reasoning
- Rationale documents that the submitter hasn't verified
- Documentation that doesn't address safety and correctness

**Supporting Experiences**: VF-E2, VF-E3

<!-- METADATA
kind: principle
id: VF-P3
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [VF-E2, VF-E3]
related-principles: [MI-P2, K-P2]
-->

---

### VF-P4: AI as Exploration Tool for Refactoring

> *"The process that Christian is talking about is you use the AI to explore, Hey, if I refactor this, what would it look like? If I do this, how many pieces of code have to be touched? It's very good at answering that question. It's not very good at having the imagination to figure out what the refactoring is."*

**The Principle**: Use AI to explore refactoring hypotheses (cost, scope, impact) while humans provide the architectural vision and design decisions.

**Why It Matters**: AI excels at mechanical analysis and transformation but lacks the creative judgment to know *what* to refactor. The human-AI collaboration is most effective when each does what they're best at.

**When to Apply**: Complex bug fixes requiring refactoring, code modernization, architectural changes.

**Red Flags**:
- Asking AI to "fix this the right way" without providing architectural guidance
- Relying on AI to make design decisions about class responsibilities
- Not using AI exploration to validate human intuitions about scope

**Supporting Experiences**: VF-E2

<!-- METADATA
kind: principle
id: VF-P4
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [VF-E2]
related-principles: [K-P1]
-->

---

### VF-P5: Expertise Scoring for Contribution Routing

> *"Not all feedback is equal, a correction from a 30-year language veteran carries more weight than a suggestion from a newcomer... we can calculate that with AI, and we can assign a score, not just in one category, but the AI can identify what the person is good at."*

**The Principle**: Build systems that recognize and leverage domain expertise, routing issues and reviews to people with demonstrated competence in relevant areas.

**Why It Matters**: Efficient use of scarce expert attention, better review quality, and faster resolution of complex issues.

**When to Apply**: Issue triage, reviewer assignment, evaluating conflicting feedback.

**Red Flags**:
- Routing complex template issues to people with no template expertise
- Treating all reviewer feedback as equally authoritative
- No mechanism to identify or leverage domain specialization

**Supporting Experiences**: VF-E4

<!-- METADATA
kind: principle
id: VF-P5
source-type: explicit
category: process/navigation
applies-to: both
confidence: medium
supported-by: [VF-E4]
related-principles: [MI-P3]
-->

---

### VF-P6: Knowledge Capture Through Expert Interviews

> *"What we do is you interview the people, like what I did with you, and you get them to talk about what's important and what's not, and you get them to talk for an hour and then we record all that and we get the transcript and then we can turn that into a document."*

**The Principle**: Capture tacit institutional knowledge by interviewing experts and converting their verbal insights into documented, teachable rules.

**Why It Matters**: Most valuable knowledge exists only in experts' heads. Systematic capture makes it available to AI systems, new contributors, and future maintainers.

**When to Apply**: Onboarding AI systems to new domains, preserving institutional knowledge, scaling expertise.

**Red Flags**:
- Deploying AI without capturing domain-specific knowledge
- Assuming AI can infer unwritten rules from code alone
- Losing institutional knowledge when experts leave

**Supporting Experiences**: VF-E4

<!-- METADATA
kind: principle
id: VF-P6
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [VF-E4]
related-principles: [MI-P3, MI-P4]
-->

---

### VF-P7: Move Cautiously and Ethically with AI

> *"If there's one thing I know is we have to move cautiously. We have to be very ethical, and we have to move responsibly."*

**The Principle**: Deploy AI assistance incrementally, anticipating problems and building safeguards before scaling up.

**Why It Matters**: AI-generated contributions carry reputational risk. Mistakes in upstream projects damage credibility and may harm the broader acceptance of AI assistance in open source.

**When to Apply**: Any new AI deployment, especially in established communities with high standards.

**Red Flags**:
- Rushing to scale AI contributions before validating quality
- Not anticipating failure modes specific to AI
- Treating AI as "just another contributor" without calibration

**Supporting Experiences**: VF-E1

<!-- METADATA
kind: principle
id: VF-P7
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [VF-E1]
related-principles: [VF-P1, VF-P2]
-->

---

## Experiences

### VF-E1: Designing the Two-Repository Workflow

**Context**: Planning how to integrate AI-assisted development into the Clang contribution process without exposing upstream LLVM to experimental failures.

**What Happened**: Vinnie proposed a two-repository structure: the C++ Alliance fork for AI experimentation and review, and upstream LLVM only for polished, verified contributions. This addresses the different failure modes of AI code.

**The Outcome**: The design was accepted, with refinement based on Matheus's concern about split review.

**The Lesson**: Separation of concerns—keeping experimentation isolated from production—applies to AI workflows just as it does to code architecture.

> *"The two repository structure is specifically designed to allow us to move slowly to anticipate problems before they get exposed to the upstream repo."*

**Supports Principles**: VF-P1, VF-P2, VF-P7

<!-- METADATA
kind: experience
id: VF-E1
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [workflow-design, ai-development]
supports: [VF-P1, VF-P2, VF-P7]
-->

---

### VF-E2: AI Explores Refactoring Options

**Context**: Discussing how experts should work with AI on complex bug fixes that require architectural decisions.

**What Happened**: Vinnie described the ideal workflow: human experts (Matheus, Krystian, Vlad) decide how to approach a fix at a high level (e.g., "use an observer pattern"), then use AI to explore "what would this fix look like if we did it this way." The AI generates hypotheses; humans evaluate.

**The Outcome**: This established the division of labor: humans provide vision, AI provides exploration and implementation.

**The Lesson**: AI is best used as a rapid prototyping tool for human-directed design decisions, not as an autonomous architect.

> *"What's the best way to fix this bug, but not at the low level of individual statements, but at a high level... then you use the AI to create a hypothesis."*

**Supports Principles**: VF-P2, VF-P3, VF-P4

<!-- METADATA
kind: experience
id: VF-E2
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
outcome: success
features: [ai-workflow, refactoring]
supports: [VF-P2, VF-P3, VF-P4]
-->

---

### VF-E3: Requesting Rationale Documentation

**Context**: Krystian had created a pull request with AI-generated patches but hadn't included the AI's reasoning.

**What Happened**: Vinnie requested that Krystian add the rationale document to the pull request—not in the branch, but as a comment. He emphasized that this documentation is essential for both internal review and future upstream submission.

**The Outcome**: Krystian added the AI's reasoning to the PR, establishing a workflow pattern.

**The Lesson**: Make documentation a required part of the AI workflow, not an afterthought.

> *"Now we might say that a pull request is not only a set of patches to the code, but also we have a markdown document that explains it."*

**Supports Principles**: VF-P3

<!-- METADATA
kind: experience
id: VF-E3
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [documentation, ai-workflow]
supports: [VF-P3]
-->

---

### VF-E4: Domain-Specific Expertise Example

**Context**: Vinnie illustrated why domain expertise routing matters using himself and Matheus as examples.

**What Happened**: He noted that Matheus is an expert with templates while Vinnie is not—so if Vinnie tried to fix a template issue with AI assistance, he'd want Matheus to review because he couldn't adequately evaluate the AI's output in that domain.

**The Outcome**: This established the need for expertise-aware routing in the workflow.

**The Lesson**: AI amplifies human capability but doesn't replace domain expertise. Route work to people who can actually evaluate it.

> *"For example, you are an expert with templates. Me, I am not an expert with templates... if I was contributing and I tried to address an issue that had to do with templates, and the AI produced some output. I would look at it. Maybe I'd say this looks OK, but I wouldn't want you to look at it too."*

**Supports Principles**: VF-P5, VF-P6

<!-- METADATA
kind: experience
id: VF-E4
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [expertise-routing, review-process]
supports: [VF-P5, VF-P6]
-->

---

# Krystian: Principles and Experiences

## Principles

### K-P1: AI as Domain Expert's Tool

> *"So ideally this like acts as a tool for like assisting you. So you, your domain-specific expert, so you use this tool to open an issue and you have the AI give you a preliminary response."*

**The Principle**: AI assistance works best when domain experts use it as a tool, not when non-experts use it to work in unfamiliar areas.

**Why It Matters**: The expert can evaluate and correct AI output; non-experts cannot. AI amplifies existing expertise rather than replacing it.

**When to Apply**: Assigning AI-assisted tasks, evaluating who should work on which issues.

**Red Flags**:
- Non-experts using AI to work in domains they can't evaluate
- No domain expert reviewing AI output before submission
- Assuming AI correctness because "it looks right"

**Supporting Experiences**: K-E1, K-E2

<!-- METADATA
kind: principle
id: K-P1
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [K-E1, K-E2]
related-principles: [VF-P4, VF-P5]
-->

---

### K-P2: Review Before Upstream Submission

> *"Once we're confident that this is like up to our standards and we all believe that this is sufficient quality to submit to LLVM then we submit it, because we don't want to just like have somebody prompt the AI to fix issues without review and just send it straight to LLVM."*

**The Principle**: All AI-generated contributions must be reviewed by qualified humans before upstream submission, regardless of how "obviously correct" they appear.

**Why It Matters**: AI can produce plausible-looking but subtly wrong code. Without expert review, these errors propagate to production.

**When to Apply**: Any AI-generated patch before it leaves the staging environment.

**Red Flags**:
- "This is simple, we don't need review"
- Submissions without domain expert sign-off
- Time pressure leading to skipped review

**Supporting Experiences**: K-E1

<!-- METADATA
kind: principle
id: K-P2
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [K-E1]
related-principles: [MI-P2, VF-P3]
-->

---

### K-P3: AI Excels at Stack-Trace Crashes

> *"The patches I'm working, I'm focusing on right now that I found that the AI to be best with are those like single line errors that cause a crash somewhere. It's great... because you have a stack trace, you have a code example, it's really good."*

**The Principle**: AI is particularly effective at fixing crashes with clear stack traces and minimal reproduction cases—well-defined problems with localized solutions.

**Why It Matters**: This identifies the "sweet spot" for AI assistance: issues with strong signal (stack trace, specific failure) and narrow scope (single-line fix).

**When to Apply**: Prioritizing which issues to tackle with AI assistance, setting expectations for AI effectiveness.

**Red Flags**:
- Expecting AI to be equally good at all issue types
- Applying AI to vague, poorly-specified issues
- Using AI for design problems rather than implementation bugs

**Supporting Experiences**: K-E2

<!-- METADATA
kind: principle
id: K-P3
source-type: tacit
category: evaluation/scope
applies-to: both
confidence: high
supported-by: [K-E2]
related-principles: [MI-P4]
-->

---

### K-P4: Include AI Reasoning in Pull Requests

> *"There's also like reasoning from the chat agent that can be included in the pull requests, so it's not entirely a black box. It does tell you how it got to its solution."*

**The Principle**: AI pull requests should include the AI's reasoning chain, not just the code changes, to make the process transparent and auditable.

**Why It Matters**: The reasoning provides context for reviewers, helps identify flawed logic, and serves as documentation for future understanding.

**When to Apply**: All AI-generated contributions.

**Red Flags**:
- AI patches without explanation
- "Black box" contributions where no one knows why changes were made
- Reasoning that doesn't match the actual code changes

**Supporting Experiences**: K-E2

<!-- METADATA
kind: principle
id: K-P4
source-type: explicit
category: process/navigation
applies-to: both
confidence: high
supported-by: [K-E2]
related-principles: [VF-P3, MI-P2]
-->

---

### K-P5: Human Verification Still Required for Complex Cases

> *"For human review, this still would take quite a while, just for verification purposes, but it is definitely a good response."*

**The Principle**: Even when AI produces good responses, complex domain issues (like template instantiation patterns with modules) require significant human verification time.

**Why It Matters**: AI doesn't eliminate review burden for complex issues—it may reduce implementation time but verification remains essential and time-consuming.

**When to Apply**: Estimating effort for AI-assisted complex fixes, managing expectations.

**Red Flags**:
- Assuming AI output requires less review for complex issues
- Rushing review because "the AI said it's correct"
- Underestimating verification time for nuanced domain problems

**Supporting Experiences**: K-E3

<!-- METADATA
kind: principle
id: K-P5
source-type: explicit
category: philosophy/tradeoffs
applies-to: both
confidence: high
supported-by: [K-E3]
related-principles: [K-P1, K-P2]
-->

---

## Experiences

### K-E1: Team Review Workflow

**Context**: Discussing who should review AI-generated contributions before upstream submission.

**What Happened**: Krystian described the intended workflow: the domain expert uses AI to generate a preliminary fix, then he, Matheus, Vlad, and others review it. Only after collective confidence is the PR submitted to LLVM.

**The Outcome**: Established the multi-reviewer workflow as a standard practice.

**The Lesson**: AI assistance doesn't reduce the need for peer review—it changes what gets reviewed.

> *"Me, you, and like possibly Vlad and other people, we review that and then once we're confident that this is like up to our standards and we all believe that this is sufficient quality to submit to LLVM then we submit it."*

**Supports Principles**: K-P1, K-P2

<!-- METADATA
kind: experience
id: K-E1
source-type: explicit
category: process/navigation
applies-to: both
outcome: success
features: [review-process, team-workflow]
supports: [K-P1, K-P2]
-->

---

### K-E2: Single-Line Crash Fixes

**Context**: Krystian had been experimenting with AI for different types of Clang issues.

**What Happened**: He found that AI excels at single-line crash fixes where there's a clear stack trace and reproducible test case. The AI can identify the root cause, propose a fix, and generate a test case—sometimes one-shotting the entire solution.

**The Outcome**: This became the initial focus area for AI-assisted development: high-signal, narrow-scope crashes.

**The Lesson**: Start AI deployment with problems that play to AI strengths: well-defined, localized, with clear success criteria.

> *"The patches I'm working, I'm focusing on right now that I found that the AI to be best with are those like single line errors that cause a crash somewhere."*

**Supports Principles**: K-P3, K-P4

<!-- METADATA
kind: experience
id: K-E2
source-type: explicit
category: evaluation/scope
applies-to: both
outcome: success
features: [ai-effectiveness, crash-fixes]
supports: [K-P3, K-P4]
-->

---

### K-E3: Template Instantiation Pattern Complexity

**Context**: Reviewing an AI-generated fix that Matheus had commented on regarding template instantiation patterns.

**What Happened**: Krystian noted that even though the AI gave "a good response" to Matheus's concern, the underlying issue—getting correct patterns for instantiated declarations with modules and explicit instantiations—is highly nuanced. Human verification would still take significant time.

**The Outcome**: Acknowledged that AI assistance doesn't eliminate complexity for domain-specific issues.

**The Lesson**: AI can help with implementation, but domain complexity remains domain complexity. Review time scales with problem complexity, not with whether AI or humans wrote the code.

> *"In this particular case, there's actually some, there's a lot of nuance in this situation because trying to get the correct pattern for an instantiated declaration is actually very non-trivial."*

**Supports Principles**: K-P5

<!-- METADATA
kind: experience
id: K-E3
source-type: explicit
category: philosophy/tradeoffs
applies-to: language
outcome: mixed
features: [templates, modules, verification]
supports: [K-P5]
-->

---

# Combined Evaluation Checklists

## When Evaluating AI Workflow Readiness

- [ ] Is there a staging environment separate from upstream? (VF-P1)
- [ ] Are reviewers trained on AI-specific failure modes? (VF-P2)
- [ ] Can contributors explain AI output without re-prompting? (MI-P2)
- [ ] Is AI attribution clear in all contributions? (MI-P5)
- [ ] Are rationale documents required before upstream submission? (VF-P3, K-P4)

**Questions to Ask**:
1. "Who will review AI output, and are they domain experts?"
2. "Can the submitter defend this change without asking the AI?"
3. "Where does experimentation happen vs. where does review happen?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: workflow
derived-from: [VF-P1, VF-P2, MI-P2, MI-P5, VF-P3, K-P4]
-->

---

## When Selecting Issues for AI Assistance

- [ ] Does the issue have a clear stack trace or reproduction case? (K-P3)
- [ ] Is the likely fix narrow in scope? (K-P3)
- [ ] Is there a domain expert available to review? (K-P1)
- [ ] Is this a fuzzer-generated crash (lowest priority) or user-facing? (MI-P4)
- [ ] Does the fix require architectural decisions humans must make? (VF-P4)

**Questions to Ask**:
1. "What type of signal does this issue provide?" (stack trace, test case, vague description)
2. "Who can evaluate correctness of a fix in this area?"
3. "Will this require refactoring decisions or just implementation?"

<!-- METADATA
kind: checklist
category: evaluation/scope
applies-to: both
proposal-type: issue-triage
derived-from: [K-P3, K-P1, MI-P4, VF-P4]
-->

---

## Before Submitting AI-Generated PR to Upstream

- [ ] Has a domain expert reviewed the change? (K-P1, K-P2)
- [ ] Can all team members explain the rationale without AI? (MI-P2)
- [ ] Is the AI's reasoning documented in the PR? (K-P4, VF-P3)
- [ ] Have complex domain issues been verified despite good AI output? (K-P5)
- [ ] Is the human review consolidated, not split? (MI-P1)

**Questions to Ask**:
1. "If a reviewer asks 'why did you do X?', can we answer?"
2. "Who signed off on this, and are they qualified in this domain?"
3. "Have we anticipated questions the upstream might have?"

<!-- METADATA
kind: checklist
category: process/navigation
applies-to: both
proposal-type: submission
derived-from: [K-P1, K-P2, MI-P2, K-P4, VF-P3, K-P5, MI-P1]
-->

---

## Open Questions

1. **What specific error patterns does AI struggle with in Clang?** (Krystian noted success with stack-trace crashes; what about semantic errors, incorrect codegen, etc.?)

2. **How should expertise scoring be calculated?** (Vinnie mentioned commit history, review accuracy, hypothesis correctness—what's the actual algorithm?)

3. **What's the complete LLVM issue priority taxonomy?** (Matheus mentioned fuzzer crashes < error recovery crashes < valid code crashes—is there more nuance?)

4. **What signals indicate when AI is operating outside its competence?** (Hallucinations, over-confident wrong answers, etc.)

5. **How should the fork-to-upstream transition criteria be defined?** (When is a PR "ready enough" to leave staging?)

6. **Who else at LLVM has implicit prioritization knowledge that should be captured?** (Matheus mentioned Richard Smith—who else?)

---

## Raw Transcript Reference

Source: `inputs/cppa-clang-meeting-1.md`
Auto-generated Slack transcript from #cppa-clang huddle, January 23, 2026
