# BOOST_BJARNE_STROUSTRUP_STRINGOUT_v00

- - - -
filmed Date: 2025-10-28  
location: Manhattan, New York  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: https://vimeo.com/1157576773/c5cad0787a?fl=ip&fe=ec   ​​  
summary: Basically said WG21 turned into a regret, too big, many bad decisions. He copped to a lot. Surprising. Felt very open, man thinking about his legacy and feeling weight of what WG21 pulled him toward. He talked a little smack about Boost but was effusive about certain libraries, esp Dimov's; good Beman remembrances.   
- - - - 

## Transcript Start

[00:00:00] 

[00:00:00] **BJARNE STROUSTRUP:** Ah, hi. Cheers.

[00:00:07] **RAY NOWOSIELSKI:** So thank you for having us here. Why did you ultimately decide to interview right now?

[00:00:12] **BJARNE STROUSTRUP:** I guess partly because I feel like a jerk if I said no. Um, people want to know how these things came about. Lots of people want to know that and well, lots of people ought to know that, so [00:00:30] I must help. There has been a fairly steady set of questions about how, uh, C++ and, uh, parts of, uh, stuff related to it came about. But there seem to be a surge now. Um, like I got another two requests this week. Um, it's, it's pretty intense. Um, part of it must be that [00:01:00] people simply have realized that, uh, C++ is all over the place, and that interestingly enough may be a result of, uh, a lot of people complaining about it.

[00:01:12] **BJARNE STROUSTRUP:** And so we find that, uh, it can't be that bad because it's everywhere. Um, from the bottom of the sea to the sky is above Mars. I mean, it's, yeah, it can't be that bad if, if it succeeds that [00:01:30] often. I haven't had a serious memory leak for years. I know how to avoid them. Um, I would like to see guarantees for avoiding it, but it's not that hard.

[00:01:42] **BJARNE STROUSTRUP:** I, I met Beman Dawes, uh, first in the standards committee and he was, uh, working for a bank at the time and I found that particularly important 'cause we have far too many people who think they're language designers and far too few [00:02:00] people who actually built, um, products, uh, built things for other people to rely on.

[00:02:07] **BJARNE STROUSTRUP:** And I think. If you want to design something good, you have to know what it's for and how it's used. Uh, it's not just math, it's also some psychology. And, uh, basically knowing, um, how it to be used, what is appropriate for use and such. And that's a, that's a constant problem, not just with c [00:02:30] plus plus, but for, um, language design in general.

[00:02:34] **BJARNE STROUSTRUP:** Because a lot of people think it's an abstract art and, uh, it's an applied art. Yes, you need abstraction. Yes you need math, but you also need to understand, stand what people wanted for what other problems people are addressing. What kind of mistakes do people make? And Beman Beman was one of the very few people in the committee who had a [00:03:00] thorough grounding in real applications of the language at a large scale.

[00:03:07] **BJARNE STROUSTRUP:** Okay. And, and in a, in, in a field where we didn't have that many at the time, uh, C++ is all over finance and banking these days, but that wasn't the case then. At least if it was, I didn't know it. So I learned a fair bit from Beman and I was very interested because of that part of the background.[00:03:30] 

[00:03:30] **BJARNE STROUSTRUP:** Um, I don't remember the exact phrase, but uh, he definitely was a major part of the, uh, libraries group. And the first really concrete thing I remember was when we were discussing, uh, the STL, uh, Alex Stepanov's, uh, suggestion for the part of the standard library with containers and algorithms and [00:04:00] iterators and such.

[00:04:02] **BJARNE STROUSTRUP:** And, uh, that was so new and unusual. That a lot of people didn't like it because it was new and unusual. A lot of people feel that if something is new and unusual then it must be complicated and slow and things like that. And I'd convinced myself that it was good. And I had, uh, all the [00:04:30] years built up a list of requirements for a good library in that domain.

[00:04:37] **BJARNE STROUSTRUP:** And even though the STL didn't look anything like I imagined or anybody else imagined in those days where object oriented was sort of the ultimate buzzword, uh, I had a list with about 12 items and it matched 11 of them. And okay, it doesn't look right, [00:05:00] but it must be, nothing else matches that many of my criteria.

[00:05:05] **BJARNE STROUSTRUP:** Okay. I come to that night, uh, Alex had gone to the committee. I've been at the committee. Andy Koenig Has been, uh, lobbying for it also. And we had some success. And then Beman spoke up at a meeting, um, out of roughly nowhere and says, well, I thought the STL was too complicated. [00:05:30] Um, but then I went and, uh, implemented, uh, 10% of it myself to see, and it isn't too complicated.

[00:05:40] **BJARNE STROUSTRUP:** We should use it. I think he used slightly more words than I just did there, but not many more. It was basically a serious person who everybody, uh, thought of as serious, who said. This is good enough and simple enough, we should go there. And I think [00:06:00] that was, uh, a, a key part of, uh, the reason that we got the STL, I think the timing is right, but I don't know it for a fact.

[00:06:13] **BJARNE STROUSTRUP:** I talked to Beman, uh, when he was starting up a boost and, uh, I remember having a, a meal somewhere with him and some others, and, uh, he was presenting the [00:06:30] ideas and I thought this might work and said so. Um, but I do not know any direct connection to, to the STL apart from the fact that Beman, uh, did apart implementation to, to learn the techniques and see how it worked out.

[00:06:51] **BJARNE STROUSTRUP:** I understood the need. And I was, uh, daunted by the scale of that [00:07:00] problem. I, I still am. And, uh, boost succeeded at many things and not everything. Uh, we, we still need more, especially, it's really, really hard to maintain coherence, maintaining direction in both the language and the library. And I think one thing that we've got consistently wrong, because people insisted, was to separate the [00:07:30] library issues from the language issues.

[00:07:32] **BJARNE STROUSTRUP:** The Bell Labs slogan in Computer Science Research Center where I worked was a language design is library design. And the library design is language design. So when you design a library, you basically extend a language that is language design. And when you design language features, you are, um, directing what can be done [00:08:00] in terms of library, uh, library design.

[00:08:03] **BJARNE STROUSTRUP:** The two things fit together closely when they're done well. And, um, I mean, even for the STL, um, Alex and Friends had built the STL twice, once in Lisbon, one in Ada, and they both failed. They just didn't meet the criteria that Alex had, and they, they just weren't good enough. And I've been talking to him [00:08:30] for years, um, partly agreeing that we needed such a, a library and partly disagreeing with some of his, uh, detailed language designs.

[00:08:43] **BJARNE STROUSTRUP:** And I went and I fixed, uh, C++ to be significantly better at generic programming. And, uh, Alex took that and ran with it. And so there, there was this, uh, [00:09:00] direct connection between language design and library design, which I would have liked to see go further. But, uh, the boost took it some way. The, uh, smart pointers in boost, um, compliments the not so smart pointers in the language, but they couldn't be built without the, uh, building pointers or something equivalent.

[00:09:26] **BJARNE STROUSTRUP:** I don't think that has to do with that. [00:09:30] Um, if we're going to do it again, which we won't, I think, uh, we'll need a time machine and, uh, we don't have one. Uh. We, we would need an organization for working out libraries, testing out libraries. But what we would need more than Boost had is direction. There are some examples of libraries that really should [00:10:00] have been within a framework, and they are just separate next to each other, and they don't interact as well as they should, um, because they are designed in isolation from each other.

[00:10:13] **BJARNE STROUSTRUP:** The most obvious example is, um, uh, variant, any and, uh, optional, which each, uh, gives us a, a set of [00:10:30] alternatives with some constraints, but their interfaces are totally different. Uh, anything you learn and can use the style. For optional doesn't work for, um, variant and variant and, and, uh, and any, uh, has different interfaces even though the only difference is, uh, what the set of alternatives are, [00:11:00] uh, is.

[00:11:02] **BJARNE STROUSTRUP:** And, uh, any group of people working on a coherent library would have not had that problem. Boost was encouraging libraries and it was encouraging individuals to do libraries, but they were not, um, working on a, with a coherent philosophy about, uh, across libraries. [00:11:30] Also, they tended to isolate libraries from language, uh, designs.

[00:11:36] **BJARNE STROUSTRUP:** Like we have Tuples these days and the question of whether Tuples should have been in the language or in the library should have been discussed seriously. And it wasn't, uh, it may be the right solution we got today, but the discussion was missing. Uh, the [00:12:00] boost people, the library people essentially never asks whether it should be a library or not.

[00:12:07] **BJARNE STROUSTRUP:** One of my weaknesses is I'm not a great organizer. And the, uh, governance of, uh, C++ has, has suffered from that. Uh, similarly, the organization of the standards committee, uh, tend to, to separate issues, uh, rather than going through anything central. [00:12:30] Uh, all the work is done in subcommittees or sub subcommittees.

[00:12:35] **BJARNE STROUSTRUP:** And, uh, in the end there's a plenary discussion, which is roughly the first place where everybody gets to have a look. Um, it, it, that's sort of backwards. It should be that as you go, uh, up the level, you get more senior people, you get people with a broader, um, view of the language [00:13:00] and care about the whole language as opposed to in many, many cases you have an individual library or language feature designer, uh, working sometimes for years, uh, in isolation and, uh, not looking at the rest of the, uh, language in the library.

[00:13:19] **BJARNE STROUSTRUP:** And that, that, that leads to things that doesn't interact too well. Different styles, different namings, uh, different [00:13:30] views about how to handle arrows and such. Um, we, we really would've been better off with some kind of, uh, secretariat or, uh, core group that could set direction. We have a direction group, but it only, uh, gives advice and people can ignore it very easily, and they do.

[00:13:54] **BJARNE STROUSTRUP:** Uh, similarly with Boost, I have not been [00:14:00] involved in detailed discussions of features, but I believe that the feature was discussed in isolation. And then the other next feature in isolation, and there was relatively little debate about how things interacted at at and t. We were talking about the, uh, feature interaction problem.

[00:14:23] **BJARNE STROUSTRUP:** And that was considered an absolutely essential problem that had to be dealt. In the [00:14:30] context of having the, uh, whole telecommunication system working it, it was a first order problem in the C++ committee. And I believe, uh, without real proof that that was also the problem in Boost. Um, I'm not a hundred percent certain about this, and that is why I am a little bit reluctant to talk about, um, what Boost is or what [00:15:00] Boost did, because I could, could be wrong.

[00:15:03] **BJARNE STROUSTRUP:** We needed those foundational libraries, um, especially the smart pointers. They had been proposed before and actually we had also pointer, which couldn't be, uh, be, which basically was a unique pointer, which we couldn't do till we'd fixed the language to be able to do it. Uh, another example of the interaction between library design and language design [00:15:30] and, um, the unique pointer is the one place that I can think of where you, where we simply built a drop in replacement for something we had and could yank out the original.

[00:15:44] **BJARNE STROUSTRUP:** So we now have unique pointer. We don't have auto pointer, but unique pointer is what auto pointer should have been had we been able to do it. And of course, unique pointer came out of, uh, the boost effort. Uh, so the share pointer [00:16:00] and unique pointer and share pointer, by the way, are designed so that they have enough commonality that I wouldn't level the criticism I did, uh, for any and, uh, variant.

[00:16:11] **BJARNE STROUSTRUP:** I, I could say. Uh, another thing I remember thinking about when I talked to you in uh Denver about problems. I have been involved in what's commonly known as de boosting, [00:16:30] which is to remove the Boost libraries from a large code base. And the main reason for that had nothing to do with the quality of a Boost Library.

[00:16:42] **BJARNE STROUSTRUP:** It has to do with the fact that the Boost Libraries came as a huge chunk and you couldn't just get one library. Uh, you, you had to sort of load the whole thing up. And when that happened, people were [00:17:00] using parts of Boost that wasn't anticipated. And if you are in, in some regulated business like a bank, you actually have to validate that there hasn't been, uh, something slipped in, uh, that there shouldn't be.

[00:17:17] **BJARNE STROUSTRUP:** So you had to review the libraries that you bring in. But since Boost come as came as a, as a big lump, you have to review the lump. [00:17:30] You can't just say, uh, get a unique 0.5 years early, uh, because you get all the rest of the stuff that you have to review. And you could say, then just make sure people don't use, um, those 95% of the, uh, boost that you don't want.

[00:17:50] **BJARNE STROUSTRUP:** But the point is that once it is there, somebody's going to use it. And in a large organization it is really, really hard to figure out what an individual [00:18:00] developer, um, uses what an individual developer, um, brings into, uh, the code is doing. Uh, these days you can have, uh, libraries and library controls that helps on that.

[00:18:19] **BJARNE STROUSTRUP:** But you didn't have that a few years ago. And, uh, not everybody has control over all of their, uh, uh, all of their [00:18:30] sources. And you bring in third party sources. And when you bring in third party sources, you have to validate them and make sure what they're using and not using and their boost became a problem because you couldn't say, I want just those three libraries.

[00:18:50] **BJARNE STROUSTRUP:** No, no, no, no, no, no. Uh, the, I, one of the ideas of Boost as expressed by Beman was to [00:19:00] be a place where you could try out ideas for standardization and bring the result to standardization. And that worked. And one of the reasons that, uh, boost faded a bit was that the really key, most important. Libraries were simply imported into the standard from Boost.

[00:19:24] **BJARNE STROUSTRUP:** And, uh, I had a chat with Beman [00:19:30] some years ago, and the observation was that something, I think he used the phrase, uh, 97% of the actual users of Boost was a handful of libraries. Uh, the, the smart pointers, some of the con uh, some, some of he mentioned, uh, the file system, uh, [00:20:00] uh, library and such. But really something like 97% use was a handful or, or two of, of the, the total totality.

[00:20:15] **BJARNE STROUSTRUP:** And they. Were systematically brought into the, uh, standard library, um, by Beman and others that counts like success. That that is major success, but only for the handful of [00:20:30] libraries. I mean, having lots of people looking at code, uh, creates quality and creates a breadth of use. And, and that is good. It also in cases, uh, leads to, uh, bloat as they try to solve every problem they can imagine.

[00:20:49] **BJARNE STROUSTRUP:** And, uh, there's a tendency for committees to choose, uh, the, the union of everybody's [00:21:00] desires. And in some cases, boost Phil, um, fell victim of that, and of course, in some cases C++ fell victim of that. And it is a very common thing and very hard to avoid. But, but it happened. I think it's the same in both cases.

[00:21:21] **BJARNE STROUSTRUP:** A lot of people involved, too little emphasis on cohesion. Um, and, [00:21:30] uh, uh, too, too much attempt to, to please everybody, um, all the time leading to, to bloat. And I think Boost suffered from that and WG 21 suffers from that. And it's very hard to do. It's not just C++, it's, it's an effect of having a lot of enthusiastic people working on something and, uh, things voted in, uh, or [00:22:00] having to gain consensus.

[00:22:03] **BJARNE STROUSTRUP:** You cannot do a simple solution to a, a lot of things and then see how, what works and how it works before going further. That's extremely hard to do in a committee setting, and I think it's often is a success, uh, secret source for, uh, successful projects, [00:22:30] successful languages, libraries, and so on. I mean, uh, democracy is a major strength and, uh, sometimes a, a weakness because if everybody has a vote, uh, well, some, some people don't have the knowledge, uh, to vote.

[00:22:53] **BJARNE STROUSTRUP:** Everybody in WG 21 is called experts. I don't think there is [00:23:00] 527, uh, language experts on it, on earth, uh, in, in terms of language design experts as opposed to implementers and users. Uh, but everybody has the the same vote. Furthermore, a lot of people care a lot about their own little world and their next project.

[00:23:26] **BJARNE STROUSTRUP:** A lot of developers are trained to think in [00:23:30] terms of quarters, a years standardization and library design must consider decades because a good library will last for decades. A good language feature will be unchanged for decades, and they will have to be used by people who may not even be born yet. And it'll be used in places that the designers have never heard of.

[00:23:58] **BJARNE STROUSTRUP:** And [00:24:00] that's quite hard because if you try and cover everything immediately you get bloat. And if you don't leave things open, you, you have painted yourself into a corner. So you have to do something strange, which is having a view of where you are going into a world that you don't know, but moving cautiously, [00:24:30] but leaving, um, things open so that you can fix it in the future.

[00:24:36] **BJARNE STROUSTRUP:** This is basic engineering actually. You rely on feedback. You do the best you can. You try not to close the possibilities, and then you fix it. But in a language design or a library design, you can't actually go and remove the old stuff. Uh, you, you are sort of stuck with it because you'll have a million people relying on it.[00:25:00] 

[00:25:00] **BJARNE STROUSTRUP:** And, uh, each time we try to remove something from the language or from the core libraries, the, the key libraries, we find that, well, there's some people who rely on the bits we want to get rid of. And some people can be a hundred thousand or a million and we don't know them. They may be In a country you've never visited, do you sometimes think C++ might have been better off with a benevolent dictator for [00:25:30] life like iPhone?

[00:25:31] **BJARNE STROUSTRUP:** No, I don't because I'm the obvious benevolent dictator and I make too many mistakes in particular, I, um, tend not to come down hard on, on things and uh, uh, I think a good dictator has to basically force things through. Um, I would've liked a secretariat of some sort, but that means you need some money so that the people can.

[00:25:59] **BJARNE STROUSTRUP:** [00:26:00] In, in that secretariat can afford to, to work full time at it. We don't have such people. And anyway, I didn't have a choice. The representatives of IBM, Sun and HP turned up in my office and told me that I wanted to, uh, standardize C++ on the ISO or, or I, on the ANSI rules at the time became the ISO leader.

[00:26:27] **BJARNE STROUSTRUP:** And, uh, I said, no, it's too [00:26:30] early to, uh, standardize and, uh, no. So they twisted my arm for about an hour. Ouch. Ouch. Um, with sort of solid arguments like, uh, of course we trust you, but we can't trust your employer. We cannot have a foundational library controlled by a potential competitor. And, uh, IPM and at and t was competing ever so often.

[00:26:59] **BJARNE STROUSTRUP:** And I [00:27:00] allies. They were so often, and so they were right and they said, well, and you might get run over by a bus. We can't rely on that. And so after an hour, I said, yes. Yeah, yes, yes. I really want to, uh, help you standardize C++ on the ANSI rules. And, uh, by the way, what's ANSI rules? I had no clue at the time, of course.

[00:27:24] **BJARNE STROUSTRUP:** And, uh, so the, the issue of exactly what [00:27:30] was the best way of standardizing, um, what was, was never there. I would've had to rebuild against, uh, the three largest computer manufacturers on earth at the time. For me, one little researcher in a, in a lab somewhere without any previous experience in that field.

[00:27:50] **BJARNE STROUSTRUP:** So I didn't, in the beginning it was not that different. Um, when I was. Doing it at at and [00:28:00] t at Bell Labs. I, I never had total freedom because, uh, well, I had users and when you have users, you have responsibilities and such. And I had colleagues that I was talking to. A lot of my work was wandering around, uh, trying out ideas and people talking to people.

[00:28:21] **BJARNE STROUSTRUP:** A lot of C++ was designed on, uh, other people's blackboards. And when the standards committee [00:28:30] started, the first many years we were writing papers, but then I've been writing papers before that so that I could communicate my ideas to get feedback. And, uh, it was a relatively small, fairly collegial, uh, group, um, with reasonable.

[00:28:51] **BJARNE STROUSTRUP:** A reasonable high degree of cohesion. And, uh, slowly things got more formal. Slowly people got [00:29:00] more diverse in, in technical backgrounds and aims, and slowly things got more bureaucratic and organized. So today we have more working groups that we had members when we started. Um, it's, uh, I'm not a good, uh, corporation man.

[00:29:23] **BJARNE STROUSTRUP:** And, uh, the standards committee is a bit like a, uh, a large organization [00:29:30] with, uh, many formal rules and such, which is very different from the early years. It may be necessary. Um, and I cannot at this stage. Uh, suggest an alternative, maybe with the knowledge I now have, if I had my time machine, I could go back and create a better standards committee, but that's not the way things work.

[00:29:54] **BJARNE STROUSTRUP:** Yes. So, uh, over the years I had to, [00:30:00] to learn many technical things, but also many things about how to interact with other people, with the, uh, diverse, diverse group of people. I, I remember one, uh, standards meeting coming up to the first standard where, um, the, the Germans for some reasons didn't seem to like what we were doing, and, uh, I couldn't figure out why.

[00:30:26] **BJARNE STROUSTRUP:** So I started getting up early in the morning and running [00:30:30] sort of five miles with, uh, with them because that's what they were doing. And eventually I learned exactly, uh, what their problem was. That done, I solved it. But you, you have to have to find ways of learning what people's problems are. That's an interpersonal thing.

[00:30:50] **BJARNE STROUSTRUP:** Uh, social skill. It's, it's not, uh, language design as you find it in the, uh, textbooks. [00:31:00] It's more similar to, uh, dealing with users, uh, finding what is the right solution to the user's problem because the user, by and large, describes what they want in terms of, uh, give, give me what I had, uh, what I have already, just slightly better.

[00:31:18] **BJARNE STROUSTRUP:** And, uh, that is usually not the right way of solving somebody's problem. It's the same with languages and standardization. I've always sort it as just one of the, uh, [00:31:30] really open, open source, uh, licenses and the splendid idea. Uh, the actual legality. If you asked me what's the difference between an MIT license and a Boost license, I wouldn't be able to tell you.

[00:31:43] **BJARNE STROUSTRUP:** And, uh, my view was I shouldn't have to know if they had done their job properly. It would just be that the lawyers at MIT and the lawyers for Boost, uh, said roughly the same thing in, uh, roughly the, um, [00:32:00] in, in, in different words. So obviously it was a success, uh, for the libraries that got into the standard, but, uh, I cannot say for, for every, uh, library.

[00:32:14] **BJARNE STROUSTRUP:** One of the things with all open source work and all standards work is that, uh, things that people are really interested in gets a lot of attention and things that is considered [00:32:30] more. French and more spec specialized, gets less attention and the other processes don't. There's different problems with processes.

[00:32:42] **BJARNE STROUSTRUP:** If everybody's interesting, it takes forever because our people argue about every detail for things that only few people are interested in. Uh, only a couple of people. Um, a handful of people are interested and, and they tend to be a co cohesive [00:33:00] group. So they build something that's really good for them.

[00:33:03] **BJARNE STROUSTRUP:** And if their problem happens to be a really, uh, important solution, uh, really important problem and their solution, a prop, uh, solution to what lots of people want, then that's great. 'cause then you've got a cohesive design. On the other hand, quite often it's, it's just isolated. Oh, yes. Um, maybe I. [00:33:30] I was thinking too much about the, the core libraries when I was, uh, speaking like that.

[00:33:37] **BJARNE STROUSTRUP:** Uh, obviously you need, uh, need some specialized libraries. Like I really want a unit library and, uh, apparently a few people are really interested in that and we, we will, we will get one, but it takes a long time. Uh, it took a lot of time, um, to get, uh, sim d [00:34:00] done, uh, standardization there. Lots of people need it, but few people can experiment with it and you need the latest hardware to work with.

[00:34:11] **BJARNE STROUSTRUP:** Uh, that's very different from building a, a shared point. You named the other key people that I knew. That's, uh, I, I didn't mean I, I didn't mean not to mention, uh, demon, but ov, but, uh, you, you already just did. And I think [00:34:30] also that, uh, Beman was good at, uh, getting people to agree. And, uh, he, he, he had a key role.

[00:34:39] **BJARNE STROUSTRUP:** Everybody respected him, everybody liked him. And, uh, I was not in the internal debates. Uh, in boost some of those boost people have, uh, major egos that somebody managed to, uh, keep, [00:35:00] uh, and somebody managed to keep them, uh, working together and getting a coherent stuff. And I strongly suspect that was Beman, but I wasn't in the room, so I can't say.

[00:35:14] **BJARNE STROUSTRUP:** It is possible. You need smart people. You need people who are willing to, to take a chance and go out and build something, um, and, uh, have a view about how, how it to be done. But you also have some, [00:35:30] some somebody that make sure that, uh, they don't all go into different directions. And I, I strongly, uh, I credit Beman for that.

[00:35:42] **BJARNE STROUSTRUP:** And you can go and ask, uh, Peter Dimov, uh, Dave Abrahams, uh, and Howard Hinnant and such. They all know they were in the room. I didn't have a strong connection with Beman. I spent time at every standards meeting with him, [00:36:00] uh, chatting about, uh, mostly standards work and, uh, libraries and such. But. I'm usually having a meal with him and chatting about what other things were going on in the world.

[00:36:13] **BJARNE STROUSTRUP:** Beman was a nice guy and, uh, as I said, uh, we, we had these meetings three times a year and, um, I must have had a one or two meals with him each time we were together for a, a week and, and remember there was a [00:36:30] hundred people there. So, uh, that in itself makes Beman, uh, one of the key people, and I listen to him when he speaks in the, in the committee.

[00:36:43] **BJARNE STROUSTRUP:** And, uh, sometimes we actually meet outside the, uh, standards committee, but not very often. Um, objection. And, and that, and that's, that's, that's probably just me not being the most social person there ever was. Um, I [00:37:00] have a family, I have, have a, a daytime job and, uh, things like that. I mean, I remember we had a sushi meal where he was outlining the ideas, uh, for me.

[00:37:13] **BJARNE STROUSTRUP:** Uh, and, uh, I, uh, don't remember many details of it, but I thought it was a good idea and I encouraged it. Um, so it's, he did not, he did not to my memory, [00:37:30] uh, outline, uh, decision procedures and such. It was the idea of having a group that developed libraries that could go into the standard. And, uh, we of course, both realized that not all of the libraries would go into the standard.

[00:37:48] **BJARNE STROUSTRUP:** I mean, you, you have, when you do experiments, some work and some don't. And for, uh, a thing like a standard. There's a very high barrier for [00:38:00] getting in and not getting in is not failure. It is just that we don't want to give it to the whole world, uh, all the time because there's a, there's a cost to having a library in the standard.

[00:38:15] **BJARNE STROUSTRUP:** For starters, you have maybe five, uh, at the time, five or more groups having to implement it. And that's, that's a cost and a burden. So [00:38:30] you, you don't put something in the standard unless you are really sure that that effort is worth, is worthwhile to the people that has to do it. I would have to sit and look at the libraries and, and, and point out, uh, this, that, and other.

[00:38:48] **BJARNE STROUSTRUP:** I remember there was a passing library, uh, that, that was very, very clever. But also led to enormous, uh, uh, compile times. And [00:39:00] so, uh, as far as I remember, didn't give good enough error messages. Uh, one of these template libraries that if you made no mistakes were great, uh, if you could afford the compilation, but if you make any mistake, you're in deep trouble.

[00:39:17] **BJARNE STROUSTRUP:** And therefore, beginners will come in and come away with a, um, somewhat, uh, negative view of the language as a whole. And, um, [00:39:30] I, I remember at some point I was looking at the libraries and there was just so many, um, you, and you couldn't, I was not willing to trust that just because it was in boost, the quality was high.

[00:39:46] **BJARNE STROUSTRUP:** Uh, maybe I should have been, but I think it is realistic to think that some. Libraries have gotten more, um, implementation effort than others, [00:40:00] optimization effort than others. And in particular that the effort to do a design for just about everybody is a very hard thing. And then again, the feature composition problem, um, I was a bit overwhelmed and I didn't have the resources to evaluate every single, uh, library.

[00:40:25] **BJARNE STROUSTRUP:** And if I downloaded Boost, I got every single library. [00:40:30] If I'm in the position in a large organization, we must assume that everything that was downloaded will be used because we did not have the ability to, to check what was used out of the set of libraries. That's. On that was unfortunate. Uh, but we, we had the ability to download individual libraries from some sources, but not boost, and we did not have the [00:41:00] ability to, uh, download individual boost libraries.

[00:41:04] **BJARNE STROUSTRUP:** I think they were so trying to solve the wrong problems. Ah, we, uh, don't have a good standard networking library. Why don't I have a standard socket? Why don't I have a standard, um, SSL, um, library and so on. Um. People were not doing [00:41:30] it. I don't don't even know if The Boost had all of these libraries. They had some of them, but they were not coming into the standard.

[00:41:39] **BJARNE STROUSTRUP:** And I couldn't just say, give me that, uh, part of the Boost Library. I come back to this again and again because I came back to it again and again. Aseo became a massive success. I've used it commercially. It's been used worldwide for at least 15 years [00:42:00] more now. And, uh, I've seen it used in high performance stuff.

[00:42:05] **BJARNE STROUSTRUP:** I've seen it used in high reliability stuff. Um, it's actually a great library and the standards committee, uh, couldn't agree on it. Um, and uh, there's the boost version of it and there's the, uh. plain Asio, uh, version of it. Yeah, this should, this was a success, but it was a [00:42:30] success outside the standard and it should have been inside the standard.

[00:42:33] **BJARNE STROUSTRUP:** And I've said that in public many times over the last, uh, 10 years. It was an example of something not being perfect for everybody and that some of the people for which it wasn't perfect, um, didn't come forward with something equally mature. And they came forward with several different [00:43:00] solutions to the problems of, of, as o and I was arguing that we'll just bring in as o it'll help a lot of people.

[00:43:11] **BJARNE STROUSTRUP:** And then, uh, you can come up with something, uh, better or extensions of as o uh, later. And they were not willing to. And they are. Uh, were big organizations, important organizations big enough, big enough to be taken [00:43:30] serious and big enough to block, uh, as you to be taken serious. I have to study it carefully and I have to, uh, write some examples and run some tests.

[00:43:40] **BJARNE STROUSTRUP:** And I have not done that. I am not a great fan of fiber, but it's only because they haven't convinced me yet, not because I have, uh, I can point to flaws that that, that are genuine as opposed to conjecture. I've always been a fan of, [00:44:00] um, coroutines. The first library ever in C classes in 1980 was a coroutine library.

[00:44:10] **BJARNE STROUSTRUP:** With extension to do, uh, simulations and the sun blocked it because, uh, they didn't want to implement it for their, uh, their new machine architecture with register windows. So we lost it after 10 years, but we wouldn't be talking here if it wasn't for coals. I am not a great [00:44:30] fan of meta programming. Um, it uses it in many versions, at least, uses types to represent what should be perfectly ordinary values, and that leads to, uh, enormous compiled times and, uh, hard to debug things.

[00:44:51] **BJARNE STROUSTRUP:** And I have seen people build, uh, debuggers for meta programming, uh, stuff that runs at compile [00:45:00] time and such. It got more and more complicated. Uh, what I did do, uh, mostly together with uh, Gabriel Dos Reis (GDR) , was to try and find alternatives for where the meta programming wasn't the right answer. By the way, it is the right answer if you want to build a new type, but if what you want is say, an in integer, then uh, cons, expo and cons.

[00:45:28] **BJARNE STROUSTRUP:** Valve are the right [00:45:30] things. Simple. It's a function that is, uh, computed at compile time. And that was, that takes care of, uh, vast number of, um, template, meta programming examples. And it does it elegantly without being special, uh, special skills, special, uh, notation and such. It's just a function core. And so that's that.

[00:45:57] **BJARNE STROUSTRUP:** That's. Part [00:46:00] of the reason I'm not the only one who worry about, uh, template meta programming. And I have many times gone and given talks and having people come up to me and say, C++ is awful. Just look at this meta programming stuff. It's just far too complicated, far too, uh, slow to compile. Uh, so it is also a burden, and I think it's because it is, it was often used to solve the wrong kind of problem.

[00:46:29] **BJARNE STROUSTRUP:** If you want [00:46:30] to generate a type, a new type at compile time, it is just the right thing. If you want, uh, to do a, a silly example like airto seed, it is completely wrong. That's why you just want to call a function cursive function and such. Um, and the other thing was that template meta programming was very often used to compensate for the lack of a type system.

[00:46:58] **BJARNE STROUSTRUP:** In [00:47:00] templates, templates are basically un typed until the last minute, uh, where you do the instantiation. It's, it's very much like a, um, runtime typed, uh, example, um, where the runtime typing happens at the very end and errors are detected at the very end if and only if there's an error. Um, the [00:47:30] solution to that is, uh, is concepts which specifies constraints as a set of function calls you, you, you simply ask a type if it has the properties you need, are you an iterator?

[00:47:43] **BJARNE STROUSTRUP:** Are you a random access iterator? Are you a floating point number? Uh, and that's how you handle constraints. And if you can do that, uh, a whole, uh, other load of. Uh, template meta programming just disappears. [00:48:00] Uh, you don't need them anymore. And I think that today, if people really look at it properly, they will realize that template meta programming is useful for fewer and simpler problems than they were advertised for.

[00:48:17] **BJARNE STROUSTRUP:** A lot of people liked them because they were complicated, because they were clever, um, not because they solved problems in the way that was most natural [00:48:30] to most people. I think partly, um, the need for the initial libraries were blatantly obvious and agreed by a more coherent standards committee than we have today.

[00:48:47] **BJARNE STROUSTRUP:** Um, something like, uh, unique point. Was voted in by a committee with a hundred, uh, voting members. And, uh, there [00:49:00] was a rule that you couldn't vote Two people from the same, uh, organization couldn't vote. One organization, one vote. Today, it's one person, one vote, and instead of a hundred people turning up, we have 250 people turning up, plus people, um, coming in, uh, through Zoom.

[00:49:24] **BJARNE STROUSTRUP:** Plus people actually voting without actually turning up. They don't have to. [00:49:30] We, last time I counted, and I should count again, but last time I counted, we had five hundred and twenty five twenty seven, uh, members in the committee. That is a problem. Um, in the early day, in the early days where booth libraries were coming in, uh.

[00:49:49] **BJARNE STROUSTRUP:** The people using and writing Boost were a larger fragment of the committee, and the committee was smaller and more coherent. I wouldn't, I wouldn't say [00:50:00] so. It was an effect of popularity. More people saw the committee as something good. More people saw the committee as something they, uh, that would be good for their careers too.

[00:50:15] **BJARNE STROUSTRUP:** Um, I don't really like people who come into the committee so they can write committee member on their business card. We have a few of those, but the major issue is that it got popular and [00:50:30] so suddenly, instead of thinking of the committee of about a hundred people, which I already was, was shockingly large, we are now thinking of five times that it's, it's difficult to get things through.

[00:50:44] **BJARNE STROUSTRUP:** If they are important, if they are, uh, affecting a lot of people, it's actually easier to get, uh, fairly irrelevant things through because people can't, uh, be bothered to object a burden. Yes, there's [00:51:00] two things. You have a problem, and that is that I, I don't really like to, uh, characterize and say things about people unless I'm really certain and unless it's reasonably positive.

[00:51:15] **BJARNE STROUSTRUP:** Uh, so you're not going to get any exciting, um, personal story out of me because I don't like doing that. Uh, the other thing is you are right. It's fun. Design is fun, implementation is fun. [00:51:30] And when a large committee and a large language like that, there's far more process and procedure and rules and bureaucratic stuff.

[00:51:41] **BJARNE STROUSTRUP:** Sometimes even politics. I would like to think that I don't do politics, but of course anything can be considered politics. And there are certainly people that are lobbying outside the committee, um, meetings for support so that they [00:52:00] can go and, uh, get more people voting. Uh, you have people coming into our meet, into our working group, uh, five minutes before the vote and voting the way, uh, they've been told to, um, convinced to do, but they haven't been there, and the discussion that's not fun.

[00:52:20] **BJARNE STROUSTRUP:** It's not actually good technical. Very rarely do things go totally off the rails. We have some examples, but no, [00:52:30] most of the time there's a little bit of bloat. The, the committee. It is vulnerable to, if there's two alternatives, then pick both. And that's not good design. And you can see that in some of the language features, but you can see it even more in the, uh, libraries where it's easier throw to throw in and extra parameter or an extra function or things like that.

[00:52:58] **BJARNE STROUSTRUP:** So it, it [00:53:00] bloats and, uh, I mean there, there's, I I, I've been using a, um, class called FI finally, or function called finally that, uh, generates a um, uh, object that has a distractor and it's this much code, not thickness, but number of lines. The standard committee is invo, is having something that serves that [00:53:30] purpose, but it's at least five times bigger.

[00:53:34] **BJARNE STROUSTRUP:** Because there's more features thrown in, and I don't believe those features have been thoroughly tested and the need has been thoroughly proven. But I can describe my original version in less than one page. And if you are going to write a complete description of the standard library, you will need [00:54:00] maybe three pages to explain the other one.

[00:54:03] **BJARNE STROUSTRUP:** Uh, probably more if you have, uh, examples of each of the users. And so there's a tendency to bloat, oh, it's never been in my control. You lose, you lose control the minute you get users. After that, you have influence. Um, you cannot, uh, just force your user, at least. I never was in a position to force my users to do things.

[00:54:27] **BJARNE STROUSTRUP:** I don't, I'm not the boss of my users. I [00:54:30] can't bribe my users 'cause I don't have any resources to bribe and I cannot fire them if I think they do something stupid. So that no control ever. But, uh, there, there's less overall, um, agreement about which direction we go to Now that there are too many members, that not all members have the outlook that is [00:55:00] good for standardization.

[00:55:01] **BJARNE STROUSTRUP:** They want to turn language design into product design, uh, which means that you have to please everybody, uh, to get the highest number of sales, uh, as opposed to, uh, design for. Um, a larger world where you can't teach everybody everything, and if you give people a lot of freedom, their code will not interact.

[00:55:28] **BJARNE STROUSTRUP:** And, um, [00:55:30] then finally they are focused on one thing at a time and, uh, on the next release. And not everybody in the committee has those problems. Obviously there's brilliant people, but some brilliant people even have those problems. They have, they have just gone through a career, successful career focusing on the next release.

[00:55:58] **BJARNE STROUSTRUP:** And most [00:56:00] people in the committee have not been in executive roles. They have always had a given challenge. You do this and you do it as quickly as possible, you pick the first solution that solves the problem. This is not language design, in my opinion. Um, you, you, you look for decades. You look for the conceptual overhead for people who [00:56:30] had to adopt it.

[00:56:31] **BJARNE STROUSTRUP:** Um, you, you look at what the real problems are. Don't take, uh, challenges from the literature or your current project as, as essential. Nowhere near everybody in the committee has all of those, uh, uh, properties. Good or bad, C++ has never been more successful than it is today. My guess is that it is moving in that [00:57:00] direction and is hurting the language.

[00:57:03] **BJARNE STROUSTRUP:** I've been trying to think about how to address this and the way I went was first for guidelines then. Enforced guidelines. And then that is now what's called profiles, which had very much hope to get the simplest ones into C++ 26. But people couldn't agree. The point is [00:57:30] that people want a simpler language and people want certain guarantees.

[00:57:35] **BJARNE STROUSTRUP:** Sometimes they talk about safety, sometimes they just want to make sure that certain, um, things aren't done. And my observation is that people don't agree on what that is. You can't create a single language that is both as powerful as C++ and much simpler and fulfills everybody's criteria. [00:58:00] Some people want guarantees for runtime performance.

[00:58:04] **BJARNE STROUSTRUP:** Some people want guarantees for, um, type safety like me. Uh, some people want resource safety like. Uh, C++ is had from day one, uh, if you use it. And so what you need is something where people can define a set of guarantees and have them enforced. And that's what profiles are. [00:58:30] And you can do that for safety.

[00:58:34] **BJARNE STROUSTRUP:** You can do that for performance, you can do that for teaching. I had very much wanted to be able to teach with a switch on the compiler. You will use these libraries. Some of them will be old boost libraries by the way. And you, uh, once you use those, you don't have to do these, uh, things that creates trouble, [00:59:00] uh, like mixed, signed and unsigned, um, arithmetic or, uh, dangling pointers and such.

[00:59:07] **BJARNE STROUSTRUP:** You eliminate it. And, uh, so my solution to. The, the simpler language is simply to provide super sets that, uh, in a given direction, gives you what you want. And once you've gotten what you want, a more ideal [00:59:30] language for what it is you want, you can then, uh, cut away ban at compile time, the, um, the, the features that gets in your way, uh, like dangling pointers.

[00:59:44] **BJARNE STROUSTRUP:** And you can also say, I want to use a library that has range checking a hardened library like today, uh, like we have today. But you also want to be able to say, I want the hardened library and I want to be [01:00:00] stopped from using pointers badly. So you want a subset of a superset that's, uh, the general strategy.

[01:00:08] **BJARNE STROUSTRUP:** I, I have not. It's very stupid of me, but I have not thought about it. Uh, seriously, I knew you were coming. On the other hand, I was, uh, in England last week, uh, doing some academic stuff and giving talks, so I didn't, but the first thing is be [01:00:30] sure you don't need a special built system. Ship the whole Boost Library.

[01:00:38] **BJARNE STROUSTRUP:** Give people the ability to say, give me that library. Uh, and the other thing that I would very much like to see something like Boost do would be to build profiles that is, uh, combine libraries as a means of extending the language, like Tuples or [01:01:00] Smart Pointers or STL, uh, or something very simple like Span, which by the way was something I was involved in.

[01:01:08] **BJARNE STROUSTRUP:** Uh, you extend it with that and then you subset, uh, to take away, uh, things. By the way, the reason this is not simple subsetting is you can't build an advanced library without using the low level features, without getting, uh, serious overhead. What you want is the [01:01:30] low level features to provide optimized, uh, implementations of good libraries.

[01:01:38] **BJARNE STROUSTRUP:** I mean, we are talking about things like Vector or Span or the Smart Pointers. They all are built on top of the. Facilities people complain the most about. So if something like Boost would try out building profiles, I would be very happy. [01:02:00] That is both the extension of the library and saying what guarantees you are providing that gives a se uh, a set of related libraries.

[01:02:12] **BJARNE STROUSTRUP:** And then you can say, I give you this guarantee, and then you can take away the low level stuff that, uh, is used to implement it. I really don't know. I mean, it seems to come naturally, but I don't know how or as it were where, [01:02:30] um, C++ is worldwide and I think user groups in, in various places will probably be the place to look.

[01:02:40] **BJARNE STROUSTRUP:** But then some things come out of, uh, of large corporations also. That's, I don't know. There's too many places, but they need an outlet. I, I mean, something like Boost would be good because they're somebody who has ideas, can try it [01:03:00] out and find a community. I don't know enough. And I, as I said, I'm reluctant to comment on, on personal, um, properties and such, unless I know them very, very well.

[01:03:13] **BJARNE STROUSTRUP:** And, and I, I don't know the current generation of, uh, people related to Boost and what is it, the C++ collective. Now, um, there's, there's various organizations that's interrelated [01:03:30] in ways I don't understand, so I'm not going to comment on individuals. I've talked to some of the people involved in that, and that's what I think changed its name recently.

[01:03:41] **BJARNE STROUSTRUP:** Um, but I don't know the details there. There was some pretty bad political fights. Um. About a year ago and such, or things like the Boost name and, uh, I know some of the people involved and I don't know the details and, and [01:04:00] really it's, there's, there may still be some politics there that I don't understand.

[01:04:04] **BJARNE STROUSTRUP:** Um, are there aspects of culture, war, politics, sort of the divisions we're seeing everywhere creeping into the coding world or the C++ world of the standardization world and what, what kind of effect may that have? I don't think I've seen anything like that affecting the actual technical work. I [01:04:30] said that I didn't understand fully the politics and I'm not very good at politics.

[01:04:39] **BJARNE STROUSTRUP:** Um, and I, I can't say anything meaningful about that. What's your message to WG 21 about how library standardization should, should work? Don't think that your local environment is the only environment designed for the long [01:05:00] term and for a big world. Don't forget the novices, the beginners, the experts in different field who don't actually want to be C++, uh, experts.

[01:05:15] **BJARNE STROUSTRUP:** Um, so it's a very broad spectrum design. Long-term design. Don't think it's same as your product development for your boss. I, when I teach my students, I insist they write a, [01:05:30] a tutorial sort of bit like the beginning to k and r book. And, uh, so think about how people get on board and, uh, don't think your first version.

[01:05:43] **BJARNE STROUSTRUP:** Is going to be perfect. On the other hand, you won't be able to, uh, change it after it becomes into the standards. So you better test it widely before it goes into the standard. Don't try and address everything by, by bloat, by throwing in every [01:06:00] feature there ever was. Balance, uh, anything at scale is a trade off and you have to balance concerns.

[01:06:11] **BJARNE STROUSTRUP:** Um, don't try and think you can do something major in a sprint. It's a long distance run. So have a life. And as it happens, I spent a couple of years studying philosophy. It's, it's there in the [01:06:30] background. I still read it. You can find some books in the other room. I think that's very wrong. When I was at at and t, the first, uh.

[01:06:41] **BJARNE STROUSTRUP:** Releases of C++, uh, the, uh, corporate rule says you, I couldn't put the names of individuals on, and I, uh, refused to deal with that. And in the end, after some negotiations, uh, every document, uh, [01:07:00] didn't say who the author was, but every document said based on a document by, and then the name of the individual who had done the work.

[01:07:09] **BJARNE STROUSTRUP:** What direction have you? So I, I, I actually fought that battle [ over licenses] back in 83, 84. 

[01:07:17] **RAY NOWOSIELSKI:** So carries author's names like a film has film credits? 

[01:07:20] **BJARNE STROUSTRUP:** Yes, I think so. The world is too big, but I think on average, uh, fewer names are mentioned and that's not so good [01:07:30] because then the only credit people get is their salary and then it's all for money.

[01:07:35] **BJARNE STROUSTRUP:** It's, uh, people should be able to build up. Uh, a reputation and you build up a reputation by having your name associated to work. And, uh, that reputation can be good or bad, but it should be there either. Remember, my first battle in this particular field was not in open source. It was in the documentation [01:08:00] of the earliest C++ libraries.

[01:08:03] **BJARNE STROUSTRUP:** They hadn't really invented open source then. But the, the point is that I think when people do something like a library, it should get a name on it. I'm all in favor of that, and it, it can't be that many people. Since I fought the first battle in, uh, in 80, 82, 83, 84, against at and t actually the biggest company, uh, in the US at the time, [01:08:30] and I won.

[01:08:31] **BJARNE STROUSTRUP:** You won. Look at, look at those documents. They, they have names on them. It was actually a compromise. They had a rule, they couldn't, uh, go back on. They couldn't change the whole rule of all of at and t just for me. On the other hand, uh, I wanted my friends and colleagues acknowledged, and we found this formula, uh, which simply said, based on, so we didn't say they had written it.

[01:08:58] **BJARNE STROUSTRUP:** We said it was based [01:09:00] on something they had written, basically, in many cases. The only thing they hadn't written was that sentence I put on, on the way out. You have to be flexible about these things. It's, it's a very difficult issue as you well know.

