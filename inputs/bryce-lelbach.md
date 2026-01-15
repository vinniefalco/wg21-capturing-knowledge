# BOOST_BRYCE_LELBACH_STRINGOUT_v01

- - - -
filmed Date: 2025-10-24  
location: New York City, NY  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1141544290/9d6d3d6e9d?fl=pl&fe=sh  
summary: Stand out interview - Just great character, shot well, excellent talking modern Boost era and WG21 library; acolyte of Hartmut Kaiser and Boost devotee from young age, talked frankly about WG21 issues, his run for convenership, diff Library WG21 leaders and their strengths, went through each Boost library rejected from standard during his tenure and others he knew about; has given up on Boost for the future - “it had its moment, and it made a huge impact, on C++ 11 etc, and that's enough”  

- - - - 

## Transcript Start


[00:00:00] **RAY NOWOSIELSKI:** He likes to make new friends and, alright, 

[00:00:04] **BRYCE LELBACH:** so my name's Bryce Adelstein, ak, uh, I'm a principal engineer at Nvidia, uh, where I work on programming, language design and evolution. So I founded the cuda com core compute, uh, libraries, uh, team here. Now I lead the Vanguard Programming Group and our job is to figure out how to make every major programming language a GPU programming language.

[00:00:28] **BRYCE LELBACH:** And, uh, my [00:00:30] connection to boost, uh, boost sort of launched my career. So, uh, I got my first job through Boost. Um, I got started programming really through Boost. Um, and almost all of my early connections in the industry were through, uh, through Boost and through the Boost Community. That's a funny story. So, uh, I used to play lots of like, online multiplayer games and I don't even remember the game, uh, but it was some.

[00:00:59] **BRYCE LELBACH:** Game [00:01:00] involving, uh, like everybody, like spaceships, um, and, uh, like interstellar war. And, um, uh, I was part of a clan and it was themed for the TV show Firefly. Um, and I eventually became one of the clan leaders and all the Klan leaders had a username of one of the major characters from Firefly, and Wash was the one remaining free name.

[00:01:24] **BRYCE LELBACH:** So it was not like by choice, it was just like, all right, this is what's available. And so I just used that as a handle for, [00:01:30] uh, for many years. Uh, it's still my login on, uh, some of my, some of my systems. Yeah. Uh, I mean, it's always been one of my favorite TV shows. Um, uh, I guess I've been at many times some form of Revel and, uh, I don't know how many times I've been on the losing side of things, but, uh, I feel like it's sort of evened out over the years.

[00:01:52] **BRYCE LELBACH:** Um, I, I feel like Boost has been, uh. A very important part of my career. As I said, sort of, I [00:02:00] got started in the Boost Community. Um, and I think that the Boost community has not, not only helped me start my career, but there's also like a whole generation of programmers about my age who got started through the Boost community, through C++ now, and through the C++ now as a student program.

[00:02:20] **BRYCE LELBACH:** Um, and when I first got started in the Boost community, um, I always felt like whatever room I was in there were like, everybody was 10 to 15 years [00:02:30] older than me. Um, and then over time, um, more and more young people like me sort of found their way to the community and, and, uh, I feel like there's this whole generation of C++ leadership that sort of got started there.

[00:02:44] **BRYCE LELBACH:** Um, so I mean, I, I feel like it's a, a story worth knowing. Mm-hmm. Um, uh, you know, it's boost obviously, I think today does not. Play the role that it, it once did. Um, but, [00:03:00] uh, I think Boost, the Boost Project largely sort of saved C++, kept C++ alive during its long winter period. Um, and for a long time it was really the only developer community for C++.

[00:03:15] **BRYCE LELBACH:** Um, you know, back in the two thousands, early 2000 tens, there was really only one C++ conference. Um, uh, before C PPP Con, it was really just C++. [00:03:30] Now that was, you know, part of Boost. Um, and, uh, in the, before the current era of software development, before sort of the GitHub era, uh, if you needed to go get high quality libraries, like you, you, you went to Boost.

[00:03:47] **BRYCE LELBACH:** Like, that was, that was sort of the defactor place that people went when they needed to then a third party library. Um, so maybe we can start with how I. First, uh, uh, like became [00:04:00] connected to Boost. Um, so when I was in college the first time around, um, I was at Union College in upstate New York. And, uh, I was very bored with school and I had wanted to, uh, make my own mud, which is a mud.

[00:04:16] **BRYCE LELBACH:** So these text-based, uh, multiplayer games. Um, and, uh, I didn't know how to code at the time. I was talking to somebody who ran their own mud and they said like, look, if you wanna do this, you don't necessarily have to do all the coding, [00:04:30] but you need to, you need to be able to, you need to be capable of doing it.

[00:04:33] **BRYCE LELBACH:** Like if you're gonna, if you're gonna build a team to do this. Um, and so I started learning how to program and uh, that very quickly sort of consumed all my time and I stopped going to classes and, uh, I was working with this one other developer, um, and we were writing this mud and C++. And, uh, he, uh, started using the Boost Libraries in this project.

[00:04:56] **BRYCE LELBACH:** And, um, I was like, oh, what's this thing? And he told me more about it. [00:05:00] And, um, I remember my first patch was we were using something from Boost String Algos. Um, and, uh, there was some bug and I was offended by the existence of the bug. And so I went and figured out how to, uh, go, you know, fix it. Um, and I joined the Boost, uh, IRC, uh, which was, I don't know what the, I guess IRC was like social media before social media.

[00:05:26] **BRYCE LELBACH:** It was like a chat server. Um, and so I, I [00:05:30] became fairly active on there because I was sort of used to IRC communities from my gaming days. Um, and, uh, I, I very quickly sort of lost interest in the game project and just started working on Boost. Um, and, uh, I mean, I was in college. I wasn't going to classes.

[00:05:47] **BRYCE LELBACH:** Uh, and I just, this. It was sort of the thing I did all day, every day. Um, and I met people through there and the first person who I met was, uh, Hartmut Kaiser, [00:06:00] um, who I didn't know anything about him at the time. He was just really a handle on an IRC channel. Um, but, uh, he helped mentor me, um, and I, I started contributing to the library that he was working on Boost Spirit, um, in addition to some other libraries.

[00:06:18] **BRYCE LELBACH:** And he, he sort of helped shepherd my early developments, um, suggested that I be the release manager for one particular version of Boost Spirit. Um, and [00:06:30] then at some point, uh, the, uh, the, the college I was at kicked me out because they're like, well, you're not showing up to classes. I technically didn't drop out of college.

[00:06:39] **BRYCE LELBACH:** I was kicked out of college because I was too stubborn to drop out. And so then I moved back with my parents who were, were not happy about any of this. Um, and they, they wanted me to get a job, uh, because all I was doing as far as they could see was just sitting on my computer, messing around all day. Um, and they suggested I like, go get a job at Starbucks or something.[00:07:00] 

[00:07:00] **BRYCE LELBACH:** And, um, so I started looking for places that would employ me. Uh, and I did that primarily through the people I knew on this Boost, IRC uh, uh, community. And, um, I found one contract job with a compiler company called Path Scale, trying to get their compiler to, uh, pass more of the Boost Test Suite. Um, and, uh, I got some money for that, but that was like a month or two.

[00:07:28] **BRYCE LELBACH:** And then I, I [00:07:30] asked Hartman, um, I was like, Hey, I need a job. And he tells me, well, why don't you come down to Louisiana State University and, uh, come work for me? And I, I knew nothing about Hartman at the time, other than that he was another, you know. A developer and that he'd been, you know, teaching me, but I didn't even know his real name.

[00:07:52] **BRYCE LELBACH:** I didn't know what he did. Um, but I was like, sure, done. I'll do it. And um, I then had to convince my parents [00:08:00] to, uh, uh, like, you know, that I was gonna buy a one-way plane ticket to Louisiana and the, to like, support me in doing that. 

[00:08:07] **RAY NOWOSIELSKI:** How did you, how did you bring that to him? 

[00:08:10] **BRYCE LELBACH:** Uh, pr I pretty much just said, Hey, you know, I, I met this guy on a chat room on the internet in Louisiana, um, and he wants me to come work for him.

[00:08:20] **BRYCE LELBACH:** Um, they of course thought he was an ax murderer or something, but he turned out to be this, you know, very nice, uh, German professor, uh, down there. [00:08:30] And, um, and I did in fact buy a one-way plane ticket, went down to LSU and uh, I joined him at his, uh, research lab and I was, uh, developer number two or three on the project he was working on, which is.

[00:08:45] **BRYCE LELBACH:** Um, library called HPX. It was built on top of Boost. Um, it was a distributed programming framework for, um, uh, high performance computing, uh, software. Um, and, uh, and so I, [00:09:00] I was there. I must have gone there and like March or April of 2010. Um, and this was a couple months before what at the time was, um, BusCon.

[00:09:14] **BRYCE LELBACH:** Um, and he suggested that I go give a talk at BusCon. Um, which, uh, which I did. Um, and I remember that was the first conference talk I ever gave, and it was not [00:09:30] good. There were a bunch of really bad Star Wars jokes, if I recall. And I remember, I, I stayed up until 4:00 AM the night before finishing my slides, and the talk was at like 8:00 AM so I had like no sleep.

[00:09:40] **BRYCE LELBACH:** I mean, it, it's, I think giving. Talks at conferences, like presenting technical ideas in a one hour lecture format is probably the, the thing I'm best at. Um, that's a, I mean, I probably give like 50 talks a year or something like that. Um, [00:10:00] and it's, it's at a point now where like I have a process for it and, uh, it's like not nervous for me.

[00:10:06] **BRYCE LELBACH:** Like if, so, if, if I needed to go give a talk right now, like I could, I got, I got like 20 of 'em I could give just on the spot. But, um, but in those early days, like, yeah, it's terrifying. Um, it's terrifying and, and you get up on stage and, uh, you choke up a little bit. And what, what does it mean? Um,

[00:10:28] **BRYCE LELBACH:** you know, [00:10:30] for me, um, as somebody who was a college dropout who didn't have any credentials, the first four years of my career, um, this was the only way to gain credentials. Um, and you know, you hear a lot about college dropouts in tech. You know, like all these billionaire founders, you know, a good chunk of 'em are college dropouts.

[00:10:57] **BRYCE LELBACH:** Uh, and so you think like there's some all Lord [00:11:00] to it and like, you know, oh, like doors are still open to you. But the reality is that if you don't have a college degree, um, uh, you, you can be successful in this industry, but it is a much harder path. Um, and the big, the biggest problem is that you don't have credentials.

[00:11:18] **BRYCE LELBACH:** And, uh, there's a lot of institutions, uh, which sort of require and expect them. And for me, somebody who was working in academia at the time with Hartman at [00:11:30] LSU, um, there's a lot of doors that have not opened to you if you don't have, if you're not a, uh, uh, somebody with a master's degree or a PhD or in a program.

[00:11:41] **BRYCE LELBACH:** One of those degrees. And so giving toxic conferences was one of the ways that I could, um, uh, build up a reputation for myself. And, um, you know, it's one of the best ways to, uh, connect with people who might use your software, [00:12:00] um, and spread the word about your software and connect with like-minded individuals, find collaborators, um, you know, find, find jobs, et cetera.

[00:12:08] **BRYCE LELBACH:** Yeah, exactly. For those who don't understand that, that's certainly true within the tech community, that solely within the tech world, in the world of software engineering, you know, um, it, it can be sufficient to just right, create software. Um, but for me, I was not in the software engineering world at the time.

[00:12:29] **BRYCE LELBACH:** I was [00:12:30] in the academic research world, uh, the, the high performance computing world. And, um, so that. That world expects you to, expected you to have a PhD to publish papers. Um, and you know, for someone, for example, somebody who's, um, not a US citizen, um, uh, or does not, uh, have a passport, that's particularly powerful.

[00:12:56] **BRYCE LELBACH:** Um, not having credentials can close a lot of doors to you. I, one [00:13:00] of the students I mentor, um, uh, Bassett, who now works at my company, um, he, uh, was from Nigeria and it was very difficult for him to, uh, get a visa to another country to go work as a software engineer somewhere that was not Nigeria. He had a prolific portfolio of open source contributions, all of which held very little value in the eyes of, you know, uh, uh, uh, a visa, [00:13:30] uh, officer at, you know, in the UK or the us right?

[00:13:33] **BRYCE LELBACH:** You needed to have. Uh, uh, credentials and speaking at conferences is something that's more understood than putting software somewhere on the web, um, uh, by the world outside of the tech community. And so I, so I think it wasn't just the talk that I gave, which I, they think was well achieved. It was, it was about this thing, yew Tree, um, uh, uh, which I'm sure no longer exists in Boost Spirit.

[00:13:59] **BRYCE LELBACH:** [00:14:00] Um, but it, it was just the conference itself. You know, I met people at that first Boost Con, who I've known my entire career connections that, um, have been sort of integral to my professional network. Um, there's actually, there's a funny story about that. I met, one of the people I met was Marshall Cloud, who I met at, um, at Boost Con.

[00:14:22] **BRYCE LELBACH:** And then I also worked on this project, LLVM Linux, at the time where I started, I started this effort to compile the Linux kernel with clang and [00:14:30] LLVM. And so I went to speak at some Linux event like two or three weeks after BusCon and Marshall was there too. And I just thought, oh, this guy's just at every conference, he's just, he's just got, I've been to two conferences.

[00:14:43] **BRYCE LELBACH:** He's been at both of 'em. They were on very different topics. He's just, he's just gotta be everywhere. Um, but you know, Marshall is somebody I've known my entire career. Um, people like Zach Lang, Dave Abrahams, Eric Ebler, um, uh, you know, all of my oldest professional [00:15:00] contacts are people that I met at that conference.

[00:15:02] **BRYCE LELBACH:** Um. And, uh, 

[00:15:04] **RAY NOWOSIELSKI:** these conferences? 

[00:15:05] **BRYCE LELBACH:** No, I mean, I think, I think it's true that some people communicate differently online than they do in person. And, um, you know, some, some people, uh, write like really angry emails, but then like you meet 'em in person and they're just the nicest person ever. Um, so I think there's something to be said for the in-person collaboration and for, for [00:15:30] Boost Con and then eventually C++.

[00:15:31] **BRYCE LELBACH:** Now, um, you're, it's 150 person conference. You're in Aspen in the off season. Nobody else is there. There's like three restaurants that are open. Um, and so it's a very collaborative environment. So you're, it reminds me a bit of the, the C++, um, uh, committee meetings, um, where everybody's basically locked in a room for a week.

[00:15:52] **BRYCE LELBACH:** Um, and it's very inspiring. I mean, you go and you, you get all excited about these ideas and you're like, oh yeah, we'll go build this thing. And it never ends up getting built. [00:16:00] But, uh, there's, there's lots of excitement. Um. And, uh, at least in those first few years, I feel like I learned a ton. Um, uh, like every conference I went to, um, uh, you know, I just got so much out of the talks.

[00:16:13] **BRYCE LELBACH:** Um, these days I get more out of just the, the hallway track. Um, uh, but, uh, that was a lot of my, like, early software education. I grew up, let's see, which way is, this is north. That means I grew up like, I don't know, 80 to a hundred [00:16:30] miles that way. Um, I grew up in Connecticut for the most part. I was born in Florida.

[00:16:34] **BRYCE LELBACH:** But, uh, when I was, uh, uh, about six or so, uh, my mom moved me up to Connecticut. Um, I was raised pretty much solely by my mom, uh, who is a single, single parent. Uh, she was a lawyer, uh, and an economist. Uh, she primarily did bankruptcy law and corporate litigation. So I have a lot of, uh, dinner table lectures about, uh.

[00:16:58] **BRYCE LELBACH:** Uh, free [00:17:00] market capitalism and, uh, you know, economic theory and trade policy. Um, and, uh, I, when I went to college, the first time I thought I was going to, my plan was to major in like political science before I sort of stepped into tech. Uh, for, for those who know me, that will not be surprising 'cause I'm something of a tech politician.

[00:17:22] **BRYCE LELBACH:** Um, but, but yeah, so I, I, I grew up in Connecticut in a town, uh, called West Hartford. Um, then later Simsbury when she [00:17:30] remarried. Um, and it was, you know, I was an only child with a single, single parent. Um, so it was just the two of us for a long time. No, you know, I, I often feel like I am, uh, there's a lot of people out there who are far better engineers than me and better coders than me.

[00:17:52] **BRYCE LELBACH:** Um, I feel like my strong suits always been. Um, the fact that I am a good communicator and [00:18:00] writer, and I feel like that's a relatively rare skill in the industry. And I also think that many people in the industry don't want to have to deal with the politics. Um, whereas I'm somebody who takes great joy in it, um, that I enjoy dealing with other people.

[00:18:21] **BRYCE LELBACH:** I enjoy figuring out how to get a group of people to work together, um, and to like reach some common ground [00:18:30] and consensus. And that's what I mean by like tech politics. Like tech politics is, um, how do we, how do we build consensus? How do we find common ground? How do we, you know, uh, uh, resolve disagreements, um, disagreements that are usually technical in nature.

[00:18:47] **BRYCE LELBACH:** But, um, I think everybody would like to think in an ideal world that. Uh, disagreements and, and, and, and, uh, uh, you know, uh, [00:19:00] strife in a technical project are always a hundred percent about technical facts. That's, that's not the reality. The reality is that sometimes it's that, you know, somebody feels like you're on their turf, like you've overstepped.

[00:19:15] **BRYCE LELBACH:** Like they weren't in the loop. They feel excluded, they feel left out. Um, and so they might, uh, be hostile to the, the technical change that you are suggesting because their feelings are hurt, [00:19:30] um, or because you did not, uh, show them respect. Um, and so being able to, uh, move past that, I think is really important.

[00:19:41] **BRYCE LELBACH:** And I think there's too few people in tech who ign, who acknowledge the human side. Of what we do. Like every, every industry, every field has, has politics, has interpersonal relationships, and we are an industry where people are like, oh no, it's all, it's all about the technology. It's all about the technology.

[00:19:59] **BRYCE LELBACH:** That should be the only thing that [00:20:00] matters. No feelings boosts value. Two, the tech industry was twofold. One, it had a technical component of it, um, uh, that it provided, um, uh, sort of a unique, so something unique for the C++ community during a dark time in C++'s history, like Boost, boost sort of thrived during a dark time for C++.

[00:20:22] **BRYCE LELBACH:** When C++ was on the decline and at risk of extinction and Boost provided sort of a lifeline. [00:20:30] Um, when people, today, I think it's hard to understand what it was like during that era. We didn't have GitHub. We didn't have, you know, uh, a. Reputable place to go to find high quality third party libraries.

[00:20:48] **BRYCE LELBACH:** Um, and, uh, it was, it was very hard to discover good third party libraries. And even if you did discover them, figure out how to, how to reliably like [00:21:00] import them and then, uh, uh, build them and use them. Um, and the, the value that Boost had was that it was this high quality collection of libraries. Um, and you, you could go and you could get boosts and then you'd have this, you know, a hundred, 150 libraries and maybe you wouldn't use all of them, but they would be there.

[00:21:20] **BRYCE LELBACH:** And like, you know, a lot of environments, people would just have boost be there. They would install it because they need some part of it, and then you'd have all the rest of it there available to use. [00:21:30] Um, and for developers today. If you needed software, you just go to GitHub, you just go and grab it. But before we had GitHub, that was like a really, really incredibly valuable.

[00:21:39] **BRYCE LELBACH:** Um, and additionally Boost filled a, uh, a lot of gaps in C++ the C++ standard library. Before C++ 11 was relatively sparse. It did not have, um, uh, threads Atomics, um, uh, [00:22:00] there were very few containers. Um, uh, there were a lot of other missing components. There was no file system, uh, library, um, like all these things that you'd, you'd need and that wouldn't be part of the standard library.

[00:22:13] **BRYCE LELBACH:** And it used to be everybody got 'em from Boost. And so that's on the technical part of what Boost provided. But during that dark period for C++, when C++ was in decline, um, you didn't have. A dozen C++ conferences like you do today, and you [00:22:30] had some C++ user groups. Um, but I think nowhere near like what you have today.

[00:22:36] **BRYCE LELBACH:** Um, and there were just not as many communities and Boost was sort of the focal point for the community. Um, there, there had been a few others over time, but Boost was really the central community during that period. Um, and uh, that, like, especially in that era, before social media, before we were all as connected as we [00:23:00] were today, that was the place to go to like meet people.

[00:23:03] **BRYCE LELBACH:** Oh yeah, definitely. So Boost is a victim of its own success. Um, so in C++ 11, uh, some of the most important and highest impact boost libraries were standardized. Um. Uh, things like, you know, shared, like everybody used to use Boost Shared Porter and Boost Thread, um, and Boost Atomics, like those are some of the most widely used Boost libraries.[00:23:30] 

[00:23:30] **BRYCE LELBACH:** Now those are all in the C++ standard, and all those libraries that were introduced in C++ 11, they were largely inspired by Boost. It used to be like that. I think most of the libraries in C++ 11, C++ 14, most of the major standard library additions were inspired by parts of Boost.

[00:23:48] **BRYCE LELBACH:** Um, uh, and it used to be that Boost was the proving ground for, you know, new additions to the C++ standard library. But then once the most widely used parts of Boost were put [00:24:00] into the standard, then people had a lot less motivation to have Boost installed in their development environment and ven it out to, to their, uh, like deployed with their libraries, with their, with their software.

[00:24:16] **BRYCE LELBACH:** Uh, by default because there, there was some cost to having to go and pull in boost and into your build and then ship boost libraries out to your users. Um, you know, boost was this big collection of libraries. Sometimes people would pull in piecemeal, but like there was a [00:24:30] cost to it. Um, and, and once the most valuable parts of Boost or in the standard, there was less of a motivation to have Boost available like 2011.

[00:24:41] **BRYCE LELBACH:** Anytime I was working on a software project, I would, I would definitely wanna have Boost as a dependency. Um, it'd be the first thing I'd set up. But by 20 18, 20 19, um, I would wanna write, if I was writing some new piece of software in C++, I would want, would wanna have no [00:25:00] dependencies if possible.

[00:25:01] **BRYCE LELBACH:** I certainly wouldn't wanna have Boost as a dependency. I'd be like, if I can write this with just pure standard C++, that'd be great. Um, and the other thing that changed is, uh, really GitHub. Um. It used to be that you'd put your library into Boost because it was a distribution channel. Um, it was a way to, like, if you got through the Boost review process, you got accepted into Boost, then you would pick up users because you would, you would be distributed with Boost everywhere.

[00:25:27] **BRYCE LELBACH:** Um, and people when, when [00:25:30] they were looking for libraries, they would go to boost.org, it would look, look at what libraries were available in Boost, and then they'd pick one of those and then, then GitHub, you know, sort of rose to prominence. Um, and then that became the place that people went to, to look for libraries.

[00:25:43] **BRYCE LELBACH:** Um, and you look at, I think really the most prominent example of this is, uh, Eric Neer's ranges. So, uh, range is famously one of the major features of C++ 20. Um, uh, one of the largest library editions [00:26:00] since C++ 11. And Eric LER largely designed it and wrote a reference implementation for it.

[00:26:07] **BRYCE LELBACH:** There were people who suggested, Hey, you should put this into Boost. He did not do that. Because by that time, the booster review process had gotten a bit slower, uh, because there were fewer people, um, involved, involved and around, and there was a lot less value to going through the booster review process.

[00:26:29] **BRYCE LELBACH:** [00:26:30] And it was a fairly high bar to clear that boost review process. And, um, it, it was gonna slow down the effort. And, and so I think Eric's philosophy was, I'm just going to, like, I don't need the boost review process. I'm just going to use the C++ standard of review process. It's the way of vetting this thing.

[00:26:49] **BRYCE LELBACH:** And so he just put his range of implementation on GitHub. Um, uh, and if it had been 10 years earlier, he definitely would've put it into Boost because there would've been no GitHub. But, um, [00:27:00] but yeah, I think that Boost, boost fulfilled its mission and was successful. Um, and. It is not as relevant today as it used to be, but there's nothing wrong with that because, again, boost fulfilled its mission.

[00:27:14] **BRYCE LELBACH:** Um, it, it helped make C++, uh, successful. Once again, like without Boost C++ would not have seen the resurgence that it saw P post C++ 11. Yeah, I, I, I, I think that the value that [00:27:30] Boost had was in the brand. Well, it had value in distribution. It had value in the brand association that Boost meant quality.

[00:27:39] **BRYCE LELBACH:** Um, and, uh, the distribution values now non-existent because everybody just puts their stuff on GitHub. Um, and the brand value, um, it's still there, but people have to pay the high cost of the boost review process and there's fewer reviewers around now. Um, [00:28:00] and C++ is a language, is, um. I, I certainly think it's, it's safe to say, uh, at risk of becoming a legacy, uh, language, uh, today.

[00:28:14] **BRYCE LELBACH:** Um, and so I think it is very hard to imagine boost regaining, uh, prominence. Um, but I, I think that's okay. It, it was, it was, it achieved its mission. [00:28:30] Um, and, and I think I, I personally am, uh, uh, like it's to some degree become a project maybe in search of a goal. Um, uh, and I, I think that, um, sometimes it's all right to just be like, we were successful wildly so I think more than anybody could have imagined.

[00:28:58] **BRYCE LELBACH:** Um, [00:29:00] but that there's no longer a need for what this was. Um, and maybe it becomes something else. Boost still has a valuable brand, um, uh, and maybe there are other ways in which the Boost Project can contribute. So there was a couple other aspects aside from just the review process and the brand that were valuable.

[00:29:21] **BRYCE LELBACH:** First of all, the libraries largely had the, um, the same code [00:29:30] style, um, and for the most part the same conventions. Um, and this is interesting because that was in no way, shape, or form enforced. One of the challenges that Boost had throughout its history is that Boost was never like a single project with a single direction.

[00:29:47] **BRYCE LELBACH:** It was always the, the library authors were always in control. Yes, you had to clear the review process. But one of, one of the challenges that Boost had is that once you [00:30:00] cleared the review process, the library's maintainer. Essentially had complete control and there was never any like recurring review process, right?

[00:30:09] **BRYCE LELBACH:** Once you were as accepted as a, as a boost library, there was never any like audit process, um, uh, that libraries largely had the freedom to make the decision that they wanted to. Um, that there was some attempts to impose sort of global, um, guide [00:30:30] like, uh, policy and, uh, you know, uh, there was a common build system.

[00:30:35] **BRYCE LELBACH:** Um, there were these common conventions, uh, but there was some amount of divergence between them. But for the most part, despite being, you know, a hundred different projects with a hundred different leaders who might have different opinions, um, they had a consistency to them that I think is rare to find in a collection of software of that scale.

[00:30:59] **BRYCE LELBACH:** [00:31:00] Um, uh. Uh, the consistency which Boost shares is greater than the consistency of software that I've seen within my own company or within, you know, other organizations that I've been involved in. Um, and I think that was because it was not something that was imposed on everyone. It was because the Boost maintainers largely agreed that these conventions were [00:31:30] the right thing to do, the right set of, uh, guidelines.

[00:31:34] **BRYCE LELBACH:** And also I think that everyone valued the consistency, valued the interoperability. So, yeah, go ahead. I don't know what the qualities were of somebody that would come to Boost. Um, I think that pretty much across the board, all the Boost maintainers, um, and contributors that I interacted with, with were, um.

[00:31:59] **BRYCE LELBACH:** The [00:32:00] best library designers, um, uh, the best interface designers that I've ever really encountered. Um, boost libraries. We'd be vented to such a wide audience, um, and, uh, uh, across so many platforms, uh, that almost every edge case would be exercised at some point. Um, uh, and so everybody had felt the pain of not carefully thinking through design.

[00:32:26] **BRYCE LELBACH:** Um, and I think sometimes [00:32:30] Boost is dinged for its complexity. Um, we certainly had our share of meta programming libraries and libraries that were, um, uh, like I think of Boost Spirit, which I worked on, or boost expressive or, um, uh, many of the various Boost Meta programming libraries. Some people see that and run for the Hills.

[00:32:53] **BRYCE LELBACH:** Um, but while some of these libraries were complex, I think that almost all of them. Were well [00:33:00] designed. Um, there were maybe a, a couple exceptions, but for the most part, in the cases where there were libraries where the design did not play out, eventually there would be a rollout of a new, you know, uh, uh, interface or a new version of the library entirely.

[00:33:15] **BRYCE LELBACH:** Um, and, uh, I think it, it takes a certain type of person to be able to design modular generic software that can be, uh, uh, [00:33:30] reused. I mean, it's the sort of person that thinks about, is this thing gonna stand the test of time? Is this gonna be there in 20, 30 years? It's not somebody who wants to do the quick and dirty thing.

[00:33:41] **BRYCE LELBACH:** It's somebody who wants to do the right thing. So maybe that's the trait that would hold. The Boost developer community together is that fundamentally everybody didn't wanna do the expedient thing. People wanted to do the right thing. And I think something like the boost review process, [00:34:00] uh, illustrates this, the boost review process, sometimes it would take a while.

[00:34:04] **BRYCE LELBACH:** Um, but that's because if something's gonna be in boost, we're gonna make sure that it's been thoroughly vetted and we're gonna think about all the possible edge cases and we're gonna make sure that this design can stand the test of time. It's been so long since I've been involved in, and I, I, I was not deeply involved in, uh, um, any real reviews that I can think of.

[00:34:27] **BRYCE LELBACH:** And I also never [00:34:30] submitted a library for the review process, so I haven't been through it, but I can give you. Uh, what I recall of the process. So first of all, you have to find a Boost Review Manager, um, which is some, I think the requirement was it had to be somebody who was the maintainer of a Boost Library, not necessarily somebody who had submitted a new library, but they needed to be somebody who was listed as a maintainer.

[00:34:55] **BRYCE LELBACH:** Um, or maybe later in the process it was just somebody who was one of the [00:35:00] OG Boost people. So you needed to find a boost review manager. Um, and then you would need to write up, um, some document that would basically describe what your library is and describe the design and sort of justify your design decisions.

[00:35:18] **BRYCE LELBACH:** It's actually very similar to what the C++ committee review process is, where you write a proposal and then it gets, you know, reviewed and pushed through. But there, there are some, there are some differences there. [00:35:30] Um, uh, and, and then ultimately the review was all based on. The mailing list. So, uh, the review manager would send out an email saying, we are beginning the review for this library.

[00:35:43] **BRYCE LELBACH:** Here is the library, here is the documentation, here is the description on what the library is. Um, and then some number of people would voluntarily decide to participate, um, in the review. And they would give their, uh, [00:36:00] feedback and their opinions. And, uh, you, the library submitter, uh, would have to, uh, address those.

[00:36:10] **BRYCE LELBACH:** Um, and sometimes that would mean, you know, trying to convince them that, no, actually we don't need to make this change and that this is fine. Or saying, okay, we fixed that. Um, and there wasn't really like a bar of like, uh, I, I, or I don't remember if there was like a bar where like you needed to have. A vote or [00:36:30] something.

[00:36:30] **BRYCE LELBACH:** I think it was more consensus driven, but you definitely needed to have some number of reviews. Um, and if you did not have enough people deciding to do the review, then you could not pass the review process. Um, so there would be some time window. You need to get some number of people to provide reviews.

[00:36:48] **BRYCE LELBACH:** Uh, some chunk of them would have to be positive, um, uh, and then you'd have to do this back and forth of talking with them, uh, uh, to address any [00:37:00] concerns. Was this painful for office? It was incredibly painful, especially later in boosts, uh, history when there were not so many people around who could be boost review managers.

[00:37:13] **BRYCE LELBACH:** Um, and there were also fewer people available as reviewers. Um, I think in the. Heydays a booster view, maybe in the best case, could take, you know, uh, three to six months. Um, but, uh, uh, [00:37:30] maybe even quicker than that. Um, you know, in like a, if the library is just perfect, if it was a short, simple thing, maybe, maybe it could be like a month or two month.

[00:37:39] **BRYCE LELBACH:** There was, there was certainly a window of time in which the review had to be open to give people enough chance to respond. Um, so it was not like a thing that would happen in like a week or so. Um, in later times, what would happen is a library would be submitted for a review and it would not get sufficient [00:38:00] reviewers.

[00:38:01] **BRYCE LELBACH:** It was not that it would be rejected per se, but there would just not be enough participation. And so I can think of, I, I know there was at least one or two times where there were libraries that. Uh, went through one, two or three submissions through review process and, uh, and did not pass because they, they just didn't get enough reviewers.

[00:38:19] **BRYCE LELBACH:** Um, there were certainly some libraries where there were maybe stubborn authors where they were submitted for review and they went to multiple review processes because the authors just weren't willing to make the changes necessary. [00:38:30] Um, yeah. 

[00:38:31] **RAY NOWOSIELSKI:** And beyond like getting approved into boost through this process, then a, a lot of how many of these libraries basically, um, were tested in the market and gained popularity before the review 

[00:38:43] **BRYCE LELBACH:** versus after?

[00:38:44] **BRYCE LELBACH:** How does that, there's, there's only one that I can think of, which was Boost aio, which was the, uh, the Async IO library. And Boost ASIO was always a unique one because it was developed by Chris Koff, um, great, uh, developer. And, uh, uh, somebody I've worked with, uh, [00:39:00] on the C++ committee, um, uh, on the executors.

[00:39:06] **BRYCE LELBACH:** Debacle. Um uh, and uh, I believe AIO was something that Chris was vending before Boost. And I believe that in the case of aio, there were some libraries where in the early days, Beman and Dave approached the library authors and said, Hey, we want this to be part of Boost. So I'm not even sure if SIO went through the review process.

[00:39:29] **BRYCE LELBACH:** I think it [00:39:30] did, but I think one of Chris's conditions was he wanted to continue to be able to distribute SIO independent of Boost. Because what happened with some Boost Libraries is once they got into the Boost ecosystem, they would, somebody during the review process would be like, oh, you know, you have this code here.

[00:39:47] **BRYCE LELBACH:** You really should just use this other Boost library so we don't have code duplication. And after that happened a few times, then. Every Boost Library would depend on every other Boost Library. And Chris didn't want that. He [00:40:00] wanted a version of EO that could be standalone. And there was also a, both a header only version of EO and a non hetero only version of eo.

[00:40:08] **BRYCE LELBACH:** But that's the only one that I can think of that had a pre-existing version. Um, there were a couple other ones that were maybe a little quirky, like the Boost Graph Library that Andrew Lumsden developed. I thought maybe that one was a research project before it was a Boost library. Um, there were some things from like our [00:40:30] HPX project that we, uh, pushed in, like things we developed in HPX that, uh, we then contributed upstream to Boost.

[00:40:38] **BRYCE LELBACH:** Um, and there's probably a few others like that. Um, no, no. Two boost libraries have the same story. 

[00:40:44] **RAY NOWOSIELSKI:** When do you get to WG? 21? 

[00:40:46] **BRYCE LELBACH:** Um, so, uh, I was at LSU working with Hartman, so I went there. And, um, I went to that first Boost Con and I was there on like a temporary contract [00:41:00] and then that was renewed. Um, and when I was there, uh, Hartman was working with this other, uh, scientist and he, the other scientist who was sort of the director of our research group, um, uh, was announced that he was gonna move to another university.

[00:41:20] **BRYCE LELBACH:** Um, but Hartman wanted to stay in Louisiana. Um, and so him and I, and, and a one or two other people stayed and we started our own [00:41:30] research group there, the Stellar group, um, which I was wildly unqualified to do. I was like a 19-year-old. I was purchasing clusters for the state of Louisiana and like overseeing interns and things that a 19-year-old college dropout was not really qualified to do.

[00:41:45] **BRYCE LELBACH:** Um, but it was a great time and, uh, Hart, MIT. Uh, kind of tricked me into going back to school. So he, uh, convinced me that it was the easiest way to keep me on payroll, which was probably true. So I started off just taking like one [00:42:00] class a semester solely to stay on the payroll. 'cause I was very dedicated to the mission of building this, uh, distributed runtime.

[00:42:07] **BRYCE LELBACH:** Um, and, um, I, the, the, I was involved with C++ now in the first year. Um, and Hartman was the program chair the first year at C++ now. Um, and when they announced, when they said it Boost Con, they were gonna form this new conference, C++, now, I was like, I, I wanna volunteer to help. And so I [00:42:30] volunteered and both Hartman and I were involved in those early years.

[00:42:32] **BRYCE LELBACH:** And, um, I, uh, organized the C++ now student volunteer program, which was, um, the, the part of Boost that I probably, uh, uh, feel the strongest about. I still think it's like the best. The best contribution that I've made to the community is probably the C++ now student volunteer program. Um, almost all of the C++ luminaries younger than me [00:43:00] are people that came up through the C++ student, uh, volunteer program, uh, like Michael Park, Louis Deone, um, you know, dozens of others who got this.

[00:43:12] **BRYCE LELBACH:** You know, the way it works is you could submit a proposal to come to C++ now, um, and we would cover your travel and your lodging and you get to come to the conference and you'd volunteer to help out. Um, and uh, I was very passionate about this 'cause I felt like I got my start at the conference and that it was [00:43:30] important for other people for sort of undiscovered talent to have a chance to come here.

[00:43:35] **BRYCE LELBACH:** Um, and so that's really what I was looking for was undiscovered talent. Um, and, uh, uh, I feel like we were very successful in our mandate there. Um, and that sort of created a pipeline of young people who came to the Boost Community to C++ now. Um, and, and I also got involved [00:44:00] then because I was involved with the C++ now organizers with John Klp, et cetera.

[00:44:05] **BRYCE LELBACH:** I, I got involved with the creation of CPP Con, um, and Hartman as well. And at some point, Hartman got too busy and turned over being the program committee chair to me. So I became the program committee chair of C++ now, and of C PPP Con and, uh, got involved with, you know, organizing the first few CPP con.

[00:44:23] **BRYCE LELBACH:** And we were talking earlier, like the, you know, I used to print out all the badges for C++ now, and for like the [00:44:30] first year of C PPP Con, all the badges were printed on, on, uh, on my printer. Um, and, uh, I just, you know, I did whatever, whatever shit needed to be done. I was young, I had a lot of free time.

[00:44:43] **BRYCE LELBACH:** I would volunteer for whatever. Um, but I wasn't on the committee yet, and I, I realized at some point I could just pick up on it from, uh, my interactions at the conference with people that, like I was out of the loop on stuff that if [00:45:00] you really wanted to be in a leadership role in the C++ community, you couldn't do that without being in the committee.

[00:45:07] **BRYCE LELBACH:** Um, and so that was the reason that I wanted to get involved in the committee because I wanted to be a leader in this community and I did not feel like I could do that without being involved in the committee. Um, and so, uh, I was at LSU for four years. I eventually got a degree in math. Um, and then I wanted to get outta Louisiana, so I went to [00:45:30] work at, uh, Lawrence Berkeley National Lab in California.

[00:45:33] **BRYCE LELBACH:** Um, and when I was there, that was around the time when, uh, I pulled the trigger on, Hey, I want to go be at the C++ committee. Uh, so I convinced my employer. Uh, that we should, uh, we should be involved in the C++ committee. And I, I, the first meeting I went to was the 2015 Kona meeting. Um, uh, sad, sad that the first committee meeting that I will miss since then will be the, uh, the, uh, the [00:46:00] 2025 Kona meeting.

[00:46:01] **BRYCE LELBACH:** So, uh, 

[00:46:02] **RAY NOWOSIELSKI:** since you bring it up, we're gonna be filming there. What, what should we expect to see what happens at these 

[00:46:07] **BRYCE LELBACH:** week, um, long meetings? Well, I, I think you'll see some drama at that meeting. Uh, I mean, there's always some drama, but, uh, the two meetings before the standard is finished, um, tend to, depending on your perspective, they're either very interesting or very boring because they're the bug fix meetings.

[00:46:25] **BRYCE LELBACH:** The way that the standard works is we ship the standard every three years. And, [00:46:30] uh, before we ship the standard, we ship a what's called a committee draft, which is like a beta release of the software. It's like when a, when a game company, you know, puts out a game in beta for like players to test it. The C++ standard, we do the same thing.

[00:46:45] **BRYCE LELBACH:** So we send out this committee, draft the beta, and then we let people test it. And in this case that means, you know, mostly reading it. Uh, 'cause in a lot of cases it hasn't fully implemented yet. Or maybe they read some of it, they do some [00:47:00] testing with the implementations have been around and then they send us some feedback, you know, some bug reports.

[00:47:05] **BRYCE LELBACH:** And then we have these two meetings to address the bug reports, uh, to make any tweaks and changes. But we're not talking about making big major additions. Um, however, almost always some. Controversies come out at this point, you're not gonna, it's not at this stage that you're gonna have like big major additions or, or, or, [00:47:30] um, stuff like that.

[00:47:32] **BRYCE LELBACH:** But this feedback process is a chance for people who disagreed with something. But were overridden at the time. They now get a court of appeals, right? They get another chance for their thing to be revisited. Um, and so that can sometimes introduce some controversy. And the thing that can happen at this stage is very rare, but it has happened, is that features can be removed if [00:48:00] we feel like they're not baked enough.

[00:48:01] **BRYCE LELBACH:** So we can't add new stuff, but we can remove stuff. This really only happened two times that I can think of. Uh, in C++ 11, they took out this auto putter thing from the committee draft. I think because Ireland, the Irish national body. Uh, they like threatened to veto the standard, which, uh, I'm eternally grateful for because it was like a fundamentally broken thing.

[00:48:28] **BRYCE LELBACH:** I think it was auto putter. [00:48:30] Um, and then in C++ 20, we took out, uh, contracts. Um, and, uh, there's a chance we might take contracts out of C++ 26. So it'll be an interesting meeting. Um, uh, but because the meeting is very focused on like bug fixes and not really on future looking stuff, um, it's not always the most exciting one.

[00:48:54] **BRYCE LELBACH:** Um, uh, just, but it is. I remember [00:49:00] for C++ 17, uh, I remember, you know. Like library, working group being up at like 10:00 PM on like Thursday or Friday to finish processing, you know, the, the, what are called national body comments, the feedback that we get. Uh, and I, I remember, 'cause I was involved in the C++ 17 cycle, I was, uh, uh, working on the, [00:49:30] um, the C++ 17 parallel algorithms and, um, it was like late at night.

[00:49:35] **BRYCE LELBACH:** Maybe it wasn't 10:00 PM but it was late at night and we were trying to resolve some bug in the wording for, uh, adjacent difference, um, in the library working group. And um, uh, uh, it, it ended with me and Marshall Cloud writing code on, uh, one of those big sheets of paper, like the big flip notepads. We used to have those instead of whiteboards, these big giant pieces of [00:50:00] paper.

[00:50:00] **BRYCE LELBACH:** And you'd flip, they would be like a notebook, but like. Big size. And, um, I, I remember we, we wrote out some code there and Marshall's like, alright, but like, it's not been implemented. We don't have field experience with it. And I'm like, gimme an hour. I'll come back, I'll go implement it now. And I went and implemented it and I came back and I'm like, Marshall, I'm sure it works.

[00:50:20] **BRYCE LELBACH:** And he is like, all right, we can ship it. Um, and so like there is a little bit of that the pre like you, you have to resolve all the bugs in before you ship the standard. Like [00:50:30] you, you, so you have this, this real timetable on you. Um, and uh, it happens less now, but in the C++ 17 and C++ 20 cycle, when we had huge backlogs of work, um, we were really burning the midnight oil.

[00:50:47] **BRYCE LELBACH:** And I wanna elaborate further on this, but given recent events, it's definitely not a democratic process. Um, you should ask David Sekel about that. Maybe he'll be willing to say more. [00:51:00] Um. So, first of all, I hate calling it WG 21. The C++ committee loves nothing more than having acronyms and obscure numbers like WG 21, Lu SG one, you know, P 3000, et cetera, drives me nuts.

[00:51:20] **BRYCE LELBACH:** It's super difficult for newcomers, uh, to have all of these obscure acronyms, like, you know, oh, what study group is [00:51:30] SG 17 or SG 11? Like, just call it the Ranges Study group, or, you know, the Concurrency Study Group. So I never, I never use the acronyms. The, you know, its technical name is ISO slash iec, uh, JTC one slash uh, SC 22 slash WG 21, the C++ committee.

[00:51:53] **BRYCE LELBACH:** Um. And most people call it w most, I, I mean, I think most people call it WG 21 or the C++ [00:52:00] committee. Um, uh, I, having been in a leadership role, I was the chair of the Library Evolution group, um, in some of the other, I was chair of some of the study groups for a while. Um, and I chaired the American Programming Language, uh, standards committee too.

[00:52:18] **BRYCE LELBACH:** Um, I know a great deal more about the process and the formal procedures than lots of other people. And, [00:52:30] uh, I, I don't think that it, that's really the thing that people need to know, but that's the thing that other people in the committee always wanna tell you about. The thing that is important to understand is like, um, what it does and what it is and sort of why it's structured the way it is.

[00:52:48] **BRYCE LELBACH:** So, uh, the, the C++ the language. Started off with a single implementation started as a research project, and then as it evolved, [00:53:00] other implementations popped up. Um, and at some point it became clear that the programming language needed a standard and other programming languages had a standard too.

[00:53:11] **BRYCE LELBACH:** This is a, a feature of languages that have multiple implementations. In the early days, there were a lot of different C++ compilers. Today there's three or four, but even so, you need to have a standard definition of what the language is. Um, and so that means that you need a [00:53:30] body that is going to decide what that definition is.

[00:53:34] **BRYCE LELBACH:** Um, some form of deliberative body. Um, historically speaking, uh, those bodies have been a part of. Uh, international standards committees, languages like cobol, fortran, ada, et cetera, they were all part of, um, uh, they were all standardized by these international standards bodies. Now, these [00:54:00] international standards bodies like ISO and particular IEC, they specify a lot of stuff.

[00:54:06] **BRYCE LELBACH:** Like we're all probably familiar with, uh, the paper sizes. Like, you know, uh, there's like the a four paper, like that's an ISO standard. There's an ISO standard for how to make a cup of tea. There's ISO standards for like water purification. There's ISO standards for, you know, uh, automotive safety, all these other various things.

[00:54:26] **BRYCE LELBACH:** Um, and then there's this one part of ISO [00:54:30] JTC one that deals with sort of software standards, um, and ISO because of. The scope of things that it has to deal with, it has to deal with standards for things that are very important in international trade, for example, because of that, um, it is structured as, uh, an international body with national membership because for some standards it's very important that different countries be able to represent themselves on a national [00:55:00] level.

[00:55:00] **BRYCE LELBACH:** Now, this is a terrible stakeholder model for, uh, a software project, um, because, uh, it should not matter what country you are from. Like, like the amount of voice that you have in the future of C++ should not be dependent on what country you are from. But the reality is that it is that if you are in America, you have, or if you're an American company, you [00:55:30] have less of a vote on the future direction of C++.

[00:55:35] **BRYCE LELBACH:** And on the future leadership of C++, then you do, if you are from some small country where you are the only representative. Um, so it's a very poor stakeholder model. But the stakeholder model for the C++ committee is, uh, that there are these national bodies, uh, represent like the represent representatives of a particular country.

[00:55:58] **BRYCE LELBACH:** And these national [00:56:00] bodies have the ultimate say, the national bodies get to vote on the new proposed standards and the national bodies get to vote on who is the convener. The convener is the person that runs the committee. Um, now that said, that's sort of like the official procedural structure. Um, then there's the technical work of the committee and the technical work of the committee is done by a bunch of different subgroups and there's a pipeline, uh, for the [00:56:30] work.

[00:56:30] **BRYCE LELBACH:** So the work starts off in. Either a in a study group or directly in a design group. There are two main design groups, the Language Evolution Group, and then the Library Evolution Group, which I chaired for three years. Um, and then there are the core groups, um, in the core groups job is to make sure that, uh, the, the things being proposed actually work and are like well vetted and [00:57:00] well designed.

[00:57:01] **BRYCE LELBACH:** And so that's the core language group and then the core library group. Um, and, uh, uh, the proposal starts off, it goes through the design groups, then it goes to the core groups, then it goes and is voted on by the committee as a whole, and then it goes into the proposal for the next standard. And then every three years that draft standard is sent out to the national bodies for their review.

[00:57:22] **BRYCE LELBACH:** And then it gets voted in. It becomes an official ISO international standard. Um, the ISO label [00:57:30] is a very, very, very heavyweight process. Um, and it was perhaps important or valuable in the early days of programming, language standardization, but I think it has very little utility today. Um, if you look at more modern languages or newer languages, they tend to not go down the right route of ISO because there's a lot of overhead and paperwork involved with it.

[00:57:57] **BRYCE LELBACH:** However, it would be very hard for a [00:58:00] language like C++ or Fortran or COBOL to be able to exit that process. But if you look at more modern languages, they usually have, they just form their own body, you know, not, it doesn't have to be like an official structure within some international, you know, uh, non-governmental organization.

[00:58:17] **BRYCE LELBACH:** Um, and that means that they get to pick better stakeholder models. No, I think there's a lot of overlap. I think that on the C++ committee, just like on boost, we, the thing that unites people [00:58:30] is that. Y the everybody there for the most part wants to make the right decisions and wants to make decisions that are going to last the test of time.

[00:58:44] **BRYCE LELBACH:** Uh, that we want to design these thing, right? We don't want ship something that is hurried and rushed. Um, and I think that generally everyone agrees on that. But on the C++ committee, I think, um, [00:59:00] there is a tug between wanting to do things right and make sure your design is fully vetted and wanting to not have to take a decade to ship the feature you've been working on.

[00:59:16] **BRYCE LELBACH:** The average C++ feature, uh, uh, from inception to shipping takes 10 years. Uh, when I joined the committee. Uh, I joined for, uh, uh, [00:59:30] actually one specific feature, uh, that was the Motiva. I said, the reason I wanted to join is I wanted to be involved in C++ leadership, which is true, but I needed to come up with a reason, you know, specific goals, you know, to be able to justify it to my employer.

[00:59:43] **BRYCE LELBACH:** At the time, I was working at Lawrence Berkeley Labs at, uh, HPC Research Center. And the feature that I thought was really important was, uh, a, a standard library abstraction for multidimensional arrays. The thing that eventually became MDs Span. Um, I [01:00:00] started co corresponding with people who are working on something similar in 2014, and we shipped MDs SPAN in C++ 23.

[01:00:10] **BRYCE LELBACH:** It must've been 23. It wasn't 20, uh, because again, things do not ship faster than 10 years. And so 2014 to 2023, that's about, that's about 10 years. Um, and every other feature I've worked on, more or less. Has been a 10 year process. Senders, executors, that was something that we started [01:00:30] talking about in 2016 or so.

[01:00:33] **BRYCE LELBACH:** And, uh, it's gonna ship in 2026. Um, and that's sort of the best case. Uh, like concepts took closer to 15 years, et cetera. And it doesn't matter how much you, you care about the principle of having a good design, of having the right design. Uh, if you've been working on your thing for 10 years and somebody's like, wait, hey, maybe we shouldn't ship it this time around.

[01:00:56] **BRYCE LELBACH:** Maybe we should wait another three years and, you know, give this a little more time [01:01:00] to bake. Sometimes you're like, you know what? This is good enough. Let's just ship this. This is good enough. Um, and I do think there's a point at which you reach good enough. Um, and we've never, we never ship a feature in just in general.

[01:01:20] **BRYCE LELBACH:** There's no software project that ships a feature that is complete. In version one. Um, and, uh, you, you have to ship incrementally, um, [01:01:30] uh, you know, in C++. The greatest example of this is conext, but the first version of Conext were that we shipped had a ton of limitations and restrictions in C++ 11.

[01:01:39] **BRYCE LELBACH:** Uh, like C++ 11. Like you, you, you couldn't really even have more than one statement in a context per function. Um, NC++ 14, we made that better. And then if you look at the evolution of ConX per over time, like wow, it's changed a lot. Uh, but that it's every three years we've made some improvements to it.

[01:01:56] **BRYCE LELBACH:** It's not like we waited 10 years before we [01:02:00] shipped the whole thing. And some people wanna do that. Some people are like, we, we can't, you know, just ship a minimal viable product. And when I was library Evolution chair, one of the. Key things I'd look for in, in my review criterion was what is the minimal viable product?

[01:02:17] **BRYCE LELBACH:** Um, when I came into chair library Evolution, we had a huge backlog problem. We had too many people proposing stuff. Um, and I'm, I'm one of the people that believes we should have a smaller standard library, not [01:02:30] a bigger one. Um, uh, and that we should only ship things that could only live in the standard library.

[01:02:38] **BRYCE LELBACH:** That there's no other possible home for them for whatever reason that they, they, they, if, if they have to be there, then you put 'em there. You don't put 'em there just because they're nice to have there because there's a huge cost to putting things in the standard library. And so when proposals came before me.

[01:02:56] **BRYCE LELBACH:** Uh, people would propose this thing and have all these nice [01:03:00] features, these bells and whistles. My first thought would be like, alright, where's, what can I cut out? Like, give me, give me a, a surgical knife. Let me see what parts of this I can cut out. You know, what parts of this do we not need to ship in version one?

[01:03:14] **BRYCE LELBACH:** How can we make this as small as possible? Uh, because that, uh, reduces risk. It reduces the amount of work we have to do. Um, and, uh, if it's something that we can ship later, if it's, if it's what's [01:03:30] called an additive change. And the question is always, if we don't ship this piece now, can we ship it later?

[01:03:37] **BRYCE LELBACH:** If it would be a breaking change to ship it later if the door is closed, if we don't ship it. Now, if, if you, if you ship this your feature and you don't have this piece of it, and we cannot add it later, then we should talk about having it now because we cannot defer the decision. Right. But if you can defer the decision, if we can be like, this is additive, we could do this later, it'd be no problem.[01:04:00] 

[01:04:00] **BRYCE LELBACH:** Great. Do that. Give me as little as possible for the first version. Um, and uh, where was the question on this one? Where 

[01:04:11] **RAY NOWOSIELSKI:** does some, so how does somebody end up in these roles? So how, how did you end up, uh, and, and when did you end up 

[01:04:17] **BRYCE LELBACH:** in the Evolution Chair role? You know, I, it is sort of the same way that I got started in Boost.

[01:04:24] **BRYCE LELBACH:** I just started volunteering for things. You know, all of these things are volunteer at works. Um, [01:04:30] and, uh, in a volunteer organization, you don't get to pick your staff. Um, you have to work with the people who show up and do the work, right? Because you're not, you, you have no control over the people that you're working with in a volunteer organization.

[01:04:48] **BRYCE LELBACH:** They are giving you their time and. So you have to, uh, lead them, not command them. Um, and that, [01:05:00] that's, that's great for people who wanna get involved, uh, because it means that the door is open to almost everyone. Um, if you show up and you say, I wanna do work, I wanna help out with this or that, like, eventually you're gonna be, you know, given things to do and you're gonna be put in charge of things.

[01:05:19] **BRYCE LELBACH:** And like, that's how I, uh, that's how I got into the C++ now scene and the CPP con scene, which is just like the, that first Boost Con when John Calvin announced, [01:05:30] you know, C++, now he is like, is there anybody who'd like to volunteer to help? And I put my hand up. Um, and it was the same thing with, uh, with the C++ committee.

[01:05:38] **BRYCE LELBACH:** I, the first group I chaired was, um, the Library Revolution Incubator group. And that was just, I had emailed Herb and said, Hey, we have a huge problem in Library Revolution. We had this huge backlog. We should create a group to, uh, incubate papers. And he is like, great, you wanna do it? And I was like, okay.

[01:05:55] **BRYCE LELBACH:** Sure. Um, it was just like, you know, you said you, you said that you had a lot of trouble [01:06:00] getting people to say yes to do this interview. Um, I guess I'm just the sort of person who you, if an opportunity presents itself, I'm just like, yeah, sure, I'll do that. I would ask him, uh, what's next? Um, both for him, uh, for C++ and for maybe, uh, systems, languages in general.

[01:06:21] **BRYCE LELBACH:** And I, I think that when people ask him that, they probably ask him that mostly on, like, the conversations with [01:06:30] Brianna about this feature of C++ are probably on the time scale of like, you know, three years, like the next standard or even six years or so. And I think that because of that, like that's not the interesting question.

[01:06:44] **BRYCE LELBACH:** The interesting question is like the test of time question. It's like beyond a like. What do you think? Where do you think C++ is gonna be in 20 years, in 40 years and 60 years? Um, and I think that's a very, that's an interesting question. [01:07:00] Um, you know, C++ was late eighties, um, which makes it roughly as old as me.

[01:07:08] **BRYCE LELBACH:** So it's like, you know, 30, mid thirties, um, there are languages that have been around for 80 years, like for trans, like an example, just gone through a few different eras. Um, cobol iss, another example, um, both of which are, uh, are, are fundamentally, you know, legacy languages. They're, they're before trans got [01:07:30] a little bit of a resurgence.

[01:07:31] **BRYCE LELBACH:** It's still used in some areas, but, uh, you know, COBOL famously they have the problem of they can't find people who can actually program in cobol, and that's what runs in most of the banks is, is CS plus gonna go that way? COBOL is actually an interesting language. COBOL is the first. Uh, language to have a programming, uh, language standard.

[01:07:48] **BRYCE LELBACH:** And, uh, the story of COBOL is fascinating. I'm actually a little bit of a COBOL historian. I wrote a long Twitter thread on it once, but it was a, a programming language [01:08:00] synthesized in the, like fifties and all the people behind it were, were actually women. Uh, like that would make a great documentary. Not that I'm pitching you, but if you, if you want another project, do a COBAL documentary.

[01:08:12] **BRYCE LELBACH:** But that's what I would ask Arna. BNA is about what the long-term future for the language is. Um, I, we're not particularly, uh, uh, close. We, um, we don't interact that much. Um, but I have a great deal of, uh, respect for bna. Um, [01:08:30] he, uh, he cares deeply about the language and the people who are using it. Um, and him and I.

[01:08:41] **BRYCE LELBACH:** Share a lot of values, um, that we both care deeply about the teachability and the ergonomics of the language. That's interesting. And I think there's multiple ways that could be interpreted. I'm not sure. Um, I, I think he [01:09:00] is per, perhaps referring to what I alluded to earlier, that there were some, li Boost had many libraries that were fairly complex and Boost was not always newcomer friendly.

[01:09:14] **BRYCE LELBACH:** Boost libraries were often things for the power user, and so maybe that's what he meant. Um, but I also think that to some degree, so I mentioned earlier when we were talking about, um, my, me chairing the, the [01:09:30] Library Evolution Group, I, I mentioned that I am. One of the, uh, the people in the, the sort of small library camp who believe that we should have a small standard library because the cost of making changes to the standard library is very high.

[01:09:45] **BRYCE LELBACH:** So we should have as few things in there as possible. My guess is that Brianna's of the other camp, of the big library camp, that he wants a standard library that has things like graphics, [01:10:00] like, uh, uh, you know, io, like a gooey library. Like he wants a standard library that's rich, like the Python standard library, where all the things that you might need, all the things that you would've reached to boost for are just in the standard library.

[01:10:14] **BRYCE LELBACH:** Um. I think that's sort of what he means is that you shouldn't need to have something like Buddhist, but it also may be that complexity angle. But, uh, I would ask him, I would ask him. I, I mean, I think Biana is one of the most respected and [01:10:30] listened to members of the committee. I think his voice holds great sway.

[01:10:35] **BRYCE LELBACH:** I have seen him, I have seen him single handedly change, um, uh, the, the opinion of a room. Um, and it's interesting because I think some people would perhaps classify me and Biana as being in opposite camps of the committee, which is certainly true. There's sort of like a, [01:11:00] an old guard to the committee, and then there's like a reform wing to the committee.

[01:11:04] **BRYCE LELBACH:** And I am very squarely in the reform wing. Um, uh, and I think Biana is, is more in the old guard. Um, but, uh, I, I'm trying to remember the specific discussion, but, um, you don't hear biana speak up frequently on the committee, but I think this was around meta classes. I, there was an evening session about [01:11:30] meta classes and, um, in bi biana raised some point, um, some technical concern or, or something that I hadn't thought of before.

[01:11:42] **BRYCE LELBACH:** Um, and, uh, uh, it, it, it changed my opinion on the, on the matter. Um, and I've seen him do that a couple times. Um, I don't always agree with him, um, but uh, [01:12:00] I've seen a few times more than the few times where he's spoken up and I've been like, this guy's really smart. Um, and maybe not so much smart, but. Maybe it's more of a, a, a wisdom, uh, like a desi like this design sense or, yeah.

[01:12:22] **BRYCE LELBACH:** I think wisdom is maybe the word. Lots of smart people can make unwise decisions. Um, I think that the [01:12:30] times that I see BNA speak up on the committee, um, uh, uh, they, they're often very wise. Um, very, he, he uncovers problems that, um, that other people aren't thinking about because he's often thinking about a bigger picture.

[01:12:51] **BRYCE LELBACH:** He's thinking about the health of the language as a whole. There's not a lot of people thinking about that. A lot of people are thinking about adding this feature or that [01:13:00] feature, or what's best for this feature or that feature. BMO's thinking about the whole picture because C++ is his baby. I mean, it's, he created a language and he's.

[01:13:10] **BRYCE LELBACH:** Um, the, the figurehead of the language. And so he's thinking about the whole, whole view. What is this, what is the, the, the composite, not the individual parts. I don't think we can talk about that that much, because then I'd have to go get Nvidia people to, to [01:13:30] sign off on that. Okay. Yeah. Um, 

[01:13:33] **RAY NOWOSIELSKI:** uh, because it goes into what, uh, 

[01:13:35] **BRYCE LELBACH:** sorry.

[01:13:36] **BRYCE LELBACH:** Uh, because it goes into, um, like, uh, uh, C++ committee politics from the period of time when I worked at Nvidia. Hmm. Yeah. Um, but I mean, I think that there's a more interesting question there, which is, you are right. A lot of people critique the direction of the standard. And it's fascinating because every time I give a talk or I'm [01:14:00] in an audience, there's a q and a about.

[01:14:02] **BRYCE LELBACH:** The direction, the standard. There's always some people who are like, the C++ standard is moving too quickly. You're adding too many features. You're, you're adding too much complexity. That's like half the people and the other half of the people are like, you're not moving fast enough. You're not adding enough stuff.

[01:14:19] **BRYCE LELBACH:** And that's, you know, that dynamic always fascinates me. It, it makes me think that, uh, maybe we're sort of getting it sort of right. Um, [01:14:30] I think that I am not concerned about the technical direction of the C++ standard. Um, I worry about the governance model. Um, the governance model is very complicated.

[01:14:49] **BRYCE LELBACH:** We could spend two or three hours talking about how WG 21 works, and it is a fundamentally a closed process. Um, it's not [01:15:00] something that just anybody can go and join. Um, and we can't film inside those meetings and you can't film inside those meetings. Um, that doesn't make a lot of sense for a software project.

[01:15:12] **BRYCE LELBACH:** Most software projects governance is a lot more open, um, a lot more community driven. Um, and I think that fundamentally the governance model is what, um, uh, is hurting C++ [01:15:30] today, um, because that is what is causing us to move maybe slower than we need to. Um, and maybe to not make the sort of decisions that we should.

[01:15:44] **BRYCE LELBACH:** Yeah, I, I mean, when I came to the committee, I found it pretty hard to get onboarded, pretty hard to learn all these things and, um, pretty. Uh, I don't, it was not designed for newcomers. It was not designed to make it easy for new [01:16:00] people to come and participate. There's like a lot of tribal knowledge, like you show up and they're like, oh, there's this wiki, and oh, you know, you gotta, well, you ask the person next to you for like, how to get the instructions to do this thing.

[01:16:10] **BRYCE LELBACH:** And there's like some instructions here and some instructions there, and you need to know like five or six different passwords to get into different things. And it's just not, there was no like, how to get started guide, you know? Mm-hmm. Um, and like we, we have more of that now, like it's a lot better than when I first joined.

[01:16:25] **BRYCE LELBACH:** But, um, I would, I would [01:16:30] have, uh, a steering council of some sort. Um, and I would have, uh, an implementer's council. So the steering council would be more directly representative of the community at large. Um, I think the most important thing, the biggest problem we have with C++ is we have too many cooks in the kitchen.

[01:16:52] **BRYCE LELBACH:** Um. The committee does not have a shared vision, a shared direction. We have [01:17:00] 300 individual authors, 300 individual cooks. Not all of 'em agree on a vision. And there's no real attempt to set down a vision to, to find a consensus vision of this is what we all agree should be the future. Mm-hmm. Um, and I think we need that.

[01:17:20] **BRYCE LELBACH:** I think we need to have a plan for the future that we vote on, that we did that because voting on it means that the plan has to be [01:17:30] something that can gain consensus. And, and if we had that, I think that would help a lot. Um, but I think also we just, we need to have fewer decision makers, most successful languages out there.

[01:17:43] **BRYCE LELBACH:** Have some form of steering council, um, which is usually an elected position, I think in the case of C++. Um, we, we need to make sure that all the major implementations have a seat at the table. And that's why I would have both a steering council, it would [01:18:00] be sort of solely community driven. And then I would've an implementer's council where every major implementation, there's about four or five, um, would, uh, send a person to the implementer's council post C++ 11, um, C++ 11, successfully standardized a bunch of boost libraries and post C++.

[01:18:18] **BRYCE LELBACH:** And it's, it's important to have a little bit of background here. C++ first standard came out in, uh, 98. Um, and, uh, uh, then the plan was they were gonna put out a revision, [01:18:30] minor revision with some bug fixes in oh three, they did that. Um, and then they were working on the next major revision, which was like originally gonna be oh six, let's say, and then it slipped to oh seven and then oh eight and then oh nine.

[01:18:44] **BRYCE LELBACH:** And they really thought it was gonna happen in oh nine. And then. Like 10. And then finally it shipped in 11. And when I refer, we, we talked earlier about C++'s dark period. The dark period was that era, the dark period was the period from like [01:19:00] 2000, 2003 until the release of C++ 11. And, uh, C++ 11 was supposed to ship way earlier.

[01:19:09] **BRYCE LELBACH:** Um, and it, the date kept getting pushed back and back and back and back. Um, because C++ 11 was a feature driven release. The, the, they said, we're gonna ship these things and, you know, we'll ship it. Like we'll ship it when they're ready. Uh, and that was a poor model because when the things were not ready, then the release [01:19:30] date kept slipping and slipping and slipping.

[01:19:31] **BRYCE LELBACH:** Um, and so there was basically a 10 year period of time when C++ got no new features. Um, and at the same time, other languages are rising in popularity. Um, like every, everybody was crazy about Java. Um. During this period, this, during this period, um, everybody was experiencing the free lunch of Moore's Law scaling.

[01:19:55] **BRYCE LELBACH:** So every couple years, new processors came out that were twice as fast, you know, four [01:20:00] times as fast as, as the, the, the earlier processors. Um, and, uh, what happened around the time that C++ 11 came out And, but because the process of beginning faster, you didn't have to worry so much about writing native code 'cause your, your software would just sort of magically get faster.

[01:20:19] **BRYCE LELBACH:** Um, and so C++ being lower level, being more performance oriented, uh, but also more complex, it was sort of like, you, you don't really need this. Like, you know, our, our, our code just [01:20:30] gets faster because the chips are just rapidly getting faster. Uh, but, uh, around the time that C++ 11 came out, that sort of stopped.

[01:20:39] **BRYCE LELBACH:** We, we reached a point where the. The scaling of transistors started to slow down and the scaling of performance started to slow down. You couldn't just make a, a faster clocked chip. Uh, uh, you could add more transistors to the chip, but, but we were reaching the limits of clock [01:21:00] speed. And so how did you, uh, get more performance?

[01:21:04] **BRYCE LELBACH:** Well, we, we moved to a multi-core era, um, uh, to an era of parallelism. Um, and, uh, and that meant that. We like because you no longer got the clock, the, the clock speed scaling, you started having to care more and more about performance. And so if you look from that era, you'll see companies like Microsoft had this whole going native movement where the early two thousands, Microsoft was all [01:21:30] about like, you know, dotnet, we're gonna run everything, all the codes gonna run as managed code.

[01:21:34] **BRYCE LELBACH:** There was this managed C++ stuff. And then around the 2000 10, 11, 12, they did this going native thing of nope, we're gonna go back to writing native C++. 'cause that's what you need for performance. And at that same time that that shift was happening, that there was a demand for more performance oriented software, C++ 11 came out a revitalized language, really almost a new language.

[01:21:56] **BRYCE LELBACH:** Um, and so that is why C++ [01:22:00] saw this resurgence in the 2000, uh, you know, 11 to 2020 era because. It. There was this, you know, new version of the language and, um, uh, also, uh, uh, there was this demand for a language like that. And what happened on the committee was after C++ 11, herb said, we're not doing this feature driven thing again.

[01:22:25] **BRYCE LELBACH:** We're gonna ship every three years on those three years. And, um, uh. [01:22:30] Th then, because we'd been so successful at standardizing libraries and C++ 11, there were these calls of, Hey, let's standardize a lot more libraries. You know, let's pull in more boost libraries, let's add a lot more libraries to the standard library.

[01:22:42] **RAY NOWOSIELSKI:** 'cause Boost saved CC++'s ass in 2011. 

[01:22:46] **BRYCE LELBACH:** Yes. I, I would, I do think that Boost, um, did, uh, contribute to this because during that dark period, um, boost was where a lot of ideas were being tested and [01:23:00] proven. And, uh, boost provided, uh, a gap for people to be able to develop code and C++ and without Boost, I think you would've seen a much sharper decline in C++ usage during the, um, during the c, during the two thousands to 2010 period.

[01:23:18] **BRYCE LELBACH:** And it may have been enough of a decline that. C++ would've really just died off even despite C++ 11 because it nearly killed the language. Okay. Because if we had, if there [01:23:30] had been a C++ oh three, a C++ oh six a C++ oh nine, that had incrementally added features, it would've been substantially better.

[01:23:37] **BRYCE LELBACH:** Um, and it would not have nearly killed a language. It's really hard. Like imagine, imagine that you had an app on your phone that you had to wait 10 years for the next software update, and it's like, Hey, in 10 years that next software update, it's gonna be great. It's gonna have all these new features, it's gonna have like 10 new features, they're gonna be great.

[01:23:54] **BRYCE LELBACH:** And you'd be like, well, can you just give me like one new feature in year instead of that? And it's like, no, no, no, we [01:24:00] gotta, they're gonna all come as a package deal. And so you asked about my predecessors. So my predecessors, I think the first library evolution chair was Alistair Meredith, who he lives like a.

[01:24:14] **BRYCE LELBACH:** He lives like, uh, one or two blocks that way. Um, and like one block over. Um, and, uh, he was the first library evolution chair. I didn't, I've interacted with him a lot, but not when he was chairing the library Evolution chair. When I joined was Jeffrey Yakin. [01:24:30] Um, and, uh, Jeffrey Yakin was the best library evolution chair.

[01:24:35] **BRYCE LELBACH:** Um, he was, um, the best at building consensus. He was just like a wizard sharing and sharing's, like a whole art form, like getting a group of people to agree on something. Uh, it's a tough scale. I'm like decent at it. Um, Jeffrey was a wizard at this. He was really, really, really good. Um, uh, [01:25:00] he just, he, he, he knew how to bring people to a table like that, that man could like.

[01:25:05] **BRYCE LELBACH:** In a different life. Uh, he could be like a, uh, you know, an international, you know, uh, diplomat, you know, negotiating peace accords between waring countries, I'm sure. Um, and uh, when I joined, we were still in this big library era of like, we're gonna standardize 2D graphics, we're gonna standardize all these other things, put 'em in the library.

[01:25:26] **BRYCE LELBACH:** And, uh, because we put out all these calls for [01:25:30] tons of proposals, we started building up a backlog, um, a pretty substantial backlog. And C++ 14 was a minor release, C++ 17 was sort of a mid-size release. Um, and there were a lot of things, a lot of proposals that were approved for C++ 17 that did not make it because of how long the backlog was.

[01:25:52] **BRYCE LELBACH:** Um, after Jeffrey. Uh, Titus Winters became Library Evolution Chair. Now Titus lives right over the [01:26:00] bridge there in Long Island City. Um, so th three of the four library evolution chairs are all within like a one mile radius of, of each other. Um, Titus, um, Titus is I think probably my favorite library evolution chair.

[01:26:17] **BRYCE LELBACH:** Um, uh, Jeffrey, I think, I think everybody would agree Jeffrey was the best, best, but Titus is the one closest to my heart, um, because I think Titus has the best sense [01:26:30] of software design and thinking. Um, uh, and he, um, his focus was not on what particular features are we gonna ship. Um, he didn't really care about that.

[01:26:43] **BRYCE LELBACH:** What he cared about was quality, was that we ship things that were gonna last the test of time and that we only ship things that were like well vetted. Um, he was library evolution chair for about three years. Um, and then, uh, yeah, then he decided [01:27:00] to, uh, uh, step down. This was around the time that Google, um, disengaged a little bit from the, the committee, um, because they wanted the committee to commit to making breaking changes more frequently.

[01:27:13] **BRYCE LELBACH:** And the committee, um, only gave a lukewarm signal about that and was sort of non-committal. And so Google, um, uh, sort of backed off a little bit. They were a lot less investment from Google. Um, and, uh, and then I became Library Evolution Chair. [01:27:30] And, um, I think to some degree my administration was a continuation of Titus is.

[01:27:36] **BRYCE LELBACH:** But, um, a large part of what I tried to do was to decentralize the work. I was also the chair during the pandemic and I was very big believer in. That we should continue the work during the pandemic. Some others in the committee were like, sort of felt like we should just close up shop and just take a pause for however long the pandemic was gonna be, which [01:28:00] I thought was nuts.

[01:28:01] **BRYCE LELBACH:** Like COBOL and FORTRAN shipped new versions of the standard during the pandemic without face-to-face meetings. I, I don't think that C++ was some special unique beast where the only way we could develop the language was if we all get in the same place. Um, uh, I think the pandemic was a unique opportunity for the committee to modernize and adapt, and we did not take advantage of it as much as we could have.

[01:28:23] **BRYCE LELBACH:** So I was faced when I came in with this big backlog of papers, um, uh, of these, this huge [01:28:30] backlog proposals. And so a large part of what I was trying to do was trying to, um, improve the process, streamline things, um, and frankly to be able to say no to more papers. One of the problems with the committee is that we're really bad at saying no.

[01:28:43] **BRYCE LELBACH:** We would rather tell somebody. Yeah, you, you go and do some more work on that and come back to us. Even when in our hearts we know that we're never gonna ship that feature. If we know that we should just tell people that. Uh, because it takes committee time, it [01:29:00] uses our time and our limited time and resources to, uh, I continue reviewing a paper and I, you'll, you'll hear now you'll see in a lot of like committee votes.

[01:29:12] **BRYCE LELBACH:** Now there's this wording, uh, knowing that our time and resources are limited, do we want to continue pursuing paper? And that this paper, and that is language that I introduced in library Evolution that I wanted every time that we voted to spend more time on something. I wanted us to [01:29:30] acknowledge verbally that we're committing to spending more time on this thing, knowing that our time and resources are limited, and that by choosing to spend time on this, we will have less time and resources for other things.

[01:29:42] **BRYCE LELBACH:** We standardized the libraries that were most like widely applicable, but Boost was a home for libraries that are also not so widely applicable. Um, and uh, uh, part of it is we didn't [01:30:00] understand in that era the costs of standardization. If you and I, I gave a talk about this a couple years ago about sort of my theory.

[01:30:09] **BRYCE LELBACH:** The talk is called What Belongs in the C++ Standard Library. Um, when you put something in the C++ standard library, it means every implementation has to implement it. Um, and so that's a very high cost and it's also, it's very hard to change things in the standard library. And we didn't understand this in the C++ [01:30:30] 11 era because we had gone a decade without making any changes.

[01:30:34] **BRYCE LELBACH:** And so when you go a decade without doing something, you don't understand the cost of that thing. The C++ standard Library, the reason that. Some orgs like Google have, you know, decided to not invest as heavily is because the C++ standard and the standard library make very long-term commitments about, um, a BI compatibility, um, essentially guaranteeing that [01:31:00] we're never gonna break a BI going forward.

[01:31:04] **BRYCE LELBACH:** Um, and we also have very high bars for source compatibility. Um, and because of that, if we make mistakes in what we standardize, it's very hard to unwind them. Whereas a library that's in boost can make breaking changes a lot easier. And so I'm, I, I'm gonna set a very high bar for what I think belongs in the standard [01:31:30] library because once it's in the standard library, it's set in stone.

[01:31:32] **BRYCE LELBACH:** Hmm. And so we, we cannot afford to make mistakes. Um, and because of that. I only wanna put things in the standard library that absolutely have to be in there. And that is things that abstract over, um, aspects of different platforms. Things that have to be implemented by the person implementing the C++ compiler in standard library.

[01:31:57] **BRYCE LELBACH:** Things that only they would know how to implement. [01:32:00] Um, other libraries that implement things where you could just write one version of the library, put it on GitHub and it would work on everybody's platform. Things that don't need to interact with the C++ compiler, um, in the way that some standard library features do.

[01:32:15] **BRYCE LELBACH:** Like there's no need to put them in the standard library. The difference that some people wanna put stuff in the standard library 'cause they're nice to have. Um, and that was the philosophy going into C++ 11. And then we learned a lot about the costs of that and, [01:32:30] and then that sort of changed the equation.

[01:32:32] **BRYCE LELBACH:** And because we've set the bar a lot higher, um, even though. There's a lot of really good boost libraries. They may be the really high quality libraries, but they may not be good candidates for standardization. If the library is doing its job well outside of the standard, then like why does it need to be in the standard libraries like the Boost Thread library, the Boost Atomic Library, um, [01:33:00] uh, the shared putter library, all of those, there was a strong reason to put them in the standard for the thread library and the Atomic Library.

[01:33:07] **BRYCE LELBACH:** They needed deep integration with the compiler for the shared putter library. That's true as well too. But also it's something that's so widely used that you really want an, an implementation of it. You want one implementation of it that's gonna be common. That can be a vocabulary across all different projects and you want a very optimized [01:33:30] implementation of it.

[01:33:30] **BRYCE LELBACH:** Things like, uh, optional and topple. That's the same thing where you need to have one definition that all libraries can use. Those we call those vocabulary facilities. Um, those are the things that are important to standardize. Something like the Boost Graph Library. I can't see a compelling reason to have that be in the standard.

[01:33:51] **BRYCE LELBACH:** Um, that is a lot more domain specific. It doesn't require any special compiler support. It doesn't need to be a, um, [01:34:00] uh, uh, a vocabulary type. It's perfectly fine as a library outside of the standard. Um, and, uh, I think that that's why we've seen less libraries be standardized is that we, we standardized the ones that most needed it.

[01:34:14] **BRYCE LELBACH:** And then our philosophy about standardizing them changed. And also again, the distri, the changes in the cost of distribution. You know, today it's very easy to go and get a C++ library. There are C++ package managers, or you can just get it from GitHub. It used to [01:34:30] be that that was not the case.

[01:34:31] **BRYCE LELBACH:** And we use the standard library as a crutch for the fact that we did not have good package management stories for C++, but that has changed. Now I 

[01:34:42] **RAY NOWOSIELSKI:** rattle off a few, maybe you've got Yeah. A take. I mean, asio I think is the one that comes up a lot. What you mentioned Chris Koff 

[01:34:49] **BRYCE LELBACH:** and Yes. What 

[01:34:50] **RAY NOWOSIELSKI:** did, what did go down regarding 

[01:34:52] **BRYCE LELBACH:** that one?

[01:34:53] **BRYCE LELBACH:** Um, I don't think I can comment on that one. I'm so sorry. Okay. Uh, [01:35:00] 

[01:35:00] **RAY NOWOSIELSKI:** what about fiber Co routine two, uh, Alki, 

[01:35:03] **BRYCE LELBACH:** um, 

[01:35:04] **RAY NOWOSIELSKI:** what did that, 

[01:35:08] **BRYCE LELBACH:** so I don't know. I mean, I think we ended up in like a pretty good place with that. I mean, that, that's, uh, the, the evolution of that is planning on shipping. I don't know if it's in this cycle or, uh, if it's in the next cycle, but that's just one of those features where like, people forget that.

[01:35:25] **BRYCE LELBACH:** We talked earlier, every feature's a 10 year story. Um, the fiber context [01:35:30] paper work started on about 10 years ago. Um, like there's always a long journey for these things to get standardized. Um, and the long journey doesn't necessarily mean that anything's going wrong, but like that's something that does belong in the standard library and needs deep support with the compiler.

[01:35:44] **BRYCE LELBACH:** Makes a lot of sense to have it there. Um, Nat Godspeed's working on that. Uh, it looks, I think that's either in the next standard or I'm pretty sure it's in C++ 26. But that one I think is a success story. That's, that's a more recent library that's gone from boost into the standard. So we, [01:36:00] we do still put things into the standard that are inspired by Boost.

[01:36:05] **BRYCE LELBACH:** Um, it just, it does happen less frequently. The perception is that C++ 11 was just like that. We took things directly from Boost. But if you go and look, the reality is that it's always been inspired by Boost Threading, boost Threading library and the standard threading library have some fairly notable and substantial differences between them.

[01:36:26] **BRYCE LELBACH:** Um, uh, the way that, uh, stood shared putter and Boost shared [01:36:30] putter, again, some differences. That's ones maybe a little bit closer. Um, uh, there's always tweaks and changes, uh, boost file system and stood file system. Again, there's tweaks and changes. Uh, we don't adopt them wholesale. Yeah, I completely agree.

[01:36:45] **BRYCE LELBACH:** Would agree with that. And I, I mean, famously on the committee, I am the, the person who sort of led the campaign against, we should not standardize 2D graphics. I stand by. I stand by that. Yeah. Uh, in fact, I would say I, I think that is one of my [01:37:00] most lasting contributions to the committee, um, is, uh, uh, was saying no to 2D graphics.

[01:37:08] **BRYCE LELBACH:** Uh, because, you know, the committee needed to learn how to say no. Um, it was good that we learned how to do that. I don't think it meets any of my criterion. Um, uh, it is not something that I see a compelling reason why the standard library could do a better job or, or why something would need to be in the standard library.

[01:37:29] **BRYCE LELBACH:** I think it's perfectly [01:37:30] fine to have it as a third party library. It's also something where logging is gonna be very opinionated. It's gonna be a little, it's, it's not that logging itself is gonna be domain specific. It's just the way that you're gonna wanna do logging is gonna be a bit more the domain specific.

[01:37:46] **BRYCE LELBACH:** I would probably entertain a little proposal for a logging library. Um, uh. Uh, it's maybe not as strictly outta scope, but, um, I, I don't think it meets my [01:38:00] criterion. I think I would probably vote against it, uh, against standardizing something like that. Yeah. What I, I have to remember. Yeah, that's like the HTT p RI library, right?

[01:38:10] **BRYCE LELBACH:** Um, yeah, that one is, uh, something that you can make more of a case for. Um, and the reason for that is because different platforms want to expose HGTP in different ways, in particular because of security. Um, and [01:38:30] so that's a case where you, you would want to have a standard interface for it, because then that way each individual platform could decide how to expose HTTP in a way that is secure.

[01:38:43] **BRYCE LELBACH:** So, like on the Apple platform, would you rather trust, uh, you know, some third party. Or Apple to provide you with a secure way of doing HT P-H-T-T-P on an Apple platform. Would you rather [01:39:00] trust a third party or Microsoft to provide you with a secure way to do it on Windows, et cetera? I would rather trust for something like that.

[01:39:08] **BRYCE LELBACH:** I would rather trust the um, the platform. So that's something like that. I think definitely in scope it's challenging though because of the security aspect of it. If we ship something like that, then the standard library becomes. Uh, responsible for shipping a security critical component. Um, and that means that we need to have a better model for [01:39:30] being able to do security updates.

[01:39:32] **BRYCE LELBACH:** There's a lot of implications to that, and that's why we haven't done it so far. But that's definitely in scope. Yeah. Things like variant, that's a vocabulary type that falls into my criterion. Yeah, I don't think there was a need for that. 'cause that was a, uh, like traditional template, meta programming library, and we've moved on to different meta programming techniques.

[01:39:52] **BRYCE LELBACH:** I, I think that it ended up turning out well for me because, [01:40:00] um, had I ended up being the person in that job, I think I would've been presiding over, uh, a, maybe a dying empire. Um, I think that a lot of the problems that C++ has are not things that the convener can fix. Uh, the convener cannot. Uh, completely fix our process problems because a lot of it is just things that are dictated by iso.

[01:40:28] **BRYCE LELBACH:** But I do think a convener [01:40:30] could, um, uh, could make the case for, uh, us trying to find a way to exit iso, um, and to evolve C++ outside of iso, um, which I think would be the best thing for C++. 

[01:40:49] **RAY NOWOSIELSKI:** Um, did things get heated? 

[01:40:51] **BRYCE LELBACH:** Um, I don't think I can answer that one. 

[01:40:57] **RAY NOWOSIELSKI:** Uh, next question.[01:41:00] 

[01:41:01] **BRYCE LELBACH:** Uh, yeah, there's, uh, I, I think there are some people who don't like me so much and there's some people who do.

[01:41:11] **BRYCE LELBACH:** Yeah, I mean, I think. There's always been disagreements in Boost, even back in like the day, or, you know, there's, there's always something. Um, I think that, uh, almost any community always reflects the times that we live in. Um, I don't think that, uh, things have [01:41:30] been uniquely, uh, uh, divisive in Booo East versus other places.

[01:41:36] **BRYCE LELBACH:** Um, uh, you know, oh, no, no, no, no, no. Anybody who's telling you that is just remembering things with nostalgia. Yeah, no, there used to be, I mean, I, I remember back when I was very early on, like a very early, uh, boost contributor, um, I actually, I was trying to fix some set of bugs across multiple libraries [01:42:00] and like, I had committed some things where, uh, I hadn't gotten like, sign off from like, the maintainer, but it was just like a bug fix and, uh.

[01:42:08] **BRYCE LELBACH:** Uh, like I remember Dave was pissed at me, and I think they'd taken away my commit access for some period of time. And then Hartman talked to him and he is like, Hey, Bryce is just a kid. Like, you know, I'll sort him out and, uh, you know, no, there were always, there were always disagreements. Um, you know, but I think there's always been, um, uh, uh, like to me it's fine.

[01:42:29] **BRYCE LELBACH:** People [01:42:30] disagree as long as they, uh, respect each other. And there have been times when that's not happened. Um, but I think for the most part, everybody respects each other and there's a shared set of values, two topics. Oh, I definitely, I definitely can't comment on those. Yeah. I will say like, I think the, um, the boost, uh, like steering council, uh, I've been very happy with.

[01:42:55] **BRYCE LELBACH:** And, um, I think David, uh, was a really great [01:43:00] leader for Boost. Um, uh, yeah. Um. But it's sort of, it gets to the question like, what is Boost and what is its role going forward? I, I, I honestly don't really know that much about that. Um, yeah, I, I mean, I know something happened, but I really don't know that much about it.

[01:43:18] **BRYCE LELBACH:** It's not super relevant to me day to day. Um, I, I kind of think of Boost as being done. Um, like it was, it was a successful project. Yeah. And, uh, like, I [01:43:30] can't think of the last time that I've used a Boost library. Um, and so it's, it's something, it's a time I think of fondly, but not something that I think of as like an act of ongoing thing.

[01:43:40] **BRYCE LELBACH:** Really talked to it earlier about that. Uh, I kind of feel like in hindsight I am happy that I did not end up as convener because, um, I think, uh, if I was just the C++ guy, uh, it would've sort of limited my career growth. And, um, leading library [01:44:00] evolution was taking up 50 to 60% of my time. Um, and it, it became clear to me at some point that, um, uh, if I wanted to advance my career, if I wanted to grow as an engineer, as a developer, then I needed to branch out a little bit more and try new things.

[01:44:20] **BRYCE LELBACH:** Um, and, um, and, uh, you know, I'd spent my entire career on C++. Um, and, uh, [01:44:30] it, it started to feel a little limiting. Like I was sort of doing the same thing, working in the same space. Um, and, you know, my, my predecessor Titus served for three years. Jeff researched for I think about three years too.

[01:44:43] **BRYCE LELBACH:** Maybe it was closer to five. Um, but I, I always had had planned that after three years I was gonna, I was gonna step down. Um, uh, you know, I, one of the things I told Inval was like, like, your first job is to figure out who your successor's gonna be. And I was very. [01:45:00] Proud of the organization that we built in Library Evolution, where, uh, all the prior leaders had just been one person doing all the work.

[01:45:09] **BRYCE LELBACH:** And I was very convinced that the right model was to build out a team and to delegate the work out and to beat up, build up other leaders. And, um, uh, in ball, I felt was the person who had the drive and the, the right combination of skills, not just technical [01:45:30] skills, but also personal skills and administrative skills, um, uh, that like, I knew she would be on top of stuff.

[01:45:39] **BRYCE LELBACH:** Um, and, uh, so she seemed like the natural choice to me. And so that was when, you know, when it, when I felt like it was time, uh uh, which was around the three, just about three years after I'd started and, and it was, I was starting to feel. The, you know, weary anyways. And I remembered seeing [01:46:00] how weary Titus felt towards the end of his tenure.

[01:46:03] **BRYCE LELBACH:** Uh, you know, I, I briefly chaired the Tooling Study group and, um, the reason I ended up chairing the Tooling study group was one time I was out at dinner with Titus, uh, and he was supposed to chair an evening session of the Ting Study Group, and he just, he looked tired and exhausted. 'cause he'd been chairing library revolution all day.

[01:46:21] **BRYCE LELBACH:** And I was like, he was like, I just wanna go to bed. And I was like, well jokingly, do you want me to chair for tonight? And he's like, sure. [01:46:30] And so I went and I shared it and then he was just like, Bryce is gonna do this now. Um, 'cause he was, he was tired. It, it's very hard. It's very, very draining. Um, because you, you're at the committee meeting and you don't have a break.

[01:46:44] **BRYCE LELBACH:** I would wake up at 6:00 AM. And I would work until, you know, 11:00 PM I would not have a break. I would work through lunches. I would work the whole day and there would constantly be people coming to try to get something from me. Um, and it was fun. [01:47:00] It was, it was great. It, I think it, it taught me a lot of skills that I know have been very valued to me in other contexts, but I think it'd be very hard to do that for more than, more than three years.

[01:47:11] **BRYCE LELBACH:** Um, so, uh, I was very happy that I had somebody like in ball to be able to turn it over to, we didn't talk about Dave and I think it's worth talking about Dave. Um, you know, when I joined Boost there was Dave and, uh, I didn't necessarily get along with David first. Um, you know, [01:47:30] David was his big personality.

[01:47:31] **BRYCE LELBACH:** He was the leader of Boost when I came along. And, um, uh, we, okay, maybe it was because there was that time when he revoked my commit access, but I don't hold that against him. But we just, um, he had a lot of strong opinions and I didn't always necessarily agree with them. Um, and then, you know, Dave went to Apple to work on Swift and he left Boost.

[01:47:52] **BRYCE LELBACH:** And um, you know, it's like you don't miss something until it's gone. I immensely missed Dave's presence in [01:48:00] Boost and I did not realize the degree to which Dave was essential to the functioning of Boost. 'cause we talked earlier about how Boost was this. Like there was no centralized decision making, no centralized policy.

[01:48:12] **BRYCE LELBACH:** It was all these individual library authors. Well, there was only one person that could, that had the willpower and the respect and the authority to be able to, uh, make the critical decisions across booze that needed to be made. And that was Dave. Um, [01:48:30] and when Dave's focus shifted elsewhere, I think that, uh, I think that Boo suffered a bit because of that.

[01:48:37] **BRYCE LELBACH:** Um, and there was nobody who could replace Dave. Um, and, and it was also, it was sad to not have him at C++. Now, it was sad that there was this period of time when he was no longer able to come to the conference that he loved in a place that he loved. Like the reason that it was in Aspen was because Dave had connections there, had roots there.

[01:48:58] **BRYCE LELBACH:** Um, and that was a place that [01:49:00] he just deeply loved. And it was sad that he was not there. Um, and I was very glad when in more recent years he was able to come back, um, uh, to the conference. And like the first time I saw him, I was, it was, it was really nice for, to see him back there again. And, um, I don't think that Boost works without Dave.

[01:49:20] **BRYCE LELBACH:** Uh, I think that a large part of Boosts success was because of his. Um, his leadership, I, I, you have to keep in mind, I only got involved [01:49:30] in the community around 2010, 2011. Um, and, uh, I think even then Beman was stepping back a bit and, uh, uh, Dave was really the one more actively involved in leadership. So, um, I, I know Beman, uh, I had dinner with him a few times, but, um, I didn't interact with him so much on the Boost project as I did with Dave.

