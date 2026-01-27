# BOOST_JON_KALB_STRINGOUT_v01

- - - -
filmed Date: 2025-10-25  
location: Manhattan, New York   
camera: A / B  
audio: Lav 
type: INTERVIEW  
video link: https://vimeo.com/1158522715/6a087f6c07?share=copy&fl=sv&fe=ci ​​  
summary: Great on Characters & Story across Boost; Boost Steering Committee & BoostCon / C++Now, Boost Foundation, O’Dwyer & Sankle incident, “Boost was where the cool kids went, but after C++11 it felt like it became establishment,” future of Boost  
- - - - 

## Transcript Start

[00:00:00] **JON KALB:** I am Jon Kalb. I do C++ training. I'm a C++ software engineer who does training mostly at corporate sites and also run CPPCon and for many years ran, uh, C++ Now, the Boost Conference. And, um, uh, that's what I do. You know, I, I do think of that [00:00:30] as a, a, a mark of quality. The, in order to become a Boost Library, it's a pretty rigorous peer reviewed process.

[00:00:38] **JON KALB:** And so from the very beginning of my association, introduction to Boost, that's, that's what, um, I would think of as a, a, a mark of approval by the community because of the peer reviewed nature of the, uh, of the process to get a, a library into the Boost Library. [00:01:00] My parents were missionaries, so I spent much of my youth in Sierra Leone, west Africa.

[00:01:07] **JON KALB:** Uh, I was, uh, I started my first three years, primary years as a, uh, at a mission boarding school. Um, and then my, uh, my parents, we came back and lived in Kansas and I was, I stayed in Kansas through university years, um, and graduated. Then, um, [00:01:30] got a, a brief, uh, uh, contract, um, opportunity in Louisiana, but then got another contract and moved out to California and I've lived in the Bay Area since then.

[00:01:43] **JON KALB:** So that was about 1991. Well, the first kind of official thing I did with OR for Boost was creating, uh, the Boost user mailing list. So I worked for a company that did mailing lists at the time, and the only [00:02:00] mailing list that was associated with Boost at the time was just the Boost list, the Boost Developer list, and that was very high traffic with lots of really technical stuff.

[00:02:09] **JON KALB:** And so if you were wanting to use Boost Libraries and you were kind of a beginner, it was pretty intimidating and it really wasn't the right place to ask beginning particularly, but just in, in general user questions. This, uh, that mailing list was for developers asking developer questions. And so I said, well, we [00:02:30] should have really, uh, different lists.

[00:02:33] **JON KALB:** So I actually created the Boost user list and then, uh, about the same time also created what I call the boost announce list, which was just a very low volume list that we would use to say, here's a new library that's just been accepted, or here's a library that's under review, or, you know, uh, so it was not designed as a discussion list.

[00:02:51] **JON KALB:** I don't know that it has much to do with the childhood. I'm a software engineer. I'm technical. I have been, you know, science and math. That's where I am. [00:03:00] But it's true that, uh, my career, what's distinguished me really has been having to do with the community, whether it's moderating the user list, whether it is, uh, uh, setting up conferences, setting up user groups, being active at those things.

[00:03:17] **JON KALB:** That's, yeah, that's where I've kind of made my mark. Um, I, I do enjoy explaining C++ particularly, but I enjoy explaining and so I've, I've done [00:03:30] both conference talks and training classes. There's a slightly different skill there, but obviously a lot of overlap as well. And, um, and it's, but that's very much about engaging with people.

[00:03:41] **JON KALB:** And one of the things I've told people, I discovered that I really enjoy writing C++, but I actually enjoy talking about it even more. So, uh, I don't know if that makes me a less good engineer, but it certainly does make it, uh, easier for me or more natural for me to be a community organizer, which is kind of a, [00:04:00] a hat I wear as a community organizer for the C++ community.

[00:04:03] **JON KALB:** Well, one of the things that really, I don't know that I've found it as a surprise, except looking back on and realizing that in. That I, I have this theory that C++ is just so hard to do really, really well, that it humbles everyone. In other words, if, if you're with a group of people, of course the C++ community, like any group is gonna have people who are, you know, hard to get along with, let's just say.[00:04:30] 

[00:04:30] **JON KALB:** But, but what I've found is that even, even the most knowledgeable people in C++ tend not to be the kind of people that go around showing off their knowledge and, and acting like know-it-alls. And I think part of it is, as I said, um, you to be a know-it-all, C++ is pretty demanding. You'd have to know a lot.

[00:04:49] **JON KALB:** And so I think that almost anybody who has given a technical C++ talk at a C++ conference has had somebody point out [00:05:00] something on their slides that was in error. It's just a very humbling experience. 'cause it's really hard. And I think that's part of it, is that, that what's been rewarding for me about being part of this community is that it isn't a bunch of people who are arrogant and boastful and those kinds of things.

[00:05:16] **JON KALB:** It's, it's a really supportive community. When people point out errors on slides at conferences, they really are doing this with the hope that you have an opportunity to improve. Not because they're trying to embarrass you in front of people. That's, that's not [00:05:30] the situation. In fact, even when someone points it out, it's almost always a question.

[00:05:32] **JON KALB:** It's like, wouldn't it be better if that was something And, um. And, and I, I really honestly believe it's just because C++ is challenging enough that it humbles everyone. And I think that's why it's a, it's a community that I've enjoyed being a part of. Um, I actually learned Pascal before I learned C and I learned Object Pascal before I learned C++.

[00:06:00] **JON KALB:** And so that, that shaped my first introduction to C++. When I learned C++, I said, oh, well this is just the c version of Object Pascal. And I worked with a fellow named John Mullins, who, who kind of patiently pointed out to me some code that he'd written that leveraged constructors and destructors in ways that just totally blew my mind.

[00:06:27] **JON KALB:** Nothing I had ever seen in, [00:06:30] certainly not in Object Pascal, which uses I methods, which is not a great way of, of doing construction. The C++ way is just better. It's just way more powerful. It lets you do RAII, which at the time I didn't even know what that meant. But, but John Mullins told, showed me some of these classes that he created that did management of resources, and my mind was blown.

[00:06:52] **JON KALB:** And I was like, we should write a paper about how to do this. This is such a cool technique. And he said, he said, John, I, [00:07:00] I think this is, everybody knows this. It's like, well, I didn't know that. And to me. It, I suddenly realized there's way, way, way more depth to C++ than there was to object Pascal.

[00:07:12] **JON KALB:** And my initial thought was just, well, this is just a slightly different syntax for what you got with Object Pascal. And it was really, uh, John was really the person who opened the door for me. And then, um, you know, the person I knew in my life at [00:07:30] that point, or shortly after that, I started reading books by Scott Myers and eventually, uh, Andrei Alexandrescu and Herb Sutter, and people like that very much, you know, shaped my thinking.

[00:07:41] **JON KALB:** And, but, but definitely at that point I began to realize, yes, there's a huge amount of depth in C++ that if you, if you leverage the complexity of that language, you can create libraries that are just so powerful and useful for users that, um, C++ is simply the [00:08:00] greatest language in the world for building libraries.

[00:08:03] **JON KALB:** Not necessarily because it makes it easy to build libraries, but because it's easy to build excellent libraries, it's easy to build libraries that allow users to, to themselves create functionality that's easy to use, but also, uh, safe, reliable, portable, all these kinds of things. Uh, and with. Unmatched performance.

[00:08:26] **JON KALB:** And that's, that's the real power of C++. It's [00:08:30] really a construction set for creating libraries. And that's what, uh, that, that, that's what the depth that I didn't, that I didn't initially appreciate, that I came to appreciate as I learned more about C++. It's just as I was thinking about it, particularly as I was thinking about how you could do programming in other languages, and I just realized that, uh, if you really are trying to make a library that other people can use that is [00:09:00] easy to use correctly, hard to use incorrectly, um, and very powerful and with, with unmatched performance, this C++ is just a language for doing that in.

[00:09:12] **JON KALB:** And, and I've been so immersed in C++, I haven't really thought much about other languages. And so that, it was only when I started thinking about other languages that I begin to appreciate why C++ to me is just such the, the language I, I wanna be working in. [00:09:30] Um, there's, there's a million different opinions in the world of programming and everybody has their own idea about what's the best language in the most library and why.

[00:09:40] **JON KALB:** Um, I, I can only say that I think the tools that the C++ language gives you for making libraries are just. Unmatched in my experience, right? Um, that doesn't necessarily mean it's the right language for every situation, and it's not necessarily, certainly not the easiest one, [00:10:00] uh, to develop in. But if your goal is to create powerful libraries for other people to use, that as I said, are easy to use, portable, flexible, and great high performance, uh, safe from memory leaks and inconsistencies and things like that.

[00:10:18] **JON KALB:** C++ is just a wonderful language giving you all sorts of really powerful tools to do that. I once heard someone say, or I guess I read it on the, on the internet, someone was, was talking and saying, [00:10:30] and they, what they said was, if your code is, is really that important, it's gonna get rewritten in C++ anyway.

[00:10:36] **JON KALB:** And what they meant by that was that the, the code that that runs the world, that's the most important code is the low level system code. It's the networking code, it's the code in, uh, in operating systems. It's the code in say, uh, application suites like Microsoft Office that are going to be [00:11:00] run by thousands of people where absolute performances just, it can't be traded away.

[00:11:06] **JON KALB:** Um, and that's. Uh, that does in a, in a very important sense, run our lives. Now, when you go to, uh, your typical website where, and maybe it's used by one small business, it's, you know, the restaurant that's showing you the menu and the hours and things like that, that's not gonna be run hundreds of thousands of times.

[00:11:29] **JON KALB:** They don't need [00:11:30] that to be squeezed out with the greatest performance. So they won't use a language like C++ for that. If I was making, you know, the, the, the code that I write to run the conference, it's not written in C++ because again, I don't need that kind of performance. I don't need it to run on multiple platforms and be, you know, infinitely scalable and all that kind of stuff.

[00:11:51] **JON KALB:** Those are challenges that are, um, that are met with C++. And that's the [00:12:00] tool you use if what you're writing is, uh, the, um, the kind of code that is absolutely mission critical for high performance with low resource usage. That's, that's what C++ is about. It's challenging to write, but it's, but it's at the heart of what we, you know, how we live our lives.

[00:12:24] **JON KALB:** Well, if they're watching this on the network, on the internet, it's almost certainly in the browser they're [00:12:30] using, not necessarily, there are other browsers, but, but C++ is, is a favorite choice for browsers. Um, the networking stack that, uh, that is, uh, making connections. It's likely that it's embedded in the router that they're using or something like that.

[00:12:48] **JON KALB:** So yeah, it's, it is the, it is the reliable system software of the world. Finance too. Yes. Oh, yeah. And finance, uh, [00:13:00] you know, it's one of the, one of the things that get, gets us a lot of interest from young people is the fact that most Triple A games are written in C++, because, again, performance is their biggest issue there.

[00:13:12] **JON KALB:** They, you know, they are creating a world, a visual world sound and, and visual, and they're driving the hardware, uh, as fast and hard as they can to create this immersiveness and this storytelling approach. And so they need a language that [00:13:30] does not compromise performance, but also has high level constructs.

[00:13:34] **JON KALB:** Um, and so that's one of the things that's kind of a limitation of C. C also has great performance. It's, it's the original system software language, but it. It scales out, this is debatable, but I would say at about 50,000 lines of code, if you have an application larger than that, it's starting to be, uh, harder to manage and see.

[00:13:55] **JON KALB:** Whereas C++ has all sorts of high level constructs that allow [00:14:00] you to create abstractions that make it easier to write code, create applications that have, um, well in the case of maybe a game or something like that, where you can just think about things in terms of, oh, here's this monster, or here's this, you know, this enemy, or whatever it is.

[00:14:18] **JON KALB:** And you don't have to think about it in terms of low level code, but instead you've created, uh, an abstraction within the, within the game world that you've created. And it just makes it easier to think about. And C++ has lots of tools for [00:14:30] that sort of thing. Uh, I think there's a, uh, yeah, exactly.

[00:14:35] **JON KALB:** I mean, experts need to know what the tools the experts are using and lay. People don't really need to know that. The problem gets to be when things become political. And in fact, um, there was a White House, uh, proclamation saying you should use safe languages. And the problem with that is not so much that people are concerned about safety, the problem is that the decisions being made [00:15:00] at the wrong level.

[00:15:01] **JON KALB:** The people at the White House are not software engineers and don't know, don't know what they're really saying, don't understand what those trade offs are, and that's where it's it. It becomes, maybe people should know how C++ is used, how extensively it's used, you know, that, that it's quite likely that the, uh, you know, transportation system that they rely on is, you know, has a backbone in C++ or something like that, that would be good for C++.

[00:15:28] **JON KALB:** But again, the [00:15:30] decisions if they're made at the right level, are made by people who understand the issues. Well, I had used, I used the Boost Libraries a little bit, but my biggest engagement was when I started to go to Boost Con. And so, um, I, I've been, I, I'm not absolutely certain whether my first Boost Con was in 2010 or 2011, but I just loved it.

[00:15:51] **JON KALB:** Um, it was so, uh, it is so exciting to meet people who were really at the cutting edge of what people were doing with [00:16:00] libraries, but also there was a lot of overlap between people who were attending Boost Con and the standards Committee. And so they were pushing the envelope for both what's going on in the library and what's going on in the language.

[00:16:12] **JON KALB:** And were passionate about and concerned about improving the C++ environment for programmers. The Boost Libraries were started by Beman Dawes. He had been the, uh, the, the chairman of the library subcommittee of the standards [00:16:30] committee when the first standard shift in 1998, the very first C++ standard, and the, the mission.

[00:16:39] **JON KALB:** The standards committee is to standardize existing practice. The problem was that almost all libraries that were in widespread use at the time, C++ libraries, were proprietary libraries. They were libraries that were simply not going to be acceptable as standards. That companies that owned the, the API wouldn't want those [00:17:00] to become part of the standard because those were things, you know, private libraries they were selling.

[00:17:05] **JON KALB:** So Beman was recognizing that in the future, if there were going to be libraries that were candidates for standardization, meaning libraries and widespread use, there needed to be some way of getting libraries and widespread use. Now, today, there's GitHub and there's it, we don't even think about anything like that.

[00:17:27] **JON KALB:** You, you, an open source [00:17:30] library on the, on the web is just, it's not even a thought. Just download it and use it. And, and particularly with GitHub, there's just tons and tons of open source libraries that you can just download and use. But at the time, that was completely unheard of. And so what, there was a need.

[00:17:46] **JON KALB:** There was a need. And, and Beman worked with other people in the standards committee, including Dave Abrahams and other people to create an organization, uh, where the idea was this would be a place where you could [00:18:00] get open source C++. And of course, the real. Thing that separated Boost from, well, I guess there wasn't anybody else really doing at this time, but the, but the truly innovative thing is that they said, we're not just gonna accept libraries that anybody wants to give us.

[00:18:15] **JON KALB:** They're gonna have to be peer reviewed. We're, we're going to have a review process for the submission where it's open to the public. Anyone can download the library, play with it, and make any comment you want. And the author is gonna respond to all the comments [00:18:30] before it's accepted. Now, that doesn't mean they have to accept everything or do whatever everybody says, but they have to respond.

[00:18:35] **JON KALB:** They have to say, this is noted, this is will be addressed in this way. Or, you know, this is a limitation. We'll accept, or whatever, whatever the response is. But this process of, of going through the peer review, it was just an amazing, amazing quality for, uh, for the Boost Libraries. And so when you say amazing quality, [00:19:00] so, um, boost was really cutting edge was really establishing what could be done with C++ using templates.

[00:19:09] **JON KALB:** Using modern C++ design was really pushing the envelope. Um, some people thought almost too much in the sense that they, uh, there was an maybe the, the trade off of complexity wasn't worth the benefits people got. But that was, but from my point of view, one of the things I, I, I liked about that is.[00:19:30] 

[00:19:30] **JON KALB:** People who were pushing the hardest at what could be done with templates and compile time approaches were essentially signaling to the standards committee, this is what the library needs built in. In other words, some of the things that, that people did, um, for boost that were so pushing the, pushing the language so hard were the kinds of things that the standards committee said, oh, let's build that in so it doesn't have to be that bad.

[00:19:59] **JON KALB:** Um, [00:20:00] and, and that's what the libraries, uh, were, they were literally cutting edge. They were the, the showing the way of what could be done with C++. Well, um, a number of, of the early libraries, and, and I should say that the Boost Library is, is very large. I'm, I'm not sure what the total number is.

[00:20:22] **JON KALB:** It's over a hundred libraries, a lot of them. And not everyone is gonna be appropriate for any individual use. Uh, [00:20:30] there's, there's a wide variety of use cases and a wide variety of even quality. But some of the libraries were just considered so valuable, so useful, such great tools that the standards committee was very eager to turn these libraries into part of the C++ standard, which was.

[00:20:53] **JON KALB:** The purpose, right? That's why Beman and the other people on the standards committee who helped set it up, uh, that's why they did [00:21:00] that. They wanted to create a, a breeding ground, if you will, uh, for libraries to become vetted, to become widely used, so that, that the mission could be, uh, could be applied, which is to say, we're gonna standardize things in widespread existing practice.

[00:21:17] **JON KALB:** And so, lots of things like, uh, one of the most obvious is, uh, Shared Pointer. Shared Pointer was this incredible, uh, innovation, very well engineered, very well designed, [00:21:30] and, um, became part of C++ 11. So, um, the, uh, the team of, of people who were boost authors, boost reviewers, people who were working on Boost got to know each other well, but only through email, only online.

[00:21:49] **JON KALB:** This was of course, way before Zoom. People weren't doing, uh, video meetings online at the time. It was just email. And so they kind of got to know each other, but they [00:22:00] also felt like they weren't getting to know each other. And so that's why there was a feeling, Hey, let's all get together. And so that's where the, uh, concept of Boost Con came from.

[00:22:11] **JON KALB:** It was an opportunity for all the people who were working and had met each other online to actually meet each other face to face. And so, I'm not. Um, I'm not certain that it would've actually been, uh, critical to the success of Boost. I think [00:22:30] Boost was successful before the conferences, but it's just a natural human, uh, desire when you start working with people, particularly people who you respect for their creativity and their intelligence and their ability to, to accomplish things.

[00:22:46] **JON KALB:** Gosh, I wanna meet this person, you know, I wanna buy you a beer, right? You wanna meet the person face to face. You want to have conversations with them. And one of the things that technical people know is that [00:23:00] ideas sometimes are a little bit hard to pin down in terms of, you know, writing something technical and going back and forth with really, you sometimes you want that crazy conversation that's a little people taking risks.

[00:23:16] **JON KALB:** 'cause it's not being recorded. It's just you and me talking. And out of that comes some great ideas and people know from experience that those kinds of conversations, casual conversations, sitting around, uh, the dinner table [00:23:30] or just while walking between sessions or things like that, casual, things like that can spark off incredible ideas.

[00:23:39] **JON KALB:** Um, the desire to have a face-to-face meeting was the, the inspiration for what would become Boost Con. Now un until. The conference boost was in this interesting, it was a $0 organization. It, it had no revenue because of course it was just free open source [00:24:00] software, but it also had no cost because the, uh, the costs of the servers and putting things were donated by, and I'm, I don't really know the facts here, but I believe it was Indiana University, uh, who was the, the financial sponsor for all the actual costs associated with Boost.

[00:24:20] **JON KALB:** So it was a $0 organization. No money comes in, no money goes out, and no. Now if you wanna have a conference, if you want to get people together, believe me, I'm well [00:24:30] aware that that's a very expensive and, and risky kind of thing because you, uh, for a conference, you make commitments about, uh, the space and food and AV and all the things, right?

[00:24:44] **JON KALB:** And if people don't show up, that's, that's where the risk comes in. And so, uh, that was, that was the inspiration. Let's have a conference. Well, in order to have a conference, as I said, there's now, it's no longer a $0 organization. Somebody's gonna have [00:25:00] to front some money or take some risks, sign some, some commitments, and some contracts.

[00:25:05] **JON KALB:** So at this point, and I don't know the history of how it all came together, but Boost and the Software Freedom Conservancy got together. Uh, boost was one of the largest. Uh, organizations for the Software Freedom Conservancy. And I know that they were, 'cause they told me some of this stuff. They were the first, they were the Boost was the first organization that, that had a [00:25:30] conference.

[00:25:30] **JON KALB:** And so they cut their teeth on, on being the sponsor of a conference through Boost. Okay. And Dave Abrahams, whose father was a physicist, had a long history of attending the, uh, Aspen Center for Physics. And so he thought of that when it was time for the Boost Conference. And he said, Hey, that's a great environment.

[00:25:55] **JON KALB:** It's small, it's beautiful, and it's [00:26:00] designed for physicists to get together and talk technical stuff and share ideas. Let's see if we can do that. So he contacted them and said, we have a small nonprofit. We would like to spend a week some time when, uh, when, when the physic, when the physics center is not being used for physicists.

[00:26:18] **JON KALB:** Is that possible? And they said, yeah, we can do that. So that's where that came from. Now, um, my understanding was that, uh, [00:26:30] Dave and Beman literally put down their own personal credit cards as. As security to guarantee the rooms. And I don't think it came to that because I, I think that from the beginning, boost Con was successful enough that it paid for itself, but there was a risk there and, and some of the early Boost people took, took that risk on.

[00:26:51] **JON KALB:** Personally, when I first heard about Boost Con, my, my initial reaction was, I think Boost is really cool, but I'm not sure I wanna spend [00:27:00] an entire week just talking about Boost. But it was only when I talked to some other people who had attended that they said, oh, no, no, it's really a C++ conference, but it's, it's focused on cutting edge library development.

[00:27:13] **JON KALB:** And of course Boost is a lot of the topic, but it's really about better quality C++, particularly better quality C++ libraries. And so it's like, oh wow, why didn't they say so? So that's when I started there. It is true [00:27:30] that there really wasn't a C++ conference. Um, there was something called SD West, and SD West was from Software Developer Magazine.

[00:27:41] **JON KALB:** There was also West SD East, but I never attended that. But SD West, which was in the Bay Area, and it was not specifically or, uh, exclusively about C++, but most of the attendees were C++ engineers. And so there was a lot of C++ content there. Um, the ACCU in [00:28:00] England was also very much C++, but.

[00:28:03] **JON KALB:** But explicitly not C++ only. Uh, and so there really wasn't a C++ only conference anywhere. Um, and I didn't really that, that, that really wasn't a big concern of mine until SD West announced. We are no longer gonna have an SD West. This is the last one. And so that's the next time I went to, [00:28:30] uh, to Boost Con.

[00:28:31] **JON KALB:** I talked to Dave Abrahams, who was the chair of Boost Con and I said, there's SD West is going away. And I know that he knew him. I actually had met him, um, at SD West. The two of us happened to both be attending and there he was, says, Hey Dave. And, uh, so I knew he knew about it. Uh, and I said, look, that with, with that passing, there's no large C++ conference.

[00:28:55] **JON KALB:** Uh, because SD West was much larger, of course, than Boost Con. Uh, but, but there's [00:29:00] no C++ conference in North America at all. And there should be, there just should be C++ is just too important to not have a conference. And what I would like to see is, and I kind of pitched him, I said, look, this is, this was in 2011, by the way.

[00:29:16] **JON KALB:** So this, the major release of the standard has not yet. Been formally happened because this would've been May of 2011 and the standard didn't come out till later that year. But we knew it was coming out. We were right on the edges, very clear [00:29:30] it was gonna come out. And I said, next year, 2012, everybody is gonna want to know about the new standard.

[00:29:37] **JON KALB:** And having, uh, at that time, boost Con was two tracks. I said we should have a third track devoted to tutorials on the new language, and that would be popular. I said, we should, we should focus on getting more attendees. We should add this third track as a C++ tutorial, specifically about the new C++.

[00:29:59] **JON KALB:** And we should [00:30:00] change the name because it shouldn't be Boost Con, it should be something with C++ something with C++ in the name. And Dave was quite receptive to that, but he said, you know, this isn't my decision to make. He said, every, the last night of the conference, we have a committee meeting to kick off next year's conference, and that is the planning committee for the conference.

[00:30:27] **JON KALB:** And so they make this kind of decision, you [00:30:30] should make your presentation at that meeting. And so I did. I showed up and I said, here's what I think we should do. And basically said. To them. What I had pitched to, um, to Dave and I said, we should call the conference the future of C++ conference, because that's kind of how I'd seen Boost as this is the cutting edge.

[00:30:52] **JON KALB:** We're showing people where we're going and these ideas in the Boost Library are going into the standards committee and are [00:31:00] becoming more and more popular. And we're showing people how to write high quality libraries. So to me, boost had always been kind of the cutting edge, the future of where we're going with C++.

[00:31:12] **JON KALB:** But the, but the meeting, the committee loved everything I proposed. They wanted increased attendance. They wanted to add another track. They were excited about what, how I laid out what that track could be as a tutorial for, uh, C++ 11. All of it was, but they did not like my idea [00:31:30] of the name of the conference.

[00:31:31] **JON KALB:** They said, we don't want, we're too impatient. We don't want C++ in the future. We want C++. Now. That's where the name of the conference came from. We called it C++ now. So, uh, we announced then that we were changing the name of the conference and that we were going to have, uh, uh, content for C++ 11 and that.

[00:31:54] **JON KALB:** That's what we did. What, what happened was I kind of felt like, you know, [00:32:00] this was kind of my idea and my vision, and I was really glad that other people loved it and embraced it because I thought, this, this is just gonna happen. But what happened was we didn't get submissions to present all these tutorial sessions.

[00:32:15] **JON KALB:** And so as the deadline for submissions got closer, um, we were kind of concerned about that. And so I took it upon myself. I basically made a list of the kinds of sessions I thought we should have. We should have something on [00:32:30] Lambda expressions and a couple of sessions on Concurrency. And we should have, you know, something about move semantics and all these, I filled in the, the boxes of the sessions I thought we should have.

[00:32:40] **JON KALB:** And then I started contacting people and I said, particularly people maybe who had proposed these uh, features or whatever, and said, could you, could you give this talk? Could you come and give this talk? Could you give this talk? And pretty much fill that out. And I think it was when [00:33:00] Dave saw that I had done that, Dave reached out to me and this was in clutter, incredibly flattering to me.

[00:33:07] **JON KALB:** Uh, Dave said, Jon [Kalb], this is your vision. I think you need to be involved to make it happen. I would like you to be co-chair of the conference. And to me, I was not a boost author. I wasn't a big wheel in the boost world. And I felt just. Like, wow. Um, and so, um, I said, okay, I'm gonna, I'm gonna step up and do everything I can.

[00:33:29] **JON KALB:** And [00:33:30] I envisioned my role as the person who handled legis logistics of the conference and let Dave be, um, the person who was the, uh, visible because he was a big wheel in the big, in the boost world. People knew who he was. He had a lot of influence, deservedly so, he was quite the leader. Uh, and so, uh, he was the kind of person who could welcome people, who could reach out to potential keynote speakers and invite them and things like that.

[00:33:56] **JON KALB:** So I saw my role as I'm gonna handle the [00:34:00] contracts and the, you know, handling, uh, anything having to do with food or AV or all the logistics that is maybe, you know, not as exciting, but absolutely necessary to make a conference happen. So that was, that was then, uh, so, so C+ the first C++ now then was my first time as co-chair.

[00:34:22] **JON KALB:** And then it went from there. The, the Boost Con experience was quite amazing. You would go into [00:34:30] Aspen. In the off season. So it was an amazing, you know, sleepy little ski town when there, when there was no skiing going on because of course we couldn't possibly afford to have a conference there when there's ski season, right.

[00:34:44] **JON KALB:** But it's beautiful. Uh, it's in the mountains, it's quiet and gorgeous and it's, it's an incredible experience. So you fly in this little tiny airport and then the resort would arrange a shuttle for us, [00:35:00] and you show up and here are all these people whose up until then, you've just seen their names as Boost authors.

[00:35:07] **JON KALB:** And then you got to meet people like Dave Abrahams and Beman Dawes, who you, you know, particularly, uh, Beman as chair of the, uh, library subcommittee of the standards committee had been very influential. He was much loved and, and very, very, uh, uh, respected for his contribution [00:35:30] to what became the C++ standard library.

[00:35:33] **JON KALB:** And, um, just to meet these people, to meet all these boost authors was just amazing. So, um, my experience, and as I said, I've been involved with, uh, community activism for, uh, community engagement for, uh, the C++ community. And for the most part, people are not drinkers. It's not that they're not social drinkers, but I, I think.[00:36:00] 

[00:36:00] **JON KALB:** Um, you know, maybe when people get drunk, they, they think they're doing their job better, but they don't know that. The problem is if you're a programmer, you have evidence afterwards and you realize that you are not doing yourself any favors when you were writing code, when you were intoxicated. So, I don't know if that's the case or if it's just a natural thing, but people who write code tend to be less, uh, interested in drinking.

[00:36:22] **JON KALB:** Um, so there's definitely, I mean, there, there was basically people would [00:36:30] socialize at the bar, but it was mostly talking and getting to know people and sharing ideas. And it was an incredibly exciting time. There was still a lot to be learned and a lot to explore. Um, a lot of new techniques were being developed and, um, so yeah, there was a lot of excitement then and there.

[00:36:51] **JON KALB:** This was, uh, before C++ 11 shipped, we were still looking at boost libraries that were [00:37:00] becoming part of the standard and, uh, which ones were gonna make it as part of the standard, and how were they going to be changed and what was the impact going to be on Boost when those libraries became part of the standard.

[00:37:13] **JON KALB:** Um. And meeting, meeting the people who are shaping this meeting. People like, uh, Jeff Garland who, uh, he ran something we call Boost Library in a week, which is an opportunity, it's, it's a hands-on part of the [00:37:30] conference. Um, it's nice to have a conference that's not just Sessions, it's, you can actually participate.

[00:37:36] **JON KALB:** And so the idea with library in a week was that Jeff Garland would pick a topic, some library, and the idea was that in one week we would have a new Boost library, uh, because people at the conference would, would start working on it. I don't think we ever got anything even close to a library in a week, but that wasn't really what it was about.

[00:37:57] **JON KALB:** What it was about was the opportunity [00:38:00] to work with people to learn how, you know, I, I definitely talked to people who told me that they learned so much in, in working with some of these boost authors on library in a week because they got to sit down with them and, and talk about specific problems and how do we approach this and what's the solution to this and how do we deal with this.

[00:38:19] **JON KALB:** Gosh, what can I tell you about Jeff [ Garland]? Um, Jeff is, uh, a consultant in from Arizona. Um, I believe his big client is, [00:38:30] is or has been, uh, the Boeing company. Uh, I don't know what exactly he works on. Um, but, um, I, I, I don't know if I can tell you. I mean, he's been, I. Um, uh, I don't know if there's great anecdotes to tell you about Jeff.

[00:38:50] **JON KALB:** I can't really think. I do remember, um, Dave, I don't know what year this was, but Dave saying, has anybody heard from Jeff? Are [00:39:00] we doing library in a week this week? And so this was literally at the conference and it's on the schedule that we're gonna do library in a week, but nobody's heard from Jeff.

[00:39:09] **JON KALB:** Nobody knows what the project's gonna be. And of course, Jeff shows up and he's got a great idea. And so it went really well, uh, because he just assumed, well, we're gonna do this. And everybody just kind of assumed, yeah, Jeff's gonna do this. But he hadn't really been, uh, communicating with people about it.

[00:39:24] **JON KALB:** It was a, it was just a, I shouldn't say it was a surprise. I don't know where Beman [00:39:30] lived or was from. Um, I do know that he was an independent software consultant. Um, and so I, I don't know, I didn't really get to know him that well personally. I did interact with him because he was, again, a Boost leader.

[00:39:47] **JON KALB:** And so as I became more, more engaged with the conference, I had more and more, uh, discussions with him about, about things. But I was never, uh, I didn't really get to know him [00:40:00] very well personally, which is kind of a regret of mine. So Dave lived in the Bay Area, and so, like I said, we, we ran into each other at SD West.

[00:40:09] **JON KALB:** Um. He, uh, was interested in music and got into computers because he wanted to write software that could write music notation. And that was what drove his interest in becoming a programmer. And so, uh, he [00:40:30] would bring his guitar to the conference and we'd, like at the picnic or something like that, would play guitar and get other people to join him.

[00:40:39] **JON KALB:** Um, I'm not real musical, but that was, that was very important to Dave. He's a very musical guy, and that was his, that's where he got interested in, in programming was because he wanted to, as I said, write software for capturing musical notation. So John Maddock, uh, was [00:41:00] very important to the Boost Libraries, but he never came to the conference, I don't think if he did, it would've been probably in the early years before I attended.

[00:41:09] **JON KALB:** So I never met John [ Maddock]. Um, but he was an important figure in the libraries. Um, and online. Um, I did meet, uh, Marshall, but I already knew Marshall Clow, and Sean Parent and Lisa Lippencott and I had, and Nevin Liber [00:41:30] were all Ex Mac hackers. We were all Mac people who had met at. Well, I mean, I met them all at Mac Hack.

[00:41:37] **JON KALB:** It's possible that they had met each other before going to Mac Hack, but, but we were all Mac hackers. We all saw each other at Mac Hack. And so Mac Hack was a conference, uh, dedicated to MAC programming. And that attending that early in my career definitely affect what I thought conferences could [00:42:00] be, and that definitely has affected my, uh, wanting to be involved with, uh, Boost Con.

[00:42:08] **JON KALB:** And what became C++ Now and CPP Con? Well, it wasn't clear at the time that we were all going to become, uh, big C++ fanatics because we were just all different Mac people doing different Mac stuff. Um, but that's how we first got to know each other. Um, [00:42:30] and then as I said, you know, um, different Mac people pursued different things, uh, different languages, different kinds of concerns, but, but those I just named, uh, were all name, uh, well, uh, Sean Parent, uh, Lisa Lippencott, uh, Nevin Liber, Marshall Clow, probably embarrassed myself because I probably forgot somebody really obvious.

[00:42:54] **JON KALB:** But, um, all of us were Mac Hack attendees and had known each other. [00:43:00] Um. Um, you know, long, long before becoming involved with Boost or, or C++ Now, or CPP... well, I don't know. Um, so I'm not sure that they were necessarily, they were all influential in the C++ community. I'm not sure that Lisa was terribly involved with Boost or necessarily even Sean.

[00:43:22] **JON KALB:** Uh, I think he did some early boost stuff. Sean [ Parent] was the first keynote for the first Boost Con [00:43:30] and I remember, so I wasn't there for the first year, but I do know people still talked about it, particularly Dave, who said that was an amazing keynote and it really, really kicked off the, uh, the conference, uh, in an amazing way.

[00:43:44] **JON KALB:** Hartmut [ Kaiser] was, yes, definitely. He was the program chair for Boost Con and for C++ Now in those early years. Yeah. What was he, what was, what was he like? So he's a professor in [00:44:00] LSU in Baton Rouge and works on, um, high Performance computing and, um, has been really, really, uh, supportive of Boost, supportive of the conferences.

[00:44:14] **JON KALB:** He still sends students, you know, we get people from LSU who show up at C+ now, and CPP Con, um, who are, you know, really talented people who Hartmut has kind of steered our way. Um, [00:44:30] so. I figured this out kind of only after the fact. But, uh, when the, when the fiscal sponsorship was set up with Software Conservancy for Boost, this was done, as I said, for the conference.

[00:44:45] **JON KALB:** It was before we had a conference. Uh, there was no reason to have a fiscal sponsor because it was a $0 organization. But with, uh, the conference and signing commitments and [00:45:00] making, you know, uh, taking on, uh, financial risk, there needed to be a fiscal sponsor. And the Software Freedom Conservancy did that in the early years.

[00:45:11] **JON KALB:** Um, the role was effectively that they had, they followed whatever Beman said, and it wasn't, I don't know how even formal that was. It was only when we formed the Boost Steering Committee that I realized. And [00:45:30] even when we did that, I hadn't really asked the question before that, well, what did we do before the Boost Steering Committee?

[00:45:37] **JON KALB:** But, um, with the, uh, with my involvement as co-chair of C++ Now, um, when Dave and Beman wanted to set up the steering committee, they asked me, would you be on the steering committee? And I was happy to do that. Um. [00:46:00] It didn't, it didn't, as I said, it was only much later that I asked myself, what did we do before we had the steering committee?

[00:46:09] **JON KALB:** Because the role of the steering committee was to make decisions and to tell the software Freedom Conservancy, which was the legal entity of Boost. In other words, you know, boost was a, a project, but there was no legal entity there. If you were trying to sue Boost, you couldn't, and I'm not suggesting anybody want to, but I'm just saying, [00:46:30] if you were gonna sue Boost, what you'd really sue would be the Software Freedom Conservancy.

[00:46:33] **JON KALB:** Because Boost was just a project of the software Freedom Conservancy, the Software Freedom Conservancy, effectively owned Boost. And they did whatever Beman said, oh, we should spend money on this, we should do this, we should do this. And it was kind of an informal thing, and it never really got challenged because, I mean, Beman wasn't doing anything wrong or irresponsible, so nobody but talked about it.

[00:46:56] **JON KALB:** But the, but eventually, um, Dave [00:47:00] and Beman decided that there needed to be a formal organization that could be responsible for making decisions for Boost. And so they, they came up with what they called the Boost Steering Committee. And it was, uh, it was an organization whose job it was to effectively do two things.

[00:47:20] **JON KALB:** One is. To approve expenses. You know, if a decision had to be made about are we gonna buy test machines or are we [00:47:30] gonna sign this contract for the conference or whatever, there's an organization whose job it was to approve those things for the software Freedom Conservancy to do for us. And the other thing was, if there was ever a situation understand that Boost ran based on consensus, people did things because people at Boost agreed that's what we should do.

[00:47:53] **JON KALB:** And for the most part, that worked really well because there was no conflict over. I mean, the decision [00:48:00] is, should we do this? Well, if you had people willing to do it, then they went out and did it. And so it wasn't really like a, a, a controversial kind of thing. If there were people willing to do it, then obviously it should be done.

[00:48:13] **JON KALB:** And so we did that. But the problem would be what if we actually had a situation where we had to make a decision, we either do X or we do not X. And there's no, no obvious consensus to come out of it. And [00:48:30] I think Beman and Dave looked down the road and they saw that there was a, um, an issue that was going to happen with how the repository was done.

[00:48:42] **JON KALB:** And switching to GitHub and using GitHub as the repository and the. I think that that's in part what motivated them to create the, the steering committee is they knew that at some point a tough decision was gonna have to be made. And they [00:49:00] didn't feel, it wasn't that they were willing to take the heat for it because they were on the steering committee and they knew that if it was an unpopular decision, they'd have to take the heat.

[00:49:08] **JON KALB:** But they didn't feel like they were empowered to make that decision, just the two of them. So they set up a committee whose job it was to be the governing body for the organization, so that if a difficult decision had to be made, there would be a formal vote. It would be decided in a, you know, well, one of the things [00:49:30] that BNE had pointed out a few times is that most languages, computer languages, particularly SEC successful ones, have had some company that promoted the language.

[00:49:43] **JON KALB:** And so, um, it might be, um, it might be like Apple would promote Swift so that developers would use Swift for developing on the Apple platform or whatever. Other languages have had someone who's who, some [00:50:00] company that promoted the use of the language. For whatever reason, C++ was created by at and t certainly had tons of marketing muscle.

[00:50:11] **JON KALB:** At t's view of C++ was that this is a great tool we're gonna use internally. They didn't care if anybody else ever used it. And so they, they spent $0 marketing C++ outside of at and t. That wasn't a priority for them. And so C++ is one of the few [00:50:30] certainly successful languages that didn't have some big corporation promoting it in some way.

[00:50:38] **JON KALB:** And some people felt like, well that was maybe a missed opportunity. And so that's, I think part of what caused the Boost Foundation to be, to be established was what if we could set up a nonprofit organization to get some funding from the corporations that have a major investment in C++, they [00:51:00] would invest in helping to promote the language.

[00:51:02] **JON KALB:** Because you know, even for at and t, it might be a little shortsighted to say, well, we're gonna use this language internally. We don't care if anybody else does it. Well, how are you gonna hire people who are experienced in this language? How are you going to be able to find, uh, of course in my case, I think about trainers who could come in and train your people on how to use the language.

[00:51:21] **JON KALB:** You want that language established, you want it to catch on, you want it to be popular, you want there to be books about it, videos about it, et cetera. And so, [00:51:30] um, and so if you are a company that's made a significant investment in C++ development, why not join the C++ foundation and give a membership fee to them to help them promote the language?

[00:51:42] **JON KALB:** So that's what the foundation was about, was to promote by who? When? Um, well it was, it was Herb and I don't know many of the details. I got the impression that Microsoft and Google did a lot of the early heavy lifting financially to make it happen. I don't [00:52:00] know anything about bad blood, about Boost Pro.

[00:52:03] **JON KALB:** Uh, Boost Pro was, uh, uh, Dave ran that as a, uh, the opportunity for a company that's using Boost Libraries to pay someone to be there to answer questions and to fix critical bugs. So with an open source library, you have this wonderful product that's available free. You don't have to pay for it. But the flip side of [00:52:30] that is if you run into a critical bug, what do you do?

[00:52:33] **JON KALB:** Well, the idea with Boost Pro was you could pay a fee to Dave and he's on the hook. If there was a Boost Library critical issue, you could contact him and he would get to the bottom of it one way or another. And that was, uh, that's what Boost Pro was for. Um, I don't know of any bad feelings that came out of it.

[00:52:53] **JON KALB:** I don't think this was terribly successful. Um, I don't know. You know, I, I don't [00:53:00] know any dollar amounts or anything like that, but I don't think it, it was terribly successful for Dave to be able to do that because I don't think that a lot of companies took him off on it. But I don't know any details about that.

[00:53:12] **JON KALB:** So I, in a, in a sense there might be, I don't think it had anything to do with the timing. I think that was coincidental. Right. Uh, Beman simply retired, um, and, uh, day, uh, excuse me. Uh, [00:53:30] Doug worked for Apple and, uh, Apple's priorities shifted into this new language that at that time we'd never even heard of yet, but it was to become swift.

[00:53:42] **JON KALB:** Um, and they hired Dave, and Dave was in a position to be the creator of the Swift Library. And what an amazing opportunity for someone who had worked on the standard library for C++. It's like, Hey, here's a brand new [00:54:00] language and you can shape the library for this. And that was just, you can see it.

[00:54:06] **JON KALB:** It's an amazing opportunity. And so Dave and, uh, Doug became kind of heads down on Swift, and I don't think it was much as. Uh, you know, that they wanted to leave C++ as that they found this incredible new opportunity to, uh, to develop something completely new and something that would be their own.

[00:54:27] **JON KALB:** So I don't think that, um, [00:54:30] uh, and I, I think it's, it's, it, I mean, it's, it's no question it was, it was sad for Boost to lose all three of them, um, because I think that their leadership could have maybe made things better for Boost, but I don't think there was anything, I don't know of anything that was necessarily nefarious about it or that it was coordinated, or, one of the very sad things is a, a, a bit of a surprising thing [00:55:00] is that I would've thought that having almost all of what got rolled into the C++ standard for C++ 11 was libraries that came from Boost.

[00:55:16] **JON KALB:** And to me, you'd think that would be a huge endorsement of Boost and everybody would be excited about, let's, let's learn more about this. But what happened was the exact opposite. What happened was [00:55:30] Boost went from being the repository of all these cool language libraries that you really need to have access to and you really need to have in your code.

[00:55:41] **JON KALB:** To suddenly being a collection of libraries that weren't good enough to be in the standard. In other words, the best Boost libraries were now in the standard. And the ones that were left, admittedly they were the less important libraries because obviously the most important ones [00:56:00] were the ones that were into the standard.

[00:56:02] **JON KALB:** But instead it just felt like, well, you don't really need boost anymore because the things you really need to boost for, they're in the standard now. And so instead of people appreciating Boost more, because it was this wonderful source of high quality libraries, it was now people were appreciating Boost less because the very best of those libraries were now available from the standard.

[00:56:25] **JON KALB:** To me, that was always kind of ironic because as I said, [00:56:30] that was not how I saw the world. What I saw the world is there's still a lot of important valuable stuff in Boost, but other people were like, eh, it's not the important stuff. The important stuff all went into the standard and um, that was kind of dispiriting.

[00:56:45] **JON KALB:** And if that happened at about the same time that Beman retired and Doug and Dave started working on Swift and we lost them, um, that [00:57:00] was a lot of bad timing and it did affect the perception that people had outside the world, uh, the outside community. On Boost and Boost development. Um, I guess as you pointed out, I could kind of see people seeing it that way.

[00:57:17] **JON KALB:** Mm-hmm. I wasn't involved enough in the, the internal politics of the committee to know if that was happening. You know, one of the things, um, [00:57:30] there's a particular library that did make it from Boost into the standard and it's the Boost Bind library. And it turns out that Lambda expressions pretty much do what Bind does in a much easier way to do.

[00:57:50] **JON KALB:** And so if Bind had not gone into the library, I don't think anybody would've missed it. And I say that a little bit strong because I know that my friend Michael Caisse would disagree with me, [00:58:00] but he was a big boost bind user. But Bind was a little bit hard and tricky to use. And Lambda expressions are just a much easier, more natural way of, of doing be because it's an extension of the language itself.

[00:58:18] **JON KALB:** It's. It's easier to express it. The library solution, which Bind did is, is a workaround for the limitations of the language. So with C++ 11, they introduced [00:58:30] Lambda expressions. You don't really need bind anymore. Lambda expressions do what Bind does in a better way. Um, so there might have been things that were in, in Boost that were overcoming limitations of the language, like Boost bind.

[00:58:48] **JON KALB:** And so not everything in Boost would make sense to be. In fact, there was actually a library called Boost Lambda, which was, again, it was a library [00:59:00] way of doing Lambda expressions and it's in many ways, you know, Scott Myers did a review comparing the language approach that the committee did with the library approach that Boost did.

[00:59:12] **JON KALB:** And he found some things about the library approach that he felt were better. But I think having to be able to go in and change the language to make Lambda expressions, that's pretty powerful. And that means that the Boost Lambda Library doesn't need to be in the standard and [00:59:30] boost bind doesn't need to be in the standard.

[00:59:32] **JON KALB:** These were created to overcome language limitations. You can put 'em in the language itself, then you don't need these libraries. So I think that there might have been some. Uh, certainly are some things in the Boost line, the boost libraries that, um, that the language, the language advances mean they're not as important in the, in the library.

[00:59:59] **JON KALB:** Um, and then [01:00:00] there are things in the library, for example, there's a Boost Python library, and it's specifically designed to make it easier to, uh, to use Python objects from C++ and to use C++ objects from Python. I'm not sure that really makes sense to put into the standard at all. That's almost certainly should always be a, you know, third party opportunity, you might say.

[01:00:24] **JON KALB:** Yeah. Uh, but I actually think there's a lot of things that should not go into the standard Library. [01:00:30] Um, and that does, I think that that's, uh, from my point of view, the, the, the fact that Boost Libraries were accepted and as are a major part of the Standard Library is a credit to boost. That was in fact why Boost was created, right?

[01:00:49] **JON KALB:** Was to be a proving ground for potential libraries, a way of making libraries in widespread usage, because that's the mission of the standard is to [01:01:00] standardize, uh, things that are in widespread usage. Right? Um, and so Boost is a, is a tool to achieve that, but absolutely not every. Not every library that's accepted into Boost is a realistic candidate for the standards committee, not because of a quality issue, but just because certain libraries, no, it doesn't really fit with what the standards should be about.

[01:01:23] **JON KALB:** Mm-hmm. Um, there may be two esoteric, two domain specific, [01:01:30] or you know, two niche or whatever. So, um, in a sense, when I approached Dave at, at Boost Con 2011 and said, there should be a large C++ conference in the United States in North America, CPP Con was effectively what I had in mind. That was my vision and my [01:02:00] thinking was Boost Con could evolve into that.

[01:02:04] **JON KALB:** And so the first step was C++. Now we increased attendance and increased the number of tracks adding this third track. Uh, but what happened was at a certain point there was some pushback largely from Dave himself who said, look, this conference shouldn't get any larger. Partly because again, he was very much in love with [01:02:30] the physical.

[01:02:31] **JON KALB:** Uh, venue and thought, we don't wanna overrun this venue. This is designed to have a certain number of physicists here, and we can have a conference of a certain size, but above a certain size. It, we are taxing what we can do, and it's not, it's not good for the venue. Um, but in making that argument to me, I recognized perhaps Boost Con could become this larger general C++ [01:03:00] conference that I wanted to create, but perhaps it would fail.

[01:03:05] **JON KALB:** But in trying to make that happen, it was gonna destroy this incredibly great conference. Don't risk that. Boost Con as it became. C++ now is an amazing conference. It's just an amazing community. It's a wonderful experience to attend, whether you're a presenter or just attending as a non-res presenter, it's, it's an amazing [01:03:30] experience.

[01:03:31] **JON KALB:** And don't mess with that. Even if I had something else I wanted to make, even if it made sense, even if that would be valuable, don't destroy this conference in the process. Maybe we could have gotten to this other conference. Maybe that's possible. But in any case, what we were risking was not worth risking.

[01:03:54] **JON KALB:** And I was disappointed at that realization because I really did want to [01:04:00] create. At this larger conference. And so I'd mentioned earlier that every year, uh, at C++ Now was the last night of the conference. We have a, a me a meeting to kick off next year's conference. And so I went to that meeting and I said, uh, look, uh, I had plans to grow this conference.

[01:04:24] **JON KALB:** We had already grown it pretty significantly, just the first couple of years of C [01:04:30] Plus Plus Now. And I said, that was my plan to continue to grow it. And I had these ideas about how we could make it bigger before we physically move from the physics center, which eventually we'd have to do if we got larger.

[01:04:44] **JON KALB:** Um, but the standards, the, the steering committee has voted that we're not going to pursue that. We're not gonna get bigger. In fact, we're gonna set a cap and we're not gonna be as large even as we were this year. And I [01:05:00] said, you know, I had a vision for a much larger C++ conference that would be an international conference for people to come together, uh, talk about C++, it would be much larger.

[01:05:11] **JON KALB:** And, um, but we're not gonna turn this conference into that. And so we had their meeting and we had the regular planning meeting. Well, what are we gonna do next year? Who should be the keynote speaker? What are we, you know, all those kinds of things. But as we had the meeting, people would keep saying. Well, this other C++ [01:05:30] conference that you were talking about, would it be, and they would ask some question and I'd say, well, you know, I don't know because I'm running this conference.

[01:05:40] **JON KALB:** I really wanted to run that conference, but I'm not crazy enough to run two conferences and so that's gonna be somebody else's problem. And so we need to focus on next year's C++ now. And then we would talk about that for a while, and then somebody else would ask a question, well, this other conference, where would it be located?

[01:05:59] **JON KALB:** And you [01:06:00] know, and it was very clear that people in the room were very excited about this other conference that I had already said, I'm not gonna have anything to do with this. I'm focused on C++ now. That's what I'm doing. What happened afterwards was, um, uh, Chandler Carruth came up to me, he said, look, if you're interested in doing this other conference, which I just said I'm not interested in doing, but he said, if you're interested in doing this other conference, [01:06:30] the organization you should talk to is the C++ foundation.

[01:06:34] **JON KALB:** And he said, when we set up the C++ foundation, we discussed doing a conference, and we just decided that we didn't have the bandwidth to take that on. It would be a great thing for C++, it would be a great thing for the foundation, but we don't, we aren't gonna be able to do that. This. The foundation isn't, doesn't have the resources to take that on.

[01:06:56] **JON KALB:** So, uh, so he said, you [01:07:00] know, this is an organization that's gonna be favorable on the idea of having a conference, if you can make that argument. Hmm. Um, and I, I'm well aware of something that's kind of, I call it conference fever, which is you go to a conference and you volunteer to do things and you get all excited.

[01:07:16] **JON KALB:** Then you go home and you suddenly realize, oh my God, what have I done? I am a full-time software engineer. I don't have the bandwidth to do all these things I just volunteered for. Um, and so I was a little bit leery of telling, uh, [01:07:30] Chandler, yes, let's do this conference. But we did literally stay up till, I don't know what it was, two or three o'clock in the morning just talking about possibilities and, and ideas.

[01:07:40] **JON KALB:** And it was really exciting to me. And so I told him, I said, look, let's go home. Chandler's in the Bay Area. I'm in the Bay Area. I said, look, let's go home. Let's give it a month and let's meet again. And if this still seems like a good idea, then we'll start working on it. And so that's what happened. And so, and that became, that became, well [01:08:00] I, we started working on a, on a pitch, a slide deck that I would present to the foundation.

[01:08:06] **JON KALB:** Now Chandler was on the foundation board. He was the treasurer of the foundation board. Um, and that's why he had kind of insight that he knew that the foundation had had considered doing this. And, um, so. I started working on a pitch for what I thought would be, uh, how we could explain to the foundation board that we should do a conference.

[01:08:28] **JON KALB:** And as we were working on [01:08:30] this, he, he called me and said, Jon, Herb Sutter, who was the president of the foundation board, he said, he's in the Bay Area to do some work on the standards committee. There was a subcommittee working on some memory issues. And so he was in the Bay Area for that. And he said, while he's here, do you want to talk to him?

[01:08:51] **JON KALB:** And I said, well, yeah, absolutely. Get his feedback on what I'm working on. So when I make the pitch to the committee, I have, [01:09:00] you know, I have a little bit of buy-in upfront knowing that, you know, getting his thoughts on this. So the three of us got together and, um, I basically laid out to Herb much of what Chandler and I had talked about ideas of what CPP Con would be.

[01:09:18] **JON KALB:** And at the end of it, he said, well, that all sounds great, but we don't, we don't really feel like we have the resources to do this. We don't have anybody to do this. And I don't know, I, [01:09:30] I assume he knew exactly what he was saying because of course. My response was, well, you know, the idea is that I would do this.

[01:09:37] **JON KALB:** And I remember thinking as I did this uhoh at this point, I can't back out. Because until then it was just kind of, we were discussing it. But at that point I said, well, the idea was that, that I would do this. And he just looked at me and he said, well, I guess we have a conference chair then. And I said, well, wait a minute.

[01:09:57] **JON KALB:** Don't we need to the [01:10:00] approval of the foundation board? And what Herb said was he said, well, I'm the president of the foundation and so I should make some decisions and this is gonna be one of the decisions I make. That's just the way he said it. And so I guess, oh, I guess we're gonna have a conference.

[01:10:18] **JON KALB:** Then at that point, I was chair of C++ now and chair of a new conference that we were getting off the ground, uh, CPP Con, which proved to be [01:10:30] as popular, more popular, uh, well measured in terms of the number of people who attend. It was much more popular. But that was kind of by design. It was from the beginning, designed to be a much larger conference.

[01:10:42] **JON KALB:** Uh, as I look back on the, uh, original, uh, planning mission and stuff, it, it. It sounds a little presumptuous because I, I pitched it as this is going to be the platform for people to get together and talk about C++ and hash out C++ issues. [01:11:00] And it has turned out to be that in, in a, in a, in a great way.

[01:11:04] **JON KALB:** Um, you know, one of the things that, uh, has helped CPP Con establish itself was the fact that I could pretty much count on every year one of our keynotes was going to be Bjarne Stroustrup, the creator of C++. Other conferences, and I know this, believe me, I know this, they're delighted if they can have him come and be a keynote speaker once every three to five years, that's terrific.

[01:11:29] **JON KALB:** Um, and [01:11:30] I pretty much count on him to open the conference every year. And then I also have Herb Sutter, who's the convener of the standards committee doing a, a keynote every year. I don't see it that way for a few reasons, but that might be because I was chair of both conferences.

[01:11:46] **JON KALB:** But it is true that the foundation is about promoting C++, promoting standard C++. So of course, they're gonna promote the standard. And we do [01:12:00] have, at the, at CPP Con, every year, there is a session called the Fireside Chat, in which members of the standards committee. Or a panel to talk about what the Standards Committee is doing and you know, so yeah, it very much is, you know, it's a product of, so the foundation is not the standards committee.

[01:12:23] **JON KALB:** Those are two completely separate things, but the foundation's mission is [01:12:30] to promote the work of the standards committee is to promote standard C++. So there's no question, but what, that's the mission of the conference. I don't really think that's necessarily in conflict with what C++ now is doing.

[01:12:43] **JON KALB:** Um, I became aware of Vinne because he had submitted a talk at CPP Con, Vinnie Falco, uh, I met him at CCP Con, became aware of him because he had submitted a talk and he came up to me as a conference [01:13:00] chair and said he wanted to. Uh, he wanted to spring for, I'm not, I can't recall exactly what the event was.

[01:13:08] **JON KALB:** It may have been the banquet. Uh, I'm not sure. But he, he wanted to spring for a round of drinks for everyone there. And I said, oh, you can't be serious. I said, you know, the, uh, that's gonna cost a fortune because when you're at a conference, the markup on food and beverages is just amazing. And so I, I cautioned him that, no, you're [01:13:30] crazy.

[01:13:30] **JON KALB:** You don't wanna do that. But he, he, no, no, no, no, I wanna do that. And I, uh, I, I kind of assumed, well, he's probably a closet alcoholic that gets off on getting everybody else to join him in his drinking. I only found out later that he doesn't drink. Uh, but that's what he, that that certainly is a memorable thing.

[01:13:51] **JON KALB:** I can't remember what it cost, but that was a small fortune to literally buy a drink for everyone at the event, at the conference. And what I think, I think [01:14:00] his, his goal was just to create a sense of community. Um, I've since gotten to know him much better as a Boost Library author and being very, very, uh, focused on the quality of, of his work.

[01:14:17] **JON KALB:** As a Boost Library author, uh, his, uh, Beast library, He paid a company to do a security audit on his library, which is just insane. It's an [01:14:30] open source library. You know, you know the joke, he, he's, he can't make it up for it in volume, right? I mean, it's an open source library that he worked hard, but of course that's not unique.

[01:14:41] **JON KALB:** Boost Authors work hard in their libraries. They do, of course, but he also turned around and paid to have a company do a security audit on. On his library. To me, that was just an amazing commitment to the quality of what he's done. But, uh, and, and at the time it was a [01:15:00] little bit hard to believe, but now as I've gotten to know him better, I realized he is really, really taking Boost seriously, because he wants to make the programming environment for C++ programmers a better experience.

[01:15:15] **JON KALB:** And so he thinks the way to do that is to make boost better. Uh, and so he's working on things like making the documentation better, making the communication experience better, and, uh, and of course, [01:15:30] uh, sponsoring the, uh, C++ language, uh, slack, which he didn't create, but he recognized there's an opportunity here to support the community.

[01:15:41] **JON KALB:** And so he has been, he's taken, taken that over and underwritten it financially, which, uh, has added to its value significantly. You jumped at. Well, um, Vinnie reached out to me and said he was, he was creating this foundation called the C++ Alliance [01:16:00] to support the environment, to support C++ for programmers.

[01:16:04] **JON KALB:** And would I be interested in being on the board? And it was like, I have no idea what we're planning to do with this, but it's certainly just the mission is something I can't disagree with. Right? Of course. I wanna support things for the, uh, for the C++ programming. Environment. And I knew that Vinny was very, very serious about Boost.

[01:16:25] **JON KALB:** And one of the things that, as you know, [01:16:30] my role in the Boost Steering Committee, particularly as I became the chair of the Boost Steering Committee, I always felt a little bit like the tail wagging the dog. I was running the conference and it was an important part of Boost. It raised money for Boost, it helped engage people who were boost, you know, that was the face-to-face meeting of people who were working on Boost libraries, all those kinds of things.

[01:16:54] **JON KALB:** And I, I, I love the conference and I thought we did great things, but I [01:17:00] also recognized this is the tale. The dog, if you will, are the Boost Libraries. That's what's important. Um, the contribution that Boost has made to the C++ community, partly through the standard, through libraries that became part of the standard.

[01:17:17] **JON KALB:** But, but, but mostly just giving thousands of programmers access to dozens of high quality libraries. That's, that's an amazing achievement. But [01:17:30] I wasn't involved in that. I'm not a Boost author. I've never done a a, a boost. I've never man, been a review manager. I've never done a release. All these things that are so important to boost.

[01:17:45] **JON KALB:** Were not what I was comfortable with. I knew everything there was to know about the conference. That part I was comfortable with. But, but I always wanted to try to find people to be active on the steering committee. I knew all the people who showed up at the conference. It would've been easy [01:18:00] for me to have a steering committee full of people who were conference attendees.

[01:18:04] **JON KALB:** But the hard part was, I was trying to find people who are active in, in all the roles necessary to make boost work. The review managers, the release managers, the authors, that's who I wanted to have involved. And so when I met Vinnie, he was a Boost author and he was willing to do hard work having to do with infrastructure because this was, again, one of the challenges that we felt [01:18:30] on the standards committee, or excuse me on the, on the steering committee for Boost, was how do we get people excited about and support work on infrastructure kinds of things.

[01:18:41] **JON KALB:** Uh, the individual Boost libraries are wonderful. The authors, uh, maintain those, some of them, the authors lose interest and they become orphaned libraries. But the, but the real challenges, the boost infrastructure itself releases, documentation, all the [01:19:00] things that are necessary, particularly as time goes by and we have, you know, technical, uh, um, rot if you will, where those kind of things need to be maintained and updated for.

[01:19:12] **JON KALB:** For, uh, security and performance and all the other kinds of things. Yeah. And here was Vinnie, who was excited about doing exactly that, supporting the boost infrastructure, making a better quality experience for boost [01:19:30] users and boost developers. And I was ready to sign on for that. Well, um, the missions are, are not incompatible, but they're not necessarily overlapping.

[01:19:41] **JON KALB:** Uh, the mission of the foundation is to promote standard C++. That certainly means letting C++ programmers know about the standard and, and how to use it properly. And of course, the conference is part of that. Part of that is promoting c [01:20:00] plus plus externally so that programmers in other languages have a favorable impression of C++.

[01:20:05] **JON KALB:** And think about it as maybe an alternative, they should explore something like that. That's what the foundation should be doing. But understanding the, and, and as I said earlier when we were talking about, you know, why was the foundation started, it was because there was a feeling that that promotion needed to be done.

[01:20:24] **JON KALB:** I mean, before the foundation started the conference, they were, there's a website to [01:20:30] let people know about. The latest news of C++ and how to find events going on and things like that. It was, it's largely promotional, that's what it's supposed to do. Whereas what Vinny wanted to do with the C++ alliance was to, um, to change infrastructure, to create tools, to do things like, uh, like CPP Lang, which would, or I mean the CPP Slack, which would, um, allow people to engage and things like that.

[01:20:59] **JON KALB:** [01:21:00] Actual, uh, building infrastructure kinds of things. So it's, there's no, uh, there's no conflict. They are, uh, they are different missions to achieve different kinds of things in different ways. So, um, the, the steering committee was, was, was created, as I said, to create a governance for the Boost Project, but the legal entity was the, uh, the fiscal [01:21:30] sponsor, that being the Software Freedom Conservancy.

[01:21:33] **JON KALB:** And that meant that whenever we did anything that involved signing contracts, making payments, uh, collecting revenue, anything like that, went through Software Freed and Conservancy, and they had made assurances to us that. You know, our funds were, they were the custodian. And from a legal point of view, they were the owner of those funds, but they were dedicated to our project.

[01:21:58] **JON KALB:** And they had [01:22:00] said, and this predates my involvement because this was something that, uh, Beman and Dave Abrahams had worked out that, that we, that boost would become a project of Software Freedom Conservancy, that if we ever wanted to leave, if it was a, um, a to another nonprofit so that legally they could spin the, the funds over.

[01:22:22] **JON KALB:** But they would do that. And, um, and initially they were taking [01:22:30] on Boost simply because they felt their mission was to support open source development. And so if a project wanted to come to them and say, we need to have a fiscal sponsor and we're doing something, and they felt like it was a good project to take on, they would take that on.

[01:22:45] **JON KALB:** It was only later that they said, our board of governance is telling us that we need to have revenue associated with all the projects. And so they came to the steering committee [01:23:00] and said, we want you to give us 10% of all the money that you had, that we are holding for you, turn it over to us, and 10% of all future revenue would come to us.

[01:23:13] **JON KALB:** So not too long after the steering committee had been set up. The software Freedom Conservancy came to us and said, look, our board of government is dis, is saying that we need to have better revenue associated with all of our projects. And so they wanted to [01:23:30] have 10% of the money that they were holding for us, 10% of our account turned over to them and also 10% of all future revenue.

[01:23:39] **JON KALB:** So this was, as I said, fairly early on in the existence of the, of the steering committee. And Beman said he had previous experience with, with, um, uh, nonprofits, and he said, it's a lot of paperwork and a big deal, and it's, you know, 10% of our money is a, is [01:24:00] a lot of money. But on the other hand, for what they're doing for us, it's worth it for us to, to have them handle all of that administrative work and let them do that over time.

[01:24:13] **JON KALB:** It kind of became. Frustrating for us because, um, and, and it, it's not really a fault of theirs. It's more that they were very busy and it wasn't necessarily their highest priority to make it easy for me to run a conference. But it was [01:24:30] frustrating that every time I wanted to, uh, pay a contractor or something like that, we were going through their policies about how that had to be done and what kind of time that would be.

[01:24:40] **JON KALB:** And it was more and more frustrating for us to negotiate with them about this time. Also, the law in this country about nonprofits change pretty significantly to make it much more easy to run a nonprofit. And so, [01:25:00] uh, we approached them and said, we think it's time for us to be spun off as a nonprofit. And foundation was very supportive.

[01:25:06] **JON KALB:** They actually hired an attorney to create the Boost Foundation Corporation, um, which I didn't really have anything to do with that part, but I did have to do with filing with the IRS to make a nonprofit. And, and as I said, that was a much, much easier process than it had been previously. Uh, and so [01:25:30] that's what we did.

[01:25:31] **JON KALB:** We spun off the Boost Foundation, but largely it was less about um, meeting some particular need than it was about being independent of Software Freedom Conservancy. The [Boost] Foundation well, effectively it was people who were on the steering committee simply became directors of the foundation. And so I was chair of the steering committee, but I had wanted to not forever be, [01:26:00] I, I wanted to be able to step down from that role.

[01:26:04] **JON KALB:** And so what I, what I decided was I created a role for myself. You know, when you set up a corporation, you can make whatever rules you want. So I set a role for myself as the executive director, which meant that I would handle the paperwork of the filing, the nonprofit stuff, which I said was not huge, but it's not nothing.

[01:26:23] **JON KALB:** Somebody has to do that. And so all of the things having to do with, uh, [01:26:30] running the necessary paperwork of, of having this corporation, this nonprofit, that would be the executive director, and I assign that to me, but rather than becoming president, the idea was that people who were on the board would take a turn being president for one year.

[01:26:49] **JON KALB:** And so, um. So that was, and the main job of the president was simply to call meetings and to basically be the, uh, [01:27:00] be the person who would set an agenda and call a meeting and actually run the meeting. And so, you know, well it was basically replacing the steering committee, although the steering committee's role was to make whatever decisions we made and then tell Software Freedom Conservancy, this is the decision we've made.

[01:27:18] **JON KALB:** Spend this money or sign this contract or do whatever we decided to do. Now the idea was that we would be independent of them and we would decide whatever, [01:27:30] but from the beginning, the steering committee was badly named because really Boost does what the people at Boost want done. In other words, there are people who are release managers and people who are review managers and people who are, all these people are just doing what they think needs to be done.

[01:27:51] **JON KALB:** And the reason that the steering committee existed was so that if some of those people said, look, we wanna buy test machines, can you authorize that person at [01:28:00] that purchase? Then there was someone to go to who had the authority to tell the conservancy, yes, spend this money on this. That was the reason.

[01:28:09] **JON KALB:** So it's not really like the steering committee was. Steering the ship. It was more like the ship was, uh, it's an open source community. And so people were doing what they felt they needed to do. Um, the steering committee was there if something had to be either one of two things. Either something had to be signed or [01:28:30] spent or authorized to purchase or, and this was what we knew might happen someday, is if the com, if consensus was difficult to find on a particularly divisive issue, such as changing the repository to the Git repository.

[01:28:47] **JON KALB:** And that was the, those are the things we did. So when we became the Boost Foundation, that was the role it took on. 

[01:28:55] **RAY NOWOSIELSKI:** Okay how did you first hear about Beman's [01:29:00] death?

[01:29:00] **JON KALB:** Um, you know, we, we wanted to create a way for people to submit comments and messages about how working with him had affected them or how his work had affected them and things like that. But I don't really remember how I first heard. I had met her at the conference, met his wife Sonda [Dawes] at, at the conference. Um, the only real interaction I had with her was one day she [01:29:30] was looking around the conference, kind of late in the conference and she pointed out, she said, everybody here is dragging. They don't have the excitement and energy they had the first day of the conference, which. Not really a surprise. And Sonda said, you should have an opportunity for people to take a break. And I thought about that. And so I proposed again at the, uh, the meeting that we have on the last night of the conference.

[01:29:59] **JON KALB:** This is, you [01:30:00] know, I said, what would you think about? And I, I said, this was Sonda's idea, Beman's wife had proposed that we have one session that you could take off. And so I said, imagine on Thursday, late in the conference Thursday afternoon, immediately after lunch, instead of having a session scheduled, there's no session.

[01:30:20] **JON KALB:** So that means that with a already we have a fairly long lunch. If with a 90 minute session missing and you have half an hour before the next session, that would be a very [01:30:30] long period of time. You could take a hike, you could take a nap, you could catch up on email, you could work on, you know, work from work.

[01:30:37] **JON KALB:** You could work on library a week. There's so many things you could do and we'd only be giving up one session. But it gives, you know, right in the middle of Thursday, it's an opportunity for you to recharge. You could, you could either take a nap or do something physical or whatever it takes to help you, uh, recharge for the rest of the conference.[01:31:00] 

[01:31:01] **JON KALB:** There was such a unanimous. Disapproval of that idea. Everybody said we may be exhausted, but we didn't come this far to not have sessions. Okay. Uh, I think people already recognized that if they were really exhausted, you know, people, people can miss sessions. If you really need a nap, you go take a nap.

[01:31:20] **JON KALB:** Well, there were people who, um, who sent some comments and so we put a memorial on the website, uh, for, uh, [01:31:30] for people to appreciate Beman's contribution. Uh, boost was very much a creature of Beman Dawes' idea. He came up with the original idea, he proposed it. Uh, he let people know at the standards committee because the original people who were boosters were pretty much from the standards committee, people interested in the standards committee and interested in standardizing libraries.

[01:31:56] **JON KALB:** Uh, and so they saw the need for it. I think [01:32:00] because they were in this situation where it was like, well, um, it's not really the mission of the standards committee to create libraries to standardize. I think it's kind of become that, and I think it's kind of a problem that that's what it's become. The idea was for people in the standards committee to identify libraries in widespread use and standardize those.

[01:32:23] **JON KALB:** And Beman saw the only libraries like that were proprietary libraries, and they're not really [01:32:30] candidates for standardization. So. What do we do? So he created Boost. He made the argument that we need to have a platform for open source libraries to become widespread. And that was so visionary at the time.

[01:32:46] **JON KALB:** Today with GitHub, people don't think anything about that. You can easily set up your own open source library, have a, have, you know, people commenting on it, all [01:33:00] sorts of things. That's just so easy to do with GitHub. But at the time, this was completely revolutionary. There was nothing like it at the time.

[01:33:07] **RAY NOWOSIELSKI:** How did the Arthur O'Dwyer incident unfold for you? 

[01:33:11] **JON KALB:** I'm not good with the chronology. We got a, I don't, I don't know who "we" is, it probably went to Herb [ Sutter] first. Um, there was some email saying, uh, one of the presenters at CPP Con, um, was discovered [01:33:30] to be on a sex registry. And I was trying to think, well, who could that possibly be?

[01:33:39] **JON KALB:** And it's so crazy, you know? And then, um, and then when I found out who it was, it was like, that doesn't make any sense. Um. Well, it's just completely uncharacteristic for having dealt with this individual for literally years, because at that point, uh, I believe he had attended every [01:34:00] single CPP con, uh, which meant he'd been there for five years.

[01:34:05] **JON KALB:** And in that time, not a whisper of any hint, of any issue, of any impropriety, of any kind. I mean, you know, he was more than just a presenter. He, uh, was involved in helping with the program in a few different ways. And one of the really influential things that he did was we'd set up a, [01:34:30] a mailing list where people who wanted to submit could send their abstract for somebody to just look it over and give 'em some feedback.

[01:34:40] **JON KALB:** Um, if you've never submitted to a conference before, if you've never been on a program committee, you've no idea what, what is an abstract, what does that mean, and what's a well-written abstract and what are the, you know, what are the things to look out for and stuff like that. So having an email that you can send your abstract to and have somebody look it over and say, [01:35:00] well, lemme give you this advice.

[01:35:01] **JON KALB:** Lemme coach you a little bit. And that's something that, um, we had difficulty getting people to agree to. To participate in that. I mean, it's software engineers are busy people. They have a lot of opportunity to do things with their time. And this individual had effectively, uh, been willing to take on that task and was doing a great job of coaching people.

[01:35:26] **JON KALB:** It was obviously potentially very [01:35:30] explosive. Um, and I, I did make my feelings known to Herb, but Herb told me, he said, look, um, the [ C++] foundation board is going to make decisions about this. It is not your responsibility to make any decisions. And so that's what happened. The board said, this is what we're doing, [01:36:00] and I, that's, it was outta my hands and right.

[01:36:08] **JON KALB:** So, um, Herb made it clear to me that anything having to do with what CPP Con would do about this situation would be decided by the [C++] Foundation board. And I will say that in effect, my heart went out to them. You can imagine if you've ever been on a board of a, [01:36:30] of a non-profit. Basically you're, you're gonna spend a few hours a year.

[01:36:35] **JON KALB:** Uh, looking at that nonprofit's budget and I approving expenditures and those kinds of things, it's generally not a huge time commitment and generally, um, not a lot of difficult decisions being made, but suddenly the board was faced with this incredibly difficult decision involving, uh, [01:37:00] just all sorts of issues.

[01:37:02] **JON KALB:** Very, very explosive. I don't, I don't know how much time went by. I think that it probably wasn't as much as it felt like at the time. Um, but the decision was made that, um, the, the conference would not have him attend. And the standard was as long as we felt it was disruptive to the [01:37:30] conference. In other words, it, it, it was, it was not because of, I don't know, I don't know how to say it exactly, but the idea is that we were acknowledging that it wasn't because we felt as if.

[01:37:44] **JON KALB:** He was a danger to the conference. You know, from my point of view, one of the things that made this, um, a situation that we could make some kinds of decisions about was the fact that he had attended the conference for five years with no issues. [01:38:00] So, um, normally you might say, if you hear about this with somebody who's about to come to a conference for the first time, you might say, oh man, this is a danger to other attendees.

[01:38:12] **JON KALB:** But here was a situation where he'd attended for five years and there was not a single whisper of any issue of all. And so it's pretty easy to say, well, that doesn't sound like he's an imminent threat to the, uh, to in, to attendees. But the decision was essentially, as long [01:38:30] as it's disruptive, we can't have him here.

[01:38:33] **JON KALB:** Which effectively meant, uh, we were, you know, it wasn't because we felt like he was a danger as much as we felt like his coming was going to upset other people. And, um, and, and that was the decision that was made and handed to me. Okay, I accepted it. Uh, partly because the, you know, as I said, that decision had already been made that I wasn't gonna have anything to do with it.

[01:38:58] **JON KALB:** And also because [01:39:00] it seemed reasonable, uh, there was no clear, obvious this is the obvious thing to do in any other idea, is completely ridiculous. Uh, it, it was an impossible situation. You know, there was no good solution. All you could do is try to find the least bad solution. I don't know. I don't know the, the facts.

[01:39:21] **JON KALB:** I know that if you talk to him, he will tell you, at least he told me his side. [01:39:30] Of course, I have no way of knowing. I mean, this happened a long time ago. He may be a really good liar about this. I have no idea. Um, if you listen to his side of the story, to me, it fit all the facts. And it was kind of a very sad story about somebody who got involved in a situation with maybe, you know, not ill intent or even [01:40:00] ill behavior, but maybe some bad decisions.

[01:40:03] **JON KALB:** Um, but as I said, all I have is his side. I don't know if there's, I, I have no way of verifying. I. I suppose maybe I could do some research or something and try to find out if there was ever anything, uh, printed about it at the time in the paper. I have no interest in doing that. And, uh, but as I said, I, I have, all I have is Arthur's side and, um, it paints a, [01:40:30] a pretty sympathetic picture, but of course you have to again, recognize that's that's his story.

[01:40:39] **JON KALB:** Um, the other thing I have of course is as I said, his behavior in the five years that I knew him and, um, the way he behaved in a lot of situations. I mean, we didn't, I didn't know him really well, but I was involved with him in some local group organizing 'cause he also lived in the Bay Area, um, [01:41:00] as well as at CPP Con and involved in things there.

[01:41:04] **JON KALB:** And in in, in no situation was there ever anything that caused me to have any questions, even in retrospect, even looking back and saying, did anything ever happen that I would consider suspicious? And, and the answer was simply no. Um, so it made it kind of easy for me to believe his story, but I always, in the back of my mind also have to recognize that's his story, that I have no idea [01:41:30] he there.

[01:41:30] **JON KALB:** I mean, there isn't any evidence he [ Arthur O'Dwyer] could present that would, that would back it up. I have no evidence that it's not the truth. Um, and to a lot of people, I suspect even his story would not be, I found it somewhat sympathetic. Other people could listen to that same story and say, uh, I have no sympathy. Um, well, the, the first email didn't blow it up publicly.

[01:41:54] **JON KALB:** We did get, uh, this, and we were [01:42:00] aware of it, and then it went public later, not, I don't think a lot later. As I said, I'm a little fuzzy on timelines and when things happen and stuff like that. And I suspect it was, it was less time probably than I remember it because, well, they were working on that and it was, I think they were still working on that when it blew up.

[01:42:23] **JON KALB:** I don't, I don't know. I mean, it, it sounds like that, yeah, that's a quite plausible scenario. It could have been worse [01:42:30] because of that. On the other hand, you don't really know the counterfactual. It's, it's also possible, but it would've gone exactly the same way if the committee had acted much more quickly and had beat them to the punch or whatever.

[01:42:41] **JON KALB:** I don't say beat them to the punch, but you know what I'm saying? If, if they'd actually announced something before it became more widely known, maybe that would have only the flyer even more. Who knows? Um, uh, but I think [01:43:00] that, um. You know, it was a, it was also a product of its time. In other words, it's, there were other kinds of things, um, that were driving, driving the social world crazy.

[01:43:14] **JON KALB:** Right. Culture war stuff. Culture war stuff. Yes. And so it was, it was very much of its time and there were lots of people who wanted to be heroes by attacking the conference and, um, it became a [01:43:30] one of those. Yeah. You know, I, I said earlier how nice it was to work with the Cple Plus community because people were, uh, humble and supportive.

[01:43:49] **JON KALB:** I got a picture of certain people in the community that, that I didn't really wanna see. Um, and, [01:44:00] and I don't really wanna dwell on that, but I think it did seem to me like there were, uh, there was a,

[01:44:13] **JON KALB:** I don't want to call it out now, cowardice, but a lack of bravery, which may be the same thing. Um, and it, some of it was maybe hurtful, but a lot of it was kind of disappointing. Mm-hmm. Um. [01:44:30] But again, it was of its time. Um, I think there may be a lot of people who acted in ways that they're not necessarily proud of at this point.

[01:44:44] **JON KALB:** One of the things that was frustrating for me in running the, the Boost Steering Committee, but also the [ Boost] foundation, was how unresponsive people [01:45:00] on the steering committee or on the foundation were. Um, as an example, the very first, the very, um, well, the, the first year that I was co-chair with, uh, with Dave for the conference, he let me know that he wanted me to be co-chair.

[01:45:22] **JON KALB:** So this was for 2012, the first year of C++ Now, and he let me know really [01:45:30] after the call for submissions had gone out. And so there wasn't a lot of time for me to be involved in the planning of the conference. But for the next year, 2013, as I said, I, I wanted to be the guy who did the logistics stuff to free Dave up to be the front man.

[01:45:46] **JON KALB:** He was, I wanted him, he was the co-chair, but I didn't see us as equals, Dave was. Very well understood and very acknowledged. And he was a leader in Boost and I was just this nobody. [01:46:00] And so I was willing to do the grunt work to make a conference happen, um, and let him be the guy who did the welcome announcements and, you know, did those kinds of things.

[01:46:10] **JON KALB:** That was the role I wanted and I was happy to do that. And so what I did for 2013 was I pulled all the financial information I could and made this very detailed budget about where we were gonna be. Um, and I sent it to everybody on the steering committee to asking for approval. [01:46:30] And I think I got one yes vote other than myself.

[01:46:35] **JON KALB:** And that was it. Nobody voted. No, nobody else voted. Yes. There was just no response at all. And that was kind of typical of some of the decisions that we made. I had to fight to get people to respond at all. So when you say, what was the reaction? You have to understand that we weren't having regular meetings.

[01:46:56] **JON KALB:** The [ Boost] foundation and the steering committee effectively had, [01:47:00] you know, a meeting every year that was scheduled for during. C++ now and then usually we would have one meeting exactly six months, kind of an offset meeting that was online. That was about it. Boost Foundation, the Boost Foundation or the Boost Steering Committee both. That was kind of, I mean, we weren't, it wasn't an active organization in that sense. Pretty much. I did what I could to make it run, and if I needed approval by the board, I would send out emails and beg them to vote. And so [01:47:30] when this happened, I knew that, that we had a submission from him and that we were gonna have to make a decision about that.

[01:47:41] **JON KALB:** And so I knew that I was gonna have to bring that up and discuss it. But because of my role at CPP Con, and because I knew the things that I knew because of that role, I wasn't, I wasn't going around telling people about it. I didn't tell anyone, maybe other than my wife about [01:48:00] any of what was going on because it wasn't my role to tell them.

[01:48:03] **JON KALB:** But I knew that I was gonna have to share this with the program committee at CPP Con, not in the whole program committee, but some level of, we have to decide what we're gonna do here. Are we gonna not accept this submission? What are we gonna do? I assumed we wouldn't accept the submission, but, uh, I knew a discussion had to be made.

[01:48:22] **JON KALB:** Mm-hmm. But what happened was when, when it became [01:48:30] very well known. The individual who was, as I said, we were kind of rotating around the position of president. Um, and so this was, I think the second year of that. So it was the individual who was the second president, um, uh, said, well, we need to have a meeting to discuss this.

[01:48:48] **JON KALB:** And he sent out, um, a request for people to indicate when they could meet. And I told him that I was doing training. I had a class going on, and so I couldn't meet for the rest of [01:49:00] the week during business hours, but I could either do after hours or I could do the weekend, or we could do anytime next week.

[01:49:08] **JON KALB:** Um, he then scheduled a meeting for during business hours that week. In other words, he deliberately scheduled a meeting when he knew I could not attend. And I thought, well, this is kind of silly 'cause they're gonna want to hear what I have to say because I have some inside information. In fact, I knew that I was gonna have to have this [01:49:30] discussion at some point.

[01:49:31] **JON KALB:** But he was the president, he called the meeting when he called the meeting. Um, after my class was over, I wanted to contact him. I contacted him and said, so how did this meeting go? And he said, well, um, you were planning to, to step down, um, from the conference, right? And I said, well, yeah, I've been working with Bob Steagall to be the new conference chair.

[01:49:59] **JON KALB:** [01:50:00] And he said, well, how's that supposed to happen? And I said, well, I'm going to do the opening, welcome at the conference, and Bob is gonna do the closing. And that's symbolically me turning over. And he said, the committee doesn't want you involved in the conference anymore. He says, you can attend, but we don't want you involved as a leader in any way.

[01:50:20] **JON KALB:** So Bob should do the welcome. I said, okay. And he said, and the committee doesn't want you on the Boost Foundation anymore. [01:50:30] We want you to turn over everything related to that Bob. And, um, I was, I was very hurt. You have to understand, as I said, um, from, from the time I took on the role as co-chair, I was doing essentially all the heavy lifting on the conference.

[01:50:56] **JON KALB:** Um, you know, uh, Dave and I were [01:51:00] co-chairs for a, a short time, I don't even remember how long until he, until he went and worked at Apple on Swift and wasn't involved in the conference at all. So I just became the chair. And then I also at that point, took over as chair of the steering committee because Beman had retired and Dave had moved on.

[01:51:21] **JON KALB:** So I took over chair of the steering committee and was effectively. Um, doing all admin stuff, and I don't want to say [01:51:30] admin in, in terms of like running the website or any of that kind of stuff, but admin in terms of dealing with anything, having to do with the conference or legal spending, any legal issues, um, that involved us working with the, uh, standards, uh, with the, uh, software Freedom Conservancy or anything having to do with setting up Boost Foundation, all of that kind of stuff.

[01:51:52] **JON KALB:** I had done that all carried all that load. And as I said, the [01:52:00] other people on the committee were very reluctant to be involved. And the thing is that they were wonderful people. They were happy to be, uh, when we had the meeting at the conference, as I said, we'd have an annual meeting. They were involved, they had great ideas.

[01:52:17] **JON KALB:** So I just felt like, uh, yeah, it, it felt ungrateful. It, it, it just hurt a lot. I had been doing so much for this organization [01:52:30] and I wasn't even wanting to be heard from, um, and I made a, a mistake in that I should've pushed back and said, wait a minute. The people on this committee are personal friends of mine for the most part.

[01:52:49] **JON KALB:** I mean, weren't close friends, but, but I dealt with them. I, I couldn't believe. I, but I, uh, you know, I was, I was hurt. It [01:53:00] was only in retrospect that I, that I actually came across the meeting minutes and found out that, first of all, there wasn't a quorum. So nothing that happened at that meeting could have had any official weight.

[01:53:11] **JON KALB:** And then when I reached out to the people who were in the meeting, I found out that, um, there was no mention of the fact that the meeting was deliberately held when I couldn't attend. And in fact, that was, and I don't know exactly how it was worded because I, I got this [01:53:30] secondhand after a long period of time because I didn't immediately follow up.

[01:53:33] **JON KALB:** I should have. But what I heard and gathered was that it was, they were allowed to believe that the reason I didn't attend is because I really didn't want to be involved anymore. I was anxious to step down. And so, what, what happened was that the, then president told them that he would ask me what I wanted.

[01:53:55] **JON KALB:** But then when he talked to me, he said that what the, what [01:54:00] the committee wanted was for me to step down. I've talked to him and since, and said, look, uh, I pointed out, you know, that I, that there wasn't a quorum, that I wasn't heard from that. You know, I was treated unfairly, and he acknowledged, he said yes, at the minimum.

[01:54:20] **JON KALB:** Uh, we shouldn't have done anything when there wasn't a quorum. At a minimum, there should have been a written report of what exactly we just made decisions based on. And, [01:54:30] um, and he said, you know, uh, clearly I made mistakes when this happened. And so it's, it's a painful memory for me. I wouldn't say I lost it in the sense that, I mean, I didn't own it.

[01:54:41] **JON KALB:** Uh, I was serving on it. Um, you know, one of the things that that came up is that I had a lot of, I spent a lot of time dealing with Boost things, and now I don't. Um, it was in fact what I was [01:55:00] working toward. I was transitioning to having Bob take over the conference, and I was, I deliberately had created this role for myself as executive director rather than president, because I was hoping for other people to take on that leadership role.

[01:55:15] **JON KALB:** And I was hoping to, um, to get out of the executive director role. Yes. I have not missed C++ now. Okay. It's a wonderful conference. I've told people that CPP Con is a, is [01:55:30] a fun conference to plan and run, but CPL Plus now is the best conference to attend. So I think the, the, the Boost Foundation, um, or.

[01:55:44] **JON KALB:** I, I don't know the details of where this came from, but there's an idea to make a different set of libraries with slightly different purpose. So the Boost Libraries was a, had as a goal to create libraries that people would use. So they would go into [01:56:00] widespread use. So they would be, become candidates, potentially some would be candidates for standardization.

[01:56:06] **JON KALB:** Um, the part of the problem with that is that it's more fun to create a library than it is to maintain it. So, um, so some of those libraries have lost their authors, they become orphaned libraries and they still serve a purpose, but it would be better if they were well maintained. Um, [01:56:30] the, someone somewhere, and I, I have no insight onto this, came up with the idea of what they're now calling the Beamin libraries.

[01:56:38] **JON KALB:** And so what the Beman libraries are, is a, is an implementation of things that are being proposed for the standards committee. And the idea is that if someone has a paper before the committee saying there should be a library that does this, then the Beman libraries are gonna implement that based on that paper.

[01:56:59] **JON KALB:** [01:57:00] And, um, I'm kind of surprised by this for a few reasons. One is, um. Generally speaking, I think most library proposals actually have implementations already. So what we're really, I think, having is that we're gonna create a, an independent implementation, not the one that the author of the paper created, which is, which is good, it's [01:57:30] proof that an independent implementation can be made.

[01:57:33] **JON KALB:** That's wonderful. But the, as far as I can understand, the plan would be that once an implementation, once a, once a library got accepted in the standard, then the Beammen Library wouldn't serve a purpose anymore. So what that means is they're not going to expect to have real world users actually writing code based on these libraries.

[01:57:57] **JON KALB:** They're only there as proof of concept [01:58:00] for standard library proposals. To me, that makes them much less interesting in terms of, I mean, the, the Boost Library, yes, it's cool that those libraries are candidates for standardization, but the real value of those libraries is that literally hundreds of developers, thousands of developers, are using Boost libraries to ship real world code.

[01:58:24] **JON KALB:** That's the real value, that's the value to the community. Do some of them become [01:58:30] parts of the standard? That's, that's an achievement. That's something we should be proud of. And that's in a sense, part of the reason why the Boost Libraries were founded. But the real value of the Boost Libraries is, as I said, thousands of people are really using these libraries to ship real applications.

[01:58:46] **JON KALB:** And if the point of the Beman Library is only to implement something that's a standard committee proposal, when theoretically whoever wrote the paper should already be doing an implementation as well. And then if that standard, if [01:59:00] that paper is rejected, I guess we throw away the Beman Library and if it's accepted, then we also throw away the Beman library.

[01:59:05] **JON KALB:** It's there only as proof of concept for a paper is that there's a different thing that they're excited about. I wish them luck. Maybe the beam in libraries will catch on. Maybe there's something I'm completely missing. Wouldn't be the first time I completely overlook the value of something that could be, I don't see it.

[01:59:26] **JON KALB:** But that doesn't mean, and I certainly don't want to get in the way of it, [01:59:30] give them the best, best luck. Right. But that has been the energy of the Boost Foundation. They have, they are not quite literally, uh, it seems to me have lost interest in the Boost libraries. They are interested in the conference still and they're interested in the Beman libraries.

[01:59:56] **JON KALB:** Mm-hmm. Um, of the three. [02:00:00] The most important to me by far are the Boost libraries, and that's what they're not interested in. Again, maintaining libraries is not nearly as much fun as creating new ones. Hmm. And, um, there are, you know, there's, for a very long time there's been frustration about Boost, partly because, um, some of the libraries, because they were from a long time ago, have an awful lot of code.

[02:00:29] **JON KALB:** That is [02:00:30] not the way you would write it if you wrote it today. Um, and so there's maybe maintenance issues. There may be other kinds of things that, um, people aren't, aren't as excited about those libraries. Well, a lot of it is, is still promise and not, um,

[02:00:53] **JON KALB:** um, it's in the future, I guess is what I'm trying to say. Um, we've already, [02:01:00] uh, shown some improvements in the documentation system, which is valuable, uh, uh, the alliance. Um, and I think a lot of the work has been done, um, um, by people working directly for the Alliance have increased the, the documentation tools, the whole documentation system.

[02:01:21] **JON KALB:** Which is great. Um, there's other, um, the website itself, which was fine for when it was created, [02:01:30] but understand it was created in the late nineties. Um, that's not a, a beautiful website by today's standards, whereas we have now a much more modern, uh, website. Um, and I think that the long-term goal is to create a website that is a true community.

[02:01:51] **JON KALB:** In other words, I think, uh, we, we have a community now with the CPP Lang Slack, but I think the goal [02:02:00] is to have a, a more, uh, inclusive immersive environment where you can talk about CPP Lang Slack, but also, uh, understand, uh, better documentation, better presentation of how to use the Boost Libraries.

[02:02:20] **JON KALB:** Yes. But it's brighter now, I think, than it has been since Beman and Dave left. Uh, that's been, as I said, that was one of my personal [02:02:30] frustrations is that I didn't get people involved who are active on the, on the library side. Uh, the people I knew were people who knew a lot about the conference, and that's, I, I didn't.

[02:02:45] **JON KALB:** I didn't have a good way of knowing what the library side needed because I didn't, because I'm not a library author and I wasn't a review manager or involved in releases or any of that kind of stuff. [02:03:00] And so to me, I always had to get anything about that filtered through those people who were active in that.

[02:03:08] **JON KALB:** And basically it just kind of continued on through its own momentum. The people involved did what they needed to do, but we didn't really have any strong leadership there. Um, that's, that was the frustration for me. Well, Vinnie has certainly stepped up and has added some life to it. [02:03:30] So that's, as I said, I am, I see more hope for the future of the Boost Libraries than I have seen since, um, uh, since Beman retired.

[02:03:43] **JON KALB:** And, uh, um, they've moved on. I don't really know anything firsthand because when, so initially there was no consistent license. Um, in fact, I, I found some, [02:04:00] some very, very early. Um, FAQ for Boost, where one of the questions was, will you accept open source submissions, submissions of open source libraries? And the answer was no.

[02:04:12] **JON KALB:** It was kind of, there was a kind of a misunderstanding about what Open source was. They were expecting people to declare their libraries in the public domain, not open source. And so it was kind of hazy, but in the initial submissions, there was no, there's no library, there was no license, there was no boost [02:04:30] license.

[02:04:30] **JON KALB:** Everybody just kind of did whatever they wanted, but it became obvious that there should be a boost license. And so, um, I think Software Conservancy helped fund and, well, I think they may have had some lawyers donate some time and stuff like that to craft what became the Boost license. And then we had to go back, and I don't say we meaning me, but Boost had to go back to all the individual authors and say, you know, will you license this [02:05:00] under the new license?

[02:05:01] **JON KALB:** And then at some point it became pretty much if you made a submission, you had to agree to the Boost license. So now everything is the Boost license. Um, it is, as far as I know, the most, the, the, the most liberal of the open source licenses. Um, because. Most open source licenses, um, say, you know, the most, the most liberal ones will say, you can use this code. You can modify the [02:05:30] code. You cannot remove, uh, the copyright or license statements from the code. Uh, and you also must, in your application at some point in the about box or somewhere, you have to state that it was made with software under this license. And the boost license is essentially that accepted, does not require that you, that you indicate anywhere that you're using Boost libraries.

[02:05:56] **JON KALB:** So you can create applications using Boost libraries without [02:06:00] ever telling anybody that you are, not that we necessarily want you to that, but, but that's permissible. It's, as far as I know, it is the most liberal license in, in that it, it doesn't require almost anything except that you can't remove, you can't remove the license information from the Yeah.

[02:06:17] **JON KALB:** Um, and I don't know that there's anything in the Boost Library that would compile to something like that. Um, I suspect if, obviously if you, uh, compile with, um, [02:06:30] debug on, you're gonna see all sorts of boost in the name mangling. You would be able to detect that. Uh, but, but I don't, but as I say, we don't have any requirement that you acknowledge Boost in your application.

