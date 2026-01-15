# BOOST_ROBERT_RAMEY_STRINGOUT_v00

- - - -
filmed Date: 2025-12-15  
location: Marina Del Rey, CA  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​https://vimeo.com/1154758596/e1a092b0aa?share=copy&fl=sv&fe=ci  
summary: Gave us probably the best take yet on formal review, using the story of his taking Boost.Serialization through it to demonstrate its strengths. He spoke highly of Vinnie & Alliance and told some good stories we haven’t heard and spoke of Boost Foundation as in over their heads individuals who let Boost become rudderless. He said he’s not sure he believes Alliance’s vision for Boost can be achieved, but he commends that a vision and effort is being made to give Boost a new reason for being.
- - - - 

## Transcript Start

[00:00:00] 

[00:00:00] **CREW:** Alright. This is, uh, boost take one, A and B cameras marker.

[00:00:11] **ROBERT RAMEY:** My name is Robert Ramey. I am 77 years old. I, um, have, I've been a freelancer all my life and I, uh, been in software development in one form or another since [00:00:30] 1968. Uh, and that includes really my professional development has kind of grown up with the, the history of the industry for the last 50 years. Um, my relationship to Boost is that I am the developer of the Boost Serialization Library, which was released around 20 20 20 0 4.

[00:00:58] **ROBERT RAMEY:** I'm also a developer [00:01:00] of the, uh, safe Numerics Library, which was released I think in 2022. I am a, been a frequent contributor on the boost mailing list, and I guess I have a reputation for being. Maybe a little bit contrary and, uh, but maybe not, I don't know. Um, and, and that's the short version of my claim to fame as it [00:01:30] regards boost, well, actually the, the participants in boost span the spectrum.

[00:01:35] **ROBERT RAMEY:** Uh, some people are particularly contrary and some people are, um, very much accommodating. And, and also it varies from issue to issue. Uh, oftentimes technical discussions get pretty animated as like, in real life. The, the less, the less, the [00:02:00] more trivial the issue, the more excited the dialogue is. So, uh, it's very hard to make a general statement.

[00:02:08] **ROBERT RAMEY:** Uh, there are some personalities that stand out. You know, we have, as I say, animated discussions on a regular basis, and I don't really get involved in a discussion unless I have something contrary to say. 'cause what's the point of just piling on board of what somebody else already said and probably better.

[00:02:26] **ROBERT RAMEY:** So in, in a sense, it's, it's selective. 

[00:02:29] **ROBERT RAMEY:** [00:02:30] Hmm, 

[00:02:30] **ROBERT RAMEY:** selective characterization, because I only get involved in stuff that I have different opinion about. There was a fundamental event in 2011 and that was the, uh, the standard. Four C++ incorporated about 70% or more of the Boost libraries into the standard.

[00:02:55] **ROBERT RAMEY:** They're not the, the standard kind of mucked a little bit with them from here and there, but as a, [00:03:00] as a boost was originally, um, the, uh, invented or, or organized in order to promote more libraries for the standard. And, uh, it had, I would say a stellar group of people that were interested in this subject.

[00:03:17] **ROBERT RAMEY:** And they made a bunch of libraries, um, shared pointer, uh, MPL and other things, uh, which became [00:03:30] extremely important. And the standards committee, in their wisdom, uh, incorporated those libraries. At that point. The original motivation for creating Boost pretty much disappeared. Boost was effectively a victim of its own success, and at that point, um, it was a little unclear where Boost would go from there because it had arrived where, [00:04:00] where it set out to go to.

[00:04:02] **ROBERT RAMEY:** And, uh, I met. I went to a Microsoft conference. I don't know, they gave me some sort of deal, or maybe they gave it to me for free or whatever. I don't remember. But, and I, I sat there and, um, they were talking about, I forget what they were talking about, but I sat next to John Kalb and then John Kalb said he was gonna become the, the head of, head of the, the, the board of directors of Boost or whatever, boost Foundation, [00:04:30] whatever it was.

[00:04:31] **ROBERT RAMEY:** Yeah. Whatever it is. And um, and I was thinking under my, I didn't say it, but I'm thinking, wow, you know, that's kind of a dead end. What are you gonna do now? And, um, I think to some extent, uh, that question has never really been explicitly addressed. And so, and that's of course a, [00:05:00] a lot of the animated discussions we have is in a sense there are substitutes for the, for the discussion that we probably should be having, which is, what is Boost, what is the, what is the purpose of Boost in this era?

[00:05:16] **ROBERT RAMEY:** And, um, I think, as I say, we've never explicitly addressed that, I think. And I think that it's part of the reason we have, um, differences that we do have because we're not always on the [00:05:30] same page as far as what we should be doing in the first place. So, uh, and, and a lot of the, uh, uh, and some of the very, uh, important contributors, particularly David Abraham's and, uh, and Beman Dawes, Beman died and Dave Abraham's moved on into other things and, uh, and for, and makes a lot of sense because they'd pretty much accomplished what they set out to [00:06:00] do.

[00:06:00] **ROBERT RAMEY:** So that's, I think that's an explanation or my view of why we are where we are now. Now, some people, uh, Peter Dimov, a stellar guy in the technical world, um, sort of a pain in the ass to deal with, but, you know, hey, we're not gonna hold anybody to a high standard here. Um, the, he still is a big contributor and, and really the top technical person in boost.

[00:06:26] **ROBERT RAMEY:** So it's, it's pretty much a mixed bag. And the [00:06:30] characterization I've give you, given you is maybe just a little bit simplistic. I think, uh, that that's really super typical of the kind of discussions that we have, you know, but, um, the, there is a lot to do, but the original mandate for Boost and a lot of the motivation for people getting involved was to, that everything we should do should end up in the standard library.

[00:06:55] **ROBERT RAMEY:** But now. I think that everything that was done that was [00:07:00] appropriate for the standard library is already in there. So I'm gonna, I'm gonna go along with Bryce [ Lelbach] and agree with him and disagree with David Abraham's on this point. And I think it shows when the discussions we have, they kind of, in my view, circle around and we're getting involved in how to build the libraries and distribute the libraries and, uh, make the, and who's, how should the documentation be to be made more like implementation issues rather than [00:07:30] foundational issues.

[00:07:30] **ROBERT RAMEY:** Now, C++ still needs a bunch of libraries, but personally I don't believe that the libraries that are needed now belong in the standard. I, so I think Boost was very closely tied to, um, promoting the standard, and I don't think that's a good goal for Boost now myself. But, uh, and that's something that I think a lot of people would disagree on because it's fundamentally different [00:08:00] from what the original intention was.

[00:08:02] **ROBERT RAMEY:** But my argument is along with Bryce, is that since the original intention was fulfilled, then you have to look for a new goal. And, you know, we don't have anybody who's really articulated a vision that, uh, large people can get on board with 

[00:08:20] **RAY NOWOSIELSKI:** Now. Last year, uh, Vinnie Falco and C++ Alliance, uh, won a community vote.

[00:08:28] **RAY NOWOSIELSKI:** And so the, the [00:08:30] Boost Foundation that was once created by John Kalb that you mentioned, uh, you know, essentially stewardship of, of the Boost brand and project moved from Boost Foundation to C++ Alliance. I think if Vinny were in the room, he would probably say I am. Uh, I do believe in a bright future for this, and I am voicing, uh, a lot of potential.

[00:08:52] **RAY NOWOSIELSKI:** I guess, what would you advise, what would you hope that the new stewards of Boost would do? What do you think would be the best thing for [00:09:00] Boost and for Code 

[00:09:02] **ROBERT RAMEY:** The Future of Boost? Well, well, first of all, I, I don't wanna speak for Vinnie , but I think that you have a good grasp on way the what, the way Vinnie sees things.

[00:09:11] **ROBERT RAMEY:** And, um, Vinnie has a direction for Boost he, that he's articulated. Um, I don't, I wasn't, I don't think he's, it's been really universally sold. Um, I characterized it as delusional to which he took some [00:09:30] offense, but, you know, um, the truth is that nobody's articulated a a di uh, a more convincing one either. So I, this kind of goes to my point that I think in a sense we're a little bit rudder rudderless.

[00:09:47] **ROBERT RAMEY:** That we don't really know what the next goal is. Now you can articulate and people can articulate a list of libraries that should be done. And, uh, that's, that's valid. I don't [00:10:00] see anybody making those libraries now. And to the extent that people are, I don't see the quality at the same level as the previous ones.

[00:10:10] **ROBERT RAMEY:** So we're back to this situation where I see that the, the whole boost is somewhat rudderless. Well, the, the one, the, the, the needs that were articulated in 1998 were very fundamental. Uh, shared pointer, [00:10:30] uh, meta support for template meta programming and, uh, things, uh, type traits, uh, some fundamental, fundamental numerical algorithms.

[00:10:41] **ROBERT RAMEY:** Uh, these were widely agreed upon to be something that would be really widely useful and well suited to the standard. And the people that, matter of fact, the original founders of Boost, I believe, were on the boo on the standards committee at the time, or if they're not, they were, [00:11:00] well, it's David Abraham certainly was.

[00:11:02] **ROBERT RAMEY:** So at that point, it was easy to agree on what, what needs to be done. Th Now, as I say, that's the, the, the, the C++ standard has metastasized way beyond the original vision. And, and my personal view has a lot of stuff in it, which should not be in the standard at all. So I'm, my view is we should set the standard aside when we [00:11:30] think about what the future of Boost might be.

[00:11:32] **ROBERT RAMEY:** That's no very few people, if any, would agree with that, because the standard has in to most people's views, served us very well up until now. Uh, the real problem is any organization, let's, let's forget about Boost for a minute. Let's talk about Ford Motor Company, or whatever you want to talk about. Once it's successful and in its in its original [00:12:00] vision, it, it becomes static.

[00:12:03] **ROBERT RAMEY:** It becomes, um, what's the word I'm looking for? It's, uh, it becomes, uh, people, it becomes bureaucratic and decisions are made, not by some guy coming up with a brilliant solution and everybody accepting it. It decisions are made by a group of, uh, pretty smart people sitting in the same room with somewhat different agendas.

[00:12:28] **ROBERT RAMEY:** Trading back and [00:12:30] forth and compromising on some new idea. But that's the death of any kind of real creative idea. And it's, and look at the movie industry. I mean, somebody makes a hit movie, and besides the sequels, there's 10 other variations on the same thing. Because then the, the way that progress happens is with one, some guy, usually working by himself comes up with a new way of looking at the world [00:13:00] or in, in my world, in com, in, uh, computability we have new hardware and fancy stuff we didn't have before.

[00:13:08] **ROBERT RAMEY:** And then it's unclear what it's gonna be valuable for. And some guy comes up and, and, uh, says, oh, wow, we can use, we can do this with it, which nobody ever thought before. And then everybody jumps on board says, tries to take credit, credit for inventing it themselves. But that's the way that progress [00:13:30] happens.

[00:13:30] **ROBERT RAMEY:** We've seen it lately in the, in the, the, uh, the graphics processes, which was a very niche thing up in, uh, up until relatively maybe 10 years ago, where, or, and then. All of a sudden some people figured out, well, wait a minute, this is a different architecture. What could we do with this? And they've applied it to things like sorting with, which I have a lot of familiarity and, uh, database operations and now, um, [00:14:00] artificial intelligence training.

[00:14:02] **ROBERT RAMEY:** Uh, these were things that were not originally envisioned when these, uh, graphics chips were originally invented. And, uh, that's how progress gets made. And the way that progress stagnates is when it becomes, uh, accepted and then everybody jumps on board. And then people with like large companies that have some peary interests, uh, wanna direct it in their direction [00:14:30] and it ends up compromising.

[00:14:31] **ROBERT RAMEY:** And that ends up in stasis. That's the way the world works. It's not just boost, it's not just the computer world, it's everything. Well, none, I think everybody would have to look for their own, uh, sitting here in this chair on the spot. It would be hard to think of one. I can think of a, uh, the automobile industry, for example.

[00:14:53] **ROBERT RAMEY:** You know, uh, they've been making the same, the same car improved every year [00:15:00] for the last, uh, you know, 120 years. And along comes the electric car, which is a whole new thing. And they don't really, they they, and they're not, haven't been successful in, in that part of the business. And, um, the educational system, the university system we have is structurally the same one that I went to.

[00:15:23] **ROBERT RAMEY:** And it, it, and it's, and I think in a lot of ways, and I think maybe a lot of [00:15:30] people would agree with this, that it's kind of, um, not the best suited for our era these days. No, we can't agree on how to fix it or change it or improve it. And I think that's actually what happens once there's so many people have an interest in a particular, uh, way of doing things.

[00:15:50] **ROBERT RAMEY:** Nothing happens until something is really disruptive. Well, we can, the one example we see is the electric car. Somebody is successful making a decent electric [00:16:00] car, and now you got five companies doing it. But why do they all do it at the same time? Well, it's not that they got together, it's just once somebody demonstrates a new way of doing things, other people are gonna jump on board.

[00:16:13] **ROBERT RAMEY:** And the people that are doing the old way of things pretty much do everything they can to stand in the way of anything changing because they have a vested interest. It's not, I, you know, to, to use the word blame, I think is a little bit, um, uh, [00:16:30] needless, needlessly, contentious. Uh, the, the thing is, these people, they've developed a committee, an infrastructure.

[00:16:37] **ROBERT RAMEY:** Um, Bjarne apparent up until before C++ most languages were, um, proprietary inventions of the companies that made them and, or the universities that promoted them or whatever, and they, um, they sold them and you paid for a compiler, [00:17:00] whatever. And, uh, that limited their market. But if they didn't know what else to do in order to fund the development.

[00:17:10] **ROBERT RAMEY:** And, uh, now I'm, I'm, I'm speaking really about stuff that I don't really know anything about, so somebody else can chime in here. But, um, Bjarne had spent his formative time working at Bell Labs, and Bell Labs was a very special organization which, um, [00:17:30] uh, promoted new ideas. And, um, and this was fruit. And in the transition or the, the, the, the C++ the improvement from C to C++ was totally Bjarne's creation.

[00:17:49] **ROBERT RAMEY:** As far as I can tell. And, uh, and that was in, in Bell Labs where he had this environment. Now Bell Labs kind of interesting. They were very successful at [00:18:00] making student new stuff, but they weren't particularly successful about from, about, uh, uh, uh, in making money from it. So a lot of their ideas ended up, um, like the Unix operating system, uh, didn't really go as far as Linux has gone, which is a sort of a clone of it because Bell Labs just never had it together as far as making a new business out of something imaginative.[00:18:30] 

[00:18:30] **ROBERT RAMEY:** But there were, uh, they, they did have a good cadre of people including, uh, yarn, uh, that made new stuff. And it's striking today. How little of that stuff, if any, the commercial aspect goes back to, uh, the invention aspect goes back to Bell Labs, but the commercial aspect, uh, you know, it stops before it gets back there.

[00:18:56] **ROBERT RAMEY:** And we have the Apple computer, the mouse was invented [00:19:00] by the Xerox labs and, um, and Steve Jobs saw it and said, oh, hey, this is just what I need. I don't know if Xerox Labs ever made a penny from it, but Geez, J uh, um, uh, Steve Jobs certainly did. So, um. The way that, well, it's the same thing he invented, uh, C++, and finally it kind of, and he didn't want it tied to a particular, um, particular organization like [00:19:30] Microsoft or Bell Labs or anybody else.

[00:19:33] **ROBERT RAMEY:** So he invented this, the C++ standards committee. Now, there have been standards committees for other languages, but he, but those were really more like trying to promote that one particular company's vision. I think he made an effort to make sure, to the extent that he could, that no particular company would control it.

[00:19:56] **ROBERT RAMEY:** And he recruit, recruited very capable [00:20:00] people for the standards committee. And I think that they were successful in creating the new standards library and codifying the language, and this is what we have today. But once you create an organization to manage something, that organization can't really keep up with changes that happen.

[00:20:21] **ROBERT RAMEY:** And so C++, in my view, the C++ standard committee has kind of worked itself into a little bit of [00:20:30] a cul-de-sac. That it's, it's, it's also looking for a vision. They wouldn't characterize that. They don't see it that way. They're busting their butt off to make the next version, but I think that it's not gonna have the huge impact that previous ones have had.

[00:20:48] **ROBERT RAMEY:** And, uh, it's really not clear what the next great thing is gonna be. Now to address some shortcomings of C++, which are, which are, cannot be really fixed [00:21:00] without changing the language. Uh, we've got now we've got Rust. They're promoting their, their thing. Um, and there've been other things, uh, c from Microsoft and I don't think they're really gonna go anywhere.

[00:21:14] **ROBERT RAMEY:** And probably because of Bjarne's Original vision was once you put it in the hands of one company, then it dies on its own. And, you know, you can point to, to, uh, uh, well, I guess C Sharp hasn't died, but then there's the one, the, [00:21:30] um, I forget what it is now. It was taken over by Oracle and, um, and Sun Microsystems and oh, JavaScript.

[00:21:39] **ROBERT RAMEY:** You know, there's a lot of complaints about that. It's been very successful, but it's also kind of a cul-de-sac. I don't know. No, I, I don't think so. I, I, I, I think it's just. That it's not that it's a mistake sell, I, I'd have, you'd have to ask him to tell you the truth. He's, he's very much a supporter of the standards committee.

[00:21:59] **ROBERT RAMEY:** I think [00:22:00] it still reflects his vision of a communal, uh, agreement and, and, and consensus formed development. It's, my argument is that designing something by consensus has its limitations. And I think those limitations have become apparent. And, uh, that's, um, yeah, it's a, I think it's a, a simple answer. Boost as a collection of libraries, uh, written in the C++ language to [00:22:30] help facilitate the creation of programs written in C++.

[00:22:34] **ROBERT RAMEY:** Well, going back to the original founders, uh, David Abraham's, uh, Beman do some other very important developers, uh, Peter Dimov, uh, who's the, gosh, I, this guy in England who wrote a, a lot of the new John Maddock. Huh? John Maddock. John Maddock. And, uh, and then a second tire also of really extraordinarily capable people.

[00:22:57] **ROBERT RAMEY:** And, uh, when you get those [00:23:00] people working together, and it's a relatively small group working together, that and into a common goal, and the coal is, is clearly defined in something, is demand, well, you get a good result. And they, they got a good result. And to say the problems to the extent that there's a problem has occurred due to their success.

[00:23:24] **ROBERT RAMEY:** And, uh, I, so I think it's inevitable. Um, it's just the way the [00:23:30] world has to work it. I don't know. Uh, well, I think that, um, the modern equivalents of those people, uh, are in other places where big things are happening. The people that are designing, um, things like, uh, array processors and, you know, the, the people that are working in Nvidia now, they're not a public group, but these guys are on the cutting edge.

[00:23:58] **ROBERT RAMEY:** And, uh, I don't know [00:24:00] if they still are, but the, the things they made, which, when, which were looked like a really, who the heck wants to spend their life making chips to make better video games for idiots to spend all their time on? I mean, but it turned out that they made incredible stuff. It's got its issues, but stuff that nobody else ever made.

[00:24:24] **ROBERT RAMEY:** And it found a niche in a whole different area. And in that sense, I, I see a certain [00:24:30] parallel between that. The original characterization of Boost? Well, I, I, uh, my parents moved here, uh, when I was about, I think four or five years old. And I grew up in, um, in, uh, Los Angeles. I lived in the Hollywood Hills. I went to Hollywood High School.

[00:24:50] **ROBERT RAMEY:** Uh, then I, uh, I, my, my parents got divorced when I was, uh, I guess, uh, [00:25:00] 12. And, uh, it was a very contenty messy operation in which kind of, um, when every, every adolescence is difficult, you know? And so mine was no less difficult than, than the average in, in part 'cause of that. And, um, and my schooling was, uh, I had some good teachers and I had a lot of dumb teachers.

[00:25:22] **ROBERT RAMEY:** And, you know, I think pretty normal. Uh, I did have a knack for math and physics, [00:25:30] and then I, uh, but I had, hmm, how should I say? I'm not gonna say discipline problems, but I was kind of like a little all over the place and, and, um, it was a little all over the place. Well, uh.

[00:25:48] **ROBERT RAMEY:** I'm trying to think. I I prefer not to go into it, you know, because, uh, it's not too relevant now and it's kind of, it would be kind of embarrassing, you know? But, uh, but the thing was that I [00:26:00] was not really considered by my school counselors as college material. Um, and then I went to, but I, and also I, I didn't really have any idea.

[00:26:09] **ROBERT RAMEY:** Um, uh, uh, my, my father was raising myself and my brother, and he, he was like working really hard at the same time. Strange for my mother. So I didn't really have much guidance as a teenager wasn't a bad thing. Uh, it worked out quite well for myself and my brother in totally different ways. But anyway, I, when I [00:26:30] graduated from high school, I went to Valley State College, which is now Cal State Northridge.

[00:26:35] **ROBERT RAMEY:** I was there two years, and then I, uh, got accepted to Berkeley and I was, I and I, I, I was there two and a half years and, and left with a master's degree in operations research. I was interested and I was, I was considering an academic career, but I, I spent some, a little time there. I was a research assistant and was writing, um, programs for, [00:27:00] uh, fort train programs for doing, uh, some aspects of operations research.

[00:27:04] **ROBERT RAMEY:** But I saw the way the whole university culture was, and I could see that it wasn't, I would not be successful in that environment. Um, so, and then I got drafted and, um, I, I was, uh, I could have probably, I got a low draft number. I probably could have gotten myself out of it by staying, uh, by, by [00:27:30] going for a PhD or something like that.

[00:27:32] **ROBERT RAMEY:** But, you know, I'd had, I was kind of done with the academic. I wanted to experience the real world. I was also, um, pretty patriotic and I wanted to, I, I had confidence that our, um, government officials were, um, uh, trying to do the right thing. And I also wanted some adventure since I'd been in school now all my life.

[00:27:55] **ROBERT RAMEY:** And that way I was kind of reaching, I felt I was reaching the end of the road to what [00:28:00] they could teach me. So anyway, I got drafted, I got sent to Monterey, California. I did basic training. Uh, that was a, uh, and that was a whole different world for me. I mean, I learned a lot about how the world really works.

[00:28:13] **ROBERT RAMEY:** I got my front tooth knocked out. Among other things. I, they gave me a job at, um, program computers, in which I spent time at the Naval Postgraduate School in Monterey. This was being 1970. [00:28:30] And, um, I was at Berkeley during the 1968 fiasco. I had something to say about that. But, uh, anyway, uh, I got out of the army in 1971.

[00:28:45] **ROBERT RAMEY:** And I had a bad attitude and I didn't, I, I didn't really feel like looking for a job. And, uh, one thing kind of led to another. And, uh, [00:29:00] the, I, I decided, I, I knew what it was. I, I decided I wanted something different before I actually got serious about life and, and work. And I, uh, had a friend of mine who was in the Peace Corps in Ecuador, and I said, well, hey, you know, I'll go down there.

[00:29:17] **ROBERT RAMEY:** And besides that, um, I felt my education was lacking in that, I think given the amount of education I had, I should be able to speak a, a foreign language fluently. I just felt [00:29:30] there's certain things that are valuable and to one's education. One would be playing a musical instrument and one would be speaking a foreign language.

[00:29:40] **ROBERT RAMEY:** One would be having a good concept of, uh, literature and history and as an engineering education. Those things were a little bit, um, lacking. And I had studied Spanish in high school, and I, I'm told my, I, I'd stayed in Spain for eight months with my mother while my father was in Korea. And I'm [00:30:00] told that I spoke Spanish then.

[00:30:02] **ROBERT RAMEY:** But any, and I'd worked when I was in going to school, I had worked at not too far from here at the farmer's market in, in, um. And, uh, down on Fairfax, and I was cutting fruit and in the kitchen, and I was working with a bunch of Mexicans. So my Spanish was, was I had something, it was very rudimentary, but I thought, well, you know, I'll take a trip and I'll go visit my friend in Ecuador and I'll go a trip by myself and that'll gimme an [00:30:30] opportunity to actually learn to speak Spanish.

[00:30:33] **ROBERT RAMEY:** And, uh, and that's what I did. And I, I traveled through, uh, by land down through Mexico and through Central America and through Panama Columbia, and got to key to Ecuador after about, it took me about six months to do that. And, um, uh, my Spanish wasn't really as good as I would hoped it would be, but it was serviceable.

[00:30:58] **ROBERT RAMEY:** And I, uh, I [00:31:00] got a, I got a job teaching mathematics at the local university in Guke, Ecuador. And, you know, that kind of led to a whole episode in my life. I don't know if you want to go into that, but, uh, anyway, I forgot even what the question was, but that's the answer. 

[00:31:17] **RAY NOWOSIELSKI:** Well, that's a, I mean, that's a good amount of background.

[00:31:19] **RAY NOWOSIELSKI:** When does C++ 

[00:31:20] **ROBERT RAMEY:** enter your story?

[00:31:21] **ROBERT RAMEY:** Ah, well, C++, um, my first experience with SEA was when I was, uh, [00:31:30] in Ecuador. I, um. Started a computer service, uh, business that would process company's accounting. And, um, I did, I wrote the code for doing this in cobol. It was doable, but, uh, I, I knew that this was not the, this was not the most effective thing, but there really wasn't much alternative.

[00:31:58] **ROBERT RAMEY:** And, um, [00:32:00] I did become interested in, uh, in the language. C at the C++ was never, uh, was not, didn't exist at the time. And I got the source code to a c compiler by some guy written who lived in Santa Barbara, coincidentally. And I adapted it for the computer that I had, um, for, uh, which was the, um, the, uh, data general eclipse.

[00:32:28] **ROBERT RAMEY:** Now c [00:32:30] made by Kernighan and Ritchie was, uh, one of the most I important accomplishments of the late 20th century. As I believe C++ also is. C, uh, before the computer language is like PL one and cobol, they just kept adding more to the language and made 'em bigger and bigger. And then you to, if somebody came out with a new computer, then they would have to, to re-implement this huge [00:33:00] giant compiler and charge letting money for it.

[00:33:03] **ROBERT RAMEY:** And Kernighan and Ritchie said, no, no, no. We're gonna take a minimalist of folks and we're just going to effectively implement, um, a syntax based on algebra. And besides that, we're gonna make a library which contain most of the functionality. This is the genesis of the what is now the C++ standard Library.

[00:33:24] **ROBERT RAMEY:** C still exists. It has its own standard, but the genius of their idea was [00:33:30] to separate the dev a. A. Computer separate. The, the problem of writing a computer program into two parts. One is the language. We'll keep that as small as possible. And the other is the language facilities, uh, which we're going to have just in libraries.

[00:33:50] **ROBERT RAMEY:** So that meant when I got, and I had this data general eclipse, the C the C compiler was actually relatively small and I [00:34:00] could, uh, make it work on the general data, general eclipse, but then all the libraries, like for IO and, uh, you know, all the arrays and all that stuff, uh, I didn't have to write anything because that they had a library which could, the simple compiler could then translate and make the thing usable.

[00:34:21] **ROBERT RAMEY:** So this is why the language c spread like wildfire to all sorts of computers in the, in the late seventies or the [00:34:30] mid seventies. And, uh, this is really, this meant that if I invent a new computer, like Prime or like the, the, um, the 80 80 or the Z 80 or the, you know, uh, 68,000 or whatever, I could have a compiler running it, uh, on it with all the facilities necessary.

[00:34:50] **ROBERT RAMEY:** And probably with one guy doing it, probably, you know, two months. Because I didn't spend more time than doing that to, to move it to a new, new [00:35:00] architecture. So all of these companies that proliferated around that time, um, ended up using c worked out great. Well, this is, this is a question for Bjarne, which he's answered many times.

[00:35:14] **ROBERT RAMEY:** The, the short version is he was inspired, uh, there was a movement after programs started to get to be a certain size. Then, uh, there was an issue of trying to keep them manageable in such a way [00:35:30] that, that you could keep track of everything. And, and they invented the concept of classes. And these classes would be a bunch of code.

[00:35:38] **ROBERT RAMEY:** And this was not invented in c it was invented. And I, Bjarne , I think, refers to as similar. It was a language which did it. Another one was, ah, shoot, I forgot the name of it. Uh, these languages, uh, implemented the concept of having a group of code and the functions that operate on the data, uh, uh, a data [00:36:00] design and then, um, functions which would operate on that data, uh, as one, one piece.

[00:36:07] **ROBERT RAMEY:** And. Uh, or as one module, as one component. And, uh, this was considered this, first it was structured, foaming, and the next thing was object oriented programming. Uh, I remember Steve Jobs made a little blurb about how object oriented programming was going to change the world, and perhaps he was right. But anyway, [00:36:30] this, um, and Bjarne seeing this, I said I, he basically made a program which took this object oriented syntax and generated the C program equivalent.

[00:36:44] **ROBERT RAMEY:** And at that point, uh, it, you had object oriented programming, but then you had the efficiency of c and so then you had something that was quite useful. And it was adopted by, well of, of many people, including Microsoft, for [00:37:00] making the programs in the nineties. And that's how, that's how C++ came to be.

[00:37:08] **ROBERT RAMEY:** It, it evolved or it evolved as an addition to the original c programming language. I was, when I was in university and afterwards, I, I had a different vision for myself than I have now, and I wanted to be a tycoon and I also wanted adventure. And I was from my adolescence. I was [00:37:30] enthralled by stories about Cornelius Vanderbilt and Thomas Henderson and Henry Ford and Andrew Carnegie, and people like this.

[00:37:41] **ROBERT RAMEY:** These were my childhood heroes. And, uh, I, I also became, um, enthralled with, uh, the, the philosophy and worldview and which, which supports those kinds of people. And so one of, [00:38:00] when I, I I, I didn't really feel like working for a big company. I wanted to be involved in the real world. I went to Ecuador and when I got there, I, I had 35 bucks.

[00:38:09] **ROBERT RAMEY:** I, and I ran into some, I ran into a guy in the bookstore who was an American, and, uh, he introduced me to some local people. I had a good educational background. They gave me a little, they actually got me the job teaching in the university. And one of them was the, the agent or the local [00:38:30] distributor for Burroughs computers.

[00:38:32] **ROBERT RAMEY:** Uh, I didn't know anything about Burroughs computers. I looked into it and they were making innovative machines, but they, uh, they and I, and I told at that time my a salary, the minimum salary in Ecuador was $24 a month. And the computer time. Was being sold at $50 an hour. So it wasn't immediately obvious how one would start a business in e computer business in Ecuador.[00:39:00] 

[00:39:00] **ROBERT RAMEY:** So I taught, I got developed a relationship with the, these guys that were distributing a Burroughs computers. They'd, they sold it to a guy. They already went bust. So they'd repe repossessed machine. I said, Hey, hey, I'll help you out with this and that. I'll run your computer center. We're not doing computer programming.

[00:39:16] **ROBERT RAMEY:** That's just a money losing business. But what we'll do is we'll run this little computing center and we'll use it, we'll try and sell the computer time to companies who want to train people or wanna learn about it or whatever. [00:39:30] And you can't really pay me, you know, a competitive something that's really worth it, anything.

[00:39:36] **ROBERT RAMEY:** But I tell you what, you, you give me 200 bucks a month plus 50 hours of computer time. And they thought that was great because computer time they had in, in abundance and, uh, the 200 bucks wasn't that far aligned with what they paid everybody else. So, um, I took that time and, and then I [00:40:00] worked and I helped them.

[00:40:01] **ROBERT RAMEY:** And they beca that little computing center, they be actually became, uh, pretty profitable just by selling computer time to businesses, which were interested in getting introduction into the, into the computer business. Remember, this was before Microcomputers even existed. So, um. Anyway, that went through a number of ma machinations and, um, what I did with the computer times I developed, I tried a couple businesses.[00:40:30] 

[00:40:30] **ROBERT RAMEY:** Uh, one was a check clearing business, um, that I, I, I, I, I thought, well, I might be able to make that successful. And I had also good, good backers, but, you know, it's gonna take too hard, it's gonna be too long to get eight, eight local banks to agree on, on computerizing buying equipment and doing a check clear.

[00:40:49] **ROBERT RAMEY:** And so I, I, I, I gave up, I said, this is not gonna, this is gonna be too, too much of a problem. Uh, Burroughs had a bunch of, um, programs that they gave to [00:41:00] customers, which didn't work, but they helped sell the machines. But the idea made a lot of sense. So I, I made an accounting system with the computer time that I had available.

[00:41:10] **ROBERT RAMEY:** And, uh, then I started selling, uh, service, uh, accounting service to businesses in Guke, Ecuador, and Guke, Ecuador was the commercial center of Ecuador. And there's a lot of small, what we consider small businesses there today, accounting. This business after a lot of [00:41:30] difficulty became successful. And, uh, somebody wanted to buy it in 1985.

[00:41:36] **ROBERT RAMEY:** And, uh, by that time I was really burnt out with it. I sold a business by that time I was married, I moved to Europe for a year. Europe. Uh, it was a nice place to visit, but it wasn't gonna be for me. I moved back to Santa Barbara. Uh, I was originally gonna go move to Monterey, but my wife chose Santa Barbara and that's fine.

[00:41:58] **ROBERT RAMEY:** Uh, I had some [00:42:00] money from the sell sales of my business and I built a house in Santa Barbara. I spent two years doing that, and then I decided, okay, now what am I gonna get involved in? I also went back to the university and studied, um, some stuff regarding electrical engineering. 'cause I was kind of more interested in, at that point, you know, developing new products or whatever.

[00:42:22] **ROBERT RAMEY:** And then I, but then when I looked into actually starting a business, uh, I just didn't, I just didn't see it as being [00:42:30] very, um, lucrative and, um, but, you know, people would pay me to develop software and this, by this time it was in the nineties, and C++ had just become really available. Uh, C++ was instantly obvious to me that it was a good vehicle.

[00:42:50] **ROBERT RAMEY:** Microsoft, uh, used it for making their, um, uh, Microsoft Foundation classes, which was its own library, which, [00:43:00] which, uh, which was kind of, was different from the standard library. It was their kind of their own version. And so I did started doing contract work with that. And then around 2002 or, uh. I needed a, uh, multi-threading package, uh, or multi-threading.

[00:43:20] **ROBERT RAMEY:** So writing something like this, I could see right away, Ooh, that's gonna be a non-trivial exercise. I can't really do that in charge a customer for it. And I [00:43:30] started looking around and that's how I found Boost. And by, so at that time, I was, some, had some experience in C++, I saw the Boost Libraries and instantly recognized their utility.

[00:43:42] **ROBERT RAMEY:** Well, I did a Google search for C++ libraries, or, you know, C++ threading libraries, something of, of that nature. Same way I would do it today. And so, and I, that's how I found Boost, because that's cpl uh, uh, boost had c [00:44:00] plus plus libraries, one of which was included Multithreading. Well, uh, that, that actually goes to the crux of what Boost is.

[00:44:09] **ROBERT RAMEY:** You say, um, I, I want a solution to my problem. I'm writing a a C++ program, which requires multi-threading. I don't have the facilities or I don't have the capability or whatever to write that code, or I don't have the time to write that code myself. I do a search. And then you find Boost has among the things [00:44:30] that the Boost Libraries, one of those libraries is a C++, uh, is a multi-threading library.

[00:44:36] **ROBERT RAMEY:** So what you do is you download a large zip file and you unzip it. Now on my machine, I have a whole bunch of new C++ code, or it's new to me, and then I can start incorporating into the programs that I write. So you can say Boost is the library or Boost is [00:45:00] the organization. Uh, depending on the context, they're both true.

[00:45:04] **ROBERT RAMEY:** You find boost.dot org and they have, um, a page. You can find it now. And I, I don't know, um, since Vinnie took over, he made a new website and I, I don't, I haven't needed to look for much, but it includes what Boost, what the goal of Boost was, what it consists of. Are these libraries included documentation on each of these libraries and how they work?

[00:45:28] **ROBERT RAMEY:** I'm gonna, sorry about [00:45:30] that. Well, I mean, I've been involved in Boost for now 20 years. I don't remember at what point I read it, but, um, the fact is you don't need to know this, uh, to use Boost. A Boost took off was highly successful just because the distribution mechanisms is exactly as I described. I'm looking for a solution to a problem.

[00:45:53] **ROBERT RAMEY:** I don't have time to fix it. Don't need to know anything. And one great thing is we go to the Boost [00:46:00] website and you say, here's a library whose name suggests that it might solve my problem. And bingo, right there is a good set of documentation describing what the library does. And how to use it. Uh, by the way, almost no software package actually ever included this before, so this meant that.

[00:46:21] **ROBERT RAMEY:** Um, and it also had tests which show how to use the library and can verify that the library does what you want. It was a nice, [00:46:30] complete package. And Boost has the standards that you have to meet as far as the documentation, as far as tests and, uh, things like that license. So it meant that I could download a whole package, uh, in a day.

[00:46:46] **ROBERT RAMEY:** It's not, I had a guy, he, he, um, he sent me a message saying that I've been using, I forget whatever. And I, I was, it was too difficult to use or [00:47:00] whatever. So I went to the Boost website. I downloaded Boost, I read that the information on the serialization library, four hours later, I'd, I'd done what it took me months to do before.

[00:47:13] **ROBERT RAMEY:** And this is not an uncommon response in situation. And, uh, that's why Boost took off. It solved real people's problems in a good way. In a definitive way, I should say, [00:47:30] well, another people way, people might, that's the way I found it. I think that's extremely common, but I'm sure other people find it. If they're working in a larger organization and that organization, uh, uses boost, then once they look at the code that that, that they're working on and it uses Boost, they're by necessity going to have to find out something more about Boost.

[00:47:50] **ROBERT RAMEY:** Well, one thing it is interesting here is a very succinct history of Boost: Beman Dawes and Robert Klarer developed the idea for a [00:48:00] website during a series of corridor conversations in March, 1998, meeting at the C++ standards committee meeting in Sophia, auntie, auntie Polis, France. Well, that's pretty much it.

[00:48:14] **ROBERT RAMEY:** Create a website and it takes off. That's the way that all websites work. If they're successful, of course, that's like only 1%. But, um, anyway, if you, if you find a solution and offer it, uh, these days it takes off like wildfire. [00:48:30] So let's just pick a couple questions I'm gonna look at in the questions in proposed answers.

[00:48:35] **ROBERT RAMEY:** You know, let's have a look. Uh, who does peer reviews? Volunteer peer reviews, very interesting. No other website at the time, and actually to this day that I know of, has a peer review process. Now, uh, you, so you submit your library. Let's take example. The serialization library. Uh, the serialization library [00:49:00] really has its origin in Microsoft Foundation classes, which had their own serialization functionality, which was basically quite good.

[00:49:10] **ROBERT RAMEY:** I had a few complaints with it, and one of which it wasn't, it wasn't totally portable to other environments. Well, Microsoft doesn't really want it to be portable, so I said, so basically this would be a good candidate for me, for me to learn C++ really well. And, uh, so I am, [00:49:30] I am, I wrote the library, I followed the boost guidelines for documentation and, uh, coding standards and things like that, and I submitted it for review.

[00:49:40] **ROBERT RAMEY:** And as it turned out, it wasn't nearly, nearly, nearly good enough for Boost because it had too many bugs. It, the documentation wasn't as complete as I thought it was. It didn't have as many tests as I thought it should have, as, as it really should have. And it had [00:50:00] ambiguities and. I and my library was the first one, well, from the peer review, peer review process.

[00:50:08] **ROBERT RAMEY:** So I submitted it and then I, it included examples and, uh, the, a lot of people had positive views of it, but, uh, many people pointed out things that were either wrong or ambiguous or needed to be improved or didn't co didn't cover the subject or [00:50:30] whatever. Now remember, I'm getting critiqued by people like David Abraham's, Peter Dimov, and really the luminaries of the C++ world.

[00:50:40] **ROBERT RAMEY:** So here's my code, and as I say, uh, I was kind of a C++ hacker as I am today. But, uh, and here my ure is getting, uh, serious treatment by the luminaries of the whole community. This is [00:51:00] pretty bracing, and in fact, the things that they brought up made it clear that it really wasn't good enough to distribute as at the same level as shared pointer and MPL and other, other boost artifacts.

[00:51:17] **ROBERT RAMEY:** Now, when I get, when I fail at something, well, when one fails at something, there's kind of two reactions is either really get depressed and dejected and move to something else. Double down [00:51:30] and make a real commitment. Well, I'm kind of in the second group, and so I decide, I took all this input, which was a lot, a whole list of things.

[00:51:41] **ROBERT RAMEY:** And I spent a few more months incorporating all of this into, uh, the, the second verge of the library, which, uh, effectively, which after some back and forth, not too much, uh, got accepted. To my [00:52:00] knowledge, this is the only library ever. There might be one other one, but at least it's better story. I'm gonna say it's the, the, the, the only library ever that got rejected and then sub subsequently accepted.

[00:52:15] **ROBERT RAMEY:** And, um, had I had this boost review process not existed, uh, that library would, that library would not exist today. And, uh, there are now [00:52:30] a number of serialization libraries, many of whom, many of which are really derived from the Boost Serialization library. The Boost serialization library has hardly changed in 20 years.

[00:52:42] **ROBERT RAMEY:** Which I think speaks well of it. Of course, part of it is 'cause I don't muck with it, but that other people can't stop messing with something. It's like plastic surgery. Um, when you have a computer data set, uh, let's take an automobile. You've got a car, and then the car's got parts [00:53:00] and the each part has its own parts list.

[00:53:03] **ROBERT RAMEY:** So if I wanna sit down, and matter of fact, you've seen one of these exploded diagrams, right? With the parts all over the place, and then you have a whole list, and then it's got numbers, and then some parts are agglomeration of other parts. So they have their own diagram. So if you have a automobile parts list, it comes up in a book with a number of pages, and it's really complicated, [00:53:30] right?

[00:53:30] **ROBERT RAMEY:** It's not only do you have the parts, you have the relationship between the parts, uh, some parts are repeated like screws, uh, other parts have variations for a different model. So your, the, the automobile parts diagram is actually a very intricate and complex interrelated set of data. Now suppose you want to, uh, write that out to a computer file, which is basically just a list of characters.[00:54:00] 

[00:54:00] **ROBERT RAMEY:** Well, how do you do that? You, how do you capture all these relationships and the, the, the, the, the questions I just described in a linear list, like pros? Well, the old way or the normal way of doing this, well, you just start doing it by hand. Well, here's a part and a part's got this part and that other part's got these parts, but this part's repeated and you end up with a hugely long list of [00:54:30] idiosyncratic pros.

[00:54:32] **ROBERT RAMEY:** Well, what the serialization library does is it understands C++ and the person codes, this parts diagram into C++ with these relationships. That's what C++ permits one to do. That. And, and that's kind of the genius of it, is you can take something, you can code something, you can describe something pretty complicated and that des and the serialization library takes [00:55:00] that description and turns it into this list of pros.

[00:55:05] **ROBERT RAMEY:** And it also generates the code, which takes that prose back and generates it back into the parts diagram data set. So it takes an arbitrary, complex data set, turns it into a serial list of characters, and then at another machine or another time takes that serial list of characters and translates it back into the C++ data set.

[00:55:29] **ROBERT RAMEY:** Has that [00:55:30] sound believable? That's the, that's really the crux of the question. It doesn't matter. Uh, once you can encode it in, in a C++ program, how would you move that to another machine or another time you can't do it because we don't have media which, and which co Oh, the only thing that we have would be the parts list that we originally started with.

[00:55:53] **ROBERT RAMEY:** But that's not really effective for, you'd have to type that in all over the place, somewhere else. What's up with that? The, it [00:56:00] takes anything you can express in C++ turns it into a linear set of characters and takes that linear set of characters and brings it back into the C++ world. So anything that C++ is used for, might and wants to save its state from one place to another or one time to another, has to do some sort of serialization process.

[00:56:26] **ROBERT RAMEY:** It has to translate it from a C++ type [00:56:30] data structure into a text type data structure and back and back. And what's not gonna do that, if you make a text editor, uh, you've got a text editor, it's got words and paragraphs and spelling and, and it's actually pretty complicated. It might have links and whatever.

[00:56:48] **ROBERT RAMEY:** And I wanna send that text editor to some, some one of my fellow programmers and what, what's he gonna do? Or I or I, I make, um, I, I make a, uh, I [00:57:00] write a book in that text and what do I do? I serialize it to a bunch of characters. I move it to another machine, or I open it up a year later and I deserialize it back into the original C++ format.

[00:57:12] **ROBERT RAMEY:** Now I can fi fix the program. So this idea, it's to move a, a, an idea, a data abstraction or, or actually implementation of a data abstraction from the computer world and place it into the text world and vice [00:57:30] versa. It's really a translation version from, uh, method, from one domain to another and back. And, and it's if, think it another way, let's suppose I wanted to make something.

[00:57:43] **ROBERT RAMEY:** I was wrote a novel and I wanted people that read Spanish. I'd have to find a Spanish translator. So we'd move it from English into Spanish. Now that guy passes around, that guy wants to translate it back into English. Well, you'd have to find a translator to do that, right? And [00:58:00] if you're in the C++ world, translating data from one domain to another, the serialization library does that without having to look at the particular data.

[00:58:09] **ROBERT RAMEY:** It's totally general in the sense that C++ is totally general. So it's a big step up from translating English into Spanish. It's like translating English to any language. We have C++. And you start looking at your data, and your data has a structure, and that structure is [00:58:30] encoded in C++ in C++ syntax.

[00:58:33] **ROBERT RAMEY:** And you say, okay, I've got the parts list. Okay, well let's make an object. And it's, I'm gonna call it a parts list. And that's a collection of parts. And each part is a collection of other parts, and each other part is a collection of other parts. So I would start out at the top and say, okay, write the word parts list.

[00:58:57] **ROBERT RAMEY:** And I would write some data about it for the Ford [00:59:00] 19 70, 19 97 Ford Towers parts list. And then. I said, look at my parcel list. It's got four wheels. And then I add onto the text output four wheels, and then for each wheel I might include includes front disc brakes. And then I would write code to say, to add to the text file, front disc brake.[00:59:30] 

[00:59:31] **ROBERT RAMEY:** And then I would say, ah, and I, by the way, I want to make a little detour, and here is the features of the front disc brake. So then I might say, oh, okay, I'm gonna indent my text and write the description of the front disc brakes, the diameter and whatever, et cetera, et cetera. This process, you would all do by hand.

[00:59:53] **ROBERT RAMEY:** That's how it was done. And some people still do it today because they're gluttons for punishment [01:00:00] because they think that it's faster or who knows what. Now with a new system, I describe, a parts list consists of parts, and there's two kind of parts. There's parts that are sub parts and there are parts that are not parts.

[01:00:14] **ROBERT RAMEY:** And this process of walking through the data structure and emitting the text is now automated by the serialization library, but I could still do it by hand. If I had nothing else to do, you know, if I started keeping track of that, I would never [01:00:30] embark upon it in the first place. But I'm gonna probably say from start to finish, no less than two years.

[01:00:37] **ROBERT RAMEY:** Not to say that I was necessarily full-time on this because I was doing it, uh, while at the same time I was doing my freelance work and I also was long, uh, I wanted to motivate myself to be a much better C++ programmer. I wanted to be at the level of Peter Dimov and John Maddock and these people.

[01:00:59] **ROBERT RAMEY:** [01:01:00] And the only way to do that is to practice. And, and by the way, this was a hard problem that nobody had cracked. And, uh, it did require, uh, as far as I know, C++ is the only language that can serialize its own stuff. I might be wrong on that. C++ is a cut above other languages as far as its ability to make, to ma manage abstract con, uh, concepts.

[01:01:28] **ROBERT RAMEY:** And, um, so [01:01:30] for all these reasons, I, and also, uh, it, it just got my goat. I just wanted to accomplish something of scale that other people had not done. It was my ego. If you wanna go a little bit more into background, my whole life is defined. By doing things which are hard or impossible to do. I, I went to Ecuador.

[01:01:55] **ROBERT RAMEY:** I started a business, uh, in the computer business in [01:02:00] 1970s. Be, and then I developed that without going into details. It was a huge accomplishment. Even, uh, at one point I was $250,000 in debt and, um, event, and then it, it event, I kept plugging away with a, a vision that I had. It became successful and I sold it for a comfortable, uh, amount of money.

[01:02:26] **ROBERT RAMEY:** That was a nobody that, nobody does that. That's [01:02:30] incredible. And I just visited Ecuador a couple, two years ago, and, uh, and 40 years ago I left and everybody I had contact with wanted to meet me and still remembered me. So I was, and I'm sure it was in large part because of that particular accomplishment.

[01:02:49] **ROBERT RAMEY:** I, I moved to Santa Barbara. I took a house on a, a course on how to build a house. I built my own house there. I'm very pleased with it. I live in it to [01:03:00] this day. It's a two year job, seven days a week. I like to take on a hard thing and I'm just, that's my personality weakness, C++ serialization, library, the same thing.

[01:03:15] **ROBERT RAMEY:** Uh, the postman sort. Another, um, a programming task on the scale of accomplishment of the, uh, serialization library. Uh, it's just, it's just the definition. My life is just a [01:03:30] sequence of random successes punctuated by a significantly larger number of, um, failures. Oh, I, 'cause I kept making progress. It's like dope.

[01:03:43] **ROBERT RAMEY:** You know, you get, you get a little positive reinforcement, you can't stop. For sure. And also, you know, once you've invested a certain effort, your ego won't permit you to set it aside unless it's, unless you're forced to, unless you're driven bankrupt or something like that. [01:04:00] Oh no, it was immediately obvious that they were right and I was wrong.

[01:04:03] **ROBERT RAMEY:** Uh, I mean, it, this wasn't, you know, a, a bunch of random, um, you know, um, podcast or posters or whatever, you know, calling me a Nazi or something. I mean, these were people who really understood what they were doing and, uh, they actually had an interest themselves in the topic and made actual detailed analysis [01:04:30] and in many, in some cases, constructive suggestions.

[01:04:34] **ROBERT RAMEY:** And, um, I did have to deal with the issue of consensus. But even so, I mean, these were people. That I could really learn from. And they were right. I mean, the criticisms they made, you know, when I step back and look at it, you know, you write, you make your own work of art and it's perfect, and other people look at it and they'll point out all sorts of flaws.

[01:04:56] **ROBERT RAMEY:** You got two responses. Wow. [01:05:00] They can't be right or wow, they are right. And you have to know when, when to use which response. Okay. The way that boost review, peer review work, uh, process works, and this is a work of genius. I don't know whether it was, whether it was, uh, David Abrahams or, um, Beman Dawes or, and probably was expired, uh, inspired by the academic peer review process for papers.

[01:05:29] **ROBERT RAMEY:** But [01:05:30] anyway, that they, they, your project get, would get accepted for formal review before just about every submission would get accepted for formal review because it was so hard to craft a, a, a, a submission. Nobody could afford to spend the time to do it unless you were, you know, pathologically stubborn.

[01:05:52] **ROBERT RAMEY:** But anyway, uh, and then it gets scheduled for the formal review, which is a period lasting two weeks. And at that [01:06:00] point. Other people interested in boost and boost collaborators and boost members or people who, who were members, and I'm gonna guess that number of people that would chime in on a, a library like serialization would be like 30 people, uh, and 30 very capable people for the most part.

[01:06:18] **ROBERT RAMEY:** And they would actually spend one or two days trying to use your library and make it work and write a report. And that period is a two week long period. And you get these [01:06:30] reports, you answer questions, and of course when you answer questions, it becomes totally apparent that the documentation you wrote isn't sufficient.

[01:06:38] **ROBERT RAMEY:** So you, uh, and then people make mistakes or misinterpret and you realize that you were ambiguous about stuff that never occurred to you was, was, was confusing. So anyway, all this feedback you get gives you fodder to make it better or to address it or to convince you that it's a lost cause [01:07:00] or both. So, uh, that's how the process works.

[01:07:04] **ROBERT RAMEY:** Sometimes the review process gets extended by another two weeks, but it's compressed into a two week period and where everybody, uh, invest some effort and makes a critique, you know, and something like that. There's so much stuff going around and remember it's 20 years ago and like, I can't remember half the stuff that I should anyway, but, um, it's very, very odd [01:07:30] that.

[01:07:30] **ROBERT RAMEY:** Um, and I don't want to really go into it, but some guy, uh, there, and there were a lot of things in there that, you know, but one particular point was on a, a technical aspect on the serialization of raw pointers. Okay? That's not gonna mean anything to most people, but he pointed out that my, I, the system that I had for doing that was not gonna work [01:08:00] or was had real serious deficiencies.

[01:08:03] **ROBERT RAMEY:** I blew it off. I argued against it because that's what one's first reaction is. And his, his final sentence is, well, okay, I've done my best. I'm sorry I failed to convince you. And then for some reason, that one sentence, that's almost word for word I'm saying, shit, man, this guy, maybe he's onto something here.

[01:08:26] **ROBERT RAMEY:** It was way of expressing it made me [01:08:30] take it seriously as opposed to just spitballing. And I stepped back and I said, son of a bitch, you know, the guy is actually right. And I, and I upgraded and the op, the, the library to uh, do it his way. Well, I'll go back a little bit farther 'cause I don't remember where I was.

[01:08:49] **ROBERT RAMEY:** Uh, so, uh, and during this review process, you know, people offer their opinions and whatever, and I either dispute them or a lot of them are trivial or I explain or expand [01:09:00] upon them. And one gentleman in one particular arcane aspect, uh, which is the serialization of raw pointers, which was, I included 'cause I, it was necessary for completeness.

[01:09:13] **ROBERT RAMEY:** The Microsoft serialization library did not have that. But anyway, I implemented this and he argued that I didn't do it right, uh, or that the way I did it was deficient in some way. And I argued against this because I invested a [01:09:30] significant amount of effort in making this work. And, uh, we had a back and forth and he said, well, gee, I'm, I guess I just failed to convince you.

[01:09:44] **ROBERT RAMEY:** And which was true. And, and the way he did that, it, it, it's, I remember that to this day, it was sometime later, maybe, maybe a day or maybe just later the same day or maybe a couple days later, I'm thinking, son of a bitch. [01:10:00] Actually that guy is right and I was wrong. And um, that's something that doesn't happen very often for somebody to say that.

[01:10:12] **ROBERT RAMEY:** And, but, uh, the way he made his argument and the way he gracefully acknowledged that, uh, I had the final say motivated me to look more carefully and I concluded that he was absolutely right and I was absolutely wrong. [01:10:30] Um, a little incident like this is, is very character building and helps one grow. And that was the beauty of Boost.

[01:10:41] **ROBERT RAMEY:** Here I'm interacting with people that arguably are smarter than I am. Maybe that, maybe, maybe not now, but anyway, whatever. The way this works is, is that review process continues on before it's done. It's pretty apparent whether or not the library is gonna be [01:11:00] accepted or not. And it's not because of prejudice or whatever, but if the review process brings out a lot of failings in it or a lot of things which are going to make it not a good.

[01:11:12] **ROBERT RAMEY:** Boost library, that becomes apparent to pretty much everyone. For the most part. Uh, I would say that applies to 80 or 90% of the libraries. Some, it's, it's, it's, it's, it's, it's in dispute till the end. But some, some libraries are so well done and [01:11:30] so obviously useful and then you get the reviews and that's confirms that then you know it's gonna get accepted.

[01:11:37] **ROBERT RAMEY:** And some libraries, uh, it's very apparent they're deficient, you know, they're not gonna get accepted. I did the, I got a lot of feedback from the first go round when the library was rejected and I recognized that the rejection was totally appropriate and valid. I doubled down and I [01:12:00] explicitly went through the list of all the points that were brought up in the first review and made sure that the second version of the library addressed every single one.

[01:12:10] **ROBERT RAMEY:** And at that point, when the thing went through, review, it actually pretty much just coasted through because I did the work. I took, I took a hint and doubled down instead of, you know, putting on my hat and saying, you know, hell with you guys. I never have [01:12:30] proposed it for the standard. No one else has proposed that or any other library for the standard, for serialization for the standard.

[01:12:38] **ROBERT RAMEY:** The standard has no serialization library in it. There. It, it's not on the list. Nobody is interested in standardizing it. I'm certainly not interested in doing it. And what's the point? It's already there. Now, but you kind of [01:13:00] touch on the actual oblique point is that the, getting your library into the standard is a, is a, is a feather in one's professional reputation, a very high order, and then you can turn around and put on your resume.

[01:13:16] **ROBERT RAMEY:** Um, I am the, uh, promoter of the, the, um, let me take an example. Ah, shoot, I not, not one comes to mind right [01:13:30] now. Um, you know, library X and you're identified with that and through your career, and it's very much helps, or I at least you hope it helps your career. It's something that very few people have accomplished and in that it's like getting a, a, a highly cited scientific paper accomplished, um, published.

[01:13:50] **ROBERT RAMEY:** It's in that order. And so a lot of people make an effort to add things to the serial, to the standardized standardization library. [01:14:00] And, uh, they're successful and that's why the standard, uh, uh, standard library continues to grow. Beyond what, in my view is its appropriate size. I'm very, very flattered because Peter Dimov and I dispute stuff all the time.

[01:14:17] **ROBERT RAMEY:** I actually asked him for once, I asked him for a letter of recommendation, 'cause I wanted to attend a particular course, and he refused to give it. So, [01:14:30] uh, we have, um, uh, we have a, and he's kind of a, a little bit of an acerbic kind of guy, you know? So, um, I, I think we have actually a quite a good relationship, but it, it's not really based on our, um, on our, what do you call it?

[01:14:50] **ROBERT RAMEY:** Uh, our emotional attachment anyway. Um, the, the truth is for me, one of the, the fundamental things about [01:15:00] Boost is, uh, there was a backtracking, just a hair. There was a, a book I read by Andrei, and I cannot pronounce his name. It starts with a name, Alexandrescu, that's the guy, and he wrote a book on C++ template meta programming.

[01:15:17] **ROBERT RAMEY:** Now, template meta programming is another layer of C++ programming, which was invented by, I don't know whom, it wasn't written into the language. It was discovered by [01:15:30] accident. They'd made the language sufficiently.

[01:15:37] **ROBERT RAMEY:** Sufficiently sophisticated in dealing with abstraction that it permitted one to write a program that would write other parts of your program. It took, it was it, that's why they call it meta programming. And meta programming is necessary to write certain kinds of tricky, uh, [01:16:00] operations like the serialization library.

[01:16:02] **ROBERT RAMEY:** And, um, Alexandrescu wrote the book and, uh, it was a work of genius, like C++ was a work of genius. Uh, and so he invented this way of extending C++ into writing about itself, trying to explain stuff that normally takes like a, a month of, of, of focus to try and figure [01:16:30] it out. So I'm trying to give you the short version.

[01:16:32] **RAY NOWOSIELSKI:** Appreciate it.

[01:16:33] **ROBERT RAMEY:** Yeah. Um, but, uh, that became apparent. On one hand that, wow, this is a very arcane, weird area, and nobody's gonna understand this, but it, it, from time to time, it does something that you can't be done any other way. Do I wanna invest any of my career time in this? My, my initial reaction was, no, because it's just too narrow.

[01:16:59] **ROBERT RAMEY:** It's just [01:17:00] too tiny, a cul-de-sac. And, you know, I had to make a living. And then, um, I, I, I discovered Boost. And one of the things, one of the things I discovered was MPL. This was called Meta Programming Language. It was written by David Abraham's and another Russian guy, I think David Abraham's and, and Aleksey something or other,  Gurtovoy, I think.

[01:17:23] **ROBERT RAMEY:** I'm not sure what, how they divided the roles there, or if maybe one or the other was predominant. But, [01:17:30] uh, David Abraham's used this meta programming facility to generate a library of useful things that meta programming can do. At that point, he brought it back from outer space just into the stratosphere.

[01:17:46] **ROBERT RAMEY:** And so it became more usable to, for the rest of us. And, uh, that made meta programming much more accessible and much more usable. And [01:18:00] I, I depended upon it to make the serialization library. For, to do the things I wanted to do. I don't know that I could have done it without, um, MPL, but I think that stands, and this is really one of the reasons and only one why I, I believe that David Abraham's is way underappreciated among the programming community.

[01:18:24] **ROBERT RAMEY:** He's just not as famous as he should be. Uh, probably 'cause he's such a unpleasant person to [01:18:30] deal with. You know, nobody really wants to be responsible for promoting him. But any case, uh, that's the one thing I think, uh, that. I believe has had a huge influence on, uh, on Boost and subsequently on C++, because now, uh, Peter Dimov made his updated version of that, which is slicker and easier to use and, um, [01:19:00] uh, whatever.

[01:19:01] **ROBERT RAMEY:** And then the, uh, the C++ standard has incorporated concepts from that 20 years later, uh, to do similar stuff so that a lot of these original libraries are not so necessary anymore. He's, he's a weird character, but unfortunately, or for what, a lot of us are kind of weird each in our own way. Well, I don't know.

[01:19:21] **ROBERT RAMEY:** Uh, you know, I do know, I, I read his Boost biography, uh, how he's from Bulgaria, he makes a living. I'm not sure how, I think he was [01:19:30] involved in the development of some video game or something. Uh, he, I think he earned, um, you know, first prize in the math Olympiad or some bullshit. I don't know. But he had some, you know, credibility in that regard.

[01:19:45] **ROBERT RAMEY:** Uh, I don't know. You know, he made the, the, the shared pointer library, which at the time, uh, was very. Was like the serial, it [01:20:00] was also the, the canonical, the canonical solution to a common problem. Let me put it that way. In that sense, it's similar to the serialization library, but it did address a lot of the most difficult aspects of multi-threaded programming and, uh, which everybody had been making his own ad hoc solution.

[01:20:19] **ROBERT RAMEY:** Almost everybody was getting it wrong. And then within the Boost framework, which required documentation and now you had a place to promote it, uh, I'm pretty sure [01:20:30] that, and that as far as I can tell, his, uh, shared pointer library pretty much got accepted or included into, um, the standard library with no change at all as far as I know, or minimal change.

[01:20:43] **ROBERT RAMEY:** So that's, that's fundamental. And he also chimes in willing to chime in on any subject at any time with a view that is probably contrary to what the person who asked the question had in mind in the first place. Only on Slack and [01:21:00] emails, as far as I tell as far now, that's interesting. I heard a rumor, 'cause I got on his case for, for something.

[01:21:05] **ROBERT RAMEY:** I said, why don't you show up and, uh, talk at a conference or whatever. And, uh, then he didn't answer, but somebody said, well, his English accent is so bad, he's embarrassed about it. And you know. I just laugh my ass off on that because, uh, here's, if you, if you read the way he writes, English is perfect. Huh?

[01:21:27] **ROBERT RAMEY:** And so here, I'm thinking now [01:21:30] here would be an opportunity to subject that this guy to the ridicule that he probably deserves, but never gets. And that's, you know, I, you know, it's kind of a little, maybe it's a little window into the hmm. Personality defects of, uh, certain kinds of software developers.

[01:21:49] **ROBERT RAMEY:** It's very, in a kin, it's very similar to, uh, serialization in the sense that it, it solved a problem for which there was no good solution at the time, and solved it [01:22:00] in such a way that nobody's come up with a better solution since a Andre Alexandre, I knew him from his book Template Meta Programming and C++, I knew that this guy was then from another planet.

[01:22:14] **ROBERT RAMEY:** And I, I, I went to a couple of his talks at C++ conferences. He's a hugely entertaining speaker, and that's all I know about him. I, I know that he collaborated with David [01:22:30] Abraham's, and uh, Aleksey Gurtovoy collaborated with David Abraham's, I'm not sure. I think it was with MPL. But I might be, I might be wrong with that, about that I or 'cause because David Abraham's made some other things, like the Iterator Library.

[01:22:46] **ROBERT RAMEY:** He might have collaborated on that. I don't know. But I, I seem to recall, and you, you should probably double check this, that he collaborate. Oh, okay. So I'm, I'm right about that. Uh, MPL was, [01:23:00] I'm gonna call it the, the sun or the offspring from, uh, Andrei Alexandrescu's library of and, and put it in more of a boost framework and, and filled in the blanks.

[01:23:15] **ROBERT RAMEY:** And so I think, and I'm sure that David Abrahams would ratify this, I would hope that, uh, it was, that MPL was inspired by, uh, an, uh, Andrei's book, my nemesis. Mm-hmm. [01:23:30] That's not true. Um, my C+ bus skills when I started the serialization library were not particularly great. Um, C++, even at that time, had a lot of, uh, quirky features.

[01:23:47] **ROBERT RAMEY:** Uh, and I, I didn't know them all. And, and also quirky rules. I didn't know them all. And, uh, I would do [01:24:00] something and, um. Then David Abrahams would dispute it, knowing much more than I about the subject. And I would then also dispute his argument. And so we, and his way of handling a dispute, uh, with a person like me, um, revealed his own personality.

[01:24:27] **ROBERT RAMEY:** Weaknesses. We had issues [01:24:30] about numerical analysis. Now my background in numerical analysis is pretty good. I, uh, I, I took it at graduate level in Berkeley. I got an a plus plus in the course. The instructor was William Kahan, who is the inventor of the floating point library for C++. Uh, world renowned is the top expert in the subject.

[01:24:55] **ROBERT RAMEY:** So it's not like my background is, um, [01:25:00] know about the subject, but, uh, but David Abraham's had no problem in subjecting to me to a lecture about how ignorant I was about the subject. Well. By that time I was old enough that I didn't care, you know? And, uh, so, uh, that was fine. But, uh, and as, and actually as we spent a lot more time going back and forth on this and other subjects, uh, [01:25:30] and I do know that he did come to respect me and, uh, which was totally contrary to our initial interaction.

[01:25:39] **ROBERT RAMEY:** Our interaction improved a lot. And that was one thing, uh, he did say to somebody at one point, he considered me, he considered me his friend. I don't know where he got that. Uh, uh, one of one person wanted to extend or refine the serialization library to better [01:26:00] handle numeric data. Uh, I was very much resistant because it polluted the pristine structure that I had for the library.

[01:26:13] **ROBERT RAMEY:** And he worked closely with that guy. And since Boost is a collaborative thing, I kind of had to accept it in the re in the longer run, I came to understand that actually they were right to destroy the purity of the library for a practical end. [01:26:30] And my always, my, my problem or my motivation for working on a piece of computer code is, is artistic perfection.

[01:26:42] **ROBERT RAMEY:** And, uh, and sometimes that will, um, get in the way of actually finishing something. So, uh, anyway, uh, they were right to actually make that improvement. And the gentleman I was working with called Mattias Troyer, who is now working for Microsoft on quantum [01:27:00] computing, uh, he was doing the work. He came over to my house in Santa Barbara because he was involved with, I think, uh, in, with the University of, uh, uh, California, Santa Barbara in some way.

[01:27:15] **ROBERT RAMEY:** I forgot. And, uh, he came over and, and we spent an afternoon talking about the, the, the change he wanted to make in the library. And he did say that I, I, we had a little discussion about David Abrahams, and he did say, well, [01:27:30] you know, David, uh, the last thing he said to me, or every day this, when the question comes up about something that you've been doing or working on, uh, the last thing he said is, you know, this guy, he surprised me again.

[01:27:46] **ROBERT RAMEY:** So there have been cases where, although he might only grudgingly acknowledge or probably forgot, is that, uh, on some cases I was right and he was wrong. And Mattias came over to my house. Uh, we went, [01:28:00] we went for a hike and, uh. He looked out over the city of Santa Barbara and came back and we discussed the, some of the, um, arcane aspects of the Boost Serialization library.

[01:28:12] **ROBERT RAMEY:** He wanted to, he had some changes he wanted to make, which would make it more faster basically, and more, uh, for, uh, floating point data. And I was reluctant because I, I didn't wanna prostitute my design, you know, to destroy [01:28:30] its purity. But in the end, um, you know, he did manage to convince me and, uh, he was working closely with David Abraham's and he did mention that, uh, David Abraham said on, on one of these points while that the Ramey surprised me again, which I take to mean that his estimation of my ability was very low, but my accomplishments apparently exceeded that estimation at least once.

[01:28:56] **ROBERT RAMEY:** He's intimidating in character. And, um, it's [01:29:00] interesting, uh, yeah, some, you know, we cut him a lot of slack because, uh, he's very, very accomplished and he did grow a lot in his boost. Um, I think he became less arrogant. He became, um, more patient and, uh, easier to get along with just in the, in the time that we were together in Boost.

[01:29:24] **ROBERT RAMEY:** Uh, as I say, he grew, he grew a lot. Well, Dave Abrahams moved on, I believe, to [01:29:30] Apple Computer. And he worked on the library and Apple made up its own language, which, who now would the name of which now escapes me. Swift. Yeah. Swift, right. Uh, that was my hearing issue, not the, not you. So, uh, and he was in, in charge of, uh, building a library for it.

[01:29:50] **ROBERT RAMEY:** By this time, all languages are now have, are more carefully, uh, divided, like C++es into the, the [01:30:00] core language and the add-on libraries. And he was in charge of the library set for Swift and which of course was like a perfect match with the work he'd been doing with Boost. And, um, so I think he did a apparently very successful job with that.

[01:30:16] **ROBERT RAMEY:** And I don't know where he is working now. Um, but I, you know, he still shows up from time to time in conferences and things like that. I haven't had any interaction with him. Uh, I might after this, but, um, and [01:30:30] Doug Gregor. Uh, Doug Gregor, uh, that's another, another genius level guy. Uh, he made the original Boost system for Boost documentation.

[01:30:47] **ROBERT RAMEY:** Uh, he did a great job. I still use it today. Unfortunately, it used what was popular at the time, which was XML, which due [01:31:00] to reasons, because of its complexity and whatever, uh, has become unpopular. But it has certain features, which I still believe make it superior of to other ways of making documentation.

[01:31:12] **ROBERT RAMEY:** And he made that work. He added, he made libraries for the XML documentation set, which, uh, do things like syntax, coloring, whatever, uh, it should be used. It's not, I don't think it's, uh, um, [01:31:30] his fault, um, Doug Gregor's fault, but that's just the way things pan out. Uh, XML had some, a couple weaknesses, which, um, made it un unpalatable for, for many developers to use.

[01:31:43] **ROBERT RAMEY:** I never met Doug Gregor. Uh, I only met Andrei Alexandrescu as a, as a member of the audience in one of his lectures. Uh, David Abraham's, I met at the first, uh, boost Con, which was the, the in [01:32:00] Aspen. Uh, I remember the first time I saw him in per person. I was sitting in tourist class and tourist class on one of these commuter planes is like super cramped.

[01:32:14] **ROBERT RAMEY:** The guy is probably six and a half feet tall and he's got a neck that looks like it's about a foot long. And he's, I, and I knew it was him right away 'cause I was like about 10 rows back and that was his head sticking up [01:32:30] and that was the first time I actually saw him in the flesh. I didn't approach him 'cause I knew I'd be running with him into him eventually.

[01:32:37] **ROBERT RAMEY:** And I didn't want to get, I didn't wanna start that now, you know. Well, I dunno if it was the first one. I probably was the first one. I don't remember. Um, I always go to, I never go to conference unless I'm speaking 'cause I don't like to pay the fee and I don't know what I was speaking about. Um, but the, the Boost Conference, uh, I really [01:33:00] loved, I'm not a really a great fan of meetings and conferences too, so much.

[01:33:06] **ROBERT RAMEY:** But anyway, uh, you fly to Boulder and you're not, well, it was Boost and uh, that was, that made it special. And then I would get a chance to meet the people that we've been talking about in court of, uh, rub elbows with a peer, with a group of peer people that I would like to consider my peers. And, um, so [01:33:30] I flew to Aspen and, uh, they have this conference in the.

[01:33:35] **ROBERT RAMEY:** At the, in the, the lodging, uh, they, they have this Aspen something or other center, and they have a lot of physics conference there. It's got mid-century modern architecture, and then it's got a bunch of sculptures sitting around. Aspen itself is a, got beautiful views. It's filled with billionaires houses.

[01:33:57] **ROBERT RAMEY:** Uh, it's really a pretty [01:34:00] cool vacation. And, um, the, and then the conferences, as I say, you get to interact in and out of conferences with, um, people you like to consider your peers. And, uh, things like the future direction of C++ and the future direction of boost, uh, our topics for conversation, which were interesting to me.

[01:34:23] **ROBERT RAMEY:** And for all those reasons, I, I've been to the conference a couple times and, uh, [01:34:30] that's pretty much that. No, it's, I, well it, you know, I guess the first conference was realized what, 2006 or something like that. And so Boost was the thing and it interacted speakers like Bjarne Stroustrup group I'm sure spoke there and, you know, we all spoke there and, um, except of course Peter Dimov.

[01:34:54] **ROBERT RAMEY:** And, um, the, and then 2011 came along [01:35:00] when. I'm gonna guess 70% of Boost got incorporated into the standard and then Boost as I'm, I I lost its way. The question is, once you've accomplished what you set out to do, what do you do? And since then, uh, as we've talked before, it's been kind of swirling around looking for its next big purpose.

[01:35:24] **ROBERT RAMEY:** Meanwhile, the conference and the foundation have continued on, [01:35:30] uh, without that defining purpose. And Vinny has stepped in. The Boost Foundation was run by a board of directors who were outta their depth and, uh, didn't really know, got involved in, I, I think, canceling people or political correctness or whatever.

[01:35:52] **ROBERT RAMEY:** And, uh, Vinnie stepped in and wrestled and, uh, Beman died. And so, uh, the, [01:36:00] the, the, the, the Boost Foundation was pretty much rudderless and Vinnie stepped in and wrestled control of it. And here we are. Uh, I've been unhappy with the Boost building process for many years. Uh, and Boost developed its own software package for, um, building the libraries, for translating the source code of the library into computer code.

[01:36:27] **ROBERT RAMEY:** And that system is called Boost [01:36:30] Build, Boost B2 , I think it was the brainchild of Dave Abrahams and he got Vladimir Pruss on board and they invented, they took a, a, a previously used scripting language, I think called Perforce and adapted it to, to build this software. At the time there were alternatives like SCONs and some other, none of them were super satisfactory.

[01:36:56] **ROBERT RAMEY:** There was Make, and there's Ninja, there's a lot of stuff like that. [01:37:00] Um, um, so, um, it, they were always kind of a hack and uh, so I was unhappy with those as were a lot of people. And, um, the thing was in turmoil, um, CMake was another build system came along also quite a bit of a hack, but less a better hack than other hacks.

[01:37:25] **ROBERT RAMEY:** And, and they continued to improve it to the point where it's now [01:37:30] sort of the standard as far as building library is concerned. But anyway, I wanted to, I had ideas about how I felt Boost should be improved. And of course I'm always happy to expound on these ideas. And the ideas almost always are not popular.

[01:37:53] **ROBERT RAMEY:** Yeah, I think it's because they represent a change of maybe, yeah. Uh, [01:38:00] people are, once something becomes established, the re there's a, a, a huge resistance to even the smallest change. And we've touched upon that before. When an organization gets too big and requires too much consensus, it's very hard to make any changes.

[01:38:16] **ROBERT RAMEY:** And that's of course why they end up in the cul-de-sac where many of them do. It's still not done. It's never gonna have done because the, the enthusiasts of boost build are hanging in there doing everything they can to keep the [01:38:30] transition from sea make to sea make from happening. And, um, they've been pretty successful at it.

[01:38:36] **ROBERT RAMEY:** Uh, they're nobody. So my, uh, alternative, I said, well, I was happy. I think the boost process could be improved. And the way I'm gonna do it is I'm gonna make a, a website which illustrates, which helps with the review process. Uh, the problem I, I saw with the review processes is if you cram the, the, I wanted people to be able to submit a Boost [01:39:00] library and get feedback on it before the review so they wouldn't have to do what I did, which is to suffer.

[01:39:09] **ROBERT RAMEY:** All that goes with making something that's not up to snuff and have it rejected and then go back and try and do it again. So. This would provide a place where, which would provide guidance, help and examples and a place where people could post their library and people could use it [01:39:30] provisionally or people could use it even though it's not part of Boost and they could give feedback.

[01:39:35] **ROBERT RAMEY:** And so a lot of the, so that, that when something finally did go to review, it would be, uh, the review process would be much more productive and the person who's making a library would get help before the review instead of having to deal with it afterwards. The other thing that it would do, it would let you post a review.

[01:39:58] **ROBERT RAMEY:** If I pick out a library, I'm [01:40:00] gonna use it. Well, oh, and I like it. I could post a review right now without waiting for the particular formal review period. Because if you've select a particular two week period, it has the advantage of everybody come in at the same time. But a lot of times they might be working on a project or they might be on a trip, uh, maybe they can't participate.

[01:40:20] **ROBERT RAMEY:** So I would, I hoped that when somebody posted their library to the Boost Library Incubator, then they would get [01:40:30] feedback on it immediately be way before the review period, and that people who wanted to post a review could do it without waiting for the, uh, review period. And so I called it the Boost Library Incubator.

[01:40:43] **ROBERT RAMEY:** And I made the, the URL, theblinkabator dot com and, uh, I implemented it and it had, and it did get a number of submissions. And, uh, since it was much easier to submit to than to boost, [01:41:00] because, you know, you didn't have the reviews or whatever, uh, the large portion of those things were submitted was some guy's piece of code, which he thought was cool, but it really wasn't up to the standard of a Boost library, which is okay.

[01:41:13] **ROBERT RAMEY:** Gave people an outlet. And of course, the feedback they would get is, well, people didn't use it much. And, you know, so it would shortcut the whole process in case of failure. And if your idea wasn't really, didn't get much traction, well at least you didn't get any public [01:41:30] humiliation. And so in that sense, it was kind of successful.

[01:41:34] **ROBERT RAMEY:** On the other hand, I, I making a website of that complexity, uh, required using some help. I used WordPress and which was the, the, and still 50% of the world's websites were made with WordPress. It had all the facilities. It, it had a lot of people had crafted add-on libraries, which were useful. So it really had the [01:42:00] ability, uh, to do what I wanted to do.

[01:42:03] **ROBERT RAMEY:** But after working with C++ and trying to make, and making this work, the level of. Effort and maintenance that would be required, I felt was really more than I wanted to dedicate. So I, I let it, I, I, I let it, I cast it aside. And also I didn't like paying whatever is a couple hundred bucks a year for the, uh, URL, which in fact, now I wasn't gonna use.

[01:42:28] **ROBERT RAMEY:** So I just let the whole thing [01:42:30] die. Nobody seems to have really missed it. Um, although some people have asked me to resurrect it, and actually I've tried, but then dealing with WordPress is like even worse than C++. But any case, uh, so that's where that stands today. I think it's still, uh, if somebody really wanted to take it and with run with it, um, it would, uh, I think it would be, uh, interesting.

[01:42:53] **ROBERT RAMEY:** It did incorporate my ideas for the way that we should alter Boost, [01:43:00] evolve, boost so that the, it's better built and better, uh, distributed. But, uh, that was my own motivation. But I think Alliance probably has this exact same idea, but as I've noted before, whenever it comes down to any specific details, uh, Vinnie and I never agree.

[01:43:21] **RAY NOWOSIELSKI:** I mean, you said "delusional" earlier. 

[01:43:24] **ROBERT RAMEY:** Well, I'll, yeah, I'll stand by that. Well, you'd have to see the, you'd have to see the quote, but [01:43:30] I, I, and also, um, Vinnie's Vision is aspirational and I'm not really sure what it is. And then there's, um, money being invested. I can't help but think that there's hope that at some point this, um, generates some sort of return on investment.

[01:43:47] **ROBERT RAMEY:** And I just don't, I just don't see things coming together for that to happen. He might disagree with that. I don't know. Uh, he talks in terms of, I'm not sure. But anyway, he did talk about once he [01:44:00] articulated a, a fu a future for the vision of Boost, and I thought that it just wasn't in accordance with my reality.

[01:44:09] **ROBERT RAMEY:** And so I used the word delusional and I don't remember what I said and I don't remember what he said, but IN but I never felt the word was ill chosen. Do you know Rene Rivera? Oh, oh yeah. No, I met him at conferences. Uh, very nice guy. And he's the main supporter and promoter of, uh, the Boost Build system, which is now [01:44:30] called Boost B2.

[01:44:31] **ROBERT RAMEY:** Yeah, I, well, it's, I think Rene is, would probably be the main person. I, I, I, and I think that, um, this another things I could spitball and nitpick and whatever, but I think the real thing would be, uh, I think that, uh, I mean Rene is an enthusiast. He, he, he, he, he's very capable. Um, I, [01:45:00] but I think that he should think of that or manage that not as a boost thing, but as a separate project, which is promoted independently as a competitor to CMake or something like that.

[01:45:13] **ROBERT RAMEY:** And then Boost would, it wouldn't be a Boost project. Boost would be an example of its use. And that would kind of shift the focus to where I think it should be. It's a tool that Rene is, uh, evolving [01:45:30] and, uh, he believes in it. Uh, I think that's fine, but it should be promoted as a general purpose tool and not as a Boost thing.

[01:45:39] **ROBERT RAMEY:** He would probably say that, well, that's what I'm doing. I would say you're not, but the thing is, it's, it Boost is, as far as I know, the only organization that uses it. And I think it's not, um, it's just not developed to the, to the point in the way that it's [01:46:00] more useful to the general public. Ha, I, you know, I don't, I frankly, I don't know much about networking to tell you the truth, but, uh, I, I will mention one thing that as long as I've been in Boost, uh, you know, count the years, uh, the network, a networking library has been a topic of discussion of the standards committee.

[01:46:26] **ROBERT RAMEY:** But they've never been able to get it together. [01:46:30] Uh, nobody apparently has proposed one that has enough consensus to, for it to be accepted. So I guess the best thing is have no library at all, which is we have now there, the Asio library was a strong contender, but apparently it's not particularly a, and I'm not familiar with that, but it's apparently not that easy to use.

[01:46:56] **ROBERT RAMEY:** And, uh, some people it's the most [01:47:00] strongest contender, but still, apparently not everybody's on board. So then I, and you know, anybody who listens to this is free to, uh, correct me. Uh, the standards committee itself under has undergone its own effort to make senders and receivers and promote that. Um, but I don't, as far as I know, it hasn't taken off.

[01:47:27] **ROBERT RAMEY:** That's another saga of different nature. [01:47:30] But, uh, the networking library, uh, remember when I told you what got me into boost was the, the shared pointer, or excuse me, the a, um, threaded, uh, multi-threaded library, right? And a networking library would be on that order of utility. Apparently it's an even harder problem to solve.

[01:47:50] **ROBERT RAMEY:** The, the, the problem to be solved is making something that's generally useful, but solves the problems that occur when you're writing a program and [01:48:00] using networking. Those two goals, conflict. And this is why that there wasn't the serialization library, there wasn't one around when, when I, when I made it, because on one hand you have an abstract problem, on the other hand, you're working with real equipment and you, if you try and meld them, you end up with something that's really a mess if you, and the trick is to find a way to, to address both of those issues without [01:48:30] turning into something that's so complicated.

[01:48:31] **ROBERT RAMEY:** No one can understand. Networking is worse than serialization as far as that's concerned, trying to solve that conundrum. So, uh, and the funny thing is, and great thing is that the consensus process, since they can't re they can, they can't come to consensus. We're not stuck, stuck with something that doesn't work.

[01:48:52] **ROBERT RAMEY:** So, although I criticize the whole concept of consensus, it does act as a break against really bad ideas. [01:49:00] Wow. Well, I laugh because 20 years people have been talking about it and 20 years as far as I'm concerned, there's zero progress. Um. Vinnie came on, he started out as the developer of Beast, which is a library which addresses, uh, one aspect of networking, which I, I believe is, um, URL Syntax or something like that.

[01:49:29] **ROBERT RAMEY:** Um, um, [01:49:30] first of all, I'm, I'm not familiar with the domain, but apparently, um, he struck a nerve and it solved a problem for a lot of people. Uh, it was a little bit out of the normal library thing in that it wasn't so abstract, it was more on the practical side, whereas something like MPL is like, as I say, you're kind of like from outer space, but that's kind of makes sense because it would make [01:50:00] sense that when the, the more fundamental abstract problems are solved, that we would kind of gravitate towards things that are a little bit more down to earth and maybe a little more narrow.

[01:50:11] **ROBERT RAMEY:** Fine and dandy. I was very put off by the name Beast because I always wanted libraries whose names were descriptive, um, to me to make a name that's. Like beast and there's a couple others. It's very egocentric. And um, [01:50:30] so it's kind of like branding, you know, which is off-putting to me. Uh, I like the idea of something is so fundamentally obvious, good idea that it takes off on its own.

[01:50:41] **ROBERT RAMEY:** That's maybe naive and probably is, but anyway, so, exactly, so, and Vinnie, the way he promoted his library was far, far more extensive than anybody has ever promoted their library. My view on that, I did, I didn't even find that distasteful. [01:51:00] I said, Hey, it's a thing. Doesn't hurt. See how it goes. And apparently it's gone well.

[01:51:06] **ROBERT RAMEY:** So that's fine. So I, of course, I met Vinnie in one conference or another, and, uh, he did say that, uh, one of the talks I made, he was inspiring to me or maybe he said it over a slack or something. Um, which of course I liked. And Vinnie, it's very funny, uh, and I never thought of this just as I mentioned that, that physically David [01:51:30] Abraham's is kind of an outside out, outsized per person, you know, and his, his size and his, his geometry and Vinnie himself is like just a gigantic character.

[01:51:45] **ROBERT RAMEY:** I mean, his, his physicality matches his character. So he's unforgettable in that regard. And I'm, of course, I'm sure I'm, I, I'm not telling you anything new here, but I, I walked up and the guy, I, I, I don't [01:52:00] know what I said, but Jesus Christ, man, you are goddamn big. What's up with that? I mean, that's not what I said, but I didn't say too far off from that.

[01:52:11] **ROBERT RAMEY:** He says, well, yeah, I used to be sort of a physical fitness thing, but this isn't fitness. The guy is giant. I must weigh 250 pounds. So I just can't picture this guy hunched over a computer like the rest of us. And then he, he, we, at this conference, I [01:52:30] forget what it was at, it was in Seattle, I believe, and we were all this bus do boost developers got a free dinner.

[01:52:38] **ROBERT RAMEY:** And, um, then, and he con he sponsored free drink tickets for everybody in the room. I mean, this is an outsized thing. So, uh, I, and I, and I stood up and made some sort of reference to that or something similar. Which wasn't particularly well received, I don't think Vinnie [01:53:00] minded did, but I, I think it was, felt as a little bit outta place.

[01:53:03] **ROBERT RAMEY:** Uh, it was pretty funny because Vinnie later said, I thought it was pretty, is, you know, software developers don't seem to drink too much. So anyway, uh, that's Vinnie is the master of the grand gesture. And, um, if you, I, I, I don't know the details, but I know if you look in his hi history, it, it's ratified by that.

[01:53:26] **ROBERT RAMEY:** And, you know, that's, that's the trip we're on, uh, [01:53:30] right now. Uh, we'll see how it goes. I didn't have any real objection to what I call a change in direction because I felt that we were rudderless, but whether this is the right one or no, it remains to be seen. We'll have to see, you know, I wish him well. I disagree with him about a lot of stuff, but hey, you know, um, it's a free country still, you know, and he can take a shot and he's doing it.

[01:53:59] **ROBERT RAMEY:** And I [01:54:00] say, um, more power to you. You know, I, I, I never got that sense though. It wouldn't surprise me if people felt that way. Um, I'm sure all of us, somebody, somebody has felt that way about all of us one way or the other. Yeah. You know, so, uh, you know, if you, if you don't have a thick skin, you shouldn't be in this business probably.

[01:54:22] **ROBERT RAMEY:** Uh, but you know, if you start. If, if that stuff starts to bother you, you're, it's really gonna be [01:54:30] inhibit your success, uh, your accomplishment. You know, you just have to accept the fact that, uh, not everybody's gonna be on board. And, and two, uh, sometimes they're right, maybe usually not. And sometimes they're gonna express themselves in a way, they just come from a place of um, lack of humility because they don't know enough.

[01:54:50] **ROBERT RAMEY:** You know, that's the world we live in. So, uh, this doesn't bother me. It doesn't bother Vinnie. It doesn't bother David Abraham. It doesn't bother any of us. 'cause we all think we're super smart. Just start [01:55:00] using Boost libraries and, uh, reading about them and just start working at it. That's what I did, actually, that's the question I really wanted to answer.

[01:55:10] **ROBERT RAMEY:** Great. I forgot what it was, but I do remember wanting to answer it. Uh,

[01:55:16] **ROBERT RAMEY:** and by the way, licensing, I, well actually I do only have a little bit to say about that, but it's probably, it. You'll probably like it anyway. Wake, it's, uh, it's C++, it's, it's a, it's almost inconceivable that [01:55:30] that's gonna be the basis of some popular topic, but you know, that's where you guys make the magic, you know, turn something that's absolutely incredibly dull into something that's interesting.

[01:55:41] **ROBERT RAMEY:** Well, if you can turn this into something that's more than the narrowest niche, I'll be impressed. The really interesting question. Really is a different one in that what is future software development gonna look like? And, um, I started out in the era [01:56:00] where all software development was proprietary and financed by big companies, and they kept it proprietary to make their investment.

[01:56:09] **ROBERT RAMEY:** And this was the way everything was done. And then, uh, that sh and then we moved to an area where a lot of stuff was open source, which, you know, between Linux and Boost and the standard C++ standard and other stuff, uh, that pretty much made Proprie a lot of pro [01:56:30] proprietary software efforts.

[01:56:31] **ROBERT RAMEY:** Irrelevant. And of course now we're into AI generated code. Very, uh, it's inconceivable to me that it's a thing, but you know, the truth is that those of us in Boost, myself included, we're all dinosaurs. Uh, it's an epic, like this is not gonna really repeat itself in the same way if young people, um, I'm also, I'm [01:57:00] astounded sometimes at their lack of depth and their lack of knowledge of any kind of history.

[01:57:06] **ROBERT RAMEY:** But you know, I've said I'm gonna be 78 next month. This is pretty common for people, my generation. Or my age, I, I should say. So I, I, I, I don't know what, what worlds are gonna have to conquer, but I don't think it's gonna be these worlds now. So that's what I have to say about that. I, I wonder how young people are gonna respond to that comment.

[01:57:28] **ROBERT RAMEY:** Oh, to me, that's the central [01:57:30] aspect of the story. That's where we got a big problem. And some smart guys come up with a solution, and through incredible effort, they managed to convince a lot of other people and make a huge accomplishment, which is C++ in its libraries, starting from almost nothing.

[01:57:49] **ROBERT RAMEY:** Um, trumping all the efforts of all the large established players and making them pretty much obsolete and creating a whole new [01:58:00] world. And that, that's just the recent, most recent or incarnation of this same phenomenon, which happens again and again. Who the, uh, I don't know who it was, it Galileo or Copernicus or whatever, who, who stated that the, the, um, planets revolve around the sun rather than the other way around.

[01:58:21] **ROBERT RAMEY:** It took a hundred years for, for people to finally buy that concept. Now we've shortened it down to [01:58:30] 20. And uh, that's the way when we look at the world and see how it progresses, that's the way it progresses. Thomas Edison invents the light bulb, and I don't know how long it took him. Well, he had to make a hundred copies.

[01:58:45] **ROBERT RAMEY:** And it's people like this and people who can understand people like this and people can see how the world actually really works that make the world what it is today. Henry Ford starts out people, [01:59:00] automobiles were handcrafted like watches at the time. Everyone was unique. You to get one fixed, you had to have parts made.

[01:59:07] **ROBERT RAMEY:** And he invented a system whereby even morons could make an automobile. And everybody drives it. And there's still morons. But the way that life is, the way that things change are people making these kind of efforts, which were seen as ridiculous at the time. [01:59:30] And when we look around and we look at things like particle physics, 50 years, almost no progress.

[01:59:37] **ROBERT RAMEY:** It's missing the next Einstein. He doesn't come along frequently enough. And when we look at the world, we should step back and think how. How special the contributions of individual people are and, and, uh, appreciate that that's the way human genius is. And, and we should, we should river it [02:00:00] more. And even people on the second tire who are not famous, make inventions in progress every day.

[02:00:07] **ROBERT RAMEY:** Some guy coding, um, coding, um, the zip format and the code to do it. We use it every day. Do you know his name? I mean, this guy and this guy is a smart guy. We and everybody in every walk of life is making those kind of contributions and we totally take 'em for granted. That's what I think should be [02:00:30] taken from this.

[02:00:30] **ROBERT RAMEY:** This is C++ a weird language for describing some sort of quasi mathematical thing designed by first rate, third rate mathematicians, which end up being something that drives the whole world in a place that nobody imagined. This is the thing that one should take from all this. Okay. I, I'm gonna step back and answer a totally different question here.

[02:00:55] **ROBERT RAMEY:** You know, just give you a little short history. First of all, the whole computer world [02:01:00] is built on stolen code. And just look up Steve Jobs, for example. He started his whole introduction to computers was, uh. Stealing time from the phone company to make long distance calls. His, he's quoted saying, whenever possible, steal code.

[02:01:20] **ROBERT RAMEY:** Uh, if I get, if, if, if somebody makes a serialization library, they're gonna look at the Boost serialization library and steal what they can [02:01:30] from it, and then think they made it. And they, and they will have, because where did I get it? I basically got it from looking at, um, the Microsoft, uh, foundation classes.

[02:01:43] **ROBERT RAMEY:** I, I saw it, I saw it was right, but it was incomplete and it left, uh, wide gaps. I said, well, that's the on the right path. I'm gonna make it better. I never actually, well, I am now, but I, I don't know. I haven't maybe often [02:02:00] enough not given credit to that, but that's the way stuff gets built in the late nineties.

[02:02:06] **ROBERT RAMEY:** Uh, and then of course, software started to become valuable and in the late nineties they had this dispute. Is software and invention subject to patents? And there are patents on software, or is software subject to copyright like a movie script? Quite a difference. Patents have a 17 year life. Uh, [02:02:30] copyrights had, uh.

[02:02:33] **ROBERT RAMEY:** The lifetime of the author, I think, until Disney got involved. And they say, oh yeah, no, we need extra time. So they got an extra 50 years on Pinocchio and Snow White on that stuff. I mean, how should I say? That's how lobbying works. But anyway, the, um, the software, uh, copyrights are, are specific work of art, like literature and inventions or something that, that you [02:03:00] reuse.

[02:03:00] **ROBERT RAMEY:** And software didn't really quite fit in either one. The industry eventually went for patents because they saw it as I, I think, a better commercial model. But it's kind of still left us in this limbo where, uh, it's pretty easy to find a, a piece of software that does sort of what you want to do and use it as a guide and write your own code.

[02:03:22] **ROBERT RAMEY:** And so now you've got, um, you've got, uh,[02:03:30] 

[02:03:31] **ROBERT RAMEY:** Jane Austen writing a novel and now you got a movie clueless. How much did Jane Austen get out of that? Uh, you know, it's, this whole concept of intellectual property is fascinating. It's been fundamental to the development of Western commercial and science for the last 200 years. It's kind. Tucked into a cul-de-sac and it actually deserves more investigation.

[02:03:58] **ROBERT RAMEY:** Look at the [02:04:00] development of music in the 20th century. Once, once, um, music moved from sheet music into recorded music, and then you had things like jazz and all. We had a whole American mo, uh, uh, movie, uh, movie music and jazz, and a whole bunch of music. And, and lo and behold, not only is it a new genre, turned into a huge moneymaking exercise, which really stoked it like crazy.

[02:04:29] **ROBERT RAMEY:** And of course, [02:04:30] like when everything gets really super developed, it degenerates into something like rap music. So any case that's, that's my thought on software licenses, the whole thing is like way overdone. The lawyers get involved so they can think they can save money, but it's a peripheral issue by the, they, by, they designed the boost software license, which was to basically leave the copyright in the name of the author, but the [02:05:00] author would be required to, uh, accept the Boost, uh, software license would, which permits anyone to use the software for any purpose whatsoever.

[02:05:11] **ROBERT RAMEY:** You can't steal it because you already have access to it. And then they came along with the MIT license, which is just a variation of that as far as I can deal. And then there's other license with more complexity as people try to, you know, uh, use it to, um, [02:05:30] maintain a certain exclusivity. Like, you know, you can, you can use it, it on a trial basis, but if you sell it, you have to pay something or whatever.

[02:05:38] **ROBERT RAMEY:** Those generally, I don't think have gone particularly far, but the Boost software license said, Hey, you know, we're changing the world here. Here it is. It's, it's, it's, it's Michelangelo. You're free to photograph.

