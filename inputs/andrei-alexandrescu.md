# BOOST_ANDREI_ALEXANDRESCU_STRINGOUT_v01

- - - -
filmed Date: 2025-11-04  
location: Kona, HI  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1140472167/a535cc6743?fl=pl&fe=sh  
summary: Excellent on history of Boost, personal w Beman, origins of Smart Pointers  
- - - - 

## Transcript Start

[00:00:00] **RAY NOWOSIELSKI:** Okay.

[00:00:05] **RAY NOWOSIELSKI:** This thing, can I have my bottle of water too? Yes. Did you want that one? Yeah. Here it is. Yeah. You got it. I, I got, thank you very much. Okay. This is great. I really appreciate 

[00:00:18] **ANDREI ALEXANDRESCU:** you. Hmm, thanks. It's fun for me. I mean, I like, uh, yapping. My name is Andre Alexandre Ku, my friends called me Andre, in the words of Baba from Saving Private Ryan.[00:00:30] 

[00:00:30] **ANDREI ALEXANDRESCU:** Um, and, um, I'm a computer scientist and I've been involved with Boost in the early days and with C++ for a long time. So, um, let me, uh, lemme bring a story that's, uh, popular and kind of dear to me as a, as a longtime, uh, computer, both user and, um, you know, and programmer, um, when Steve Jobs introduced.

[00:00:53] **ANDREI ALEXANDRESCU:** Um, the iPod, uh, way background, right? So, you know, he had a very interesting thing he said. He didn't, he [00:01:00] didn't say it has this many megabytes of memory, this, you know, this, these like technical specific, he said, he said, uh, 5,000 songs in your pocket, right? He said, he said actually something that mattered to the end user.

[00:01:13] **ANDREI ALEXANDRESCU:** He didn't say like, you know, and that was very, uh, it was a very common for windows like Microsoft to, to come with, oh, we have these megahertz and these Giger, whatever, and these, uh, you know, parameters. And he said, you know, he showed, you know, we have 5,000 songs in your pocket. And I, I thought that was a [00:01:30] very compelling argument because it, it tells you the power of technology, but in a, in a, in terms that people care about.

[00:01:37] **ANDREI ALEXANDRESCU:** And that was amazing. And the same, uh, the same deal with Steve Jobs and the, the, um, the, the thin, uh, air laptop, right? The, uh, what do you call that? The apple? Apple air. The air, yeah. And he pulled it out of a, of a manila envelope. Right. He pulled it like just like that and the fact that it would fit there and it was kind of, you know, difficult to imagine that something like that would [00:02:00] come out of that envelope.

[00:02:01] **ANDREI ALEXANDRESCU:** Uh, it was amazing. So it was a very practical is here's what what we did with technology. It's not the gigabytes and the gigahertz and the whatever. It's, uh, the usefulness to people. There's a lot of personal, um, uh, kind of feelings involved. Like people, people have a very interesting relationship with language.

[00:02:19] **ANDREI ALEXANDRESCU:** And the same goes about natural language. I'm, I'm sure you love and hate English. Um, you know, and any, any person, whoever uses a language, uh, has a relationship with that [00:02:30] language. Uh, and the same goes for, similar, goes for programming languages and people fall in love with them. There's a lot of, you know, politics, involvement, um, nonsense if you wish, fights, uh, you know, what have you.

[00:02:42] **ANDREI ALEXANDRESCU:** About, uh, about language. Um, because language is what is, is part of us. It's very, it's a very important part of, uh, of, of one's life. 

[00:02:51] **RAY NOWOSIELSKI:** Love and fighting often go together. We fight the 

[00:02:53] **ANDREI ALEXANDRESCU:** heart. Absolutely. Yeah. It means you care, right? Yeah. Um, so I, I have no doubt that, uh, there's a lot of, [00:03:00] um, uh, subjective feeling involved in people caring about one language or another.

[00:03:05] **ANDREI ALEXANDRESCU:** But I agree that for a user it shouldn't matter that, you know, oh, actually this laptop was written in, uh, whatever. And it's like, whoa. So what? Does it make a more interesting laptop necessarily? I mean, no, let's, uh, use it and see what, what can do, right? Yeah. People shouldn't care. They should care about the end results.

[00:03:22] **ANDREI ALEXANDRESCU:** Uh, what does matter to them is, um, my programs run well. They don't crash and they're fast. [00:03:30] So I think to the extent that any language would provide a good mix of these three people are gonna be happy, right. I think, uh, for better or worse, uh, C++ is what civilization runs on. Uh, without even knowing any of us is using C++ several times a day.

[00:03:52] **ANDREI ALEXANDRESCU:** Uh, maybe in the elevator, which has a controller someplace that optimizes the traffic of elevators, maybe in the [00:04:00] airplane that you, you know, you and I use to, to fly, uh, here, uh, to Hawaii. Um, maybe, um, uh, in the, you know, the browser you use on your computer, you know, operating is everything. You, everything electronic that is, uh, even remotely, uh, sophisticated, it's going to have C++ in it.

[00:04:18] **ANDREI ALEXANDRESCU:** Uh, and that's, that's a reality. And, you know, C+ is the backend of many things. Um, AI runs on C++. I mean, you know, essentially if, if AI ever becomes our [00:04:30] overload, you could absolutely say that C++ has won over, over humanity, over humankind. Um. Uh, the, the, the interesting tidbit about, uh, about C++ is that, um, you, it's kind of like, um, it's like dark matter.

[00:04:44] **ANDREI ALEXANDRESCU:** It's kind of in the background. Because, for example, when I talk to somebody, oh, well, ai, what do you use for ai? You know, I'm using Python and PyTorch and these kind of Python language environments. But, uh, what happens in reality is everything Python that does anything [00:05:00] interesting is going to call into some C++ libraries.

[00:05:04] **ANDREI ALEXANDRESCU:** It's going to go down to C++. C+ does the rummaging, the difficult part, and returns to Python, a simple result. And Python says, Tara, right? So here's a result. But, uh, really all the heavy lifting is done in C++. There's absolutely no con, uh, there's absolutely no contest for that. Let me lay on the table as, as things are, um, first of all, so I work at Nvidia in the, in the, in the business I'm in.

[00:05:29] **ANDREI ALEXANDRESCU:** Um, [00:05:30] 10% of, uh, faster means a lot. 10% faster means instead of, uh. You're spending $10 million on electricity on some task, you spend 9 million. So you save 1 million, right? Uh, 10% means instead of waiting for 10 minutes, you wait nine minutes or 10 seconds, you know, et cetera. So it, it means a lot because it's 10% that is always gonna be there, and essentially everything you start from then on, it's gonna be 10% faster so you can actually compound these.

[00:05:59] **ANDREI ALEXANDRESCU:** [00:06:00] Um, and C++ is, uh, unique in that way because it, uh, allows you absolute freedom for reaching the best. Uh, the, the best, uh, speed there is, I'm talking about very low level of safety, like the system crashes and that kind of stuff. So other languages are safer in that sense. So, you know, they, they don't have bugs as as many as, uh, as a typical C+ program, but at the same time, C+ is the absolute winner with, uh, with regard to speed.

[00:06:28] **ANDREI ALEXANDRESCU:** And it turns out that [00:06:30] speed for these modern AI systems is absolutely paramount. 

[00:06:34] **RAY NOWOSIELSKI:** So I've been asking these, uh, two kindergarten questions of almost everyone, and sometimes people have an interesting answer, sometimes they don't. But if you'll bear with me, um, is there a word or a phrase that comes to your mind when I say boost 

[00:06:47] **ANDREI ALEXANDRESCU:** a phrase over?

[00:06:48] **ANDREI ALEXANDRESCU:** Uh, yeah, there is. Um, it is, um, I would say the heyday of C++. This is it. This is the phrase that comes to mind, the hey of C++. [00:07:00] 

[00:07:00] **RAY NOWOSIELSKI:** Alright. Now, is there a word or phrase that comes to your mind when I say 

[00:07:03] **ANDREI ALEXANDRESCU:** WG 21? Um, boring standardization committee stuff. Yeah. Yeah. So Boost was more, much more fun than WG 21.

[00:07:14] **RAY NOWOSIELSKI:** So let's get into that. As a great storyteller, we are making a movie about Boost. Um, if you were in our shoes and you were making that movie, what story would you tell and. 

[00:07:25] **ANDREI ALEXANDRESCU:** Would you tell it? Ah, okay. So, uh, you, you want me to do your homework? Huh? Do my job. [00:07:30] Job. Alright. Um, if I were to make a documentary of about Boost, I think I would focus on its number one, it's, um, enthusiastic beginnings, uh, because there's a lot of, there's a lot of interesting stuff about that.

[00:07:49] **ANDREI ALEXANDRESCU:** So, the enthusiastic beginnings, the scrappy starts, the, um, the, the, the level [00:08:00] of the qu the, the bootcamp, the Elite Bootcamp, um, atmosphere that it soon created, it created a, an elite core, uh, kind of, um, morale and style of doing things, um, which was very interesting and. It became very quickly the, the thing that everybody aspired to do, even though, and this is, this is [00:08:30] weird.

[00:08:30] **ANDREI ALEXANDRESCU:** Nobody was getting, getting paid for it. People were not getting paid to contribute to Boost, yet they would have given, you know, a, a kidney to be, to be a, have a Boost library in there. Um, and so that's the second thing that, um, I would stress in, in the documentary. The third would be Boost became the conduit to standardization.

[00:08:52] **ANDREI ALEXANDRESCU:** Hmm. So it became, because it, it was such a high quality and such an imposing, um, such an [00:09:00] imposing, uh, milieu, uh, community. It became the, the path to standardization for somebody who wanted to, to get something in, into the standard library. So these three, I think are the key, uh, aspects of Boost and the most interesting.

[00:09:15] **RAY NOWOSIELSKI:** Love it. And there is an open question as to whether it was the, the formula of boost. That's the thing that can kind of keep being replicated and still make boost very relevant to this day, or whether it was these particular set of people who showed up [00:09:30] when that formula presented itself. What do you, what do you think?

[00:09:32] **ANDREI ALEXANDRESCU:** I think it's, um, very difficult to tell. I think it's, uh, as, as usual, it's a combination of the two, right? Because you could have the formula but not the right people to push it. Or you have the right people, but they don't have a vision, right? Um, I think it was a, can be a mix of the two. Um, and also of the weather of the times.

[00:09:50] **ANDREI ALEXANDRESCU:** Um, as it were back then, as I told you, the heavy days of C+ were just then and there. And, um, there, there was such a palpable [00:10:00] enthusiasm for, for everything, C++ and, uh, C+ the language, uh, had so powerful technology for the time. So it was 1997 C+ had templates and these like, uh, exceptions and all of these mechanisms to do great things and they were for a few years, which is very interesting for a few years out there, let's say from 97 through 2001 or something, uh, there, there are a couple of years in which people are like, wait a second, C+ is such a powerful [00:10:30] language.

[00:10:30] **ANDREI ALEXANDRESCU:** And everybody says how great it is, but there's no evidence of that. There's no incarnation of that promise. Right. Like, I dunno, like crypto is today, whatever, you know, you could compare with any number of things. Even ai, maybe some people still think that AI is not, um, is not giving results and that kind of stuff.

[00:10:53] **ANDREI ALEXANDRESCU:** So back then it was like, well, Cipro has all of this, uh, these cool ideas in it. Uh, it needed to put up a shut up that, right, [00:11:00] exactly. So it was like, uh, and yeah, so where's the evidence? And one piece of evidence definitely was boost. One piece of evidence was definitely boost. Um, another piece of evidence is, was the standard template library.

[00:11:12] **ANDREI ALEXANDRESCU:** The, the, uh, Alexander Stepan of, um, Magnum Opus, uh, which was abs it was like a, a kind of, um, a, an apparition. It was a revolution. It was like when everybody saw, it was like, oh, okay, so. God does exist. You know, it was kind of that kind of [00:11:30] stuff. It was like just a miracle. Uh, and Boost was not, not the, not the same, but it was a, a, a good second.

[00:11:38] **ANDREI ALEXANDRESCU:** Um, and, uh, it was the times a lot of enthusiastic people who were again, were willing to put, do the work of their lives for no money, right? Willing to do the work of their lives for no money. And, uh, all of this, uh, ESP pretty core and all of this, uh, high standard of quality and all of this exacting like, [00:12:00] uh, attention to detail and everything.

[00:12:01] **ANDREI ALEXANDRESCU:** So if you got the library into Boost, it was a rite of passage. Um, people were very, very excited about Boost. So the SDL was, um, absolutely, uh, proofing the pudding. That civil process was a great language. Um, back then, um, a variety of languages had the variety of ideas. But computers were slow enough that if you, a language would lose speed by I implementing those great ideas, it would not be very [00:12:30] usable.

[00:12:30] **ANDREI ALEXANDRESCU:** Uh, and c Processs came, uh, so BNA created C process and he said, you know what? I'm not gonna compromise on speed. I'm gonna do all the great ideas I have, but with this, um, speed in mind, and, um, I would say BNAs turned out to be a very good language designer. Um, I've done, uh, some language design myself, and I can tell it's very difficult to, it's like keeping a lot of balls in the air, juggling out of balls in there, you know, couple with your feet and, you know, and there's a firing [00:13:00] behind you, you know, that kind of stuff.

[00:13:00] **ANDREI ALEXANDRESCU:** So it's, it's absolutely like, uh, crazy. And Biani did a great job at, um, uh, at, um, adding these features to the language without compromising, uh, performance. So, but again, as I said, it was a, it was an unproven promise. Unrealized promise. Uh, and when the STL came in 94, I think it was 94 when I first, uh, uh, read about it, when SDL came, it was, oh, so this is what C+ is [00:13:30] supposed to look like, right?

[00:13:30] **ANDREI ALEXANDRESCU:** So this is like, this is the realization of the promise of C+es, and believe me, it was everything that you hope to be and more. Um, it was such a good proof that, um, c was, was a good language that a lot of, uh, mathematically sound concepts couldn't, could be. Um, incarnated represented within C++.

[00:13:52] **ANDREI ALEXANDRESCU:** Um, it was such an elegant piece of work, and it was, in many ways it was, here's how it's done. Because before that, [00:14:00] everybody had their own, um, you know, there, there's like a whole cottage industry of like, oh, let me make my own little library here and my own, and companies try like, you know, imagine in a company like Borland.

[00:14:10] **ANDREI ALEXANDRESCU:** You're a company, uh, that makes compilers and makes, you know, has essentially it's a business and they run like a business. They have a good, uh, market value, and they say, let's make a great library and we're gonna hire the best people there and they're gonna make a great process library. And you know what, how, how is that so difficult?

[00:14:27] **ANDREI ALEXANDRESCU:** Right? And it turns out that [00:14:30] in spite all, all of these companies, uh, uh, trying, uh, there comes this Russian mathematician and he says, you know what, this is ave right? This is the, this is the way, right? He, um, I'm doing like a Russian accent with my Roman Romanian accent, which must sound lovely. So essentially, um, it was very clear that all of that cat industry of everybody doing their own stuff in their own little ways.

[00:14:52] **ANDREI ALEXANDRESCU:** Um, where in a completely different level of nirvana and much lower than where the SST l uh, was. So it became [00:15:00] clear like, oh, once you get oh SDL is, this is the way to do things. Right? And that inspired a lot of like, oh, so that's how you write a library. And then, you know, the whole boost inspiration came along and a lot of boost, um, imitates in a good way, not in an epione way, in a good way.

[00:15:16] **ANDREI ALEXANDRESCU:** A lot of boost imitates in a good way. The STL, um, so Stepan of is, uh, so, you know, it has this, um. Uh, math background, and he has this, uh, Soviet education background and he, uh, he came [00:15:30] with, uh, with fresh eyes to, uh, some program, pro problems in programming. And, um, when I say crazy, um, I'm referring to him being obsessive about a few aspects of programming.

[00:15:41] **ANDREI ALEXANDRESCU:** Um, but I, I don't think that's a defect. I think that's actually a good thing because how many geniuses are like, obsessed with, uh, whatever the object of the genius is, right? So, you know, um, he was obsessed with, uh, with representing math in, uh, in com, in, uh, in programming. And, uh, he came with, uh, [00:16:00] with this library, which is just amazing, amazing, good and amazing, uh, kind of, uh, set the whole tone of the community and ejected so much, so much enthusiasm into, into C+ and, uh, libraries and Boost in particular, um, uh, and Stephan, he, he might, he, uh, he immigrated to, to the us um, at, I think it was, um, maybe 10 years before me.

[00:16:22] **ANDREI ALEXANDRESCU:** And, um, uh, he, uh, he worked in like, on, I forgot this driver, some unrelated, uh, program businesses and [00:16:30] whatnot. But he has this obsession with, uh, with, uh, representing mathematics in, uh, programs, right? And that kind of stuff. And, uh, this obsession paid off and he tried to implement his ideas in a variety of programming languages and figure out that C+ is the only programming language in which he could do all that.

[00:16:48] **ANDREI ALEXANDRESCU:** And he spoke with bne, who bne, to his credit, he was probably among the first people who understood the power of STL and the, the how good, uh, Stefano's ideas were. [00:17:00] So BNA was like, oh, we gotta put the scene right. So BNA was like, yes, we're gonna push the scene no matter the cost. And it was a good decision because, uh, I think it was a, a very positive influence on, on the future of C++ and the present today, as it were.

[00:17:15] **ANDREI ALEXANDRESCU:** Um, so yeah, so, you know, and, um. I think some of, uh, stefano's ideas were exaggerated because he, he tried to take it, um, you know, further in number of ways. I think some of those are not, uh, are not very inspired. Some, you know, [00:17:30] some are whatnot. Some people differ in the details, but I think his body of work remains, uh, remains very solid.

[00:17:37] **ANDREI ALEXANDRESCU:** So there's, uh, at some conference, um, uh, we met Stefano, which who was cordial with me and he offered me a glass of wine, which, uh, it was very nice of him. Uh, and it was with me and Dave Abrahams and I was a, um, doctoral student at the time. And, uh, we made conversation polite. But, um, so it was David Abrahams, Stephan and [00:18:00] myself, right.

[00:18:00] **ANDREI ALEXANDRESCU:** But it became, uh, obvious to me at least, I'm not sure they even realized it, but it was just them talking and Stepan kind of convincing David, uh, to do a, um, PhD. Um, but essentially Stepan had absolutely interest in making conversation with me. So he offered me a glass of wine and we all, we, you know, he offered both, uh, Dave and I a glass of wine.

[00:18:22] **ANDREI ALEXANDRESCU:** It was very nice, very cordial. So there's no complaint I could ever, but at the same time, it was obvious that he considered David the great [00:18:30] hope of, uh, humankind. And Mia also ran right? And kind of, yeah, so Andre was also there and he, uh, was nice or whatever, right? So I grew up in, uh, in Romania to, to the, uh, ripe age of, uh, 27 when I moved to, to the, to the states.

[00:18:45] **ANDREI ALEXANDRESCU:** Uh, my mom was a, my mom was a music teacher. My dad was, was an architect. Uh, so sort of an intellectual family. Uh, there's one thing that I had an inclination for, which is literature. I've always had since I was a, a kid, [00:19:00] I learned to read like, uh, at age four by myself, with my, you know, my sister was kind of older sister.

[00:19:06] **ANDREI ALEXANDRESCU:** She was going to school and she was showing me her, whatever she learned that day. Letter a, letter E, whatever, right? So I would, uh, I would, I learned, I acquire very fast, um, uh, uh, reading. And I was an, uh, an avid reader for a good while. I mean, you know, lifetime. Um, of course there are the, the real realities of communism, um, kind of, um, looming, uh, in the [00:19:30] background at all times.

[00:19:31] **ANDREI ALEXANDRESCU:** But as kids, you don't care that much. Uh, when I was 19, um, there was a revolution in Romania when I was 19. I was in the streets. Uh, I got, uh, hit by shrapnel and that kind of stuff. So it was kind of, uh, it was, uh, heady times. It was interesting times. So that was, uh, 1989. And, um. Uh, the revolution changed everything in, in, in many ways for everybody, uh, in, in Romania, in the region.

[00:19:59] **ANDREI ALEXANDRESCU:** [00:20:00] And, uh, for me it was great because I, I was a student. I was fresh out of the military. I was, um, um, going to the, uh, college and, um, uh, if there's one thing that, uh, that, uh, communist Romania still did well, it was, um, it, it was actually, um, education. So the, the, the education was pretty good. Um, so I got, um, I got a degree in, uh, electrical engineering, but uh, all I was doing was software.

[00:20:25] **ANDREI ALEXANDRESCU:** I, I was very passionate, uh, programmer. I would, uh, go at [00:20:30] nights in the, in the, in the college and using the computer and all that. Uh, I was programmed Pascal. It is kind of a, one of those, uh, old computers. Uh, with floppy discs and all that stuff, so, yeah. Um, so, you know, everything was, let's say 10 years, um, um, older in Romania because of the difference in, uh, uh, in level of, um, um, you know, financing of, of the, of the college.

[00:20:57] **ANDREI ALEXANDRESCU:** Uh, but you know, you, I learned all the same and it was [00:21:00] great. So I, I moved to the States and it, it was a, a very good career start for me. 

[00:21:04] **RAY NOWOSIELSKI:** What year was that? 

[00:21:06] **ANDREI ALEXANDRESCU:** 1998, January. January 16, 300 bucks in my pocket. Um, a friend, uh, arranged, a very good friend. Um, um, um, classmate of mine arranged me an interview with a company, uh, his, his employer.

[00:21:24] **ANDREI ALEXANDRESCU:** And, uh, he offered me a, a bed in his house, in his apartment in New [00:21:30] York. Um, he and his sister. So they arranged everything for me and a couple of other friends, and for a while we lived. Five people in a one bedroom apartment. And, uh, it was exhilarating times. It was good times. Um, you know how they say like, athletes, like a good runner would have to have a good core.

[00:21:51] **ANDREI ALEXANDRESCU:** Mm. Although you don't run with your core explicitly, but it's a kind of second order muscle that helps you. And I think for a programmer, having a [00:22:00] good, uh, literature inclination is, is very useful. And I think that is that streak that helps me explain things. Being able to explain things and, um, uh, clarifying things to people.

[00:22:12] **ANDREI ALEXANDRESCU:** First of, I would say there's, uh, there's a link between music and a variety of, um, uh, mathematical coding, you know. This kind of ability, uh, I'm not sure what, what the, the connection is. So I think that's a, that remains a mystery. Um, [00:22:30] I know my, my, uh, my kids, he's a, he's a musician. He's a conservative European.

[00:22:34] **ANDREI ALEXANDRESCU:** He's very good. And, uh, his talent and passion for math grew together with, uh, his talent, passion for music. So it was very interesting. It started with music, which is unusual for, for others, right? He started with music and he got good at math. It sort of in parallel there, there was a clear co correlation there.

[00:22:52] **ANDREI ALEXANDRESCU:** Now, I suspect, let, let me hypothesize here. Uh, I suspect it has to do with, uh, [00:23:00] program being, uh, kind of semi creative work and um, uh, music requires some, some of this, uh, creative muscle. And, um, having that, um, obviously is gonna help a programmer too. Yeah, I was much more convinced about all of the above.

[00:23:14] **ANDREI ALEXANDRESCU:** Before a AI came, uh, forward, because, you know, here's the thing, uh, you're a musician and, uh, a and a comes and makes like great music in like five, five minutes. It creates, creates like a piece of music and you're like, wow. You know? So I thought [00:23:30] this is a creative act that's, uh, unique to people, to, you know, to human beings.

[00:23:35] **ANDREI ALEXANDRESCU:** Uh, same about programming. So right now there's AI that writes programs very well, and, uh, it's, it makes me think how how much of the creative act is in there. You know, how much creative act do we have in us? And, you know, uh, these are open questions right now. I don't remember the, the initial announcement.

[00:23:52] **ANDREI ALEXANDRESCU:** Uh, I do remember at some point, uh, there's like, uh, the boost site and they had like, I think five libraries on it. [00:24:00] And they're all lame, kind of uninteresting, but at the same time, um, they were, oh, so if I wanted the library to finally do this and not redo it again in my own code, I could simply use this.

[00:24:14] **ANDREI ALEXANDRESCU:** Um, those are the beginnings. I remember this, I forgot, but it was like a library for, for like a race, fixed size, a race or something like date and time. Like very simple, uh, non-interesting matters. But it was in the STL style, which was kind of nice. And, uh, plus, [00:24:30] and they were useful and you could actually, uh, instead of writing this, uh, simple call myself, I could simply just, uh, download the library and use it.

[00:24:37] **ANDREI ALEXANDRESCU:** So that was, I, when I, uh, when I looked at Boost for the first time, it was already established a little. Uh, but I think that was, uh, before, just in the early days of Dave Abrahams. And as I said, uh, Dave changed everything about Boost. Um, and, you know, I, um, I'll, I'll, I'll confess, um, I was on high horses after [00:25:00] writing the book and I was in the doctoral program and I was kind of a, uh, new newcomer of fresh, uh, prince of, uh, you know, uh, C templates or whatever.

[00:25:10] **ANDREI ALEXANDRESCU:** No, I was kind of a bit snooty about it, but just a bit without meaning it, without I, you know, I, I'm fundamentally very modest in, in, uh, inside, but nobody knows. Um, but I came with an attitude like, oh yeah, so I wrote this, uh, this book and it should do what it says, you kind of, kind of [00:25:30] attitude. Um, and I remember like, there's this, uh, gentleman, uh, Peter ov, uh, very nice guy.

[00:25:36] **ANDREI ALEXANDRESCU:** I think he, he's also Russian, uh, or Bulgarian or one of, one of his, I thought it was Bulgarian, but Right. Bulgarian, right. Yeah. So Peter, a very nice guy and everything. He had the, he had the boost proposal for, for um, kind of smart pointer. And my book had the whole chapter on what they call smart, smart pointers, which is kind of a little abstraction in programming.

[00:25:56] **ANDREI ALEXANDRESCU:** It doesn't matter. But essentially my abstraction and his abstraction were different in [00:26:00] details, right? And mine was like, whatever, more flexible, it could do more things and whatnot. And his was, his was simpler and. Uh, more limited, but at the same time, uh, very well put together. Um, and, you know, we had a few run on, uh, on the Usenet, and, you know, uh, to be honest, if I remember right now about the so-called flame wars, I'm not sure if the word is even in the dictionary anymore, flame war.

[00:26:25] **ANDREI ALEXANDRESCU:** So back in the day, the flame wars are like, you know, polemics about the different topics, [00:26:30] uh, especially in programming and, uh, long threads that would last for weeks and months. And people fight and call, call each other names and stuff. But then look at those early days of the internet because there're still daily, early days, right?

[00:26:43] **ANDREI ALEXANDRESCU:** Back in the day there were flame war on Boost, and everywhere on the internet, uh, the so-called use net, the old, uh, messaging protocol, uh, public kind of people could change. Uh, like the old Facebook if you wish, like the, you know, or Twitter. Um, and there's this [00:27:00] frameworks, which, uh, in retrospect when now with the, with the political environment we're in and the level of, uh.

[00:27:05] **ANDREI ALEXANDRESCU:** Of polemic and the level of, uh, you know, of division that, uh, range, that, that rules right now they seem so innocent in comparison, people would have these frameworks over like, you know, um, tab style and, you know, all of these minor details of, uh, whatever and naming convention. Yeah, naming conventions.

[00:27:26] **ANDREI ALEXANDRESCU:** Crazy, you know, simple things, um, that, you know, people can, [00:27:30] can be struggling about. But anyway, so even though we consider those like very inflammatory at the time, uh, those were like a very little thing compared to the inflammation that exists today in society. That's an aside, uh, any, anyhow, so getting back to Peter, Peter had a couple of runnings when essentially he had his, uh, smart point pointer proposal and I said, oh, you should, you should do it in a different way because you know it's better and that stuff, but I wasn't willing to put in the work.

[00:27:59] **ANDREI ALEXANDRESCU:** I was like, you know, I'm, [00:28:00] I'm in the, you know, I'm having my students, uh, things to worry about my grad, uh, research. Um, and, uh, but I, I, you know, I'm telling you what to do kind of thing, which was very, um, inappropriate of me, not, not nice of me. And he had a message that actually stays with, I remember it to this day.

[00:28:18] **ANDREI ALEXANDRESCU:** He, he wrote me a note, not, uh, he wrote me a public, uh, answer. And he wrote, here's the thing, if you think your approach is better, I can't, I'm not writing it for you. I, you can't tell me to do this and I'll do [00:28:30] it. And, you know, I'll do what I want to do and what I like, what I think is good, and you do what is what you think is good.

[00:28:36] **ANDREI ALEXANDRESCU:** And, uh, this dynamic in which you are asking me to do, uh, work in your way, but without doing the work doesn't, doesn't work. So he continued with his proposal, which was actually a high quality, um, uh, implementation. He did well, um, which ultimately got standardized. And, um. I think it's not impossible that, uh, my approach would've [00:29:00] done probably, possibly marginally better, but I don't think it would've, uh, changed the world.

[00:29:06] **ANDREI ALEXANDRESCU:** Um, but anyway, so, uh, what I'm getting with this is that this was the spirit of boost. If you wanna do it, you gotta do it. You can't just, uh, armchair people into doing it. Right. There's two smart pointers involved. One was auto pointer, which was a complete failure. And, um, I'm glad to report I had nothing to do with, uh, and the other was the so-called shared pointer, and that was, [00:29:30] uh, Peter Diaz's work.

[00:29:31] **ANDREI ALEXANDRESCU:** And, you know, I wholeheartedly think it, it's a great, uh, it's a, it's a great piece of work. Um. And, you know, that was, uh, sort of, um, you know, you could compare and contrast it with, uh, my idea, which was a so-called policy-based pointer, which was more complex, but more flexible in, in some ways. But again, I, I, you know, I, I was, uh, I, I was at a time not, uh, I didn't have the, [00:30:00] I couldn't afford the time, uh, to put in the effort.

[00:30:02] **ANDREI ALEXANDRESCU:** I was busy with my research. I couldn't put in the, uh, the effort to actually present a con, a contender in, in that race. And simply it went, his work was, uh, was just, uh, compelling to enough to including a standard. And, um, you know, now nowadays, people have used, uh, SharePoint or all the, everybody ev everywhere.

[00:30:24] **ANDREI ALEXANDRESCU:** And it's, uh, it's a very popular, uh, artifact. And, um, I think the C [00:30:30] process, um, uh, landscape would be worse off without it. Yeah. So, um, traits were, um, a use of templates that I promoted in, uh, in my book. And, um, it was quite interesting. So, you know, traits could, uh, could, uh, give you answers to questions that people didn't even, not, not only they didn't know they have an answer, but they didn't, uh, even understand it's worth asking.

[00:30:54] **ANDREI ALEXANDRESCU:** So, you know, the, the kind of stuff like, you know, is this, uh, type, uh, inheriting this other type, [00:31:00] uh, and you have that as a Boolean, as a, as a variable. And it was kind of a weird thing to even ask. And I remember, um, I, I had, I went to an interview once, uh, programming interview. I was applying to HP and I, I told the manager, oh, so actually I know way to, you know, to figure that out via type trade.

[00:31:19] **ANDREI ALEXANDRESCU:** And he said, oh, really? So I wonder how would you ever use that? So, you know, again, it was this kind of, uh. Uh, interesting, brave new world in which, uh, there, [00:31:30] there were all of these, these things that people could do with C++ that were, it was unclear the, the power of, uh, um, where, where does it take you?

[00:31:39] **ANDREI ALEXANDRESCU:** Um, so yeah, type traits. Uh, and yeah, I'm credited in boost in a number of boost libraries for, for, uh, of variety of artifacts here and there. Um, and, you know, I'm, 

[00:31:49] **RAY NOWOSIELSKI:** you never brought any of 'em through formal reviews? 

[00:31:51] **ANDREI ALEXANDRESCU:** No, I, I actually, I didn't. Uh, so I'm, I'm, um, I did not go through the rite of passage of, uh, of pushing a Boost library, but I'm very happy that other [00:32:00] people actually use my work in, in it.

[00:32:01] **ANDREI ALEXANDRESCU:** And, you know, I'm, this is like a very, uh, this is a very, um, I feel it's a, it's, I feel realized because of, uh, you know, not vicariously because I, I think it, uh, those people have done a great work at, uh, at, uh, taking my work and making it better. S story of Mother Ross Design is, um. I had some ideas. It was, you know, at a smaller scale, like, uh, step on it.

[00:32:28] **ANDREI ALEXANDRESCU:** He had some ideas [00:32:30] and, uh, there's this language, he figured, oh, I can do these ideas in this language. And it was pretty much the same for me. I had these ideas about, uh, how you can design software in a way that is flexible and, um, configurable and infinitely, uh, infinitely tweakable and reusable. And, ah, so there's this language here and which, which can do has these, uh, knobs and, you know, it has these, uh, mechanisms for, uh, allowing you to do this, this kind of stuff.

[00:32:56] **ANDREI ALEXANDRESCU:** But it was unclear how you map one one onto the other, right? Um, [00:33:00] without claiming, uh, without claiming real comparison here. Um, so this is Chopin, right? The musician, right? The, the composer. And Chopin wasn't a pianist initially. He is just a very musical guy, a kid, very sensible, very musical, very, and he had this, this way of singing and think of music that was very, um.

[00:33:21] **ANDREI ALEXANDRESCU:** Uh, unique, right? It was very, and then he found piano. And piano was a vehicle for his ideas to apply. So his music is not necessarily, [00:33:30] is very, uh, unlike any other, you know, piano music. 'cause most pianists would play a different way. But his music, he mapped his music onto the piano without claiming comparison status.

[00:33:40] **ANDREI ALEXANDRESCU:** Here you could say, Stephan, I've had these ideas, and he mapped them onto this language. I had these ideas, I mapped them onto this language. I think most critical is to C++ because it's such a flexible language. I think the, the, uh, the best sign of, uh, the enthusiasm were the, was the sheer volume and participation on boost.

[00:33:59] **ANDREI ALEXANDRESCU:** [00:34:00] Because every day it was like hundreds of messages. It was just amazing. And it's, it's, it was like trolls would be like there and kind of troll, but it's like competent people who again, did the best, did their works, their lives, work, uh, there and then. So it was very palpable. Um, and, uh, this, this mailing list, this, uh, this Usenet uh, this forum thing on Boost was, uh, was just amazing.

[00:34:27] **ANDREI ALEXANDRESCU:** And, um, I remember like for example, if you wanted to [00:34:30] get, you could get a digest at the end of the day, you could get a digest of, uh, all, everything. I was spoken in that day, but you open that digest is like, you know, 200 emails or 200 messages, right? So it was crazy. So they're better off like getting in real time.

[00:34:44] **ANDREI ALEXANDRESCU:** So anyway, so the volume of quality content was so high that it was impossible for something now to come great out of it, right? So, um, uh, I think it, I think, I think it was, uh, it was an [00:35:00] atmosphere that was very clearly conducing to something. The protagonists were. I think a very important, so Biman, he essentially created a site, Biman do.

[00:35:11] **ANDREI ALEXANDRESCU:** And you know, he, he's the nicest man anybody would meet. And, uh, I, I, I knew him and we liked each other and we, you know, we had a good relationship. And, uh, he, you know, his death was a great loss for the community. Um, so Biman, but Biman was more of an a, a ular, uh, figure. Uh, he was not a direct [00:35:30] and, uh, you know, saying strong contributor to, to the library per se.

[00:35:34] **ANDREI ALEXANDRESCU:** But, uh, for a good while, the top dog in Boost was Dave Abrahams. Um, and I think it was he who gave boost to this, um, this, uh, fame slash infamy of being like this very difficult community to get into, uh, very exacting standards. Very, like, it was like, you know, you had to be. A top [00:36:00] programmer to be able to get anything into boost.

[00:36:02] **ANDREI ALEXANDRESCU:** And I think Dave was, uh, was the person who did that, who instilled that, uh, that ethos. Dave was the, the absolute prototype of an alpha dog. He was, um, imposing, like, and we're talking about the online community, right? He was imposing, present everywhere, relentless, um, tire, no, uh, just tireless, um, on top of [00:36:30] everything, um, with uh, crazy detail oriented and, uh, right most of the time.

[00:36:37] **ANDREI ALEXANDRESCU:** So it's a combination that, you know, so that it's a combination that makes it very difficult to kind of how to do him in any, in any way. And, uh, uh, he was very dominant in, in, uh, in many ways. So he was, uh, you know, quite literal. And, you know, I remember I, I got into Boost and I was, you know, I had written a book about Cilo that was pretty notorious and, um, kind of, I [00:37:00] came with a, a good, uh, good karma about me, right?

[00:37:02] **ANDREI ALEXANDRESCU:** So I, I came to the community and I said, Hey, hi, boost, you know, what's, what's happening? And Dave immediately was like, oh. So my status as top dog is gonna be, uh, you know, impeded by this, uh, little pup. So let's, uh, so he and I had a number of run-ins over, over the years. Um. Uh, but you know, it, it's, it's undeniable that Dave has had, um, a absolutely huge overwhelming influence on Boost.

[00:37:28] **ANDREI ALEXANDRESCU:** And I think for the most part, [00:37:30] positive though, you know, but I can't pinpoint it to like one event or one, one anecdote. Dave was all over. He was like, um, um, that, that guy in, uh, in platoon, right? He was like the, the sergeant in platoon on top of everybody just screaming at everybody and make, putting an order in the ranks.

[00:37:47] **ANDREI ALEXANDRESCU:** There was nothing that would go through that, uh, that mailing list without Dave having an opinion, answering some way, being there in some, some capacity, doing something, airing, something about it. Um, it was [00:38:00] amazing. He was like on, on the whole field. Uh, my recollection is that the Boost license was created by Dave's wife, who's a, an attorney and, uh, is my favorite license Of all, it is the most permissive, the mo, the kind of the most plain language e there is.

[00:38:19] **ANDREI ALEXANDRESCU:** The clear there is, uh, the clearest there is, um, and the most, uh, accepted and understood organizations around the world. They're [00:38:30] like, oh, boost license, we're good. Um, every, you know, every, you know, college, every organization, every non-profit or profit for profit or whatever, they're going, ah, boost. That's fine.

[00:38:39] **ANDREI ALEXANDRESCU:** It works work for us. So, uh, boost is my personal favorite. Uh, there's a variety of controversies surrounding pretty much all other licensing models. Oh, you gotta insert, like the attribution, the binary code, all the, there's some nonsensical sentence in every license that, uh, you know, everybody hates. Um, but in Boost, like there's no such thing.

[00:38:59] **ANDREI ALEXANDRESCU:** It's, it's [00:39:00] to the test of time. And, um, the whole D language, which I worked on for, you know, for a decade plus, has the boost license, uh, for everything. Just because it's the best license there is, the most permissive, the most, the, the most generous. If you wish, you can take that coat, do whatever the hell you want with it, and you're good.

[00:39:19] **ANDREI ALEXANDRESCU:** And, um, we like that. It, it's never been a problem for us. So the boost license, I think, is a winner in the software world. I think it was a, a ba uh, response to [00:39:30] the overly complex and weird licenses that were, no, I'm not kidding. So it was just like all of these license that had all of the, each had, uh, something that nobody liked.

[00:39:40] **ANDREI ALEXANDRESCU:** So I think, uh, I, I fantasize that they told his wife, honey, you know what? Make a license that makes sense and that's, that doesn't have any bad sentence in it. And, you know, I think that's how it came about. What should you ask Dave? Ask him about what, uh, you know, what Boost was for him, for example, [00:40:00] what, what did it mean to him?

[00:40:01] **ANDREI ALEXANDRESCU:** Because I think he was, uh, very deeply, uh, involved with Boost and very passionate about it. Um, and then he left, uh, he left the community. He left the Boost and the civil community. Uh, I'm not sure what, what the details were, but essentially he was a very strong personality in any attempt to, uh, to how todo him, him as the top dog in the RO community was, you know, was uh, meant to create difficulty.

[00:40:26] **ANDREI ALEXANDRESCU:** Right. And I remember something with Binet that got Dave [00:40:30] to leave the community. So it, you know, he got as far as, wait a second. So now you p you're poking the lion, right? So BNA is like, by absolute definition, the father of C++. There's absolutely no way anybody could, anybody else could take that role, right?

[00:40:46] **ANDREI ALEXANDRESCU:** So then when, uh, Dave comes and says, wait a second, you know, so he had, I think, uh, if I remember correctly, he had the running with bna. He all beat indirectly or whatever, but essentially BNA kind of put him in his place and they was like, you know what? I'm not gonna [00:41:00] be in this community anymore.

[00:41:00] **ANDREI ALEXANDRESCU:** Something like that. So I remember like at some point there's like, there was some proposals on how to add concepts to the language. So there's a thing called concepts and there's like a fight between factions who wanted to promote their own ideas. And one of the faction was bna. You know, BI BNA was in one of the factions.

[00:41:17] **ANDREI ALEXANDRESCU:** And, uh, Doug, Gregory and Dave were in a d different faction. And at some point, I remember Dave told BNA publicly, he was in a forum. He said, oh, uh, you shouldn't question what Doug [00:41:30] thinks about contracts or whatever, something like that. And, you know, so. It became clear, wait a second. If Brianna can't ask questions of, of S'S feature or can't kind of, uh, lay claim or lay, you know, lay doubt on something, then who can, right?

[00:41:50] **ANDREI ALEXANDRESCU:** So it was, that was a definitely a, a kind of a defining moment for, for the, for the, the rupture that, for the break that, uh, that followed. [00:42:00] So, yeah, so, you know, they, they got their revenge. I don't know. So I think, uh, the best revenge is to do something great, which, you know, um, I'm happy they contributed to Swift and whatnot, so, you know, very good for them.

[00:42:12] **ANDREI ALEXANDRESCU:** I, you know, I don't think it's a productive state of affairs that people are, um, you know, fighting each other and destroying each other's work and that kind of stuff. So I'm happy that, uh, you know, um, uh, Dave and uh, Doug Gregor contributed elsewhere and that's totally cool. And, um, you know, it, it became, uh, sanctioned by a [00:42:30] variety of people in the, in the committee that clearly Boost is a very good, uh, is a very good device for getting your, uh, your libraries or whatever, um, proven before, before getting a standardization.

[00:42:42] **ANDREI ALEXANDRESCU:** And that's a direct consequence of the high level of quality of, of all submissions. 

[00:42:47] **RAY NOWOSIELSKI:** When do you start attending WG 21? 

[00:42:50] **ANDREI ALEXANDRESCU:** Uh, so I, I attended like, um, once in 2000 or something, and then I started my graduate student, uh, work and then I [00:43:00] started attending again, like last year, uh, at, as an Nvidia since I joined Nvidia.

[00:43:05] **ANDREI ALEXANDRESCU:** So I had a large gap. That doesn't mean I have not been in the, in touch with the language, uh, but um, getting involved with the standard, uh, is relatively new and I'm very happy I'm doing because these again, are heavy days. Uh, there's this work on this so-called reflection, which is awesome. And, uh, I'm very happy to be working with, uh, with, uh, very interesting people on, on reflection.[00:43:30] 

[00:43:30] **ANDREI ALEXANDRESCU:** Um, what the future holds for C++ is, uh, an anybody's guess. Um, but what I can tell is that, uh, a lot of competent people are doing the best they can to push the language forward into the next era of computing. And, uh, I'm very excited. Herb, um, herb and I met, uh, maybe was, uh, at the conference in 2000 or early two [00:44:00] thousands and, um, had this idea of, um.

[00:44:04] **ANDREI ALEXANDRESCU:** Because C+ was maturing at the time, so it was, uh, it was changing from like the, the buck to like the, you know, the adult, the adult, uh, deer right. Or whatever, you know, whatever the adult animal. So it was, it was changing, uh, its skin in a way, C++. And I thought this is a good time for a book that, um, that, um, condones good practice.

[00:44:28] **ANDREI ALEXANDRESCU:** Like how, you know, how do [00:44:30] you become a good C programmer? You know, what, what are the steps you, you're gonna take? And, uh, to me that was a very compelling theme. Um, because again, we're we're, uh, getting from the point when nobody knew to how to write C++ to wait a second step on, off came and explained everybody how to write C++.

[00:44:47] **ANDREI ALEXANDRESCU:** And then boost came in. Here's how the, what level of quality you should hold yourself to write good C++. And then it's like, okay, good, so we know where we should aim, how do we get there? And that's where C+ is coding [00:45:00] standards comes. Uh, that's the title of the, the second book. And, um, I went to Herb very enthusiastically, um, at, uh, it we're like, um, uh, in Belvia at a conference.

[00:45:10] **ANDREI ALEXANDRESCU:** And I went to him, he was having dinner and I, I literally, I barged in into the restaurant and I said, herb, I have a great, I have a, a book idea. He had some, uh, coding standards published online. And that, uh, that makes me a kind of, um, uh, more of a beneficiary of his work than, than a co-author. So he had a lot of work, but, um, but [00:45:30] I came with my own, my own ideas and, and my own format.

[00:45:33] **ANDREI ALEXANDRESCU:** And I said, here's the thing. We should have a, a book this collecting a book. And the book should have one or two pages per, um, item per notion so that people can easily, like, one page is one tip. One page is one standard, one, one little thing you should do to write good C process code. Um, and that turned out to be a very successful format.

[00:45:55] **ANDREI ALEXANDRESCU:** It was very difficult, uh, to achieve. To accomplish. And, uh, I remember like Herb was, he [00:46:00] was a, he, uh, he was a whi of Microsoft Word, and he knew how to adjust, like the spacing between words and the font size, all like infinite, you know, just so everything fits, uh, properly. Um, so that book was, you know, we're very enthusiastic about that book.

[00:46:18] **ANDREI ALEXANDRESCU:** And, uh, you know, though Herb has definitely more than half the credit. So he, uh, he authored, uh, most of it and the material is, uh, is inspired very heavily from his, uh, [00:46:30] uh, his, uh, website and his, uh, uh, his previous articles. But having it collected in one book and, you know, having it all in one place and in a very, uh, easy to digest format, I think it was a boon for the community because it kind of, uh, uh, it, it established like this is the.

[00:46:46] **ANDREI ALEXANDRESCU:** Uh, this is your code, right? This is your code in the military sense, right? This is the code, right? And if you read the code, if you understand the code, then you, you can, uh, do things. Um, so, you know, um, [00:47:00] and, you know, boost, uh, um, definitely, uh, took, um, uh, took the book to heart so they, you know, people like the book.

[00:47:07] **ANDREI ALEXANDRESCU:** The community will receive the book. Well, and I really like Boost, had it for a long time. I'm not sure if they still have it at, at the top of the site. They had like, uh, a recommendation from, uh, from, uh, from that book by Herb and myself. Uh, that Boost is a great library and, you know, everybody should, should follow.

[00:47:22] **ANDREI ALEXANDRESCU:** Its, uh, its way. So Herbie is, okay. So in, in many ways, Herbie is, uh, the, one of the [00:47:30] most amazing people I, I have ever met. And he's also, you know, uh, he is very different from Dave, but at the same time, similar, very different kind of leader. But, um. Very good leader. Um, and, um, herb has this unique ability to convince people of things.

[00:47:57] **ANDREI ALEXANDRESCU:** Um, uh, uh, you wouldn't believe [00:48:00] it, like he could. Um, he could, he could talk about like the sew system in Montreal and make it fun. I'm not kidding. And make it interesting. I remember like you, you, you, you run of his talks and he, he could talk about the most mundane thing and still instill it with so much passion and energy that at the end of the talk is like, yeah.

[00:48:22] **ANDREI ALEXANDRESCU:** So I guess these collapsing rules of, uh, references C+ source is a great thing, although it's such a boring thing and such a like, [00:48:30] uh, you know, annoying thing. And, um, but Herb has this quality of making everything interesting. Um, and, uh, he has a very, uh, um, relentless focus. And in that, in that way, the, uh, he's similar to Dave, uh, but also he is like the, you know, he's very nice and he is, he's not, uh, he's not the kind of guy who would be, uh, imposing himself and that kind of stuff.

[00:48:55] **ANDREI ALEXANDRESCU:** So in that way, he's very different. Um, not to say any of them is wrong or, [00:49:00] or whatever, but, you know, just to say that, uh, herb is a very different personality and, um, I, we're good friends. We're, um, um, we're, um, we go, we go, we go way, way back then. And, uh, I've, I've done with him events, conferences, and uh, you know, we're very, very good friends.

[00:49:16] **ANDREI ALEXANDRESCU:** Actually, I'm gonna have dinner with him tonight. Um, and, um, he's the kind of guy who would be able to, uh, coalesce and, you know, uh, bring a community together. Now, uh, there's a story I wanted to tell you [00:49:30] about the winter of C++. Have you heard of about the winter of C++? I assume not. So, okay.

[00:49:37] **ANDREI ALEXANDRESCU:** So, uh, something very interesting happened in the nineties and early two thousands. Um, so imagine like, you know, there is 1981 IBM pc, boom. Whoa, everybody was happy. Like, we have a pc. And, uh, uh, the next decade it was that thing like, um, four megahertz, eight megahertz, 16 megahertz, 33, 100, 200, what have you.

[00:49:58] **ANDREI ALEXANDRESCU:** So it was like this increasing [00:50:00] speed, which was, um, unstoppable. It seemed right for a decade. It kept on going the Moores Law and all that stuff, and people were, and I remember like, uh, people were thinking, wait a second. So if computers are getting fast, so fast, then uh, maybe performance of software is not very important or what's, what's happening here?

[00:50:19] **ANDREI ALEXANDRESCU:** Right? Uh, so people started writing bloated software. So it was kind of a weird exuberant, uh, period of, uh, of computing. And I remember like Microsoft Word was very slow, [00:50:30] even though it was running on the fastest computer at the time. So it was kind of a weird, a weird time. But anyway, people did care about perform.

[00:50:39] **ANDREI ALEXANDRESCU:** Uh, so the late nineties come and people are like, you know what, uh, I think, uh, we're good with performance. So then this exuberance, uh, uh, took hold in which, uh, language such as Java and Python came about. Uh, Java 94, Python, about the same. I forgot. But essentially it was in the nineties that they, they became [00:51:00] popular.

[00:51:01] **ANDREI ALEXANDRESCU:** So then it was like, oh, wait a second. So we don't, you don't have to have a fast language to have a good language. Java is simpler. Python is so easy, you know, the glue language, whatever. And they were both much slower than Cipro, let's say five times slower than C++ for any task. But people didn't care anymore.

[00:51:17] **ANDREI ALEXANDRESCU:** They're like, oh, we can do plenty because the computers are fast enough. And that was the winter of C+. Plus. The winter of C++ started, let's say around year 2000 with, uh, Java becoming very popular. Python becoming [00:51:30] popular. And, um, it lasted up until 2000 Oh, and the.com crashed. So, you know, it was also like, um, unemployment among programs and that kind of stuff.

[00:51:41] **ANDREI ALEXANDRESCU:** So the winter C++. So it goes up until year 2004. Guess what happened in year 2004? Um, um, people figure out the speed of light is limited. I'm kidding, of course, because everybody has that, right? But [00:52:00] essentially it was like this, it was like, oh, we know how to make these processes faster. And at some point it became, oh, wait a second.

[00:52:06] **ANDREI ALEXANDRESCU:** Uh, the speed of light is such that we can't make them faster anymore because we reached the speed of light with term in terms of the clock speed and, and that kind of stuff, the speed with which you can move data around the, the, the processor. So that was year 2004. Now remember the year exactly because at that time I bought the top of the line.

[00:52:26] **ANDREI ALEXANDRESCU:** Laptop and I bought a top of the, the most expensive laptop that [00:52:30] money could buy. Literally it was a Dell. And, uh, I bought the most expensive laptop because I did some consulting for a company. And the company told me, Andre can buy whatever laptop you want, we pay for it. So I said, of course, free lunch, right?

[00:52:45] **ANDREI ALEXANDRESCU:** So let's have it. So I, I bought the most, those two gigahertz. And the funny thing is 2004 in those two gigahertz, and the speed, uh, grew as, uh, it had grown before. We'd be talking about like, uh, you know, 2000 gigahertz by now, right? [00:53:00] But no, it's, uh, there's a lot of good computers running at two, four gigahertz, like comparable speeds.

[00:53:06] **ANDREI ALEXANDRESCU:** So, uh, comparable clock rates. So, um, chips did not get faster anymore. For a while, then it became, uh, like Nvidia apparel, computing, all that stuff. But before that, there was a period like 2004 through 2014. And in that period, like, uh, people are like, wait a second, we can't make the computers that much faster, so we gotta make the software [00:53:30] faster.

[00:53:30] **ANDREI ALEXANDRESCU:** And that was the renaissance of C++. I know there's a conference by, uh, by Microsoft. Uh, I forget the exact year. Uh, but it was like, you know, um, the name was, and it was in Las Vegas with all the PO and circumstance and, uh, the name was, uh, purity Plus or something like that. So, you know, it, it was essentially we're getting back to our roots and cilo is the roots and we gotta, you know, we gotta, uh, give [00:54:00] CPL seed due.

[00:54:01] **ANDREI ALEXANDRESCU:** And, uh, that was the Renaissance. So the winter of CPL was that early 2000, uh, time, uh, the, that come crash up on, up until 2004. And, um, um. What does this have to do with Herb? You may ask, because we're talking about Herb, right? So Herb, um, was the man who brought the renaissance of C++ to, to roost.

[00:54:24] **ANDREI ALEXANDRESCU:** He brought it to the fore. He made it happen. He was instrumental to making it happen. [00:54:30] Um, how do I mean that, uh, after, uh, c process got standardized in 1997, C+ 97 or 98, let's say January 98, whatever. But, you know, it was that year the, it got standardized 98. So time goes and a sense of complacency, uh, had dawned upon the committee of C+ and especially the committee and the committee's attitude and the, I remember the leaders of that committee, the, the attitude was, [00:55:00] we did this work.

[00:55:03] **ANDREI ALEXANDRESCU:** Good for us. You get it, use it. Everything's well, all is good. So. What, why are looking at me for what should I, I shouldn't do anything anymore. I should like, uh, fix a little thing here and there, a little defect or whatever, but my work is done. Literally, my work here is done. It was a very complacent and very, uh, toxic, in my opinion, um, um, morale and spirit in, in the standardization committee.[00:55:30] 

[00:55:30] **ANDREI ALEXANDRESCU:** And what changed everything was Herb. Herb came and completely changed the tone, completely changed everything. He said, we gotta standardize things. Um, we, we got, we gotta push the new standards, uh, improve the language, make it better, and have these, uh, every three years releases in the language. We gotta work on it.

[00:55:51] **ANDREI ALEXANDRESCU:** And it took from 98 to 2011 Roses 11 for Herb to convince everybody on the committee that [00:56:00] we need to push new standards. Otherwise, I'm, I'm not kidding. If it were, uh, if it were after the, the leadership before. It, it would be like C which has like a, a new standard every 20 years or whatever, right? You do like four tran, I forgot.

[00:56:17] **ANDREI ALEXANDRESCU:** Like, they have like a standard every like, um, million millennium or so, right? Whatever. So essentially it was Herb who came and said, no, we gotta push this. We gotta push this. I take credit with, uh, with, uh, one issue, which is, uh, kind of, uh, [00:56:30] an email that became, uh, if you wish, viral in the pre viral days.

[00:56:33] **ANDREI ALEXANDRESCU:** And the title was Multithreading, is the CPLs Committee listening. So I wrote that email and, uh, herb, so it was not an email. Um, it was a public message on all of these forums. Uh, C uh, multithreading is the C+ committee, uh, listening. And Multithreading was a huge topic in C++. It was not standardized properly.

[00:56:53] **ANDREI ALEXANDRESCU:** It was like a mess and everything. And, uh, herb read that and he, he took it to heart. Uh, another, [00:57:00] uh, expert Hans Bomb took it already, took it to heart. He came on the committee, uh, and I like to believe that it was my email that kind of, uh, catalyzed, uh, that kind of stuff. And it was part of the impact that her brought into the committee.

[00:57:14] **ANDREI ALEXANDRESCU:** We got, we got release new standards for civil process because the world is changing, the world is improving and we gotta change the language and improve it. And, uh, the rest is history. Um, I think without Herb, the language would've, would be right now in a way, worse shape than, than it is. [00:57:30] So there's absolutely no comparison.

[00:57:32] **ANDREI ALEXANDRESCU:** Oh, I totally understand bne. Yeah. Um, I think of this, uh, C+s is Brianna's baby, right? And the standardization committee is, uh, putting that baby in a suit and forcing him to dance or, you know, it's kind of a boring. Soul killing process that takes the fun out of everything. And it's, you know, so, and BNA is also like, um, [00:58:00] it's not Brianna's ego necessarily, but anybody's ego who have a creation and then the creation takes its own life and kind of, uh, evolves in things that the creator did not intend, did not one, did not care for.

[00:58:11] **ANDREI ALEXANDRESCU:** Um, and in the standardization process, a lot of people come and do a lot of things to the language that maybe the creator doesn't like. So, uh, Binet does have an influence on the committee that's undeniable, but at the same time, he's not the only one who has an influence on the committee. So I'm sure there's things in the language that BNA doesn't like getting the [00:58:30] language, but got standardized because they went through the process and people are like, I like that feature.

[00:58:35] **ANDREI ALEXANDRESCU:** I want it in, even if BNA was having his misgivings. So I totally understand. BNA with regard to the, the process of standardization, I see it as a necessary evil. I, I, I don't know of that, uh, firsthand, but I am not surprised in the least. Okay. I know, um, the creative of Python Roso, whom I know, great, great guy.

[00:58:56] **ANDREI ALEXANDRESCU:** He left Python, the Python community for a while. [00:59:00] Um, I myself left the committee for a while. I went, I, you know, I went, I joined the D language team and then I came back. Um, there's, uh, like the creator of the Ross language essentially is not, doesn't do anything anymore. So he created a language and after a while he just quit and he's doing something else.

[00:59:18] **ANDREI ALEXANDRESCU:** Um. So there's any number of stories about creators who, who, uh, who quit, uh, quit the language. So I'm, I'm not surprised and I'm, I'm not surprised at all that BNA get got sick of the, [00:59:30] the committee workings and that kind of stuff. It, it's, um, it's, it's not the accelerating creation process that, uh, that I'm, I'm sure he felt in initially with, uh, his own language, but it's, uh, it's boring work and it's unpleasant work, and he has this role in the committee that's important, but at the same time, uh, ign Noble, so, you know, I'm, I'm sure I'm, I totally understand.

[00:59:53] **ANDREI ALEXANDRESCU:** Um, well simple. Uh, the, the whole C+ phenomenon has been a [01:00:00] large and complex, a very, very long and complicated and a lot of people involved. Um. And in, in many ways. Uh, so for example, when a company goes good and bad, maybe the CEO would be the person to, you know, when a country goes good and bad, maybe we do the President or Prime Minister, you, you talk to, um, in C+, it's a bit, um, more like, let's say, uh, let's compare to the uk right?

[01:00:26] **ANDREI ALEXANDRESCU:** Which have the royalty and then you have the Prime Minister, [01:00:30] and, uh, BNA would be the king Herb would be the Prime Minister, right? Um, so with everything that happened, um, essentially, um, BNA is a very involved Monarch and Herb would be a, a very good executive. Um, so I think a lot of the judgment would go to both in whatever proportion.

[01:00:54] **ANDREI ALEXANDRESCU:** Um, uh, but they, they have formed a very good duo over the years. Um, I think, [01:01:00] um, I'm, I'm sure there's been any number of issues and any number of, um, frictions and any number of disagreements and any number of, oh my goodness, I'm quitting, uh, moments. But at the same time, you know, how many, uh, McCartney, Lenon, Leonard McCartney couples are gonna get in this, in this world, right.

[01:01:19] **ANDREI ALEXANDRESCU:** Um, I think, uh, I think they stood the test of time, uh, very well by, by any standard. Um, now, um. Clearly the ROS would not [01:01:30] exist without Binet, and I'm sure Ros today would not exist without Herb. Um, at the same time, there's been any number of o you know, other people who have, uh, exercised influence over, over the language and, you know, the bus library.

[01:01:42] **ANDREI ALEXANDRESCU:** Uh, so Dave, as I mentioned, and the now you know, Peter die of, uh, Doug Douglas, um, uh, Biman himself in the, in the very beginning, Matt Austin. Um, so there, there's been a number of luminaries in, uh, in Boost who definitely have influenced the language majorly. Um, [01:02:00] as to WG 21 in particular, um, I could say, I'm sorry, I ha I didn't return earlier actually, because I have this, um, I have this, this concept in my mind, which is a community of brilliant people could miss a point, which is very interesting if you think of it, a community of brilliant people.

[01:02:22] **ANDREI ALEXANDRESCU:** A PAA country could miss the. Think of, um, Weimar, Germany, right? [01:02:30] They're like a whole country of, I'm sure like the rank and file German person would be a good person, right? They missed the point and they elected Hitler. He was elected, right? Et cetera. The same about Italy and whatever. But essentially it could, there are times in history when a whole community misses a point, and it could be a vital point for that community.

[01:02:51] **ANDREI ALEXANDRESCU:** Um, where am I going with this? So what I'm seeing is that, uh, it, it has been the case historically [01:03:00] that WG 21 has missed some important point and that, uh, might have been, you know, in initially because of exuberance, like the language was, was very successful in the late nineties. It was very heady, very up, up and coming.

[01:03:15] **ANDREI ALEXANDRESCU:** Um, and people are like, oh, we're gonna design name spaces and all of the, you know, all of these features, export templates and, you know, auto BTR. So a number of failures in the language, right? And those could be ascribed to this kind of exuberance and, uh, excessive confidence if you wish. [01:03:30] Right. And, um, later there's been mistakes, maybe because of other reasons, but, um, like the committee, um, could make this, uh, could fall into this pattern of missing an important point, uh, which the community, the larger community is trying to make what the committee's missing it.

[01:03:47] **ANDREI ALEXANDRESCU:** And, um, I think coming with a fresh perspective, um, from the outside into the committee, uh, I think it gives me a bit of a perspective as to how to improve [01:04:00] on that. I like to believe that. 

[01:04:03] **RAY NOWOSIELSKI:** And why are you, why, where are we right now and what are you here for? 

[01:04:08] **ANDREI ALEXANDRESCU:** Right now we're in a beautiful Kona, Hawaii, but, uh, mostly indoors, uh, sadly.

[01:04:14] **ANDREI ALEXANDRESCU:** And, um, we are at, uh, one of the three annual meetings of the Standardization committee. Um. And, uh, we are discussing very, uh, very hotly debating the [01:04:30] introduction of some features in the C+ 26, uh, standard, such as, you know, there's so, so much discussion about contracts and, uh, and the variety of other topics.

[01:04:39] **ANDREI ALEXANDRESCU:** And the national bodies come and make comments and the committee must, must address them. A country has a bit of, of a power, leverage power over the, over the committee because they could, Beto, they could say, you know what, we're not gonna prove the standard. So, you know, I, I don't know. Uh, imagine like, uh, Madagascar does not approve the standards, so, you know, it's a problem because there's a part of the world that doesn't [01:05:00] believe the language is good enough for them.

[01:05:01] **ANDREI ALEXANDRESCU:** Right. Uh, and I, I didn't, um, I didn't even pejoratively Madagascar, but I'm saying like any, any, literally any remote country in the world could, uh. Uh, could, uh, use that leverage. Um, and even today I'm very happy because the Romanian delegation of which I'm, uh, a part of, uh, managed to push what I think is a good, uh, is a good, uh, change in the, in the upcoming standard.

[01:05:25] **ANDREI ALEXANDRESCU:** So I'm, you know, I'm, I'm, uh, very happy about that and I'm happy I had a role in that. Uh, but [01:05:30] essentially this is what's happening right now. It's a committee meeting and, uh, topics of very, very, uh, very, uh, disproportionate importance to future users of the language are being discussed right now. Mm-hmm.

[01:05:41] **RAY NOWOSIELSKI:** And why after this long gap are you back for this that, 

[01:05:44] **ANDREI ALEXANDRESCU:** ah, ah, where should I start? So, um, after I wrote my book on C++, I wanted to do more things. So I thought, let me, um, let me actually join this other language, the D language, which had more flexibility with reflection and the number of, uh, of [01:06:00] various, uh, um, within program language design.

[01:06:04] **ANDREI ALEXANDRESCU:** And also had the, the ability to design my own. My, my own features into the language. So it was a newer scrappier language. By then, CPL was maturing. So it was 2009. Uh, 2007. Yeah. Uh, so by the, by the time the CPL was becoming the big incumbent, and I was like, oh, I want the scrappy startup feeling again. So I, I joined the deep wronging language, my smaller community.

[01:06:27] **ANDREI ALEXANDRESCU:** I had, uh, a large influence in it. [01:06:30] Um, and also was, uh, uh, was doing my graduate studies. Um, so, um, I kind of left the civil process world, uh, because I was on my research, uh, graduate studies and also on, uh, this deal language, in this deal language community. Um, ultimately, I, I, uh, decided to, um, kind of as by means of a long arc.

[01:06:51] **ANDREI ALEXANDRESCU:** Uh, I decided to, let me go back to research at Nvidia. And, uh, research at Nvidia means you're doing parallel computing and doing parallel computing [01:07:00] today means you're cuda, which is the C in cuda is C++. So essentially, let me get back to C++ within, uh, this context of, uh, parallel programming and AI on all that good stuff.

[01:07:11] **ANDREI ALEXANDRESCU:** And inevitably that ties me, that gets me back to the, to C++. You know, um, I, I don't know anybody who got married twice, but it, it did happen to me professionally, um, to the same person. I mean, so you got married, you kind of have a hot, uh, yeah, that's, 

[01:07:28] **RAY NOWOSIELSKI:** that's a great line. Maybe [01:07:30] start that again. I don't know anyone who.

[01:07:31] **RAY NOWOSIELSKI:** Married the same person, 

[01:07:33] **ANDREI ALEXANDRESCU:** right? So, you know, uh, my arc with, uh, with C+ and the, the C+ language and the D language has followed a sort of a romantic, uh, kind of, uh, drama of sorts. So I started with C++ in the, in the, you know, young, uh, exciting, exciting days. It was a very hard relationship.

[01:07:52] **ANDREI ALEXANDRESCU:** And then I, you know, it was kind of gaining weight. I don't know, I'm not sure, I'm not sure this is appropriate, but it kind of, it was [01:08:00] become big and bloated and unpleasant to be with tedious. So I said, oh, let me get a fling with this new language, and I can, you know, there's, there's any ways, uh, there's so many ways in which, uh, honey fun is gonna be had.

[01:08:12] **ANDREI ALEXANDRESCU:** Um, and then it was like, oh, actually wait a second. Actually, CIVA did have some good qualities, you know, so let me get back to the, you know, to the, um, old relationship and, um, you know, rekindle it. And that's what happened. Uh, that's pretty much what happened. I think, uh, I think [01:08:30] it's a very good. Um, an all a, a better analogy than most people think because, uh, I remember when I left the de community, I was very hurt.

[01:08:40] **ANDREI ALEXANDRESCU:** Um, almost, I mean, I didn't divorce ever, but I felt like a professional divorce of sorts. Um, the community has been kind to me, so it wasn't, there was no scandal that would be exciting to, to talk about. It was just that my feeling was that the relationship had reached its arc and has ended, and that was very, um, [01:09:00] it hurt me, um, as much as it hurt leaving C+ as when I did.

[01:09:06] **ANDREI ALEXANDRESCU:** Uh, and now coming back to C++, kind of an interesting, uh, so we're both older now, wiser, hopefully, um, bigger, um, more cautious about a lot of things. More, um, wise, you know, more, more of everything. So, um. I feel an arc has been closed here [01:09:30] and it is been closing here, and I'm, you know, I, I want to stay with C++ who, and improve it for, uh, uh, for the time being.

[01:09:38] **ANDREI ALEXANDRESCU:** Oh, yeah. Um, every three years. Uh, like wine, I guess. Um, it's a, it's an interesting pace. Um, and I think it's, I understand the downsides of it, uh, which is like, oh, I'm using C+es, which C+es are using, you know, which year, whatever. So it kind of, uh, balkanize the language a bit. [01:10:00] Um, but at the same time, this world is, is the way it is.

[01:10:03] **ANDREI ALEXANDRESCU:** It's, it is that way. And, um, C+ has done a great, uh, a great job at adapting itself to the times it's, I don't know, it's the Rolling Stones of program languages. Hmm. Uh, like the Rolling Stones in the seventies, they're like a great band. And now they're a great band. It's like, it's been like there forever.

[01:10:23] **ANDREI ALEXANDRESCU:** Um, I don't know, like bgs like, um, bgs have, have this longevity, this artistic longevity and the that [01:10:30] to the, to the Times or Janet Jackson, I don't know. So there's any number of, uh, examples in the music world or in the, uh, in the movies world, in the art world, in, you know, of, uh, of people who kind of managed to change their tune and change their way, uh, to fit to, to fit the Times.

[01:10:46] **ANDREI ALEXANDRESCU:** And with this pace of standardization, cpl, you know, it's ace, the proof is in the pudding. Uh, it, it is a successful language and I am absolutely positive that it, if it were not for herb's leadership and for [01:11:00] this, uh, pace of standardization and this relentless work of make the the language better, it would not be in better shape.

[01:11:06] **ANDREI ALEXANDRESCU:** It definitely would not be in better shape. It would be like four Tran. Yeah, there's 477 and 495, and nobody knows what came after that. Literally, nobody. So. So 95 minus seven. Minus 77. Right. That's 18 years, right. Or whatever. So it's uh, kind of slow. Right. And fortune is, uh, not very popular nowadays. So, um, I totally understand [01:11:30] that.

[01:11:30] **ANDREI ALEXANDRESCU:** Disadvantages and there's a bit of a, which are an overwhelming feeling of I need to learn, uh, new things every three years as a professional programmer. Right? Um, but with the advent of ai, I think everything changes. I really think everything changes with the advent of AI in programming, because now it just, you know, the details are, the AI is gonna take care of it.

[01:11:53] **ANDREI ALEXANDRESCU:** Yeah. Um, uh, it makes for a very different program world. Even the definition of a programmer, the definition of a [01:12:00] C++ programmer is gonna change, is changing as we talk. Um, since the, uh, advent of AI in programming, um. And I'm sure the AI is, is only going to be a positive for a language that is so big, so complex, and so ever adjusting.

[01:12:17] **ANDREI ALEXANDRESCU:** It's just gonna be like, yeah. So I'm gonna code and which center of Ros do you want? I want Ros, uh, you know, 26. Oh sure. So I, I'll do that for you. No problem. So, you know, it's, it's a very different style of programming and [01:12:30] it's one in which details, um, are not that essential anymore. In the previous, uh, years, it was all the details that mattered.

[01:12:37] **ANDREI ALEXANDRESCU:** Uh, yeah. So actually this is a, a valid criticism and it, uh, it goes back to my comment about, uh, people missing the point in the, in the committee mm-hmm. And losing contact with the community sometimes. Right. Uh, at the same time, a community that puts constant pressure on the process. Uh, maybe that's not too good either.

[01:12:56] **ANDREI ALEXANDRESCU:** So I'm not sure about the, what's the best, uh, the [01:13:00] best way here. Um, all in all, I don't think it's a vital thing, a fundamental thing. Um, but, uh. But I do think that it, it does make a difference. Um, but this is the case right now because, uh, the, you know, it's just the meetings that are, let's say, secret, they're not, uh, recorded.

[01:13:18] **ANDREI ALEXANDRESCU:** Uh, and that gives freedom to a, a variety of discussions and debates and whatnot. Uh, but the papers being published are published, are definitely open to the world and people can comment on them and [01:13:30] everything. Um, so I, I don't think, uh, the meetings themselves being private, for example, I have not been on the committee for a decade, right?

[01:13:36] **ANDREI ALEXANDRESCU:** Mm-hmm. And I didn't feel like, uh, that was an impediment, lemme put it that way. Yeah. The fact that, um, for example, let's say a very capable person, uh, very good at what they're doing, very smart, very everything, but kind of outside the standardization process. Maybe they're, they don't have the time, they don't have the, the funds.

[01:13:56] **ANDREI ALEXANDRESCU:** They can't travel everywhere. They can, they don't have the focus to stay [01:14:00] with the committee and, uh, put here somebody who is mediocre. In many respects, but no such to work the, the ropes, they're very good politically. They're very good at convincing people. They're very good at pushing a paper through, and they're very good at essentially staying with with it until it happens, right?

[01:14:21] **ANDREI ALEXANDRESCU:** And I would contend that, that, um, there are a number of small features in the language that are the result of [01:14:30] mediocrity, uh, being slowly but surely, you know, pushed into the standard small, not, not, it's not nothing that would, that kills the language. Um, and there may be example of potential greatness, uh, that did not get realized simply because, uh, there, there was, uh, there was not knowledge on how, how to do so.

[01:14:50] **ANDREI ALEXANDRESCU:** Uh, also in the discussions, uh, there could be the, um, the, the advocate who's very [01:15:00] eloquent. Hmm, very well spoken, very well, uh, presenting very well, right? But who doesn't have is not very good at, uh, at what they do at, at the core of the, the, the features involved, but they are able to talk a lot and convince lot of people and essentially make a good case.

[01:15:19] **ANDREI ALEXANDRESCU:** I'll compare this with CNBC, uh, uh, open parenthesis. Um, I watch CNBC one occasion, right? It's the co whatever commercial business, uh, [01:15:30] market, uh, commentator of the, you know, um, it's this TV station, right? So if you are CNBC, you're gonna notice something very interesting. Everybody there is very well spoken.

[01:15:40] **ANDREI ALEXANDRESCU:** There's not one person who makes like a grammatical in there. They very, they're very eloquent. They speak very well. They, they can come, they can sell, uh, they can sell like, uh, uh, you know, carrots to the gardener, right? And they come, come in, what's happening in the markets, and they make predictions on what's gonna happen in the market.

[01:15:59] **ANDREI ALEXANDRESCU:** And [01:16:00] with time, you notice an interesting pattern. These very, very well spoken people, they have no idea what they're saying. They absolutely have no idea. They could very well explain what happened yesterday with the benefit of hindsight, oh, the market fell yesterday because this happened. But they have absolutely no clue on what's gonna happen tomorrow.

[01:16:18] **ANDREI ALEXANDRESCU:** They can speculate and convince people that they know what's gonna happen tomorrow, but tomorrow comes and it doesn't happen. And they, they explain what happened. Oh, that happened because, right. So, um, [01:16:30] there's a, there's a, you know, in, in the, the finance industry, there's this, uh, there's this entire, um, way of doing things, which is very well spoken.

[01:16:39] **ANDREI ALEXANDRESCU:** People not knowing what they're saying. I'm not kidding. Um, but they have the manner and the eloquence and the, the coherence and it turns out parenthesis closed. It turns out that, um. Such a person would, uh, would do some, some, uh, would exercise some influence on the [01:17:00] standardization pro process that isue and disproportionate, right?

[01:17:04] **ANDREI ALEXANDRESCU:** Because they could very well speak about something, uh, positively or negatively and convince other people, uh, about it without actually having a good point. And that's a negative. Um, uh, but at the same time, the ray of hope here is that, you know, at, to some extent it's unavoidable. Such people are in all communities.

[01:17:25] **ANDREI ALEXANDRESCU:** Uh, they're in all, you know, ever since there was like more than two humans [01:17:30] on the earth, this has happened. There was a person who had the good mouth and the good, uh, marketing, and they, they had the instinct of selling things to people negative or positively, and they exercise and the influence. And that's what happens here too sometimes.

[01:17:44] **ANDREI ALEXANDRESCU:** And that's expected. That's, uh, very interesting question. I would say it's, it's the same as, um. Uh, I'm sure he watched Matrix. Right. And, um, was the neo the French accident guy? Uh, the Ian? Right. Okay. [01:18:00] So the Ian was the sort of the previous Neo, and he was like a jaded, older and nasty kind of guy. And, uh, but you know, he's, uh, you know, that, um, his, uh, partner, she, she was, uh, she was telling Neo he was more like you, right?

[01:18:19] **ANDREI ALEXANDRESCU:** When he was younger. And I have the feeling that, uh, boost and C+ 11 was DIO and the Ian, it, it became from the hot new thing and the, you know, the, the [01:18:30] exciting thing and the pure thing in a way. So there's a lot of like moral purity if you wish, in Boost principles 11, because it was the up and comer and it was like, again, there's this, all this.

[01:18:40] **ANDREI ALEXANDRESCU:** This very high standard of quality that, um, was, uh, imposed on that community, right? And, uh, I think that was a sort of a moral purity, if you wish, right? So, you know, not, not making this too spiritual, but I think there's something there, right? So you have this, uh, up and coming, um, uh, [01:19:00] community and it was very enthusiastic, very, very strong, very powerful, very, um, um, progressive.

[01:19:08] **ANDREI ALEXANDRESCU:** And it kind of, uh, it, it had this, uh, moment of, um, uh, of it had this, this stern mo turning point in Osis 11. 'cause a lot of what happened in Boost became standardized in C+ 11. And that point, at that point, guess what happened? It became the incumbent, it transformed from Neo into the Merian, and it [01:19:30] became a bigger, bloated, larger, uh, more, uh, political, more, uh, process driven, more bureaucratic version of itself.

[01:19:40] **ANDREI ALEXANDRESCU:** And then, uh, inevitably some people didn't like that and I, you know, hard to disagree, right? At the same time, its influence continue to exist and that's also difficult to deny. So, um, I think that's what happened. It was a turning point for, for Boost, because Boost became from the up and coming, um, thing to the [01:20:00] try them proven.

[01:20:00] **ANDREI ALEXANDRESCU:** And, uh, we don't need to prove ourselves anymore, kind of, uh, kind of community. I think what changed was, um, at some point it's, it's easy to figure it out. Wait a second, there's too much of a good thing, uh, boost in very many ways. It's, it's too much of a good thing, uh, right now. It, it's an absolutely humongous library.

[01:20:21] **ANDREI ALEXANDRESCU:** It's huge. It has so much in it. It's even the size is like large. It's difficult to download, you know, [01:20:30] for somebody who's been in the days when they're like five files in it, you know, back in the, like the beginning. Uh, it's, it's a heavy proposition. Like, oh, so boost, which version, which, like, there's, there's all of this, uh, bureaucracy that surround it now.

[01:20:46] **ANDREI ALEXANDRESCU:** Um, and inevitably, um, just like the committee in Boost, there's been an, our libraries pushed because there are people who are very perseverant, uh, and, and pushed a variety of things. And it became, um, [01:21:00] maybe, um, too large for its own good. Uh, it became, um, it, it, it, uh, encompassed a number of libraries that maybe don't have enough merit, uh, as, as as they stand.

[01:21:12] **ANDREI ALEXANDRESCU:** Uh, and BNA is, uh, and I, uh, it's hard to disagree with him. BNA is one of the critics and he says there's a lot of tricks in Boost that don't belong there. That's just too much, uh, too much stuff. And I think BNA would be, uh, would be, um, um, an [01:21:30] important opponent of standardization, standardizing without much due process, everything in boost.

[01:21:35] **ANDREI ALEXANDRESCU:** Um, uh, because again, in boost there's a lot of stuff that is perhaps too, um, lacking enough significance to standardize. Mm-hmm. It could be argued, uh, that way and you know how to disagree. Um, so I think there's a number of, um, parallelism related, uh, [01:22:00] artifacts. So again, so both, both looms large in the committee, so it's impossible to not have some, uh, some influence on something.

[01:22:07] **ANDREI ALEXANDRESCU:** I have not been in those discussions because I've been in this, um, in this con in this contract related discussions. And contracts are not a boosting their language feature and Boost does not do that. Uh, they're focused on libraries, so I'm, you know, my answer is I'm not sure, but I'm sure there's something because it's impossible for there to be nothing.

[01:22:25] **ANDREI ALEXANDRESCU:** Very good. I'm aware of it. Um, but I'm not, I, um, not being in the [01:22:30] community at the time, I, I was kind of an observer from afar. Um. Culture wars have reached boost, um, uh, and, um, but at the same time, they reached, you know, all aspects of life. So why wouldn't they reach, uh, a community of mostly men and, you know, et cetera.

[01:22:49] **ANDREI ALEXANDRESCU:** And, um, so I think there, there was a lot of scandal there, and it's regrettable that it did happen. Uh, it's very [01:23:00] regrettable. Um, I, I think, uh, for me it's, um, it's very sad because the way I see it is it's, um, it's as a loss, you're losing value. You're losing value because there's people who don't, don't want to be in the committee for political reasons or people who don't want to be to go to certain conferences for, for political reasons.

[01:23:19] **ANDREI ALEXANDRESCU:** Or you have like people who don't want to work together for political reasons. And when I say political, not being political in the sense of governance, but I mean political, like, you know, um. Correct political correctness [01:23:30] and whatnot. So for, for a variety of un unrelated, uh, for reasons unrelated to technical aspects.

[01:23:37] **ANDREI ALEXANDRESCU:** And I think literally this is a loss of value because, you know, there's people who don't, uh, participate on, uh, or who are not, uh, seen well when they participate, or there's all these frictions in the community, and essentially we're losing value because of that. I don't think that's a good thing. Um, I hope, um, I hope with time, um, people are gonna, you know, are gonna become [01:24:00] more, um, um, you know, that maybe there's gonna be forgiveness, maybe there's going to be excuses, maybe there's gonna be people who apologize.

[01:24:09] **ANDREI ALEXANDRESCU:** Maybe there's gonna be a, a variety of things and such things did happen. So, you know, there's been, there's been public, um, display of, uh, for example, like, um, apologies from people and that kind of stuff, and that, that's a lot about, I think that's great. And I think that should go on and should, we should mend fences, you know.

[01:24:28] **ANDREI ALEXANDRESCU:** Because at the end of the day, again, we're [01:24:30] not paid. Uh, this is not the money thing. It's not, uh, it's simply we literally, everybody wants to make the program world better with, uh, with these, uh, these meetings and these conferences. Wow. There, uh, I dunno much. Um, and I try to stay away from politics simply because I think it's a waste of time.

[01:24:47] **ANDREI ALEXANDRESCU:** Yeah. But, uh, that being said, uh, here, here's a thought. Um, I, I worked at Meta, uh, the Facebook, you know, meta ne Facebook, right? So I, I worked at Facebook and um, I've met Mark Zuckerberg [01:25:00] personally, and, and I know him. Um, and he's a controversial figure, right? Um, people like, um, other entrepreneurs are controversial figures.

[01:25:11] **ANDREI ALEXANDRESCU:** Um, Bezos, um, you know, mosque, what have you, right? A variety of, uh, highly successful people have their controversies, um, and. There's been a lot, for example, around the creation of Facebook, there was a lot of, uh, you know, the Kovi, right? The Kovas [01:25:30] brothers. And they, they had the, you know, they had the claim to the company and et cetera, and, you know, they, they had definitely, they had their point.

[01:25:37] **ANDREI ALEXANDRESCU:** But, uh, what I'm saying is that essentially, um, with any major endeavor, uh, there's going to be, uh, intering fights and there's gonna be, uh, strife and there's gonna be strong, strong-minded people doing things that other under strong-minded people don't like. And that kind of, there's gonna be controversy [01:26:00] and the fact that this, uh, this is happening, uh, in the, in the Boost community.

[01:26:04] **ANDREI ALEXANDRESCU:** It's no surprise to me, it's human nature. People are going to have the aggression instinct, they're gonna have egos, they're going to want to do great things, and then sometimes they're gonna step on other people's toes in doing so. And this means it's Thursday in in the world, right? It's pretty much the way of the world.

[01:26:20] **ANDREI ALEXANDRESCU:** So, uh, on, on the, you know, on overall, I think it's good. I think it's good that you're making this documentary. The, the fact that it's funded and it's, it's done obviously [01:26:30] congratulations professionally and, uh, kind of at the level of quality that I think is, uh, is, uh, mimicking the boost level of quality.

[01:26:37] **ANDREI ALEXANDRESCU:** Um, thank you. I think it's, uh, I think it's testament to the fact that yeah, good things are happening and it's, uh, it's a great thing that it's happening and the fact that, uh, there's, uh, uh, there's funding in, in the alliance and there's a sense of, uh, you know, getting to some, some, uh, great values that, uh, that boost is having and, um, re reg invigorating that community.

[01:26:57] **ANDREI ALEXANDRESCU:** I think all of this sounds great to me. [01:27:00] The danger party is the following thing. Um, uh, C++, um, has, um, come from being a young and scrappy language when Boost started. So when Boost was starting, it was a young and scrappy language with young and scrappy people. And, uh, it, it, it was exciting times, right?

[01:27:21] **ANDREI ALEXANDRESCU:** The ahead times. So I'm talking about the nineties and the, you know, the early two thousands and that kind of stuff. And it's become like the big incumbent now. [01:27:30] And just by being the big incumbent now is kind of, uh, it's an unstable state to be in. Because under the big incumbent, and number one, everybody's gonna be, oh, I want to hack into that business.

[01:27:40] **ANDREI ALEXANDRESCU:** Right? I want to get into that. I wanna be better. Right? Um, and uh, different languages have approached this, uh, this matter differently. Uh, Java for example, was a great, um, was great at marketing. So Java was so good at marketing and Sun Microsystem has spent so much money on Java that actually I had a manager come [01:28:00] to me, we, you know, wow, we gotta start using Java.

[01:28:02] **ANDREI ALEXANDRESCU:** And I'm like, why? He said, I dunno what it is, but we gotta start using it. So, you know, they saw these commercials and does this excitement created about Java. Uh, and Java grew up with the internet. So it, it came, it gave people the illusion that it's, uh, it, it's powering the internet, which is not the case, but it kind of, you know, it, it figured out a way to market itself as, as the internet language.

[01:28:24] **ANDREI ALEXANDRESCU:** And then there's Python, which says, oh, we're, we're not, we're not gonna do much, but we're gonna be the glue language of [01:28:30] everything. So, yeah, you got the C+ program here and this C+ program there, and you have this library here and this library there, and some code that you wrote yourself. And I'm gonna be, uh, allow you to write 100 lines and you glue them all together and it works, right?

[01:28:44] **ANDREI ALEXANDRESCU:** So Python took this approach is the universal glue language, right? The duct tape of, uh, of all other languages, right? Um, and there's, um, the Russ language, which, which is very interesting and said, you know what? We're gonna be the safe language. We're gonna be the safe language, and [01:29:00] we're gonna be, uh, we're gonna be a fast, good language, but we're going, we're not going to have the kind of, uh, bugs that, uh, for example, when, when your, on your computer, when you misuse some program, whatever, it's gonna crash the program and you gotta, you know, turn it off and on again, right?

[01:29:15] **ANDREI ALEXANDRESCU:** That, uh, the, the universal joke. Why do you sometimes need to turn off and on, uh, a program or a computer, um, uh, device of any sort, because there's bugs in it. Hmm. And the Ross language has very successfully, uh, managed to, [01:29:30] um, avoid the class of bugs that plagues C+'s programs. And that's why Ross comes with this promise.

[01:29:36] **ANDREI ALEXANDRESCU:** We're gonna be as good as C++, but we're gonna be more safe. It's, uh, the programs are gonna have fewer bugs, they're gonna run smoothly, they're gonna, uh, be better and that kind of stuff. Um, and Rust claims it, there's no loss in in efficiency there. Uh, that point is still kind of under some debate.

[01:29:52] **ANDREI ALEXANDRESCU:** And with, uh, with regard to ai, uh, there's no major AI system that is, that is built in rust. All of them use, uh, [01:30:00] Coda, the C++ dialect from Nvidia. Um, Harry and I met, uh, by means of John Lakers and another, uh, heavyweight in the ci Rosas community. And, uh, Harry struck me as, um. As a Renaissance man, uh, a man who knows a lot of, a lot and extremely smart, he has like a huge IQ and just realizing so many fields.

[01:30:24] **ANDREI ALEXANDRESCU:** He's a musician. He's an accomplished musician. He has like, uh, you know, he composed [01:30:30] pieces that are, you know, being, playing, has music and has, uh, an organ in his house. And, um, uh, he's also like a great trader. Like he, he was a, a team lead at Citadel and, um, he managed an entire like, uh, team of, of traders.

[01:30:45] **ANDREI ALEXANDRESCU:** Um, and the fact that he's involved with, uh, with Boost and C+ right now, you know, makes me very happy because he's a, he's such a good man. Uh, good soul, kind, soul, um, very. Um, kind of monk style [01:31:00] guy. And, uh, you know, he tells me the stories about, uh, how he says his metronome at a really slow pace to, and walks in that pace to kind of get his mind into the rhythm of music.

[01:31:10] **ANDREI ALEXANDRESCU:** And then he started practicing and he taught my kids a number of ways to practice the piano that are very effective and very profound. Um, uh, it's the touch technique. So you don't actually push the, uh, push the keyboard. You just touch them and you just push them as little as you can. So, and that way you memorize the piece.

[01:31:28] **ANDREI ALEXANDRESCU:** And, uh, he's a great [01:31:30] guy and, uh, he's a multiple accomplished, uh, person and, um, a renaissance man. And it is my belief that today in the era of ai, um, it's this kind of people who are gonna succeed the most. People who are not specialized, they're not, uh, narrowly dedicated to one thing. Uh, but people who have a, a, a vast understanding of the world.

[01:31:52] **ANDREI ALEXANDRESCU:** Uh, he's read philosophy books, um, uh, a variety of like books that almost nobody knows about. And we found Oh, so in the [01:32:00] book of, yeah, yeah, sure. I read that too. So, you know, all of these, uh, things we have in common that, uh, that, um, made me very fond of him. So I think he's a great guy and I think his, uh, his presence in the community is, uh, is gonna be very, a very large positive.

[01:32:16] **RAY NOWOSIELSKI:** How did you know his iq? 

[01:32:19] **ANDREI ALEXANDRESCU:** Um, he told me, he, he did tell me to brag, but uh, the word came and he told him that somebody, um, has measured it, uh, at, um, I think it was at Stanford, I forgot. But essentially [01:32:30] somebody pro professionally measured his IQ and it turned out to be 172. And I said, ever, you know, ever since I heard that number, I.

[01:32:37] **ANDREI ALEXANDRESCU:** I said, I said, you're never i'll. I'll make fun of this number forever. And whenever he does something dumb, I'm like, oh yeah, there's not something that somebody with 1 72 IQ would do, you know, and that kind of stuff. So I, I, I, uh, pull his leg all the time. Um, he's very smart and, um, he's very modest too, so, you know, he wouldn't mention it, uh, to anyone just to brag.

[01:32:57] **ANDREI ALEXANDRESCU:** You can't be sure of that. So [01:33:00] first all, let me start with a, a big of a history of ai. Um, uh, so one interesting thing is that humans have associated AI with what, whatever was the most complex mechanism of the time. Uh, in the steam I was steampunk, right? So that was imagined as a collection of, uh, you know, steam powered whatever, tubes, what, what have you, right?

[01:33:23] **ANDREI ALEXANDRESCU:** And then, you know, you have like the clockwork era, and it was a very complicated clockwork. Uh, and then, uh, like for [01:33:30] example, in the eighties it was, of course computers, um, became popular, but before computers you'd have vacuum tubes and it was a collection of vacuum tubes and that kind of stuff. Um, so we get to the computer and we got to the, we get to the eighties.

[01:33:43] **ANDREI ALEXANDRESCU:** And in the eighties it was all about, um, so I'm, I'm, I'm not sure it's a very popular term nowadays anymore, but I'm old enough, I'm dating myself right now. Uh, it was expert systems, so it had this so-called expert systems and the Japanese built an expert system that, you know, drives the subway here [01:34:00] and there and whatever.

[01:34:01] **ANDREI ALEXANDRESCU:** And, uh, you know, Americans got an expert system that can help you with, uh, I don't know, booking a flight, which was amazing in the eighties, right? So all of these expert systems were. Uh, decision making, uh, computers, which was, uh, if this happens, then the other thing happens. And if this kind of a, of, of a series of decision making of, um, a series of decisions leading to a very complicated, very large decision making system.

[01:34:29] **ANDREI ALEXANDRESCU:** And that was your [01:34:30] expert system. And, uh, Ray, I'm sure you know very well, uh, much better than me, the history of, um, of, um, AI related movies, right? So there's, uh, there's a lot of AI movies, some optimistic, some pessimistic and invariable. They're going to be attuned to the era they was, they were, uh, made in, right?

[01:34:48] **ANDREI ALEXANDRESCU:** So, you know, you have all these, uh, you have the famous, uh, space o in which you have an expert system help, uh, which was faced with an ethical. Dilemma, which made it go, you know, crazy. [01:35:00] Um, and that was very apropos to, uh, the, the, uh, the understanding that people had of ai. So, you know, turning the clock forward, so you get to the nineties and, uh, you know, people are talking, oh, neural networks and all that stuff.

[01:35:11] **ANDREI ALEXANDRESCU:** Well, this is awesome, but there are not networks were, uh, so slow and the memory available was so low that they couldn't do anything interesting. Like, if you could build a human with 100 neurons, how smart would they be? Right? It would be like pretty bad human. So then, um, [01:35:30] uh, so it was kind of an uninteresting field, uh, neuron networks and they, uh, talk about, um, I'm not sure if you, um, uh, if again, this has remained a popular term, AI winter.

[01:35:40] **ANDREI ALEXANDRESCU:** So there's an AI winter in the seventies and eighties because, um, all of the hype of AI didn't, uh, turn out to be, uh, uh, to, uh, deliver. So then, um, 2000, the two thousands came. And at that point, something really interesting happened. Uh, computers became [01:36:00] fast enough, computers became fast enough, and they had these, uh, GPU chips in, uh, 2009.

[01:36:07] **ANDREI ALEXANDRESCU:** So, you know, it's all like in that decade, it was very interesting. So, um, uh, the gpu, uh, people figure out, uh, Alex net. Um, the guy who ended up at, um, at open a, so Alex net was a student in, uh, university of Toronto. He built this thing and he figured, oh, wait a second. These GPUs that are made for gaming actually are good for neural networks, [01:36:30] you know, and, uh, they can do the same operations that the neural network is supposed to do.

[01:36:35] **ANDREI ALEXANDRESCU:** And he figured out I can do, instead of like 100 a second, I could do a bajillion a second. And, um, this, uh, sheer increasing power of the computers and this, uh, increase in memory available and this increase in parallelism. Uh, has led to what we have today as, um, you know, absolutely in, we, you can't deny.

[01:36:59] **ANDREI ALEXANDRESCU:** It's a, [01:37:00] it's a huge revolution. I think we're, uh, just on the cusp of it. And now, uh, now you know, what's the deal with C++ and AI and all that stuff? So, so as I alluded earlier, all of the heavy lifting, uh, that's happening is actually happening in C++. Uh, there's a dialect of C++ called Cuda, which runs on Nvidia, uh, GPUs.

[01:37:20] **ANDREI ALEXANDRESCU:** And whenever anything, uh, wants to do some neural network operation is going to call a function into that, uh, into that, uh, language. In that [01:37:30] language. And that function is going to run. And I'm talking, um, you know, I'm talking literally like, uh, it's very difficult to even understand for us, um, the scale at which, uh, these, uh, processes run.

[01:37:43] **ANDREI ALEXANDRESCU:** You're talking about hundreds of, of thousands and millions of things happen simultaneously in cheap, like this big right? And, uh, all of these operations are done simultaneously, and they, they pump these things really fast, uh, amazingly, um, uh, quickly. And, um, [01:38:00] cleverly I would say, so instead of expert systems, right?

[01:38:03] **ANDREI ALEXANDRESCU:** Instead of the eighties, you have the expert system, if, and Nelson, whatever. You have all of these, um, neurons, uh, which is like a much more, um, it's a statistical thing. It's not a yes or no, it's not a if else, whatever. It's not a decision process. Uh, and it turns out that scientists figured out that it turns out to be, uh, rate a matrix, multiplication recall from college matrix multiplication.

[01:38:25] **ANDREI ALEXANDRESCU:** You have algebra and you know, all of this, uh, high school level algebra that people, uh, [01:38:30] people, uh, have done. And it turns out that, uh, what the neuron does is a matrix multiplication. And at that point, all help broke, broke loose because somebody figured out, um, how to make matrix multiplication really fast on a GPU.

[01:38:46] **ANDREI ALEXANDRESCU:** And then if you string together a few thousands of these metric metrics, multiplication, you get a system that can talk to you. And this is absolutely mind blowing. Like when you think of it, what happens inside deep down, it's [01:39:00] simply some numbers that are multiplied and added and what not. Metrics multiplications.

[01:39:05] **ANDREI ALEXANDRESCU:** And we think at the top level is that you, you are making conversation with the system and it's, uh, ex explaining things to you. And you can use it as a partner and you can use it as a mentor. You can use it as whatever, as a tool, uh, in so, uh, so many ways. Um, the fact that you have this, uh, scale of, um, uh, scale of amazing, um, all the way from a level, from the one [01:39:30] multiplication, all the way to human, uh, understanding, I think it's fascinating.

[01:39:36] **RAY NOWOSIELSKI:** So I don't even know how I wanna follow that up. Just to touch, because I don't even know how to ask this question because I'm not knowledgeable enough, but it's sort of like. When I, when my brain is thinking mm-hmm. As a human, uh, I guess I'm thinking in English on some level, but I think instinctual thoughts may be almost this other thing.

[01:39:53] **RAY NOWOSIELSKI:** Yep. It sounds like AI is thinking in C++, or how would you break that? Ah, 

[01:39:57] **ANDREI ALEXANDRESCU:** no. Um, I would, so, [01:40:00] okay, so first of all, like, uh, the way we think, so we have like several brains and all that, the neocortex and the dinosaur brain, like the chicken brain, you know, in the cerebellum back in the, so the brain itself is going to do some electrochemical things that are not unlike some simple mathematical operations that a lot of them in parallel.

[01:40:21] **ANDREI ALEXANDRESCU:** Um, but I would say that the computer is not thinking in C++, but it's thinking in statistics. This is weird. So I'm gonna explain, [01:40:30] so the, the way the computer thinks, and I'm sure you're gonna notice this, for example, Ray, how many times did you have a, like you, you chat with Chad GP or whatever, and there's a typo in the, in, in there, right?

[01:40:40] **ANDREI ALEXANDRESCU:** Many times, many times. And, uh, you know, it still figures out, yeah, it kind of, you know, it, it, uh, finagles its way out of it, understands what you meant and that kind of stuff from context. So all of, uh, all of this is happening because it's all statistical. Unlike the eighties with the decision making process that could get completely [01:41:00] blown away by a typo.

[01:41:01] **ANDREI ALEXANDRESCU:** Oh, you have a typo here. I dunno what to do if fail. I have no idea where to go. Right. Um, here, it's all statistical and they, they go, uh, the system goes with what is the most likely, uh, meaning of these words and what is the most likely, uh, word that, uh, human type and that kind of stuff. Um, so the way, uh, the computer thinks is in statistics.

[01:41:22] **ANDREI ALEXANDRESCU:** So you could, you could say it's a very mathematically oriented, uh, system. So it's not thinking in C++, but the way the whole [01:41:30] thing is implemented, use a C++ as the implementation device. Right. So, just as you would say, you're not thinking in electrochemistry. Your brain, right? It uses electrochemistry to do the thinking.

[01:41:44] **ANDREI ALEXANDRESCU:** Similarly, I could say that the comp, the, um, AI is not thinking in C++, but it is made to think using C++ as a, as a mechanism. Hmm. A shortage of compiler engineers. Yeah, that's [01:42:00] true. Um, I think, and I'm, I'm gonna sound like a broken record. I think the advent of AI is gonna change all that because there's going to be a lot of people who are good, uh, smart people with good background, with, uh, good ideas, with great creativity, and they're going to use tools to create compiles.

[01:42:19] **ANDREI ALEXANDRESCU:** And I actually have an example for you, uh, only a few days ago, um, my friend Barry Rezin, who's a major contributor to, uh, to the committee, um, [01:42:30] he implemented a feature in the, in the client compiler. Um, he implemented an important, kind of a difficult feature. And he implemented, he had no knowledge of the compiler initially, and he used, uh, an element to guide him through.

[01:42:41] **ANDREI ALEXANDRESCU:** And he made it. He actually implemented it. He was himself amazed, and I'm sure like this is just the beginning. A a lot better, better models are gonna come better AI, and people are gonna learn how to use them better. So I'm not very worried about the shortage of, uh, compiling engines or any kind of, uh, specialized [01:43:00] engineers for that matter.

[01:43:02] **ANDREI ALEXANDRESCU:** It's just, it's difficult to put it in. It's not that you want to remove it, it's just like, uh, for example, if you put it in a string, the compiler is gonna see that the string is never used. It is gonna eliminate you from the, so it's a constant, uh, thing you need to mind or otherwise, the lawyers are gonna come after you.

[01:43:17] **ANDREI ALEXANDRESCU:** So it's like a little, little thing that you gotta do always. And, uh, you know, mind it, uh, relentlessly. Um. And otherwise the consequences are dire. So it's very unpleasant, right? It's not that you don't want to, [01:43:30] it's just like, oh my goodness, I forgot about this. I gotta do this. So, and uh, again, so the compiler by its nature wants to generate the smallest, uh, code possible.

[01:43:39] **ANDREI ALEXANDRESCU:** So it's gonna see, oh, there's this texting here that nobody's using, so I'm gonna throw it away. So then you gotta actually inspect the compiled code and look at the binary and all that nonsense to look for the licensing it. And it's kind of a ridiculous requirement if you ask me. And my codes, um, is definitely going to [01:44:00] rewrite the book on attribution, uh, already is there's a lot of controversy happening with creative work, right?

[01:44:06] **ANDREI ALEXANDRESCU:** And software is no exception. Um, so I think simply we're entering a new era and I think everything is gonna be different including licensing, attribution and that kind of stuff. And, uh, I think all, we all are learning as we're going because there's no map for that territory.

