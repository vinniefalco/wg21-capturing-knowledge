# BOOST_GLEN_FERNANDES_STRINGOUT_v01

- - - -
filmed Date: 2025-10-28  
location: Darien, NY  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1140474568/a6c8392c2d  
summary: Strong on general Boost history since 2011, characters across Boost and WG21, Foundation vs Alliance in 2024  
- - - - 

## Transcript Start

[00:00:00] **GLEN FERNANDES:** So I'm 

[00:00:21] **GLEN FERNANDES:** Glenn Joseph Fernandez, and, uh, I'm software engineer, but, uh, for Boost, [00:00:30] I am, I guess first and foremost a contributor. I think that's the, probably the highest title you can have in Boost. You can be a library author, but really Boost is all about, you know, the contributions, right? Like you, you, you commit, you, you make, uh, changes to existing libraries.

[00:00:46] **GLEN FERNANDES:** You make them better. That that's, yeah. Uh, that's a tough one. I mean, I think, um, you know, I, I would go to the source, right? I, I like, or as close to the source you can get the people that were there [00:01:00] when, um, they started the project. Like people like Dave Abrahams and um, uh, you know, Doug Gregor and um, you know, obviously Beman is no longer with us, but, um, yeah.

[00:01:12] **GLEN FERNANDES:** Uh, so the, I mean, you know, boost, uh, started because, um, I mean the way I look at is Boost was the original library evolution working group before there was a library evolution working group. When there were, when the committee had, you know, just core and library, uh, boost was the place where. [00:01:30] Uh, ideas took form, right?

[00:01:31] **GLEN FERNANDES:** Like, uh, people design new library facilities and with the, with the view of, um, uh, proposal for the standard. So it was a vehicle for entry into the standard, and then it, you know, it, it had that initial, um, uh, I guess how, how would I put it? It, it followed that path initially, but then it took it, uh, life of its own, right?

[00:01:55] **GLEN FERNANDES:** Because people writing production code started using [00:02:00] Boost because the libraries were useful. They weren't in the standard yet, but they were great libraries. So, um, you know, my introduction to Boost came, uh, in 2011 when I was working at Microsoft. Right? And to me, micro, you know, I was wondering why, why the team was using Boost or, or the lead architect, um, you know, chose to use Boost because for many of the facilities, you know, visual, C++ 10 at the time [00:02:30] started to implement, uh, you know, various library pieces that would eventually go into C++ 11, right?

[00:02:36] **GLEN FERNANDES:** Like they were already targeted for the next standard and they were supporting. So, and you know, it was explained to me when I joined this team that, that they were using Boost because they trusted Boost more than the standard library implementation of the visual c plus post compiler. And what was interesting about that was this is Microsoft, the people that make the compiler and groups of developers within Microsoft, you know.

[00:02:59] **GLEN FERNANDES:** Preferred [00:03:00] boost over the product that the company, uh, develops. Right. And I, and uh, for me finding out what the reasons behind that were, were interesting too, because for, in some cases it was, well, this boost does this better because it's faster or, or, uh, boost the boost equivalent of this has less defects in these cases.

[00:03:22] **GLEN FERNANDES:** Maybe, you know, like, um, it works with Null PTRT or something. And the other, um, and and related to that [00:03:30] was, well, if there's a bug and boost, we know we can upgrade within, uh, three months 'cause that's their, their release cycle. Whereas to get an upgrade in, in visual C++, we might have to wait 10, uh, sorry, two years, right.

[00:03:42] **GLEN FERNANDES:** For the, for the compiler because that's their release cycle. So for me it was, you know, working with Boost in a code base and then, you know, that led to, oh wait, here's something that we need, but, uh, or people need and Boost doesn't have. And I thought, [00:04:00] well, you know, I'd love to, you know, not just invent this for the people that need it, but invent this for, you know, uh, for Boost.

[00:04:07] **GLEN FERNANDES:** Contribute it to Boost so that everyone gets to benefit from it, right. So that, that's I guess, my connection to Boost working at Microsoft and, and deciding to, um, contribute back to Boost. I think so. I mean, I don't know if that you could say that for open source in general. Right. You know, to some extent, um, you feel like you want to give back because you benefit from [00:04:30] it.

[00:04:30] **GLEN FERNANDES:** I think that that, that has resulted in a lot of contributions to boost and, and you know, obviously pride is another thing, right? Like, I invent this and I want the world to, you know, to see it and, and it'd be credited to me, right? And, um, you get the much bigger scope in, in something like an, an open source project like Boost than, you know, inventing something in a, in your close source organization, right?

[00:04:52] **GLEN FERNANDES:** When Boost stop being the, um, just a thing to get experimental libraries into the standard and [00:05:00] became this very hardened, uh, you know, collection of libraries that people treated almost like production code because they knew that all these companies depended on it. Right? You know, I think that was before 2011 because before my time in Boost, but I would say that's probably one of the key, uh, key turning points in boost history.

[00:05:20] **GLEN FERNANDES:** Okay. So, um, I guess the, I'll start with New Zealand, which is where I, you know, where, where I basically grew up in Auckland. Uh, my dad was in, [00:05:30] uh, tele in the telecommunications industry. So he, he did a little bit programming when he was younger, but mostly he was in networking. Um, so New Zealand was where I grew up.

[00:05:40] **GLEN FERNANDES:** I, I had an interest in programming when I was very young and he bought me a book on. C programming. It was by, uh, it turned out to be a very, a terrible book. It was by this author called Herbert Hilt. And, and it's widely guarded today as, as one of the worst, more, not one, one of the worst books on c programming, but any, in any case, you know, that was the book I had.

[00:05:58] **GLEN FERNANDES:** And he, he bought me a, a copy [00:06:00] of the, uh, turbo C compiler for Dawson. That's the sort of environment I I I learned on. Um, you know, we, we, uh, at some point we moved in 2000, we moved from Auckland, uh, New Zealand to Sydney, Australia, which was, uh, my dad's job. He, he, um, started working for IBM, uh, so in Sydney, you know, when we, I mean, I was still programming for fun, mostly writing, uh, programs for people at school or, you know, maybe doing things like [00:06:30] breaking copy protection on video games and, and stuff like that.

[00:06:32] **GLEN FERNANDES:** But we could cut that out. Um, but, uh, yeah, so I started using C++ just out of interest because I, you know, it, it, you started to see a lot more, um, uh, projects start to use C++, even though I was predominantly a C programmer. So I started learning C++. Um, I think I was probably in high school, like 15 or 16.

[00:06:57] **GLEN FERNANDES:** Um, and yeah, I think [00:07:00] while I was, uh, you know, I went to college. I mean, the, the, what led me to it was just that, you know, it was starting to gain widespread adoption. What I liked about it was very easy to, um. You know, with the, with the, uh, standard library to, to write, um, very succinct code. Things that, you know, I'd have to, uh, wouldn't be succinct and see, but also have to reinvent a lot of stuff because, uh, you almost never find, you know, a, a good set of library, like a, a good total collection of [00:07:30] containers and, and things like that.

[00:07:31] **GLEN FERNANDES:** So it was a very easy language to use. And, um, you know, I, I guess at that time I, I felt it was easy because I didn't know as much as C++ as you know. So everything is easy when, when you don't know that much. But, um, but yeah, you know, I continued doing programming on my own time, uh, all the way up until college.

[00:07:51] **GLEN FERNANDES:** Uh, you know, I did a software engineering degree. Um, and, uh, it was interesting because, you know, the software classes were a breeze. [00:08:00] So I, I spent most of the, you know, my time not attending the lectures and tutorials 'cause I knew I could go for the final exam or do the assessment and get a good grade.

[00:08:08] **GLEN FERNANDES:** And I spend most of my time, um, tailoring my now wife around when, in her classes and, and spending time with her in college. But, uh, while I was in college, I ended up doing a, um, internship with Microsoft in Redmond. So they, they, they came to the college campus and they scouted people and gave us interviews and, you know, they, they, um.[00:08:30] 

[00:08:30] **GLEN FERNANDES:** They like, uh, they, they, they wanted to, you know, give me a shot. So I, I, in, this was in December, 2008, I came to Redmond to do an internship with Microsoft, and, um, they made me an offer at the end of it. So I was graduating, uh, start of 2009, and so I had an open offer, uh, 2009, graduated, uh, my wife. What's that?

[00:08:53] **GLEN FERNANDES:** That open offer? Oh, it was nice. You know, it was, it was nice to know that, um, I mean, I enjoyed working there, [00:09:00] so, you know, I, it was an easy decision for me to say, oh, I would love to, love to go back. Um, and I, I, you know, I, I, I like Redmond, uh, and Washington State in general. And, um, uh, yeah. So, um, graduated.

[00:09:14] **GLEN FERNANDES:** Tell that if I, I'm just curious. Sure. What was your wife studying and what did she ultimately Oh, she, she was doing a, a bachelor of, of Commerce, majoring in finance. We met in our first, uh, so she, she was doing some, um, I said she's, she, she did [00:09:30] a Bachelor of Commerce majoring in finance, but she also did some, um, side courses.

[00:09:34] **GLEN FERNANDES:** And one of the ones she picked was, uh, introduction to Software. Um, so it was a programming course. And, um, uh, that's where we met. We were assigned to the same group of four for the sort of final project. And, um, you know, if, if, uh. The, the way we ended that, that semester, you, you, you'd never think we'd get together because what, what happened was, so [00:10:00] initially, you know, the, the groups, people formed their own groups and then the, uh, lecturer decided, you know, the groups that were formed and didn't have a good distribution of expertise.

[00:10:07] **GLEN FERNANDES:** 'cause you have people who had been programming for years before, and then people who were just learning to program in the course. So that's, that's how the sort of assignment happened. And then we were working on the major project together. Um, and, you know, my, my wife's the kind of person who, who wants to put in work and, and, um, you know, like do things properly.

[00:10:27] **GLEN FERNANDES:** But what happened was, um, [00:10:30] you know, everyone worked on the project together. And then a week before the, um, project was due to be submitted, I did what I planned on doing all along, which was, uh, rewrite the whole thing myself and submitted that. And even though we got a great grade, she wasn't happy about that.

[00:10:46] **GLEN FERNANDES:** So, you know, um, it wasn't until I think a year later that we just happened to meet for other reasons. And then, um, I guess all, you know, um, she didn't hold it against me that I, um, you know, took control of the [00:11:00] project at the very end and, and did it myself. But I think she, she didn't find it interesting enough to pursue herself.

[00:11:06] **GLEN FERNANDES:** Um, but, uh, no, you know, she, she, uh, I think, um, yeah, no, I think I, I think she found it, um, interest, you know, interesting, but just not. Not, not for her. Yeah. So when I was at Microsoft, I was in the online services division, so writing this stuff in the backend that powered things like Bing, um, [00:11:30] initially, and then I moved to a team that worked on, you know, like a, a, a competitor to Proto Buff, um, called the Bond, um, serialization library, and it's corresponding, you know, compiler and code generator.

[00:11:46] **GLEN FERNANDES:** And after that I moved to, um, uh, a different team working on, well, still working on sort of backend services for like, as part of the online services division. But, [00:12:00] um, yeah, I guess that's when I was in that last team. I, I think I already knew I was on the, on the way out. So, um, at that point I was, uh, you know, I think it wasn't long after that that I accepted a job offer at Intel working on, um, software development kits for, uh, mobile devices.

[00:12:20] **GLEN FERNANDES:** I think I just found it, you know, I found it interesting. I think I found it was, you know, better than working on an application, working on, uh, I think [00:12:30] my customers being developers is the thing that, that made all the difference, right? Like rather than writing something for the end user, writing something that, um, different developers could, could use to make their projects better and, and, and make their code faster or simpler.

[00:12:44] **GLEN FERNANDES:** Oh, sure. I mean, you know, um. Most people, so, you know, windows as an operating system has a large use, you know, user base, right? Um, I mean, probably one of the biggest in the desktop space, and most of the code behind that is [00:13:00] C++, right? Um, almost every, uh, application that you would've used in the, you know, um, nineties, up until the early two thousands would probably be written in C++.

[00:13:13] **GLEN FERNANDES:** Today, I guess it, it's shifted because a lot more applications are, are web based and, and, um, but, uh, you know, I would say a good, good page that sort of shows people what, um, the different kinds of things that C++ was used in would was the old [00:13:30] website Boost website page, which, you know, where you had testimonials or, or little blurbs from, um, uh, for various companies using Boost, like Adobe, using Boost in, in Photoshops, you know, so you know that applications like Adobe Photoshop were written in C++, right?

[00:13:46] **GLEN FERNANDES:** Um, the other place that I, I sort of got a big sense of, you know, who's using C++ and, and and, and why is, um, and, and also using Boost is the boost mailing list because you'd see you emails to the [00:14:00] boost mailing list from, uh, you know, some contractor working on, like for Airbus, right? Because you'd see the, like the Airbus thing in the email or like addresses at, at US af dot mill.

[00:14:12] **GLEN FERNANDES:** So people in from the, from the US Air Force, right? Um. Okay. And then obviously working at, at companies like Microsoft, you'd see, oh, boost is being used here. And so, you know, all these different, uh, programs that you might be using. Well, yes, boost is used in the, [00:14:30] you know, um, and, and, and obviously C++ is used in the, the, um, in the back, you know, pride and the, the sense of giving back is, is a big thing, or at least it was for me.

[00:14:40] **GLEN FERNANDES:** Right. Um, it, it, it feels really great to, you know, talk to someone who works at a company and then, you know, they, you find out, oh, they're using, you're using this library, and then you can tell 'em, well, you know, uh, I, you can take a look at the, uh, you know, the, the, uh, headers and then at the start you'll see, you know, copyright Glenn, [00:15:00] Glenn Fernandez and my email address.

[00:15:01] **GLEN FERNANDES:** Right. Like, it's, it's, it, it feels good. Um, but Al yeah, also the idea of, well, if you're benefiting from something, it, it, it feels good to give back. Right? I think that's just intrinsic in people. Um, yeah. So in, in my case, it was in, uh, you know, when I worked at Microsoft, it had a, at, at the time, right? This was Microsoft in between 2009 to say 2014, it was very averse to, um, open source.

[00:15:29] **GLEN FERNANDES:** So [00:15:30] much so, um. You weren't allowed to say contribute to open source in your own time. So all my contributions to to, to open source while I was at Microsoft weren't my 20% project time at Microsoft. 'cause I didn't, um, I, I think we, we could have had 20% project time or something like that to work on things for the company, but, you know, working on open source libraries wouldn't have, um, uh, qualified.

[00:15:53] **GLEN FERNANDES:** So, um, but e even to do that, like, you know, um, contribute to boost on the [00:16:00] weekends and, uh, needed approval. I didn't know this, but fortunately I had a, I had a great manager at the time, a guy called Chad Walters who, who, um, you know, when I expressed a desire to, you know, give back to Boost and, and um, you know, had ideas and things I could invent that could, would be great being, um, part of the library collection, he actually made sure, um, within Microsoft that I had, you know, legal permission to, um, contribute to Boost.

[00:16:24] **GLEN FERNANDES:** And there's an interesting story about this actually. Um, you know, the very first sort [00:16:30] of interaction I'd had with Herb Sutter was while I was working at Microsoft. And it was an email from him. Um, and the email was about, you know, he mentioned, oh, you know, Glenn, you know, um, many people have said you, uh, this is paraphrased, but that, uh, you know, we've been, you've been talking about your contributions to Boost and, you know, I'm sure this is the case, but I just wanna make sure that you have, you know, approval to do this.

[00:16:51] **GLEN FERNANDES:** And I guess what, what had, um. Uh, provoke the email was, you know, in, in sort of these distribution lists we call [00:17:00] them at Microsoft, where people would, um, like, kind of like internal mailing lists, you know, targeted to specific things like C++ or Windows programming. You know, on one of them, I, I was sort of bragging about, oh, you know, well, uh, I've done this and it's in boost.

[00:17:11] **GLEN FERNANDES:** And, um, I guess someone saw that. And, um, you know, I don't know if they, I, they didn't reach out to my manager, but for some reason, I guess they reached out to Herb and they said, you know, there's this guy Glen, who's, who's talking about his contributions to open source. So, um, at, at the time I was, I was really grateful for that manager, um, Chad, [00:17:30] who, who, you know, made shy.

[00:17:31] **GLEN FERNANDES:** I was sort of protected by, by getting, you know, going through the right, um, legal process at Microsoft or for open source contribution. But it sort of gives you the picture about how averse to open source they were, even though they were say, benefiting from it, that an employee would contribute in his own time outside of work was still, you know, um, not a great thing.

[00:17:50] **GLEN FERNANDES:** Yeah. I don't know if it's unique to Microsoft, right? Because, um, maybe a different company that is, was, was more open source friendly at the time, would have a different perspective. [00:18:00] Um, now I, from what I hear, you know, um, long since removed from that scene that, um, you know, Microsoft is very open source friendly.

[00:18:09] **GLEN FERNANDES:** I, but again, it's just, um, secondhand knowledge. I can't, I can't remember his, his actual title. Um, but I know, I know he worked in the, um, developer division and I guess he was a sort of evangelist for, for Microsoft products. And he also participated in the, you know, sq plus plus standards committee at the time.

[00:18:25] **GLEN FERNANDES:** And, and, um, yeah, uh, with contributions to [00:18:30] Boost. Um, the first one was to the Smart Pointers library. I eventually became a co maintainer at the Smart Pointers Library, you know, under Peter Doff, who's probably one of the, the greatest minds I've ever had. The, the pleasure of knowing. Um, I started contributing to a lot more boost libraries.

[00:18:47] **GLEN FERNANDES:** You know, initially was things like adding, um, support for C++ 11 features, like move semantics and, and so on. And then eventually I, I, I became passionate about the C++ allocator model, so it was adding make, [00:19:00] making more boost libraries, allocator aware and supporting the C++ allocator model.

[00:19:04] **GLEN FERNANDES:** Um, in 2014, I, I think I, I wrote, it was either 13 or 14, 14 where I wrote my first Boost library, which was Boost Outta line. Um, and then, you know, I think it just sort of continued from there. I became the maintainer of more libraries, contributed to more libraries, but besides the code contribution part, um, you know, I participated in Boost, uh, formal reviews as a [00:19:30] reviewer initially.

[00:19:31] **GLEN FERNANDES:** And then at one point I was the, uh, review manager for, um, a, a review. And then I, I think I managed, um, a few more reviews after that. Um. And then I joined the, what was then the Boost Steering Committee, uh, which was the, you know, organization that managed Boost assets and, and things like that. Uh, eventually the steering committee reformed as a, uh, nonprofit organization, the Boost Foundation.

[00:19:59] **GLEN FERNANDES:** [00:20:00] So I went from, you know, being a member of the steering committee to being a director in the, in the Boost Foundation. Um, and then some point throughout all that history, I also became a Boost Release manager. So alongside, you know, Marshall Cloud and Michael Case, um, and, um, now Young, um, you know, uh, looking after the, the boost release process and, um, I'm not sorry, I, I didn't join the fiscal, um, sponsorship [00:20:30] committee when it was formed, you know, that was formed very recently.

[00:20:33] **GLEN FERNANDES:** Um, and then the Boost Foundation handed over the assets to that, uh, organization. Um, I did manage the, the, the formal review in which, uh, the committee, uh, sorry, the community essentially voted for, um, the, um, fiscal sponsorship com, uh, committee under the C++ Alliance. Um, they, in, in, in that review, I was asked to join the, um, [00:21:00] the, uh.

[00:21:01] **GLEN FERNANDES:** The, the FSC and I declined only because, you know, I felt it wasn't right. Being the person who, the arbiter who gets to decide at the end based on the results of the, you know, um, based on the, the contributions and the review, which way things go to, to also accept a position on the, on the committee, which I was going to decide upon.

[00:21:19] **GLEN FERNANDES:** Right. Um, but, uh, for the C++ Alliance, I, I, um, you know, I was never a paid employee. I, I [00:21:30] always volunteered my time, um, and it was, I think my title was technical consultant, so I, I, I basically provided advice to Vinny about I, you know, projects, ideas, um, hiring decisions and things like that. But it was, was, um, just out of a desire to help Vinny, Peter Mov, um, is the, you know, author of many Great Boost Libraries, the contributor to almost, I would say, you know, probably 80% or [00:22:00] more of the Boost Libraries at this point.

[00:22:02] **GLEN FERNANDES:** Um, I, I met him when I was contributing to Boost Smart Pointer, right? Which is, um, the, uh, uh, the library he's most famous for, I guess, or, or was most famous for now. He's got some really great libraries that, uh, people know about. But, um, uh, you know, he, he's, I would say right now he's the, the rock that that.

[00:22:27] **GLEN FERNANDES:** Boost stands upon, you know, like, uh, boost has a [00:22:30] lot of contributors, but there are some people that, you know, have, um, tirelessly been there from the start, um, and, and, and, um, still today, you know, put in hours of work to just make Boost. Great. And he's one of them, you know, besides his effort, he, he's also, he's, he's brilliant.

[00:22:48] **GLEN FERNANDES:** You know, I've never met, uh, I've never met anyone like him in my life. And, uh, um, I, I think it's just an honor to know him and, uh, um, like my life is [00:23:00] enriched just, just by having met him. Right. And, and, um, so, and, and you actually have, he's a mysterious figure, you know? Um, he, mysterious his personal life is mysterious, right?

[00:23:12] **GLEN FERNANDES:** His, um, his public life in, in, in the way of the Standards committee. And the, and Boost is, is really well, uh, known, I think. Um, so I mentioned, you know, we mentioned not being able to talk to Beman, right? But, so I, I met Beman, um, at a C++ committee meeting, and [00:23:30] I had the opportunity to sit with him at breakfast, you know, before sort of the, the, the day started and people went off into their groups and it was a, it was a table, you know, there were a bunch of tables and Beman was at the table.

[00:23:40] **GLEN FERNANDES:** I was at, um, as well, along with a few other people. And what was interesting was, you know, when I mentioned I, I, uh, uh. Boost Library author, you know, he started talking about Boost and one of the things that he talked at length about at the table, um, you know, that I, and, and everyone else were, were, uh, got to hear was, was about, [00:24:00] uh, Pete of and, and, um, you know, uh, how he took over the smart point as the library and, uh, you know, in some sense how, how great he was.

[00:24:09] **GLEN FERNANDES:** And, and then, um, you know, it was just this, uh, uh, sort of surreal experience for me, right? Like, here's Biman DA's a, a legend in his own right talking about Peter Dema, the person who I probably had the most respect for in the world. Um, but, uh, yeah, so [00:24:30] it, it's hard to, um, find anything in, in C++ standardization without running into Peter's name somewhere.

[00:24:38] **GLEN FERNANDES:** I think his, his, yeah. Smart pointers are, uh, you know, a collection of RAI types resource acquisition is, is initialization types where, um, which take care of memory management in the way that, um, they, they free memory upon destruction. So it, it, uh, makes it very easy to write code that doesn't leak or is, you know, exception, safe, [00:25:00] and, uh, because.

[00:25:01] **GLEN FERNANDES:** Uh, you know, the owning type takes care of the, the, um, cleanup, you know, boost Smart Pointers gain notoriety because it was, it was really well designed. You know, I mean, many people would've invented say, you know, owning pointer types, whether they were, uh, shared pointers or unique pointers. But, um, uh, but you, and, and Boost Smart Pointers has a collection of them, right?

[00:25:20] **GLEN FERNANDES:** It has Scope pointer, share Pointer, but it was Boost Shared Pointer that was, um, I guess really well designed and to the point where it, it fit the needs [00:25:30] of almost everyone, right? When they needed a reference counted. Um, you know, sharing semantics, uh, smart Pointer Boost Share Pointer just worked. Uh, you know, Peter ov, uh, I guess you could say he was responsible for both the design aspects of it as well as, you know, really great quality of implementation.

[00:25:53] **GLEN FERNANDES:** You know, it was optimal. It, it worked really well. Um, and, uh, [00:26:00] it, it was also, I guess the dedication to it, right? Like he would con constantly, um, improve it and, and so on. So much so that, uh, you know, people say, well, smart Part Boost Share Pointer became STD SharePoint, or when C++ 11 was, was, um, adopted, right?

[00:26:18] **GLEN FERNANDES:** So it, it was now part of the C++ standard library, but Boost Shared, you know, the Boost Smart Pointers Library and, and SharePoint as well sort of evolved past that. Um. [00:26:30] You know, we, we made changes to, um, share pointer that later, um, became part of C++ 17, and then C++ 20. And, you know, there are, there still things in, in Boost Smart pointer like Boost Local Share Pointer where, where the reference count, you know, is, um, is non atomic that isn't yet in the standard, you know, so, uh, it's, it's one of those things where, uh, it really shows, you know, his prowess and, and, um, his, uh, and how great Boost is.

[00:26:59] **GLEN FERNANDES:** I, I would say for me, [00:27:00] MP 11, you know, he, he's, he's done some, uh, great things since that. Right? Um, you know, a lot of people like Lambda too and, and describe and, but, um, to me, MP 11 was, was a, um, probably the, you know, if you need everyone read, everyone who writes library code then eventually decides to, you know, um, leverage template meta programming to make library code, um, more concise and, and, and more generic, um, w would, would see, would seek a meta [00:27:30] programming library.

[00:27:30] **GLEN FERNANDES:** And I would say Boost at MP 11 for the most part, just fits the bill for everyone. It, it, um, uh, it's, it's a, it's a great library. Um, you know, at one point I even had hopes for it going into the, into the standard. Obviously it, it, it, it didn't. Um, and, and now with, um, you know. With reflection in C++ 26, um, I don't know how many people still see that need to have, you know, a library like MP 11 as part of the standard library.

[00:27:58] **GLEN FERNANDES:** But, um, for all [00:28:00] those of us who are still, you know, live in the C++ 11 to, um, 17 world, you know, MP 11 is, is fantastic. I do have one contribution to MP 11. So if you open up, I guess one of the, uh, headers you'll see, uh, MP 11 starts with. So that meta function was contributed by me. Um, right. Yeah, I mean, there have been a lot of great people in booths that, you know, have, have worked on libraries that are, um, uh, you know, instrumental [00:28:30] in, in, in so many projects.

[00:28:31] **GLEN FERNANDES:** Like, you know, John Maddock, um, worked on RegX and RegX was so great that, you know, um, everyone wants RegX in some way, in some programming language, right? So C++ 11 has STD RegX, which was basically based on a proposal, largely defined by, by Boost RegX. Um, but John Madock also, you know, even though.

[00:28:49] **GLEN FERNANDES:** Um, I've never, you know, been a user of Boost regex in any of the libraries or, or projects I've worked on, you know, his other libraries like, um, boost at config and boost at type traits [00:29:00] were, were fantastic, right? Um, booster config, basically providing, um, macros were feature detection before C++ had feature detection macros, which again, you need as a library writer because you, you really, you, you want to cover as many, uh, compilers and platforms as possible and, you know, um, ultimately you need workarounds 'cause nobody, um, has, you know, perfect implementations of the language or library.

[00:29:24] **GLEN FERNANDES:** Um, so that's where boost config came in, boost our type traits, again, for, for things like template meta programming, [00:29:30] right? Um, a lot of those type traits, uh, are now in C++, um, 11, and then some in later standards. I think the last two type traits that I contributed to boost type traits, that made it into probably C++ 20.

[00:29:47] **GLEN FERNANDES:** Um, yeah. But again, again, you know, libraries that are, are, are really useful. So, so John Maddock is this other person in Boost that I have a, a lot of [00:30:00] respect for, um, another old timer who's been there, um, since the beginning and then still somehow it's time today to, you know, participate and contribute.

[00:30:08] **GLEN FERNANDES:** Sure. So this is interesting. Um, you know, John Kab, uh, was the chair of the steering committee, but by the time I joined the Boost Steering Committee, you know, a. There were, I, there were very few developers, boost developers there. So, you know, there were people that were still contributing to boost by, um, uh, you know, managing [00:30:30] like the assets, right?

[00:30:30] **GLEN FERNANDES:** Like the, the domain and things like that. Or they, they had a big part in the, um, uh, C++ conference, which was, um, C++, uh, now formerly Boost Con. Um, so at one point, I think it was you, the library developers or library authors in, in, in the steering committee. And, and then the Boost Foundation were basically Peter Dav and myself.

[00:30:57] **GLEN FERNANDES:** So I guess I wasn't part of the steering committee [00:31:00] when it would, would've been, would've consisted mostly of, of Boost, boost developers. Um, you know, John Kab is a, is is a great guy. You know, he, he's, he, he worked tirelessly on the C++ conference and, and that conference has benefited, you know, um, hundreds and hundreds of C++ developers.

[00:31:17] **GLEN FERNANDES:** Um, I came to know John, you know, from his work on the conference as well as his, you know, participation in the, and chairing of the, um, the, the, the steering committee. Um, I know as a profession, [00:31:30] John, uh, you know, uh, was a teacher and he, he, um, uh, I guess, um, ran courses on, on C++, uh. You know, his, his story in the, in the as part, you know, he, he, he had great sort of, um, visions for, uh, or had a great vision of, of what he wanted the, um, steering committee to become, right?

[00:31:52] **GLEN FERNANDES:** He, he, he was the one who decided to, um, form the nonprofit. Um, and, you know, he wanted to use the, [00:32:00] the sort of, sort of the money that the organization was earning from, uh, you know, from the conference to benefit C++ in, in a big way. So, you know, that that's, that was the intention. It was a great intention.

[00:32:12] **GLEN FERNANDES:** Um, you know, his story, uh, in the, in the foundation. Um, it, it didn't have such a great ending because, um, you know, he, um, resigned or essentially [00:32:30] was felt, uh, was made to, was forced to, was, yeah. I, I, I don't know how to say this actually, you know, um, because I'm not entirely sure how it was communicated to John, whether he felt like he had to resign or, um, but, um, you know, because of various issues that, that came up, uh, in the foundation over, um, the handling of, um, an individual who, um, [00:33:00] uh.

[00:33:03] **GLEN FERNANDES:** How, how, how candid can I be here, you know, and, and not worry about Well, 

[00:33:06] **RAY NOWOSIELSKI:** I always encourage full candid, it doesn't mean we use it all 

[00:33:09] **GLEN FERNANDES:** will tell it to us. Sure, yeah. Because, you know, maybe after discussion with nie, we might decide not to, um, include certain pieces of this Exactly. That can always be 

[00:33:17] **RAY NOWOSIELSKI:** decided 

[00:33:18] **GLEN FERNANDES:** in the edit room.

[00:33:18] **GLEN FERNANDES:** Sure. Okay. So, um, you know, John was essentially made to resign, um, over his, [00:33:30] including Arthur O'Dwyer in something in, you know, related to the C++ now conference. Right. That, that was my understanding of it. Arthur o' Dwyer was this individual who, um, you know, people Googled and found out he had a, a, a, a record.

[00:33:45] **GLEN FERNANDES:** Um, he was charged and then, um, you know, um, released at some point on. Um, but, uh, you know, he, uh, it started this, this sort of uproar and in various commun, [00:34:00] you know, C++ communities where people were asking for him to be banned from attending the conferences. And, you know, John, the, the

[00:34:14] **GLEN FERNANDES:** issue that, um, with John's handling of things was that he knew about Arthur's background but didn't disclose it. And, um, that was turned into something that, um, you know, um, it was, it, it, it became a big [00:34:30] thing and. At, at some point a a a com, a foundation meeting was held where John was, um, supposed to be a part of, you know, to present his side.

[00:34:41] **GLEN FERNANDES:** And when, when I talked to John, you know, um, the, the, the meeting was rescheduled and, and when I talked to John, it, it turned out that he wasn't, he wasn't made aware that the meeting was rescheduled. So he, he didn't have a chance to actually go in and tell people his side of things. So he, um, you know, my understanding is John felt like he was, um, [00:35:00] given the short end of the stick, that, that, you know, that, um, you know, I, you know, it's, it's not possible for me to say that the person did that deliberately or, you know, um, uh, or that he didn't try to make John aware of the, the rescheduling.

[00:35:14] **GLEN FERNANDES:** But, um, da David Sanko is the, per the person who, you know, um, uh, was running, contacted all of us and, and asked us to, you know, um, be part of this, this, this meeting. So you, at the meeting? Uh, yes. Yeah, I, I, I do. What do you 

[00:35:29] **RAY NOWOSIELSKI:** remember [00:35:30] being presented there? 

[00:35:32] **GLEN FERNANDES:** Um, it, it basically painted a picture of, um, you know, John being derelict in, in his duty where whereas, you know, he should have actually made it clear that he, you know, um, to people that he was, uh, like what, what Arthur's background was, right?

[00:35:52] **GLEN FERNANDES:** Like, that he did have this criminal history, um, because Arthur disclosed it to John and, um, John made the. [00:36:00] In the meeting, it, it was presented that John made the conscious decision that to, um, to hide it. Um, I don't, I I don't even remember if it was booking him to speak or including him as part of some committee or, you know, conference committee or something, like being part of the, the team of the conferences.

[00:36:15] **GLEN FERNANDES:** That, that's what I seem to recall the, the, uh, the deal with Arthur was. But, um, because I never paid too much, uh, attention to, um, the conference side of things at the time, I wasn't aware of the, uh, you know, [00:36:30] uh, what that duration was. I do know that the way it came up, like people I found out was, um, you know, someone asked John, uh, if he knew about it and he, and he said, yes, I did know about it.

[00:36:42] **GLEN FERNANDES:** And, you know, so it was clear that he, he knew and, and, and, uh, hadn't said anything. Um, and I think John told, told that person that Arthur was the one who actually came forward and said, oh, you know, you are including me in this thing. Um, but just to be aware, I have this, this, um, this background. [00:37:00] So almost nothing because I think you know, it, if you, if I remember correctly, the only thing that would've, um, you would've, the outside people would've seen on the, on the boost list is, you know, something from John saying he's resigned or something.

[00:37:16] **GLEN FERNANDES:** May maybe David posted saying John had resigned. But, um, oh, the DWI thing became a big deal in, I like, you know, I said in, in various. Places like there were posts on Reddit and, you know, uh, arguments about whether, [00:37:30] um, you know, he should be able to attend the standards committee meetings. And, you know, ultimately it was decided, well, you know, as long as he's a member of i, of the, um, the US National body, you know, um, he, he's, he, he should be able to attend.

[00:37:44] **GLEN FERNANDES:** But there were, you know, people in various, um, uh, places, uh, strongly opposed to that, you know, like, um, very upset that Arthur o' Dwyer would, would be able to attend the, uh, committee meetings or, yeah, I think maybe, you know, in hindsight, I [00:38:00] think too many things happened too quickly without having, without people getting a chance to, to speak and, and hear everyone, you know, I think, I think maybe if we, um, you know, had a, had, uh, gave on, uh, the opportunity to sort of present his case to the whole, um, board, we might've taken a, a, a different turn.

[00:38:21] **GLEN FERNANDES:** Um, and I, and, and you know, that only became clear to me later after talking to John, you know, outside and then to sort of hear [00:38:30] that, um, you know, what I thought the sequence of events were, were, were, were, were, were not the case at all? Um, no. No, not really. I think, you know, I, I, I do feel, I do feel bad for John.

[00:38:41] **GLEN FERNANDES:** Um, but, and I, I, I, I don't, you know, I, I'm not, uh, opposed to talking about it, but I, it, it's also, um, it's, it's a little tricky to, to, uh. To talk about without, you know, falling into the, the pit of, of, of blaming someone, right? Like, um, [00:39:00] with that. Yeah. And yeah, ideally, you know, we could keep all this stuff out of, out of boost, right?

[00:39:06] **GLEN FERNANDES:** Um, and, and my position is look, um, everyone should be able to contribute to, to boost. Um, I remember hearing, you know, not so long ago that certain, um, you know, in, in one open source project, certain maintainers were removed just be by virtue of them being from, um, from Russia, right? And, you know, we would never do something like that in boost, right?

[00:39:28] **GLEN FERNANDES:** Uh, whether [00:39:30] you're Arthur o' Dwyer, whatever your, your background is, it doesn't affect your, you know, the, the fact that you're contributing C++ code to boost. Nothing else should matter there. Um, so, so, you know, obviously I, I, the conference is, is another side of things where people, um, have a better idea of what, what is right there for the, for the conference.

[00:39:50] **GLEN FERNANDES:** And, and, and there I kind of defer to their judgment, right? Because it's, it's a, it's a different ball game. It, it's people meeting together and, and who knows what, what the right, [00:40:00] um, requirements are for, you know, um, for either for, um, people to be okay with attending or as well as for not lose business, right?

[00:40:07] **GLEN FERNANDES:** Sometimes it's just a business decision. You, you say, um, uh, we have to, um, make this call because otherwise we, we, uh, the conference will, will falter, but um. You know, whether it's issues like this or, you know, at one point in time there was this idea of boost being part of this thing called Outreachy. And the, the, the majority, the [00:40:30] consensus, you know, um, from the Boost community was, um, you know, we outreachy is, is might be great and it has, you know, noble goals, but to some extent it's, um, you know, it's, uh, discrimination in its own form, right?

[00:40:47] **GLEN FERNANDES:** Like even if you're giving special treatment to some, uh, uh, minority classes or, or, you know, um, and, and Boost is not about, you know, the Boost Library, um, side of things is not about that. You know, ev everyone [00:41:00] is, is, is welcome here. So I think even that was, you know, speaks to, to boost being sort of neutral to social and, and, and political issues, right?

[00:41:09] **GLEN FERNANDES:** Like I, and that's one of the things I think is, is great about it. Describe, I think that's the perfect word for it. And meritocracy, you know, boost is merit based. Um, you know, Vinny likes to, to throw around this phrase that, you know, more people have gone to space than have gotten the library into Boost, right?

[00:41:25] **GLEN FERNANDES:** And, um, but it, it's, it's not because of artificial restrictions and, [00:41:30] and, and people who get their libraries in, it's not because they're, um, they have some background. It's just because the, the code pass passes formal review, right? Mostly pay the bills is what, is what the foundation would do, right? Like keep, keep things running in that sense.

[00:41:44] **GLEN FERNANDES:** Um, yes, there were a lot of, uh. You know, good intentions and ideas, right? And one of my sort of reasons for continuing to be part of the foundation at the time when, when, when the foundation was forming was I thought, oh, well, you know, one of the things we, you know, one of the [00:42:00] ideas that we, we could realize is, um, helping boost by providing continuous integration or, or, you know, um, uh, maybe paying for a better website, but for, you know, um, all the good ideas and intentions, the, the foundation.

[00:42:16] **GLEN FERNANDES:** You know, we, we never ended up doing those things for Boost. Um, but, you know, we kept the lights on, but even there, there were, you know, there were certain things that it, we, we couldn't do. Um, [00:42:30] you know, at one point, boost downloads hit 60 terabytes a month, and then, um, you know, we had to move from, um, I think it was bin traded Jfr, because they were the only ones able to, to support our, our downloads for free.

[00:42:43] **GLEN FERNANDES:** At towards the end of that, you know, our downloads started hitting 200 terabytes per month, and even they couldn't afford to, you know, um, you know, let us stay on for free. So they, they talked to us about, you know, getting a, um, uh, um, what, [00:43:00] what's the, I, I've forgotten the, uh, phrase here. Um,

[00:43:08] **GLEN FERNANDES:** but essentially we, we needed a, um, uh, we, we need. Caching, uh, in front of, of the downloads, right? So, uh, you know, they, they recommended a bunch of vendors and we talked to, I, I went out on, on to, on behalf of the foundation to talk to each one of them to, to see what deal I could get for Boost. And the best deal we got was from Fastly.

[00:43:28] **GLEN FERNANDES:** Um, [00:43:30] and, uh, even that was, you know, too expensive for the foundation to pay. So it was, it was Vinny and the C++ Alliance there that that sort of came into, you know, foot the bill to keep, keep Boost alive. So, you know, I, I say we, we paid the bills except for those bills that were too expensive to pay.

[00:43:47] **GLEN FERNANDES:** Um, now, even though that might sound, um, you know, it may, may, might make the foundation sound like it doesn't do that much for Boost. Um, that's just the Boost Libraries, right? [00:44:00] Because it, it would do a lot of things for the, for the conference and, and, and, um, various other things. Which conference? Uh, C++ no supporting Boost, right?

[00:44:09] **GLEN FERNANDES:** Because if it wasn't for the Alliance, we wouldn't have downloads. And without downloads you don't have Boost. Um, but, uh, you know, the biggest thing, um, the, you know, the Alliance has done is, has give us, uh, a new website, right? Which is, um, something that everyone has been [00:44:30] asking for, for, for years. I mean, I remember in 2000 and, uh.

[00:44:35] **GLEN FERNANDES:** 13, you know, we, we had complaints and, and about, oh, you know, people are trying to read the website on, on a, on a mobile device, and it doesn't, you know, automatically adjust font sizes and things. But e even in 2013, the, the look of the website was, was fairly dated, right? It, it looked like a 2000 era, uh, website.

[00:44:53] **GLEN FERNANDES:** Um, and, uh, again, it was something that, you know, we never got to do it through the Boost Foundation [00:45:00] funding it. But, um, you know, Winnie, Winnie, um, stepped up and, and like so many things in Boost, right? Um, if, if it came down to sort of just community consensus, you wouldn't get anywhere. But it, a lot of things just happened because one or two people say, let's, let's do the work and, and let's, you know, uh, let's make this a, a reality.

[00:45:19] **GLEN FERNANDES:** Like CENIC was one thing, you know, people kept asking for, uh, CENIC support. And at one point in time, you know, the Boost Steering committee, um, declare this is before I joined, declared, oh, [00:45:30] boost is moving to CENIC without any plan of moving to cec. Just a, um, you know, a sort of blanket statement, which a annoyed a lot of contributors made one threaten to, well, he did leave and then come back.

[00:45:41] **GLEN FERNANDES:** Renee. Renee. Yeah, exactly. Um, but again, you know, boost has CEC now, right? And, and it was basically because one person, Peter Dema said, I'm, I'm gonna start making, you know, adding CENIC support. And so, um, so Vinny with the website was, was was like that, right? Like he, he just. [00:46:00] Said, I'm gonna, I'm gonna put in the effort and build it, and then let the com, uh, after it's built, let the community opine and, and we can change it and, and evolve it.

[00:46:09] **GLEN FERNANDES:** And now we have the, the new website, which is, which is, um, yeah. Great. I mean, to me it's, uh, I and I, yeah. I think it's just a testament to boost being unique in, in, in that way. I know it's hard to define that uniqueness because there are so many open source projects and many successful ones too, that, that, that, um, and, and maybe what Boost [00:46:30] has, uh, what, what makes Boost successful is, is the same thing that, that keeps those open source projects successful.

[00:46:35] **GLEN FERNANDES:** But, um, you know, it's this, it's this idea that nobody owns anything, right? You know? Um, yes, uh, we have someone paying the bills, but they don't, they don't decide what, uh, what happens in Boost. Right? Um, it's, it's, it's this idea that, you know, things organically work, um, and, and come together because of consensus or things work because [00:47:00] people are willing to put in the effort.

[00:47:01] **GLEN FERNANDES:** But there's, it's almost like, you know, you, you, you can't shut that down, right? Like, um, you know, I mean, let's say, let's say we didn't have, um, tarball downloads. We, we maybe we, we moved to using, leveraging GitHub for the releases and, and then, uh, using the storage there, right? Or, or changing the model and, and then just, um, you know.

[00:47:23] **GLEN FERNANDES:** Scripts that people would run that would generate a boost distribution from the, you know, tagged, um, uh, git repositories [00:47:30] on GitHub. But it, it's, it's one of those things where, you know, boost has gone through, uh, you know, direction change in, in, in its in, its like, um, in its goals. It's, um, survived, you know, key founders leaving and it's still sort of picked up speed at, at some point and, and started thriving after that.

[00:47:53] **GLEN FERNANDES:** Um, it, it, it, you know, went through a shift in like, uh, you know, subversion to, to, to [00:48:00] to, uh, not just gi, but GitHub, um, a trend towards modular Boost, you know, things that, um, yeah, it, it's, it's survived a lot and, and it, um, I think it's just a, it is just great that it, it keeps going, you know, that people are still invested in, I, I think it's, I, you know, I think it's the, you know, the, the community, the, the fact that you have a lot of interested people, um, opining on, um, [00:48:30] you know, what, what things should be.

[00:48:31] **GLEN FERNANDES:** And if things aren't, you know, perfect in some way, you know, they, they, they would, um, they would either con contribute to try and make it perfect or, or, you know, yell about things on the mailing list or, you know, um, and, and so I think Boost has a lot of key, great key ingredients, right? First of all, it has this license, which is amazing.

[00:48:50] **GLEN FERNANDES:** Right. Uh, the, the Boost license is something that, uh, uh, makes it so easy to adopt, uh, boost in, in, uh, commercial organizations. Um, [00:49:00] you know, there, there were times where, uh, uh, a standard library maintainer would say, well, if it's under the Boost license, then we can use it, right? And, and this is, you know, using parts of Boost to benefit their own, improve their own standard library, or as a test bed for their standard library implementation.

[00:49:15] **GLEN FERNANDES:** Um, so the boost license is great. The boost formal review process is also great. Um, you know, it, it's like the,

[00:49:25] **GLEN FERNANDES:** you know, you have a a period of, of 10 days where, um, you know, [00:49:30] everyone who has an opinion on things, um, gets to voice it. And, and some of them have gotten quite heated and, and, you know, looking back on it, you know, a lot of those heated discussions were actually really great for the library author, right?

[00:49:41] **GLEN FERNANDES:** Libraries can get rejected and people, you know, um, take that as a sign. Oh, you know, it's, it's a rejection. Doesn't mean the end. I'm gonna, you know, you know, work on it and, and come back for a second round of review, right? We've had libraries that, that failed and got in on, on a, on another review. Um, 

[00:49:59] **RAY NOWOSIELSKI:** so battles and [00:50:00] arguments can be 

[00:50:00] **GLEN FERNANDES:** a good thing.

[00:50:01] **GLEN FERNANDES:** Absolutely. Yeah. Um, and then the other thing is, is freedoms as well. So, you know, once you're a library author or you're a maintainer of a library, you know, you, you, you, you can, um. S define what C++ language standard, you want your library to, um, you know, to, to support and what, what, what support you wanna drop.

[00:50:21] **GLEN FERNANDES:** But the other thing that's great is, you know, um, I don't know how boosters achieved this, but library authors have, have prioritized [00:50:30] portability, right? Even though the requirement for boost is only is, is, is quite literally has to compile on two, uh, uh, major compiler vendor implementations. Uh, the majority of Boost library authors, um, will, you know, when they get a bug report or if they find out that, you know, a particular implementation has this cork that they need to work around, or, um, you know, they, they would do, uh, they would make the extra effort of, of, um, oh, I'm gonna act conditional [00:51:00] compilation here, detect this, this vendor's implementation and, and have this work around.

[00:51:04] **GLEN FERNANDES:** Um, and, and, um, maybe it's just culture that sort of spreads, you know, like as you're a part of the community, you sort of see that's the, the, um, you know, Peter deem of, uh, wants his libraries to be production grade. So, you know, uh, I, I should too, right? I should care about the, the end user and, and not break them or, or make sure that if, you know, I can cover these, these extra implementations and, and so on so [00:51:30] way around.

[00:51:30] **GLEN FERNANDES:** Sure, sure. Yeah. I mean, you know, when I, um, when my library went through formal review, I remember, um. Yeah, I just remember it was, it was very intense. It was one of those things where, um, you know, I would, uh, log on, uh, check my email at, uh, you know, like two in the morning just to see if someone else posted a, a comment like, is someone else saying something, something, something bad that I have to refute?

[00:51:53] **GLEN FERNANDES:** Or, you know, like, or, or, or do they actually have a point and you, you know, maybe I need to tell 'em, look, I, this is, this, this is [00:52:00] correct and I'm gonna make this change to my library. And, and, and, you know, uh, I had both, right? I had, uh, people who said something and I had to point out, no, this is wrong. But also people who made like very useful suggestions.

[00:52:12] **GLEN FERNANDES:** And I realized, oh, you know, yes, you know, I should have, um, you know, the documentation really is terrible. Your, or really, you know, I shouldn't call this unqualified, right? Because it's subject to a DLI really should prefix this with the, with the namespace there. And, and I would, I would say, yes, I've made this change on this developed branch.

[00:52:27] **GLEN FERNANDES:** And, you know, um, uh, [00:52:30] hopefully, you know, so that there are follow up, uh, review, you know, review, comment would say, yes, it's a, it's an accept or conditional accept. I know Glen makes this change. Um, so does 

[00:52:40] **RAY NOWOSIELSKI:** your library make it through on the first round? 

[00:52:42] **GLEN FERNANDES:** Yes. I only went through one formal review, the, the, the 10 day period.

[00:52:45] **GLEN FERNANDES:** And, um, is 

[00:52:46] **RAY NOWOSIELSKI:** that common? How common is, is that versus not? 

[00:52:48] **GLEN FERNANDES:** No, I think that's, that's the more common cases as far as I've seen. You know, um, it's been less common that a library gets, I mean, um, that gets rejected and then the author comes back, um, you know, um, for, for another round. [00:53:00] Um, there have been some cases where the library has rejected and the author has decided not to, you know, um, not to pursue Boost again.

[00:53:06] **GLEN FERNANDES:** Um, there've been cases where, uh, someone had people where people have not participated in the review process 'cause they feel it's too much effort and, um. Hive is an interesting, uh, uh, example of that because I remember, you know, I'm credited in, in the paper for, for Hive because I, uh, you know, I, I I really wanted to [00:53:30] help Matt, um, you know, get his library up to, uh, what I would believe is S Plus was Standard Library Quality or Boost Quality, right.

[00:53:36] **GLEN FERNANDES:** Is that Calabrese? No, this is, uh, Matt Bentley, who's the author of Hype. And um, so I think he credits Jan and myself in, in his, in his paper that proposed Hi for the Standard. And it's because we offered a lot of advice to him on how to make things allocator aware and, and, and, you know, deal with allocator traits that, uh, at least, sorry.

[00:53:55] **GLEN FERNANDES:** That's what I was helping him with. And Jan was probably helping him with some other stuff because Jan is the author of, [00:54:00] you know, boost Our Container and, and, um, he's the expert on containers. Right. Um, but I remember at the time he, you know, his plan was to go through Boost, formal review, get it into Boost, right.

[00:54:10] **GLEN FERNANDES:** Also as a vehicle for getting into the standard, because even up until, you know, um, I would say 2020, you know, you, uh, we would still have this notion of well, you're trying to propose something for the standard, you know, why don't you put it in Boost first because it needs like actual real world experience.

[00:54:25] **GLEN FERNANDES:** Right. Um, and all of my contributions to the standard have always gone [00:54:30] through, through Boost. Like there's always been some implementation in Boost. Um, but at some point he dropped out of that, like, you know, he, he, he said like, you know, this, you know, the, the requirements are too, too much or, or something.

[00:54:41] **GLEN FERNANDES:** I can't remember what it was, but you know, he, he, uh, decided not to pursue getting his library through Boost. Because he decided to, to go through the standardization track instead. And, and at one point, you know, I don't forget, it was, if it was him or someone else made, made a post on the mailing list saying, well, [00:55:00] you know, look, this is what's, you know, what's so, you know, um, rough about the boost, formal review process, right?

[00:55:06] **GLEN FERNANDES:** Like, uh, it's, it's hard enough that people might, it's easier to get into the standard. Like it's, you know, I spent this many months on the loose form reports, but I, you know, I think this Hive is gonna, or whatever was called before Hive, 'cause it was renamed at some point, would get into the next standard.

[00:55:22] **GLEN FERNANDES:** Now, you know, that didn't age too well because that email was probably, you know, more 10 years ago at this point. So, you know, hive [00:55:30] didn't get in, um, into the standard within a year. It still isn't, you know, fully, um, adopted in the standard, or unless it is for c plus was 26. That part, um, I'm not clear about.

[00:55:42] **GLEN FERNANDES:** Um, I haven't been following too closely, um, in the last, uh, year. Um, so yeah, our research shows it's pending for 26. Pending for 26. Okay. Yeah. Um, so it's been, you know, it, it turned out to be even, even longer, right? I, I, I personally, I, I think the right call [00:56:00] would've been to get it into Boost because, um, getting the real world users through Boost would've been much more beneficial, um, than, you know, I, I know he has users, but again, boost would open 'em up to, um.

[00:56:13] **GLEN FERNANDES:** Uh, one order of magnitude users, but you know, more so, so I think, what's the most heated, uh, moment that jumps outta you from a review outsource? Uh, it would be, I think it was e it was definitely, um, uh, one of Vladimir BOVs, uh, [00:56:30] libraries. I think it was Boost Conversion, and it was a, it was sparring on the list, you know, um, between him and, and Rob Stewart.

[00:56:38] **GLEN FERNANDES:** Um, and, and I forget if, if that one ended with, you know, some, a amicable, um, uh, uh, closure or something. But, uh, I remember there, their things got, you know, um, fairly heated. I, I forget if insults were thrown, but, um, yeah, again, it was, it's called the 

[00:56:56] **RAY NOWOSIELSKI:** Bone of Contention there. 

[00:56:59] **GLEN FERNANDES:** Yeah, it was [00:57:00] all technical. I mean, the content, you know, but, um, I, I forget what the actual, um, the, the, the disagreement was.

[00:57:06] **GLEN FERNANDES:** Um, yeah. But, but I think a later form of his lie, we did manage to get in, I think it was conversion or boost, stop, convert. But yeah, for me it was, I worked on my library because I felt it would be useful library. Um, and, uh, you know, I had one person who was the motivating reason for me writing it. Um, and, you know, being a boost contributor, it was only natural for me to think, you know, I'd, [00:57:30] I'd like to try to get this into boost, right?

[00:57:32] **GLEN FERNANDES:** So I, I post it to the, um, to the mailing list, you know? Um. Asking for, for feedback, saying, look, I had this library. I'd like to, um, I'd like to propose it for Boost. And I got a lot of feedback that, you know, that helped me improve the library. But also, um, uh, affirmation, you know, that people felt it would be useful not just for end users, but for Boost Library authors to use some of those pieces.

[00:57:52] **GLEN FERNANDES:** Right. Um, and uh, at that point though, scheduling the review was, was, [00:58:00] it was, um, interesting because there was this period where sort of boost activity had, had, had, had died down a lot. I think it was, you know, towards the, um, tail end of 2013, in two th 2014. So it was a long period before the last library got accepted or something.

[00:58:16] **GLEN FERNANDES:** And I remember someone actually, you know, um, saying to me, well, uh, uh, I don't even know if you're gonna find a review manager, uh, for this library. 'cause it doesn't look like there are, you know, there, there, there's the boost review schedule queue, which [00:58:30] had a bunch of pe, you know, libraries in there where people were looking for a review manager and, and, and so on.

[00:58:34] **GLEN FERNANDES:** Um, but, uh, no, someone did volunteer to be a review. Someone, it was a guy who used to work at Microsoft, then he wanted to work for Amazon. Um, and so I was very happy for that. So the, the, the, you know, it, it went to being on the boost review queue and then with the Boost Review manager, um, the review wizards who, who, who do deal with the scheduling, you know, um, asked us for a date.

[00:58:57] **GLEN FERNANDES:** We picked a, a 10 day period [00:59:00] and, uh, the, the review was scheduled, so then it was on me to make. To, to do the best job I could to make sure people participated in the review. So it was a, you know, um, because, uh, boost activity on the list had had, um, was, was at an all time low at that point. I, you know, I found myself emailing people, asking them, you know, you know, um, could you please, you know, uh, submit a review during this, this time?

[00:59:23] **GLEN FERNANDES:** Right. You know, ideally it's an accept review, but even, even a, a reject, you know, um, it is something, um, uh, I was [00:59:30] really, you know, I was worried about getting to the 10 day period and, and, and having like one, or just like one review or something, and then the review manager who gets to decide, you know, um, it's not, it's not a, it's not a, um, counting votes thing necessarily.

[00:59:43] **GLEN FERNANDES:** Like the review manager has the final decision and has to exercise their best judgment to, um, so, and not having enough reviews is, is, you know, reasonable, uh, reason for, for rejecting a library. Um, so I really, I really didn't want to get to that series, but, you know, we had, um, [01:00:00] uh, several people contribute, uh, during the review period.

[01:00:03] **GLEN FERNANDES:** Not everyone who contributed feedback actually submitted a formal review. So I think we had, um, uh, five yeses in one conditional Yes. You know, conditional on me making changes or something like that. Um, but even still, you know, I didn't know if it was enough for the re manager to consider it, you know.

[01:00:22] **GLEN FERNANDES:** Worthy for Boost and, and, and, you know, based on the review feedback. But, uh, it turned out to be so, you know, uh, I got an accept and my library [01:00:30] became, uh, well, it was accepted into Boost, you know, the next stage was transfer the repository from, um, you know, my GitHub account to the boost org thing, so that the original sources is, um, the boost org library, and then everyone else is a fork.

[01:00:45] **GLEN FERNANDES:** Um, and yeah, at that point it was just getting it into shape for the first, you know, boost release that it would release with. Oh, okay. So that, that, you know, ev everything happens on the boost mailing list, right? That's where people write their formal review email, like in an email saying, um, you know, [01:01:00] this is your background and this is your expertise and, and, uh, this is my opinion of the library.

[01:01:04] **GLEN FERNANDES:** This, the, the code, the documentation, the tests and, and, and so on. And, and then ult, you know, ultimately, ideally an accept or reject outcome. The review manager, um, who, who answers people's questions if, or directs them to me or, uh, um, you know, take some time after the review period ends to come make a decision.

[01:01:27] **GLEN FERNANDES:** And it, and, you know, usually, uh, [01:01:30] is about a week. I think that that's the typical time that, you know, uh, a result gets posted. And then at the end of that, uh, you know, um, period where they made the decision, they posted an email to the, to the list. And I think multiple lists at this point. Not just the developer list, but the boost announcement list too, saying, you know, this is the, uh, review result and whether it's accept or reject or, you know, um, accept with conditions or, um, yeah, I just remember telling, you know, my wife Carol, oh, [01:02:00] uh, boosted a line as part of Boost now.

[01:02:01] **GLEN FERNANDES:** So, you know, uh, um, I, I, I mean, I, I was happy. Yeah. Um, it's a small library, but again, you know, you go through that process and, and you feel, you feel good to have the, um, you know, to get the feedback of your peers and, and, and, and, you know, um, contribute. Um, yeah, the first library I, I was a review manager for, I believe was Boost Hannah by, um, Louis Dion, also really smart guy.

[01:02:27] **GLEN FERNANDES:** Um, and that was [01:02:30] a, um, terrific review in, in the sense that I think there were maybe 30, um, review contributions, like people writing emails, you know, uh, opining on the library. And it was something like, um, 20 votes of yes, you know, 20 reviews saying, please, you know, accept this library in a boost. And, and, um, you know, I think there was maybe one or two reviews, which were, um, conditional acceptance.

[01:02:55] **GLEN FERNANDES:** But, um, it was a great review to manage. It was, I mean, it was easy in the sense that [01:03:00] everyone loved the library. Um, but, uh, yeah, so it's al almost, so usually it's, it's the 10 day period. There's been, um, we, we have a provision for what's known as a mini review, and that's if something is, you know, has either gone through the 10 day period and it was accepted with conditions and they really, but, but, but not just conditions, but conditions.

[01:03:21] **GLEN FERNANDES:** One of the conditions is subject to a mini review. So that in that case, we've had like a five day review. Um, and then we've had maybe one or [01:03:30] two reviews that I remember in recent years where, you know, there wasn't enough feedback in the, in the review period, and maybe it was because it was scheduled at a bad time, that was a conference at the same time or nearby, you know, around that time.

[01:03:42] **GLEN FERNANDES:** And people were busy working on their, their talks for the conference or, um, a committee meeting. So, uh, I think we've seen extensions from 10 days to like, I think maybe at most, um, 17, like a total review period of 17 days. But I don't think I've [01:04:00] seen anything, you know, Beyonce 20 days. Um, yeah. Okay. So, so the, the, yeah, the, the different, um, players, right?

[01:04:07] **GLEN FERNANDES:** So there are, um, boost developers, which, uh, within them you have just contributors to boost. Um, but generally, you know, contributors more than say like a one line contribution. Like to be a Boost developer, you, you must have contributed something substantial, but you're, you're a contributor and or a library author, right?

[01:04:28] **GLEN FERNANDES:** And a maintainer is just someone [01:04:30] who is a contributor, but also, um. Uh, is, you know, responsible for that, uh, for that library. And every Boost Library author is a maintainer, right? Just implicitly. And they might add more maintainers, or if they resigned from, you know, like they, they, um, retire, they, they would hand over a maintainer ship of their library to someone else.

[01:04:48] **GLEN FERNANDES:** So you have, yeah. Um, boost, uh, developers you want, should we wait?

[01:04:58] **GLEN FERNANDES:** So we have, we have Boost [01:05:00] users, right? Like the, they're, they're, they're part of the community and they're a big part of, you know, um, part of the, uh, like interactions on the mailing list and, and opening up, um, uh, bug reports and, and feature requests on the repositories. We have, um, the Boost, you know, boost Review managers are just anyone in, in, who is part of the Boost community in some way has made some, you know, um, contributions to boost in some way, whether it's code or, or time in, in, in, um, [01:05:30] uh, in, in.

[01:05:32] **GLEN FERNANDES:** Um, opening issues on, on, on the, on the libraries or, or maybe helping out with boost infrastructure. Um, so any, any, any, anyone in the community in that sense can become a boost review manager. The, the review wizards who, um, are the custodians of the review process have to accept that person as the review manager.

[01:05:51] **GLEN FERNANDES:** And so, and the comm community does too, right? So the community have to say, well, we're okay with this person managing the review for this library because that person gets the final say. Right? Um, [01:06:00] we've never had a, a situation in Boost that I know of where someone is, um, uh, called out a review manager on making the wrong decision and said, look, you know, we, we need to have a re-review because, um, we want to invalidate this result or something.

[01:06:13] **GLEN FERNANDES:** Um, so, so there's review. Yeah. You know, so, so John is unique, right? You know, uh, I I don't think anyone else, uh, besides John would sort of, would fit the role of a boost evangelist, right? That, that's, that's one of the things he [01:06:30] did. I think, um, I, you know, I don't, I don't know how much of that was, um, just, uh, incidental, like, you know, as he, as he's doing his regular, um, uh, you know, teaching C++ or, or, um, running the conference, that he would also, um, try and spread boost like in some way through that.

[01:06:48] **GLEN FERNANDES:** But, um, no, I, you know, I, I think that's a unique thing. I don't think that's a sort of classification given, given that the. Um, the later part of the steering committee's [01:07:00] life and now the, and then the Boost Foundation really just, um, supported Boost, uh, I guess, yeah, they supported financially, but also to some extent, um, through some kind of maintenance of the servers, right?

[01:07:14] **GLEN FERNANDES:** Like Michael Case who, um, when his company CR Pro provided, um, infrastructure, you know, he or his team would be involved in, in, in upkeep. So I guess, uh, infrastructure support and, and, and funding, right? Um, now on the C++ [01:07:30] Alliance side, you know, you have that to some extent too, right? But, um, now the people that are, um, uh, contributing in some way to, to the boost libraries by, you know, work, um, adding, um, continuous integration with drone and, and all these other things via our pull request, you know, Sam Darwin, who's, who's, uh, excellent.

[01:07:50] **GLEN FERNANDES:** Uh, again, is, is another, is, is is a boost contributor in that sense, right? Um, so yeah. Very good. Just participant. Sure. So, um, my [01:08:00] first contribution to, um, boost, uh, smart Pointers led to. Us changing shared pointer to support, um, arrays, basically. So not just shared pointer of t where T is scaler, but shared pointer of, you know, t with square brackets, right?

[01:08:18] **GLEN FERNANDES:** Or t with, um, square brackets with a compiled time size inside. So a, a bounded array and an unbounded array type. Um, before it boost, you would have shared array for that. [01:08:30] But now with my, you know, one of my, my first contribution boost was well make shared is great and allocate, shared even greater, but those work for scalers and we need something for arrays.

[01:08:40] **GLEN FERNANDES:** So, you know, my, my first contribution to boost was shared, make, shared and allocate, shared for arrays, which led to say, you know, um, uh, changing the shared pointer template to support a raise. So that, um, was a paper, um, in, in a, so there were two papers. One was shared pointer [01:09:00] extending shared pointers for a raise and the second paper, um, extending make, shared and allocate share to support shared pointers for arrays.

[01:09:07] **GLEN FERNANDES:** So that's sort of those two papers. Um, well one was co-authored with Peter Mov, um, uh, that led me to, um, uh, participate in, in, uh, WG 21. Um, the first of those got was adopted for C++ 17, the second for C++ 20. So shared pointer raise support, [01:09:30] got in C++ 17, make shared and allocate shared for raise, got in C++ 20.

[01:09:35] **GLEN FERNANDES:** While, um, following that, you know, um, standardization track. At the same time I was also working on a, a, a new facility that we eventually put into the Boost Core Library, which, uh, another library that I'm a maintainer of alongside Peter ov. Um, and, um, Andre, uh, was a, a utility called two address boost to address, to convert a, a a, you know, a, um, pointer to address.[01:10:00] 

[01:10:00] **GLEN FERNANDES:** And, um, it, it, I also felt that this is a useful facility to be, you know, to be part of the CL plus standard. So I wrote a paper for that and I, um, the initial version, you know, 'cause I wasn't attending the committee meetings at this time, so the initial version of my paper, I asked someone, um, I think it was Joel Falco to present on my behalf.

[01:10:19] **GLEN FERNANDES:** And he, he did, he did that. Um, and then I, I presented the paper when it got through the later stages of standardization, but that, that, that was my entry into the, um, [01:10:30] WG 21. So initially before I was even part of the, um, the global directory, um, which I was later on, uh, part of the global, um, ISO Global directory through the CQ plus plus Alliance organization, um, I was, you know, able to participate in the reflectors because, um, you know, exemptions were made for people who in some way were, um, uh, known in SQL Plus or, or part participating in, in, in, you know, various things like Boost and so on.

[01:10:59] **GLEN FERNANDES:** [01:11:00] Um, and the same applies for, for p Edem of, right, like, you know, um. Uh, he, he also, uh, uh, participated in standards committee, um, without ever attending a meeting for the long, you know, he, he got, um, so many things into C++ 11, and then later standard of C++. And he did that without actually being there, which is, um, yeah.

[01:11:18] **GLEN FERNANDES:** Okay. Yeah. But for me, I attended a few meetings and, and, and like I said, one of those meetings was, um, where I met, um, you know, b um, but I also met a, uh, but yeah. So 

[01:11:29] **RAY NOWOSIELSKI:** when was that first time 

[01:11:29] **GLEN FERNANDES:** [01:11:30] you met B? It was in at, at the, uh, um, Albuquerque, New Mexico Standards Community meeting. Okay. Yeah. Um, so around what year do you think that would've been?

[01:11:42] **GLEN FERNANDES:** I think that was either 2017 or 2018. Yeah. Because the next one was San Diego, so I think, um, I'm, if I'm off, it'll be by one year. So, uh, it's either just, uh, 7 20 17 for the, um, Albuquerque, New Mexico one, and then 2018 for the San [01:12:00] Diego created, or No, no, no. I, no, I, I, um, I guess it's just not my personality to do that.

[01:12:06] **GLEN FERNANDES:** So it was only when, you know, I, I picked a table to sit at at breakfast and, and, and, um, Beman was at that table where I actually introduced myself to him and I said, oh, you know, I, I, I, I working on this in, you know, um, this paper for, for, um, CL plus 20 at that time. And I'm also, um, uh, you know, and, um, I'm, I'm contributing to Boost and, uh, yeah.

[01:12:26] **GLEN FERNANDES:** What kind of sense did you get? I could tell that, uh, he [01:12:30] was still proud of, of Boost and, and you know, just by how he would, uh, uh, you know, how he, how he would speak about it. But, but, but what was also amazing is, you know, um, he, he could, he was recalling things, you know, from Boost that, you know, would've happened, you know, um, in, in the two thousands, right.

[01:12:48] **GLEN FERNANDES:** And, and he had like, um, like very clear detail about, about certain things and, um, no, it was, it was great to hear he was participating in things, you know, Al almost until the very end. I don't, I didn't, [01:13:00] I didn't see him at the San Diego mean, I don't know if he, I don't think he attended anything after that, but, um, you know, it, it's, you know, up until maybe, um.

[01:13:14] **GLEN FERNANDES:** Yeah, at least up until 20 17, 20 18, I, you know, there would still be contributions from him, right. Um, and, and participation in the, whether it's participant status committee or the, um, odd email to the boost mailing list. Um, and to me [01:13:30] that, you know, that's, um, that's amazing, right? Like someone who, um, cares enough about something to participate, you know, un until the very end.

[01:13:40] **GLEN FERNANDES:** So, so that was great. So I think it was a huge loss to, to the, uh, to the community, right? Whenever some, uh, someone who, who, uh, has, has, um, devoted so much of their time to, uh, to the thing you love, uh, passes. I think it's, um, it's a very sad thing. 

[01:13:59] **RAY NOWOSIELSKI:** [01:14:00] But he was largely out of the, I mean, he was, he had retired as like the product manager and so forth.

[01:14:05] **GLEN FERNANDES:** Sure, yeah. Yeah. In that way, yes. Yeah, yeah. No, yeah. At that point, he wasn't actively contributing to, to boost, right? He wasn't making, um, commits in, in, in the libraries. He, he developed like a file system. But, uh, yeah, we, the standardization processes being able to recreate C++ 11, C++ C 11, um, you know, was unique in that, uh, it was this release that, [01:14:30] uh, gave C++ life again.

[01:14:32] **GLEN FERNANDES:** You know, I think, I, I remember, uh. Uh, people wanted to attend C++ conferences. They wanted to hear what the committee was up to. Right? It was because C++ C 11 added all these great things to the language, you know, very addict templates and, and, and great library facilities. So many of them from Boost, um, since then, um, you know, I think it, you know, I'm sure the committee's intention is to, to [01:15:00] recreate that, uh, to, to have another standard that is as beloved and adopted as C++ 11.

[01:15:06] **GLEN FERNANDES:** Sorry. Oh, it's new when we need to get 

[01:15:09] **GLEN FERNANDES:** at least in the, uh, end zone here. Sure. Um, but yeah, so the standardization committee, I, I don't think has, you know, had another C++ C 11 moment. Um, since then there have been some great additions to the language and library. Right. Um, but nothing on that scale.

[01:15:28] **GLEN FERNANDES:** I, I have my own [01:15:30] opinions about, you know, um, the direction standardization to take. Again, you know, it's hard to say whether, you know, um, going down the, these routes are, would be the best thing for the language. But, you know, one, one of the things that sort of changed after C++ 11 with this renew, with this renewed interest in C++ and now suddenly interested in standards plus plus by, by the, um, the wider C plus community was, you know, a faster release cadence for SQL Plus standards.

[01:15:57] **GLEN FERNANDES:** Right. And, um, [01:16:00] since then I've sort of noticed that, uh. Directionally, it feels like a, it feels different, and I don't, I don't know if, you know, the, the, the way to, um, pre to recreate C++ 11 is to have a, a longer period before each standard. So more things get to bake as open source libraries and get more industry experience and, and when language features, uh, come in, they're, they're, um, well, it, it's harder to do this for language features obviously, but for, at least for, for library features, [01:16:30] um, uh, more real world experience is, is, um, might result in more of a C++ 11 type effect.

[01:16:37] **GLEN FERNANDES:** Um, 

[01:16:41] **RAY NOWOSIELSKI:** you have, you have opinions, um, yeah, which, yeah. Well actually, let's, I think the, the best way to get, I think to probably get your opinions to emerge a little bit here is what do you understand happened with, uh, ASEO Christopher Ops? 

[01:16:57] **GLEN FERNANDES:** Oh, [01:17:00] right. Is that controversial? So A ZO was controversial. Um, well, networking was controversial, right?

[01:17:05] **GLEN FERNANDES:** Because networking now is essentially, uh, stalled. And at one point in time we, we thought, uh, we would get networking because, you know, it was not just a normal paper, it was a, you know, uh, ts right. Technical specification. Um, and I guess what, 

[01:17:22] **RAY NOWOSIELSKI:** why did that make it more likely? You get it? 

[01:17:26] **GLEN FERNANDES:** Oh, it, it was because, um, [01:17:30] vendors had already started implementing, you know, um, pieces of it.

[01:17:36] **GLEN FERNANDES:** And, you know, when you have something that's based on a real world library like aeo, it's, it's sort of easier, right? Like the same way it was easier to sort of get existing libraries into, into the standard because there's a, there's an implementation that that's in use and, um, not just a toy implementation, right?

[01:17:50] **GLEN FERNANDES:** A ZO is a library that's used in, um, like throughout the finance industry, for example, right? So it, it, it, it felt like we [01:18:00] were on the cusp of, of networking and C++ based on, um, you know, the networking ts, which was largely based on a ZO with Chris Koff as the, um, you know, one of the authors of the paper.

[01:18:11] **GLEN FERNANDES:** Um, ultimately, you know, uh, it, the committee decided it wasn't, um, you know, generic enough. It, it, it, it's only networking and they want, uh, and there was a [01:18:30] desire, like my, my impression is there's, there's a desire to have something that can pro, you know, um, back both networking and other kinds of, of IO and a synchronous operations.

[01:18:40] **GLEN FERNANDES:** And so, um, you know, it, it it's the, the state now is, um, stalled or. Um, uh, completely halted, right? Like 

[01:18:54] **RAY NOWOSIELSKI:** what, what do critics say? What have critics tended to say about that? 

[01:18:58] **GLEN FERNANDES:** I think the biggest, [01:19:00] uh, complaint is, well, it's now, you know, 20 25, 20 26, and C++ won't have networking, right? And he would one of the most instrumental languages in the, in, in, in the world.

[01:19:16] **GLEN FERNANDES:** And, uh, you know, you need, you need to find a third party library to connect to the internet. Um, which, which isn't great, I think. Um, and so what is networking in a nutshell? I mean, the ability to [01:19:30] write program, you know, the ability to, um, write programs to, to, um, for internet connectivity, right? So open up a socket or, or write a web server or write a server that handles connections and, um, where you don't have to write platform specific code, right?

[01:19:43] **GLEN FERNANDES:** You don't have to, uh, say, oh, I, I want to, um, write code that targets, you know, um, VSD sockets on this, this OS or win soc. But the ability, the ability to write cross platform code because something's in this, in the standard library that can, um, [01:20:00] do the tasks that, you know, everyone wants to do with, with regards to connecting to applications on the internet or writing internet enabled applications.

[01:20:08] **GLEN FERNANDES:** Yeah, 

[01:20:08] **RAY NOWOSIELSKI:** I believe you had said in some of our pre-interview stuff that, um, when you. Talk about when you look for success stories in recent years, uh, you always bring up Flat Map, is that right? Was this an attempt to innovate for the standard? 

[01:20:25] **GLEN FERNANDES:** Oh, can you quote? No. So I mean, if I, yeah, if, if you're talking about success [01:20:30] stories into the standard or success stories for, for Boost, 

[01:20:34] **RAY NOWOSIELSKI:** you know, I, I just had a note from you that I put down right before this interview for success stories.

[01:20:40] **RAY NOWOSIELSKI:** I always bring up Flat Map, and I think you might have said Zach Lane decided to innovate for the standard. 

[01:20:45] **GLEN FERNANDES:** Ah, okay. So then, so not, not success story. So, uh, the opposite of success rather. Yeah. So, um, yeah, flat, flat Map is one of those libraries where, you know, the Boost implementation is used almost everywhere.

[01:20:59] **GLEN FERNANDES:** And, [01:21:00] um, it's also the typical, uh, implementation you would use for, you know, someone would think of for a flat map, which is, um, a vector of pair of key in value, uh, the implementation. And that was the original implementation Zach was proposing for, um, the original design Zach was proposing for the, for the standard.

[01:21:20] **GLEN FERNANDES:** Zach who? Zach Lane. Right. So Zach, this, yeah. So, um, and through the, uh, standardization process, you know, as his paper went through the different [01:21:30] groups, I guess, um, feedback shaped that proposal into, uh, a design where rather than the, the very typical, um, uh. A vector of, of, uh, or, or, or to more be more general sequence container of pair of key and value.

[01:21:47] **GLEN FERNANDES:** It became, uh, two sequence containers. A sequence container of of, of keys and a sequence, container of values. Now that's, that's a viable implementation, right? It's not the boost implementation, but it's also not the implementation that [01:22:00] has that, um, you would see in, in so many other, uh, uh, library collections besides Boost.

[01:22:07] **GLEN FERNANDES:** Right. Um, I think maybe app sales flat map is also similar to the boost one, right? Which would, which I would say is the more common of the two. Uh, it's, it's one of those cases where, um, you know, design by committee has, has, has played a little role. Um, even though, you know, the standard, uh, [01:22:30] standardization process is, is not supposed to be designed by committee.

[01:22:32] **GLEN FERNANDES:** It's supposed to be a process where the de design is done and then, you know, you, um, you, you accept a proposal or you, you, uh, for the standard that's already been baked. So it's, it's one of those libraries where I still question what we put into the, um, C++ standard. Okay. Um, and it, you know, where it deviated from, what boosted

[01:22:59] **GLEN FERNANDES:** [01:23:00] why, I mean, I guess you kind of gave it to us, but anything else you wanna say there? Yeah, so I mean, the reason I question is because, you know, um. I, I know of cases where people don't want to adopt the standard version because the, uh, they want the, you know, they want the single allocation, they don't want the double allocation that would be involved with two sequence containers, you know, the vector of keys and the vector of values.

[01:23:22] **GLEN FERNANDES:** So when you hear, when you hear things like that, you, you, you know, you question whether, um, the right thing got into the standard, right? Um, if, [01:23:30] um, yeah, 

[01:23:32] **RAY NOWOSIELSKI:** geometry log, multi precision, these are all somewhat recent ones that there were never standardized. You know, any takes on, on why. 

[01:23:41] **GLEN FERNANDES:** I think in those cases, there was no, uh, desire to standardize them.

[01:23:45] **GLEN FERNANDES:** And so there was no, um, at least as far as I've seen in my, uh, observance of the reflectors, no huge push to, um, to write a paper on them and then, uh, put them forward. There have been for other libraries like boost up fiber, which is [01:24:00] still, you know, um, at least as far as I lost checks chugging along in the standardization process.

[01:24:06] **GLEN FERNANDES:** Um, you know, it's, it's an alternative to core routines and both core routines, which now exist in the, in the, in the core language. And fiber could, could coexist in, in C++ because fibers do, you know, um, solve a different need. Um, but for the other libraries, they're all useful libraries because, um, I mean, clearly useful 'cause they have a lot of users, but, um, not things that I've [01:24:30] seen users clamoring for to be part of the C++ standard.

[01:24:33] **GLEN FERNANDES:** I actually don't know. Um. I don't know what, why necessarily, I mean, I guess maybe some things are best served by, um, you know, uh, independent library collections and, and maybe there is no true generic, uh, um, candidate for the, for the sequence of standards library, right? You, you have to make a decision on certain things and then you alienate certain users and, and maybe that's the, [01:25:00] maybe that's the best way forward for certain libraries that they should exist outside the, outside the standard.

[01:25:06] **RAY NOWOSIELSKI:** It's interesting though that, that that wasn't so much the case or that wasn't argued or I can't, I'm not aware of examples where people gripe about, uh, that being the case, uh, in the era before 2011. That's the only part I can't quite put my head around, but like, what changed, you know, in terms of philosophy or approach, but 

[01:25:26] **GLEN FERNANDES:** yeah, it's hard to say, right?

[01:25:27] **GLEN FERNANDES:** Because, you know, thinking about the libraries that, that [01:25:30] were accepted for, for E 11, sure, some are ver are high level like RegX, um, but a lot of the other ones are core like foundational pieces that, um, uh, you know, very small, uh, independent, uh, components. Whereas something like, um, well, well, I guess you can also make that point for libraries like rational, right?

[01:25:56] **GLEN FERNANDES:** It, it's, it, it can be foundational in, in, in its own way. So it's, it can be a [01:26:00] vocabulary type that, that, um, that, um. Is a, is a decent fit for the standard. So I, I don't know. Um, you know, rational wasn't proposed before, um, C++ C 11 today. If it was, I, I, I, I question whether it would have much success.

[01:26:17] **GLEN FERNANDES:** Um, yeah, yeah. Beast is, you know, a, um, beast is a HVP and, and web sockets library in a nutshell, right? Um, [01:26:30] it's, uh, it's a great library. I, I know of, you know, uh, a few places that are, are, are using Beast, um, only by virtue of being a release manager. And, and, you know, people get to know me with and associate me with Boost.

[01:26:43] **GLEN FERNANDES:** So they, they send me questions and, and, um, I noticed, you know, a, uh, an, an uptick in, in Beast adoption. So, so, uh, uh, organizations where people have started using Beast. Um, but yeah, it's, it, to me it's a, it's a sock. It's [01:27:00] in HT p uh, library. It's, that's the library that, uh, someone might want to use to write a, a, a, you know, um, a, a program that talks to rest API or write, write a web server, write a, write a miniature web server.

[01:27:13] **GLEN FERNANDES:** Um, it would be in the C++ language Slack where, um, you know, Vinny was, uh, he joined the Vinnie Fal where, uh, Vinnie Falco had joined the Boost Channel to, um. I talk about contributing his, his [01:27:30] library beast into, uh, boost. I don't even remember if at the time initially if it was Beast or it was a, it was some other name, like a HTTP library.

[01:27:37] **GLEN FERNANDES:** Maybe it was Boost at http. It was the initial, uh, name. Um, but that's where, you know, uh, I, I saw Vinny ask questions about, uh, C++ and Boost, not just about the review process, but feedback about his library. And I remember, um, you know, providing some opinions and advice and, and how he could deal with allocators and, and, um, uh, and, and [01:28:00] he used that to enhance, um, enhance Beast.

[01:28:03] **GLEN FERNANDES:** So, so yeah, Vinny, Vinny has a, a personality where it's, it's, uh, uh, he, uh, it's larger than life in some way, right? Like he, he, uh, he's very outspoken about what he believes in, and, uh, he's very passionate about what he does. The passion is very infectious. You know, a lot of people, um, post questions about C++ or, or boost and, um, you know, you, you answer them, but, but with Vinny, it was like, you know, you want to help this, this guy, or you want, [01:28:30] you wanna, um, you wanna, uh, uh, talk to him because he, he's just so enthusiastic about what he does.

[01:28:36] **GLEN FERNANDES:** And so it, it's, uh, you know, that's where I became, that's where I met Vinny. Um, I think he even credits me in, in, in like the beast documentation or something. But, uh, you know, he didn't stop at, uh. Um, just getting a library into Boost. Right. Which he did. He got, he got, he got Boost, uh, he got Beast into, into Boost.

[01:28:57] **GLEN FERNANDES:** But, um, [01:29:00] I think that same desire to, uh, contribute back is magnified, you know, 10 times in many. So, uh, it's not just, oh, I, I, you know, I wanna contribute to all these Boost libraries. He, he wanted to, um, help boost in, in, in, in big ways. Um, and it was, it was always clear, right? Like he, his, he would always post on the mailing list with suggestions for how, uh, things should be done and, and willing to provide resources to do it.

[01:29:27] **GLEN FERNANDES:** Um, yeah. [01:29:30] Uh, have you since met him in person? I've met Vinny in Per, when did I meet Vinny in person? It would, would've been, I think it would've been at the, um, San Diego, uh, standards committee meeting. I don't think I would've met him in person before that. He's, he is, he's asked, you know, he's offered to, to get me out to where he lives many times, and, um, at some point I'll accept.

[01:29:55] **GLEN FERNANDES:** Um, but, uh, well, what, uh, I think, uh, well, I mean, on [01:30:00] me or on, on and and on the people that didn't know Vinnie, right? Because open question. What do you recall? I mean, for me it was, it, it was, it was, um, when I, when I met Vinny, it was like I'd known him, uh, forever, you know, and he's, he's in in person. He's exactly, he is online.

[01:30:15] **GLEN FERNANDES:** So, um, there, there was almost like. You know, nothing changed for me when I, when I met Vinny. Um, but I think, you know, when, when I was at that committee meeting, I, I, I get the impression that he made the same, um, impression on, on the, [01:30:30] on people who hadn't met him, right? Like he, he, he, uh, he is, he always speaks his mind and, and, um, yeah, I, I think, you know, some people like that and, and, and others, it might, might rub the wrong way, but, um, there's no question that he, he cares deeply about what he, you know, um, what he does.

[01:30:51] **GLEN FERNANDES:** Yeah. Um, my, my, uh, model of Vinny is this, right? He, he worked on bearer, made a lot of money there, retired, came out of retirement to work at [01:31:00] Ripple, um, went back into retirement, and then decided to do something good with his money. And, and the, one of the things that, you know, um, uh, the C++ community has, is, is probably grateful for, is that one of the good things he is decided to do with his money is put it into C++ by, you know, and, and help the community in a way.

[01:31:15] **GLEN FERNANDES:** And a big vector for that he sees is, is the Boost Library collection, right? He, he wants to use that as the vehicle to, to, um, make C++ better and, and benefit the C++ community, um, ah, in [01:31:30] that sense. Okay. So in, yeah. So the C++ language Slack, you know, was, was, was fantastic, right? It suddenly grew in size to the, to the extent that, um, the free plan was no longer enough for us, but it was, it was taking off as a, as a, a, a venue for communication about C++.

[01:31:47] **GLEN FERNANDES:** Um, you know, people, um, from WG 21 were, had, had the WG 21 channel. Uh, the Boost Channel was booming. Um, at some point, um, the, [01:32:00] you know, the person who created the Slack started to add as administrators, various members of the community that decided to take the slack in a, in a different direction, like enforce more rules around certain things.

[01:32:12] **GLEN FERNANDES:** And, um, essentially, uh, created the impression for many people that they were stifling open conversation. Um, so, but at, at the same time, the slack was, was, was, um, was too big to, uh, to, [01:32:30] to handle on a free plan. Like we didn't have history. And history was probably one of the most important things, right?

[01:32:34] **GLEN FERNANDES:** Like, you, you, you, you, you wanna know what you talked about for, you know, a week ago. And you, and when, when it had more than 10,000 users, um, uh, you know, you, you couldn't do that. So at the time, you know, Vinny, um, uh, wanted to, you know, he, he wanted to solve both problems, right? He wanted to, um, give us a proper slack, which was not on the free plan.

[01:32:56] **GLEN FERNANDES:** So he, uh. Bought the slack from the person [01:33:00] who, uh, set it up, basically bought the rights to it, and then started paying for a Slack. So it wasn't a, a free planned slack anymore, which was, which was also great. Um, because, you know, besides history, we had all access to a lot of Slack features now. Um, but, and of course, as part of this mini, um, also now manage the Slack, and he wanted to make it a, a, a place where, you know, um, uh, people could communicate in, in the way that people would communicate on the boost mailing list.

[01:33:27] **GLEN FERNANDES:** And for, you know, it did, uh, [01:33:30] it, it was super effective in, in the sense that a lot of mailing list conversations that started happening on Slack. You know, I, I remember I, well, look, if I, I really want, wanna reach these three people like Peter's here, I can just, you know, type a message in Hash Boost rather than, um, post it on the mailing list.

[01:33:49] **GLEN FERNANDES:** So, you know, slack, slack kept growing. There were people that, um, that didn't like the, the way Winnie ran the slack, you know, that he wouldn't, um, [01:34:00] uh, censor people in certain ways or allow people to, you know, speak freely in other ways or, or, um, um, or allow certain individual on the Slack that maybe they, they, they felt had, you know, uh, for, they didn't want, uh, participating just because of, um, non-technical issues.

[01:34:20] **GLEN FERNANDES:** But, you know, um, sounds like code of conduct issues 

[01:34:24] **RAY NOWOSIELSKI:** similar to debates that were happening on Twitter. 

[01:34:27] **GLEN FERNANDES:** Exactly. Yeah. Right. Um, [01:34:30] a lot of the, the, um, topics of, of say, you know, censorship and, and why people institute a code of conduct, were, were some of the con, uh, points of contention there. So there were some people that decided to leave the slack.

[01:34:43] **GLEN FERNANDES:** I think that the, the, the Exodus, uh, happened later than 2019 Pro probably, right? Like, um, but the, but the conflicts were, were there already. And, you know, there were, there, there was some animosity born towards Vinny [01:35:00] because of that, uh, that, uh, uh, ownership of the slack and the way he, he managed it. Uh, you know, personally, I, I didn't feel it was the wrong thing because again, I, uh, I err on the side of you.

[01:35:15] **GLEN FERNANDES:** You don't like someone, you, you ignore them. Not, you know, you stop them from, from speaking. Um, but, uh, yeah, so I think, and do you think that's more consistent with the long term boost [01:35:30] philosophy? Like what the way messaging has happened over the course of Boost? I think so, because I think, I think that that's consistent with how things are, are, you know, work, work on the boost mailing list because we know ban someone from the mailing list because they're offensive, right?

[01:35:44] **GLEN FERNANDES:** We, we ban the spam bots because they're automatons. But, um, and, and I, I, I like that the slack, uh. Has that same, uh, philosophy. It, but it, again, it doesn't, uh, appeal to everyone. And, um, eventually there was a, [01:36:00] um, an, an exodus from Slack, you know, certain groups formed their own, um, uh, discord for, for communication.

[01:36:09] **GLEN FERNANDES:** Uh, although, yeah, I don't know how successful those are. Yeah. 

[01:36:16] **RAY NOWOSIELSKI:** And, um, iso C++ 

[01:36:19] **GLEN FERNANDES:** the standard. There's, there, there is the standard C++ foundation standard, um, you know, which, which, which, um, had come into existence, not that, not that long ago. Um, but, uh, when the C++ [01:36:30] Alliance was forming, you know, I was aware of it because Vinny was talking about it right in, in the Slack.

[01:36:34] **GLEN FERNANDES:** And of course, I, I, you know, I I was in good terms with Vinny and, and, and would hear about it from him. And, you know, my my point of view was, um, yeah, I think it, it's great that, you know, Vinny wants to, um, do something more for C++, but to the extent of creating a, you know, an, a non-profit for it, right?

[01:36:54] **GLEN FERNANDES:** And that's even C++ themed. It's not, um, you know, some organization [01:37:00] where an ancillary goal is to benefit programming languages and within that C++. Um, so I thought the C++ alliance was a, was a, you know, the, the invention of it was a great thing. Uh, I didn't really draw parallels to between IT and the standard C++ foundation, because again.

[01:37:18] **GLEN FERNANDES:** The standard C++ foundation, in my view, was, uh, I knew it, it played a big role in, in C PPP Con in some way. But again, it, you know, it's, its goals were towards [01:37:30] standardization. Uh, uh, I knew from the get go that, you know, C++ Alliance, um, was going to play a big role with Boost, right? Like the Boost was, its, um, was its, uh, uh, vehicle for, um, improving C++ or, or benefiting C++.

[01:37:47] **GLEN FERNANDES:** Yeah. 

[01:37:49] **RAY NOWOSIELSKI:** That's where you got the sense of, so that's where Benny's heart was, in particular, within c at the time. 

[01:37:54] **GLEN FERNANDES:** Yeah. Yeah. Um, yeah. 

[01:37:57] **RAY NOWOSIELSKI:** Um, we, we covered the [01:38:00] foundation, but there was one question I didn't get to there, which is, uh, when that, when that meeting took place that you were in, uh, regarding John Cal, that was a fairly small meeting, correct?

[01:38:09] **RAY NOWOSIELSKI:** Like, who was, who was in the room? Uh, se calls a meeting and who was there, including you? 

[01:38:15] **GLEN FERNANDES:** I think it was everyone. So, at the meeting, I think it was everyone except for John, maybe one person who was on the, uh, uh, com steering committee at the time. No Boost Foundation, I think. 'cause we'd already become the, so maybe one person wasn't in attendance, but I think, [01:38:30] um, you know, besides John, everyone else was in attendance.

[01:38:33] **GLEN FERNANDES:** Who was, 

[01:38:33] **RAY NOWOSIELSKI:** who's everyone else? 

[01:38:35] **GLEN FERNANDES:** Um, who were, who was in the room, or essentially who was in the room. So. In the room would've been myself, uh, David Sanko, Michael Case, I think maybe Hartman case. I might have been there. Um, Zach Lane. And I've actually, I've actually forgotten who was, uh, part of the, the foundation of the time.

[01:38:58] **GLEN FERNANDES:** But yeah, I just remember it being [01:39:00] almost everyone. And, and the cal, uh, matter went to a vote. Did 

[01:39:04] **RAY NOWOSIELSKI:** anyone not vote in favor of removal or how did that go? 

[01:39:10] **GLEN FERNANDES:** Uh,

[01:39:14] **GLEN FERNANDES:** I don't know if it went to a vote or, I don't remember actually. Um, did it go to a vote? I actually don't remember. I'm sorry. I don't remember like, whether it went to a vote or not, but I just remember it was almost like unanimous consent in the sense that [01:39:30] no one, um, like everyone was uncomfortable, you know?

[01:39:34] **GLEN FERNANDES:** Um, about, but I think the impression I got was, you know, um, we would, someone would talk to John, but it wouldn't be that he was evicted from the, you know, kicked out of the organization. It would, it would, we'd be to persuade him to resign. I think that was the, the conclusion that I walked away from that meeting with, that that's what someone was going to, they would, [01:40:00] they would reach out to John and, and convince him to resign his position.

[01:40:03] **RAY NOWOSIELSKI:** So what went down last year in, in terms of the, uh, boost website. And ultimately the fiscal sponsorship. Um, right. Tell me the story of Alliance versus Foundation. 

[01:40:16] **GLEN FERNANDES:** Sure. It turned out, so, you know, Vinny had started development on the website, but one of the things that, um, you know, is, is necessary, uh, to launch the website on is, is the domain, right?

[01:40:28] **GLEN FERNANDES:** And the, um, [01:40:30] the domain is man was managed by the foundation, and, you know, Vinnie felt that the domain should be, um, managed by, uh, an organization more co Vinnie felt the domain should be managed by an organization more competent to, to, uh, to handle not just the, the boost.org domain, but all the boost assets.

[01:40:50] **GLEN FERNANDES:** I mean, Vinnie was already, uh, the C++ Alliance and was already managing the, um, the Fastly, um, uh, layer, right? [01:41:00] But, um, you know, the, the, his reasoning was not so much incompetence on the Boost Foundation, um, uh, on the side of the Boost Foundation, but also, uh, you know, that, uh, actually no, I take that back to some extent, maybe Vinny felt that the Boost Foundation was, you know, not competent enough to, to, uh, manage a property as critical as the Boost domain because there was already one incident where, um, the, [01:41:30] the domain registration lapsed and people going to boost.org would get that, you know, that, that, um, the, uh.

[01:41:37] **GLEN FERNANDES:** Landing page where, uh, to, to, uh, where someone had, um, could buy the domain or, or something like that. I forget what it was, but basically it was, for us, it was a boost outage, right? Um, at that, at that point, there was no boost.org that people could go to. I remember calling, you know, Michael Case at the time to try and, uh, I think he, he was probably at work or something to, to try and figure out what was going on.

[01:41:58] **GLEN FERNANDES:** Like why, [01:42:00] um, uh, why can, why, why don't we have boost.org up and at, at, you know, at that time it created this impression, not just in Vinnie, but you know, the wider boost, uh, community that, um, we're not doing a good job with, with, um, maintaining these things if we, if we let the domain lapse, right? Um, so it was, it was probably since then that Vinnie felt that, uh, there should be a more competent entity in, in, in charge of the domain and the other boost assets.[01:42:30] 

[01:42:30] **GLEN FERNANDES:** And, um, you know, he, he put in a lot of money and, and effort into this website, so he didn't want it to be wasted behind, um, uh, you know, just by virtue of say, the domain being mismanaged or something like that. So it led to, you know, what, what it ultimately led to was, um, the, um, contention on the list because, [01:43:00] you know, on one side you had, uh, um, you know, David Sanko who, um.

[01:43:06] **GLEN FERNANDES:** I, I can say this, right? He, uh, he, uh, David Sekel, I, I see him as a, as a, a decent human being who, who, uh, um, has, has good intentions. Um, he, uh, was vehemently opposed to how, you know, to Vinny having control over any part of Boost because he believed that this would be boost. Um, he believed this would be Boosts downfall.[01:43:30] 

[01:43:30] **GLEN FERNANDES:** Um, so dire. Yeah. Um, meanwhile, you know, I, I, I, you know, I could say Vinny, um, also didn't feel like, uh, the Boost Foundation as a whole or, or, you know, under David's, um, leadership would be the best custodians of Boost Assets. Ultimately, what, what, what, um, what was proposed, and, you know, what the foundation agreed to as well is to let the community decide.

[01:43:55] **GLEN FERNANDES:** So it was decided that it should be a, a boost, um, [01:44:00] you know, go through the Boost formal Ruby process, just like any library getting into Boost, maybe the entity that, that manages Boost assets. Um, you know, something equally important be, be, uh, DEC decided by the community. Um, through the, through the same rigorous review process with the review manager, the community voted, uh, to make me the review manager.

[01:44:21] **GLEN FERNANDES:** And, um, I accepted, even though I was, uh, I, you know, I was hesitant on, on one side [01:44:30] because, you know, I, I, it's a. A tough decision to make as well as, you know, I was, I was a member of the Boost Foundation at the, at the time, uh, and, and, um, uh, so, you know, when, when it was first suggested, I, I thought it, um, it wouldn't, uh, it wouldn't materialize just because, well, you know, why would the community want someone who's a member of one of the, of, of an opposing entity to, to weigh in on it?

[01:44:57] **GLEN FERNANDES:** But I, they, they, um, [01:45:00] there was, um, uh, there was a more than a handful of, of, of voices in support of me being a remanage and, and non opposing it. So I, I decided to accept, uh, it was a very, an honor. Mm-hmm. Uh, yes. Yeah, it was, and it was an honor in that, in that sense. And some of the things that were, were said about me in the, uh, by the reviews were, were also very, uh, heartwarming.

[01:45:25] **GLEN FERNANDES:** And I, and I, uh, I, I wouldn't soon forget them, but, uh, [01:45:30] it, it was an intense review for different reasons. Not technical, not the same technical reasons anymore, but, um, um, it, it was also a very clear cut review in the sense that there was overwhelming support for, um, the, you know, uh, the fiscal sponsorship committee, the proposal designed by the C++ Alliance and backed by the C++ Alliance to manage and, and, uh, take control of the boost assets.

[01:45:56] **GLEN FERNANDES:** So 

[01:45:56] **RAY NOWOSIELSKI:** let's, let's cut stakes and the whole thing. 

[01:45:59] **GLEN FERNANDES:** [01:46:00] Right. So at least during the, the review period, um, you know, all before the review period started there, um, there was, uh, a lot of, uh, uh, jabs thrown on, on the list, right. By by by Vinny and, and, and by David. Um, I think during the review, the, uh, foundation members, I mean in general, the foundation members are silent list, you know, you know [01:46:30] Zach Lane, myself, and, and, and, and, and Peter Dima, I don't remember when he actually left the foundation.

[01:46:35] **GLEN FERNANDES:** You know, we, we, we would, um, we would talk as boost developers on the list, but in general, the, the Boost Foundation members would wouldn't speak. And, and it was the same for the review. David would speak on the list, but, um, you know, during the review he, he was mostly, um, silent, but, so the drama actually happened before the review, leading up to the review.

[01:46:54] **GLEN FERNANDES:** And, and the drama was one of the motivations for the review in the first place. And I think the community sort of felt like, [01:47:00] you know, um, they wanted an end to it. They, they didn't want to be in between two, two sides. Um, and, and, and by that time, most of the community, you know, as, uh, had been divulged to me and, and by what members of the community had, uh, spoke to me about, had already formed, you know, opinions about.

[01:47:21] **GLEN FERNANDES:** Um, the Boost Foundation and, and, and, um, some of their members and, um, and, and obviously about many as well, [01:47:30] but, uh, you know, 

[01:47:31] **RAY NOWOSIELSKI:** what, what do you think persuaded ultimately that the vote went down the way it did? 

[01:47:37] **GLEN FERNANDES:** You, so if we're, we're talking about what, um, what convinced the foundation to put it to be, you know, to let it go through a review?

[01:47:47] **GLEN FERNANDES:** The, the, the, um, the motivating reason would be that the, the, that the foundation members were also, um, tired of, of the drama. [01:48:00] And at, at this point, um, it, it was starting to become clear that, you know, um, they, that there was no desire for the, you know, uh, community desire for the, for the foundation members to be involved in Boost.

[01:48:16] **GLEN FERNANDES:** So, uh, I, I think it, it, they didn't have to agree to the, you know, um, to the, the formal review. But I think at this point, uh, there was a, a desire to, [01:48:30] to let the community decide and accept the decision. You know, like this is the sign for us to, to, um, to leave Boost alone. Um, and I think in some ways I think it, you know, um, just to, uh, comment on that, I think, I think it would be, I, I think it is.

[01:48:49] **GLEN FERNANDES:** Could be the best thing for the foundation. You know, they have their own goals, whether it's related to the conference or other things in C++ that, um, you know, to divest from, from, [01:49:00] from Boost. I think it was, you know, it was probably something like 90% to 10% or even more probably, I would say even 95% to 5%.

[01:49:08] **GLEN FERNANDES:** Uh, the, there were, I can, I can only recall, you know, one or two, um, voices in favor of the foundation. Clearly. What 

[01:49:18] **RAY NOWOSIELSKI:** were the votes about? 

[01:49:19] **GLEN FERNANDES:** Yeah, I, I, you know, I read every single piece of feedback that was given during the review period, whether people, you know, took a stance or not, and most of them did. [01:49:30] Um, and the ones that did, you know, were not, were people who are, who spend their, you know, um, spent hours and hours of, of their life contributing to boost.

[01:49:41] **GLEN FERNANDES:** Um, but what was very surprising was we asked, we had boost users, um, opine and then, you know, pick the C++ Alliance because they, they had interactions with C++ Alliance members, or, or, or libraries, you know, uh, with maintainers who, um, are [01:50:00] employed by the C++ Alliance, that, that took over maintenance of Boost Libraries, as well as, um, users who were just aware of what the C++ Alliance was doing for Boost and the way of setting up, you know, CI or, or, um, um.

[01:50:14] **GLEN FERNANDES:** When, you know, when the domain, uh, sorry, when the hosting, uh, issue came up that the C++ Alliance was, was contributing there. So, um, it was, the surprising part was not so much the, the Boost, um, uh, developers who I think, [01:50:30] you know, it was clear that they were, um, would favor the C++ Alliance, but also these Boost users, um, coming out of the woodwork to, you know, um, to vote in favor of the C++ Alliance.

[01:50:43] **RAY NOWOSIELSKI:** What is WG 20 one's Beammen project? 

[01:50:46] **GLEN FERNANDES:** So the Beammen Project is an initiative, um, started by, um, the Boost Foundation, and it's the, the leader, the three leaders of the, of the BEAM Project are all members of the Boost Foundation. And they're also, two of them are [01:51:00] chairs of various working groups in WG 21.

[01:51:03] **GLEN FERNANDES:** So the Beman Project is, what are those names? Uh, inal Levy, uh, Jeff Garland and David Sanko. I, I forget if he was, uh, one of the three, or is, or still is. Um, I'll have to refresh my memory on that, but yeah. But Inal and Jeff are chair, uh, respective chairs of, you know, um, of, uh, WG 21 [01:51:30] working groups and, uh, are two of the key people in, in, in the leadership of the, of the Beman project.

[01:51:37] **GLEN FERNANDES:** Um, and so the Beman project, the Beman project is being, um, uh, pitched as the. As the next sort of vehicle for entry into the standard, what Boost was originally. Um, and I, and, uh, I, I sort of see, uh, it being the recommended choice now, right? I, I remember, um, [01:52:00] before you would say, well, why haven't you put it through Boost?

[01:52:03] **GLEN FERNANDES:** Maybe now people might, might say, you know, why haven't you put it through the, through the Beamin project? I think I, I wouldn't call it a competitor if I, if I subscribe to the, uh, future vision of Boost, that Boost doesn't really, um, is no longer gonna be about, uh, getting things into the standard. And maybe it will still serve that purpose, but only because things Bake Will, will bake and boost and, and become, you [01:52:30] know, uh, high quality libraries used in the industry.

[01:52:32] **GLEN FERNANDES:** And then there are good, great candidate for standardization, but I think it's unlikely that Boost will fill that original role just because a boost review now is gonna care about so many more things than, um, what is necessary for just eligibility. For standardization. I think, you know, the idea of Beamin project is you, you have a paper and you want, you want to provide a real world implementation that people could use, [01:53:00] that, that's, that's where you go.

[01:53:02] **GLEN FERNANDES:** But Boost is, um, more about, say more, more than just a working implementation. It it, the goal of Boost, um. Ha has sort of, uh, if not the goal, what Boost has sort of become now is a li is a way to get, you know, high quality libraries for, for real world use. And, and even though it might seem like those, those two are, uh, related, I think, um, [01:53:30] the, the bar is probably gonna be lower, um, for one than the other.

[01:53:36] **GLEN FERNANDES:** So I would hope that's not the case. You know, I would hope that, um, anyone in any position, be it a chair or, um, involved in any, any way in, in, in say, standardization is not going to, um, carry personal conflicts or, or you know, like bad interactions with people and, and, and forget about the technical merit of, of a library.

[01:53:58] **GLEN FERNANDES:** So it really shouldn't [01:54:00] matter if a library from Boost is being proposed for standardization, if it's, um, a well-written library. And, and the paper is, is a well-written paper. I think, um, with the standards committee, you know, obviously direction, direction is a big one. So talking to people about where they see C++ going, you know, already there's um, there, there's the side of things where.

[01:54:28] **GLEN FERNANDES:** People are afraid [01:54:30] of, uh, obsolescence. Like they, they're, they, they don't want C++ to, um, fall by the wayside. And, and, you know, compared to, uh, languages that seem to be picking up, uh, steam like rust or, uh, you know, and, and they don't want C++ to be, to have this image created as a, as the unsafe language that, you know, no, that, uh, um, isn't gonna be recommended for the industry to use.

[01:54:56] **GLEN FERNANDES:** Right? Like there was that, that paper published by [01:55:00] the, um, under the Biden administration about, you know, c plus that talked about C++ being unsafe. So I think, you know, figuring out where the key people, um, uh, who, who are spending all their efforts now in, in, in, in standardization, uh, see the future of C++ is, is a, is a big thing.

[01:55:20] **GLEN FERNANDES:** But I would, you know, I would, I, another, I would also, you know, uh, be interested in knowing [01:55:30] in aggregate, you know, what, what, what different people, um, see as the future for Boost. Because even though it's direction has shifted, you know, it WG 21 was the birthplace in some sense right? Of, of, uh, of boost and um, yeah.

[01:55:47] **GLEN FERNANDES:** Yeah. That is though. No, I think, I think individual sort of, you know, features, I think that the, the big thing is, is whether standardization is [01:56:00] producing. Um, the big thing is whether standardization is producing features that act that people actually want, right? I think, um, if it's fulfilling that goal or it's just people inventing great things that, that nobody's really that excited for and, and, and, and how do they, um, like figure out what, what, you know, there, there's limited resources, right?

[01:56:21] **GLEN FERNANDES:** People can't be, um, uh, in all working groups or, um, and, and certain things can only happen as part of the ISO process [01:56:30] at physic at meetings, which take place with, you know, at at end points in the year. So I think figuring out what, what's, what the best thing to invest in for C++ is future is, is, is, uh, is probably the most interesting thing to find out from W 21 members 

[01:56:47] **RAY NOWOSIELSKI:** because there's actually no Boost Library proposals in consideration.

[01:56:50] **RAY NOWOSIELSKI:** Well, other than the ones we've discussed, 

[01:56:52] **GLEN FERNANDES:** correct? Yeah. Um, that's true. Uh, when, what's true? Can you give it back to me? Sorry. Yeah. So as far as I know [01:57:00] besides Fiber, that's still, you know, fighting the, the fight. Um, I don't see any new Boost libraries propose for standardization. Um, and, and currently in discussion for, um.

[01:57:14] **GLEN FERNANDES:** I guess what's next? After C++ 26, when we were at the, uh, you know, uh, in the week of the committee meeting, there was a, uh, um, a plenary schedule, which is not, you know, one of [01:57:30] the individual working groups for, to discuss the future of meta programming, I guess in C++. So the, the one of the key things being, you know, whether MP 11 gets into the, you know, it should, should be even considered for the, for the, um, C++ standard.

[01:57:45] **GLEN FERNANDES:** Um, Walter Brown was representing, you know, that side of things like getting boosted MP 11, and there were various other people, um, who, uh, had the other side [01:58:00] where, you know, the future of, uh, of meta programming wasn't, um, a meta programming library as in the MP 11 sense, but more towards, uh, compiled time reflection.

[01:58:12] **GLEN FERNANDES:** And so, um, what was odd about this was the, uh. To me at least. The, what was odd about this was the meeting was only really open, um, to select people. Now, anyone could physically go in and [01:58:30] attend, but really, you know, the, the invites were, were for, um, for select people. And I, and my understanding was, you know, they want, wanted, um, expert opinions in, in that field and, and so on.

[01:58:41] **GLEN FERNANDES:** So, um, but anyway, Michael, case and I, uh, I think were both, uh, present, um, because we just happened to be around and attended, not because we were, uh, invited. Um, and, uh, you know, it was brutal, but, uh, it, [01:59:00] um, I think it, it was one of those meetings where it, it didn't seem like the O one side had a shot, right.

[01:59:10] **GLEN FERNANDES:** And, um, so it didn't seem like, uh, it, it was one of those arguments where one, it didn't seem like one side had had a shot. Uh, you think the, the deck was clearly stacked against the, the MP 11 side. So, um, he, he, I, I think he was, you know, upset with the outcome. And, uh, we all knew, you know, we, we all, we all, [01:59:30] um, we, uh.

[01:59:33] **GLEN FERNANDES:** Those of us, you know, who were on the side of MP 11, getting into the standard because we felt it was a useful library and, and would be useful for many years. Um, you know, um, we we're disappointed with the outcome. Yeah, it boil, boiled down to not wanting to invest in, um, you know, uh, a library from meta programming when, when a language feature would, would, um, be the superior choice, which is reflection.

[01:59:58] **GLEN FERNANDES:** Now, [02:00:00] this happened in 2018, reflection is now, you know, guaranteed thing for C++ 26. Um, you could say in that interim, uh, the world would've benefited from MP 11 being in the standard. But, uh, at the same time, you know, maybe it's one may, maybe it, it, it's one of those things that, um, [02:00:30] reinforces the idea that's, that, uh, we shouldn't necessarily depend on the standard to get certain features.

[02:00:35] **GLEN FERNANDES:** Maybe the right thing is, you know, um, you have libraries like Boost or library collections, like boost, uh, fill, fill the need and, and my per my personal view now has, has also shifted in that direction that it, it isn't so important to, to get, um, to get things into the standard because it, it, uh, it's. [02:01:00] Yeah, it, it that maybe Boost is a better place for things to live.

[02:01:05] **GLEN FERNANDES:** So if, if I look at different, uh, iterations of the standard, um, you know, they're frequent and they introduce many, like, they introduce, you know, some, sometimes very, uh, prominent language features. I, the impression I get from is that a lot of these don't have a high level of adoption, like modules, for example.

[02:01:27] **GLEN FERNANDES:** Um, you know, I I, that's [02:01:30] not to say they're not being adopted. 'cause you know, surely you'll find people that say, oh, our organization completely depends on, on modules and, and we, we use this language feature. But, um, it seems like the standard is, is is evolving faster than people are adopting. And, um, that, that, that creates this space for, for library collections that support all the way up until older standards, you know, to, to, um, to thrive.

[02:01:53] **GLEN FERNANDES:** Right? I should not be, you know, like, um, uh, [02:02:00] yeah, I think there's a great page. I should, I, I want everyone to read, um, that Peter Dav wrote about the Boost, uh, software license. Um, the thing I will say about it is, um, lawyers at various companies have looked at it and have found it, you know, to be more permissive and better, you know, uh, less, um, uh, difficult to adopt than almost every other license.

[02:02:27] **GLEN FERNANDES:** Right. There are, there are few, few [02:02:30] exceptions I guess, but, um, I think it's, it's, uh,

[02:02:39] **GLEN FERNANDES:** yeah, I, I, I, yeah, I, I wouldn't say, I don't wanna make a statement like, oh, you know, the Boost license is great because unlike the MIT license, it, it, it doesn't require you to ship the license with, with your, you know, the, the, with binaries and things like that. But I would, I would say, um, read, read the page created by Peter Dema on, on the, on the Boost.

[02:02:57] **GLEN FERNANDES:** On the boost software license, and yeah. What, what, uh, [02:03:00] in your opinion, so like what does attribution mean in the context of an open source license like this? Having to give, uh, credit basically, yeah. Attribution in that sense is, yeah. Giving credit. Yeah. 

[02:03:11] **RAY NOWOSIELSKI:** And why do those details matter? Who gets credit and where within, you know, open source libraries

[02:03:21] **RAY NOWOSIELSKI:** or does it, what's your thought? 

[02:03:22] **GLEN FERNANDES:** No, I think, I think in this sense in the, in the license, it's that you don't have to publish the boost license along with your, with your [02:03:30] release. So, you know, you can use it and, um, you know, but you don't have to ship it. Um, yeah, I, I would not take any of this because again, like, you know, it's, it's something that, uh, yeah.

[02:03:45] **RAY NOWOSIELSKI:** Well, do you have a strong opinion about, um, attribution in binaries? 

[02:03:50] **GLEN FERNANDES:** Um, 

[02:03:52] **RAY NOWOSIELSKI:** yeah. And what does that term mean to you? 

[02:03:57] **GLEN FERNANDES:** Yeah. So I do, I do, you know, I do, I do have a [02:04:00] personal opinion on that, and I, and I don't, I don't like it. And, and, you know, um, and I can see why organizations would, would, uh, would try and avoid it, but avoid what, avoid attribution in, um, in, in binaries.

[02:04:15] **GLEN FERNANDES:** Again, it, it, it gives them more freedom in how they, you know, and what they ship to the public, right. Without having to, um, publish certain pieces of information and what, what they're using. So, um, I, I think, I think it's, you know, it, [02:04:30] it's one of those I things that, um, uh, makes people favor the boost license.

