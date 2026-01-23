Transcript of huddle in #cppa-clang on Jan 23 from 11:41 AM to 12:07 PM Pacific Time (US and Canada).

This transcript is auto-generated, so some information may be inaccurate. It won’t be surfaced in search results.
@Matheus Izvekov [6:59]: Requires the C++. Sorry I got interrupted here. if we're doing that in the our own fork, our own reefer, right? Then like those full requests are not gonna get merged anywhere. They're just gonna sit there till they're ready and then we're just going to close them and submit the same branch through the upstream repo as a new poll requests if that, that's like my understanding, of the process that we we're going to be slightly misusing

@Matheus Izvekov [7:32]: All replies because technically that's I guess it's the only way to interact with the AI properly, I guess. I don't know. So, the, the other point, is that like, it, it wouldn't be ideal, to understand what points, like human review comes in, you know, it's like the way that I'm envisioning in this process would work best.

@Matheus Izvekov [8:02]: Would be like the Author works with his, you know, changed and the AI feel like he feels that's ready for human review, right, for even other people from the C++ Alliance to review, right? And at that point, I, I think like the, the

@Matheus Izvekov [8:25]: Full request will be ready enough to like be submitted to the LVM project, but I was a poor request there anyway, and then we can start woman review over there so like if we can put like split those domains up, you know, then we're sure that we see like poor requests in the C++ alliance, LVM report them, you know, like we're not supposed to reveal this only AI reviewing.

@Matheus Izvekov [8:55]: And then when that goes to LVM project, then everyone reviews. I, I think that makes most sense and avoids splitting the review up or like new people coming up through the review, they like. Ask for a change or, or something that has been discussed previously, right, and like we split that up, you know, then we're gonna be repeating ourselves, right, as well. That, that's another problem that that I wanted to like avoid, at least like splitting the human review of, you understand.

@Vinnie [9:32]: Well, yes, OK, so, that's a good point. That's a very good point. We don't want to split up the review. However, we need to recognize that the workflow that we're envisioning, it has, there's there's two There's two parts of the workflow, right? There's the review of the AI generated code, and then there's the review of the approved code. So these are two fundamentally different things that require different skills because AI generated code looks different from code that you get in a pull request in the upstream repository, and the author is aware of that and also, you know, Christian, the people that are on the team, they're going to review the AI's work. So that's a fundamentally a different skill. It'

@Vinnie [10:15]: S related, but it's a different skill. So because the, the eye can hallucinate and also the way that we correct the things in the AI generated pull request is different than how you correct with the human. So we use our repo to capture that part of the process where that's specific to the AI workflow. Then once we feel that it's ready, that it's done, and that it's polished, then we move to the human part. That's when we submit the pull request to the LLVM. That's why I feel like we do

@Vinnie [10:45]: Need to have the separation. Now maybe you're right, and maybe I'm wrong, and maybe in the process of like we deploy the system, we discover, oh, the AI is just like another person. It's it's just like having another contributor, and it's, you know, maybe we set up some rules where we could improve the quality of its output because you can, you know, you can control how it writes code. You can tell it some rules. You can, you can teach it about your code base so it does things the way that you want. Maybe it gets to the point where the AI is equal in terms of being a contributor as everybody else, and then

@Vinnie [11:15]: We might change our workflow. However, if there's one thing I know is we have to move cautiously. We have to be very ethical, and we have to move responsibly. So the two repository structure is specifically designed to allow us to move slowly to anticipate problems before they get exposed to the upstream repo. I mean, what do you think is that, is that good? Can we, can you work with is that good? Is that OK?

@Matheus Izvekov [11:36]: So I, I, I, I understand. So like, I, I'm still like trying to like, Think, I, I guess the, that's like only something that will figure out the experience like if, for example, Christian, you know, like, as Laba to create like a full request based on his pro, you know, then like does anybody like needs reveal that, you know, besides Christian, right? Like the do we need to get like multiple people involved with like just,

@Krystian [12:08]: No, the

@Matheus Izvekov [12:14]: You know, like, you know that like low hanging fruit, you know

@Vinnie [12:17]: Let me, let me answer that. Let me, let me answer that. So that's a, that's a great question. So I think everybody, all the contributors to Clang, they have expertise in a specific area. For example, you are an expert with templates. Me, I am not an expert with templates. I'm an expert at Mr. Docs. So like if I was contributing and I tried to address an issue that had to do with templates, and the AI produced some output. I would look at it. Maybe I'd say this looks OK, but I wouldn't want you to look at it too.

@Matheus Izvekov [12:19]: Yeah, yeah Mhm.

@Vinnie [12:46]: Because you're an expert

@Matheus Izvekov [12:46]: Oh yeah I see

@Krystian [12:49]: So ideally, can you hear me?

@Matheus Izvekov [12:49]: Yeah Yeah

@Krystian [12:52]: Yeah. OK. So ideally this like acts as a tool for like assisting you. So you, your domain-specific expert, so you use this tool to open an issue and you have the AI give you a preliminary response and then me, you, and like,

@Krystian [13:09]: Possibly Vlad and other people, we review that and then once we're confident that this is like up to our standards and we all believe that this is sufficient quality to submit to LLVM then we submit it, because we don't want to just like

@Krystian [13:26]: Have somebody Prompt the AI to fix issues. Without review and just send it straight to LLVM because Who knows what is going to be in its response, and

@Vinnie [13:40]: Let me ask, let me, let me add some, let me add some more color to that. OK, Mattias.

@Krystian [13:41]: I got lost Yeah.

@Vinnie [13:46]: Some issues are easy to fix that like Christian has discovered, the AI can once shot it. It fixes the issue, and it's done. I've experienced it myself. It's been able to create, it's created working implementation the way that I want for me on the first try. However However, sometimes when you want to fix an issue the right way, you need to refactor. You need to maybe you need to rearrange the responsibilities of some classes. Maybe you need to reintroduce a new algorithm, and then you need to go through the code and you need to do things. Those types of decisions cannot be made by the LLM. They have to have a human, and the process that Christian is talking about is you use the AI to explore, Hey, if I refactor this, what would it look like? If I refactor, if I do this, how many pieces of code have to be touched?

@Vinnie [14:31]: It's very good at answering that question. It's not very good at having the imagination to figure out what the refactoring is. That's why we need the humans. So part of the review process for the complicated cases, which those are the interesting ones is the experts, you, Christian, Vlad, you get together and you say, how are we going to refraction? What, how should we, what's the best way to fix this bug, but not at the low level of individual statements, but at a high level like, you know, do we use a do we use an observer? Do we use

@Vinnie [15:01]: A generator? And then you use the AI to create a hypothesis. What would this fix look like if we did it this way, and then you review that, but we do not want to expose the upstream to this process. We want to do this experimentation and shit on our own. We don't want to get people worried. And then once we get it right, then once we see what we like, then we prepare the pull request to our repo. We get it the way that we want. We make sure the comments are all right. Everything looks good, and then we go through that workflow. It's very exciting. It's very exciting

@Matheus Izvekov [15:32]: Yeah, I, I mean, so like, another point is that like the Human like the us, you know, like that we need to be able to respond or account for everything that the bot does, right? So I, so, so like, for example, if we come up, you know, like go to all of them, review, and they're like someone

@Matheus Izvekov [15:55]: Suddenly we have to ask the bot, you know, like, what's going on here? Why we did things this way. That, that, that, that would be bad, right? so like, we definitely want to avoid getting to that position, right?

@Vinnie [16:08]: OK, so you know what, so listen, this is a beautiful conversation. I'm so glad that I'm recording. OK, so what Matias is saying is that when the, when our pull requests, when we believe our pull request is ready and then we submit it to the upstream, we need to be able to answer questions. So Christian, what that means is part of the workflow is that when, when we're ready, like when our poll request is ready, we have the AI generate

@Vinnie [16:31]: A a big description, a full explanation of the change, why it's safe, the deep analysis of all the code that gets touched, you know, how it proves that it's correct. We get that whole analysis and then we look at it and we verify that as well. So now we might say that a pull request is not only a set of patches to the code, but also we have a markdown document that explains it, and that is good for us to understand it so that we make sure that it's right. We can also provide that to the

@Vinnie [17:01]: Reviewers so that they know our rationale. That's a really good suggestion, Mattis. Thank you.

@Krystian [17:07]: So, I think, so well Mate was Matteus, Mateus, I'm not sure how to pronounce it, but what, what you saw is just the, the, the output, but I, there's also like reasoning from the chat agent that can be included in their polar requests, so it's not entirely a black box. It does.

@Krystian [17:27]: Tell you How it got to its solution. So that just needs to be included in the poll requests. Right now, I just, I just opened those myself for testing purposes just to see if it would pass CI and stuff. But in the, yeah, in the future, it's, there's no problem including the AI's reasoning.

@Vinnie [17:44]: Christian, I think for you, so now that you have a pull request up in the alliance repo, I think you should generate the rationale document and you could.

@Krystian [17:51]: I already have that. I have that I'll add it.

@Vinnie [17:53]: Can you, did you include it in the, in the pull request?

@Krystian [17:55]: Yes. Sure

@Vinnie [17:56]: Let me see what that looks like, OK, let me see what you got there. I don't see it Is it in the

@Krystian [18:06]: I'm adding it right now.

@Vinnie [18:08]: As, but added as a reply, don't put it in the branch.

@Krystian [18:12]: All right.

@Vinnie [18:12]: Oh, what the hell, man? This, this patch is tiny.

@Krystian [18:17]: Yeah, no, so the patches I'm working, I'm focusing on right now that I found that the AI to be best with are those like single line errors that cause a crash somewhere. It's great.

@Vinnie [18:27]: That's amazing, that's, that's crazy, really?

@Krystian [18:30]: Yeah, because you have a stack trace, you have

@Vinnie [18:33]: But

@Krystian [18:33]: You have a code example, it's really good to get.

@Vinnie [18:35]: OK, I wanna see, I wanna see the, I wanna see the analysis. Please, please, please, paste it, paste it, paste it, paste it, paste it.

@Krystian [18:39]: All right, all right. Let's I'm working. Is there a way to copy the plan because it's, it's rendered markdown. If I copy the markdown, will it be already formmented?

@Vinnie [18:44]: Yeah. So she bought a copy what you wanna copy the plan?

@Krystian [18:50]: Yeah

@Vinnie [18:51]: OK, so you got a right click on the tab and you got to say open and file explorer. And then you've got to take the file and you got to open it and you got to drag it into the browser and

@Krystian [18:59]: I'll just drag drop it here. Here we go.

@Vinnie [19:00]: Yeah. That part sucks. Usually I don't share plans. Usually I ask it to make a report, so you can say generate a report based on the plan that can be useful for somebody who needs to understand the code and the rationale. You can just ask the AI and to give you whatever you want.

@Vinnie [19:18]: OK, where is it

@Krystian [19:19]: I sent it in a CPPA claim.

@Vinnie [19:23]: So why didn't you attach it to the issue?

@Krystian [19:26]: Because I was just opening those issues quickly just to for experimentation purposes, just to see if it works.

@Vinnie [19:31]: That's super irritating. OK, I'm gonna respond. I'll, I'll, I'm gonna face.

@Krystian [19:32]: Sorry man Oh yeah, no, those are, they're, that's why I opened them as drafts initially. You can have.

@Vinnie [19:36]: There, there, OK, so Mattius, here it is Problem analysis Right The crash occurs when Oh, the failing assertion, Jesus Christ Christian, it knows, it fuck fucking it knows root cause, oh my God, get constrained. This only goes now, man.

@Krystian [19:50]: Yeah, it's, it's actually really good.

@Vinnie [20:00]: Wow, solution. Holy shit! Mantis, do you see this? Do you see this shit?

@Krystian [20:07]: So, and, and Matthias, I know you commented on this issue.

@Vinnie [20:08]: God, that's great. That, it gave, it gave you the test as well.

@Krystian [20:13]: Yeah, no, it always gives you a test case. I found

@Vinnie [20:17]: We're done, we're done.

@Krystian [20:21]: So, Matheus did comment on this pull request, and I still have to review his response.

@Vinnie [20:27]: OK, here's how you do it. You copy his text and you paste it into the so when, when, OK, let me explain something. So when you ask the AI to fix something, like when it comes up with a plan and then when you press build and it applies, you know, the plan, it has the information in its context. So that's what we call a rich context. If you ask it any questions in that context, it will know. So the best way to address Matius's point is in that dialogue that has that context where it applied the fix co

@Vinnie [20:57]: P y what he said, Go into ask mode, and then just paste it.

@Krystian [21:00]: Yeah, I did that. I have a response already. I did that like.

@Vinnie [21:03]: Oh God

@Krystian [21:04]: 20 minutes ago.

@Vinnie [21:04]: I want to see the response. Can you paste the response?

@Krystian [21:07]: Yeah, I'm gonna do a screenshot because I don't know how to copy paste it, you know, formatted manner.

@Vinnie [21:12]: No, just, no, please, no, don't take a screenshot. Copy the markdown, do it the right way. I want to establish a good workflow.

@Krystian [21:14]: OK, sorry Well, there's some marked down. I could put

@Vinnie [21:20]: Where is the text?

@Krystian [21:21]: It's in the chat window.

@Vinnie [21:23]: Share your screen and I'll show you

@Krystian [21:25]: All right, splendid. Sorry, one second

@Vinnie [21:39]: That's OK, take your time. This is really, this is all terribly exciting. We're gonna be the we're gonna beat GCC and MSBC. Oh, that he did the opposite of, oh, there it is. I want to work, I want to close every open issue in Klang.

@Krystian [21:54]: Hm All right, you see my screen

@Vinnie [22:00]: No

@Krystian [22:03]: Bye bye now. Oh, it

@Vinnie [22:06]: Stop for a second

@Krystian [22:07]: Oh XDG desktop portal KDE closed unexpectedly. Let's try that again.

@Vinnie [22:14]: Well, if you put the cursor in the chat area near the bottom, you'll see a little 3, you'll see like 3 dots, like it'll be like a little dot here, and I'll show you on my screen.

@Krystian [22:22]: Yeah, no, I'm sharing my screen, it's just like the I'm using, I'm on KDE right now, so it's.

@Vinnie [22:28]: Now, let me show you, I'm gonna just show you what to do, OK?

@Krystian [22:32]: All right.

@Vinnie [22:33]: Read Street there. OK, so you see my, you see my chat.

@Krystian [22:37]: Yeah.

@Vinnie [22:37]: You see these three dots, you just say copy message, then you'll get marked, you'll get marked down.

@Krystian [22:39]: Oh, I see. OK, cool.

@Vinnie [22:44]: And take that mark down and paste it as a reply in the issue, please.

@Krystian [22:49]: Yes, sir

@Vinnie [22:50]: And, and at Mattis, so he knows you're replying to him. This is so crazy. This is so good. I wonder what this could do for Mister Docs. Allan is using AI like I know he's huffing that shit hard. Like he's, he's so dude, that guy's, oh, there it is.

@Vinnie [23:13]: That's a good point. Oh, that's the AI talking. Oh my God, Mattias, it answered you. You're right. Oh, you're right, dude, whenever the AI tells you something like that, it means you're getting a good answer.

@Krystian [23:26]: Well, actually, in this particular case, there's actually some, there's a lot of Nuance in this situation because trying to get the correct pattern for an instantiated declaration is actually very non-trivial, especially when you account for like modules and like explicit instantiations that are defined in a different module.

@Krystian [23:47]: That's when things get really difficult. So I guess for, for human review, this is, this still would take quite a while, just for verification purposes, but it is definitely a good response.

@Vinnie [23:59]: To

@Krystian [23:59]: What do you think,

@Matheus Izvekov [24:01]: So is someone sharing a screen right now because I, I, like I only see your faces, your pictures, and you talking,

@Krystian [24:01]: Bias Oh, here, I'll link the issue.

@Vinnie [24:11]: Hold on, hold on, hold on. Mattis, it's the issue. Open the issue. I put the link in the clangtown and see.

@Matheus Izvekov [24:15]: 000, OK, OK, so I should be, OK. I, I thought someone was gonna share it again.

@Vinnie [24:21]: So So there's the issue, you can see So, so by the way, this is what, this is what the dialogue with the bot is going to look like. You're going to interact with it through GitHub.

@Matheus Izvekov [24:33]: Yeah, so like one weird thing here is that like at least like the way Christian did this year. So it's all not clear, you know, like who's talking, right? Zac Christian, or is that the board? Like, could, could we have like the book as a person.

@Vinnie [24:33]: Like it No, no, this is full this is full.

@Matheus Izvekov [24:51]: The bot as a person in the GitHub, you know, like putting these comments in his own name because that don't make things clearer, right?

@Vinnie [24:58]: Yeah Yes, yes, Mattias, so you'll forgive, you'll forgive me if I haven't yet deployed the cloud instance necessary to make that happen, but I like that I like that you're requesting the feature that we plan on deploying. Thank you. That sounds like you've got buying.

@Matheus Izvekov [25:07]: Oh yeah Oh yeah Oh yeah, oh yeah. All right. yeah. So, I have a, a little thing, in my mind, so, there's this thing about in Alge projects about how we like grade importance of issues of LA issues that are basically like compiler crashes. They're like fuzzy generated. They're like the lowest priority thing for us to fix, right?

@Matheus Izvekov [25:45]: And above that, like you could say, a light crashes, like yeah, crash on the valets or especially crash on the valets after, you know, like a, an error has already been emitted right like a crash on the air recovery situations. So like right now, like the, the examples that that we're dealing with here are are these kinds of issues, and one thing I remember many years ago, Richard Smith talking

@Matheus Izvekov [26:15]: About like fuzzy generated, you know, issues in playing, you know, like discouraging people throughout, submit them because basically he said, oh, like we need an army of engineers, you know, like to fix all those kinds of issues, right? And you know,

@Krystian [26:32]: He's your onions

@Matheus Izvekov [26:34]: Sorry

@Krystian [26:35]: Here's your army

@Matheus Izvekov [26:37]: Yeah, yeah, yeah, yeah, that's what, what I was thinking, you know, yeah.

@Vinnie [26:40]: Let you, let me ask, let me ask you a question. So it sounds it sounds like you're telling me that there's like a priority. There's a, there's a categorization of where the priority system. Is that written down or is that only in people's head?

@Matheus Izvekov [26:51]: No, that, that, that's not recondolence. Basically like a greed upon thing, like I I I don't remember that, that, that they never been rich enough. But I, I mean, it is, it is kind of logical, right?

@Vinnie [26:57]: Yeah, that part is. Please Wait wait Up. Please, I, OK.

@Matheus Izvekov [27:05]: So sorry

@Vinnie [27:07]: Slow down I didn't understand you. Is it, is it yes, it's written down or no?

@Matheus Izvekov [27:08]: Yeah No, no, it's not written down. It's just past knowledge, right?

@Vinnie [27:16]: And so, so then what we do is you interview the people, like what I did with you, and you get them to talk about what's important and what's not, and you get them to talk for an hour and then we record all that and we get the transcript and then we can turn that into a document where we can like any anything that you can get people to talk about with their experiences with the compiler, how do you fix things? What's important when you look at in a review, what makes a good, you know, all that stuff we can capture all of that knowledge

@Vinnie [27:46]: And we can teach the AI, so that means if you talk to your friends, you know, your, your colleagues or your other implementers in the compiler, and you can get them to talk about, for example, like what's the priority? How do you identify what bugs are easy or hard? How do you identify how much risk if you can get them to talk about that for a few hours, then we can take that information and we can turn it into a rule, and we can have the AI will be able to look at an issue and evaluate it according to the human framework, and it will say this

@Vinnie [28:16]: Issue is risky, this issue is easy and high yield, then we can do all of that is perfect for AI. Like AI is very good at that. It's very good at those patterns.

@Matheus Izvekov [28:25]: But But it's some sense, this information is already available, right? Like what I'm mostly talking about like discussion in issues, right? So like, this is like for the I wanted, it could like grab through all the discussions in all the issues, you know, like it, it would need to figure out, you know, like what, what people, they need to take seriously, right? Like first some like Richard Smith, like you, you, you should give a lot of

@Matheus Izvekov [28:56]: Weight to his opinions and things like that, you know, like, all I'm talking about is not just like talking like this on Zoom, right? Because we almost never do that in the old project. Almost everything's like talking through issues, right? Yeah.

@Vinnie [29:11]: That's fine from the Mattias, Mattias, this is, this is actually great. I love, I love where you're going with this. So, so part of, part of the capturing knowledge system is I have developed like a much larger system, and

@Matheus Izvekov [29:13]: Yeah

@Vinnie [29:32]: OK, so what you're talking about is reputation. So I have an agenda, I have this very this is very big, sorry for the size, but so this, this idea for Klang is part of a larger concept, an agentic workflow that is applicable to any problem domain, and one of the things that we have in there is expertise scoring, OK? That means not all feedback is equal, a correction from a 30-year language veteran carries more weight than a suggestion from a newcomer,

@Vinnie [30:02]: Right? So, so I have a I have all the specification in here for how the AI can measure signals of expertise. For example, you know, we can calculate like a score, and this can be calculated by looking at the history of a project. Like when we see, if we look at the commit log and we see that one like Richard Smith, we see that Richard Smith is involved in many, many commits, and we see that when he commits something or when he approves of something that it doesn't come back with the same bug, and we see that like that when he's involved in the conversations

@Vinnie [30:32]: Like he, his, his hypothesis tend to be correct. We can calculate that with AI, and we can assign a score, not just in one category, but the AI can identify what the person is good at, right? So if we have an army of volunteers, we can route issues and reviews to the person who's already an expert. The AI can do all of this. It's very well within its domain, OK? This is the domain classification, right? So, when a contribution comes in, by the way, this is for WG 21 papers, but it's

@Vinnie [31:02]: It's applicable to client contributions. It's applicable to anything. We can develop an entire system is my point. So like everything what you can imagine is possible. You you no dream is too big.

@Matheus Izvekov [31:19]: Oh yeah

@Vinnie [31:21]: I gotta go to lunch, but this was fun. I think this is very exciting. This is awfully exciting, Christian. Very good, very good stuff. All right, y'all, can you all get out so I can get the transcript and then I'm going to do the knowledge capture on this conversation and then share it.

@Matheus Izvekov [31:38]: All right.

@Vinnie [31:38]: Because I think a lot, a lot of good stuff came out of it.

@Matheus Izvekov [31:41]: All right. All right. See you then. Thank you.

@Vinnie [31:42]: And it.