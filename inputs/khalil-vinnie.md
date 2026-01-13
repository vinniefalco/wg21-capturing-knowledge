Transcript of huddle in kammce on Jan 13 from 11:00 AM to 12:23 PM Pacific Time (US and Canada).

This transcript is auto-generated, so some information may be inaccurate. It won’t be surfaced in search results.
@Vinnie [0:51]: On for yeah. Like. We're human

@kammce [0:55]: Yes, yes, yes. Actually, I, hold on, give me one sec. Give me one sec

@Vinnie [1:06]: And I'm done with video. OK, that's enough of that.

@kammce [1:09]: Also just confirming that, you know, I am, my, is my face here. Hello, yes, I am also here.

@Vinnie [1:13]: My man's, yeah Wait, let me see your shirt

@kammce [1:18]: Oh yes, the Conanfargarian shirt.

@Vinnie [1:21]: I love it OK

@kammce [1:24]: Oh. Let's take a look

@Vinnie [1:26]: Deep breath. OK, did you read the paper?

@kammce [1:29]: OK, so I, unfortunately, I read like parts of it. I had some other things I had to do today, but I, I got some idea from it.

@Vinnie [1:33]: That's OK It's very exciting, isn't it? Does it says everything you want to hear. Am I wrong

@kammce [1:42]: I think, I, I think it's very similar to It, from what I, from the little bits that I read, it, it has this vibe similar to that of like Zig's IO object. I feel like there's like something along those lines here, but if you could kind of go through it with me, that'd be great.

@Vinnie [2:00]: Right, so first of all, this is a ground OK. The whole concept of this thing, can you see my screen?

@kammce [2:03]: Mhm Yes, I can

@Vinnie [2:08]: It's called JUCB.

@kammce [2:10]: OK.

@Vinnie [2:11]: That means just use co routines, bro.

@kammce [2:14]: I think that, yeah, I agree, I agree. Uh-huh.

@Vinnie [2:16]: Yeah, well, you know, for the last 3 years I've been disagreeing and I've had to hear Peter Dimov like so it's so irritating he's saying this shit all over again and I'm like, you know, I like C++ 11 a lot. It's not that I'm a it's not that I'm opposed to CO routines. I'm, you know, I'm not, but I wanna have a wide audience and also I was afraid of co routines because they're very complex, but

@kammce [2:28]: Mhm Yes, yes

@Vinnie [2:39]: So I asked Peter a question about, you know, how do I, because I'm building the server and you know I'm trying to copy Express JS and the asynchrony is very easy. Like you could say, oh wait, and there's no controvers, you know it's very smooth in a way that C++ is not. And so there was like some design pressure that's pushing me towards co routines to make my APIs look nice.

@kammce [2:49]: Mhm, mhm. Mhm, mhm

@Vinnie [3:02]: Like, let me give you an example, like,

@kammce [3:03]: Yeah, show me

@Vinnie [3:04]: So you have like, you know, these two. Application, you know, you have your app and then like you initialize it and then you go app.use And then serve static.

@Vinnie [3:27]: And then you're done. So now you've just put up a website.

@kammce [3:32]: Yeah, that's good. Yeah, yeah.

@Vinnie [3:34]: So, So surf static is what they call like middleware.

@kammce [3:38]: Mhm

@Vinnie [3:39]: And, and then, you know, it doesn't stink, but what if you want to write like What if you wanna have your own route handler, so you might do this.

@kammce [3:46]: Mhm

@Vinnie [3:47]: You might say I can't remember the syntax, but Oh yeah, let's just do it like this. Sorry, this is, this all looks very laborious compared to the to the JS version I know.

@kammce [4:07]: No worries. I mean, I actually don't think it's that bad. But I'm also, you know, I'm supposed to go over, so I got used to verbosity.

@Vinnie [4:15]: That is really like a sad thing to hear. OK, so now, here we go. So now we're just going to say co Return I guess. I'm not that good at it. And then we're gonna say RP.status 200.sends

@Vinnie [4:34]: Boom So now we just, now we just sent an HTTP response, right?

@kammce [4:35]: Mhm Yup

@Vinnie [4:40]: So OK What was I gonna tell you now? So we want, this is what we want. Like we want to have like this flexibility, we want to have like this convenience, like there's no socket here. OK, great.

@kammce [4:47]: Mhm

@Vinnie [4:52]: OK, so, so let's talk about Let's talk about the paper So for for the networking IO You need, you need 3 things You need to control where the co-routine executes.

@kammce [5:07]: Mhm

@Vinnie [5:08]: You need to control When you need, you need to be able to cancel IO, right? So you need to cancel signal. That's number 2. And number 3, and this is probably the most important. We must control how the co-routine frame memory is allocated and de-allocated.

@kammce [5:23]: Mhm

@Vinnie [5:24]: That's like the number one rule. So the way that this whole thing was started was just use co routines, bro, was I was gonna, I want to shut Peter up and I want to show him how callbacks like suck.

@kammce [5:26]: Yeah.

@Vinnie [5:35]: But

@kammce [5:35]: Mhm mhm

@Vinnie [5:36]: A funny thing happens. I found out that they actually, they actually don't suck. In fact, they're rather good at some point. And the reason is because In ASIO

@Vinnie [5:52]: When you, when you compose, you have like that you have the completion handler and which is really the operation state and every layer of composition, it grows the size of that struct, right?

@kammce [5:59]: Yeah Yeah

@Vinnie [6:04]: And If it's small, if you only have like one layer, like it's fast, it's great, but you know what, guess what? Every layer you have to do a move. You have to do like a me move. You have to do, you know, stood move into a bigger and bigger struct, and that shit starts adding up like those bits that mem copying at each layer, it starts adding up and there's a point where the co routines become better.

@kammce [6:25]: Hm.

@Vinnie [6:26]: Because the co routine callback a quote, you know, air quotes, callback, it's only a pointer. It's just a cover routine handle.

@kammce [6:33]: Yeah.

@Vinnie [6:34]: So if you have 5 layers of composition in ASIO, that could be 500 bytes, whereas if you have 5 layers of composition with co routines, it's only 40 bytes.

@kammce [6:43]: Gotcha, gotcha. OK

@Vinnie [6:45]: OK, so Where are we? I hm Hm. OK So, we want We wanna make sure that execution Happens under our control. Why? Because

@Vinnie [7:03]: First of all, we don't want to use locks. We want to have the model of concurrency where we use like the strand, you know about the strand?

@kammce [7:11]: Grand. I'm not sure it's my brand.

@Vinnie [7:14]: OK, so let's say So when, when you're doing, when you're doing asynchronous IO you have what's called a reactor. And that is an operating system level construct that informs you when your operation is complete, right? Pretty simple.

@kammce [7:28]: OK.

@Vinnie [7:29]: And of course we, we wanna have multi-threaded react. We want to support multi-threading, so we don't want to have We don't want to be responding to completions on just one thread. That's how node does it. That sucks. We want to have multiple threads. So if you have multiple threads That are processing IO

@Vinnie [7:47]: And you have like some object, right? Like some, let's say you have like something getting quotes from, you know, like a, an exchange. You're set, you're doing reading and writing. You want to make sure that You're not accessing your data from two different threads at the same time.

@kammce [8:04]: OK

@Vinnie [8:05]: So you want to make sure that when you're doing that IO that when you're doing that reading and writing, like when it completes, you want to make sure that any of your other operations, they're not running at the same time. So that's called a strand And a strand is a type of executive. It basically it's just a policy for how, how, your completion executes. Do you, do you understand what like what a completion is?

@kammce [8:30]: So this is, this is me trying to dig up my old knowledge of standard exact, which Like I kind of said before I haven't fully grasped it yet to go for it, yeah.

@Vinnie [8:41]: That's OK. I can listen, no problem. I'll explain it. OK, so here's the, here's, here's what happens. You you call the operating system to do something.

@kammce [8:51]: Yeah

@Vinnie [8:52]: Your co routine is suspended.

@kammce [8:55]: OK

@Vinnie [8:56]: Now you go about your business and then at later at some point later, the operating system, it finishes, and now it has to inform you. It has to say, hey bud, you're done, we're done here. And it has to, it has to resume your co routine. That's called a completion.

@kammce [9:10]: Mhm Gotcha

@Vinnie [9:13]: Right? So for example, if I do a read, if I do an asynchronous read, your co routines is suspended. The operating system takes over, it performs the operation, and then when it has the results, now it, it resumes your co-routine. But here's the problem. I know what you're, I know what you're thinking, but Vinny, what thread is your co-routine resumed on, right?

@kammce [9:33]: Mhm, mhm, yeah

@Vinnie [9:35]: So, In, in, in, in this system, co routine first We, we launch, when you launch a a co routine launch like this, you say as sync run. You see, see at the bottom

@kammce [9:47]: Yup

@Vinnie [9:48]: And, and you choose your executor, and then you have like, you know, like my task. That's how it's launched, and then This, it's we call this a dispatcher. The, the, the The invariant is that

@Vinnie [10:05]: Co-routines will always be resumed Using the dispatcher And the dispatcher is just a function object. That it looks like this And it takes a co routine handle. And it returns a cover routine handle, for that's what you put in, that's what you put in like your await suspend, you know, whatever that, all that crap, you know what that crowd.

@kammce [10:23]: Gotcha. Yeah. Mhm Yeah

@Vinnie [10:29]: So, so, and this factor is just a function object that takes a co routine and it returns a co routine. That's it.

@kammce [10:36]: OK.

@Vinnie [10:36]: That's it. That's all there is to it. This is, this is the alternative to P 2300, by the way.

@kammce [10:44]: OK

@Vinnie [10:44]: It's just that. OK, so EX is that dispatcher, and the system, you want a system that guarantees that every time a co routine is runs Or it's resumed, it uses its dispatch through this executor. Get it?

@kammce [11:00]: Yeah

@Vinnie [11:02]: OK, so now So what does that look like? OK, so I've created a la, I've created a language or like I've created an annotation to describe that. OK, so For example, this is a this is a co-routine flow.

@Vinnie [11:18]: See that, see in the upper right

@kammce [11:19]: Yup. Mhm.

@Vinnie [11:22]: So what we have here is we have, you're doing a cult, you're doing an async run and the exclamation point means that like I'm using an executor. I'm saying this is the thread I wanted to run on And then I'm co-waiting another co routine. So far so good, right?

@kammce [11:37]: OK.

@Vinnie [11:38]: We want to make sure that that co-routine that you're co-awaiting is goes through your, your dispatcher. Now, on the way in, there's nothing to do because it's a symmetric transfer. You're already on the right thread, so there's really nothing to do here. You just pass it and OK, it's great. Now you do some IO. Now this C2 does a coweight on Wasaki to follow whatever. Now you're doing some IO. OK, now the IO completes. Now, guess what? Now we have to go back to C2.

@kammce [11:49]: Yup. Mhm. Mhm

@Vinnie [12:04]: So at that moment, C2 has to resume using the executor that was used to launch this entire chain.

@kammce [12:12]: Mhm

@Vinnie [12:13]: Do you agree? Do you agree

@kammce [12:14]: Yeah, makes sense

@Vinnie [12:16]: So, in the transition when we go from IO to C2, as long as the IO object, you know, follows the rules and it uses the executor, uses the dispatcher to invoke the co routine to resume it, then we're OK. Then when we go on the way back to C1, we're already in the right context. We don't need to switch because we don't want to dispatch every time. We only want to dispatch when necessary.

@kammce [12:36]: Yeah.

@Vinnie [12:38]: OK, so now here's my little stupid little language that like it explains all this. So. All right, here we go. Let's see what makes sure it's thinking, it's gonna do the right thing Here we go

@Vinnie [12:55]: Perfect See it knows, the AI knows and smart.

@kammce [12:58]: Hm, hm.

@Vinnie [13:00]: OK, so from this, by the way, just from this diagram, it knows how to write the code so you could see what the code is, right?

@kammce [13:03]: Yeah Yeah

@Vinnie [13:07]: So we've launched C1 with and we call this executor affinity. So when a co routine has affinity, it means that it it it wants to run on a certain executor. So look at the execution flow. This is exactly what I described.

@kammce [13:22]: Yep.

@Vinnie [13:23]: So when the OS signals completion, IO resumes C2 through EX. And here, when we go from C2 back to C1, it's a symmetric transfer, a tail call.

@kammce [13:33]: Yep

@Vinnie [13:33]: It knows OK So, but what about a more complicated flow like what if we've got this? What if we have C2, I have a function called like run on. OK, now we're back in this document. So I have this thing in a cover routine you can do like

@Vinnie [13:52]: I can say Co await run on. EX2 And then, you know, other other stuff. Right? So, here, where C2 is already has its own context from how it was launched. So now we're transferring to another executor and so that means that when other stuff executes, it has to go through EX2, and it has to follow all those rules that we just talked about on the and then on the way back it has to go to X2, but then when, when we, when this coweight completes when the when C2 is resumed, we need to be back on the original executor.

@kammce [14:10]: Mhm Mhm

@kammce [14:32]: OK

@Vinnie [14:32]: Because, right, there's an implied executor. OK, so what does that look like? I'm so glad you asked. OK, so let's, let's, let's figure that out. So and C2, we're doing another, we're doing another affinity and now we're going to go call like C3, and then we're going to call the IO object. All right, let's see what that looks like.

@Vinnie [15:00]: There we go. Let's see run on, it knows. Dude, it knows, man, and see itine was changed affinity. So, so here is the execution flow, right? When the aisle completes, we get a symmetric transfer back to C2, but when C2 goes to C1, we have to do the dispatch.

@kammce [15:10]: OK

@Vinnie [15:20]: Now I know what you're thinking. Like this is all very nice, it's all very like very textbook, but what happens if we want to delegate work to a foreign To a foreign thread pool first, right? So for example, OK, I want, let's talk about B crypt. So, something that like if you got, let's say you have a client, you say you have a web server, you're implementing a web server and you want to put a cookie on someone's ass. Like you want, you want them to authenticate, but then you want to give them a cookie and it's a bearer token. All they have to do is present it in the future and and you'll, you'll assume that they're logged in, and it sounds a little link, sounds a little dangerous, so we have to make sure that

@Vinnie [15:58]: That whatever token we give them is cryptographically secure. So there's a little thing called Bcrypt. So Bcrypt lets us generate like this really like, you know, strong encrypted token that proves that they had logged in at one point in time, but the call to be crypt is expensive. It can take 100 milliseconds. If we're doing and if we're in an IO chain, like if we're, you know, servicing sockets like we don't want to block the IO thread for 100 milliseconds. That would be bad. So we have to delegate that work to a foreign thread pool to do the B crypt operation. So

@Vinnie [16:28]: That looks like this C2, we're going to go down and we're going to call a foreign thread. Right? Well, guess what, that foreign thread might want to do another thing, right?

@kammce [16:35]: OK

@Vinnie [16:40]: Like, he might want to, and he might want to do like another operation and then, and then there's that. OK, so let's see what that looks like. Well actually, let's do the simple one. So let's see what that looks like

@kammce [16:41]: Mhm

@Vinnie [16:55]: Getting more complicated shit Oh boy. OK, so here Hold on, I did, I did the diagram wrong. I should have done it like this.

@Vinnie [17:13]: Sorry, I don't know how to do. I don't know how to use my undo.

@kammce [17:14]: Yes

@Vinnie [17:21]: OK, there we go OK, so here it's a foreign awaitable that it has its own ainity, so that's like another thread pool that has nothing to do with like IO. Like it's just like a regular thread pool. Things run, they finish. There's no operating system level like interaction, but you can see it here, right? Coweight F.

@kammce [17:25]: In interesting Please hold on, let's, let's let's actually kind of focus in on that coweight F,

@kammce [17:45]: It was your goal just to kick off F and then when it's done, then kick off. Wait, I'm a little, hold up. Oh that's in C3. Interesting. Is that a mistake on the AI side or was or was C2 supposed to kick that off?

@Vinnie [17:55]: OK. Right, so C2 Oh yeah, that looks wrong All right, so the AI this got a little glitch there. I mean, don't ask.

@kammce [18:06]: Yeah, yeah No worries

@Vinnie [18:10]: But, but I think you get the point, right? Like,

@kammce [18:12]: I I get the point. Yeah, yeah, yeah, that's what you're trying to do, yeah.

@Vinnie [18:14]: OK, so now you understand that. So Co-wrote first is it explains the affinity or no affhenoatables, it explains the affinity. Principles I hope

@Vinnie [18:31]: Sorry, I'm getting, I'm man. There we go, OK All right, so this is an explanation of how this, how that system works. Right? Like this is an explanation of the system, and this tells you, I mean, you can read all that crap, but at the end of the day

@kammce [18:49]: Mhm

@Vinnie [18:50]: It's right here The awaitable receives the dispatcher We take advantage of the fact that The lifetime is extended. So that we can type your race, we can type erase it at zero cost, and then we can propagate it forward. So like when we suspend we propagate it to the next one. So that means that when you do the Aync run

@kammce [19:03]: Mhm

@Vinnie [19:15]: On a, on a certain executor like that or on the dispatcher, it propagates through the whole co-routine chain all the way to the IO object. And it doesn't cost anything

@kammce [19:24]: OK

@Vinnie [19:30]: I I feel like I'm doing a very, I feel like I'm doing a very badly.

@kammce [19:31]: Got it No, no, I think, I think I'm starting to, I just 123. Can you hear me?

@Vinnie [19:36]: Yeah, I hear you

@kammce [19:38]: OK, cool, cool. I'm making sure the thing was messing up a little bit. I think I'm starting to get where I think I'm trying to figure out what you're, what you're, what you're doing here. Continue on, continue on. I think I'm getting it.

@Vinnie [19:47]: OK, so So, so if you look at co routines, if you look at co routines first, the principle, here's the thing that I, here's the thing that I discovered.

@kammce [19:53]: Hm.

@Vinnie [19:56]: You're never Halo's never gonna work. If you're expecting to, if you think Halo is gonna save you, you know, it's not gonna save you. you know, it's most compilers don't handle it well, and the clang, when it does, it doesn't always work. So, but the reality, here's the reality of it. It can never work for IO.

@kammce [19:59]: Yeah, I No Yes

@Vinnie [20:17]: Because at the end of the day, if you're calling into the operating system, right? If you're calling into the operating system to do something, and then you're, and then your co routine suspends

@kammce [20:22]: Mhm

@Vinnie [20:28]: You have to allocate memory

@kammce [20:30]: Yup

@Vinnie [20:30]: Because otherwise, you can never, otherwise you can never get back control of the thread that launched the operation, right?

@kammce [20:35]: Yeah Yup, yup. Mhm, mhm.

@Vinnie [20:38]: So if, if you have a thread and it launches an asynchronous operation that's underpinned by the operating system, that whole chain has to be allocated, period. And you know, it doesn't matter what you do, you have to allocate. So now we've accepted it, right? Like we've come to terms, we've come to Zen, and we said we have to allocate memory. So,

@kammce [20:47]: Yeah Mhm

@Vinnie [20:58]: What does that mean The allocation that we can't avoid can pay for the type erasure that we need, right? OK. What does that mean? That means here in a way suspend, guess what? This parameter

@Vinnie [21:14]: We're guaranteed that it will outlast our co routine.

@kammce [21:20]: Mhm. Yup

@Vinnie [21:21]: Do, do you agree?

@kammce [21:21]: Yup, yup. Yup. That makes sense

@Vinnie [21:24]: OK, did you know that before we talked? Like, did you realize that?

@kammce [21:28]: No, no, that's, that's what you brought up before when you the first time you brought this up, and I, I think I see where you're going with this and just, just to make sure this is clear. That ditch, that the dispatcher in this case, if we go back to your code representation on the right hand side, like that's your IO object. You're basically trying to feed forward that iolog object that you were passed in into the weight suspend, right? Or am I getting that incorrect? And please correct me.

@Vinnie [21:49]: No, that's not right. That's not right. That's not right.

@kammce [21:51]: OK, no worries. Tell me what's up.

@Vinnie [21:52]: Yeah, yeah, that's OK. So the dispatcher is actually You know, place to write something. OK, the dispatcher is here The dispatcher is this EX.

@kammce [22:09]: Sure

@Vinnie [22:11]: This is the IO object is the sock.

@kammce [22:13]: OK.

@Vinnie [22:14]: So one of the, so one of the revelations is that I've discovered in my research, and I think it's explained in the paper is that IO objects don't, they don't care about your Where they run. Like they run at the operating system level

@kammce [22:28]: Mhm

@Vinnie [22:29]: You know what I'm saying? Like They don't care, so You shouldn't bake You shouldn't bake the Executor into the IO object. The executor is actually the responsibility for choosing the executor is in your code. It's in the client code because only you know if if you're doing multi-threading. Only you know if you need to give some tasks, like if you need to give some IO higher priority than others. The socket doesn't know that. The socket only knows how to do three things connect, read, and write.

@Vinnie [23:01]: So it has to be told when it's done, this is how you dispatch my CO routine, and that's what this parameter is

@kammce [23:09]: Yeah, I think, yeah, go on, so.

@Vinnie [23:09]: So Yeah, so I call it an executor, but in afina waititables it's called a dispatcher, and the reason is because executors have more operations, but for the purposes of resuming co routines, all we need is that one signature, right? We just need the one, we just need that one thing.

@Vinnie [23:29]: Which is that dispatch function, hopefully I'll be able to find it, co-wrote first and maybe co-wrote first, OK. No, no, it's not coiners, it's affeatable. Sorry, I have never presented this before, so.

@kammce [23:42]: Yeah

@Vinnie [23:44]: So I you know, everything that I described is this, it's the lost context problem. This fully explains it. This paper explains it really well. It's very simple, and then it provides the solution. Which is here, this dispatcher, and then the dispatcher has Does it even say what the oh there it is here, there's the concept. That's it.

@Vinnie [24:03]: This is the concept

@kammce [24:05]: I'm, I'm, I'm a little confused here. Like, like how exactly is the dispatcher making its way to the await suspend, like, like what's the connection between these two. I see that you had your previous example with like Aync, you know, parentheses EX, and then you had some function at its calling.

@kammce [24:21]: Is, is it that the core routine already has access and like as a reference or whatever to that. The execution, like, yeah.

@Vinnie [24:27]: Great question, great question. So the question is, here's your question. The question is How does the dispatcher start and how does it propagate through to the end?

@kammce [24:37]: Yeah. Correct, yeah

@Vinnie [24:38]: And the answer is that every co-routine in the chain has to opt in to the Athenaweightable protocol, which is described in this paper.

@kammce [24:48]: OK.

@Vinnie [24:50]: So how do you opt in? Well, that's the paper tells you, check section 4 So as an awaitable, you implement the protocol to respect the caller's affinity, right? So in your awaitable, you put something in there so that when you're called with the parameter you respect it. That's the code that you saw. But then

@kammce [25:07]: Yeah you

@Vinnie [25:08]: Then when you implement a task Right? Like when you implement your task type, then you, you put in the promise, you put some logic to propagate the affinity forward. So the answer is that it's in the task.

@kammce [25:24]: OK

@Vinnie [25:26]: Now, here's the cool part. What if You run, what, what if you want to coaweight What if somebody gives you an awaitable, right, but they don't follow the Athena weightable protocol, right?

@Vinnie [25:42]: Like legacy code. OK, that sucks, but guess what? We actually have a solution

@kammce [25:42]: Mhm

@Vinnie [25:49]: For supporting Oh, by the way, here's here's the answer to your question the requirements like this tells you what you have to do to forward the dispatcher, right? Here's the instructions that you're asking a weight transform is the answer.

@kammce [26:01]: OK

@Vinnie [26:01]: I don't let full disclosure, I gotta give you a full disclosure, Khalilo. I don't actually fully understand it. I had the AI write all this.

@kammce [26:08]: OK

@Vinnie [26:10]: And so it, it can spit out that bullshit, you know, what I'm talking about, you know, do you know the bullshit I'm talking about?

@kammce [26:13]: OK I'm not sure which bullshit you're talking about.

@Vinnie [26:19]: That bullshit whenever you do something with co-routines, you end up with this big pile of slop. Here, let me show you

@kammce [26:23]: Oh yeah, no

@Vinnie [26:25]: Let me show you what I'm talking about. So here's my task.

@kammce [26:27]: OK

@Vinnie [26:28]: And my task is fun. My task is cool. Look how fun it is. Look, we've got all this stuff, you know, we've got well constructor and all looks very nice, but like then, like when you get to here and you got, oh, OK, here's this is, by the way, this is the stoppable protocol. This is a fina weightable with the dispatcher and then now augmented with the stop token, that's the second paper. Here's the first paper that you saw that here's the dispatcher, right? We've got our dispatcher. The caller's executor, we're saving away all looks very nice. But then something happens.

@kammce [26:37]: OK

@Vinnie [26:58]: Then you get to this thing and it's like, oh my God, what the hell is that? Oh, here we go. 00 my God, dude, what is this? What is all this? What is all this? Help me understand it, OK, here we go, here we go. This is the crap I'm talking about, OK. This, what the heck is this?

@kammce [27:06]: And then Just OK

@Vinnie [27:15]: That is

@kammce [27:15]: I mean, that's I'm about to be real, like that's us all the crap you have to do to get co-routines to work, like, just the final suspends a little long. Actually, what is your final suspend doing? I'm just curious, can you zoom in on it back again?

@Vinnie [27:28]: You see, now you know what the bullshit is.

@kammce [27:29]: I again That looks about right actually, I think, same dispatcher through yeah, not, yeah.

@Vinnie [27:41]: Yeah, and or

@kammce [27:41]: I mean like that's, that's.

@Vinnie [27:43]: Or this is the fun, this is the good part though. This is the collars. This is where we respect follower's affinity, right?

@kammce [27:46]: Mhm mhm Yeah, yeah, yeah

@Vinnie [27:50]: So when I say that bullshit, this is, that's what I'm talking about. I let the AI write this. I, I, I find all of this incredibly laborious. It's why I've avoided co routines, you know, but it's what we have, but this is not fun. But now that AI can do it.

@kammce [27:55]: Yeah.

@Vinnie [28:05]: So now the AI can take my ideas and it can turn them into something, you know, which is great. I can finally, I have a voice now

@kammce [28:10]: For sure

@Vinnie [28:13]: OK, so, so what makes this awesome? OK, so back to the key principle, the allocation we can't avoid pays for the type erasure that we need. That's that's principle number one of this whole philosophy. So principle number 2 is

@kammce [28:13]: Mhm OK. OK

@Vinnie [28:29]: Parameters passed into the promise functions. From the calling code routine, have a lifetime that extends beyond your frame. That is the key insight. So once you internalize that, now you can have type eraser that's for free. So how do we type erase the dispatcher? Well, as you know, it's just a, it's just a one function. So we capture the member in a pointer.

@kammce [28:44]: OK. Yeah Yeah

@Vinnie [28:58]: Right? So this can typerase anything, so there's no small buffer. There's no heap allocation as a fallback, right? This is, this is a fixed cost right here, boom, we're done.

@kammce [29:06]: Mhm, mhm, yeah

@Vinnie [29:11]: And This is what gets propagated forward because we can't propagate the original type, you know.

@kammce [29:18]: Mhm

@Vinnie [29:19]: This is what gets propagated forward, because if we propagated the original type, then the awaitable, then like the task.

@kammce [29:26]: Yeah, yeah, I get you

@Vinnie [29:26]: Template It would leak into the template parameter list of the task, and we don't want, we don't want that. That would suck, right? No, that sucks.

@kammce [29:30]: Yup. Yeah, yeah, yeah.

@Vinnie [29:34]: So this keeps your task clean. Your task is like spotless, bro. Like it, it's perfect. It does all the things and it's nice a nice API and you don't pay. It's it's this is the least amount that you can pay. Now,

@Vinnie [29:51]: Let's talk about senders and receivers

@kammce [29:54]: OK. just remember, I am, remember I told you I stopped, yeah.

@Vinnie [29:55]: So, No, no, no, no, no, don't under, don't worry. I don't understand here, but here's, here's what I do, here's what I do understand.

@kammce [30:01]: OK OK Mhm

@Vinnie [30:06]: There's a thing, it's called connect. OK, you see that

@kammce [30:12]: Yup.

@Vinnie [30:14]: That is the fundamental operation. In senders and receivers. It, it attaches the sender to the receiver, and this, and this function is a template.

@kammce [30:19]: Yes Yup

@Vinnie [30:25]: OK, and what that means is, and this has to go in the co routines, machinery and that, that big pile of bullshit, right?

@kammce [30:26]: Yeah. Yup Mhm mhm

@Vinnie [30:35]: The implications, Khalil Is that every type in the entire chain has to be visible at the call site of the Koaway. That means you can't have any, you, you can't hide any of your implementation. You can never be ABI stable. You're gonna, you have long compilation time.

@kammce [30:53]: Oh yeah, mhm. Yeah, no, you're right.

@Vinnie [30:54]: All Form The type erasure of this thing here is is ridiculous. It's crazy. It's in practical terms, it's not possible. That is the fundamental flaw of senders receivers. It's great for GPU. It's great for like heterogeneous computing, but it's exactly the opposite of what we need for networking, for IO.

@Vinnie [31:17]: So in this model, the way that the dispatcher works and the way that the type eraser works, you, we, we can actually type erase Everything Like sockets, everything, none of it is visible and everything stays in the TU. You can even switch, like you can change SSL providers. You can go from OpenSSL to Wolf SSL just by linking a different library and, and, and the libraries that you use that use like sockets and stuff like that, they don't have to be recompiled cause it's ABI stable.

@kammce [31:44]: Mhm

@Vinnie [31:50]: We do have a little, we do have a little problem though.

@kammce [31:50]: OK What's that

@Vinnie [31:54]: How do we allocate the frame?

@kammce [31:57]: Yeah, how do you go about doing that? What's what's your strategy?

@Vinnie [32:00]: Well, unfortunately, this is where things get like a little tricky.

@kammce [32:04]: OK

@Vinnie [32:05]: So, OK Let's take your basic operation, right? Like Spawn OK, at the bottom, I'm at the bottom of this file, right?

@kammce [32:18]: Yup

@Vinnie [32:19]: OK, if this is your main Like guess what, you're like you're already sunk because the moment that the compiler evaluates this parameter is now you've allocated a frame. Oops.

@kammce [32:25]: Mhm Mhm, mhm

@Vinnie [32:32]: Are you familiar with this problem?

@kammce [32:34]: Yeah

@Vinnie [32:35]: OK, so you know So now the question is, how do we get control? How do we get a handle on this thing? OK, so you know that like operator knew

@kammce [32:45]: Mhm

@Vinnie [32:46]: It, it gets forwarded the parameters like it could see this X.

@kammce [32:48]: Yeah Yup

@Vinnie [32:51]: So, you know, there people are like The allocator arg and you know, you know, like a, like a frame recycler on whatever.

@kammce [33:00]: Mhm

@Vinnie [33:01]: And like You know, we, we don't know each other that well yet. Like you don't know me that well yet, but I got to tell you, this doesn't really appeal to me

@kammce [33:06]: Yeah. OK.

@Vinnie [33:10]: Cause you know, what is it gonna happen here? We have to pass that shit in to every co-routine? Like what is that? This is how does this even work? First of all, what's that? I don't want to see that. That's unsightly. I don't need, I think it has to be like this. Or even this one, I don't think is any good. We need a, we need a, we need to construct it. So like this is not how I want to write my code.

@Vinnie [33:28]: OK, so what can we do OK, so Here's what we do in Cappy. We do async run EX, and then we put little parentheses. Now I know what you're thinking, Khalil, but Vinny

@Vinnie [33:44]: The compiler can evaluate this before this runs.

@kammce [33:46]: Yes Yeah

@Vinnie [33:49]: A little thing happened in C C+ + 17, it, it guarantees that this gets evaluated first.

@kammce [33:57]: Interesting. OK

@Vinnie [33:59]: OK, so what do we do? OK, now, now this is where things are going to get like a little dicey because how do we get the allocator into the operator new. The answer is we use a threadlo. So,

@kammce [34:15]: Oh, OK, all right

@Vinnie [34:17]: Now, now I know

@kammce [34:17]: I see. OK, OK

@Vinnie [34:19]: Now I look, I know what you're thinking. You're thinking like

@kammce [34:21]: Yeah

@Vinnie [34:22]: I know what you're thinking, you're like, I like I hear like that you're that defeated like Thread Local, because why? Because Tread Locals are problematic, OK. Thread local.

@kammce [34:32]: I'm almost at levels on the exceptions guy, I, I am building that into exceptions. So I'm fine with very local, but you continue on. You tell me what, but I I know exactly how you propagated it over now. You just pull it in.

@Vinnie [34:44]: Well, but see here's the problem with Dread Locals. The problem with Dread Locals is what happens in a currency situation because what happens if

@kammce [34:46]: Hm. You're swapping it, yeah

@Vinnie [34:52]: Yeah, what happens if your Co-routine switches contexts, like it gets resumed on a different thread. Like, how do we make sure that the value of that thing is the thing, OK? So, actually, I haven't answered, I have an answer for you.

@kammce [34:59]: Mhm. Mhm. Yeah

@Vinnie [35:10]: I got to find it. It's gonna be worth it

@kammce [35:12]: OK. Let me see

@Vinnie [35:14]: It's called The Window. Let me see if I can find it.

@kammce [35:18]: OK

@Vinnie [35:19]: Where the hell is it? Where's the window, the window, the window, the window, the window, there it is, the window. The window OK, let me, wait, I, I'm gonna give you a message on Slack

@kammce [35:33]: OK.

@Vinnie [35:33]: OK, you ready for this? Oh, the window.

@kammce [35:35]: Yeah.

@Vinnie [35:38]: The window By the way, just full disclosure, the AI figured all this out like I'm not like some kind of genius. This is the result of prompting. So I like I, after I taught it like how these stupid co routines work, and I asked it to find a window. What's the window where I'm guaranteed that the Thread Local is not going to change, and guess what, it found it.

@Vinnie [36:00]: And this explains it So

@kammce [36:03]: OK, let me check this guy Sure.

@kammce [36:23]: I'll just read through it real quick, making sure.

@Vinnie [36:26]: Huh

@kammce [36:27]: I'm reading through it really just to make sure It

@Vinnie [36:32]: That's good because, you know, you know,

@kammce [36:33]: Yeah Question,

@kammce [36:50]: Let's say that You actually, so I have a different way that I go about kind of doing my co routines, just in general. It's a, I think it's a different mentality than like the centers receivers and centerator exec. I'm not gonna go into too much here.

@kammce [37:09]: I feel like I'm trying to figure out like, so let's say, like, let's say you do, do you have a queue of co routines on a threat, because if you do, I'm kind of wondering how do you go about and when you resume one and then that one's blocked and you decide to resume the next thing in the queue, how that

@kammce [37:28]: Top-level co-routine ends up resetting the TLS. Do you, do, do you have that, described or so I'm not sure if that I get the fact that, you know, you're coaching actively running. That's when it sets the TLS. But when does, when you, when you resume again, when does that like changing of the TLS current allocator happen?

@Vinnie [37:46]: That's a great question. So I'm so glad you asked. So what you're saying, what you're saying is, but Vinny, this is per this is great. OK, like here we are in a sync run. So here, here's the spoiler alert. Ayc run returns an object which who's constructor sets the TLS and then

@kammce [37:50]: Yeah, yeah, let's go

@Vinnie [38:07]: It we're guaranteed that when this operator, because the thing that async Run returns is a funk object. That's why you see the, do you notice the syntax is a little weird here?

@kammce [38:11]: Yeah, yeah Yeah Yeah, yeah, yeah, you know, I, I, I know it's, yeah, it's a funkter, yeah, yeah, yeah, yeah, yeah, I get you, yeah.

@Vinnie [38:19]: See it, right? Like this is OK. Yeah, and by the way, you can't separate it like you can't there.

@kammce [38:26]: Yeah, you cannot, yeah

@Vinnie [38:27]: I put some, I put like some bullshit on the function to make sure that you're not allowed to capture that little weird thing. So it's, it's airtight So You're asking how does the allocator propagate through to the like if if my task it's another co routine, how does it propagate?

@kammce [38:42]: Mhm But actually I think I get it now. So you will create one, you'll run async, run EX creates creates an function object. You pass in the information you, after that point, you set the TLS variable, you now call this thing, it uses it for its thing.

@kammce [39:02]: Here's the next question, like, can you duplicate that line? Just so you're making like two A sync Yeah, I If you had changed the executor gear or whatever like that would then changes TLS for that duration of time. So I think I see where the, where the

@Vinnie [39:17]: No, no, no, no, no, no, no, sorry, I'm so

@kammce [39:18]: No

@Vinnie [39:20]: No, no, no, no, no. This uses

@kammce [39:21]: Nona.

@Vinnie [39:25]: This uses the default frame recycler. But if you want a custom one, then you do this. Sorry. You can pass your own allocator

@kammce [39:37]: Got you. OK

@Vinnie [39:39]: Now I know what you're thinking, but Vinnie, how do we guarantee that this allocator gets propagated to every co-routine in the chain because that's what you want, right? We don't want it just for this one, that would be stupid.

@kammce [39:48]: Yup.

@Vinnie [39:52]: So the answer is, it is, we have like a protocol in the task. So the first thing we want to do is we want to make sure that whenever a task is resumed, We put the allocator back

@kammce [40:06]: Makes sense. Yeah

@Vinnie [40:07]: And then we want to make sure that every time we're suspended, we put the we put the allocator in the TLS At the right time so that the co-regime that we're co-waiting uses it.

@kammce [40:15]: Yeah Yeah, that makes sense. I mean, it sounds it sounds straightforward. Yeah.

@Vinnie [40:19]: So here's So it's in here somewhere. I don't really remember it too well, but it's like it's tucked up in here. Where did I put it?

@kammce [40:30]: You search for TLS colon colon.

@Vinnie [40:32]: I don't even, I don't know

@kammce [40:34]: OK

@Vinnie [40:34]: I I think I wrote, I think I, I rolled it up into like a, a mix in. That you can inherit from Oh yeah, frame allocating base. You just slap that on your promise. And it does everything for you

@Vinnie [40:51]: You just derived from it, right? Let me see where that is. Oh man Damn it So sorry, it's like the anti-demo, OK, the task, the task.

@kammce [41:07]: Very good

@Vinnie [41:09]: There it is. So, all in your promise, if you want to opt in to the system, you just derive from frame allocating base.

@kammce [41:11]: Yeah

@Vinnie [41:17]: And then it takes care of everything, except, but you need to put, you need to stick a call in Near one of these things somewhere in here. Let me see where I put it. Is it in here? By the way, this is the tramp, remember I was telling you that if you have a legacy awaitable,

@Vinnie [41:35]: And like you coweight it and you want to make that little motherfucker respect the protocol even though they don't. You, you wrap their ass in the in the trampoline.

@kammce [41:39]: Mhm OK

@Vinnie [41:43]: And then, and then when they come back, when they resume you, you're back on your dispatcher.

@kammce [41:49]: OK, OK

@Vinnie [41:51]: Where the heck is this thing I don't see it. Is it possible that it's, that it's all in frame allocator, that would be nice. I think

@kammce [42:02]: Yeah, so, I mean,

@Vinnie [42:10]: Mhm. I don't see it

@kammce [42:15]: I mean, I see the new, the current allocator. I, I, I know, I don't see the part where it gets reassigned, but I bet it's somewhere in here. I mean, there's set frame allocator, I see that, and then clear it.

@Vinnie [42:25]: I'm, I'm so sorry to be.

@kammce [42:27]: Very good.

@Vinnie [42:31]: The AI wrote so much code, it's kept, got a little out of hand.

@kammce [42:36]: Yeah, that's one, that's one thing about AI generated code is a If you hadn't, if you're not the one who wrote it, it gets kind of hard to kind of search like, where did it put that thing?

@Vinnie [42:48]: Maybe I lost it

@kammce [42:51]: But no, I think, I think I get, I get your point though. I, I totally, I, I could understand how you can get to the point where it does the automatic handoff between the allocators between each invocation. So that makes sense.

@Vinnie [43:08]: Let's just ask OK, well, anyway, so But the problem of course is We have to store the allocator So this is where things get a little bit messy, right? Because we don't want that, we don't want the allocator to leak into the task type.

@kammce [43:23]: OK.

@Vinnie [43:28]: So the way that it works is like this.

@kammce [43:29]: Definitely, mhm.

@Vinnie [43:30]: It here's the co-routine frame. And then we store a copy of the allocator here.

@kammce [43:40]: Oh, OK

@Vinnie [43:42]: So the core routine at the top of the chain has the full allocator.

@kammce [43:44]: Mhm

@Vinnie [43:45]: Right? And we also store the deleting function. We also store like the delete function. We type erase that. Because

@kammce [43:53]: Mhm

@Vinnie [43:54]: Because as it propagates, we lose the type. We don't have the type anymore, so we need something, and this is just like the dispatcher. It's just a function pointer.

@kammce [44:02]: Yeah

@Vinnie [44:03]: It's a fun, it's 2, it's 2 pointers. It's the object for the allocator, and the funkin pointer. This supports state full allocators.

@kammce [44:10]: Mhm mhm

@Vinnie [44:12]: And then, you know, then the last thing that we need is the stop token, so we just put that in there. That's, you know, pretty straightforward.

@kammce [44:21]: Yeah

@Vinnie [44:21]: At parameter Oh, it looks like I lost it. Oh wait The allocator is not restored. The current implementation doesn't need it. Oh, because all qua routine frame allocations happen during the initial call chain. Oh, that makes sense. But there's no need to restore it on the resume because by then we've already been allocated.

@kammce [44:48]: It's, it's more that like, how do you manage when you have, when you've created multiple like separate coating frames on the same thread.

@Vinnie [44:48]: OK

@kammce [44:58]: Like that's, that's the, that's, but like again, you know, we don't have the, we don't have to get the exact, coach for that because I, I can imagine how you could go about doing that. So, yeah.

@Vinnie [45:06]: So that's, that's, that's pretty much the idea is you we put the we put the ale copy of the allocator in the extra memory, and then we propagate it using the same type erasing technique.

@kammce [45:11]: Mhm I think I might like, I, I'm gonna investigate the like your, your pattern with the functors. And it's like that with kind of my co-routine library, although I don't know if I will.

@kammce [45:33]: It's an interesting choice because I, because I'm probably going to stay away from the TLS variable for now, at least for my design, you know, this, this, this seems interesting. I, I

@Vinnie [45:44]: How do you support a stateful allocator?

@kammce [45:46]: I don't, I don't do any of that. that's not important to me actually. to me, I just need something that runs my co routines on it. So that's why I have one stack frame to just do all of my co-routine allocation, the allocations. If you're curious, like, oh, what do you do when you run out of memory or like when you run out of your like your stack depth, that means you chose the wrong stack depth. Same thing that we do in all of embedded software, which is you, you, you map out how much you're going to need upfront.

@kammce [46:10]: And then you get the stuff, then you size up from there. not the most desirable choice for most people. You also give it a big stack, but then you can pretty much run into the car. So, you know, I just

@Vinnie [46:19]: You

@kammce [46:20]: Yeah

@Vinnie [46:21]: Do you see anything in here that's not that's like embedded hostile.

@kammce [46:25]: Not gonna lie, tell us is not that bad. I've, I'm actually at some point, I want to finish my implementation I, I implementation. I finished my demos of showing like how you can use TLS in How to implement it yourself with her arm and other devices in that, in that,

@kammce [46:46]: The The, the one thing that is kind of looking interesting to me is the size of your promise. It does have quite a few members. The storage of this allocator is not a problem. that's a problem.

@Vinnie [47:02]: Talking about this

@kammce [47:04]: Yeah, there's a lot of stuff here. There's a lot of, there's a lot of additional things here. Just a lot of extra memory. I think my promise type, my promise I probably has like 4 words, 44 pointers in total size. not to say that, you know, like if this fits your needs and like does what you need, then like, you know, does what you need. this that like might be me being nitpicky. Also, another another thing about how I did my stuff, actually.

@kammce [47:30]: How do you return values? Where, where are the return values go in your implementation?

@Vinnie [47:35]: Right here

@kammce [47:36]: Just has to be some Oh, can you go to that real quick? I want to see how that, how that works.

@Vinnie [47:40]: I mean, you know, it's it's pretty simple.

@kammce [47:43]: That makes sense

@Vinnie [47:46]: I'll pro I could probably do something when T is default constructible. I can like Not have an optional

@kammce [47:52]: You know, I'm gonna, I'm gonna actually steal that too. Not, not, not like, not all of us, but simply just the task return base because I've, I've been doing like, I, I've, I've split it up in a different way and I'm like, this is a better way to implement return that void and return value because I hate having to like, add more things to my promise type.

@Vinnie [48:10]: The reason I did this is because I don't want to have a specialization for Void. It's super irritating. I mean,

@kammce [48:14]: Yeah, so, yeah, same, yeah, that's the same exact way.

@Vinnie [48:19]: By the way, that was my idea, not the AI. I just want to be clear about that.

@kammce [48:22]: Yeah, understood. I said no, no, no, that's actually so clever because like, I didn't expect the AI to have come up with this because I think I've tried to get it to do something like this and it didn't work. I see you're using clouds, so like, yeah, I've tried using, doing the same thing.

@kammce [48:39]: I guess, so here's one interesting aspect of my design for cover routines. It's, I think, backwards probably to how everything else is done, When you get the return object Like, I call my objects futures. I don't it conflicts with the standard future, but I don't care. when you get that return object, that is the container for your return value. The promise keeps a pointer to that container so it can update it with your value. And the reason of this is that I don't want the promise to

@kammce [49:08]: I want when the value is finished being created for it to be put into its container and then for the promised to be able to be destroyed at any point in time. but yeah, I My implementation is very different from probably the way that everyone else thinks about using cartoons.

@Vinnie [49:22]: That's like an emplacement into the final location without going through temporary.

@kammce [49:26]: Yep. Correct. Yeah, that's the plan It works. It's, it's, it's, it's, it's.

@Vinnie [49:30]: I'll be honest, it bothers me that the, it bothers me that the value has to be like moved twice in this thing, but you know, look, here this is the difference. This, you see here is this is intended to be like a general purpose library.

@kammce [49:39]: Yeah.

@Vinnie [49:46]: And you have something that's like fit for purpose for like a, you, you have certain requirements that you're trying to achieve.

@kammce [49:52]: Yeah

@Vinnie [49:52]: So, and it's not even clear to me that you're doing, are you even doing IO?

@kammce [49:57]: Yeah, oh yeah, yeah, I do it all the time. I, I, I got like nothing but embedded is IO and waiting for things.

@Vinnie [50:02]: So what's the bottom, what's at the bottom? Is it E-pole? What is it?

@kammce [50:06]: Oh, and interrupt, a physical hardware interrupt has to unblock my co-routine, but what it does is rather than like Rather than like The way that I do all the micro routines is the first thing you do is you create a context that contains your your actual stack frame and then information actually I can show you just a little bit of it so you can get an idea of like my approach to this.

@Vinnie [50:28]: OK

@kammce [50:30]: Let me Yeah, let's do this. Oh, OK, then I get to choose. Is that how that works? Let me First time Are you able to You know, how's this, how does this work? Hold on, sorry.

@kammce [50:48]: Click share my screen And

@Vinnie [50:51]: You you have to pick the window. It's fun, isn't it? Ho, isn't it cool?

@kammce [50:58]: OK. Yes.

@Vinnie [50:59]: I guess on

@kammce [51:00]: OK, so there's a button called share my screen. I click it and then like, then the, the, the screen that you're on goes away. And

@Vinnie [51:06]: Yeah, I, I thought, I stopped sharing so that you could share.

@kammce [51:10]: Yeah, yeah, I know. I'm actually just trying to figure out how to get the share button to work. Click the share button.

@Vinnie [51:13]: But you

@kammce [51:15]: Wait a minute. Is it maybe it's like a permissions thing, and that's why it keeps bringing me back

@Vinnie [51:18]: No, no. No, no, you can share for sure, dude. There's no permissions here.

@kammce [51:24]: No, no, no, it's more of a like my MacBook being like upset, like, oh, you're trying to share this, but did I give you permission?

@Vinnie [51:30]: Oh, yeah, that's, that's how, that's plausible.

@kammce [51:32]: Yeah, I know. OK. Give me like a sec to just like Google around for like

@Vinnie [51:50]: So interesting embedded

@kammce [51:53]: Oh yeah, yeah, 00 yeah. So as, as we're as I'm figuring this out, I'll explain to you all right, so I got to go to the settings. so my maxims. So, There are like I, I, so in this whole framework that I'm building up, they're like, and I'm trying to make it as thin as possible.

@kammce [52:12]: The design is around Block states, and that's where you get opinionated. So I understand that not everyone's going to want to use my thing. My thing is built for my embedded itself, but like there's block by No, blocked by time, blocked by IO, blocked by synchronization and blocked by external. External means you've called some third party co-routine. in a second, I'm going to show you how I manage my co routines and then how scheduling is supposed to work, because I've, I've seen these standard exact way, and it just never really clicked with me. So I just had to go in and in a way implement

@kammce [52:46]: My idea and then try to see where things start to fall flat. haven't found it yet though.

@Vinnie [52:49]: Well, are you Are you using, I don't, I can't see your screen, but are you using multiple threads?

@kammce [52:54]: You can, you don't need to. It's not necessary whatsoever. The goal is to be concurrent without needing threads, but then you can also stack on threads as much as you like. It's a, you can use whatever you like with this system.

@Vinnie [53:08]: I just feel like If you only have, if you only have one thread, you don't need a dispatcher.

@kammce [53:10]: Yeah. We have a, like, in my, in my design, like you can, you have like a top-level scheduler that you know can put your, if you want to do an event loop, if you want to do works dealing with multiple threads or whatever else, you know, it's up to you to choose how you want to go about,

@kammce [53:31]: Dispatching your workout, but that's it. I do it at the top, I let the top level do it. I don't let my co routines specify that because I In your design, you have your coach routine make the choice of I want this executor to execute this thing, and I've seen other people kind of write their code in that way. it just seems odd because it needs a certain resource to exist before the function gets called, or at least it needs to like, you know, drive that at some point. And maybe that

@kammce [53:55]: Works for, sorry, I'm still like looking.

@Vinnie [53:59]: That's OK. It works for that, it works. This is purpose built for the like for networking.

@kammce [53:59]: In the system and audio Gotcha, gotcha And I guess that's another thing for me is, wanting to know more about, OK, I don't see why this would not be working. OK, so I'm already gave permissions for this. All right, let's see. Is there any way in here that I can like,

@Vinnie [54:19]: Why don't you just share me a repository link.

@kammce [54:22]: Sure, sure I don't have any good documentation on this project. So like that's a bit.

@Vinnie [54:28]: OK I'll generate, I'll generate it for you. Have you seen my doctors, dude, I have a, I have some very good scripts for producing docs. Wow.

@kammce [54:33]: There's Nice.

@Vinnie [54:38]: You'd be amazed

@kammce [54:40]: Don't worry about making it because I'm probably still going through a few final design changes with this. but the I guess I'll, I'll send you a picture. I'll just get the slides real quick.

@Vinnie [54:50]: You'd be a, where is the code, modules?

@kammce [54:53]: So what

@Vinnie [54:54]: Where's the code

@kammce [54:56]: Yeah, go to modules

@Vinnie [54:58]: I only see a CPPM file.

@kammce [55:00]: Yeah, yeah, and that's it. That's the only file.

@Vinnie [55:02]: That's it

@kammce [55:03]: Yeah, that's it I think it's like 1000 lines or something like that. Let's see.

@Vinnie [55:08]: Oh, of course, you want it to be small, so it makes sense that there would be very little code.

@kammce [55:13]: Oh, yeah, there's very little to, I mean, once you get, once I've gotten my idea down, there wasn't really too much like, I mean, it's mostly just getting like getting the plumbing just right. there was one picture that I showed before. I don't know if you saw it in the thread. I'm going to repost it actually I'm just repost it to you real quick so you have it.

@kammce [55:31]: This is the overall design approach of The Ascent context idea. I simply need a place to allocate my co-routine frames. I need to put them somewhere so that they can be executed and resumed. The idea is that when one co-routine cowaits another one, it becomes suspended. The next one becomes active. And whenever you resume the context or the future, you get these two parts of the same thing, you can make more progress down the line. the one thing that I added in, I went back and forth on different ways of doing this, but eventually I'll say eventually I might, who knows, I might change it, in the next week. But the thing that I

@kammce [56:11]: I used to have a scheduler object that would be bound to each context so that the stat for in that context could point out to the schedule and say, hey, I need to be scheduled sometime into the future. You handle when you're going to resume me. And then that thing can then decide to take that context that it has now and go, all right, well,

@Vinnie [56:27]: Let me understand, let me understand this. So these are co-routine chains.

@kammce [56:29]: Yeah. Yes, these are covering chains.

@Vinnie [56:31]: This is like, this is like my notation.

@kammce [56:35]: Oh, it's like a notation.

@Vinnie [56:37]: Yeah, yeah, exactly.

@kammce [56:38]: Oh We'll keep in mind these are all on the same, this is all in the same stack. This is not like separate execution, actually can you still hear me? My, my earbud just went a little crazy.

@Vinnie [56:48]: Yeah, so this is showing the this is showing the evolution of how it evolves when you coa away and then on the way back.

@kammce [56:49]: OK. Yes. Correct. And

@Vinnie [56:57]: Exactly, this is exactly what my, what I was showing you. It's the same thing.

@kammce [57:01]: OK, OK, cool, cool Actually, that's probably

@Vinnie [57:04]: But, but wait, hold on, hold on, hold on. OK.

@kammce [57:07]: Yeah.

@Vinnie [57:08]: So your allocation, you actually have a stack.

@kammce [57:12]: Yeah.

@Vinnie [57:13]: Oh, I like this a lot. I like it a lot.

@kammce [57:16]: Yeah, because then I don't have to like worry about Halo. I just say, well, and I'm working on a tool to be able to like search through your your debug information afterwards to kind of pull out the information similar to what GCC gives you when you're doing a better code, which is get stack usage. You can get the Mac stack usage of any function.

@Vinnie [57:30]: Oh You actually, you want to estimate the stack using static analysis.

@kammce [57:36]: Yeah Yep, that's the goal

@Vinnie [57:39]: I love it. That's amazing.

@kammce [57:40]: Yeah.

@Vinnie [57:41]: Dude, can I give you another idea?

@kammce [57:44]: Sure, sure, go for it

@Vinnie [57:45]: Use AI and No, no, no, seriously, you, you use AI and the coverage and you have it You have it start, we have it start with the low stack, and then you run a test that covers every line and then every time it blows up the AI will increase the number and it will just loop and keep increasing it until it can hit every line of coverage without, without failing of memory.

@kammce [58:12]: I will note that down. I will get to doing more of the coverage testing once I got the whole design complete. I think the last, yeah.

@Vinnie [58:19]: No I'm, I don't mean coverage for your library. I'm saying like it because you're, you're, so you have a problem is how do you, how do they figure out the stack size?

@kammce [58:28]: Yeah

@Vinnie [58:29]: And I'm saying that

@kammce [58:29]: Oh, we're talking about that, yeah, yeah, mhm.

@Vinnie [58:31]: An agentic workflow can figure that out it can iterate like it can try 100 bites and then it'll run a test that, that, that exercises every line of code using coverage. Make sure that every branch is taken, every co routine runs, whatever, and then it will blow up because it's too small and then it'll just increase the value a little bit every time until it can run without failing.

@kammce [58:52]: Got you. I see. oh, is this a way to just to make sure you're talking about this is a way to like figure out, if my, if the frame size was too small.

@Vinnie [59:01]: Yes, it's to figure out for a it's a for a given piece of code, what is

@kammce [59:02]: OK

@Vinnie [59:07]: The stack size that works

@kammce [59:09]: Got you. The one thing I'll bring up is, the information about how big the stack frames are is in a debug symbol that clang dumps into your debug objects. It's called Coro something Ty and I think all I need to do is get the causal chain of caroutins and then sum those up and then give it for each one. So it seems like it should just be doable and I probably can just get like, you know, myself or something to do that, but like, yeah, but I like, I like, I like your

@Vinnie [59:23]: No.

@kammce [59:39]: Your agentic approach.

@Vinnie [59:42]: Here, tell me what you think about this.

@kammce [59:44]: OK, let's see OK, to use a basic context. OK, that's good at least.

@Vinnie [1:00:04]: Is this correct

@kammce [1:00:06]: There's some parts that like I would definitely, there's a lot of things I would change. So like that's, there's some parts in here that are perfectly fine though. yeah, no, I know I can generate a lot of this stuff. The only reason why I haven't is that I don't see a reason to generate the code when I haven't completed everything, like, for example, I just recently changed the semantics for what it meant to be an external, externally blocked, and before, I didn't actually have a solution for how you schedule for externally blocked things, so like that's the reason why I haven't generated a lot of the code, but it's, it's nice, yeah.

@kammce [1:00:36]: No, I can throw the so Claude and get the same kind of notes out.

@Vinnie [1:00:41]: This is pretty good. I, I have to say, like, looking at your code, it was kind of like, it was hard to read because, oh my God, we got to redo all this, but now that I'm looking at this, like this is pretty cool. I see you have your future.

@kammce [1:00:41]: Yeah Mhm Oh yeah Mhm, mhm

@Vinnie [1:00:54]: You have context, dev, device. Hey, this looks very interesting now. Oh, the contact class is the foundation of the library. By the way, it figured all this out just from your code.

@kammce [1:00:59]: Yeah Yeah Oh yeah, no, it makes sense they could figured all that stuff out for my code. Yeah. Yeah,

@Vinnie [1:01:09]: Everything expects no card. Oh, look at that. That's a nice looking, that's a good looking class. Well, there's the, there's your stack layout. It's that's the diagrams that you were showing me.

@kammce [1:01:18]: Yes.

@Vinnie [1:01:19]: Drive classes must call initialized stack memory in their constructor. Oh, you have to provide the scheduler. Oh, look at that.

@kammce [1:01:28]: Yes. This is all about providing to the user control out to whatever they're building up so they can build up whatever classes, objects, whatever they want to do, or if they want to be very like, I have students who like, I don't want to deal with any of the Ayc stuff, but I'm building up all of my APIs with Async first. So all, all the APIs are sync.

@kammce [1:01:47]: So, yeah.

@Vinnie [1:01:48]: But My context unblock. What does that do that just runs like one thing.

@kammce [1:01:56]: No, all that does is, call your scheduler with the blocked by state of nothing, and it's up to your schedule to do something about that. So from there, it would then relay that back to its own scheduler if it has a pointer to it, like, for example, in the initialized thing it says my context. If you have a schedule to defer to, you probably take that scheduler as an input parameter of some smart pointer, and then

@Vinnie [1:02:16]: Sure.

@kammce [1:02:17]: Pass that along

@Vinnie [1:02:18]: 00, so you're taking it, I see you've inverted, you've basically flipped the whole game upside down. You're coming at it from the resumption.

@kammce [1:02:23]: Yes Correct. Yes

@Vinnie [1:02:29]: I'm coming at it from the top, I'm coming at it from this is how you launched the code routine.

@kammce [1:02:34]: Yes, and this is how everyone else, I think in in the center's receivers group does things. I, I get where that's coming from, but it's, it's a There's been some key problems in the software that I write that I've been trying to figure out how to solve. One of them is

@kammce [1:02:51]: Analyst is very domain specific, but like low power Time, like how, how to, how to judge how much time we want to delay for something. and Detecting whether there's no work, and I know that sounds a bit weird, but the thing that comes up that I've been thinking about a lot of is, I need a way from on high to dictate to the things that are going below, how I want them to handle their time blocking because I might want to do something in that context, or, if I have

@kammce [1:03:25]: A particular scheme I got multiple cores, now I can start delegating work off to separate course. Like there's, there's, there's like I, I, that had like a long I I'm, I'm currently I'll, I'll put it like this A lot of the Scheduling and design problems that I have been thinking about and trying to work towards for embedded systems kind of resulted in getting to this, not saying that you couldn't solve it with the same thing that you have. I think you definitely could. It's just that, in my case, yeah, yup.

@Vinnie [1:03:50]: We Who

@kammce [1:03:53]: What's up

@Vinnie [1:03:53]: Wait a minute, what's this? What the hell is this?

@kammce [1:03:56]: Let's look at that

@Vinnie [1:03:57]: What is this

@kammce [1:04:03]: Oh, I don't know. I don't think you could do a co ed with nothing. I don't think that's possible. That's not.

@Vinnie [1:04:08]: No, but wait, no, what is that one, what's this 100 millisecond thing? Does that work?

@kammce [1:04:13]: Oh yeah, yeah, so I have a weight transform on Koro Cronoan chrono duration, and that passes a blocked by time. This is a shorthand for saying blocked by time. And then this just passes the 100 milliseconds into the scheduler, and the schedule can then it's, it's one of the one block based states that schedule it has to is mandated to follow. That's the wait that duration of time before it re resumes your your co-routine. They can take longer if it wants.

@Vinnie [1:04:36]: I love that. I love that syntax. Is it, is that anyone, anyone else done that?

@kammce [1:04:41]: I Actually, actually, there might be one other group that I came up, I kind of came up with that myself, just so I know, but I, I actually found someone else who did something very similar in another co routine library.

@Vinnie [1:04:52]: Basically, that's just like going to sleep.

@kammce [1:04:55]: Yeah, precisely that you get to choose how you want to go to sleep. You can use, if you're on some real-time operating system, there's a VAsk sleep function you can call for on Linux you can call it normal sleep. If you're on, I don't know what you do on Windows, but like, you know, whatever system you want to do or if you want a busy loop because a lot of embedded projects don't care about like getting a timer and figure all that stuff out. You can do that, or you could set up a timer to wake you up, go to sleep, low power mode, and then wake back up when the time has elapsed. So like these are the use cases that I have for when you would call this function.

@kammce [1:05:25]: And the controller, the person at the top level The person who created the context, who passes it to the first top level curve routine. That is what sets the the policy of how time is managed.

@Vinnie [1:05:36]: I think what I've learned from this Khleo, and by the way, thank you so much for your generous time. Is that there is a

@kammce [1:05:40]: Welcome. Yes.

@Vinnie [1:05:43]: There's not one model that's works for everyone.

@kammce [1:05:46]: I agree. Yeah

@Vinnie [1:05:47]: Like senders and receivers works for Nvidia. Great. OK, nice.

@kammce [1:05:50]: Mhm, mhm

@Vinnie [1:05:51]: Cool, cool story, bro. What I've done, you think the thing that I make is amazing for networking, but you you have my library is not suitable for you.

@kammce [1:05:53]: Yeah Mhm Yeah

@Vinnie [1:06:03]: So it's like We have to recognize that we shouldn't be standardizing things in such a rush.

@kammce [1:06:06]: Mhm I agree. I I, for the most part, I think I, if I remember correctly, actually I don't remember how I voted, but if I, if I was thinking about it now, I would have voted neutral. people seem to really care about centers receivers. There's a lot of hype behind it, but I just didn't see its exact place. I know, but I also know there's embedded people who are very excited about sentences receivers and like, the guy from Intel, forget his name, but you know, so, but I agree though, it's, I, I've, after sends and receivers, I think

@kammce [1:06:42]: Michael Wong said something along the lines of we should pull back on standardizing frameworks. And I agree with that. I'm very concerned about standardizing frameworks. I actually After a long time, realized, especially working with the coins over and over again.

@kammce [1:06:59]: It's, it's this, it's this hodgepodge of trying to make everything work for everyone. And At first, I really hated it. Well, my, all my students hated it. A lot of people I know hated it, and then I started realizing, oh, but I get to have all of the control, every single knob I can tune and twist and make if I want to make it happen. There's some things that aren't exactly ergonomic, like how you have the dispatcher synthex for a weight suspend in order to properly pass that along, which I think

@kammce [1:07:23]: Makes, again, I think that makes sense. But Yeah, no, I think you're right. We, we need to think about what's more holistic, even though it might upset The community because I know a lot of people in the community want more features and mostly ergonomic things like a nice split function from a

@kammce [1:07:43]: From string and stuff like that, yeah. That's it

@Vinnie [1:07:49]: Well, look, you know You're right. So there's, I, so I have this thing called use case first, which came from Peter. It's the idea that you start with the what the user writes like for you write out the thing that the problem that the user is trying to solve. And then you, then you design backwards from there. And unfortunately, those types of things tend not to be able to pass through the committee because when, when you do use case first, when you have a library that's 5, 1015, 20 years old, it has scars, right? Like, you know,

@kammce [1:07:56]: Mhm mhm Yeah

@kammce [1:08:18]: It is, it is.

@Vinnie [1:08:20]: From from from having to satisfy actual real world needs, it deviates from the theoretically pure foundation and the reality is that these big framework first designs, they're more easily able to pass through the committee because people can look at it and, and, and they, they don't have any real world thing to compare it to.

@kammce [1:08:38]: Mhm

@Vinnie [1:08:41]: So You know, I don't know if you've saw, I don't know if you've seen, but I have like, I have the I have a blog, I have a sub stack where I've been, I've been creating like these papers. They're not intended to be published at WG 21, but they, they look at certain WG20 outcomes, WG21 outcomes through the lens of what's called great founder theory.

@kammce [1:08:53]: Mhm Mhm

@Vinnie [1:09:00]: I don't know, so great founder theory says that like functional functional institutions are the exception. And there are every major social technology in history can usually be traced back to one person. In other words, one person created a social technology that transformed how people collaborate and, and it became enduring and durable, right? Like, for example,

@kammce [1:09:22]: Mhm, mhm

@Vinnie [1:09:23]: Napoleon, are you familiar with like like French history, like, you know what Napoleon was famous for?

@kammce [1:09:28]: Yeah

@Vinnie [1:09:30]: Tell me.

@kammce [1:09:31]: Actually, you know what? I'm gonna say no just because like I, I remember him being that like it's all of his wars that eventually losing all of them, but you know, yeah.

@Vinnie [1:09:38]: Exactly, exactly. So people, people know him for like his military prowess, but in reality, what made him a great founder was the Napoleonic codes. After he won those battles, he imposed a system of rules like laws, but he imposed them across all of Europe. That means every little city they had to follow the same set of rules. So why is that great? It's because if you're like a merchant or if you're in a if you're like a, you know, like a contractor, you can travel all throughout the lands. It doesn't, doesn't

@kammce [1:09:43]: Mhm.

@kammce [1:10:02]: Mhm

@Vinnie [1:10:08]: Matter where you are, the same set of rules apply, so it created a consistent legal framework that enabled trade. And that lasted for hundreds of years, well well beyond his depth. And so WG 21 is social technology, right? Like it's the committee. It's that it's that, it's that collaboration and, and it lost its great founder, Bijarni because he gave up all of his power when he, when he put C++ in ISO.

@kammce [1:10:21]: Yeah And

@Vinnie [1:10:33]: So, you know, I have a bunch of papers where like I explain You know, through the lens and like It's like what you were saying, it's so it's so funny that you say it because like framework first. Is exactly a big problem, you know.

@kammce [1:10:47]: Yeah

@Vinnie [1:10:48]: So, I've been trying to figure out Like what to do. And I don't wanna just lob grenades, of course, because it's very easy to criticize, right?

@kammce [1:11:00]: I

@Vinnie [1:11:00]: So. So I had this paper that I was researching about like, what do we do about WG 21 and I actually came up with the workflow. It hopefully it won't surprise you that it's an agentic workflow. But it's called

@kammce [1:11:12]: OK, interesting

@Vinnie [1:11:13]: It's called knowledge capture. And I don't know, maybe you'll find it interesting, but I'm gonna, I'm gonna link it. So

@kammce [1:11:20]: So I can take a look

@Vinnie [1:11:22]: So basically it's about inter interviewing people and then using AI to distill what are called the generating principles, right? And, and then

@kammce [1:11:32]: OK

@Vinnie [1:11:34]: And then if you interview like multiple people, you can get You, you know, you can get a like, like, like a lot of confidence. So what I did was I I interviewed a bunch of people and then, you know about the boost, you know, did you see like that boost documentary?

@kammce [1:11:41]: I No, I I've heard of it.

@Vinnie [1:11:50]: So we, we, we, we're sponsoring this documentary about like WG 21 and Boost. There's like some independent like filmmakers are like doing it. They're very famous, and they gave me some transcripts. So what I did was I used my knowledge capture prompt to capture in the transcripts to capture the knowledge. And then what I did was I did another algorithm which correlates what are the things that, what what is everybody saying that's the same? Like what's a repeated signal in all of the interviews and like, and then

@Vinnie [1:12:20]: I capture all of that and then I sort them to create what I call combined principles, right? OK, so, so I, so look, I got Dave Abrams, Doug Gregor, Howard Hinnett, Mattias, is Sean Parent, you know these people, right?

@kammce [1:12:25]: Yeah And and Yeah, yeah, yeah

@Vinnie [1:12:34]: OK, so as he we here is the result, the AI synthesized output would called combined WG 21 principles. Do me a favor, open that up and tell me, tell me what you read. What's the first item?

@kammce [1:12:47]: We're talking the, oh, OK, let's click on that. So this existing practice, not invent? Yeah, of course. Yes, yes.

@Vinnie [1:12:55]: What about number 2

@kammce [1:12:55]: Yeah Require positive field experience before standardization. I agree. Yeah, yeah.

@Vinnie [1:13:01]: Oh shit, what's going on? Oh no, I any or where I'll do it to Leon built and we got the AI, the AI AI knows what's up. OK, so, OK, does this look? It looks fun, right?

@kammce [1:13:12]: Yeah, it was good, yeah

@Vinnie [1:13:13]: OK All right. Check this out OK, so what if we do this? What if we take everybody's like What if we take everyone's knowledge and we create Like an evaluation framework for papers in WG 21, like we take a WG 21 paper, we run it through a categorizer because you know there's different types of papers. There's bug fixes, there's library, there's evolution. You know what I mean? We run it through a categorizer and then we, depending on what kind of paper it is, we use an evaluation protocol, and the evaluation protocol is based on the distilled knowledge from the experts in the committee that are captured using a process that I describe in my paper, which, by the way, it's very simple. It's just people talking

@kammce [1:13:38]: Yeah

@Vinnie [1:13:57]: People all you got to do is talk and my paper knows what to do. So what if we have an evaluation framework for library only proposals. Well, it might look like this. So you might have something that looks like this. See that paper tester?

@kammce [1:14:13]: OK, let's see

@Vinnie [1:14:14]: OK, so the paper tester has a gate. That means it's like you have to, you have to get past the gate or else your paper is not going to be considered very good. And it has to be justified because standardizing is very expensive, right? So you have to justify your standardization.

@kammce [1:14:15]: Yeah, yeah Is it, is it?

@Vinnie [1:14:32]: So this document you you scroll through it real quick, it has all these rules like for example, go down to Let's say category 11, just jump down the cat just search for category 11, safety and stability.

@kammce [1:14:44]: I think OK

@Vinnie [1:14:48]: So safety is very important and like we want to get a signal. OK, so I know what you're thinking. You're like, OK, Vinnie, this is very nice. So what do we do with it? You know, you know what's coming, right?

@kammce [1:14:54]: OK OK, go for it. What's coming.

@Vinnie [1:14:59]: So what's coming is now we have a system where we can just take any paper, and we can just ask, well, evaluate it, right? OK, so give me, OK, you ever heard of Pylos, random number engine.

@kammce [1:15:12]: They're gonna pay for it

@Vinnie [1:15:13]: No, OK, what about in-place vector?

@kammce [1:15:16]: Yeah, liature, yeah, yeah.

@Vinnie [1:15:18]: OK, so you've heard of in-place vector, right?

@kammce [1:15:20]: It's

@Vinnie [1:15:20]: OK, let's run the paper on, let's run the paper tester on in place vector. OK, we're going to do it. You ready? Peach 0843R 10, ding ding ding ding ding ding ding. OK. Oh, there it is. Node, we're evaluating and we're doing it

@kammce [1:15:25]: OK All right, yeah

@Vinnie [1:15:38]: Look at that summary

@kammce [1:15:41]: Hm Interesting. It's actually pretty good. I like that a lot actually.

@Vinnie [1:15:49]: You like that?

@kammce [1:15:50]: Yeah, no, I'll probably pass my own stuff through this. Once I have, yeah, actually, no, this is, this is pretty good. I like this actually.

@Vinnie [1:15:58]: OK, now let's look at one that, let's look at a bad one. Let's look at one that sucks. And let's make one that's rejected, you're gonna laugh. OK, you ready for this? This is funny. This is all, this is all, this is all in the paper, by the way, but the paper's kind of long, so I'm gonna spare you. So I'll just get you the maximum entertainment, OK.

@kammce [1:16:02]: OK OK. OK. Send it over. Mhm

@Vinnie [1:16:16]: There it is

@kammce [1:16:16]: There's this one A view of 01 elements, views may be.

@Vinnie [1:16:22]: 00, what's with the red X's?

@kammce [1:16:23]: Yeah, yeah, yeah. Well I'm out of 26 below threshold, 14, yeah. Yeah. No, I honestly, this is having something I, yeah, actually this is, this is, I think this actually has quite a bit of value. especially as like a first pass on things. I just, especially for people with their own, like papers were like, oh I'm gonna throw this paper out there and see how it goes.

@kammce [1:16:50]: You know, this is good

@Vinnie [1:16:52]: Yeah, you just ident so, yeah, so this, that's actually a really good insight, Khalil. So people that are proposing something like they should use the paper tester first to see where their proposal might be weak. And then once they submit the paper, then we can have a process where it's it's automated every everything in the mailing gets analyzed and then, and then you get a report and the reports are available before the meeting. So people, so people don't have to read the paper. You can immediately see, like, you know, like what's going on. So why is this good? So the

@kammce [1:17:15]: Mhm mhm

@Vinnie [1:17:22]: AI is not making the decision. The AI is just providing signal and then the humans decide what to do. Like, does this signal matter or not, right? And, and to be clear, the paper tester that I developed has a lot of my own opinions in it, like, you know

@kammce [1:17:26]: Mhm Yeah Yeah, Mhm Yeah

@Vinnie [1:17:35]: So a real paper tester would have to be, you know, collaborated in the WG 21, but my, my CEO told me not to publish this. He said like, don't put this in the mailing

@kammce [1:17:40]: Mhm, mhm, yeah I, I, I would say I, I kind of agree with him, not, not, this is not me being mean or they trying to say anything against us. Like, I think this is a good idea. I just think that the moment you put something like this on the mailing, you'll, you people will collectively try to curb swap you, you know, you know, they, they'll make their way out to you. They'll be like, Yo, Vinny, what the fuck is this? you know, so, P I I I, I like the idea. I think you should continue to bring it up to other people because

@Vinnie [1:18:06]: Yeah

@kammce [1:18:14]: Or how should I put this, I mean, so long as you, you put it out there with the intention of like this is a tool that I'm not sure exactly what, what the right pathway is for you to get inside of people, but I think just simply showing, hey, this thing I came up with that I thought was pretty useful to pass papers through it, your own papers, maybe even other ones to kind of see where there might be some issues at the AI can identify. So, I think overall, this is a good useful tool and thing,

@Vinnie [1:18:22]: It's.

@kammce [1:18:40]: I just don't know how others are gonna, are going to take it. I've seen what happened with other people who posted AI stuff. That stuff was slop in my opinion though, and then they got a properly curved up.

@Vinnie [1:18:50]: You mean on Reddit

@kammce [1:18:52]: No, I think this was actually on the mailing. Although I can't go back to my mailing right now, for my mailing history just because I, you know.

@Vinnie [1:18:57]: Oh yeah, I, I know what you're talking, someone, someone was putting someone was like pushing those papers through.

@kammce [1:19:02]: Hm, yeah

@Vinnie [1:19:02]: Yeah, but my slop is good though. I spend a lot of time

@kammce [1:19:04]: No, no, I don't, I'm not calling this up. This is, this, I think this is actually a, having a document that goes over how to like the things that we care about, and then in a, in a really succinct way that is, and obviously you said bring up other people and collaborate and all that. Once we have a really good document that describes what makes a decent paper.

@kammce [1:19:20]: You could shove your paper along with it in there and then get something out. I think that's actually pretty good. I think that's a good idea.

@Vinnie [1:19:26]: The commit, thank you. I appreciate that. The com but the committee collectively has to decide that they want to change because the way that they're, the way that they're going about, like, for example, I hate, I don't want to rag on Eric, but like, look, the fact that he has like 10 papers in flight related to stood execution tells you that the design is not mature.

@kammce [1:19:28]: Yeah.

@kammce [1:19:45]: I agree with this. There have been so many papers, again this is why I stopped, I stopped being a minute taker for LEWG. It's because so many papers were about sends and receivers, and and, and once you get into someone's weird, like it, like, I, I don't know the depths. So like when they're going into the depths into conversations, I don't even know how to, how to compress things when I write stuff because

@kammce [1:20:08]: They're at some other level and they've already passed me trying to figure out even how to write stuff down. So, no, I feel you. Senator receivers is, is, me and, David, forgetting his last name.

@Vinnie [1:20:22]: And and the mortar thankel.

@kammce [1:20:25]: Sankel means me and him agree on the fact that we are both afraid of centers and receivers. He doesn't, he has a hard time wrapping his head around it, and I do too, and even at some point made a comment saying like if Khalil, the person who's been ming all this stuff, is having a hard time and he's trying to figure this out and it can't, then what hope do we have for like,

@kammce [1:20:43]: For like new people, and I agree with that. but yeah, yeah, yeah. I agree.

@Vinnie [1:20:50]: So you know what, here, I'm going to give you a sample of my slop.

@kammce [1:20:53]: OK

@Vinnie [1:20:55]: Here you go So this is actually, it's, it's slop. Look, the, the fact of the matter is, is that all of this stuff is AI generated.

@kammce [1:21:02]: OK

@Vinnie [1:21:03]: You know, that's why I, I label it clearly. It's like this is my very best AI slop, but you know what though, it sounds really good.

@kammce [1:21:12]: I mean, you went through it, right, before you posted it.

@Vinnie [1:21:12]: Like I what

@kammce [1:21:16]: You read through it before you posted

@Vinnie [1:21:18]: Dude, let me, let me tell you something This slop is so good that like I read it, I read it over and over again just to get it

@kammce [1:21:25]: No

@Vinnie [1:21:26]: Just to get a dopamine hit.

@kammce [1:21:28]: Bro, I mean, if, if, if you've like to me, and this is me and my fiance have talked about like what it means to use AI responsibly. If, if you are, if you're, if you're taking the time to review it and make sure like this is, this is my voice. This is what I want to put out into the world, then it's, it's perfectly fine. I don't consider that slop. slop is when you create the thing and throw it out there and don't even think about it, you know.

@Vinnie [1:21:48]: That was the first thing that I made. OK, so the my first Yeah, the first thing that I made was a work of fiction, actually, the first thing that I made was Prompagorov complexity. Oh, you'll like this one. This is good. This is actually quite good. So, you know, AI gave me a voice.

@kammce [1:22:04]: Is it true

@Vinnie [1:22:05]: AI gave me a voice because previously, you know, it's, I want to write code. I don't want to write papers. And I had all these ideas and the AI, let's bring them to life. So this is like Karl Magorov complexity, like the Promagorov complexity of like a piece of data is the smallest prompt that can reproduce it.

@kammce [1:22:11]: Mhm Mmm. Interesting.

@Vinnie [1:22:24]: Right? I mean, so, and you know, and make can that can make for some funny jokes, right? You know, like, like you could tell some like someone like has like right makes a big wall of text like they post a big wall of text that's like, hey man, that's very, that's Promagorov compressible.

@kammce [1:22:30]: Yeah, yeah

@Vinnie [1:22:42]: So then I made this other stupid thing, it was like a work of fiction, which is, it was like a prediction of what's going to happen in 10 years is that there's going to be these quasi corporate states that like in in the American outback where like polorilexon and rugal, the two companies emerged and they have like they're like they're like practically sovereign. they have their own nuclear reactors. They have their own like manufacturing and like they have their own like their they have their own armed like security forces, and they approach

@kammce [1:22:54]: Mhm

@kammce [1:23:11]: Goodness

@Vinnie [1:23:12]: Like a government level

@kammce [1:23:12]: You already do

@Vinnie [1:23:14]: Yeah, you know, so that was slop, dude, that was pure slop. OK, to be fair. And then I started inventing like words, right? Like I started, like, I want to make up my own words. So, like, here's like I made up the word bot line

@kammce [1:23:22]: Mhm OK

@Vinnie [1:23:29]: And And like and botline is the minimum botline is the minimum performance that you can achieve with that with at the top of AI. So like if someone's at work is not producing an output that, that even an AI could produce they're below the bot line.

@kammce [1:23:45]: It is, it's a Dacha. Damn. That's funny though. I like that.

@Vinnie [1:23:47]: It We're gonna make up words anyway. I gotta go to lunch.

@kammce [1:23:53]: All right, you do your thing

@Vinnie [1:23:55]: Hey, listen, thank, thank you, thank you so much. Read, read the transcript, feel free to do whatever you want with our transcript.

@kammce [1:23:55]: Yeah, good talk. Yeah You're welcome OK

@Vinnie [1:24:03]: All right, later

@kammce [1:24:04]: Later