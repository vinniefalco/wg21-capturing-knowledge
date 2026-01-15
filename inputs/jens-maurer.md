# BOOST_JENS MAURER_STRINGOUT_v01

- - - -
filmed Date: 2025-11-04  
location: Kona, HI  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1140852773/f4f135ef24?fl=pl&fe=sh  
summary: Excellent on creating Boost.Random, formal review, Beman Dawes, history of WG21 across 30 years from neutral perspective; hit many of the bullseyes we were seeking. Not Foundation but WG21. He’s a very honest German, and he laid out a host of truths about the committee. Herb has solo picked all the chairs of groups since 2002, tipping scales for outcomes go the way he might wish. He picks the locations for these meetings bc decided by his foundation—we are in Hawaii bc he likes Hawaii. Most telling was when questions about Microsoft’s competing coroutine and number of times “best code” fell to corporate influence, Jens’ long dramatic pause before answering while making grimaced face before saying “such a question requires a very careful response” and then essentially admission that it happens a lot and helps to make friends and socialize w chairs etc. Also said that Nat Goodspeed would do himself a favor for his library if he worked the social circuit rather than just being a diligent maintainer arriving and following the letter of the rules  
- - - - 

## Transcript Start

[00:00:00] **JENS MAURER:** Oh, that shirt. Yes. Um, the shirt is from our, uh, Sophia meeting in Bulgaria. And, uh, it, the hosts of that meeting handed it out, uh, to the attendees. So since it's from Bulgaria, it has slic writing on it. And [00:00:30] the, um, drawing on the front is actually the, um, subway map of, uh, Sophia and with special marking for where the meeting was.

[00:00:42] **JENS MAURER:** So I got a free shirt. I'm happy. My name is, I'm from Germany. I work for, uh, FactSet. Uh, it, um, with or more precisely the German subsidiary of FactSet. And FactSet [00:01:00] is a, um, company dealing in financial data similar to what, uh, Bloomberg and Reuters do. And I'm writing software for a living for them. So the official title is Principal Software Architect, but that's just a English, uh, an American style overblown title, I believe.

[00:01:21] **JENS MAURER:** Well, my role in the C++ story is that I joined the committee in, uh, October, 2000. [00:01:30] Um, at this time I was working for a, the IT subsidiary of German roadways and a very long time committee member that is still with the committee, uh, was hired as a consultant there and he said, oh, you seem to be interested.

[00:01:45] **JENS MAURER:** Why don't you come join the committee? So I did and never stopped. Um. When you say boost, I think what comes to mind is that be dos [00:02:00] has died much too early. Herding cats, I guess is what comes to mind when I hear WG 3 21, at least sometimes, sometimes it's quite smooth, but sometimes it's a bit on the interesting side.

[00:02:18] **JENS MAURER:** Alright, so where did did I grew up, I grew up, um, in the western part of Germany, not super far from Frankfurt, where the big airport [00:02:30] is and um, maybe 50 kilometers from Frankfurt. Um, and so it was a not very big village. I grew up in about 3000 inhabitants and went to school there. My, uh, went to university in Kai, studied computer science there.

[00:02:55] **JENS MAURER:** Um, my, yeah, so [00:03:00] my mother, were you 

[00:03:02] **RAY NOWOSIELSKI:** an only child or did you have siblings? 

[00:03:06] **JENS MAURER:** I am not the only child. My brother is four and a half years younger than I am. He still lives in the same village where my father still lives and I grew up in and everything. Um, my mother is studied pharmacy in Munich and before marrying my father actually worked for various [00:03:30] pharmacies in across Germany actually.

[00:03:33] **JENS MAURER:** And she had friends from her studies, uh, study time all across Germany where, you know, those pharmacists ended up being, um, she, however, she mostly stopped. Working when, um, we were, when the kids were young or were just born, um, so that she could more or less full-time, um, deal with the children. [00:04:00] My father, um, is, uh, and now that's the part where the English words escaped me.

[00:04:11] **JENS MAURER:** So he is essentially in mechanical, not quite engineering, but um, he trained in milling in steel, uh, milling, I think is the English, English term, so he knows how to operate milling machines. Um, so my father trained in milling and [00:04:30] in operating milling machines. He then, uh, went to a, some sort of advanced technical school and designed, uh, parts, mechanical parts for manufacturing.

[00:04:44] **JENS MAURER:** Um. F for manufacturing machines that can make, um, the, the upper, uh, tower based layer of roads. Um, pardon. [00:05:00] So he worked for that company for quite a while, and then he went, he switched to the chemistry industry and designed, um, pipes and tanks and all kinds of stuff for a, um, for a chemical factory in Mannheim, uh, which is also a popular, uh, or used to be a popular US military.

[00:05:25] **JENS MAURER:** I first came in contact at the university, I think, um, [00:05:30] read a few educational resources on that, and that was in 1993, approximately. Uh, so before the first version of the C++ standard was released. Um, and I think I always found it a fairly powerful language in expressing myself and therefore, and it was commercially relevant.

[00:05:53] **JENS MAURER:** Um, I probably never did, um, programming in anything but C++ for, [00:06:00] um, for, for business purposes. The language has a plenty, the language has plenty of features and that helps me. Um, and that helps me express the, the design, the structure of the program. I need to write in natural, in a natural fashion.

[00:06:22] **JENS MAURER:** And that is helpful in getting the job done, uh, quickly and maintainable and all the other properties you want. The first WG [00:06:30] 21 meeting I attended in October, 2000, uh, was in Toronto, Canada. Um, actually I think downtown Toronto, if I remember correctly, although it's been a long while. Um, and yeah, as I said, the um, a per a per, uh, deep who was, uh, hired by the IT sub subsidiary of German railways as a consultant, um, [00:07:00] I, and I was actually a permanent employee of that IT subsidiary.

[00:07:05] **JENS MAURER:** We met there and he said, uh, come, come to the committee. So I went to the committee with him. What did I find there? Um, I found at the committee about 45 to 50 people at that time, um, to subgroups a library and the core subgroup and. A committee that was addressing the residue and fallout from publishing the first standard in [00:07:30] 1998, and all the buck reports that poured in since then.

[00:07:33] **JENS MAURER:** So it was a week of, um, rather detailed buck fixing operation and not talking about features. Well, I did like the very detailed oriented, um, nitty gritty, if you wish, German style attention to detail that I experienced there. I didn't think much other than I like the experience. People were kind. Um, so I didn't think, I think I'm probably not very much future [00:08:00] strategy oriented thinker.

[00:08:01] **JENS MAURER:** Um, so it, it's not like, oh, I go there and then let's, let's make a strategy plan that, um, plans ahead for the next 10 years on how I would develop personally or whatever. That's not my thing. I just do it and, um, if I like it, then fine. Why do something else? Um, I was not working at, I was not working on Boost Random at that time.

[00:08:28] **JENS MAURER:** Um, [00:08:30] the foundation of the Beman Pro of the Boost Project was a little later, I believe, and it actually started as a dinner meeting. And, and one of those, uh, during one of those meetings, I think when Beman, um, suggested the plans to, that we should move from, or shift from maintenance mode of C++ 98 towards, um, being more open to [00:09:00] extensions.

[00:09:00] **JENS MAURER:** And then he found it, uh, he essentially said, let's make that a more, um, a more structured, uh, project. At least that's what I remember. I definitely know I was at a dinner meeting where he, he socialized that idea of, of creating boost. And it is very well possible that I misremember that that was already has had been published before.

[00:09:22] **JENS MAURER:** I was not part of any inner circles of email distribution, uh, or anything, uh, before I joined the committee. So it is [00:09:30] very much possible that I just didn't, wasn't aware of that happening before my involvement. Well, Beman was a very slim, um, at that time from, from my perspective already, not very young person.

[00:09:46] **JENS MAURER:** Um, he, he was with it much longer than I was, so I don't know what the actual age difference was, but, um, I definitely, uh, so he was already much more senior in the age [00:10:00] sense and, um, also I believe from the experience sense. Um, but he, yeah, he was a kind guy. He, he, um, he, he did. Um, he, he did invite me. He, he did encourage me to continue joining the committee.

[00:10:20] **JENS MAURER:** Um, he was friendly to me. He, he, um, thought I would join the library subgroup of the committee because that's what was his [00:10:30] interest, because, you know, boost was feeding into the library portion of the standard. But I actually ended up sitting in the core subgroup all the time that sort of disappointed him.

[00:10:42] **JENS MAURER:** Um, at least he said so Mockingly. Um, but yeah, so I do distinctly remember telling him, uh, say, uh, saying to me that, um, he was hoping for me to join the library group, and then I ended up in Core and that was sort of a [00:11:00] lost cause, um, if you wish. Uh, so not, not exactly with these words, but, um, and, and of course not really, uh, trying to discourage me from, uh, joining the committee, but just.

[00:11:11] **JENS MAURER:** Mentioning that he, he thought I would join the library part of things. But then, uh, it, it turned out that I would be joining the core part. So the employer I was with at the time, which was the IT subsidiary of German Railways, [00:11:30] um, that I was working for them to help create their system of offering discount tickets during times when there is little, uh, demand.

[00:11:44] **JENS MAURER:** But you have to run the trains nonetheless. And that is the same question that airlines face. They run the aircraft and the flights regardless of whe whether they're full or not, because they just run [00:12:00] them and it is of benefit to them to run full flights. So in times of high demand, they would write, raise their prices.

[00:12:11] **JENS MAURER:** Prices such as Thanksgiving in the us and flights are expensive for Thanksgiving because they have a fixed capacity. They offer almost, uh, but, and they know they get their flights full because everybody wants to go get, uh, to their Turkey in various places of the us, right? [00:12:30] Uh, so however, in times of low demand, um, they still want full flights, but people are less willing to go with high prices at that time because of the prices are too high.

[00:12:41] **JENS MAURER:** They just say, oh, I don't care. I don't just, I just don't go. So therefore, airlines lower their prices for, um, for flights in low de during low demand times, uh, such as maybe Tuesday morning, 6:00 AM or something. [00:13:00] Um, assuming there's no commuter traffic during that time, I mean, maybe coast to coast flights or so, um, so that's called revenue management.

[00:13:08] **JENS MAURER:** And hotels do the same, right? Hotel rooms are cheaper, uh, when, uh, it's not, uh, Christmas and it's not Thanksgiving and so on. Um, and at that time, German railways was introducing a, um, one of this revenue management system for their long distance trains. And you have to [00:13:30] understand that the German long distance railway network is, um, at least in order of magnitude more complex than a large airline network even in the US because more stops, um, the trains run for, uh, service longer stop, uh, more stops.

[00:13:50] **JENS MAURER:** So you have a train servicing 15 stops, for example, while the train travels through Germany. Um, that would be equivalent to having. A single [00:14:00] flight that you can stay into and not change airplanes, uh, land 15 times across the us which nobody does. Um, so yes, and that of course needed an IT system to handle all the data and handle the, the forecasts and handle the information of which days are high demand days and which, um, and, and which times of day and everything.

[00:14:25] **JENS MAURER:** And that's what that, what I contributed to that was what German railways wanted to [00:14:30] do. Yeah. And I was just the minion that helped make their dream true. I was looking for other projects inside of German runways and it turned out they, that they only had Microsoft Windows based projects. And I thought, um, and I never was a friend of Microsoft Windows, so I figured, um, thank you very much.

[00:14:49] **JENS MAURER:** Let's look for greener pastures. And therefore, um, and at that time there was a, uh, monthly dinner round [00:15:00] table, whatever you call it, of, uh, of Unix enthusiasts. And at that dinner round table, I met, uh, someone working for what would then become my next employer. Uh, so I said, look, this place isn't to my liking anymore.

[00:15:20] **JENS MAURER:** And you already said, uh, three months ago that you might have a job for me. Do you, is that position still open? And, um, within a few days I got that new [00:15:30] position. Um, so right. Um, it's, so that's how I ended up actually at FactSet because that new employer was, uh, a German company that via different stages was then.

[00:15:47] **JENS MAURER:** Actually bought, um, by FactSet. So there's, the company I worked for had, uh, had plenty of owners, uh, in between, and eventually now it ended up at FactSet. And that's why [00:16:00] I work for FactSet now. However, I need to backtrack here, and I understand you're editing all of this, so it doesn't, it doesn't matter that we're going in, in backwards and all that.

[00:16:11] **JENS MAURER:** Um, sorry about that. I have to backtrack because, um, actually the, the random number, uh, thing I did happened to be before I got employed by German railways. I was employed by another very small company that rented me to German railways. And at some point German railways said, [00:16:30] why don't you just co um, work for us for real as opposed to being hired, uh, hiring you as a, as an, as a consultant or something.

[00:16:40] **JENS MAURER:** And in between that I had accumulated enough overtime with my previous company that I had. Um, something like four or six weeks of continuous time off prior to actually starting with German railways. Uh, so I, and I was feeling that the random number support, uh, we had in the [00:17:00] language previously, which was just the random number, support of the c programming language, the basis that C++ is based on, um, was insufficient.

[00:17:10] **JENS MAURER:** It was, uh, not well designed. It was dealing, it had global state in it, uh, which is bad because, um, for abstraction purposes, because if you have to deal with global state, it requires, uh, that you need to, um, that you need to [00:17:30] carefully coordinate access to that global state so that different, uh, parts of the program don't interfere.

[00:17:36] **JENS MAURER:** Uh, in undesirable manners and so on. So I figured that is something that should be fixed. Uh, so what would 

[00:17:44] **RAY NOWOSIELSKI:** that mean if they interfered in undesirable manners? What would be the outcomes? 

[00:17:48] **JENS MAURER:** Uh, well, it could be, for example, um, interference in undesirable manners is what technical people call race conditions.

[00:17:55] **JENS MAURER:** So if you have two threats of execution that operate independently, uh, then, [00:18:00] and they both try to modify the same global state, you get essentially unpredictable outcomes because, uh, you need either need coordination between two threats or it just doesn't work correctly. End of story. So. Right. Um, so I figured, yeah, that's something that actually should be improved and should be fixed.

[00:18:20] **JENS MAURER:** And, uh, so I took the time to go to Frankfurt University Library and read up on the current research state of random numbers and, [00:18:30] um, and, and try to design a proper framework for, for those, uh, trying to understand what the appropriate attraction boundaries would be. And then I wrote, essentially, I, I made that implementation and I played around with it and eventually I ended up, uh, publishing it, um, on boost, and later on it became part of the C++ standard.

[00:18:56] **JENS MAURER:** What was key to solving that problem? [00:19:00] I think it was finding the right abstractions and determining that there is two different. Um, parts towards random numbers that are clearly separable and minimizing the interface surface between those parts because minimizing the interface surface, uh, supports independent [00:19:30] evolution of those two parts, uh, to the extent possible.

[00:19:35] **JENS MAURER:** How did that, um, a good feeling if you solve a technical problem that, that you, that you have? Uh, so, uh, it feels gratifying, gives you nice, warm, fuzzy feeling, I would say so. Um, there's nothing like, uh, I mean, I pro I'm probably not the person telling you that, uh, it feels like Napoleon, [00:20:00] um, you know, uh, invading Germany and winning all the time until he no longer did so.

[00:20:05] **JENS MAURER:** But, you know, so the formal review process, um. And I have not following Boost for a decade now, unfortunately. So I can't say whether the process is still the same, but back then it is essentially publishing your implementation together with documentation for your implementation. So, um, you publish that, [00:20:30] there is a review manager that, uh, schedules a de a, a well-defined timeframe, uh, in order to allow everybody to focus on the review.

[00:20:41] **JENS MAURER:** A few weeks usually. And, uh, then other PAR participants, volunteers on the mailing list for Boost. Um, look at your documentation and your implementation in detail and just send you [00:21:00] comments to the public list. And then you essentially get a long list of. Comments, and then you address these comments by changing your documentation, changing your implementation, um, or refuting bad allegations, bad assumptions, uh, because people didn't read the documentation properly or because maybe your documentation is sub power and you better approve it so people don't, aren't confused.

[00:21:29] **RAY NOWOSIELSKI:** So do you [00:21:30] recall who was your review manager and who were some of the people you recall, uh, providing, uh, comments? 

[00:21:37] **JENS MAURER:** I don't remember. I think I have all those emails. I, I go again, I don't remember who my review manager was back at the time and I don't remember any particular names, uh, back at the time because it's just, you know, more than 20 years ago.

[00:21:55] **JENS MAURER:** And, um, I, uh, 

[00:21:58] **RAY NOWOSIELSKI:** that's fine. I didn't know if it would [00:22:00] end up being somebody like Dave Abrahams was my review manager. 

[00:22:03] **JENS MAURER:** Yeah, I mean, Dave Abra Abraham certainly was a popular figure back at the time. Um, in Boost. I don't remember whether he was to which level he was involved in the boost review. If you want me to speak to that, I need to check my emails from that time, which should be still on my computer.

[00:22:23] **RAY NOWOSIELSKI:** Well, did you get through right off the bat without a problem? Were there bumps along the way? Did, did your, uh, did your library get [00:22:30] better as a result of commentary? What do you recall? 

[00:22:33] **JENS MAURER:** Well, as usual with any peer review process, the end result is better than what goes in. So I think there were substantial improvements made, um, but I don't remember, I must admit, I don't remember details at this point in time.

[00:22:51] **JENS MAURER:** Sure. Do you 

[00:22:51] **RAY NOWOSIELSKI:** remember it being sort of a frustrating process or a painful one, or what do you recall?

[00:22:59] **JENS MAURER:** [00:23:00] Being criticized is always. A process that is a bit, um,

[00:23:13] **JENS MAURER:** feels a bit awkward, let's put it that way. And it probably depends on, uh, your personal, um, mindset and character. Whether it's just awful or whether it's, you know, it's you live through it or whether you, [00:23:30] you get anxious or aggravated or something because people criticize you. But I think it's the only way in, it's the best way people have discovered so far how you can make progress in, in a situation where the best you can get is peer review.

[00:23:48] **JENS MAURER:** And peer review is applied to the scientific process as well. If you want to publish a scientific paper, it's subject to peer review. So, uh, the imprint would send out your paper to. [00:24:00] They are reviewers, which are presumably peers and experts in your domain where you are also an expert and give review comments and then the end result is better.

[00:24:12] **JENS MAURER:** So it's not a, not a teacher pupil relationship, uh, but it's a peer review relationship, but still you are, um, you will be criticized. So, uh, the thing you believed was the next best thing to slice [00:24:30] bread, um, actually scaled down a bit because your reviewer told you, oh, maybe it's not slice bread just yet.

[00:24:37] **JENS MAURER:** Uh, so please slice the bread actually instead of just offering bread, um, for example. So, um, yeah, so, so, and, and that process is essentially applied to the publication of these, uh, libraries and yeah, as I said, you get the peer review and people are criticizing you and you have to deal with that. It was not.[00:25:00] 

[00:25:00] **JENS MAURER:** Back then GitHub was not a thing. So, um, the, and the publication of software was definitely not subjected to peer review. So you could certainly publish software on the internet, on web pages. Here it is, but it was usually just individuals posting software and not, uh, and, and then you use it or you don't use it.

[00:25:28] **JENS MAURER:** Or maybe, [00:25:30] uh, organizations posting software. Um, but it was not, it was not peer reviewed libraries. That was, I think, the novel thing, actually investing the time prior to putting it out there and to use it or don't use it, putting in the time to, for rigorous quality control. 

[00:25:53] **RAY NOWOSIELSKI:** Yeah, 

[00:25:55] **JENS MAURER:** I think that was the novel thing that, that, uh, about booth.[00:26:00] 

[00:26:00] **RAY NOWOSIELSKI:** And so random was one of those libraries that made it into the standard. Mm-hmm. In that early two thousands period, you know, leading to C++ 11. Mm-hmm. Um, did you submit a proposal? Can you walk me through the experience that you went through of the standardization process there? 

[00:26:18] **JENS MAURER:** Yes. Actually, um, what we did prior to integrating that into c uh, yes.

[00:26:25] **JENS MAURER:** I know not enough context. I'll repeat it again. Sorry. [00:26:30] The propo, the proposal process for getting my random number library from Boost actually into the C++ standard, in this case, C++ 11, involved several steps. I wrote a proposal first to integrate that library into the C++ fundamentals, um, technical specification that was planned at that time.

[00:26:59] **JENS MAURER:** Hmm. [00:27:00] So it was not directly proposed for integration into C++ 11, but, uh, we were doing something like a trial balloon and, uh, so the Boost random number library was first published in that, uh, technical specification and then incorporated from there into the C++ 11 standard. So what I did was essentially, um, write A-H-T-M-L paper, if you wish.

[00:27:28] **JENS MAURER:** It's still available out there on the [00:27:30] internet. No, I don't know, know the number by heart. Um, and that essentially summarized or, or iterated through the design goals of that library and, um, highlighted or, or investigated design alternatives and why the design was the way it was, and writing down the design criteria and the design.[00:28:00] 

[00:28:00] **JENS MAURER:** Um, and, and the design decisions is materially different from what the Boosts review checked because the Boost review checked just the library implementation itself and the description and documentation of the library, but was not asking a lot, a lot of questions about the rationale of the library and the rationale for that.

[00:28:23] **JENS MAURER:** Those particular designs, I mean, there was a certain level of, of that as well, but it was [00:28:30] mostly a question of, um, of the, the actual library and the, and the documentation of that library. And furthermore, um, at the boost level, you have a specific library and a specific library implementation, and you document that for purposes of the C++ standard.

[00:28:50] **JENS MAURER:** What you want is to write requirements so that, that you can have multiple implementations. That have a clear understanding whether [00:29:00] they conform or not to the specification you write. Mm-hmm. So it's not that you donate your code to the C++ standard instead, um, you, you write a specification and abstract description of what software someone else will write, IE his implementation of your random number library.

[00:29:23] **JENS MAURER:** Um, whether that is good or not good. And it, the [00:29:30] tricky part is to make that specification specific enough, uh, so that um, users can have a, uh, uniform successful experience with whatever implementation they actually you are exposed to yet you le leave enough implementation freedom. To each implementer so that they can do the optimal thing for their particular environment.[00:30:00] 

[00:30:00] **JENS MAURER:** Hmm. I think it was on the order of three meetings that it took to get the random number stuff into the library fundamentals ts, um, technical specification. Um, at least I think I remember making three revisions of my paper. Maybe four, but not many more. Okay. I think, and, um, part of that, that it is [00:30:30] so that it was relatively few is of course, uh, that I had a certain level of maturity in the, um, in the implementation because of the boost review and because of the boost process.

[00:30:48] **JENS MAURER:** So, and yeah, and, and on the other hand. Um, uh, so that, and [00:31:00] then there was, yeah, and then people generally apparently liked, uh, the presentation in my paper that proposed the integration into the C++ library fundamentals, technical specification. And I have heard since I'm a core working group guy, not a library guy, I was never present except for presenting my paper in library most of the time.

[00:31:27] **JENS MAURER:** So this is all rumors, but I have heard, [00:31:30] uh, that, uh, future library authors were pointed to my proposal paper as when they asked, how should a proposal look like, make it look like this. So apparently people liked my style of presentation and the depth of the analysis and all that. So that, of course, contributed to convincing the people, uh, that this was a well thought out design as opposed to a, um, you know, random fart.

[00:31:56] **JENS MAURER:** So when you present a proposal, the first thing is you [00:32:00] actually publish a paper describing your proposal, which means a PDF document or an HTML document, well in advance of a meeting so that it is included in what we call a mailing. Of course, nobody sends around paper things anymore, but we have cutoff dates.

[00:32:20] **JENS MAURER:** When we say a paper needs to be released by that time in order to make that mailing, that's the first step, and that usually means between [00:32:30] three and four weeks before, uh, the next meeting. Okay. All the papers that have been published and time for the next meeting, IE before that, uh, three to four weeks, uh, cutoff date are considered for the, that, uh, next meeting.

[00:32:49] **JENS MAURER:** Yeah, so you have that paper out there. Everybody is at least able to read your paper and give you comments way ahead of the meeting. And that [00:33:00] hopefully makes your paper better because, um, at then you go, then your paper is scheduled by the respective chair of the, uh, subgroups of WG 21, where that, uh, paper is scheduled to be heard.

[00:33:20] **JENS MAURER:** Um, nowadays, back in the day, as I said, we had nothing more than library and core groups. Um, we [00:33:30] pretty. Quickly had an evolution group and I think afterwards we had a library evolution group. Uh, but, um, library proposals for quite some time, I think were heard by the library. Uh, the only library group we had.

[00:33:51] **JENS MAURER:** But my re my, my recollection is hazy in that regard. So we would have to do the archeology on the documentation to, to understand what happened. [00:34:00] I remember Bill Blogger, um, being in the room and everybody saying a few knits about my presentation and which was actually more or less a five minute presentation, which wouldn't fly anymore these days.

[00:34:16] **JENS MAURER:** But, um, as in. Look, here's the two fundamental abstraction concepts that are in this paper, and that's the central thing that that paper embodies and everything else as mechanics and for details, read my paper [00:34:30] and, um, which you should have had anyway prior to coming into the meeting. So yeah, so that was a five minute presentation probably, as I said, nobody would dare are doing this anymore these days.

[00:34:41] **JENS MAURER:** And, uh, some people had some shock and awe reactions, I believe. But, um, others just had a few knits and said, oh, what about this? I answered all the questions and more towards the end bill blogger who apparently was, has a PhD in mathematics or [00:35:00] so, um, said, uh, yeah, that is good, that is well thought out. Um, that, that works.

[00:35:06] **JENS MAURER:** And yeah, that, that more or less was it from a, um, approval perspective of let's do that. So, um, and how many people, the library 

[00:35:17] **RAY NOWOSIELSKI:** chair. Or can. So 

[00:35:19] **JENS MAURER:** how many, how many people were in the room when, when that happened? Maybe 20, maybe 15. Uh, let's call it 20. [00:35:30] And I think at that time Biman DOS was the chair of the library working group.

[00:35:34] **JENS MAURER:** He was the chair for quite some time. What was is still being done is back then and nowadays, um, is that beyond the fact that we want this feature in principle and it's well thought out and everything. Um, we of course need to carefully review that the wording changes that are proposed in the paper, that actually implement that feature, [00:36:00] that these wording changes, um, satisfy all the detailed requirements we have because we have a certain wording style in the standard we use.

[00:36:11] **JENS MAURER:** Certain English words and phrases that are defined to have certain meaning. And you can't just def define, uh, can't just invent your own wording style. That would not create a harmonized, uh, new standard. Um, so that a lot of review goes into making [00:36:30] sure everything just fits the, the general picture and the, the presentation and, and wording style.

[00:36:36] **JENS MAURER:** And of course we also want, um, the words to say the exactly right thing. And as usual, if you try to describe formal systems in the English language, you often discover that the English language is unfortunately a natural language and has its shortcomings and ambiguities and stuff like that, that you would like to avoid as much as possible in formal, in in formal [00:37:00] specifications.

[00:37:00] **JENS MAURER:** So that has a lot of review, uh, going on. Um, I can certainly talk, uh, to the fact of what the review process. Looks like these days much more, uh, than I can talk about the review process back then. The fundamental properties are the same. Uh, you back then and right now. Um, you first degree on design and then you review the wording, and then you have a plenary approval vote.

[00:37:29] **JENS MAURER:** There [00:37:30] are a lot of individual, small, if you wish, baby steps that lead to the eventual, um, standardization moment. As I said, there is first, there is this paper publishing that's already a good moment for you. You've written a paper, you, you've read through it multiple times yourself. You believe it's perfect.

[00:37:55] **JENS MAURER:** So you, you have this warm and fuzzy feeling at least for a moment until the first emails come [00:38:00] in that say, oh, there's a typo over there. And by the way, this isn't thought out. Well. So you have that paper published, then you get scheduled, you have your presentation. You have agreement in the group that they want this particular feature.

[00:38:13] **JENS MAURER:** And again, um, having a boost, uh, boost Library helps quite a bit. Boost had quite a few credentials of being a high quality library, uh, conveyance vehicle. Um, so that helped in, [00:38:30] in, in benefiting from that reputation and the standards committee meeting. Then you have the approval of, yes, we want that feature.

[00:38:38] **JENS MAURER:** That's the next step. Then you have the approval of the wording and the plenary vote that says your wording will go into the next chip vehicle. In this case, it was library fundamentals technical specification that was expressly intended as a trial balloon, but with the intent of standardizing [00:39:00] everything afterwards.

[00:39:02] **JENS MAURER:** Very little from library Fundamentals. TS one was not standardized in the end. Uh, no, I don't remember details. Um, so and so that already feels good if you are selected, if your proposal is selected to become part of that library Fundamentals, ts now it's only the Ts not the next standard. So ts gets published.

[00:39:25] **JENS MAURER:** Then there is this, when is the right time that we get, got enough [00:39:30] experience from the Ts out there that we actually can, uh, can propose to take features from the Ts into the next standard? Yeah, I think it was a year, maybe one and a half years, maybe two years when that started. So I made a proposal, or, yeah, I think I made a proposal to Introdu to introduce that random number proposal from the, um, technical specification to introduce that into the next standard proper with a few [00:40:00] amendments because we had more experience from the publication of the Ts or from the.

[00:40:05] **JENS MAURER:** From the Ts being out there and people, more people looking at it and trying to do independent implementation. So having that approved, including the mild adjustments that were made, was the next milestone. Now it was in the, uh, working draft, leading to the next standard proper. That felt good [00:40:30] as well. And then we had the moment when we actually shipped C++ 11, uh, in, into the ISO process.

[00:40:40] **JENS MAURER:** And the ISO process starts with a committee draft and a, uh, draft international standards. The standard, these are two stages of approval, uh, that you do. And then you have the actual publication stamp from ISO and they put in an official ISO number and put it on, on, into their store. And, you know, [00:41:00] you, you actually have done something.

[00:41:02] **JENS MAURER:** So, um, the. Uh, that moment was, um, when, when we actually had the final vote that, that this package is now ready and we usually make, make a picture of all the committee members that are present at that time. Um, so that was the next big thing where you could say that was a champagne popping moment when we made that group picture.

[00:41:26] **JENS MAURER:** Um, and, uh, we shipped that c plus [00:41:30] plus 11 standard. It was a meeting in Madrid, Spain, where I had to leave slightly early. I don't remember why, but the, uh, the, the plane was leaving from the airport at a time where I had to leave maybe an hour early. And, um, so I actually missed that last vote. Um, and the picture, 

[00:41:59] **RAY NOWOSIELSKI:** did somebody [00:42:00] text you or something?

[00:42:01] **RAY NOWOSIELSKI:** How did you, what did you hear after? Words about how, oh, there's 

[00:42:04] **JENS MAURER:** minutes from the meeting, so you just read the minutes. And, uh, that's about it. I mean, and there was no, uh, there was no expectation or even rumors that, um, that that would've been in jeopardy, that vote. I mean, uh, you, the process sounds complicated.

[00:42:24] **JENS MAURER:** The baby steps sounds overly bureaucratic, but the entire process in ISO [00:42:30] is geared towards not having surprises, in particular, not having surprises at the late stages of development. So the final vote is sort of the anti climactic moment of the process, right? Um, in, in one way it's the final vote. On the other hand, uh, if there is a surprise at that final vote, it would be, uh, really a surprise.

[00:42:58] **JENS MAURER:** So. Um, [00:43:00] so it, it's hard to get into suspense mode just for that final mode because you already know that nobody actually has a, I mean, you've sorted out all the technical objections, you've sorted all out, all the other concerns that people have. People are, have already voted at least once in favor of the package.

[00:43:22] **JENS MAURER:** So, yeah, you know, um, it took a very long time between c [00:43:30] plus plus 98. And the next real standard that we published what was, which was C++ 11, we did publish C++ oh three in between. Um, but that was essentially a back fix release. And the only reason why we had that. Um, C++, uh, oh three release was that we didn't want to be bothered with, uh, writing differences against the standard.

[00:43:53] **JENS MAURER:** And so we just published a new standard and, and that's it. Um, so [00:44:00] yes, it took a very long time, 13 years between C++ 98 and C++ 11 to publish the next standard with additional features. We had a number of delay moments in between where people felt we weren't quite ready, so let's delay a little more, you know?

[00:44:18] **JENS MAURER:** Um, so, um, we knew that C++ 11 was the next standard. Obviously it was certainly a great leap [00:44:30] forward relative to C++ 98. Nobody can predict the future, so all we can say is, or all I can say from my perspective is the. Relevant, pro relevant proposals we had that seemed to have merit have been integrated into C++ 11.

[00:44:49] **JENS MAURER:** We did the best we could in, in making that package. We always rely on individuals proposing features. Because we don't [00:45:00] have act, we are not a big corporation that can direct someone to develop a feature. So it's all volunteer based to some extent. Of course, attendees are employed by corporations and sometimes our corporations out of their own motive, want a certain feature to be developed so that they pay their people to do so.

[00:45:19] **JENS MAURER:** Okay, fine. But, um, in general, as a committee, we can't direct people to do work. Um, so that means we're, as I said, we're volunt. [00:45:30] Volunteer based, and that means we, we sometimes don't get all the features we would be nice to have. Uh, but, uh, C++ 11 certainly was the feature set that was the best we could have had at that time.

[00:45:48] **JENS MAURER:** And yeah, the, and then people use that feature set that apparently were sort of happy. So, um, and we kept going and, and I mean since then we kept going every [00:46:00] three, we, uh, years as you may have not authoring a booth, uh, library is entirely voluntary. Um, if, again, if you happen to be employed by someone or you are self-employed and, um, someone pays you for developing a Boost library, then you get paid for it.

[00:46:15] **JENS MAURER:** If you don't, then you're not paid for it. I wasn't paid for Boost Retina, or 

[00:46:20] **RAY NOWOSIELSKI:** is it voluntary? 

[00:46:21] **JENS MAURER:** It's entirely voluntary to the extent I was explaining. I repeat that. Sorry. No, not enough context. I'm sorry. [00:46:30] Bringing a proposal to standardization is not a paid operation unless you are employed by a company that decides it has business merit for them to get that feature standardized.

[00:46:45] **JENS MAURER:** Attending those committee meetings three times per year. These days, back at the time when Boost Random was standardized, it was just two ti twice per year is voluntary unless a [00:47:00] company sees business benefit in paying their employees for being at the meeting. 

[00:47:08] **RAY NOWOSIELSKI:** So what do people get? 

[00:47:10] **JENS MAURER:** In reality, a lot of the committee participants are sent by the companies they're employed with.

[00:47:20] **JENS MAURER:** So in reality. I am here as on business travel. So my company pays for me being [00:47:30] here. They don't pay me for making a proposal, but they do pay me for being here. I don't particularly care whether they consider that part of the, uh, re uh, of the payment package of the remuneration I get for working for them, or whether they see an actual, you know, uh, technical business impact on my being here other than, uh, I'm the go-to C++ person at my company of course.

[00:47:56] **JENS MAURER:** Um, but well, there is [00:48:00] certainly, I I, I mean, if you could write in your CV for certain companies that value that kind of architectural design work that is represented as a, in an, as a Boost library, um, there's certainly a reputation to be gained because if you have, for example, if you have designed. A library that is then being standardized and that li and that library turns out to be well designed and the review process in boost and also [00:48:30] for standardization certainly weeds out all the bad candidates.

[00:48:33] **JENS MAURER:** Um, then I think you really have gained yourself some reputation in the relevant circles. My personal motive was not to gain reputation, I just felt it would be a good thing to do in the abstract. Um, increasing goodness in the world sense. The position in WG 21 was always as an individual contributor.

[00:48:58] **JENS MAURER:** I'm just a [00:49:00] regular minion. Um, joining these three meetings per year and, um, helping to shape a well, uh, reviewed next C++ standard. Um, I have also written a number of papers myself. Uh, over the past years where I felt that, um, this is awkward, let's fix it. Um, I have not written large proposals, uh, in the past [00:49:30] decades beyond both random.

[00:49:32] **JENS MAURER:** I have helped write large proposals, but I've not, you know, been the primary author, author of large proposals, uh, simply because, um, I'm not paid by my company or to do so, and there's other responsibilities such as, um, wife and, uh, son that, uh, doesn't allow me to do a lot outside, uh, of my daily paid work, if you wish, or, well, I'm currently doing quite [00:50:00] a bit outside of my paid work, but still adding more proposal writing work to that doesn't really help.

[00:50:07] **JENS MAURER:** So, um, I, so yes, I, uh, was writing. Um, so yeah, my position in the stand and sorry, I, the jet lag kicks in. Oh, I hear you. Um, so, so yes. I, I, I, yeah. Cut off all the, all the, all the [00:50:30] garbage here. You know how to do that. 

[00:50:33] **RAY NOWOSIELSKI:** No worries. 

[00:50:35] **JENS MAURER:** So, my role in the standard as I, uh, in the standards committee was, um, as an individual contributor, and in particular as an individual contributor in the core working group for two decades or so.

[00:50:50] **JENS MAURER:** Um, we have very long lasting, um, chairpersonship in the core working group. In particular, the library working group changes. Its [00:51:00] its chair every three years, maybe, or every four years, sometimes. Whereas in core, we really have hereditary kind of situations, uh, where, um. Uh, Mike Miller was chairing for quite a while, and then Steve took over and, um, when he, uh, retired, I got, I got the call.

[00:51:22] **JENS MAURER:** So, you don't apply for this job, you're being just chosen, you know, 

[00:51:27] **RAY NOWOSIELSKI:** by the convener. 

[00:51:28] **JENS MAURER:** Um, [00:51:30] well if formally, yes, you are chosen by the convener, but of course, um, I believe there were recommendations being passed around. Yes, herb Sutter has been convener for ages and Herb Sutter essentially. Appoints, uh, those, uh, chair, chair roles, but, um, as usually you need a volunteer for these roles.

[00:51:56] **JENS MAURER:** So, um, I don't think there has [00:52:00] actually been a competition sort of thing that, you know, there were 20 applicant applicants and then you have to choose and oh my God, that's hard. Well, he usually asks the outgoing chairperson who could be the successor. And in recent times we, um, had installed co-chairs, uh, meaning, uh, that, uh, chairs are invited to appoint co-chairs and those are the natural successors.

[00:52:27] **JENS MAURER:** Should the chair go out or be hit [00:52:30] by a bus or whatever 

[00:52:31] **RAY NOWOSIELSKI:** You may, because we're 

[00:52:32] **JENS MAURER:** picking a best library, working group or library evolution, working group chair is hard for me because simply I haven't been part of the process most of the time. Unless I'm presenting a paper there, I don't go there. Okay. No, that's fine.

[00:52:49] **JENS MAURER:** So that's like, um, you know, uh, picking the best US president in the past two decades because I don't go there. [00:53:00] I have no detailed insight into domestic political issues. So, um, I better leave that just judgment to people that are more exposed to that. Admittedly, the rest of the world is exposed to, um, actions by the US President, probably more than some part of the rest of the world really appreciates, but whatever.

[00:53:21] **JENS MAURER:** The more I got involved with the C++ standardization process, the less I paid attention to boost. [00:53:30] That means I am unfortunately not the ideal candidate to talk about the Boost developments in the past 10 or 15 years. Simply be because just I. Phased out of boost. I'm still sub subscribed to the mailing list, but I have an auto filter on my email that just shuffles away that email.

[00:53:48] **JENS MAURER:** The library working group chair position is probably considered fairly taxing. They have a very high workload because there's [00:54:00] substantially more library proposals coming in than core language proposals. So in particular, in the past when there were no co-chairs, but all the administrative and scheduling work and chairing meeting work, lay, lay on a single person, it's just, you know, um, a lot of effort.

[00:54:22] **JENS MAURER:** And so I think library chairs just were [00:54:30] sort of. Happy to, um, be able to resign maybe, although I obviously have no insight into personal motives. Um, but I am not aware of anyone being, um, hitting a hard limit. As in, you've been in that job for three years, now it's time for you to go out. It was more, at least my impression that those pe uh, those former chairs decided that it's enough and [00:55:00] let's have someone else do the work.

[00:55:02] **JENS MAURER:** Locations of WG 21 meetings get chosen because we have a host, a sponsor that pays for, in particular the conference facilities in the particular place we go to. So if you wish for the C++ committee, the WG 21, uh, to have a meeting in, let's say Nashua new. [00:55:30] Then find a meeting venue, find a location there, pay for it for the entire week, and we're happy to get there, however.

[00:55:39] **JENS MAURER:** So that means meeting locations, repeat because hosts, uh, tend to be the same and they like certain cities because maybe they live there, maybe they have a cheap venue there. And so that's it. So in particular for the Hawaii location, [00:56:00] which, uh, tends to repeat a lot more than some other locations we go to.

[00:56:05] **JENS MAURER:** Um, that's because the sponsor for the Hawaii meeting, um, himself likes to be here as far as I've understood. And the meeting location is surprisingly not as expensive as a lot of other, uh, potential, uh, US locations. 

[00:56:26] **RAY NOWOSIELSKI:** Who's the sponsor? 

[00:56:28] **JENS MAURER:** The sponsor of this meeting is [00:56:30] the C++ Foundation, which is a foundation chaired by Herb Sutter, um, the convener, and my understanding is it's also organizing CPP con, uh, the, uh, C++ conference and or one of the major C++ conferences.

[00:56:48] **JENS MAURER:** And the proceeds from that conference are, uh, are taken to fund the foundation, which is a tax reduced, uh, [00:57:00] you know, 4 0 1 whatever, uh, under us, uh, law. Don't, don't ask for the details. Um, and, uh, those and the funds of the foundation do help sponsoring meetings. So if we do have a host, uh, that. Almost got the f uh, got the financials to host the meeting, but, uh, is missing a few thousand dollars.

[00:57:23] **JENS MAURER:** Uh, then the foundation is available to co-sponsor those meetings. The foundation has also paid [00:57:30] for projectors, um, that are carried between meetings because if you rent projectors in a hotel, that is usually a very large cost as in ridiculously expensive. And it's actually cheaper to buy projectors for a meeting for instead of renting projectors from the hotel for an entire week because, so 

[00:57:54] **RAY NOWOSIELSKI:** her likes Hawaii 

[00:57:56] **JENS MAURER:** and Herb likes Hawaii.

[00:57:57] **JENS MAURER:** That is at least my understanding, [00:58:00] 

[00:58:00] **RAY NOWOSIELSKI:** um, how did you end up in somewhere like Bulgaria? 

[00:58:03] **JENS MAURER:** Well, we have a, um, there's a company called Chaos Group. Um, that is, has a, is either headquartered in Bulgaria or has a substantial presence in Sophia, Bulgaria. And, uh, the relevant people and the relevant person, um, apparently has good ties to, uh, to the business side of the, um, of them.

[00:58:28] **JENS MAURER:** And they decided to sponsor a [00:58:30] meeting. So we went to Varna. Um, Peter ov, Peter OV has only ever joined a committee meeting once or twice, I believe. And no, he was not, Peter Mov, to the best of my knowledge, was not, um, the, the driving force between for, for being in Bulgaria. Okay. So, um, no, no, it's, um, what's the names?

[00:58:58] **JENS MAURER:** Um. The [00:59:00] name of the organizing person, person is Maya, but, uh, that's not the committee member or, um, that's just the, the person doing the leg work of talking to hotels and everything. The most frequent locations that come to mind are actually for me, just Hawaii, because it's such a long flight from Germany, and that's the most obnoxious thing about Hawaii.

[00:59:23] **JENS MAURER:** Uh, and I can't really spend much longer here because I have to go back to the family and my wife is getting upset. [00:59:30] Um, so, um, so, but, but everything else, I mean, yes, we've been to Varner, we've been to to Sophia, but there are a lot of locations we have been to in the past or we were going to, that are once in a lifetime locations.

[00:59:50] **JENS MAURER:** So we've been to Tokyo, uh, recently, but, uh, Tokyo, the last time we went to Tokyo is, uh, before I joined. So more than 25 years [01:00:00] ago, uh, we've been to some place in Austria called Hagenbeck in Murai, which we've never been to before. Um, we've we're, we'll be going to Bruno in Czechia. Um, we've never been to, been to, to that place before.

[01:00:16] **JENS MAURER:** We've been to Sydney, Australia once in the past 25 years. Um, we've been to Albuquerque, New Mexico once, just to mention a few places. Um, so, um, yeah, I, [01:00:30] I don't think the impression of repetition is, is warranted, um, of, of sustained rep, uh, repetition is warranted except, uh, for Hawaii, but maybe my impression is wrong.

[01:00:42] **JENS MAURER:** Well, the headline for this particular meeting is a bit extraordinary because we're addressing national body comments, meaning we have published a committee draft, we have sent that committee draft, which is. Uh, essentially what we would like to [01:01:00] publish as the next C++ standard C++ 26. We have sent this committee draft to what we call the national bodies, which are the national standardization organizations that federate as iso and the ultimate power is vested in these national standardization organizations.

[01:01:20] **JENS MAURER:** So we have sent our proposal for the next C++ standard to those national bodies, and we've asked them for comment [01:01:30] and they have come up with 412 comments in total. So we're now processing as a committee those 412 comments, uh, in order to, again, a peer review process, if you wish, uh, to improve the next, uh, revision of the C++ standard.

[01:01:47] **JENS MAURER:** Uh, that we publish. So we have typos being fixed. We have, uh, certain inconsistencies, uh, that are being fixed. Uh, we have desires [01:02:00] for new features that did not make the C++ 26 cutoff to be considered nonetheless. And somewhere in that spectrum, herb Sutter has decided to step down from convener ship at the end of the year.

[01:02:15] **JENS MAURER:** Um, so our parent body, which is called SC 22, has uh, um, has chosen a new convener. Um, Mr. Guy Davidson, who, um, will, um, [01:02:30] who will be instigated at the 1st of January is that the general committee member, you don't interact a lot with the convener because the sole power that is vested in the convener is to convene meetings.

[01:02:43] **JENS MAURER:** So the convener decides where we have our next meeting. And the convener, um, decides what consensus is in one of those WG 21 meetings. Um, at the plenary level, which we don't have a lot. So other than we have [01:03:00] that Monday morning where we approve the agenda and we have that Saturday morning when we approve plenary, approve all the proposals we have prepared during the week in the subgroups.

[01:03:11] **JENS MAURER:** And yes, there is a moment where we might have contentious vote votes. We usually have that two or three, uh, once, twice, no for one, two, or three votes. Uh, on in Saturday's plenary, we [01:03:30] sometimes have a control, not quite unanimous votes. And there is actually a, uh, a question of calling consensus that is not o super obvious.

[01:03:39] **JENS MAURER:** And yes, that's where we need the consensus. Uh, the convener. But other than that, um, herp is relatively invisible during the week. Um, so, uh, I mean, I have a little more contact with Herp, uh, because, uh, he is the sponsor in his role as [01:04:00] Chair of the C++ Foundation, or CEO, I think is the formal title.

[01:04:04] **JENS MAURER:** Um, I, uh, have a little more contact with him because he's arranging the Hawaii meeting and he's paying for it, and I'm arranging for the hotel to know where the chairs and tables go and all that. So, um, when the hotel ends up, uh, creating what they call the banquet event orders, which is a detailed rundown of how the, uh, meeting works, I need to tell [01:04:30] Herb to actually sign those things and so I have a little more contact with him.

[01:04:34] **JENS MAURER:** But, um, other than that, I mean, life goes on, people get older and I can understand that, uh, her, um, no longer wants to do that. So, uh, let's move on. Dramatic moments are certainly ones when, um, and when people really get upset because, um, [01:05:00] the tides aren't in the way that that particular person likes. And in former times, in rooms, I have not been in, uh, there have been reports of, um, people shouting at each other and, uh, not generally nice behavior.

[01:05:23] **JENS MAURER:** Um, not that, but as, uh, someone. [01:05:30] I think maybe actually the wife of Biman dos once put it, it's actually surprising how people that were, that were really angry at each other on the technical leverage during daytime were still perfect, perfectly fine. Having dinner together, spending the evening together and just socializing.

[01:05:51] **JENS MAURER:** Uh, so people could make the difference between their technical differences and, um, still being nice people, uh, [01:06:00] with the addition of a code of conduct with the, um, with our group growing larger, uh, that shouting matches have subsided. And I think, uh, we're much better at, um, you know, just cutting off those shouting matches when they start developing as opposed to, um, just experiencing them.

[01:06:23] **JENS MAURER:** Uh, so those are certainly, um, 

[01:06:26] **RAY NOWOSIELSKI:** is there one, what was the one that caused shouting. What was that [01:06:30] issue? 

[01:06:31] **JENS MAURER:** And that's where it gets hazy because again, I am in the coworking group, okay, which has been compared to a Quaker meeting, um, as in very calm, except when someone has something to say, then he says that, and then it's very calm again.

[01:06:48] **JENS MAURER:** Is it 

[01:06:48] **RAY NOWOSIELSKI:** libraries? Which section gets the most? 

[01:06:51] **JENS MAURER:** It is usually core language features because for libraries, um, I would say at least that's my position. If you don't like a [01:07:00] parti, a particular standard, standard library, um, or portion of the standard library that caught, uh, standardized don, tough luck. Don't use it.

[01:07:08] **JENS MAURER:** Write your own, use something else. No harm done. 

[01:07:12] **RAY NOWOSIELSKI:** You seem 

[01:07:13] **JENS MAURER:** well, Nat Goodspeed. Um, I've helped Nat Goodspeed, uh, progress his fiber proposal in terms of, uh, helping him write wording. Um, helping him fix the wording he has, uh, helping him to write his paper. [01:07:30] So, um, that's why I, I have been working with him for quite a number of years and, um, but I, the understanding I have is that, um, his turnaround of the papers wasn't always very quick.

[01:07:49] **JENS MAURER:** At least that was my impression. Maybe it's wrong. And the other thing is sometimes he just wasn't scheduled, uh, quickly enough in the subgroups and felt through the, through the cracks. [01:08:00] At good speed is very, very quiet and calm guy. Maybe sometimes he should have been a little bit more aggressive in marketing his paper.

[01:08:08] **JENS MAURER:** Um, so currently I think his paper is with our group, uh, the core working group, but I actually have to double check the. Uh, the status and it barely missed the C++ 26 cutoff. Um, so, uh, and, and because there was just, we focused on [01:08:30] very large ticket items and therefore a number of papers including net good speeds, possibly it just fell through, fell just, you know, we have 15 or so papers in the queue in the coworking group that need review, but because we prioritized the big ticket items for C++ 26 contracts and reflection, we just didn't get to a lot of small things that are still sitting, sitting the air for a plus plus 29.

[01:08:58] **JENS MAURER:** Sorry about that. We have limited bandwidth. [01:09:00] 

[01:09:00] **RAY NOWOSIELSKI:** No, totally. The last few questions, 

[01:09:02] **JENS MAURER:** the question of whether there's favoritism towards certain proposals regarding, um, personal acquaintances certainly needs careful choice of words in the response. Um, there's certainly overall value in, uh, socializing with other participants in WG [01:09:30] 21 as oppo, as opposed to just running your solo mission, uh, because you want acquaintances that can review your papers ahead of time.

[01:09:43] **JENS MAURER:** You want acquaintances and that you can ask between meetings to informally look at an idea. Um,

[01:09:57] **JENS MAURER:** I, there is [01:10:00] certainly a personal preference proposal when chairs have a large choice of papers to look at more that they can handle in the time they have available during a meeting. So there so. Uh, chairs of subgroups get the power to select certain papers that they schedule and others that they don't schedule and therefore will come later.

[01:10:28] **JENS MAURER:** Um, [01:10:30] and therefore maybe being good friends with a chair is, is helpful in these situations. On the other hand, if you are dropped from the schedule two or three times in a row, two or three meetings in a row, that would certainly be reason to make a stink with either the subgroup chair or with the convener.

[01:10:50] **JENS MAURER:** Um, so yeah. Um, I try to, uh, me personally as a chair, [01:11:00] uh, in particular when it came to the hard cutoff about C++ 26, I was making it very clear in plenary that that cutoff would happen, that we would drop papers that are not on the plate. And we would focus on reflection and on contract to the detriment of other papers.

[01:11:19] **JENS MAURER:** And plenary wasn't yelling at me, so I mean, yeah. Um,[01:11:30] 

[01:11:30] **JENS MAURER:** I don't know. Was that an answer? 

[01:11:33] **RAY NOWOSIELSKI:** I think that was 

[01:11:36] **JENS MAURER:** the benefit of the ISO process is that we actually have representation from a wide variety of market participants, both corporations that make C++ compilers, as well as corporations that use C++ in their daily use, or that make [01:12:00] C++ ecosystem components, that it is hard for a single corporation to put their thumb on a scale and.

[01:12:11] **JENS MAURER:** I do remember that for example, Google had a much, much bigger presence in the C++ committee. Uh, in former times they sometimes sent maybe 10 people to committee meetings, which is a lot. And they made proposals. [01:12:30] But some of their proposals took flight. A non-trivial number of their proposals did not take flight to the, uh, uh, to the content of the proposals.

[01:12:44] **JENS MAURER:** I think. And now Google has substantially cut down on their presence here, and they've taken their ball and gone home. Right? Um, there are still people, at least one [01:13:00] person, um, I know of that is employed by a subsidiary of Google that is still present here. Um, I am not claiming, I know all the aff affiliations of, uh, of people here.

[01:13:12] **JENS MAURER:** So that means, uh, the, that I think is a good sign in that, um, even though Google showed a lot of presence, a lot of, let's say sometimes maybe something that looked like [01:13:30] strategizing or so, um, they didn't get their way because there were plenty of other people that have had different opinions on hopefully just the technical merits and not because Google, and I don't like Google or reasons, I think I should not speculate on the reasons of Google why they decided to create carbon.

[01:13:51] **JENS MAURER:** Admittedly, the release of carbon coincided temporarily, uh, with respect to timing [01:14:00] with the, I believe with Google no longer being present on the C++ committee. Hmm. So, um, yeah, I, I think that's a prudent answer here. Well, in, at the times when I was contributing to Booth at the Booth Random Library, um, there was actually a free choice of license for contributors.

[01:14:24] **JENS MAURER:** All it needed to be is a free license. Um, that did not [01:14:30] impose restrictions on people using that library. Uh, since then, corporations have come to boost and, uh, said, uh, this is a lot of bureau bureaucracy for us to vet all the various, probably slightly different licenses. Um, why don't you establish a standard license?

[01:14:49] **JENS MAURER:** We bet that once and everything in Boost is under that simple standard license. And that's my understanding why we have that Boost Standard license and what. I mean, [01:15:00] a lot of non MIT stuff uses the MIT license. I mean, um, it's just convenient to just grab something from the shelf, um, that hopefully a lawyer has seen, um, before you write your own stuff that probably doesn't do the right thing in some corner case attribution, um, means that, as far as I understand, that you don't lie about [01:15:30] who's respond, who's the author of the code.

[01:15:33] **JENS MAURER:** Well, um, it's like saying that not Shakespeare wrote this novel, but I wrote it. And, um, so the question is how credible is that claim given that we are in open source software land that is publicly available, that now that nowadays has. Uh, [01:16:00] commit histories of, um, revision tracking systems available, uh, that use cryptographically strong hash sums and everything.

[01:16:08] **JENS MAURER:** It's sort of hard to lie about provenance and, and attribution of code. Well, it essentially means if you ship a binary, at least that is my understanding, if you ship a binary such as a smartphone app or something that usually does not come with source code, that nonetheless, in the documentation you have to state, uh, [01:16:30] that this particular piece of software was made using these and such components from these and such sources as sort of a, you know, um, reputation building, uh, mechanism if you wish.

[01:16:44] **JENS MAURER:** Or, or, you know, just, just being honest about what components used in your software product that are not your own invention. 

[01:16:53] **RAY NOWOSIELSKI:** Credit. Where credit is due. 

[01:16:55] **JENS MAURER:** Credit where credit is due. Thank you for the phrasing. Sorry I didn't, uh, did [01:17:00] Well first of all, documentation is a nuisance full stop. Um, because the more documentation and stuff you provide, the more angles lawyers might find to sue you over it.

[01:17:10] **JENS MAURER:** So, uh, if you don't provide documentation, nobody can sue you about something that doesn't exist presumably. Um, and so, and I could also envision that companies, uh, just want to pretend to their layman customers that they wrote all this stuff that they ship themselves as [01:17:30] opposed to standing on Giant's shoulders that were there before them.

[01:17:35] **RAY NOWOSIELSKI:** Yeah. Do you think, 

[01:17:36] **JENS MAURER:** um. The new general public license, um, which essentially requires that you publish source code and some licenses that require that you actually, um, state attribution in your, uh, documentation, um, made it more common for, [01:18:00] for users to be required to, to talk about these things in their documentation.

[01:18:05] **JENS MAURER:** Uh, so I, and of course the wealth of software, foreign third party software available these days. I mean, we have, we have approximately 30 years of, of open source software as a public phenomenon under our belt. There. Of course there was stuff before that, but um, I think it really [01:18:30] took off, um, in, in the past decades only.

[01:18:36] **JENS MAURER:** Um, and, and the idea of, you know, having lots of library ecosystems we're talking about that, um, that, that, uh, made the attribution problem a lot more visible, a lot more prominent than, um, than what used to be the case. I guess. 

[01:18:57] **RAY NOWOSIELSKI:** Last one, have you, have you ever seen your [01:19:00] work used in commercial products without acknowledgement?

[01:19:03] **RAY NOWOSIELSKI:** Is there a story? Uh, 

[01:19:06] **JENS MAURER:** so my work is both random. Um, I don't think the library, the, the license it is under requires attribution. Um, I guess, um, I don't, didn't pay attention. 

[01:19:18] **RAY NOWOSIELSKI:** I, I guess I wasn't thinking of that one. Um, I just didn't know if you've ever, with your. With your, so for instance, with the company that sends you out here Yes.

[01:19:29] **RAY NOWOSIELSKI:** Pays for your travel. I [01:19:30] just didn't know if you've ever seen your work used. 

[01:19:33] **JENS MAURER:** Um, the company that sends me here sells services and I'm writing software that powers those services. That software never leaves, leaves the company. Yeah. So, um, and, and certainly when a salesperson goes to a customer, they don't sell.

[01:19:46] **JENS MAURER:** They say, oh, and in order to provide this and that service we're using software written by this employee named Jenz. That seems stupid. So, um, so the only [01:20:00] major piece of open source software I've written is Boost Random. I would say, I guess maybe 

[01:20:05] **RAY NOWOSIELSKI:** it's, but it's interesting you say that 'cause you take it for granted that that would be normal.

[01:20:08] **RAY NOWOSIELSKI:** But it's like in, um, in my industry, uh, a company would never put out a movie and then not mention. Who was the cinematographer, or, you know, 

[01:20:18] **JENS MAURER:** oh yeah, there's 15 minutes of credit scrolling by, um, and including who, who did the, who did the, uh, the, the, the sandwiches for lunch and, and exactly. [01:20:30] Garbage like that.

[01:20:31] **JENS MAURER:** Um, yeah. Um,

[01:20:38] **JENS MAURER:** I was in particular, let's, let's focus on Boost random. Sure. I was actually positively surprised that I heard stories, um, that a commercial company doing a little game, uh, a card game or whatever it was, um, said, and I heard stories. [01:21:00] I, I don't remember them telling me directly, um, that they said, oh, they used a traditional random number generator beforehand and that wasn't actually generating random enough numbers.

[01:21:13] **JENS MAURER:** So. People actually did notice that the card game on the computer wasn't actually, you know, was, was sort of biased or skewed or whatever you call it. And then they replaced that random number generator with my boost random stuff. And [01:21:30] problem solved. 

[01:21:32] **RAY NOWOSIELSKI:** How did that feel? 

[01:21:34] **JENS MAURER:** Well, felt good. Very good. That a, that people are actually using my work.

[01:21:40] **JENS MAURER:** People I've never heard about. Right. 

[01:21:42] **RAY NOWOSIELSKI:** Which car game? 

[01:21:43] **JENS MAURER:** I have no idea. It, the, the level of detail I just gave is, uh, is a level of detail I have about that. Rumors and just an abstract description. Sorry about that. 

[01:21:54] **RAY NOWOSIELSKI:** You said your, your proudest real world impact that you know about from. 

[01:21:59] **JENS MAURER:** [01:22:00] Well, I hope I have a lot more public impact on the stuff I do for, for pay as opposed to, uh, the stuff I do.

[01:22:07] **JENS MAURER:** Um, I mean, but I mean about beyond, regarding 

[01:22:09] **RAY NOWOSIELSKI:** random specifically. Uh, 

[01:22:11] **JENS MAURER:** well, yes, I mean, that's the broadest impact I have about Boost Random because probably there's a lot happening that I don't know about. I mean, um, now that Booth Random is integrated into the standard, nobody probably knows that. I'm actually the original author of that.

[01:22:29] **JENS MAURER:** Even in the [01:22:30] committee a few years ago, I've met someone who wanted to propose a new. Um, random number engine to be added to the random number stuff. And, um, he said, uh, oh yeah, that corner is stupid in, in the existing design and, and a few other things. And I said, yeah. Um, just in the interest of full disclosure, I'm the original author of this, um, so Oh, he said, yeah.

[01:22:53] **JENS MAURER:** Um, well, um, yeah, so [01:23:00] bad and, and of course I assured him that no hard feelings there and everything, but, uh, um, yeah, so as I said, probably nobody knows out there that, uh, there's a person behind that particular facility beyond the committee as a whole doing all the review work. But it still needs an individual or a very small focus group of individuals to progress, uh, a proposal, uh, through the committee process, which intentionally is, uh, designed to be, let's [01:23:30] say, careful and slow moving.

[01:23:32] **JENS MAURER:** Even though sometimes slow moving is really glacial. 

[01:23:37] **RAY NOWOSIELSKI:** Yes. Thank you very much. This was, uh, a lot of fun and appreciate you trusting. Tell, tell your friends on the committee. We do fun. Good interviews. 

[01:23:45] **JENS MAURER:** Uh, yeah. Ah, am I free to leave now? 

[01:23:51] **RAY NOWOSIELSKI:** Yes, sir. Hold on. We're gonna 

[01:23:54] **JENS MAURER:** Alright. Hope, hope it was okay. Uh, tone and, and, and everything.

[01:23:57] **JENS MAURER:** Sorry, I, I'm doing this for the first time ever in my [01:24:00] life, so Really? Really? Yeah, sure. Thank you. I mean, nobody, nobody, nobody films me. I mean, I'm not a person you do movies about, I mean, sorry. 

[01:24:09] **RAY NOWOSIELSKI:** Um.

