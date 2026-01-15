# BOOST_DAISY HOLMAN_STRINGOUT_v01

- - - -
filmed Date: 2025-09-16  
location:  Aurora, CO  
camera: A / B  
audio: Lav  
type: INTERVIEW  
video link: ​​https://vimeo.com/1141523385/9843033d39?fl=pl&fe=sh  
summary: Really strong documentary film stuff, in terms of the themes of meritocracy and the division that has formed in the Boost community; could see intercutting Vinnie Falco future interview and hers, makes really compelling contrast regarding takes on the Boost community and where its headed; also really strong on AI’s change to coding (she’s leading Anthropic’s Claude Code)  
- - - - 

## Transcript Start

[00:00:00] **DAISY HOLMAN:** I'm 

[00:00:11] **DAISY HOLMAN:** Daisy Holman. I, uh, study programming languages, or I make programming languages. I design programming languages. I don't know, that's what I usually say. Um, I'm a software engineer. Um, but I have done C++ professionally for my whole career and obviously used [00:00:30] boost quite a lot, especially earlier in my career.

[00:00:32] **DAISY HOLMAN:** Uh, I think when it was more relevant, um, and I've given talks at, at the Boost Conference, C++. Now it's a good question. What my specific connection to Boost is like. I have done a lot of C++ community stuff. I've been a C++ committee member, so I've. Worked with a lot of library design proposals.

[00:00:53] **DAISY HOLMAN:** This is not a short introduction and I'm sorry, um, I'm wordy, but like yeah, I've worked on a lot of [00:01:00] library design proposals that were kind of tried out in Boost. I think that's probably the closest connection I specifically have is that Boost was this kind of proving ground for a long time for C++ standard library features.

[00:01:12] **DAISY HOLMAN:** And I did a lot of C++, uh, standard library work and, uh, was quite involved in the library Evolution working group. Um, was a chair of study group nine ranges, um, which is something that was, um, well ranges weren't [00:01:30] proven out in boost, but it was like the first thing that wasn't. Um, but yeah, the first thing that I could describe that comes to my mind is this picture of early two thousands C++ that was.

[00:01:44] **DAISY HOLMAN:** Like this is before the era where we had really good package management ecosystems and like Boost was this kind of lightweight version of that for C++. And to some extent it put off the development of package [00:02:00] management ecosystems in C++ because of, so it's this like, it's this painful nostalgia.

[00:02:07] **DAISY HOLMAN:** Is that a way, is that a word? I can say it's like programming was more painful back then, but there's a little bit, a tiny bit of nostalgia, right? It's, it's not a lot. I'm happy to be with 

[00:02:20] **RAY NOWOSIELSKI:** nostalgia 

[00:02:22] **DAISY HOLMAN:** a little bit. Yeah. I think pain always comes with a little bit of nostalgia, but I think, um, yeah, I mean Boost was obviously [00:02:30] used extensively in the code I wrote for my PhD, for instance.

[00:02:34] **DAISY HOLMAN:** Um, and. A lot of my early C++ experience. And then, then also like times when I had to be, uh, was working on code bases that had to work in C++ oh three. A lot of the only options for modern, uh, things. The other thing that the, I guess the other word that comes to mind is macro. 'cause there's so much stuff in that library, in those libraries that are just hatched [00:03:00] together, um, through lots of weird tricks and uses and edge cases with, um, with macros.

[00:03:08] **DAISY HOLMAN:** I grew up in Louisiana, I in, uh, Baton Rouge, um, which is not known for producing, um. Big tech, um, software engineers. Um, my parents are both medical doctors. I knew very early on I did not wanna be a medical doctor. [00:03:30] Um, but I also, I think was always expected as a child to get a PhD. That was the, oh, you've graduated high school now.

[00:03:40] **DAISY HOLMAN:** Equivalent from, uh, like my grandfather was a relatively famous mathematician, um, Richard Anderson, um, which doesn't tell you anything 'cause there's like, you know, 300 Richard Anderson's on, on Wikipedia. But he was, [00:04:00] um, he studied infinite dimensional topology. And this is what I grew up with as like, oh yeah, this is what, this is just what our family does.

[00:04:07] **DAISY HOLMAN:** You know, you of course, you, you get your PhD. He was mad at me for taking four years. So I would, I swam in college, uh, varsity. It's competitively. And, um, he was mad at me for taking four years to go to college. 'cause he was like, you're wasting, you're wasting two years of your best professional part of your career.

[00:04:27] **DAISY HOLMAN:** Um, and I, I always thought I [00:04:30] was gonna go into math. I thought I was gonna go into to chemistry. I ended up triple majoring in, um, uh, chemistry, math, and computer science. Uh, 'cause I had enough credits going in and I had the ability to, to do all of that in four years. Um, I pushed it a little bit. I maybe pushed it a lot.

[00:04:52] **DAISY HOLMAN:** But, um, that was, yeah, that was my, uh, undergrad and uh, I wanted to be there [00:05:00] four years 'cause I wanted to swim all four years of my eligibility. And I knew I wanted to do a PhD right after undergrad and I wasn't gonna try and swim while I was doing a PhD. So, um. But yeah, I went straight from there to a PhD program in quantum chemistry, which is kind of the best of all three of those degrees.

[00:05:20] **DAISY HOLMAN:** It's very, very math intensive. Um, the software engineering in quantum chemistry is among the most difficult in all fields of natural [00:05:30] science. Um, the, it has, it's at this conflict of, uh, conflict, I think I'm using that word correctly, uh, dimension, uh, sorry. It is at this confluence of demand for scale and, uh, demand for rigor.

[00:05:48] **DAISY HOLMAN:** So you have the physicists doing their smaller toy problems, um, but only you know, on one node only with, you know, not. Uh, [00:06:00] big supercomputers just to, to prove out the, the theory. And then on the other side, uh, you have the biologists who want to do real problems and figure out how to understand these floppy molecules.

[00:06:16] **DAISY HOLMAN:** And in right in the middle you have the, the quantum chemists who are trying to do physically rigorous, um, calculations on very large molecules. And this leads to a field where a lot of people learn [00:06:30] very, very good software engineering very quickly. Um, and so like, yeah, people are very surprised when they hear my doctorates in quantum chemistry and it's like, how did you end up in programming languages?

[00:06:40] **DAISY HOLMAN:** Yeah, that 

[00:06:40] **RAY NOWOSIELSKI:** was my little, uh, simplistic question was essentially that, but it sounds like you answered it. 

[00:06:46] **DAISY HOLMAN:** Yeah. Um, I mean, some of the best software engineers I know are people who just had to do it to make their code work in the context of quantum, uh, chemistry. Hmm. [00:07:00] And, uh, yeah, a lot of, a lot of my friends from that field have ended up in software engineering.

[00:07:06] **DAISY HOLMAN:** I think it was just, I mean, it's a collection of libraries, right? I think it was always just this repository of libraries. It was this extensions set of extensions to C++, right? It was like, I think there was, I think in retrospect, I think maybe some of the draw of boost in the early two thousands was that the C++ committee was moving very slowly and there was a need [00:07:30] for something that was pseudo standard or broadly used, but not necessarily part of the standard, which is kind of like a role that package managers have filled at this point.

[00:07:43] **DAISY HOLMAN:** Right. But, uh, yeah, it was, um, I think I, it was, it was this vague, like pseudo standard. Uh, collection of libraries and it's like, is there something in Boost that does [00:08:00] this Was is a question that you would ask, right? It's like is um, you know, boost Shared Pointer was around before, um, you know, was more broadly compatible and things like that, I guess.

[00:08:16] **DAISY HOLMAN:** Um, yeah. And Boost did all kinds of like experiments that really influenced the standard. There. There was a really hacked up library that did move semantics in boost, um, with macros and all kinds of [00:08:30] crazy things. And, um, you know, I'm very into, I mean, I guess you don't know, but like people who, who know my professional work know that I'm very into meta programming.

[00:08:41] **DAISY HOLMAN:** And I was obviously back then also in Boost provided a lot of tools for that boost in pl boost meta programming libraries. One of the things I played around way more with way more than I should have, um. And I, I still think that playing around with meta programming libraries is a good thing for [00:09:00] developers to do.

[00:09:00] **DAISY HOLMAN:** It really helps you understand the language at a deeper level. 

[00:09:04] **RAY NOWOSIELSKI:** Was there a, uh, 

[00:09:06] **DAISY HOLMAN:** no. I mean, I don't wanna overstate Okay. The accolades of what it takes. I don't, I probably thought some of those things at the time, but I don't actually think that that's the message that I'd like to put out into the world about Boost.

[00:09:23] **DAISY HOLMAN:** I think anyone can write a Boost library. I'm sure you've heard by now that there is no shortage of Hot [00:09:30] Takes on both Boost and the C++ Alliance in this community. And I will warn you that I have some of those takes. I think I'm willing to say most of them to a camera question mark. Um, yeah, no.

[00:09:46] **DAISY HOLMAN:** Um, and I totally understand that you're trying to get to the bottom of a story here. And there's a really interesting one to be told. I don't think it has a lot to do with the [00:10:00] libraries or the technical aspects of the libraries. I think a lot of the contributors to Boost are very lovely people. I think a lot of the libraries are very well written.

[00:10:10] **DAISY HOLMAN:** I'll start by saying I'm not fully up to date on everything that's happened recently in, in all of this drama. I moved fields to really focus in on ai. 'cause I think this is the time to do that. Um, back in February, uh, and that was the last C++ committee meeting I went to, which sounds very recent, but [00:10:30] it means I've already missed one.

[00:10:31] **DAISY HOLMAN:** Um, I am, so I was program chair of C PPP Con in 2022 and 2023. Part of the way that that came about is that there were some things that happened. At CPP Con. Now, this is not directly related to Boost, but it's a, it's a part of the story. Mm-hmm. [00:11:00] Um, so this, the CPP con had a, um, I have to pause for a second to make sure.

[00:11:10] **DAISY HOLMAN:** I don't think there's any like, pending legislation, legislation pending legal stuff around this, but, um, we should check. Okay. Um, but, uh, yeah, there was, so there was a person who [00:11:30] is part of the leadership of C PPP Con, who was a registered sex offender and was not indicating that the way that they should, um, there was another person in the leadership of C PPP Con who was covering this up.

[00:11:54] **DAISY HOLMAN:** One of those people is no longer involved in leadership. The, the, the person who is, um, [00:12:00] the registered sex offender, one of those people is, um, this person was also involved in leadership of Boost Con, which became C++ now, and is very prominent figure in the community. Um, and I think to some extent the reason I got the opportunity to lead CBP Con is because people wanted to try and clean up that reputation, bring in a minority and make them look good.

[00:12:29] **DAISY HOLMAN:** Bring in a [00:12:30] woman and say, oh, you know, she's not afraid to be here, therefore women shouldn't be afraid to be here, even though we had a sex offender, as a, as a person of leadership. So, and I was aware. What was 

[00:12:44] **RAY NOWOSIELSKI:** the level of leadership? It was, um, 

[00:12:46] **DAISY HOLMAN:** it was a track chair. So a person who was, um. Um, a chair of one of the, uh, subsets of CBP con, uh, like a set of talks.

[00:12:58] **DAISY HOLMAN:** Mm-hmm. [00:13:00] Um, and, um, I'm sure other people will use names. I'm gonna try and avoid names for now. Understood. Because I think the, the more important thing is, is this part of the story. Um, and so yeah, I, um, I was aware at the time that that was a part of what was going on. I am not that far off of a level of person who could be a program chair of a conference like this, but I definitely was getting an opportunity that I otherwise wouldn't have [00:13:30] had.

[00:13:30] **DAISY HOLMAN:** Uh, a bunch of people in the community left this conference, uh, because of that. Um, the person who did the covering up was removed from leadership of, uh, the Boost Conference, uh, um, sequence plus now. Um, but not from this conference. And that caused a lot of stuff. [00:14:00] Um, 

[00:14:00] **RAY NOWOSIELSKI:** that same person ended up, uh, out of Boost Foundation as well.

[00:14:04] **RAY NOWOSIELSKI:** Is that right? 

[00:14:06] **DAISY HOLMAN:** I believe so, yes. Although I, I think under the current leadership of the Boost, I, I think the C++ Alliance would have supported this person. Mm-hmm. Um, we'll get there. Yeah, we'll get there. Okay. Good play, right? Yeah. I never was heavily involved in the [00:14:30] community, so Yeah. I did give the caveat that like, I've been out outside of this drama a little bit and I've tried to stay.

[00:14:36] **DAISY HOLMAN:** I'm not a good mailing list person. I'm not good at email. Um, but I, um, that you all kind of lucked out in that I, um, happens to be checking my email for some. Unrelated reason when I saw your email. Um, but I, you know, I'm, I'm glad that I'm getting this opportunity to tell parts of the story at least. [00:15:00] Um, but I, let's see, I probably, it's possible I sent some Boost emails back in 20 14, 20 15, maybe even 2012 when I was playing around with libraries or trying to, uh, get Boost MPL working for things.

[00:15:18] **DAISY HOLMAN:** Uh, boost MP 11 is another library that I played around with some, I don't know timeline wise where that came out. I really got involved in, [00:15:30] or connected with a lot of this stuff when I started going to C++ committee meetings. And that was in 2016. Mm-hmm. So I went to my, my first C++ committee meeting was the week that Trump was elected the first time.

[00:15:42] **DAISY HOLMAN:** Mm-hmm. Um, and was there like a, like, I think like. As to some extent, I wouldn't say as a kid, but like when I first learned that there was a C++ community, uh, committee, like maybe in high school, I knew that I [00:16:00] wanted to try and be a part of that. I wanted to influence the direction of the language and be able to make things better.

[00:16:10] **DAISY HOLMAN:** Um, and I got the opportunity because I was at Sandia National Labs at the time, I was working on, uh, multidimensional Race for Scientific Computing. So MB Span, uh, is the name of the feature that made it into C++ [00:16:30] 23. Um, and this is kind of, I think 2016 is starting to get closer to the end of where there was this relatively regular pipeline of something goes into Boost and then the standard looks at it and then it goes into the standard.

[00:16:46] **DAISY HOLMAN:** Mm-hmm. Um. You know, there was never an official version of that pipeline, but people were starting to publish libraries in separate and other sources, partially 'cause Boost had gotten to be, I think, so big and such a big deal that it, that their, their [00:17:00] quality standards were at the point where you couldn't, it was harder to prototype something into the Boost Libraries, um, directly.

[00:17:13] **DAISY HOLMAN:** Yeah. I I was like a, yeah, no, I think that's, that's more or less what was starting to happen. Right. Um, and that was, I mean, we also, ours, our, our library was part of maybe something that's [00:17:30] more or less the boost for scientific computing, a package called Trinos at the, uh, national Labs. Um, and so because we were part of that, it didn't make sense to also try and be a part of Boost.

[00:17:41] **DAISY HOLMAN:** I was working on a package called Cocos at the time, and they, we had a multidimensional array. Abstraction that we wanted to standardize parts of. Um, and that was, uh, ended up being a 11, 12 year long process total. I think the first paper was 2014, maybe 2013 even. [00:18:00] Um, and the first parts of it went into 23, and then the last part of it's going into 26.

[00:18:06] **DAISY HOLMAN:** Okay. So that's how, that's why I went to the committee at first and I just immediately felt like I fit in with everyone there. Like it's, it's a, I don't know if you ever walked into a room and felt like you're in a room full of people who are like you. Like that was the C++ committee for me, for sure.

[00:18:25] **DAISY HOLMAN:** Um, no, I mean it was, it was literally mostly people I'd never heard of. [00:18:30] Um, although like, you know, later heard of, 'cause I got involved in community, community more, um, and the committee more, but, uh, no, beyond and Herb were mostly doing language evolution things and I was much more interested in library level things.

[00:18:44] **DAISY HOLMAN:** Mm-hmm. Um, why. Because it was stuff that I could do. Mm-hmm. Um, I at the time had no experience working on compilers. It was also, I think things that were on the scale that we [00:19:00] felt like we could propose. Mm-hmm. As a, a national lab that doesn't write a compiler Right. You really have to build consensus between compiler authors to try and add a, a language feature.

[00:19:13] **DAISY HOLMAN:** And that is hard. Mm-hmm. Um, and I was at that time still calling myself a scientific computing expert or programming models, scientific programming models [00:19:30] expert. I wasn't, I don't think I would've called myself a programming languages expert. I wouldn't say I design programming languages or something like that.

[00:19:36] **DAISY HOLMAN:** Um, and so I felt like the library was more accessible and I think there's probably an alternate history where Boost. Figured out a process that capitalized on accessibility and ended up filling that role, um, 

[00:19:57] **RAY NOWOSIELSKI:** capitalized on accessibility. 

[00:19:59] **DAISY HOLMAN:** Yeah. I [00:20:00] think I Boost could have grown into a real package manager, right.

[00:20:06] **DAISY HOLMAN:** Boost could have. I don't blame anyone for trying to have high quality standards. I think that is an admirable goal, but there is, right, there is a alternate history where people didn't skip Boost because they didn't, um, because they didn't wanna get, you know, because [00:20:30] it was easier, quote unquote easier to get things into the standard or whatever.

[00:20:32] **DAISY HOLMAN:** Right? Um, I think it's, I mean, I don't know. I, I haven't actually thought about it. In those terms specifically, but I think maybe there was a mistake in there or missed opportunity in there. I think there's a lot of interesting versions of that in C++. Um, and you can kind of, because C++ has this, this legacy requirement, right?

[00:20:56] **DAISY HOLMAN:** It has this backwards compatibility, require [00:21:00] this backwards compatibility requirement. Um, you, you get to see a lot of the long-term effects of decisions. Um, the Boost one's not one that I thought about, but now that I think about it, I think there was the opportunity to be, to evolve into something like pi pi, right?

[00:21:19] **DAISY HOLMAN:** The, the Python package interface. Python package. I think it's, I think the I interface, I don't know. Um, but basically a, a, a, you know, [00:21:30] a hosting domain for variety of quality packages, um, that people needed to distribute. And part of the thing that I think part of the reason people used Boost or implemented things in Boost in 2010 say, was that you could get everything you needed within the same ecosystem.

[00:21:51] **DAISY HOLMAN:** Right. It was almost like a package manager in that sense is that if you, if your library was part of Boost, um, you could use other Boost [00:22:00] libraries and then whoever used your library wouldn't have to go get another Boost Library. They would've just had all of Boost. Yeah. I mean, Python is very much not benevolent dictator model anymore.

[00:22:10] **DAISY HOLMAN:** Um,

[00:22:15] **DAISY HOLMAN:** I don't know. I don't know if that's a positive or a negative. I think I never would've gotten to be involved. Mm-hmm. So, like selfishly, like I built, I've gotten the opportunity to build a lot of my career on C++ community and, and [00:22:30] standardization potentially more than most people at my level. Um, I really got a lot of amazing opportunities.

[00:22:39] **DAISY HOLMAN:** Like I said, when I first went to my, my first committee meeting, everything kind of clicked and I, I got involved in a bunch of papers because I felt like everyone was speaking the same language. And I definitely showed up with a particular way of looking at things that I think resonated with a lot of people.

[00:22:58] **DAISY HOLMAN:** Mm-hmm. 

[00:22:59] **DAISY HOLMAN:** The, [00:23:00] the story I tell, and I don't know if this is actually true or how true this is, but I, I think it's a, there's at least a kernel of truth there. I have, um, I've diagnosed dyslexia. I have pretty bad dyslexia. I had to have all my books read to me in high school and college. Um, there's a service called Reading for the Blind and Dyslexic that I, they sent me cassette tapes.

[00:23:25] **DAISY HOLMAN:** Yes, I'm that old. Um, and in college they actually sent me [00:23:30] files. So, um, but. Uh, and I would listen to my textbooks that way. Um, so you can imagine that programming has been difficult for me at times. Um, I've learned to use tooling in ways that that allows me to, um, program efficiently. And I think that has been a big boon to my career.

[00:23:53] **DAISY HOLMAN:** But it also meant that I think, you know, dyslexic people, dyslexic programmers, make the same mistakes [00:24:00] as normal programmers. We just make them a lot more often. And I think because of that, when I got to the committee, first committee meeting that I was at, I was able to see the places where people would make mistakes much more readily than other, uh, members who had, you know, been around for a short period of time.

[00:24:25] **DAISY HOLMAN:** And I think a lot of the people on the committee who had been around for a very long time. [00:24:30] Recognized this intuition and wanted to bring me onto papers and things like that, and I got a lot of great opportunities through that. I, yeah, I don't know. I'd have to look back. This has been a, this has been a long time.

[00:24:45] **DAISY HOLMAN:** Certainly the last time I would've sent a boost email would've been somewhere around 2015 or 2017 if I did at all. And I don't know if it was on the official mailing list or if it was on like a fan mailing list or anything like that. [00:25:00] I certainly, that entire world kind of immediately got replaced with the standards committee mailing lists when I joined the committee.

[00:25:11] **DAISY HOLMAN:** Okay. Um, I know I'm not telling directly the story of Boost, and so I don't know how much of this footage will use, but it's, it's, it's all connected, let's say the hot takes. Mm-hmm. Um, the first thing you need to understand about this is that the C++ community committee. The [00:25:30] people who are in charge of steering the language is very, very heavily, um, not very diverse, let's put it that way.

[00:25:39] **DAISY HOLMAN:** Mm. 

[00:25:40] **DAISY HOLMAN:** I walked into my first committee meeting in 2016 and there was one other woman in the room, and there were two, two women actively evolved in the committee at the time, and one had missed her flight. And I always wonder like, what if the other one had missed [00:26:00] her flight? Like, would my career be different?

[00:26:04] **DAISY HOLMAN:** Right. Like, that really impacted me. Um, and in, in very complicated ways. Uh, I'm, I'm trans and I was not out yet, but I knew I was out. I didn't know if I was gonna talk about this or not. And you can decide whether or not you wanna put this in the video. Um. But everyone in this community knows this, so I don't wanna [00:26:30] like, try and hide it or anything.

[00:26:32] **DAISY HOLMAN:** Um, but when I first went to my committee meeting, my first thought was, well, I'm gonna have to choose between C++ and living my life as a woman. Um, this is a thing that repeatedly came across my brain. Uh, even in, in 20, uh, like as I started to get more involved in the committee, and the committee grew probably around 2025, or sorry, 20 [00:27:00] 25, 20 20.

[00:27:01] **DAISY HOLMAN:** There were still only five of us women who were pretty regular attendees. Um, and we'd cycle in maybe three or four per meeting and most of them would just not come back. It's a very toxic environment, so it is, you know, it's not a boost versus C++ standards. Thing here. Um, [00:27:30] but there is, there was also a real attempt to try and make the committee more diverse.

[00:27:35] **DAISY HOLMAN:** Um, herb has been trying his best for a long time. I think it's very important to him. Um, I genuinely assume best. I think there are people who would sit in this chair and say, um, herb is a very good politician and knows the right things to say in order to get his agenda accomplished. And I [00:28:00] genuinely don't believe that he is been an extraordinary mentor to me and has consistently wanted to do the right things to try and improve diversity in C++.

[00:28:15] **DAISY HOLMAN:** Um, despite how toxic it is. And there, there are women contributors to boost. I don't know how any off the top of my head, but, um, but. Uh, boost had this idea of meritocracy [00:28:30] and sometime around 2016, I think this framing of meritocracy started to take for a lot of people, uh, politically. The framing of meritocracy started to take a very different direction that's very, you know, anti woke, right?

[00:28:50] **DAISY HOLMAN:** It was really about trying to weed out people who were improving diversity and, uh, trying to make things [00:29:00] truly a meritocracy and denying that there are factors other than, than pure merit that might hold someone back. Right? Um, and that is when I think we saw, uh, some rifts between, um. Mainstream C++ community and the Boost Community, um, there was [00:29:30] this organization called Include C++, which I'm sure you've heard a little bit about that story too.

[00:29:34] **DAISY HOLMAN:** Yeah, I mean, there was a time in which, um, you had the center C++ community and the Boost community was on the right, and the include C++ was on the left. And I don't know if that's exactly the right bins to put everyone in or characterizations. And I honestly hate the idea that inclusivity is a political issue.

[00:29:55] **DAISY HOLMAN:** I think it's dumb that it's a political issue. I think human beings should be respected [00:30:00] regardless. Um, I just, you know, uh, well, we won't get too far into that, but, well, 

[00:30:07] **DAISY HOLMAN:** so and so, 

[00:30:07] **DAISY HOLMAN:** no, this is what I wanted to talk about. 

[00:30:09] **DAISY HOLMAN:** Yeah. 

[00:30:09] **DAISY HOLMAN:** I'm, you know, I can talk about my work at Google and philanthropic. I don't think it's interesting in a documentary perspective.

[00:30:15] **DAISY HOLMAN:** I think the interesting thing is the influence of politics on this community and the risks that it's created. It. And this idea of merit accuracy, I think is actually the exact framing that I was trying, struggling to really [00:30:30] interject. And I, I think putting in that perspective makes me realize just how much this started going downhill around 2016.

[00:30:40] **DAISY HOLMAN:** Um, I do remember my, I think my first CBP gone was 2017, and I remember that specifically at that point, the include C++ dinner was scheduled at the same time as the Boost dinner because there was this assumption that those two communities just don't overlap. The people who wanted to promote [00:31:00] inclusivity diversity in the community were not interested in Boost.

[00:31:04] **DAISY HOLMAN:** And the Boost people were not interested in promoting inclusivity and diversity in the community. I think there is one person who had a big finger on the scales in this respect. Um. If there were one name I was gonna name in this whole discussion, it would be that person. I'll think about it. I think you know exactly who I'm talking about though.

[00:31:28] **DAISY HOLMAN:** Um, [00:31:30] because he's sending your paycheck and that's a little bit scary. And I'm not saying that you're not good journalist or anything like that, but No, I mean, this is the story that really needs to be told. And I am really, like I said, I'm a, I'm an optimistic person and I'm really optimistic that you all are the right people to tell it.

[00:31:51] **DAISY HOLMAN:** It's, to some extent, it's a microcosm of the bigger tech world. I think there are [00:32:00] a lot of people, um, because it's such a high paying industry, I think there's a lot of people who have a vested interest in kind of turning a blind eye to the diversity problems in this industry. Hmm. And so there's a lot of backlash against anyone who wants to promote diversity.

[00:32:23] **DAISY HOLMAN:** Um, and I've been on all sides of this. Um, obviously as a trans woman who no one knew [00:32:30] was trans for many years in this industry, I've experienced both sides of this. And now I'm at the point where I think my current employer doesn't know I'm trans. I don't mind them finding out. I just don't bring it up.

[00:32:43] **DAISY HOLMAN:** Mm-hmm. Um, and I've been in a lot of, involved in a lot of women's efforts in this community. I've been involved in a lot of different perspectives. I've been involved in this community from a lot of different perspectives, and it really has shown me that like [00:33:00] something needs to change about this industry as a whole.

[00:33:04] **DAISY HOLMAN:** But I think programming languages especially, and then especially systems, programming languages, um, really are at the worst of it. Um. And that's, that, that is part of why you see Rust as a community embracing diversity so much. Mm-hmm. It's kind of one of the ways that they have distinguished themselves.

[00:33:27] **DAISY HOLMAN:** I also think it's just the right thing to do, to be clear, but [00:33:30] I, I think it's one of the ways they've distinguished themselves from the old guard, from, um, I mean, that's maybe a little ageist to say it that way, but, 'cause there's, there's wonderful people of all ages in this community, but, um, they've distinguished themselves from the, the anti woke crowd if, if, if I can say it that way, in that they, they wanted to be a intentionally inclusive programming language community from the start.

[00:33:57] **DAISY HOLMAN:** And I think the Mozilla Foundation has done an excellent [00:34:00] job of promoting that. Um, I think there's some individuals in the community that have really stepped up and pushed for that. I wanted to be as much of that person as I could be for this community. I'm. I'm kind of tired, to be honest. Yeah. Um, I'm just curious as to how it came up.

[00:34:17] **DAISY HOLMAN:** 'cause this was on my list of things that I wanted to talk about and I was, I actually specifically asked some of the people involved in the story. I won't give names again. Um, I suspect some of these people are on your, [00:34:30] your list of people to interview. Um, I, I know one of them is, um, and they, uh, yeah. So when, um, in Ball asked me in ball is part of, um, well, I'm not gonna name names, so can we go back?

[00:34:52] **DAISY HOLMAN:** No. Involved one of the people, one of the women on the, it narrows it down a lot, but one of the women [00:35:00] on the board of the C++, um, foundation asked me if I wanted to. Um, program chair c PPP Con and, um, this was at C++ now, which is the, the Boost, former Boost Con. Um, but still very much similar organizers.[00:35:30] 

[00:35:30] **DAISY HOLMAN:** Um, and, uh, this story is so hard to tell without saying John Cabb, um, was there, um, and this is after everything had blown up, concealing, you know, uh, status of leadership members. Um, and [00:36:00] I said I'd be willing to consider leading the conference, but. I did want to do it my way and there were some things that needed to change and one of those was double blind review.

[00:36:16] **DAISY HOLMAN:** It is ridiculous to have a conference in 2022, um, doing, um, non blind reviews. Um, [00:36:30] and John was very adamantly opposed to this. I, with a couple of my colleagues who have helped with leadership of CPP Con since then, um, went into, there's this specific room in the, so CC++ now is held in this, um, in, in Aspen, in this, uh, like physics [00:37:00] Institute building of some sort.

[00:37:02] **DAISY HOLMAN:** That's connected to hotel? Kind of, but kind of not. I don't exactly know, but it's, it's, it's got these like little classrooms and offices where people, I think like physicists come and do sabbaticals or something like that. So we're in this like little office with like a traditional chalk blackboard and everything, and we sat there for five hours trying to convince John that doubleblind review is the right thing to do.

[00:37:27] **DAISY HOLMAN:** Um, that it [00:37:30] will, um, which is so funny that to me, that meritocracy people don't like doubleblind. I don't understand that that, that, that doesn't compute in my head. But, uh, his argument was, uh, seeing someone's name on a submission helps you understand whether it's gonna be good or not. And I was like, that's the whole point of double-blind review, is that you don't do that.

[00:37:56] **DAISY HOLMAN:** And he said, well, it makes the conference better if you do. Hmm. [00:38:00] Uh, he, at one point in this conversation said, I want to run the alternative to the woke conference. Um, I had to dredge up the exact quote this morning, so I had written it down somewhere just 'cause it, it, it shocked me. I was just like, this is a person I trust.

[00:38:22] **DAISY HOLMAN:** This is a person, I think is a leader in the community. And, you know, I had [00:38:30] been out as a woman for a long time at that point and had been experiencing that for a while. And, and it, it was shocking to me that this person who was a leader in the community was so adamantly opposed to something that really could improve diversity.

[00:38:50] **DAISY HOLMAN:** That really could give me some role models to look up to. It hurt. It hurt in a very personal way. [00:39:00] Um, and two of the three of us in that room who spent time trying to convince him left the room, crying, like could not handle it. Um, it was emotionally intense and not something someone should have to go through in a professional setting, and especially not in 2022.

[00:39:23] **DAISY HOLMAN:** Um, even, I mean, that, that five hour discussion was very eye-opening for me. And it's [00:39:30] weird, right? I, like I said, I am, I am a trans woman from Louisiana. I have very low expectations for how well people will treat me. That's like a really sad thing to say, but it's, it's, it's a real thing to say. It's, it's whatever.

[00:39:44] **DAISY HOLMAN:** It's, it's the reality. Um, and I, um, you know, when I started coming out, John was very kind to me. Um. Lives in [00:40:00] like one town over from the town that I was living in at the time and, you know, would gimme rides back from, gave me a ride back from, uh, uh, uh, a meeting, uh, a meetup in the area once and was very good about doing his best to, uh, use my correct name and pronouns from the very beginning when I, when it was hard when I didn't look like this at all.

[00:40:27] **DAISY HOLMAN:** Um, [00:40:30] and, and this is, there's this, there's this, this clash in my mind, right? Whereas this person that's also like fought tooth and nail to not have pronouns on name tags. And I'm like, I don't understand. Like, it is this, this whole experience has really contributed to my tendency to not put people in a single good box or a single bad box.

[00:40:53] **DAISY HOLMAN:** I did because I went over John's head and told Herb that I wasn't gonna do it unless. And, and Herb said, we're gonna do [00:41:00] this. Um, well, yeah, I think, I think we, we got some, I mean, I think we got some very good talks that we wouldn't have gotten otherwise. To be honest. I think we had some very good conferences.

[00:41:10] **DAISY HOLMAN:** We also got, uh, as my first year, uh, the conference, as the conference chair, we had I think four out of 120 talks were by women. And my second year, I think 18 out of 80 were [00:41:30] women. And that really was meaningful to me. Um, and, and got more people involved. Many of them are still giving talks, um, in this community.

[00:41:42] **DAISY HOLMAN:** I, I basically, I, I told people and did follow through on this, that I would personally mentor any. Women or minority who wanted to give a talk and didn't feel like they could. Um, and several of those people [00:42:00] are still very good friends and, and gave very good talks. Like, um, you know, I think that working to increase diversity and give people role models is the right thing to do, whether or not it makes the conference better, but I also think it makes the conference better.

[00:42:16] **DAISY HOLMAN:** Um, the, you know, there were some people who definitely should not have been, would not have felt psychologically safe being in the same [00:42:30] room with someone who's a known sex offender because of personal experiences. And those people found out later that they had been in the same room with this person.

[00:42:43] **DAISY HOLMAN:** And I think it profoundly affected these people psychologically. Um, like, I don't like to put people in boxes, but I also have certain lines that I have to draw for my own mental health. [00:43:00] I understand these people do too. Um, I don't know enough specifics that I don't wanna make accusations. I do know that when I talked to John about it for the first time specifically, um, his immediate response was,

[00:43:22] **DAISY HOLMAN:** oh, okay. So one of my frustrat, one of the frustrations was that some of the [00:43:30] women involved in leadership of the C++ foundation did not want to hear Arthur's side of the story without hearing his victim's side of the story. Mm-hmm. Which I think is a, a very reasonable approach to take, um, especially for a woman in this industry who has to protect her mental health also.

[00:43:58] **DAISY HOLMAN:** Um, [00:44:00] and this person was overruled and the, they, they, um, they heard him out. Um, I don't think it helped, but the, the leadership committee, um, heard his side of the story and obviously did not hear hers, um, the victim. Um, and I remember telling John, um, I'm think really badly about not [00:44:30] using names, but whatever.

[00:44:32] **DAISY HOLMAN:** Um, sorry, one second. Sorry about that. Yeah. I, uh, remember telling John, you know, I don't think it's right that we should. Um, not hear from the victim in the situation. And John said, well, you have heard from the victim in this situation. It's Arthur. 

[00:44:57] **DAISY HOLMAN:** Mm-hmm. 

[00:44:59] **DAISY HOLMAN:** And [00:45:00] I didn't even know how to respond to that.

[00:45:01] **DAISY HOLMAN:** Like, that's, that's a, a, a stunningly awful thing to say in context. And, and so I don't know how much covering up was doing was, was being done, but at this point, hearing that perspective was enough to convince me that this is a person that doesn't need to be [00:45:30] involved in leadership if we're going to be working together to make a more diverse industry.

[00:45:36] **DAISY HOLMAN:** We've had a lot of fights. My husband once told me that I am not allowed to work with this person anymore. Because he got tired of picking up the pieces of my, um, of, of my emotions. That's not the right metaphor. Picking up the pieces of my, [00:46:00] yeah. Helping me recover. 

[00:46:04] **DAISY HOLMAN:** Hmm. 

[00:46:05] **DAISY HOLMAN:** Um, every time I had a meeting with this person, I did try to, um, make a rule that I would not be on calls alone with this person.

[00:46:22] **DAISY HOLMAN:** Um, I, and it, it was a lot of the same thing as [00:46:30] this five hour discussion. It was me having to fight tooth and nail for everything, um, that I wanted to do to try and make the conference more diverse. Um, and it, it hurts. 

[00:46:45] **RAY NOWOSIELSKI:** You're giving a keynote, right? 

[00:46:46] **DAISY HOLMAN:** What? 

[00:46:47] **RAY NOWOSIELSKI:** You're giving a keynote or you, you, 

[00:46:49] **DAISY HOLMAN:** I gave a keynote earlier today.

[00:46:50] **DAISY HOLMAN:** Yeah. Did 

[00:46:51] **RAY NOWOSIELSKI:** good. 

[00:46:51] **DAISY HOLMAN:** It went really well. Awesome. Yeah. I'm very proud of it. And this conference has meant a lot to me. I think that's why I wanted to do so well on the keynote because it has meant a [00:47:00] lot to me. Like, nothing here is black and white, right? Like this is not, um, and to be clear, the, the keynote, I will say this, um, my hard rule for the entire time I was in leadership at the program committee, my hard rule was that no one who was part of the program committee leadership gets to give a keynote.

[00:47:21] **DAISY HOLMAN:** I think that that is, um, there's too much of a conflict of interest there. It's an amazing career opportunity. And if you're giving it to yourself, that's not fair. [00:47:30] Um, and so this is my first year officially not involved in CPP Con leadership, and I was lucky enough to have been working in a very hot field right now.

[00:47:41] **DAISY HOLMAN:** It's the same thing as as, as always for me. It's that, um, people come up to me afterwards and say, this changed my perspective. It's people that come up to me. It's especially the women that come up to me and say, um, oh, this, this is gonna change the way I work. I [00:48:00] think I'm gonna be better at this now, understanding what I'm doing or, you know, the impact that I'm having by just being there and being visible is the most meaningful thing to me by far.

[00:48:17] **DAISY HOLMAN:** Um, and I'm really grateful for those opportunities and that's, that's why I want to do a good job. Um, but anyway, 

[00:48:27] **RAY NOWOSIELSKI:** use to that 

[00:48:28] **DAISY HOLMAN:** person. Yeah. I think it was [00:48:30] 2016 or 2017 CPP con. Um, it was the year that we had the diversity panel, so I, we could go look that up, but I think it was 20. 17. Um, probably you've heard the story of the diversity panel incident.

[00:48:46] **DAISY HOLMAN:** I'm sure there is. There's much more story to be told there and there's people to tell that story better. But, um, there's so many stories I could tell here, but, uh, 

[00:48:54] **RAY NOWOSIELSKI:** we can find people. 

[00:48:57] **DAISY HOLMAN:** Yeah, yeah, yeah. Um, [00:49:00] but, uh, uh, yeah, that was the first time I was aware of someone saying, oh, this is the epitome of the person who would not come to a diversity panel.

[00:49:17] **DAISY HOLMAN:** And it just didn't, like, it still doesn't really fit with my brain. I'm just not really sure why anyone cares so much. Why do you care [00:49:30] if people are trying to, you know, um, improve everyone's opportunity to. Make a difference. And, and I understand that they don't see it that way, but yeah, that was the first time I was aware of this.

[00:49:46] **DAISY HOLMAN:** Yeah, I mean, I think you started to see this, this spike driven, um, in the community by this, right. I think I, Vinny is not quiet about those political [00:50:00] views and, and those are views that don't sit well with a community that very many people realize is in dire need of better diversity. And and I, to be fair, I do think there is a lot of putting people into boxes here, right?

[00:50:15] **DAISY HOLMAN:** When you have someone who supports a certain political party in ideology, you just assume that they are going to be, um, adversarial in other ways. I think [00:50:30] Vinny has had ample opportunity to try and prove that that's not the case. Um, and has not, and, and even. I was not very heavily involved in this whole interaction, but apparently published an apology like earlier this year, I think.

[00:50:47] **DAISY HOLMAN:** Um, and we were all willing to, um, you know, uh, people I knew involved in Leadership of Boost and the Biman Project [00:51:00] were all very willing to accept this apology and start working on mending some relationships. And I even started thinking about like, yeah, what, what would it look like to, you know, um, accept this person?

[00:51:17] **DAISY HOLMAN:** I think not accept this person. That's the wrong way to say that. Completely. Um, to

[00:51:27] **DAISY HOLMAN:** work with this person [00:51:30] to try and start making a difference in the community the way that I have worked. To do so. Mm-hmm. And then 2, 2, 2 weeks later, I heard from Boost Leadership friends that, um, the apology didn't stick, I think is the phrase that, um, specifically was told to me. So the C++ Slack as many tech spaces tend [00:52:00] to, especially in a political politically charged environment.

[00:52:04] **DAISY HOLMAN:** Um, C++ Slack. To be clear, I was not involved in C++ Slack. I, I know the details of this story from, uh, a secondhand, but I'm not the kind of person who goes on to like a programming language Slack. I was spending all of my extra programming language time on C++ committee mailing lists, um, interacting directly with these kinds of things.

[00:52:28] **DAISY HOLMAN:** And, um, [00:52:30] but, and I don't go on Reddit. I'm not a Reddit person. Um. I did Twitter for a little while, but only because I got to post, you know, C++ memes, basically. Um, but, uh, yeah, slack had become a somewhat toxic place. I believe there were some sort of private channels where people were coordinating on kind of [00:53:00] pushing the meritocracy notion further in the community.

[00:53:04] **DAISY HOLMAN:** Um, there was a clear understanding that there was a need for moderation. And then the acquisition of Slack by Vinny's organization I think was the point at which many people realized that that was not gonna happen. Um, which I, I, I honestly don't know Vinny that well. I've met him a few times. Um, [00:53:30] but a lot of the people involved in this.

[00:53:34] **DAISY HOLMAN:** Exodus, I, I have met many times, talked too many times, so I don't wanna give an unfair perspective here. But at the same time, like the kinds of things that these people say about Vinny and about that whole situation with Slack. Mm-hmm. Um, I think it made me feel like that was not a space that I needed to enter for my mental health.

[00:53:58] **DAISY HOLMAN:** Okay. I think [00:54:00] that's, that's, I think that's, that's what my real takeaway was from there. The C++ Alliance is, is performing a hostile takeover of the Boost organization. That is absolutely, that is the details that I'd heard and I was like, I don't want to hear more of this. I'm, I'm good. I trust people in charge to handle this.

[00:54:19] **DAISY HOLMAN:** I was, um, thought about getting involved in the Boost Foundation Board at one point to try and help fight this, um. [00:54:30] Was very kindly invited to a few of their meetings and, um, ended up declining for various reasons. Um, but it was not a, it's not a monster that I was ready to take on, I think. Mm-hmm. Um, and, and I think the end result has kind of proven that out, but I, I wasn't [00:55:00] aware of the details of, of the actual purchase of boost.org or anything like that, or, uh, any of the, the, the details there.

[00:55:08] **DAISY HOLMAN:** Um, that all makes a lot of sense. Um, or what, whatever actually happened, I don't even know if it was a purchase@boost.org, but that, that all makes a lot of sense and that tracks with the kinds of comments I had heard and I mostly had heard things that convinced me I didn't want to hear about it. Um. 

[00:55:26] **RAY NOWOSIELSKI:** So you're right.

[00:55:27] **RAY NOWOSIELSKI:** This is an incredibly interesting story. Yeah. [00:55:30] 

[00:55:30] **DAISY HOLMAN:** But, uh, I wish I knew more details to tell you, like, I wish I had stayed on top of these things or actually like, pushed into them. I can tell you, I, I, I don't know if you're, um, it's this person has declined, then please don't put their name in the documentary.

[00:55:47] **DAISY HOLMAN:** But, uh, if you talked to David Skel so that this Yeah. I mean, I think it's entirely possible that the sponsorship from C++ Alliance and the potential [00:56:00] lack of understanding that that of your level of independence is scaring people off. Yeah. Um, and you all to be clear, have been absolutely lovely and I would recommend any, anyone speak, I mean, I mean also not to be included if this person decides not to, to join, but, um, in Ball specifically asked me.

[00:56:26] **DAISY HOLMAN:** To find out if these are people that are worth talking to or [00:56:30] are these people who are gonna twist her words. And I, I think I, I don't really feel like he will, so I, I don't know. I'm a very trusting person. This is a problem. We've talked about this, but, um, I'll, I'll send, I mean, I'll send Sekel a text and see what he thinks, but, um, I, I, I really Oh, okay.

[00:56:52] **DAISY HOLMAN:** Yeah, yeah. Um, he's a, a very lovely person who's been very supportive. Um, he's been very interesting, he's been [00:57:00] very supportive of me throughout this, this whole, you know, I very publicly transitioned in front of the entire C++ committee. Um, and David Skel is very Catholic. Um, and so I had no idea how he was gonna respond and, um, has been nothing but supportive of the entire time.

[00:57:23] **DAISY HOLMAN:** So, uh oh, Dave Sekel. Curious. Oh, I've never called him anything but David. So sorry about that. 

[00:57:29] **RAY NOWOSIELSKI:** God, 

[00:57:29] **DAISY HOLMAN:** [00:57:30] what's his 

[00:57:30] **RAY NOWOSIELSKI:** claim? The fame and Boost, I guess is 

[00:57:31] **DAISY HOLMAN:** my kind of curiosity before, um, he has been involved for a while. Um, he has been involved in the C++ committee for a while. Um, he's very good at leadership, administrative type things.

[00:57:49] **DAISY HOLMAN:** Um, I, I do not know how he became the lead of the Boost Foundation. I think, um, it doesn't surprise me is the kind of person [00:58:00] who, um, is trusted in the, in the circles of people who make those decisions. Right. Um, I know that he loves C++ now as a conference. I know that is one of his favorite conferences in the whole community.

[00:58:16] **DAISY HOLMAN:** Um, and so I, I suspect wanting to be involved in that and the direction of that conference. Was probably a part of it, but I don't know. I don't want to. 

[00:58:26] **RAY NOWOSIELSKI:** When was Boost Con, like 2007 was the first one. Did you happen to go [00:58:30] to the, the first one? 

[00:58:31] **DAISY HOLMAN:** I was in college. Uh, yeah, no. Um, I, when was my first C++ now?

[00:58:39] **DAISY HOLMAN:** It might have been 2017 or 2018. Um, it was, um, I got involved in it pretty late. Like, you know, I, I made an entire career industry switch to end up in software engineering and programming languages, you know, so, [00:59:00] uh, no, I, I was not involved in it that early. I know a lot of people who were, a lot of them were very lovely people.

[00:59:06] **DAISY HOLMAN:** Um, I think there'll be a lot of the same things that, uh, John said to me in the, that room where we tried to convince him to accept. Um, double blind review. Um, I think that that is, a lot of people don't think we have a [00:59:30] diversity problem. Um, or I think some people think that we, um, that leaning into the meritocracy aspect is the way to solve the diversity problem.

[00:59:40] **DAISY HOLMAN:** I think people genuinely have good intentions sometimes. Like I just, I don't know. I don't think anyone is, I hope anyone, no one is actively malicious. I think a lot of people really want the best for this community. I just think that they aren't thinking very hard [01:00:00] or maybe aren't listening very well to, you know, data on diversity and, and ways to improve diversity.

[01:00:10] **DAISY HOLMAN:** Um, and maybe it's just not as much of an issue for them. I think there are definitely are people, I was told at my first. C++ committee meeting, which remember I'm stealth woman at the time, right? Like, this is a, a man speaking to me who did not know I was a woman, um, said, [01:00:30] well, you know, the reason why there are so many more men here than women is because the, the men are, are smarter.

[01:00:38] **DAISY HOLMAN:** Um, like this is in 2016. Somebody said this to me and said, well, it's, he said, the women, the men are, are smarter and they're also dumber. And there's like this flatter bell curve argument and blah, blah, blah. And I, I don't, that was a stuck in my mind. It was [01:01:00] kind of a horrifying moment. Um, I think I said something like, I don't think that's it.

[01:01:08] **DAISY HOLMAN:** That doesn't seem right to me, or something like that. It was, it was hard. It was really hard. Um. And every woman in this community has been through some version of that. Mm-hmm. Um, especially the ones involved in the committee. Um, and, and [01:01:30] they've, they've been, one thing I absolutely want to say, if there's any space for it, is that the women on this committee, on the C++ committee have been to a person.

[01:01:40] **DAISY HOLMAN:** Absolutely lovely. They are some of my best friends in the world. All four of the other women who come to every meeting, uh, regularly. There are other women involved, but not quite as regularly involved. Um, all four of them, like [01:02:00] absolutely would've been perfectly justified in saying, well, you know, you, you made it to this point without having to deal with the things we had to deal with.

[01:02:11] **DAISY HOLMAN:** So we're going to, you know. Accept you, but you're not one of us or something like that. Yeah. Like I think that would've been a, a, maybe this is my, you know, Louisiana upbringing speaking, but I would have not fought ill of any of them [01:02:30] saying that and, and not a one of them has. So was the code good or is the code not good?

[01:02:36] **DAISY HOLMAN:** Yeah, yeah, absolutely. No, I mean, I, I think part of the, the thing that's happened with Boost being this imagined meritocracy that's kind of ripe for, um, for this political perspective to influence it, is that, you know, code is code either [01:03:00] works well or doesn't. Um, but I think that there's are, are you a, a developer, a d write code?

[01:03:07] **DAISY HOLMAN:** Not at all. There's something that I think. The non-developers may not understand here, and that is like the vast majority of code. The purpose of code is not to communicate with a computer, it's to communicate with another human, right? So there are 30 different ways you can say the same [01:03:30] thing in code and have it generate, have it generate the same actual machine behavior, but they all look different to the human.

[01:03:40] **DAISY HOLMAN:** And the compiler turns it into the same thing, right? And so there is a very subjective element to this meritocracy, and it is often there's a lot of kind of inbred thinking where the [01:04:00] person thinks the best code objectively is the one that they understand the best, but that's because they're in the same industry.

[01:04:11] **DAISY HOLMAN:** With the person who wrote it. And so they, it becomes this very closed sell thing where yes, like the two versions of code benchmark equally well, but someone says, oh, this is, this is this, this one's much better organized and this one's much worse. To be [01:04:30] clear, some of the code in Boost is brilliant, beautifully written.

[01:04:35] **DAISY HOLMAN:** Some of it is just there to work. Um, and, and anyone who is a C++ expert will say this, anyone who is very pro Boost will say this if you read the code. Some of it is just doing its best to work in a wide variety of situations. It's very difficult to work in all of those scenarios. And, and, and that means that [01:05:00] the code is very unreadable.

[01:05:01] **DAISY HOLMAN:** And so how do you decide who has the best code in that situation? The other side of that is you have to advocate for your code. You have to advocate for your inclusion in the Boost libraries, and that means you have to have free time. Uh, you know, a single mother with two children is not getting a library into Boost regardless of how good they are at coding, you don't have time to sit around mailing lists and argue that your library is the best.

[01:05:28] **DAISY HOLMAN:** Um, um, and [01:05:30] I'm not saying anything negative about the people involved in Boost, but this is not, you know, MERITO, the illusion of meritocracy is significantly overstated there, right? You can have code that works the same way and communicates different things, and PE-people, experts will disagree on which, which is the better code.

[01:05:51] **DAISY HOLMAN:** Okay? So I, I do agree though. I understand where you're coming from and 

[01:05:56] **RAY NOWOSIELSKI:** I'm not even sure where I stand on it. I just thought I would raise the best argument I [01:06:00] could think of, which I could find persuasive. 

[01:06:02] **DAISY HOLMAN:** And I think that, I think there, they're well-intentioned people. Who really do want to put together the library that makes the world a better place through this meritocracy system.

[01:06:19] **DAISY HOLMAN:** And they haven't had to step back and think about, you know, um, what it must [01:06:30] be like to come from the other perspective or what someone outside of their industry is reading. I think that's another piece of this, right? Like how is someone from outside the industry understanding this code or outside of their subset of the industry, right?

[01:06:44] **DAISY HOLMAN:** Um, and, and Boost is, is a very base layer library ecosystem. And so a lot of it is very, um, widely used. And so judging the quality of a library in that context is very difficult because you can judge its [01:07:00] quality in terms of use from one industry and be completely wrong about its quality in terms of usefulness for another industry.

[01:07:06] **DAISY HOLMAN:** That equally needs the library. Mm-hmm. Right. So shared pointer for finance might be different for shared from shared pointer for games. Like it's really subtle and like it's hard to explain exactly what differs there, you know? Yeah. Um, I think it, I think that ship has sailed for other reasons. Okay. [01:07:30] Um, I don't think that inclusion in Boost is, can seen as all that relevant to inclusion in the standard library at this point.

[01:07:39] **DAISY HOLMAN:** Okay. Um, I think, um, people do still use the Boost Libraries and the Boost Library ecosystem in professional contexts, but it's a lot less than they used to. Mm-hmm. Um, I think that, uh, the committee has its own issues [01:08:00] with this very similar divide on meritocracy versus. Um, diversity of opinions. Um, and how much do you value understandability of your code or understandability of your interface by someone in a different area?

[01:08:20] **DAISY HOLMAN:** I think the committee has a different, um, maybe something working in the opposite direction in that you actually do have to make everyone [01:08:30] happy to some extent, and so you do actually have to kind of walk in their shoes a little bit in order to get a feature standardized. So I had to learn all kinds of things in order to work on MD Span.

[01:08:42] **DAISY HOLMAN:** I had learn all kinds of things about the games industry and how they use multidimensional arrays that I had no idea. Um, and it influenced the design. Signif influenced the design significantly and I think for the better. Um, [01:09:00] but it was a, it was about the diversity of opinions. And not necessarily about the, um, specific quality of the design for one particular use case.

[01:09:14] **DAISY HOLMAN:** I'm not saying that Boost is completely blind to diversity of use cases, either. Like I, I think that they're good software engineers and understand how generic code works and, and et cetera. Like there's, there's, there's a lot going on there. None of this is black and white, but I think [01:09:30] there is a sliding scale here.

[01:09:31] **DAISY HOLMAN:** I don't think that the, I think the C++ committee has issues with over indexing on meritocracy also. But that's a, that's a, a different discussion. Um, but I, and, and I think it's, there's a continuum. Yeah. Maybe it's not a different discussion. Maybe there is a continuum of this between, um, kind of the boost process and library acceptance process and the, the C++ [01:10:00] committee.

[01:10:00] **DAISY HOLMAN:** And the criteria there started to kind of meld at some point. But, um, yeah, there's, there's been influences in both directions. Um, it also helps that for, oh, I don't know, seven years or something like that. The chair of Library Evolution was someone from Google, which is a weird way to say that that helps, but Google is one of the companies that's big enough to have their own version of something analogous to boost [01:10:30] and so doesn't use Boost internally.

[01:10:33] **DAISY HOLMAN:** Um, and so that I think gave a different perspective on, I don't know how much that influenced things. I, I honestly, I don't think there's any ill intentions in any either direction. I joined in 2021. Um, I was, I had written a grant related to the Carbon Language project. I don't know if you've heard anything about carbon in this whole process.

[01:10:58] **DAISY HOLMAN:** Yes. [01:11:00] Um, I wanted to ask you about, yeah, so that was an interesting part of the story also. Um, I had written a grant related to that and related to using it at the national labs. I had always assumed, like from my background we talked about earlier, I always assumed I was gonna be an academic. I was going to be either in a research lab or in a professor position.

[01:11:23] **DAISY HOLMAN:** I was at a research lab. I kind of was, um, you know, more or less this, this [01:11:30] big early career grant was, um, a really great opportunity. Uh, I was really competitive grant. Um, I had one of the leads of the grant agency signed on as a co-author. I had Google, uh, endorsing the proposal and, um, offering to collaborate and the, the lab didn't take it very seriously.

[01:11:57] **DAISY HOLMAN:** I didn't feel like they [01:12:00] respected the grant proposal all that much as something that could really be done. And so then I, I reached out to Google and, and a couple of the other collaborators I had and said, Hey, I, I would still like to work on this. Um, are there were any interesting jobs that I could do?

[01:12:19] **DAISY HOLMAN:** Um, or they, you know, do you have, do you have openings? Are you hiring? Right? And, um, got some really positive responses. Um, [01:12:30] and, and honestly very lucky to have a lot of the connections that I did. Um, you know, this is, this is exactly why I don't believe in this idea of meritocracy, is that I absolutely benefited from something that is not necessarily fully meritocracy.

[01:12:45] **DAISY HOLMAN:** I knew people. Texted them and then they had interviews for me. You know, like that's, that's how a lot of this industry works. So Google is the, the Google story is, is is the story of my involvement in C++, um, [01:13:00] at Google is not, absolutely not the story you think it is. Um, it's really interesting. I had to fight tooth and nail for every little bit of involvement in C+ in C++ standard.

[01:13:12] **DAISY HOLMAN:** Um, I got to do from the committee, from from from Google, um, Google kind of had a, uh, take our ball and go home moment, um, in 2020 where they, Google used to send 50 people to every committee [01:13:30] meeting or 30, 40 big people. I don't know. It's somewhere around that order of magnitude. Um, and they said, none of us are coming back.

[01:13:39] **DAISY HOLMAN:** You know, like, here's our final list of demands. And the committee rejected it, and then they were like, well, none of us are coming back. Um, 

[01:13:48] **RAY NOWOSIELSKI:** what was the motivator there? 

[01:13:50] **DAISY HOLMAN:** Because that's a number of things. Um, some of which I probably shouldn't say for legal reasons because they're internal to Google. [01:14:00] Right.

[01:14:00] **DAISY HOLMAN:** And it's not the topic of this documentary. I think there's actually a really interesting documentary to be made there too. There's some interesting things to be talked about there, but, um, 

[01:14:09] **RAY NOWOSIELSKI:** the reason I thought it included connect. 

[01:14:11] **DAISY HOLMAN:** It did, yeah. Um, no, no Carbon was in the works before that. That happened, uh, slightly before that happened.

[01:14:18] **DAISY HOLMAN:** Uh, I was read into the project in, uh, fall of 2020, I believe. The project went public in, let's see, it was at c [01:14:30] plus plus North, I think 2022. Um, many of the Google people Can 

[01:14:38] **RAY NOWOSIELSKI:** we 

[01:14:39] **DAISY HOLMAN:** what? 

[01:14:39] **RAY NOWOSIELSKI:** Just gimme a quick, like what? What is carbon for 

[01:14:42] **DAISY HOLMAN:** those who, yeah. Carbon is an attempt to have a, uh, file for file compatible successor language to C++, very much like TypeScript is to JavaScript or Kotlin is to Java.

[01:14:56] **DAISY HOLMAN:** Um, and this is like, could you migrate [01:15:00] to something, um, newer or, um, more modern in terms of programming language, um, without having to throw out all of your, uh, old C++ code and still be able to say, include a C++ header from a carbon, um, source file. Or even invoke a C++ template that generates [01:15:30] a, uh, you know, carbon generic, um, that then calls a C++ template.

[01:15:38] **DAISY HOLMAN:** Right? It needed to be really. Easily integrated, um, in, in that way. And, and in order to migrate the millions and millions of lines of C++ that Google has, Google has the world's largest C++ code base. Um, to my knowledge, having worked on it for, for years. [01:16:00] Um, but yeah, I, I did, I went to, so I was on, I was a, a co-author on the paper that turned out to be, uh, Google taking its ball and going home.

[01:16:09] **DAISY HOLMAN:** 'cause I wanted some of the same things that they wanted. But I am, I've, I've always been much more, I mean, I'm here, I've always been much more of a, um, try and see the good in everyone. And I didn't think that walking away from the C+ C++ committee was good. I also felt like, you [01:16:30] know, I was 20% of the women on the committee.

[01:16:32] **DAISY HOLMAN:** I didn't feel comfortable changing that either. I felt like I had a responsibility to. Women coming to the committee meetings to be able to find role models. Um, I think there was a part of that me that was just, didn't wanna give up for that reason. So, to be, to be clear, I did not work on Adan from Google.

[01:16:57] **DAISY HOLMAN:** Okay. So I, I was [01:17:00] semi lead on the project, um, the two years before I went to Google. Okay. Um, most of the standardization was done at that point, but there's the, the people who pushed across the line deserve just as much, if not more credit. Uh, and the people who started it before I was even involved deserve a lot of credit too.

[01:17:20] **DAISY HOLMAN:** So like I got to play a very key role in that paper. But I don't wanna, I don't want to, um, imply that this was like [01:17:30] my thing. But yeah. Uh, I think that, so that's a good question. Was indie span. And a lot of the, so a lot of the backlash against in vsan on the committee was for very different perspec for, for very different reasons.

[01:17:48] **DAISY HOLMAN:** One of the ones is that the, this thing that we've already talked about is that sometimes people aren't all that great at seeing the needs of another industry or another part of the industry. Um, and [01:18:00] scientific computing was coming so far out of left field for a lot of these, a lot of people. Um, that the, the needs that were being expressed didn't make a lot of sense and people didn't understand the need for complexity.

[01:18:15] **DAISY HOLMAN:** They thought it was over-engineered. You know, all of these different discussions were there. I think, um, yeah, I think part of [01:18:30] we had implementation experience. Which is what the committee is mostly looking for. Whether it had been in Boost or in, um, like whether it had been in Boost or in Trinos where we use it a lot.

[01:18:47] **DAISY HOLMAN:** I don't think that that changed a lot. There were several times I remember people suggesting that we try and put it into Boost and I think we decided it wasn't worth it. [01:19:00] Um, time-wise in terms of the kind of political favor we would curry. I also think there was some worry that we weren't gonna get a lot of scientific computing users there, and so that putting it into a more general context like Boost was going to make the things that we needed from the future.

[01:19:25] **DAISY HOLMAN:** Seem less important because they weren't getting, wouldn't get used in boost. Yeah. [01:19:30] Honestly, I mean, this is my bias in seeing the best in people, but I think there's not as much funny business going on there as you think. I think that quite often the reason why proposals from Microsoft, from Google, from Apple see a lot of attention is because they are good.

[01:19:55] **DAISY HOLMAN:** Um, I don't think the fact that they come from these big companies [01:20:00] gives them any sort of boost other upon, not intended, other than that they are, um, coming from people who have deployed them in a very wide variety of scenarios, right? So a large company gives you a lot of usage experience internally. Um.

[01:20:22] **DAISY HOLMAN:** And makes you have to balance the needs of a more diverse set of stakeholders. And because you've already done [01:20:30] that balancing of diverse stakeholders within your company or even within a product that your company ships, like a lot of things that came out of Cuda from Nvidia and made it made their way towards the standard were things that that company had already spent time building consensus among their users for, uh, yeah.

[01:20:51] **DAISY HOLMAN:** Um, there's a long story about how my time at Google ended that I won't get into. Um, [01:21:00] yeah, I don't wanna, there's not time to tell that whole story without portraying people the wrong way. But, um, more or less, my last day at Google with very short notice, like 30 minutes notice, was the day before CPP Con last year.

[01:21:19] **DAISY HOLMAN:** Um, my slides were all on the corporate network that I lost access to. My talk was about how Google uses C++ in a very specific [01:21:30] way, and I did not wanna do that talk anymore for obvious reasons. Um, and so I come here to this conference last year, um, and I, like I said, I think more than most people in this community, I've really benefited from this conference and this community embracing me and treating me as family.

[01:21:48] **DAISY HOLMAN:** And I really, really felt that last year. Um, it was very hard. You can imagine that for someone who's, you know, parents [01:22:00] gave them a pat on the back when, when I got my PhD and was like, good, good job with that high school diploma. You know, they didn't say it that way, but that was the sentiment that, you know, losing a job is a brutal setback.

[01:22:16] **DAISY HOLMAN:** In that context. And I was not doing well emotionally getting there. Yeah. And, and I, um, this community really embraced me, really [01:22:30] helped me through this. I went out and I literally went out and because I hadn't owned a personal laptop in years, 'cause my, my job had always been my hobby. And so if I was gonna do, you know, personal projects that were always closely enough, close enough related to my job that I'd just do 'em on my corporate computer.

[01:22:48] **DAISY HOLMAN:** Right. Like, um, it was always like I had a joy in representing my employer and showing the cool things that they were [01:23:00] letting me do. And so it was always related to work. I, I literally went out and bought a, a personal laptop at Costco on the Monday of CPP Con last year. Um, and, uh, that was. Yeah, that was rough.

[01:23:17] **DAISY HOLMAN:** And then I wrote, wrote my talk. They moved my talk to Friday and I, and I wrote my talk during the week on something different than I was gonna present on. Really enjoyed that process. Um, [01:23:30] but, and, and, and got back up on my feet eventually, but it was, it was hard and, and I, you know, would not have done it nearly as well as I did without everyone in this community that helped me.

[01:23:41] **DAISY HOLMAN:** Um, and so I started interviewing like crazy. Interviewed a lot of different places. Um, philanthropic came along very late in the process, and I initially had no interest in working in ai. Um, [01:24:00] I had kind of missed, I thought I'd missed my opportunity to work in ai. So quantum chemistry is surprisingly closely connected to, uh, deep neural networks in large language models through the math.

[01:24:15] **DAISY HOLMAN:** Uh, I won't get into that much, but it's a lot of the same kinds of non-linear optimization techniques. Um, particularly closely related to some of the things I did in my, in my, uh, quantum chemistry, [01:24:30] my first quantum chemistry, chemistry postdoc, um, when I was studying kind of, uh, approximation methods for some small aspect of some, you know, you know, how PhDs go.

[01:24:40] **DAISY HOLMAN:** Um, but, uh, I kind of missed my opportunity to make a jump into AI around 2014. I think. I thought it was a fad. And, uh, so this time around, I, I guess I, I, I interviewed, this is gonna [01:25:00] sound dumb, I interviewed with philanthropic because a friend of mine had said that he couldn't even get past the screening.

[01:25:12] **DAISY HOLMAN:** And I said, wow, there's a challenge. I wanna see if I can get past the screening. Um, it's not the best of reasons to interview somewhere, and like it's a little embarrassing knowing what I know now. But, um, I said, why not? And I, I kind of immediately fell in [01:25:30] love with the company and the culture. Um, it is really a company full of people who wanna make a difference in the world.

[01:25:37] **DAISY HOLMAN:** Um, it's a group of the founders of the company split off of open AI because they were very concerned about the harm it was gonna do in the world and they wanted to do it differently. I think we've seen some of that. Um, won't comment on that further, but, um, 

[01:25:54] **RAY NOWOSIELSKI:** you, you sort of, 

[01:25:55] **DAISY HOLMAN:** I think it's really interesting.

[01:25:57] **DAISY HOLMAN:** I think we're gonna see, we're gonna have to see, [01:26:00] um, things are gonna change a lot, but I think there's a chance that we've really passed some sort of programming language singularity where. The quality of language features is, gets kind of balanced out by the quantity or size of the training data available.

[01:26:27] **DAISY HOLMAN:** Um, and I wouldn't say just the size, but the [01:26:30] familiarity in the training data with the language, um, kind of the universal familiarity of the language and its functionality, or there's gonna be a crossover point where, you know, programming languages at their root can all kind of do the same thing. And I think it's interesting that, you know, boost in particular provides a lot of utilities [01:27:00] that were much harder to produce on your own before the rise of age intake coating assistance.

[01:27:12] **DAISY HOLMAN:** And I wonder how much of that continues to be valuable. Um, I think it will be very interesting to see what happens. I think C++ May, many people would've said a year ago that C++ is a [01:27:30] dying programming language. I think many people still will say that. I think it might less so be the case if we have reached some sort of programming language singularity.

[01:27:46] **DAISY HOLMAN:** I think that models can write code just as happily in C++ as any other language. We can train them on C++ just as easily as we can train them on any other language. Sure. There are like little [01:28:00] knits here and there and like the verbosity of C++ is a probably a problem for its efficiency in, uh, you know.

[01:28:08] **DAISY HOLMAN:** In models and in agents, but I don't think it matters as much as we thought it did six months ago. Like I literally left my last C++ committee meeting at least for a while, um, and went directly to my first day [01:28:30] at Anthropic. I accepted the offer at the beginning of the week. Um, I have some excellent mentors at that, on that committee that I wanted to talk to first about the decision.

[01:28:42] **DAISY HOLMAN:** Um, said, Hey, I'm really leaning towards philanthropic. Philanthropic doesn't do any C++. They actually are hiring me in a rest role. So I, I got the opportunity entirely based on my C++ reputation, um, and Andros willingness to believe that, that that expertise would transfer [01:29:00] to rest. And I worked on rest at Philanthropics.

[01:29:05] **DAISY HOLMAN:** Still work a little bit on it, but. Immediately when I got there, I saw what Claude Code was doing and I said, oh, this is the most important thing this company's doing. I wanna be involved. I started doing 20% work on the project. I got a little addicted to it, and probably the first three months or so there I was working a full-time job on my normal job in a full-time job on the CLO code team trying to contribute and trying to make a dent, [01:29:30] maybe not quite a full-time job on the cloud code team, but I was doing a lot.

[01:29:33] **DAISY HOLMAN:** Um, and, and I finally got the opportunity to transfer full-time to the cloud code team. And it's been, it's been really interesting. I'm writing code and TypeScript and I'm surprised at how little it matters. It, it, I very rarely write actual type script. I kind of am starting to understand it as a language and, and in fairness, like I'm a language nerd.

[01:29:53] **DAISY HOLMAN:** I've spent my whole life studying languages in one aspect or another. Programming languages in one aspect or [01:30:00] another. Um, like I said, I wanted to be involved in the C++ committee even when I was a kid. Um, but so, so like the fact that picking up a new language that I've never worked in professionally and running with it is, is easy, is not too surprising, but it's also like, it is surprising to me how little I actually write of the language.

[01:30:22] **DAISY HOLMAN:** I write the, the ideas, and then the, the agent writes the language and like Boost [01:30:30] is in a very interesting place when that's the world we're in, right? I think carefully crafted libraries are still very important. Don't get me wrong. I think like library organization especially is still critical in terms of separating out the parts of the code that the AI has written and the parts of the code that the human has written or separating out making the, the interactions between code, uh, small enough that the AI can only mess so much of it [01:31:00] up.

[01:31:00] **DAISY HOLMAN:** And this is, this is exactly what you do with junior engineers. This is exactly what you do with intern. This is how you build software at scale, and this is something we know, right? I think the interesting thing about Boost specifically is that Boost has invested very heavily in being the library ecosystem that supports legacy users.

[01:31:21] **DAISY HOLMAN:** It supports people who can't compile on anything newer than C++ oh three, right? Like how much of the [01:31:30] Macro soup in Boost is devoted to trying to support users who have C++ oh three and can't use very arguments, right? Like there's a lot of macro soup in there. Look at eo, last time I looked at it, still supports C++ oh three.

[01:31:54] **DAISY HOLMAN:** I think that in a world where you can write a [01:32:00] prompt and seven hours later your entire ecosystem is upgraded. From oh three to 2011, um, or from 2011 to, you know, 2020, uh, C++. I think that the need for legacy software support. Now, I'm, I'm not saying that like it's the only reason people often have compilers that, like the company that Right wrote the compiler for this one piece of hardware went out of business 20 years ago, and that's why they have to use C++ oh three, [01:32:30] right?

[01:32:30] **DAISY HOLMAN:** Like, or they have one library that's a BI compatible with y, yada, yada, yada. But I think that AI does make a lot of these things less important than anything else. I also think that AI makes kind of language zealotry a little bit more laughable, [01:33:00] I think. If you're to some extent, we had a very long time where developers were kind of, um, especially junior developers, were partitioned off by the languages that they, they knew, right?

[01:33:18] **DAISY HOLMAN:** Oh, I'm a C++ developer. I'm looking for C++ jobs. And I think the future looks more like I'm a software engineer. I'm looking for software [01:33:30] engineering jobs, and the language just happens to be the thing that the model spits out and that you read. But like, reading a language is much, much easier than writing it.

[01:33:44] **DAISY HOLMAN:** And writing it is much easier than writing it. Well, but that's another discussion, right? Um, sorry. But, uh, yeah, I think that, that, that is, I, I, I do think there's a place [01:34:00] for. Highly crafted, well-crafted libraries. I think that Boost may or may not have survived to this singularity point where like, you know, I was talking about how to some extent the quality of the, or the features in the language or in the library are maybe less critical relative to the amount of [01:34:30] use and the widespread ness widespread.

[01:34:34] **DAISY HOLMAN:** There's, I've been talking for a long time, I'm sorry. Um, 

[01:34:38] **RAY NOWOSIELSKI:** machine returns after two hours, it's gone. 

[01:34:40] **DAISY HOLMAN:** Yeah, but it's, what, what I'm saying is that like Boost is very popular and it's possible that at least portions of Boost have survived to this singularity where AI has, agents have so much of it in their training data.[01:35:00] 

[01:35:00] **DAISY HOLMAN:** That they are more efficient with it than something that's maybe more modern, more well designed, um, or like redesigned from scratch without all of these legacy concerns that Boost prioritizes. Um, but it's just not as present in the training data because it hasn't been used as widely. Right. I think that there's, there's, there's an interesting discussion to be had there, and I think we're gonna have to see how that plays out over the [01:35:30] next year.

[01:35:30] **DAISY HOLMAN:** I think it's also possible that agents take a direction in which their training doesn't need large volumes of training data. It only needs kind of smaller volumes of high quality data. And in that world, I don't think the singularity exists. And, and so this is an open question. This is an open question in the future of software engineering.

[01:35:58] **DAISY HOLMAN:** This is an open question [01:36:00] in the future of library development and programming languages. Um, and it's really an exciting time to be alive because the field of developer experience has changed more in the past six months than in the past 25 years before that. And I don't think it's all that controversial to say that like, I think most experts in developer experience, which is kind of this parent field of programming languages, um, [01:36:30] would agree with that statement.

[01:36:33] **DAISY HOLMAN:** And so like, what does the next six months look like? How in the world do you predict that when you have that rate of change? And how lucky are we that we get to live? Like how many people get to live through a six month period that's more influential than 25 years before in their field? Like imagine living through that period in documentary filmmaking focus, never stop being curious.

[01:36:58] **DAISY HOLMAN:** Like, I think [01:37:00] that's the story of my career is that I was a, a quantum chemist using C++, and then was curious about how the libraries worked and wanted to improve on them. And then I was curious about how the language worked and then I was curious about how the standardization process worked.

[01:37:19] **DAISY HOLMAN:** And I've always been quite curious about ai. Um, I, I missed one opportunity to pivot into the field and I wasn't gonna miss my, my next one. And, [01:37:30] um, I think, I genuinely think I am lucky in that I have had the opportunities to pursue the things that I am curious about. And, and there's a lot of, of privilege in that statement to be clear.

[01:37:47] **DAISY HOLMAN:** But if you get the opportunities to do the things you're curious about professionally, uh, take them. Like it, it will [01:38:00] make you happier, right? Um, I mean, that's a big statement, but like, it has made me happier. Um, I think letting your curiosity drive your, um, career is not the best way to make a billion dollars, but I think it's a great way to end up in a place [01:38:30] where you experience a lot of fulfillment, right?

[01:38:36] **DAISY HOLMAN:** Um, and find out what, find out what drives you. Find out what I like to say. Find out what gets, gets you out of the bed. Find out what gets you out of bed in the morning and find out what helps you get to sleep at night. What can you do that will get you outta the bed in the morning and still lets you sleep at night?

[01:38:57] **DAISY HOLMAN:** One of those is happiness, one of those is [01:39:00] fulfillment, right? And between those two things, I think you can chase curiosity and let curiosity take you along that spectrum to the spot where you really feel the most comfortable. I think I'm career-wise, facing a really interesting spot where I'm, you know, learning that I fall into a area that's much closer [01:39:30] to, um, curiosity driven work, regardless of the pay.

[01:39:40] **DAISY HOLMAN:** And I get paid plenty, well, don't get me wrong, but it's not as much as I could be making other places. That's a really uncomfortable thing to learn. That's a really uncomfortable thing to learn about yourself at this age when you, you're like, wow, if, if this current opportunity, which really I'm at this awesome, like, it's [01:40:00] basically just, you know, it's a think tank.

[01:40:01] **DAISY HOLMAN:** It's a research lab and it's kind of, sort of a company also. Um, and like, what if this experiment in doing the right thing in AI and trying to make money with it doesn't pay off? Where am I going next? Like, what if the company doesn't pay off as, as an entity? And I think I kind of knew this at Google and I was scared to make the step, but I [01:40:30] think it means that I end up in academia.

[01:40:33] **DAISY HOLMAN:** Um, so like there could be more twists, but happiness comes from a wide variety of things. And if you get the opportunity to pursue. One of those things that makes you happy professionally. Don't let it pass you by, and that's what I'd say.

