# BOOST_MARSHALL_CLOW_STRINGOUT_v00

- - - -
filmed Date: 2025-12-16   
location: Poway CA  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1154755036/6f9fa1c6fc?fl=ls&fe=ec  
summary: Personified 3 different Boost.Docu interviewee types–1, the Boost author (detailing Boost.Algorithm, Stepanov as inspiration, Abrahams-led formal review explained, BoostCon stories); 2, the WG21 leader (LWG chair 2015-2020, talked of the change in Boost standardization, Asio & Kohlhoff, his desire for Networking and wish for Asio to have been accepted, touching standing ovation story of his final moment after C++20), and 3, the Alliance team (let go by Qualcomm before brought on as first Alliance employee & paid to do C++lib, WG21 & Boost work he would have likely had to stop doing, gave account of Foundation vs Alliance showdown, decline of Boost under Foundation, why he thinks it came down to Alliance, detailed what Alliance has been pursuing for Boost, “a project that accomplished its mission and is in search of its next mission,” with Alliance helping them find it  
- - - - 

## Transcript Start

[00:00:00] **RAY NOWOSIELSKI:** Be careful. Don't trip over anything. (laughs) 

[00:00:05] **MARSHALL CLOW:** Hmm. Yes, that's very bright. Um, my name is Marshall Clow. I am. I have been a boost contributor for going on 20 years now. Um, I write software for Boost, well wrote, I I'm slouching towards retirement, as I like to call it. Um, for both, uh, boost and the LVM project and a few other [00:00:30] things. What is a maintainer?

[00:00:31] **MARSHALL CLOW:** A maintainer is, well, the theological answer, somebody who maintains something, but in particular, um, from the boost point of view, maintainer is someone who is responsible for a library, one or more libraries, and their job is to make sure that it continues to build. Even though environments change, new compilers are released, old compilers are retired.

[00:00:55] **MARSHALL CLOW:** New operating systems, new co new versions of the C++ standard are [00:01:00] released. Um, bugs are reported, but that those bugs get fixed or get at least get triaged to the point where somebody could say, yeah, no, this is not really a bug. This is a, this is a difference in, um, difference in design. Or this is, no, this, the person who was using this was mistaken.

[00:01:20] **MARSHALL CLOW:** This is how it's supposed to work. Difference between an author and a maintainer, um, at the beginning of a project. Those, those are [00:01:30] usually the same person, but as time goes on, sometimes people, somebody who has written a library, um, no longer has the time or the interest or the inclination to continue working on it because, um, why they have a new interest, they have a new job.

[00:01:48] **MARSHALL CLOW:** Uh, they get married and have kids. Boy, that's, that's a big time sink, as you know. Um, and so somebody else will come along and offer to help and gradually sometimes they end up [00:02:00] taking over that project and become, you know, the main, uh, the main go-to person for a project. Nico Josuttis wrote Boost Array back in the day, back in the pre C++ 11 day, and, um, then went off to do other things, you know, got accepted into Boost and went off to do other things, to write books and to, uh, standby.

[00:02:25] **MARSHALL CLOW:** Nico Josuttis wrote Boost Array and then, which [00:02:30] was a, a popular library in the pre plus, pre C++ 11 days. And then C++ 11 was released with STD Array, which is a drop in replacement for boost array. And matter of fact, you could argue that that that Boost Array was one of the inspirations for the, for standardization.

[00:02:52] **MARSHALL CLOW:** Nico decided to go off and do other things like writing books and working on thread and a whole bunch of other things, and he didn't really have much [00:03:00] time for booster. And there, frankly, there are not a lot of people who are work who are using booster array anymore. But I offered to pick it up and maintain it, which basically means if people report bugs, I will look at the bugs and say and fix them.

[00:03:15] **MARSHALL CLOW:** But there really haven't been any bugs in a couple years. I was the lead engineer on Libs C++. I'm, I'm sure we'll talk about that later, but I was, and Lib C++ is a C++ standard library implementation. And [00:03:30] I used to joke that my code went into a billion to a billion and a half devices every single year.

[00:03:37] **MARSHALL CLOW:** Every. iOS device. Every iPhone, every iPad, every Mac os device, every Android device, um, a whole bunch of routers and embedded things. You, it's amazing how much Android software, how much Android hardware there is out there. Basically, every point of sale terminal there is manufacturing in the last three or [00:04:00] four years runs Android.

[00:04:01] **MARSHALL CLOW:** And so my software is on that. I was down at this last weekend, I was down at, in South Texas at SpaceX, and I was asking people, you know, what kind of stuff, what kind of, what do they run on their software stack? And I was pretty sure that Libs C++ was in their software stack. They, they didn't want to confirm anything.

[00:04:21] **MARSHALL CLOW:** They're, they're a very secretive bunch. Yeah, I, I'm very confident that. A billion and a half devices a year is probably a low estimate at [00:04:30] this point. Boost is not going to be as prevalent as Libs Plus Plus just because the hardware and software vendors don't ship it as part of the os. But still, yeah, boost.

[00:04:41] **MARSHALL CLOW:** Boost has made a huge difference in the computing world and shows up in a lot of places. Boost is a, um, one of the more successful long-term open source software projects. Uh, open source, I mean, where people make the source available to anybody under a fairly, [00:05:00] uh, permissive license that they can incorporate into their own projects, or they can take it and change it, port it to new, new hardware, new software, new ecosystems, and use it to build things.

[00:05:15] **MARSHALL CLOW:** Um, it's like that old joke about, um, was it, was it Einstein who said the reason I can see. Farther than everybody before is 'cause I'm standing on the shoulders of giants. I won't claim that the people who write [00:05:30] Boost are giants, but certainly people who are writing software using Boost are standing on their shoulders and using it to build bigger things than they would be able to otherwise.

[00:05:41] **MARSHALL CLOW:** It's hard to, to pull something down to just a little phrase. I mean, when you said, you know, what phrase jumps to mind? I was like lifting kids up so they can see lifting, lifting other people up so they can do more things. A word No, there's come to mind, there's, there's so much [00:06:00] there. There's um, there's the people on the committee, there's the, um, there's the accomplishments of the committee.

[00:06:06] **MARSHALL CLOW:** There's the challenges that they have faced. There's the WG 21 is stands for Working Group 21. It is a. Um, it's a working group that's part of the International Standards Organization. Um, it's tasked with standardizing C++. There are lots of working groups. They do various things. WG 14, for [00:06:30] example, standardize is the group that works on C.

[00:06:32] **MARSHALL CLOW:** Um, but it's responsible for the language and the, the runtime environment, like the standard library. I was a member of the committee for 10 years. Um, I spent a five of those years, um, leading one of the, the working groups inside of it, the library working group. That group that is in charge of the, um, standard library definition.

[00:06:57] **MARSHALL CLOW:** Now, we should back up for a second and say [00:07:00] really all that, the, the only product that technically comes outta WG 21 is a written document. It is the C++ standard. Okay. That's all it, um, all that comes out of it. But the members of the standards committee, many of them work on implementations of the, uh, of either the language or the standard library or both.

[00:07:24] **MARSHALL CLOW:** And so they're, they're always working with their, their implementation in mind. How [00:07:30] am I going to do this in lib, C++ or in GCC or in the Microsoft compiler or whatever. Um, WG 21 is, is a, well, the last meeting I was at was, you know, 130 people all with their own agendas all getting pulled different ways, trying to, trying to go in the same direction, which is to produce a, uh, a new version of the standard that people can agree on, and then people can [00:08:00] implement and then people can use those implementations.

[00:08:03] **MARSHALL CLOW:** Nobody who is writing software really uses the standard. The standard is a definition for implementers who provide implementations for people to use. WG 21 has some, some really smart people in it. In general, people work together pretty well, although there's a lot of problems with people who have different visions of what the standards, how the, how the language [00:08:30] should work, how the library should work.

[00:08:32] **MARSHALL CLOW:** And so there tends to be some fairly heated arguments. There was a proposal from Bjarne about, uh, unified function calls syntax. That was a, actually a major change to library the language, which would've simplified things for users while complicating things for implementers. And we discussed it for a couple years and it got, it was voted on by several of the subgroups and then came to.

[00:08:59] **MARSHALL CLOW:** Came to the [00:09:00] final vote at the plenary session, what in Jacksonville, I think in 2016. And a lot of people stood up and spoke out against it, and there was a lot of discussion and eventually it was voted down. Which is kind of surprising because usually by the time it gets to the plenary session, the final thing, it's pretty much everything's cut and dry.

[00:09:18] **MARSHALL CLOW:** The objections have been hashed out by that. You know, there was a lot of disagreement in the final plenary session and people were talking about how raising very general objections and [00:09:30] people were getting very frustrated, having stuff coming up at the last minute, as it were. Could, I could believe that auto pointer was, is well, auto Pointers and smart pointers, you know, I mean, well, smart pointers, shared pointers are two very different things.

[00:09:45] **MARSHALL CLOW:** And Auto pointer was,

[00:09:50] **MARSHALL CLOW:** yeah, not, I mean, may have been the best thing you could do for C++ oh three. Um, in C++ 11, we got Move Semantics and [00:10:00] we were able to retire Auto pointer for, um, for unique pointer, um, which has much more, much easier understand semantics. How's that? Um, but, um, I was not there in 95. I didn't join the committee until right 2011 first, the first, um, [00:10:30] the first meeting after C++ 11 was approved.

[00:10:35] **MARSHALL CLOW:** So we were just starting the next round of, I fit much better in the, the first or the second bin than the third, even though I was employed by the C++ Alliance for a couple years. Yeah, most of that was as part of my standardization work and most, and it was entirely remote. It was all. Out of the office upstairs.

[00:10:56] **MARSHALL CLOW:** The whole disagreements between the Boost Foundation and the c [00:11:00] plus plus Alliance. While I have opinions, I tried to stay out of the line of fire.

[00:11:05] **RAY NOWOSIELSKI:** Were you already gone by that point? From the Alliance?

[00:11:08] **MARSHALL CLOW:** I, yeah. I was gone from the Alliance by 2020 almost entirely. There were attempts to recruit me on both sites.

[00:11:15] **MARSHALL CLOW:** My impression was that the Boost Foundation did was not really interested in continuing. Its the stewardship of Boost. They're the Boost Foundation. They wanted to do thing, other things like the Beman Project and so on. [00:11:30] Kind of sad, but there it is. Oh, it's sad because, um, the people who were, who were part of the Boost Foundation Board at that point had, had been contributors to boost for a long time.

[00:11:42] **MARSHALL CLOW:** Some of 'em, and, um, will miss their contributions. It's hard for me to say because I have not. Attended any events and haven't, so I haven't really talked to people face to face and this is the kind of thing you get, you know, sitting in a bar in the evening over a beer or you know, talking in a [00:12:00] hallway between sessions or things like that.

[00:12:02] **MARSHALL CLOW:** Certainly can't speak to anybody else for anybody else about that because I, you know, I haven't had those conversations with other people because, uh, he was kind of in the middle of a lot of that, you know, he is, um, last time I, I talked to him, he was on the Boost Foundation Board, but he also is a recent Boost author.

[00:12:20] **MARSHALL CLOW:** I am happy that there are more libraries being added to Boost, um, that the focus has been hard to say widened when you're talking about focus, but [00:12:30] the, that, but is no longer has a, a laser-like focus on things that can go into the standard library, which is great because I don't ever see, for example, beast.

[00:12:42] **MARSHALL CLOW:** Going into the standard library and some of the other new libraries, which is fine. They're generally useful and they feel a need, but they don't have to be in the standard library for a long time up until like C++ 14 time. A lot of the things in Boost [00:13:00] were poked at, were proposed specifically so they could be standardized, is to gain experience in implementing things so that they could be standardized.

[00:13:10] **MARSHALL CLOW:** That, I mean, the whole point of the committee at that point, you know, in the, in the aughts in the early teens was the C++ standard standardization committee was there to standardize existing practice. And Boost was one of the places where people would gather, would get implementation experience and [00:13:30] usage experience and so on.

[00:13:31] **MARSHALL CLOW:** It's, it, it has changed its mission. Um, like I said, if you look at the new libraries that have been accepted in the last say. Three or four releases, you know, I don't see any of them, um, going to standard, going to standardization and that's fine. But they are generally useful. They're, they can be used by a lot of people to help build bigger things, produce libraries that people can use to build cool stuff, which is kind of, was kind of [00:14:00] the subtext of the original boost as well.

[00:14:03] **MARSHALL CLOW:** But very clearly understood the original boost in the, you know, 2004, 5, 6, 7, 8, 9 timeframe was and build libraries that can be added to the standard library. And I don't think there's near as much of that anymore, which is fine. There are more paths to standardization now in, back in the day, you know, if you wanted to standardize something, 'cause submitting it to Boost was to, would give you a big leg up because it [00:14:30] shows that, you know, you have, you have, you have past review, you have, people are using your code and so on.

[00:14:35] **MARSHALL CLOW:** Um, now that's less necessary because there's lots of other paths. Howard Hinan took his chrono library and did not submit it to Boost, just put it out there on GitHub and people were using it. He had thousands of users over for four or five years before it was standardized. And there's nothing that says that Boost is, um, the only way to do things.

[00:14:58] **MARSHALL CLOW:** It was just, it was a [00:15:00] major way before, and it's not as much now. Where did I grow up? I grew up here in San Diego, um, down by San Diego State. My dad was an accountant. Where's that at? Where's that located from here? About 20 miles that way. And, uh, my dad was an accountant. And what kind of life did we have?

[00:15:18] **MARSHALL CLOW:** Uh, it was suburban life. It was a, it was a fun time to grow up. Um, lots of things to do. I. I have four sisters and a brother. So there we, we were [00:15:30] always a hoard. Not so much my dad and not so much my mom. It's kind of independent. Although I, I take behaviors from both of them. Um, 

[00:15:39] **RAY NOWOSIELSKI:** what was your first kind of, your first love?

[00:15:41] **RAY NOWOSIELSKI:** Was it code or was it 

[00:15:41] **MARSHALL CLOW:** something else? So all through growing up, junior high school, high school, I kept trying things and falling in love with them and, and thinking about is you, I do this, could I do this for a living? And the answer was yes. And then they would last a couple years and then I discovered something else that I liked.

[00:15:59] **MARSHALL CLOW:** And so I went [00:16:00] through printing and graphic arts and architecture and chemistry. And then college, I took a computer class and it's like, oh, there we go. 'cause I was a chemistry major in college, um, for a couple years. And before that, I was looking at, when I was looking at schools to go to college, I was looking for schools.

[00:16:22] **MARSHALL CLOW:** I had good architecture programs and, um. So on, and it's, I like solving puzzles. I was [00:16:30] one of these kind of kids where you would bring, you know, I get for Christmas from, from my parents, I'd get a book of brain teasers and I'd sit down and work my way through the book. Writing code is the most of that.

[00:16:41] **MARSHALL CLOW:** It's all about solving puzzles. You have a puzzle, you have a problem, and you need to figure out how to solve it. And then when you, you try to solve it and it doesn't work, now you have a bigger puzzle. And it's like, it's like building structures in your head and, and turning them around and looking at them and pointing, pointing at it and say, [00:17:00] oh, that's what's not right.

[00:17:02] **MARSHALL CLOW:** And figuring it out. If you like brain teasers, if you like, you know, solving problems, then writing code is a great thing. I don't need to actually do either of the second or the third. My wife is a, is a great cook, which is a constant struggle for me because, well, I'd like to be skinnier, but. She's a really good, um, I got a job with a company doing, um, printer driver development [00:17:30] for Mac, for Mac Os.

[00:17:31] **MARSHALL CLOW:** Um, they were up in Oceanside. I was living in Carlsbad at the time and they had built a framework for writing printer drivers, which was an amazingly arcane art then. And there were only a couple of companies outside of Apple who, who were actually writing printer drivers, I think two. And then we started, uh, one of the guys I worked with was, was trying to do stuff in C++.

[00:17:56] **MARSHALL CLOW:** And so we started trying to write chunks of [00:18:00] the printer driver in C++. And it was like, oh yeah, this was back when C++ was like supposedly C with objects. And we did some of that. It was reasonably successful, successful enough that I wanted to keep trying it. And eventually, um, I left there and went to work for hp.

[00:18:18] **MARSHALL CLOW:** Doing the same kind of thing, printer drivers, and continuing to write stuff in C++ and talking to people about it. I was bouncing around through the, through the late eighties [00:18:30] and middle nineties and, um, I went to work for, uh, HP for a while, and Aladdin Systems and Adobe doing mostly C++.

[00:18:39] **MARSHALL CLOW:** And these places I ended up at Qualcomm again, working on Eudora, an email client. Uh, it was mostly C with some C++ in it, but, um,

[00:18:55] **MARSHALL CLOW:** the, the group of Macintosh software developers [00:19:00] in the, in the eighties and nineties was actually pretty small, independent Macintosh software developers, and so we all knew each other. Aladdin was a great place for that because. They talked to everybody and so got to know everybody. And one, uh, after I left Aladdin, one of the, one of my friends from that era decided to put on a little software company conference up in the, uh, Santa Cruz mountains.

[00:19:25] **MARSHALL CLOW:** This was fall of 2003. And I had started at, at [00:19:30] Qualcomm couple years before. And I said, sure, let's, let's go to this. So I took a couple days off and I was gonna say, got in a VW microbus and drive off to Santa Cruz. But it wasn't that, it was, I got in our, the van, we hauled the kids around in and headed up towards Santa Cruz and stopped in LA and picked up a couple of my friends who we, who was going, who were going to the conference as well.

[00:19:50] **MARSHALL CLOW:** And we went up there and it was a fun conference. They did it just once. 'cause it wasn't, didn't, was not a huge financial success. [00:20:00] 2003, fall of two th September, 2003. But the keynote speaker was Alex Stoff and he gave a talk called the. The greatest common measure 2,500 years. Um, and it's a great talk.

[00:20:17] **MARSHALL CLOW:** Okay? It is an amazing talk. You can find it on YouTube. You search for step awe of greatest common measure. Um, you can find it if you watch it, if you look around the, the audience, you [00:20:30] probably see me there. But it was mostly about generic programming because the greatest, the search for solving the greatest common measure starts off very specific.

[00:20:42] **MARSHALL CLOW:** And, and as mathematic progresses, it becomes more and more generic. The, the, the solutions become more and more general, I should say. And you know, at this point in 2003, Alex had, um, had in fact, you know, produced the first version of the [00:21:00] standard template library, and it had been accepted into C++ oh three.

[00:21:05] **MARSHALL CLOW:** It was part of C++ 2003, and this was a revelation to me. I went home and started tearing it apart and trying to write all sorts of things and basically that, that changed my whole outlook on programming and, and basically sent my career off in a completely different direction. The generic programming is this idea that you have, that you describe [00:21:30] a set of operations that work on, not on concrete objects, but as on an abstraction of, or concrete values or concrete that, but on a abstractions of that.

[00:21:45] **MARSHALL CLOW:** And so for example, vector in the standard C++ library vector is a dynamic array. Okay? It's an array of what? It's an array of things. Okay. You can have a vector that holds. [00:22:00] You can have a, a vector that holds floats. You can have a vector that holds strings. You can have a vector that holds complex numbers.

[00:22:07] **MARSHALL CLOW:** You could have a, a vector that holds whatever object you just made up. Um, the point is, is that you don't have to write a dynamic array of SA dynamic array of floats, a dynamic array of complexes. You, you have vector and it, it, um, it describes how to write a dynamic array of pretty much anything that, [00:22:30] that fits the requirements and the requirements, uh, for to go into Vector are pretty minimal.

[00:22:36] **MARSHALL CLOW:** Worship at the alter of stepping off because he is a brilliant man, a very nice man, generally a great guy. But he is, he was not the only person doing generic programming, but he was the one who, um, may basically got it to the point where it was part of the standard library. I wish I had known what he was doing when I was at [00:23:00] hp.

[00:23:00] **MARSHALL CLOW:** And he was at hp, but he was in, um, Palo Alto and I was in Rancho Bernardo. I was Rancho Bernardo. I was working in Rancho offices like three miles that way. And so he was 500 miles away. If I'd have known what he was doing, I would've tried my best to get to become part of his group and work with them.

[00:23:18] **MARSHALL CLOW:** But it didn't happen 'cause I didn't know. Um, but the second part, the second question you asked why this was so important is I have wor, I [00:23:30] read a bunch of code in c in another languages where you had to write, if you wanted a dynamic array, you had to write a dynamic array for inch. And then you had to basically create an entire new thing, which was a dynamic array of strings and or a link list of.

[00:23:50] **MARSHALL CLOW:** Points or, and it's just like nobody likes doing things over and over again, and you end up with a bunch of things that look like they ought to be [00:24:00] the same, but are subtly different. And it makes it hard to reason about things. One of the things that the, that generic programming does is it lowers your cognitive load.

[00:24:11] **MARSHALL CLOW:** You don't need to know that. Well, this implementation, implementation of dynamic array, of complex numbers has these special cases as opposed to this dynamic array of floating point numbers. You don't need to worry about that. You say it's a vector. Okay, [00:24:30] I understand a vector. Um, or I understand what you know, uh, a.

[00:24:37] **MARSHALL CLOW:** A map is, I understand where the, um, where the advantages and the disadvantages of the map are. And the fact that the STL gives you requirements and performance guarantees is really important because you then you can, you can decide is this the right choice for me? If not, I mean, one of the things that Boost has done is [00:25:00] convinced people that it's okay to write your own containers.

[00:25:03] **MARSHALL CLOW:** Um, it's okay to write your own algorithms. I've done a bunch of talks at various places about you should write your own algorithms. You know, the ones that are in the standard library are not the be all and end all. Um, and so that's a great thing. But the standard library kind of points the way, points a way says, you know, if you want to play nice with the rest of the standard [00:25:30] library, you should think about doing it this way.

[00:25:33] **MARSHALL CLOW:** And, and Boost is like, yeah, we write our containers in the style of the standard library and document them in the standard of the standard library here. Here's, here are the performance guarantees you get. Here's the memory usage guarantees you get. I was not involved in Boost until about 2003, so this would not be, this would be hearsay at best.

[00:25:56] **MARSHALL CLOW:** Stefano's work and others, right. [00:26:00] Basically pointed, you know, pointed out a way. And the people who founded Boost, Beman and Dave Abrahams and so on were fans were, um, thought this was a good way to go. And so they picked it up and ran with it. Um, a lot of the things that were in the early versions of Boost were things that ended up in C++ 11 or 17.

[00:26:27] **MARSHALL CLOW:** Um, you. Boost Optional, for [00:26:30] example, was very, very early on, and it made it into C++ 17. There's, there's too much that happened there. I mean, he was, he was born in Russia. He was identified as a math prodigy and enrolled in a, um, in a special math to school where he did math for eight hours a day from the time he was about five.

[00:26:50] **MARSHALL CLOW:** And then, you know, he and his, his parents, he and his parents were, came to the United States. There's a whole story there that, that I know very little about. [00:27:00] Um, he likes to joke that he's the only one in his math class who is not the head of some math department somewhere, but he has a tour award, so I guess that's okay.

[00:27:13] **MARSHALL CLOW:** I've met him a few times. He's, he's a gracious man. He's a brilliant man. But I wish I had had more interactions with him. Like I said, I wish I had known what he was doing at hp. When I was at hp. I would've figured out some way to. Attach myself to his [00:27:30] project to contribute. Sean [ Parent], I've known Sean for a long time.

[00:27:33] **MARSHALL CLOW:** Sean is, Sean is also a, a very smart person, but, um, not in the same kind of way that BNI is. Sean is a very, very, he likes to think hard about abstract things, but his focus is almost entirely on practical things. You know, the working on the transition, when he was at Apple, working on the transition from 68,000 to Power pc, he wrote a lot of software that made that go [00:28:00] very, very smoothly.

[00:28:01] **MARSHALL CLOW:** Um, that very, when he was working on Photoshop, he was very concerned about performance and reliability and things like that. When, um. When he started his group at Adobe, that was one of the places that I thought about. I was pretty happy at Qualcomm at the time, but I kept that in the back of my mind that if things went bad at Qualcomm, I could call up Sean and see if I could go [00:28:30] back to Adobe working in his group.

[00:28:31] **MARSHALL CLOW:** 'cause his group had a lot of very smart people in it. Lately, lately he's been doing, lately being the last 10 years, he's been doing a lot more theoretical stuff. And it's, and you know, in interesting stuff, um, taking small to medium sized projects and trying to figure out the underlying patterns and then writing software to solve.

[00:28:51] **MARSHALL CLOW:** After seeing Alex's keynote, I went, I went away with my head spinning and, and started looking at [00:29:00] hard at the standard template library and reading the papers he'd written and thinking about these and tr and using them and learning all I could about them and. Looking for people who are doing similar kind of stuff.

[00:29:15] **MARSHALL CLOW:** And eventually I found Boost, I found a couple of other groups, but Boost was far away the, I won't say most popular, the most active people were talking about it. I talked, I asked people about it. I joined the mailing list in the fall of [00:29:30] 2004. I lurked for a little while. I started contributing. Um, I started providing, you know, commentary, providing patches, reviewing things.

[00:29:40] **MARSHALL CLOW:** There's a whole bunch of people who have, I was struck by the idea that there were a whole bunch of people here who have the same fascination with generic programs that I had developed on my own. And that there was lots of different ways to look at it. And so that was a great thing. Um, I did, I was working at [00:30:00] Qualcomm on Eudora and I wrote some, some things in C++ there.

[00:30:06] **MARSHALL CLOW:** Um, I was, um, contributing to boost, uh, when Boost Con got started in 2007. I managed to talk to my Boston and let me go to it and I had a great time. And so I went to Boost, boost Con. This was the first year. This 2025 was the first year that I had not attended Boost Con. Boost Con C++. Now it's the same conference, um, run by the same people.

[00:30:29] **MARSHALL CLOW:** Yeah, in [00:30:30] the same place. It has not been running for 19 consecutive years. There were a couple years during COVID where there weren't any, but um, there are only, only two people now who have been to every Boost Con that I know of. Who's that? Um, Zach is one of them and, um, Jeff Garland's the other. For a long time there were three of us, but this was this year.

[00:30:50] **MARSHALL CLOW:** I wasn't there. I heard about it on the Boost mailing list. I'd have to go back and look it up, but Dave Abrahams said, Hey, we're gonna have a conference, you know, Dave Abrahams and um, Beman Dawes said, [00:31:00] we're gonna have a conference. It's gonna be in Aspen, it's gonna be in May. You know, invited people to submit, submit, talk proposals.

[00:31:08] **MARSHALL CLOW:** I had not done anything that I felt was worthy of that. So I didn't submit a proposal, but I showed up and talked to people, got to meet all these people. I'd been exchanging email with Dave Abrahams was there, and, um, Sean was there. Um, Beman was there. Um, those were the three that I, that stood [00:31:30] out to me.

[00:31:30] **MARSHALL CLOW:** But there were a bunch of other people, Sean, many, many times. Um, Dave, a few dozen. Um, I almost went to work for Dave at one point, not to boost pro consulting. Um, and, um,

[00:31:49] **MARSHALL CLOW:** Sean and Dave and Beman, I, I didn't meet Beman that many times. I met him at a lot of boost cons and a few, and once or twice at. [00:32:00] At, uh, CPP Con and then, but he was mostly retired from the Standards committee by the time I started. He was, I saw him a few times at standards committees, just sitting down with people in writing code.

[00:32:12] **MARSHALL CLOW:** You know, Jeff Garland has run the library a week thing at Boost Con for Forever, and I've helped him out with that for many years. But, you know, it's like he brings a few problems and people sit down and they, they go away and they talk about the problem. They talk about Popable [00:32:30] solutions, and then we sit down and rewrite code and try to solve them.

[00:32:34] **MARSHALL CLOW:** And then when the conference is over, people go home and keep working on it. And sometimes you get a Boost Library out of it. One year we did algorithms and I got a library out of it. Boost Algorithm, that's where it started. Jeff and I talked about. Doing algorithms for library in a week and people started throwing out ideas for algorithms and I started writing down ideas and people wrote some, which was great, and I wrote some and I went [00:33:00] away and said, I'm gonna run with this.

[00:33:01] **MARSHALL CLOW:** And I ran with it. And then Sean popped up with, you know, it's a real shame that there isn't a good Boyer Moore implementation for C++. And I said, oh, okay, I can do that. Went off, read the Boyer Moore papers and there's Boyer Moore and Boyer Moore Horse School, and there's basically three algorithms there and implemented them and tried them and found bugs in them and fixed them and so on.

[00:33:27] **MARSHALL CLOW:** And eventually packaged these all up into [00:33:30] an algorithms library and put it out for review. Um, I found somebody, I found Dave Abrahams to be the review manager, and Dave said, I'll, I'll review your library if you review, if you, you manage a review of this library. I said, okay. I reviewed a. Library that was not accepted was, was, was a proposed boost process library.

[00:33:49] **MARSHALL CLOW:** Process management resigned. He was resigned. We were, we were talking as the reviews came in and he was looking at them and answering questions. 'cause the review process is very interactive. You know, [00:34:00] people review it and they ask questions and they, they say, I have concerns and so on. And some of the concerns they pointed out were pretty serious.

[00:34:07] **MARSHALL CLOW:** And, you know, I said to someone, at some point, most of the way through the review, it says, he said, I said to him, I said, I don't think you, the library's gonna be accepted. And he said, yeah, I know. Because somebody had pointed out a few, um, a few, what, what he thought, and I thought were, were fundamental flaws.

[00:34:26] **MARSHALL CLOW:** Things that, things that had not actually been addressed [00:34:30] or things that, things that weren't, were going to surprise people, or things that just didn't work. And so he went away and, and worked on it for a while and submitted to for review again later. Couple, three years later, I believe the second time it was accepted.

[00:34:47] **MARSHALL CLOW:** Okay. But, um, but the library was, the review process was, was interesting. People were like, these lib algorithms, you are fine, but, but you need more. And I'm like, yeah, I'm going to make more. [00:35:00] But this is, this is a good set to start with. And I had all the C++ the new algorithms and C++ 11 and, and a few others.

[00:35:08] **MARSHALL CLOW:** It was accepted with conditions. Some of the conditions were like, you know, some of the documentation needs to be better and, and you need to think about how you're gonna test this and so on. But in, in general, it was a pretty, is a successful review. And it got added. 2013, 2014, something like that. It's been 10 years.

[00:35:29] **MARSHALL CLOW:** [00:35:30] It was, um. I'd have to go back and look what version of Boost It it appeared in. It was pre 1.50, so it's been 40, there's been 40 boost releases with it in it. And along the way, along the way, I started picking up various administrative tasks in Boost, you know, review, review manager occasionally, and, um, mailing list moderator.

[00:35:54] **MARSHALL CLOW:** And much later I became one of the review managers series of corridor conversations, C++ com [00:36:00] standards committee in France. Um, I have always opined that the, that no matter which conference you go to, the best track in the conference is always what I call the hallway track, but the discussions that happen in the hallway between conferences or at dinner in the evenings or whatever, see additionally a site might foster C++ standards activity by, uh, established existing practice because the standards committee was.

[00:36:29] **MARSHALL CLOW:** Supposed [00:36:30] to be standardized existing practice. Well, boost was one of the, as it says here, one of the things was to invent existing practice to bring, bring it into existence so that it could become existing practice so that it could be standardized. High quality libraries. Yes. Review volunteer peer reviewers, whether qualifications were being a peer reviewers who does a peer review, volunteer reviewers, how do you qualifications for being a peer reviewer?

[00:36:55] **MARSHALL CLOW:** Basically self identify. Say, hi, I'd like to review stuff and [00:37:00] this is, this is why I believe my expertise is worth, worth considering. And basically it said, you know, says here the moderators might try to fill out people, filter out people who don't have a reasonable background. But in general, that was a pretty low bar pe If you're interested in the project that a library is trying to solve, and you know, you're not just some, you know, you have at least some track record with Boost.

[00:37:29] **MARSHALL CLOW:** Being, [00:37:30] submitting a review is fine for a long time. This, this was, was how Boost was laid out was, you know, a, a website full of libraries, the source codes available, and a process for adding stuff as well along the way. We have picked up, um, picked up a lot of infrastructure around that, you know, automated testing and release management and so on.

[00:37:59] **MARSHALL CLOW:** I'm not [00:38:00] sure how to answer that. How much did Beman get right off the bat? He got a, you look at this proposal, he got a lot, right? This is, this is surprisingly similar to how Boost was in, you know, 2003, 2004. Gotcha. So this was a, um. This proposal is, I mean, there are, there are differences, but the, the major thrust of this was very much so, um, a lot of, a lot of this in the questions and proposed answers is, is to be decided, but [00:38:30] still, you know, what support is available for the libraries news group or mailing lists.

[00:38:33] **MARSHALL CLOW:** Yeah, we, we had mailing lists split here early. Will libraries become part of the next C++ standard? No. But as the extent a library becomes existing, practices practice, the likelihood increases that someone might propose it for future standardization. Good people, a shared vision, the right time.

[00:38:51] **MARSHALL CLOW:** There were a bunch of tools that were becoming available and made it a lot easier to do it. Um, obviously the internet in the late nineties, but also, [00:39:00] um, subversion and, you know, source just. Not distributed, but source control systems that made it easy. The ability to, you know, buy hosting, not that Boost actually bought hosting, but other people bought hosting for Boost.

[00:39:14] **MARSHALL CLOW:** The question is really, um, there's nobody who's going to found something like Boost again, because Boost was, was founded with a specific set of guidelines in mind that you've, that are written in that document. You handed me the part [00:39:30] of the thing, the impetus for Boost was, you know, the paucity of, of things in the standard library and the STL.

[00:39:38] **MARSHALL CLOW:** There was a, people had lots of ideas for new algorithms, new containers, new facilities. Optional is one of them. You know, something that can hold a value or nothing, which is really a generalization of what a pointer is. A pointer can point at something or it can be nil and point at nothing. The boost license was still being hashed out.

[00:39:57] **MARSHALL CLOW:** When I joined, it was [00:40:00] very much, this was, you know, the early two thousands were all. A time there was, there was a lot of consternation, a lot of confusion about open source licenses. There were, there were, um, people had fallen into the, into several camps. There were the BSD license people. There were the GPL license people.

[00:40:24] **MARSHALL CLOW:** Um, open source was really becoming a big deal. The [00:40:30] Boost people went on a long discussion. The people who were part of the Boost project went on a long discussion for quite a while before deciding that none of the existing licenses really had quite what they wanted. They hired a law firm to write up the Boost software license, which is very short, refreshingly short, it's like know two paragraphs, and it's much more similar to the BSD style licenses than the GPL licenses.

[00:40:58] **MARSHALL CLOW:** Um, they [00:41:00] wanted to make sure that it was. Able to be used in commercial products while the GPL license tried really hard to prevent that. It's been a few years since I looked at it, so I can't tell you off the top of my head why, you know, what the difference between the g, the boost license and the uh, BSD licenses or, or, and then there's of course there was also a lot of people who were just putting stuff in the public domains, says, I relinquish any rights to this, do whatever you want.[00:41:30] 

[00:41:30] **MARSHALL CLOW:** Um, and they didn't want to do that. It's been a pretty successful license. It, there are a lot of people who are use the Boost license who are not part of Boost. Like who? Um, not off the top of my head. I can't know. I just, every now and then I run across something that is not part of Boost and it says license under the Boost software license 1.0.

[00:41:48] **MARSHALL CLOW:** Okay. 'cause they like the license. If you're going to, if you're gonna put something out as open source, you have to pick a license. A lot of the places people will not use it if you do not have a [00:42:00] license and. The boost license is one of the licenses that's usually in the conversation. Yeah. Although I can't really talk to why it's, it wa became more successful than some of the other ones.

[00:42:15] **MARSHALL CLOW:** But, um, in spite of the fact that I spent a while in the open source group at Qualcomm, I've tried really hard to forget what I know about software licenses. 'cause we spent way too much time dealing with those. There's always that kind of different [00:42:30] views, um, users want basically, you know, as, as Gilbert says, we should ask our users what do they want better products for free.

[00:42:38] **MARSHALL CLOW:** But, um, basically the, the idea behind, you know, copyright and licensing stuff in the United States has been, you know, if you do not assert your copyrights in some way, they might as well not exist. And so the boost. You know, sticking a copyright and say, this is licensed under the boost license is a way of protecting your copyright.

[00:42:59] **MARSHALL CLOW:** When if they've come [00:43:00] back to drop off a a bin, take one away, take a full one away and bring back your copyright, is one thing. But, um, a lot of places, a lot of corporations, Qualcomm was one of them, would not use any open source if, if it didn't have some kind of license on it, stating what the responsibilities of the users are and what the, what the rights of the, um, of the, uh, authors hat are.

[00:43:26] **MARSHALL CLOW:** One of the things that the Boost license was, um, [00:43:30] was specific about, if I remember, which I haven't read it in a decade, so I, I could be wrong, was, um, the question of patents. Um, you know, do these use, does this use any patented technology? And it was like, not as far as we know. Um, that's a, that's a hard thing.

[00:43:49] **MARSHALL CLOW:** It, there was an awful lot of discussion. During while it was being developed and people had lots of different ideas and, and, um, I won't say [00:44:00] heated, but there was a lot of back and forth and back and forth and back and forth, but by the time it came, it was done. Everybody was like, okay, I can live with this.

[00:44:11] **MARSHALL CLOW:** It may not be what I want, but I can live with this. That's a story. How did I get to WG 21? Microsoft put on a C++ conference in 2011, and I can't even remember the name of the conference. It was three days of doing C++ in, in [00:44:30] Bellevue and or Redmond. And I pitched to my boss that these are, I showed him a list of speakers and it's like, these, these are my people.

[00:44:44] **MARSHALL CLOW:** I should go to it. You know, if I'd known about the, the call for papers, I might've pitched a talk. And he went away and looked at this and came back and told me that,

[00:44:57] **MARSHALL CLOW:** you know, it's not that much money, but we [00:45:00] don't have any money in the budget this quarter. And so no, not going, not going. So I started calling friends and saying, Hmm, can I like go on the cheap? Because admission was like 99 bucks and a plane ticket was not that much. The biggest expense was really the hotel room.

[00:45:17] **MARSHALL CLOW:** And I started calling friends of mine who were going to the conference and saying, Hey, you know, can I crash in your hotel room or something like that. And I didn't get any, um, [00:45:30] didn't get any joy from that, but three of them all said, you know, you should just go to the standard meeting. And so I went back to my boss and I said, you know, I started doing some calling around to people about is there any way I could attend this on the cheap, and so on and so forth.

[00:45:45] **MARSHALL CLOW:** And they all said, you should go to the standards. You should join the standards committee. And I didn't know this at the time, but he was an EX IETF member. So this was right in his wheelhouse. He was, he was [00:46:00] predisposed to, to like this idea. And we talked about this for like an hour and he was pretty, pretty favorable about this.

[00:46:07] **MARSHALL CLOW:** And he says, okay, yeah, I could see this. Let me go talk to people and see if we can figure out a way this. And it's like, when's the next standards meeting? I said, it's in two weeks, it's in Hawaii. And I'm thinking to myself, he just told me I couldn't go to WA to to Seattle for three days 'cause it was too expensive.

[00:46:27] **MARSHALL CLOW:** He didn't have any money. So instead I'm telling him, [00:46:30] I'm going, I want to go to Hawaii for a week. And he looked at me and he stood up and without a word, he walked outta my office. And I figured, okay. He'll come back and say, you know, well there'll be another then his meeting in four months, maybe we'll go to that one.

[00:46:46] **MARSHALL CLOW:** But the next day he walked in and said, okay, it's approved. You go, you know, make the arrangements and go a bunch of geeks. Oh, the, the, the follow up story about the conference in, uh, they live streamed the conference in [00:47:00] Seattle. And so I was watching the presentations live and of the first five presenters, four of them mentioned me by name in their presentations and I'm like, oh, I should have been there, but that's okay.

[00:47:14] **MARSHALL CLOW:** Um, so I show up to Kona. Yeah. There's, there's Herb Sutter and there's Bjarne Stroustrup, and there's, yeah. And there's Dave Abrahams and there's Beman Dawes and there's, um, yeah. Um, that's all Matt Austern and yeah, it's a whole [00:47:30] bunch of people who I've, who I've exchanged emails with or who've written books that I've bought, or there's PJ Plauger whose books I bought when I was in college for Kona.

[00:47:40] **MARSHALL CLOW:** It was, it's held at a hotel. It's a, there's a hotel there and there's meeting rooms at the hotel, and it's all right there. Well, okay, from the beach about a couple hundred yards from the water feet, but the, but right there where the hotel is, the water, the waves are breaking on lava, lava [00:48:00] rocks, sitting in a windowless room talking about C++.

[00:48:06] **MARSHALL CLOW:** I, um, the first day I'm sitting there in the, the plenary session and we're, there's like 60 guys sitting around the table with laptops. They're not all guys, but they're mostly guys and. We're in a windowless room. So I pull out my phone and I take a couple of pictures and I sent them off to my boss and says, nyner, nyner, nyner.

[00:48:27] **MARSHALL CLOW:** I'm in Hawaii, and you are not with this [00:48:30] picture of this windowless room. Um, did he appreciate that? Yes. He thought it was funny having been at two IETF meetings. He said, yeah, that's exactly how it goes. But, um, we sit around and you argue about C++ and you know, the first meeting I did an awful lot of listening and asking questions of people during the break and saying, well, I don't understand this, but why, about how about this?

[00:48:55] **MARSHALL CLOW:** Or why don't we do it this way? And people were quite, [00:49:00] um, gracious at saying, oh no, we tried that, it didn't work, or, no, we don't, we don't do things that way because of this and this and this, and so on. He was a convener for 20 years. He has, he has a lot of control when it comes to setting directions. As a convener.

[00:49:19] **MARSHALL CLOW:** He, uh, he has, um, he works with the, the working group chairs to kind of, you know, make sure everybody knows where we're [00:49:30] going and so on. And, um, he was the one who really pushed, he and other people, he was the public face of pushing to get a new C++ standard out every three years. Yeah, I mean, there were lots of other people doing this right.

[00:49:45] **MARSHALL CLOW:** But he was the public face of that because C++ 11 was really supposed to be three C++ oh 7, oh 8, oh 9, 10, 11. Um, but [00:50:00] people could kept coming up with new things and people would say, oh, well we could just slap this in. We'll just slip it one meeting. And one meeting at three times a year became four years at 12 meetings.

[00:50:13] **MARSHALL CLOW:** Um, you know what?

[00:50:18] **MARSHALL CLOW:** Three is probably the minimum you can do. But the thing is, is that if it was five years, it just means we'd take bigger steps and we'd still be weed. Weed. I'm not part of the committee anymore. The committee would still be as rushed at [00:50:30] the end. Okay. Yeah. The hardest thing that the committee has to do is say, Nope, this is not going in this time.

[00:50:38] **MARSHALL CLOW:** You know, that train is leaving the station and this is not ready. No, that's, that was one of the hardest things. He is responsible for picking the chairs. People. If you want to be a chair, you talk to the existing chair and the, and the existing chair makes recommendations and Herb picks them. When my time as chair was [00:51:00] up, um, I, I gave her, I, I mentioned that my time was coming up and I talked to a few people about being the next chair, and I gave Herb three recommendations and he picked one of 'em.

[00:51:13] **MARSHALL CLOW:** He picked Jonathan. I recommended Jonathan Wakeley and Jeff Garland and Dietmar Kühl. And in fact, what Herb chose was he chose Jonathan and the other two as assistant LWG chairs. The idea was to have [00:51:30] assistant to LWG chairs so that when Jonathan steps down, which if he continues the five year term, should be right about now that either Jeff or Dietmar will step up.

[00:51:44] **MARSHALL CLOW:** And so they've been, they've been participating in the chairing for five years.

[00:51:50] **RAY NOWOSIELSKI:** Who did you replace? 

[00:51:52] **MARSHALL CLOW:** Um, I replaced Alistair meredith. Herb came to me and asked me if I was willing to be the chair of the library working group. It's [00:52:00] one of the, there at the time there were four main working groups. There was five, four or five.

[00:52:07] **MARSHALL CLOW:** There was the. Evolution Working group at the time. There were three actually there. The Evolution Working Group, which works on evolving the language. There was the core working group, which controls the language. There was the library working group, which is all about the standard library. We've added the library Evolution working group since then, which is involved in, in evaluating new proposals, which will go into the library.

[00:52:28] **MARSHALL CLOW:** It's too much work. [00:52:30] There's too much work for one group to do. The library, the Library Evolution Working Group was created in about 2012. So, and I was, um, 2012, 2013, and I was LWG 12 from 2015 to 2020. So how did I get to be LWG Chair? I don't know. I suspect Alistair recommended me. Herb deserves. A lot of it.

[00:52:56] **MARSHALL CLOW:** Yes. But he's not the sole person. I mean, the entire [00:53:00] committee. I mean, he can, he can set a direction and say, I think we want to go this way. But it's all about who brings proposals and who champions them and, and how people react to the proposals. Um, he doesn't get to decide things for the committee. He, he might, he's, he's an administrator.

[00:53:19] **MARSHALL CLOW:** Okay. He also sits in EWG and, and argues for and against proposals. But as a convener, he is, he does a lot of administrative [00:53:30] stuff and he, he tries to keep things moving and as I said, he set the, the schedule for like every three years. Yeah. Um, he deserves a lot of praise ultimately him. Yes, he does. But at the same time.

[00:53:46] **MARSHALL CLOW:** At least when I was chair, I, he did not actually come to me and say, Hey, I really want you to do this, or anything like that, even indirectly, you know, he and I, he came in, sat in LWG and, and talked [00:54:00] about proposals while I was chairing, but we didn't have many of the, the, we didn't have like one-on-one conversations where it's like, no, no, you really need to do this, or something like that.

[00:54:10] **MARSHALL CLOW:** So here's the thing. Microsoft sends people the standards group. Google sends people to the standards meetings. They propose libraries that they've worked on that they think are suitable for standardizations. They champion them. They, they talk them up, they write papers. Um, so yes, that [00:54:30] happens. That libraries that came out of Google or Microsoft or Oracle or wherever, or you know, or language features that were pioneered as part of GCC.

[00:54:44] **MARSHALL CLOW:** Do end up in the standard because the people who have written them write pri write papers and make proposals and come and champion them at standards meetings. Yes, that happens. Um, is this some secretive kind of underhanded thing? [00:55:00] No, it's very, very, it's very, very open and it's like, hi, we have this thing here.

[00:55:07] **MARSHALL CLOW:** Um, you know, Google has their ab sale libraries. They have proposed several of their ab sale libraries for standardization. Several of the, the pieces of ABS sale, um, the whole Flat Map thing came out of Google. Zach [ Laine] did, no, Zach did the boost implementation of [00:55:30] Flat Map and flat set. Um, but no, the, the people who wrote the papers were.

[00:55:36] **MARSHALL CLOW:** I'd have to go back and refresh my memory, but I believe they were mostly from Google. That doesn't make it bad. It just means, you know, you gotta know where, you know where they're coming from. And it's also, the good news is those kind of, those libraries tend to have implementation experience. 'cause they've used, you know, they've used them internally or they use them in their compiler or they ship them as part of [00:56:00] their additional libraries.

[00:56:01] **MARSHALL CLOW:** I would call it more, I, I wouldn't call it tools that they're exposed to, to entice folks. They have more resources. Yeah, they could, they could, they could put an entire team on working on their proposal. They could put in, they could put, they could ship their proposal as part of the additional libraries with the compiler so they can get a lot more users.

[00:56:20] **MARSHALL CLOW:** Yeah. Um, one way you, one way you say it sounds like it's kind of underhand and other way say it is like, yes, [00:56:30] big companies have more resources, um. Fair. Bloomberg sends, Bloomberg has their own implementation of the standard library, and they do experiments in that, and they write papers based on what they found, and they send a dozen people to the, um, to the standards committee meetings, to the, they write lots of papers.

[00:56:55] **MARSHALL CLOW:** Um, Alistair writes, uh, 10 papers for [00:57:00] every, every mailing. Um, trying to get things changed is Christopher Kohlhoff. Christopher is a guy who lives in Australia, who is a consultant who does a lot of stuff for financial companies. Um, he writes libraries and software for, you know, traders who for whom, you know, networking and low latency [00:57:30] and so on is, um, is p.

[00:57:33] **MARSHALL CLOW:** By the way that is in, that is a big constituency in the C++ community is financial traders, financial, um, financial, you know, banks and trading companies and insurance companies and so on. And those people are obsessed with performance. These are the people who, you know, [00:58:00] lease space from the, from, you know, from NASDAQ so that they can put their data center in the same building as the exchange so they can cut down on transmission delays for speed of light.

[00:58:18] **MARSHALL CLOW:** That you could be two floors away instead of three miles away, as opposed to 20 miles away. As opposed to if you're in Chicago a thousand miles away. That's, um. [00:58:30] That's a competitive advantage when you're, you're trying to get rid of latency and these people are deeply, deeply interested in these kind of things.

[00:58:41] **MARSHALL CLOW:** Um, anyway, Chris, why is networking controversial? Network networking is controversial because C++ doesn't have it. So as Chris went off and, and built this library called AEO that does networking and it, it's high performance and it's been out there for a [00:59:00] long time. He's been using it and other people have been using it and it's been part of Boost for several years.

[00:59:07] **MARSHALL CLOW:** And, um, people proposed standardizing it and putting it in the sta into the standard library, making it available. Uh, and there was in fact a networking ts and we spent a reasonable amount of time on it. But there were a lot of people that said, this is not the architecture we want. This is not the [00:59:30] architecture that, you know, this is not the way we write C++ today.

[00:59:33] **MARSHALL CLOW:** This is how we did it five or six years ago, bef back before we knew better. Hmm. And we don't want to standardize this because it's kind of backwards looking. Not that it's a, it's a poor design, it's just this is not how we do things now. And we do some, we would do things more generically. And so I can see the attraction to that.

[00:59:58] **MARSHALL CLOW:** But at the same time, [01:00:00] um, if you're going to be standardizing existing, uh, practice, you're going to be standardizing something that's been out there for several years. You know, if you start right now and write a new networking library and then go out and use it for several years and then try to put it in the standard library.

[01:00:21] **MARSHALL CLOW:** People will say exact same things. Well, we don't write C++ like that anymore. That's how we did it five or six years ago. And so [01:00:30] it's kind of a, it's kind of a hard place. It's, it's not a, there's not a, there's easy solution there. Um, Chris came to a couple of standards meetings. It was hard to him when, for him, when he's in Australia, it was not well received and I wasn't a part of those discussions, so I can't really say why he was discouraged at, at the end of them, he was discouraged, he was feeling discouraged as opposed to he [01:01:00] was discouraged from going farther.

[01:01:02] **MARSHALL CLOW:** Uh, he was discouraged and feeling discouraged and now it's six or seven years later and we still don't have networking in the standard library, which is unfortunate. One of the things that I really like about writing code in Python is that we have a, a whole set of networking libraries for doing things.

[01:01:20] **MARSHALL CLOW:** I don't believe there's a simple answer to that that involves the standards committee. No. There are enough people on the standards committee who have differing view differing views of how things should work. Maybe [01:01:30] something will come out for C++ 29. I don't know. That is, that is all my experience on that was back in the 2017 timeframe.

[01:01:38] **MARSHALL CLOW:** So that's, that's a long time ago. I'm kind of, of the opinion that, that the C++ would have been better off adopting Asio because then we would have s some, some networking built into all, all of the, all of the, into the standard library as opposed to nothing. That wasn't what other people said.

[01:01:56] **MARSHALL CLOW:** And what the thing is, is that most of these discussions went on [01:02:00] in the, um, in the Library Evolution working group. It started off being Jeffrey Askin. But after that, I don't remember. So I was not actually part of those, most of those discussions because as the chair of, I was in the room in LWG all the time, I was running LWG.

[01:02:14] **MARSHALL CLOW:** So I did not get out to go into the other groups hardly at all for like five years. So I have a very narrow view of what happened during the standards, uh, meetings for those, for the five years where I was, um, I was chair, my [01:02:30] opinion is most of the really low hanging fruit, the very popular libraries for, um, from Boost were picked up and put in the standard for C++ 11 variant and optional.

[01:02:41] **MARSHALL CLOW:** And there's a third one that I'm forgetting. Were not, and they were added for C++ 17. But a lot of the value of Boost the, A lot, I don't wanna say a lot of the value, a lot of the very mainstream value of Boost, the things that people were clear, oh yeah, this is, stuff is missing [01:03:00] from the, um. From the standard library, like smart pointers and hashing and unordered containers and so on were picked up and dropped in for C++ 11 and Boost became when that happened, and C++ 11 implementations started appearing Boost became much less of a, well, [01:03:30] duh, of course you need it.

[01:03:31] **MARSHALL CLOW:** Boost. Started doing a bunch of other things, which were good, which were interesting, which were inventive, but they weren't as widely applicable in my opinion. Okay. There was less of an attempt to promote stuff as it were. You know, take stuff from boosts and make it part of the standard library in C++ 14, and then C++ [01:04:00] 17 some.

[01:04:01] **MARSHALL CLOW:** Although we did get Variant and Optional and Beman did Boost File System and yeah, that was a huge library. And you know, everybody, that was one of these things that was obviously a whole, um, people wanted a C++ interface to the file system better than the C the C++ and Beman provided it and did a really nice job of it.

[01:04:28] **MARSHALL CLOW:** And then he and some other [01:04:30] people sat down and wrote proposals and wrote wording. And we spent a long time working on the wording. 'cause file systems are hard things. Files, file systems are full of edge cases. You know what happens when you try to create in a, create a file in a folder where you have right permissions but not read permissions.

[01:04:53] **MARSHALL CLOW:** Um, you can create a file, you can, and then you can write to it and you can close it, but then you can't open it again [01:05:00] for eating. Um, or you, maybe you don't have execute permissions, you can't even see that it's there. There's all sorts of weird error cases and different file systems have different permission models and so on.

[01:05:13] **MARSHALL CLOW:** And so, um, that was, that was very much a, um, a great big hole and that went in for C++ 17. Actually, the last library that Beman I talked to Beman about that he was working on was a B [01:05:30] Tree library. And he came and gave a talk at, I think the last BoostCon he was at, about the thing he was doing with it.

[01:05:37] **MARSHALL CLOW:** And this was something he had developed an earlier version for, for his consulting work where he was doing GIS systems. Before GIS systems were a thing. The, um, the file system byway was a big deal and it was a, it was, it was a strain for the, um, the committee to accept it just because it was so big. Hm.

[01:05:59] **MARSHALL CLOW:** Um, I would've been [01:06:00] very happy to take it in chunks, but I couldn't figure out any way to, to, to break it. He was, he was happy. It was a lot of work on his part and a lot of other people, but it was a lot of work on his part, and he was happy to see it go in because, you know, it was going to help a lot of people.

[01:06:17] **MARSHALL CLOW:** How did you learn that Beman had passed? There was an announcement at a committee meeting, sadness, a couple people cried. We all had a moment of silence. A lot of people wrote, uh, wrote letters to his wife, [01:06:30] sent cards to his wife. Um, I had never, I had never met his wife. Far as I know. She's a very, she's a lovely woman.

[01:06:36] **MARSHALL CLOW:** Everybody tells me she's, I have no reason to doubt it. But yeah, Beman was a great guy. Um, Dave Abrahams got hired by, uh, by Apple to work on Swift, to work on the, the standard library for Swift, and he, so he disappeared inside Apple for. Probably five years. Um, and apparently working on a different, uh, standard library with different, um, [01:07:00] different sets of tools and constraints and goals, opened his eyes to, um, to a, to different approaches to things.

[01:07:10] **MARSHALL CLOW:** But last I heard he was working for Sean at Adobe in Sean's advanced, um, whatever he's calling it now. His, his team. But he's, yeah, he spent five years at Apple, I think maybe six. And, um, and so once you're, if you're, if you're working on stuff inside Apple, that Apple hasn't released, nobody [01:07:30] hears from you because you can't talk about any of it.

[01:07:33] **MARSHALL CLOW:** Well, we'll always miss them Sure. If they're not around. But there are a lot of, there are people who are leading the Boost project and providing a lot of guidance and helping new people along. I mean, Peter Dimov leaps to mind. Um. He's doing a lot. Some of the people at the Alliance are, um, you know, providing new libraries and helping mentoring [01:08:00] people.

[01:08:00] **MARSHALL CLOW:** Peter seems to be everywhere these days commenting on all sorts of things. That's a really good question. Peter's this guy who lives in Southern Europe and as far as I can tell, doesn't travel and far as I know, doesn't sleep and sits there and writes code and reviews other people's things and answers emails and is, um, is write a surprisingly amount, amount of the time.

[01:08:28] **MARSHALL CLOW:** My last [01:08:30] plenary Okay. Was where? Prague? It was Prague. It was, my last plenary was in Prague. It was February of 2020. We were voting out C++ 20. Um. I had left the C++ alliance a couple months before, so I was unemployed. I was pretty sure this was going to be my last standards meeting 'cause I'm not, I was not going to, [01:09:00] um, I was unwilling to, shall we say, self-fund, um, traveling all over the world to do C++ standards work.

[01:09:06] **MARSHALL CLOW:** And frankly, I was kind of burnt out. Five years is a long time to be a chair. And so this was the end of my WG21 term as LWG chair. And I had picked out three people to succeed me and, um, Herb had chosen Jonathan. Um, but we went through and we, we just ratcheted through a whole bunch of stuff. That was the very last minute to [01:09:30] see how much stuff was ready for C++ 20.

[01:09:33] **MARSHALL CLOW:** And we voted it all through and I announced that I was stepping down and got a nice round of applause and a lot of people came up and shook my hand. And you a 

[01:09:42] **RAY NOWOSIELSKI:** standing ovation, didn't you? 

[01:09:43] **MARSHALL CLOW:** I did, I did get a standing ovation. Um, five years is, was is the traditional term for LWG chairs. Matt Austern had five years and Beman did five years, and um, Alistair did five years and I'm remember, I'm trying to remember who [01:10:00] was the very first LWG chair?

[01:10:02] **MARSHALL CLOW:** No, it was before Beman. Um, one of the old times C++ guys, but I just can't remember if you tell me his name, I'll say, oh yeah. Him, like, I was standing Ovation and Jonathan stood up and said hi. And um, and then came home. Big storm rolled into, um, rolled into England as I was changing planes and Heathrow and I had to spend the night in Heathrow to go home.

[01:10:26] **MARSHALL CLOW:** And that was Valentine's Day two, th [01:10:30] 2020. And they had a new security question for everybody as you were boarding the plane. 'cause this was the start of COVID. And the question was, have you been in China in the last 10 days? I said No. And they said, get on the plane. I was grateful. I was, I, 'cause you know, it's a lot of work and you, you sit in that room and you sometimes get the feeling that people take you for granted.

[01:10:58] **MARSHALL CLOW:** But the standing ovation was great. [01:11:00] Everybody stood up and, uh, made it clear that they appreciated all the work I'd done. And people came up and said, thank you, and shook my hand and bought me beers. And it was, it was a nice feeling. What makes a good library? Wow. It's easy to use. It's general and it's extensible and it's hard to use.

[01:11:21] **MARSHALL CLOW:** Wrong. Um, you go back to Liscow's open closed principle, which I'm not going to explain because that will take too long, but it's [01:11:30] basically, you know, open to extension, flexible, you know, um, for, for the standard library. It's like we, we, we lean really hard into generic, usable in many contexts. Go back to Vector.

[01:11:42] **MARSHALL CLOW:** 'cause Vector is kind of the poster child for the standard library, right? It has a few, few knobs that you can twist. Not very many allocation strategies, basically, um, allocators. But, um, you know, you can use it to hold order sequences of [01:12:00] just about anything. And a lot of people understand how it works or how it works from the outside.

[01:12:05] **MARSHALL CLOW:** And so it's, it's like a go-to tool for everybody and that, that's why it's a good library. Um, if you ask, I need a container to hold stuff, which container should I use? Vector? If that doesn't work, then map or list. If those aren't work for you, then okay, now you're, you're, you're in in the 1% range. Well, [01:12:30] yeah.

[01:12:30] **MARSHALL CLOW:** Look at, look at the rest of them. And if they don't work, yeah, invent your own. 'cause Vector is like 90% of the time. The C++ Alliance is, uh, was founded by Vinny Falco and some other people to promote the creation and publish publication of C++ libraries. A lot of this is, you know, the kind of thing that Boost was set up to do.

[01:12:56] **MARSHALL CLOW:** And, um, Vinnie wanted to do this in the [01:13:00] context of Boost. Vinnie had financial resources to do this, and so he set things up and he hired a few people. The person he wanted to hire at first was Chris Kohlhoff to work on networking, but Chris had his own consulting clients in the financial industry and so he, he said, I, I need to keep my existing clients happy.

[01:13:18] **MARSHALL CLOW:** I had just gotten, I was in the process of being laid off from Qualcomm. Qualcomm was going through a round of layoffs, and so Vinny reached out to me and said, we'd like to hire you to keep doing the things you're doing, which is [01:13:30] work on Boost, work on Lib C++. And continue to do standards work.

[01:13:35] **MARSHALL CLOW:** And I said, okay, I can do that. He was gonna pay me to do it instead of Qualcomm paying me to do it. Um, he thought it had value. He, he thought I was providing, you know, helping things along. He didn't wanna see it stop. Um, which is good because otherwise I would've had to go find, either do it on my own without getting paid or go find somebody else to work for, which may or may not have led led to me continuing doing these things.

[01:13:59] **MARSHALL CLOW:** So [01:14:00] it was, it was a nice fit for me for two years. I basically, you know, kept doing the things I was doing at Qualcomm without the large company overhead stuff that was part of Qualcomm. That is really, that's very much our question for Vinny, that your question is, what, what is the vision? What should the vision of the C++ Alliance be, and how should it be doing that with Boost?

[01:14:24] **MARSHALL CLOW:** I, I'm not gonna put words in their mouth. Okay. I enjoyed my time working there. Um. [01:14:30] I hope they feel, hope that Vinnie feels that he got value for his money. He's doing a lot of stuff to improve Boost, to make Boost more active. Boost kind of fell into a doldrums in the post C++ 11 era because a lot of their reason for existence had been subsumed into the standard library and it took them a while to recover from that.

[01:14:56] **MARSHALL CLOW:** Or while being several years, Vinnie has helped a lot [01:15:00] by getting people to propose libraries, funding people in many cases for, for libraries that are not quite suitable for standardization, like, um, well, Beast, I don't think we'll ever get standardized. URL might. JSON might, the Readis Library, I don't think ever will, you know, there's a lot of very, very useful libraries that the C++ Alliance has supported and, and has championed that.

[01:15:29] **MARSHALL CLOW:** I don't think we'll ever [01:15:30] get into the standard library and that's fine. Not all the libraries and booths need to go into the standard library. I'm feeling more confident about the future of Boost today than I was say, eight or nine years ago. I think that Boost has picked up some new people, picked up some, some new enthusiasm as opposed to just, you know, going through the motions of putting out a new release of the same old library with libraries, with minor, with minor tweaks or minor updates.

[01:15:59] **MARSHALL CLOW:** [01:16:00] Now there's people who are doing different things, exciting things. Um, I wonder what people are going to do with. The reflection capabilities that are coming in C++ 26. I suspect that people will find amazing things to do with that, both inside of Boost and outside of Boost. Um, so we'll see. Um, it's an interesting time to be part of C++ and I hope that [01:16:30] Boost continues to, um, point out, you know, to point out interesting directions. 

