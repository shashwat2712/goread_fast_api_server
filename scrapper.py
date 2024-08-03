from newspaper import Article
import nltk
import requests
from duckduckgo_search import DDGS

nltk.download('punkt')
def scrape_article(url)  -> dict:
    try :
        url = DDGS().text(url, max_results=1)
        article = Article(url[0]['href'])
        article.download()
        article.parse()
        print(article.text)
        article.nlp()
        return {
            'title': article.title,
            'authors': article.authors,
            'publish_date': article.publish_date,
            'text': article.text,
            'summary': article.summary,
            'keywords': article.keywords,
            'image' : article.top_image
        }
    except requests.RequestException as e:
        return {"error": str(e)}
    


# url = 'https://www.linkedin.com/in/shashwat-sai-vyas-92395a224/'
# print(url)
# article_data = scrape_article(url)
# print(article_data['text'])
str1 = '''{
  "latest_news": [
    {
      "title": "Toll rises to 108, at least 128 people injured",
      "authors": [
        "Hariharan S"
      ],
      "publish_date": "2024-07-30T11:10:50",
      "text": "Wayanad Landslides Highlights: Kerala Chief Minister Pinarayi Vijayan confirmed in a press conference on Tuesday evening that 93 bodies have been recovered so far after multiple landslides triggered by heavy monsoon rain in the Wayanad district. Kerala government announced that two days, July 30 and 31, will be observed as state mourning. All state government programmes have been deferred....Read More\n\nMultiple landslides triggered by pounding monsoon rains have killed many with hundreds more feared trapped under mud and debris in Kerala's hill district of Wayanad on Tuesday. The Indian Meteorological Department (IMD) had forecast heavy rain for the district.\n\nThe Indian Army was roped in as a temporary bridge that linked the affected area to a nearest town was also destroyed. The Army has mobilised four columns, including two columns ex 122 Infantry Battalion (Territorial Army) and two ex the DSC Centre, Kannur.\n\nTwo helicopters of the Indian Air Force have also been mobilised, said a statement from Kerala chief minister Pinarayi Vijayan's office.\n\nA rescue official said rescue efforts remain challenging as there was no internet connectivity in the area.\n\nAlso read | Wayanad landslide: 84 dead, rescue teams face rain, terrain challenges | 10 points\n\nState forest minister AK Saseendran said that the situation is serious, and the government has pressed all agencies to assist rescue operations.\n\nA special control room has been set up by the district administration at the police headquarters in Thiruvananthapuram.\n\nPrime Minister Narendra Modi spoke to Kerala chief minister Pinarayi Vijayan and assured all possible help from the Centre.\n\n\"The Prime Minister has announced ex-gratia of ₹2 lakh from Prime Minister's National Relief Fund (PMNRF) for the next of kin of each deceased in the landslides in parts of Wayanad,\" PM's office said in a post on X. The injured would be given ₹50,000.\n\nFollow live updates here",
      "summary": "Wayanad Landslides Highlights: Kerala Chief Minister Pinarayi Vijayan confirmed in a press conference on Tuesday evening that 93 bodies have been recovered so far after multiple landslides triggered by heavy monsoon rain in the Wayanad district.\nKerala government announced that two days, July 30 and 31, will be observed as state mourning.\nTwo helicopters of the Indian Air Force have also been mobilised, said a statement from Kerala chief minister Pinarayi Vijayan's office.\nA rescue official said rescue efforts remain challenging as there was no internet connectivity in the area.\nPrime Minister Narendra Modi spoke to Kerala chief minister Pinarayi Vijayan and assured all possible help from the Centre.",
      "keywords": [
        "injured",
        "district",
        "128",
        "rises",
        "rescue",
        "rain",
        "pinarayi",
        "landslides",
        "kerala",
        "minister",
        "wayanad",
        "108",
        "indian",
        "chief",
        "toll"
      ],
      "image": "https://images.hindustantimes.com/img/2024/07/30/550x309/Screenshot_2024-07-30_171237_1722339768992_1722339779127.png"
    },
    {
      "title": "10 Incredible Sea Creatures That Look Straight Out of a Fantasy",
      "authors": [],
      "publish_date": null,
      "text": "With its dark red color, cloak-like webbing between its arms, and bioluminescent capabilities, the vampire squid looks like it could be a creature of the night. Despite itAs menacing appearance, it primarily feeds on detritus in the deep sea.",
      "summary": "With its dark red color, cloak-like webbing between its arms, and bioluminescent capabilities, the vampire squid looks like it could be a creature of the night.\nDespite itAs menacing appearance, it primarily feeds on detritus in the deep sea.",
      "keywords": [
        "sea",
        "looks",
        "primarily",
        "menacing",
        "look",
        "webbing",
        "incredible",
        "itas",
        "straight",
        "squid",
        "vampire",
        "creatures",
        "fantasy",
        "red",
        "night"
      ],
      "image": "https://images.news18.com/webstories/uploads/2024/07/cropped-Sheetal-Kumari-1-2024-07-21028a07b2f5264f0f57a63c8c4427af.jpg"
    },
    {
      "title": "Olympic Games Paris 2024 Highlights Day 4: Manu Bhaker-Sarabjot Singh Win Bronze, Archer Bhajan Shines",
      "authors": [
        "Ndtv Sports Desk"
      ],
      "publish_date": null,
      "text": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennis\n\nEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\n\n\n\n\n\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\n\n\n\n\n\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
      "summary": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennisEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
      "keywords": [
        "shines",
        "paris",
        "late",
        "highlights",
        "singh",
        "games",
        "strike",
        "manu",
        "surprise",
        "superb",
        "egypt",
        "olympic",
        "win",
        "bronze",
        "group",
        "tennisegypt",
        "spain",
        "day",
        "stunning"
      ],
      "image": "https://c.ndtvimg.com/2024-07/27vcqib8_manu-bhaker-and-sarabjot-singh_625x300_30_July_24.jpeg?im=FitAndFill,algorithm=dnn,width=1200,height=738"
    },
    {
      "title": "Nasa finishing work on Nisar mission but Isro can't launch it till February 2025",
      "authors": [],
      "publish_date": "2024-07-30T00:00:00",
      "text": "Nasa's work on the radar antenna reflector for the Nasa-Isro Synthetic Aperture Radar (Nisar) satellite is nearing completion in California.\n\nThe American space agency said that the testing is currently underway to ensure that this critical hardware component will deploy correctly following its launch from India.\n\nNisar mission represents a significant collaboration between Nasa and Isro, combining the expertise and resources of both organizations to advance our understanding of Earth's dynamic systems.\n\nadvertisement\n\nThe drum-shaped reflector, measuring about 39 feet (12 meters) across, is one of Nasa’s key contributions to this joint mission with the Indian Space Research Organisation (Isro).\n\nThe reflector is designed to transmit and receive microwave signals to and from Earth's surface, enabling Nisar to scan nearly all the planet’s land and ice surfaces twice every 12 days to gather essential scientific data. The reflector will be reintegrated with the radar system by teams from Nasa’s Jet Propulsion Laboratory. (Photo: Nasa)\n\nThis capability will provide valuable insights into various Earth processes, including ecosystem disturbances, ice-sheet collapse, and natural hazards such as earthquakes, tsunamis, and landslides.\n\nIn March, the reflector was transported back from India to a specialised facility in California. There, reflective tape was applied, and other precautionary measures were taken to mitigate temperature increases that could potentially affect the deployment of the reflector from its stowed configuration before beginning science operations.\n\nAfter the successful completion of testing, Nasa plans to transport the reflector to an Isro facility in Bengaluru, India.\n\nAt this facility, the reflector will be reintegrated with the radar system by teams from Nasa’s Jet Propulsion Laboratory in Southern California and Isro. During this period, a launch readiness date will be determined by Isro in coordination with Nasa.\n\nHowever, it is important to note that the Nisar launch cannot occur between early October 2024 and early February 2025. Nasa said that launching during this window would subject the satellite to periods of alternating sunlight and shadows due to the Sun's position, causing temperature fluctuations that could affect the deployment of Nisar’s boom and radar antenna reflector.\n\nOnce operational, Nisar will provide unprecedented data to help scientists monitor and respond to environmental changes and natural disasters, ultimately contributing to global efforts in climate science and disaster management.\n\n",
      "summary": "Nasa's work on the radar antenna reflector for the Nasa-Isro Synthetic Aperture Radar (Nisar) satellite is nearing completion in California.\nNisar mission represents a significant collaboration between Nasa and Isro, combining the expertise and resources of both organizations to advance our understanding of Earth's dynamic systems.\nAfter the successful completion of testing, Nasa plans to transport the reflector to an Isro facility in Bengaluru, India.\nDuring this period, a launch readiness date will be determined by Isro in coordination with Nasa.\nHowever, it is important to note that the Nisar launch cannot occur between early October 2024 and early February 2025.",
      "keywords": [
        "launch",
        "nasas",
        "cant",
        "2025",
        "temperature",
        "isro",
        "reflector",
        "radar",
        "testing",
        "till",
        "facility",
        "finishing",
        "work",
        "nasa",
        "nisar",
        "mission"
      ],
      "image": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202407/nisar-mission-testing-launch-111755932-16x9.jpg?VersionId=1R9Wh1zqCCzyD64j4L5Tt4pPtiD8j3A8"
    },
    {
      "title": "MSN",
      "authors": [],
      "publish_date": null,
      "text": "",
      "summary": "",
      "keywords": [
        "msn"
      ],
      "image": ""
    },
    {
      "error": "Article `download()` failed with 401 Client Error: HTTP Forbidden for url: https://www.reuters.com/world/india/india-not-rethinking-issue-allowing-chinese-investment-trade-minister-says-2024-07-30/ on URL https://www.reuters.com/world/india/india-not-rethinking-issue-allowing-chinese-investment-trade-minister-says-2024-07-30/"
    },
    {
      "title": "Kriti Sanon’s smoking video goes viral; Mother Geeta Sanon’s old tweet resurfaces : Bollywood News",
      "authors": [
        "Bollywood Hungama",
        "Bollywood Hungama News Network",
        "Https",
        "Www.Bollywoodhungama.Com"
      ],
      "publish_date": "2024-07-31T10:01:26",
      "text": "Kriti Sanon was recently seen celebrating her birthday in Greece with her friends and sister. However, a video from her vacation showing her smoking cigarettes has gone viral on social media. The video quickly spread, igniting a heated debate among netizens. Some defended Kriti, arguing that it's inappropriate to film celebrities during their private moments. One comment read, \"Let her live her life and enjoy her vacation. What is the fuss here I don't know.\" Meanwhile, others called her a hypocrite due to her previously stated stance against smoking.\n\nKriti Sanon’s smoking video goes viral; Mother Geeta Sanon’s old tweet resurfaces\n\nGeeta Sanon's old tweet resurfaces\n\nAmid the controversy, an old tweet by Kriti Sanon's mother, Geeta Sanon, has resurfaced. In response to a fan's post about Kriti smoking for her role in Bareilly Ki Barfi, Geeta had tweeted, \"She has always been anti-smoking and always asked people around her to quit smoking.\" This tweet has reignited discussions about Kriti's personal choices versus her public statements. The resurfaced tweet has added fuel to the debate, with many questioning the authenticity of Kriti's anti-smoking stance.\n\nRumors of a new relationship\n\nAdding to the buzz, there are also rumors about Kriti Sanon being in a relationship with a US-based businessman named Kabir Bahia. Photos from their Greece vacation have circulated online, but neither Kriti nor Kabir have addressed the relationship rumors publicly. The speculation about her personal life continues to intrigue fans and followers.\n\nKriti Sanon's professional milestones\n\nDespite the personal controversies, Kriti Sanon has been making significant strides in her career. She recently impressed audiences with her performance in the film Crew, which turned out to be a success. Kriti's next project is Do Patti, a movie she is also producing. This film marks her second collaboration with Kajol after Dilwale and is currently in production. Her professional achievements continue to garner praise, highlighting her talent and dedication to her craft.\n\nAlso Read: Happy Birthday Kriti Sanon: 5 times the actress wowed us with her saree look\n\nBOLLYWOOD NEWS - LIVE UPDATES\n\nCatch us for latest Bollywood News, New Bollywood Movies update, Box office collection, New Movies Release , Bollywood News Hindi, Entertainment News, Bollywood Live News Today & Upcoming Movies 2024 and stay updated with latest hindi movies only on Bollywood Hungama.",
      "summary": "Kriti Sanon was recently seen celebrating her birthday in Greece with her friends and sister.\nKriti Sanon’s smoking video goes viral; Mother Geeta Sanon’s old tweet resurfacesGeeta Sanon's old tweet resurfacesAmid the controversy, an old tweet by Kriti Sanon's mother, Geeta Sanon, has resurfaced.\nIn response to a fan's post about Kriti smoking for her role in Bareilly Ki Barfi, Geeta had tweeted, \"She has always been anti-smoking and always asked people around her to quit smoking.\"\nRumors of a new relationshipAdding to the buzz, there are also rumors about Kriti Sanon being in a relationship with a US-based businessman named Kabir Bahia.\nKriti Sanon's professional milestonesDespite the personal controversies, Kriti Sanon has been making significant strides in her career.",
      "keywords": [
        "old",
        "resurfaces",
        "sanon",
        "sanons",
        "kriti",
        "movies",
        "vacation",
        "bollywood",
        "video",
        "viral",
        "mother",
        "personal",
        "geeta",
        "goes",
        "smoking"
      ],
      "image": "https://stat4.bollywoodhungama.in/wp-content/uploads/2024/07/Kriti-Sanons-smoking-video-goes-viral-Mother-Geeta-Sanons-old-tweet-resurfaces-1.jpg"
    },
    {
      "title": "SpaceX's historic Polaris Dawn astronaut mission delayed until mid-August",
      "authors": [
        "Mike Wall",
        "Senior Space Writer",
        "Social Links Navigation"
      ],
      "publish_date": "2024-07-26T21:00:26",
      "text": "We'll all have to wait a bit longer to see the first-ever private spacewalk.\n\nSpaceX is now targeting mid- to late August for the launch of Polaris Dawn, a mission funded by billionaire entrepreneur Jared Isaacman. The upcoming flight, which will employ SpaceX's Crew Dragon spacecraft and Falcon 9 rocket, had been slated to lift off no earlier than July 31.\n\nSpaceX announced the delay today (July 26), during a press conference focusing on the company's upcoming Crew-9 astronaut mission to the International Space Station (ISS) for NASA. Crew-9 will launch no earlier than Aug. 18, and Polaris Dawn will fly sometime after that, the company said.\n\n\"There's a lot going on on ISS right now,\" Sarah Walker, SpaceX's director of Dragon mission management, said during today's press conference. \"We opted to fly the Crew-9 mission as our next [astronaut] mission and are ready to fly Polaris Dawn in late summer, as soon as we fulfill those obligations.\"\n\nTurns out we have a little bit of time before Polaris Dawn launches, so I will be attending in person. Thanks for the invite @teslaownersSV https://t.co/VHNSeHajM8July 25, 2024\n\nLater in the press conference, Walker clarified that \"late summer\" means next month: \"Right now, we're still planning to launch Polaris Dawn in August.\"\n\nRelated: How SpaceX's private Polaris Dawn astronauts will attempt the 1st-ever 'all-civilian' spacewalk\n\nPolaris Dawn is the first of three planned missions in the Polaris Program , all of which will be funded and commanded by Isaacman. He did the same for SpaceX's pioneering Inspiration4 mission, which carried Isaacman and three crewmates to Earth orbit in September 2021.\n\nGet the Space.com Newsletter Breaking space news, the latest updates on rocket launches, skywatching events and more! Contact me with news and offers from other Future brands Receive email from us on behalf of our trusted partners or sponsors\n\nThe Polaris Dawn crew consists of Isaacman, pilot Scott \"Kidd\" Poteet, a retired U.S. Air Force lieutenant colonel; and mission specialists Sarah Gillis and Anna Menon, both of whom are engineers at SpaceX.\n\nLike Inspiration4, Polaris Dawn will be a free flyer, zipping around Earth solo rather than linking up with the ISS. But the coming mission will go higher than its predecessor and feature at least one spacewalk — the first-ever private extravehicular activity.\n\nThis isn't the first delay for Polaris Dawn; originally slated to fly in late 2022, the complex and ambitious mission has been pushed back multiple times.\n\nToday's press conference came just 15 days after a rare Falcon 9 mishap. The rocket's upper stage failed to complete a planned orbit-raising burn during a July 11 launch, resulting in the loss of the payloads — 20 of SpaceX's Starlink internet satellites.\n\nThe proximate cause was a leak of liquid oxygen. SpaceX traced that issue to a crack in a line for a pressure sensor in the upper stage's liquid-oxygen system, and has taken measures to ensure the problem won't recur. In fact, the Falcon 9 is slated to bounce back early Saturday morning (July 27), with another Starlink launch.",
      "summary": "SpaceX is now targeting mid- to late August for the launch of Polaris Dawn, a mission funded by billionaire entrepreneur Jared Isaacman.\nCrew-9 will launch no earlier than Aug. 18, and Polaris Dawn will fly sometime after that, the company said.\n\"We opted to fly the Crew-9 mission as our next [astronaut] mission and are ready to fly Polaris Dawn in late summer, as soon as we fulfill those obligations.\"\nTurns out we have a little bit of time before Polaris Dawn launches, so I will be attending in person.\nLike Inspiration4, Polaris Dawn will be a free flyer, zipping around Earth solo rather than linking up with the ISS.",
      "keywords": [
        "launch",
        "late",
        "isaacman",
        "delayed",
        "astronaut",
        "polaris",
        "press",
        "dawn",
        "historic",
        "fly",
        "midaugust",
        "mission",
        "spacexs",
        "conference"
      ],
      "image": "https://cdn.mos.cms.futurecdn.net/RcxpQm9zPPNBHC3hTSeepH-1200-80.jpg"
    },
    {
      "error": "Article `download()` failed with 404 Client Error: Not Found for url: https://www.ndtv.com/entertainment/shah-rukh-khan-flies-to-us-for-an-eye-surgery-6220906 on URL https://www.ndtv.com/entertainment/shah-rukh-khan-flies-to-us-for-an-eye-surgery-6220906"
    },
    {
      "title": "Jharkhand train updates: 2 killed, 20 injured as 18 coaches derail in Jharkhand",
      "authors": [
        "Authors"
      ],
      "publish_date": "2024-07-30T04:02:34",
      "text": "July 30, 2024 12:18\n\nYet another rail accident but ‘PR machine of Fail Minister’ continues: Congress\n\nThe Congress on Tuesday took a swipe at Railway Minister Ashwini Vaishnaw after the train derailment in Jharkhand, saying since June the “Fail Minister” has “overseen three accidents” that have cumulatively cost 17 lives but there is “no accountability” in Prime Minister Narendra Modi’s new India.\n\nCongress general secretary in-charge communications Jairam Ramesh said in a post on X, “Yet another railway accident. But the PR machine of the Fail Minister continues.” “In June and July 2024 alone, the Fail Minister has overseen three accidents that have cumulatively cost 17 Indians their lives and left 100s injured,” he said, hitting out at Mr. Vaishnaw.\n\nCongress’ media and publicity department head Pawan Khera said, “Train Accidents: A Weekly Reality in Modi’s New India.” “July 18: Train accident in Gonda, UP: Chandigarh-Dibrugarh Express: 4 killed, 31 injured. July 19: Goods train derailed in Valsad, Gujarat. July 20: 12 wagons of a freight train derailed in Amroha, UP. July 21: 3 wagons of a goods train derailed in Alwar, Rajasthan. July 21: Goods train derailed in Ranaghat, West Bengal. July 26: Goods train derailed at Bhubaneswar Railway Station, Orissa. July 29: Bihar Sampark Kranti Express detached from other coaches in Samastipur, Bihar. July 30: Several coaches of the Howrah-CSMT Express train derailed in Chakradharpur, Jharkhand: 2 killed, 20 injured,” he said.\n\nIn the usual aftermath, Mr. Vaishnaw would visit the site with his PR team by evening and will upload a reel by tomorrow, Mr. Khera said, taking a dig at the Railway Minister.\n\n“In Modi’s new India, there is no accountability, no resignations, only grandiose talks about irrelevant rail projects that no one uses,” he said.",
      "summary": "July 19: Goods train derailed in Valsad, Gujarat.\nJuly 20: 12 wagons of a freight train derailed in Amroha, UP.\nJuly 21: 3 wagons of a goods train derailed in Alwar, Rajasthan.\nJuly 21: Goods train derailed in Ranaghat, West Bengal.\nJuly 30: Several coaches of the Howrah-CSMT Express train derailed in Chakradharpur, Jharkhand: 2 killed, 20 injured,” he said.",
      "keywords": [
        "updates",
        "railway",
        "injured",
        "18",
        "20",
        "goods",
        "mr",
        "jharkhand",
        "train",
        "pr",
        "killed",
        "minister",
        "coaches",
        "modis",
        "fail",
        "derailed",
        "derail"
      ],
      "image": "https://th-i.thgim.com/public/incoming/u9t69p/article68463284.ece/alternates/LANDSCAPE_1200/AFP_366F23W.jpg"
    },
    {
      "title": "Realme 13 Pro Series LIVE 2024 Updates: Realme claims its AI-powered camera rivals DSLR cameras",
      "authors": [
        "Authors"
      ],
      "publish_date": "2024-07-30T06:30:56",
      "text": "Realme launched the Realme 13 Pro+ 5G and Realme 13 Pro 5G phones after weeks of teasers and unveiling its AI-powered camera, on July 30 at noon. The event also saw the launch of the Realme Watch S2 and Realme Buds T310.\n\nThe company is aiming to conquer the mid-segment and high-end smartphone markets, and has hailed India’s community of young smartphone users.\n\nAlso Read:Realme to launch 13 Pro series 5G phones this week: specs, features, what to expect\n\nThis live blog is now closed",
      "summary": "Realme launched the Realme 13 Pro+ 5G and Realme 13 Pro 5G phones after weeks of teasers and unveiling its AI-powered camera, on July 30 at noon.\nThe event also saw the launch of the Realme Watch S2 and Realme Buds T310.\nThe company is aiming to conquer the mid-segment and high-end smartphone markets, and has hailed India’s community of young smartphone users.\nAlso Read:Realme to launch 13 Pro series 5G phones this week: specs, features, what to expectThis live blog is now closed",
      "keywords": [
        "updates",
        "launch",
        "cameras",
        "live",
        "13",
        "week",
        "smartphone",
        "young",
        "dslr",
        "camera",
        "rivals",
        "5g",
        "claims",
        "phones",
        "realme",
        "series",
        "pro",
        "weeks"
      ],
      "image": "https://th-i.thgim.com/public/sci-tech/technology/y6l35c/article68463601.ece/alternates/LANDSCAPE_1200/thumbnail_image002.jpg"
    },
    {
      "title": "Asim Riaz fans defend him after he's kicked out of Khatron Ke Khiladi 14: 'Self respect always comes first'",
      "authors": [],
      "publish_date": "2024-07-30T11:56:28",
      "text": "What did Asim Riaz actually do on KKK14?\n\nRecently, Asim was unceremonious eliminated from Khatron Ke Khiladi Season 14. After a challenge he called impossible – asking the Khatron Ke Khiladi team to perform it in front of him – Asim got into a fight with someone from the show's team and said that he 'won’t take a rupee' from them. He also called his co-contestants 'losers' and was in turn called rude by Rohit. Asim, who was seen on Bigg Boss 13 in 2019, later apologised after seeing the rehearsal video of the task he failed to perform.\n\n'We are with you Asim'\n\nHis fans on X are now trending 'We are with you Asim' and defending the Kashmiri model after backlash over him 'disrespecting' Khatron Ke Khiladi co-contestants, the makers and the host.\n\nA fan tweeted on Tuesday, \"Self respect always comes first. @imrealasim keep shining bright! Your strength and dignity are truly inspiring! WE ARE WITH YOU ASIM.\" Another said, \"Asim Riaz has clearly said it: apology should be loud as disrespect. Proud to be supporting someone that know is worth PS: People disrespect in public but apologises in private.\"\n\nA fan also tweeted a clip from the show, and said, \"Rohit Shitty: 'Sun meri baat warna idhar hi uthaake patak dunga (Listen to me or else I will beat you)'. Sigma male Asim Riaz coming in front him.@Colors show us unedited version of episode. WE ARE WITH YOU ASIM.\" Another tweet read, \"Asim Riaz is dominating the trends, with his fans showing strong support. The hype around him on the show is real!\"\n\nKhatron Ke Khiladi Season 14's fresh episodes stream on JioCinema and air on ColorsTV every Saturday and Sunday.",
      "summary": "What did Asim Riaz actually do on KKK14?\nRecently, Asim was unceremonious eliminated from Khatron Ke Khiladi Season 14.\nAnother said, \"Asim Riaz has clearly said it: apology should be loud as disrespect.\nAnother tweet read, \"Asim Riaz is dominating the trends, with his fans showing strong support.\nKhatron Ke Khiladi Season 14's fresh episodes stream on JioCinema and air on ColorsTV every Saturday and Sunday.",
      "keywords": [
        "kicked",
        "season",
        "hes",
        "rohit",
        "self",
        "tweeted",
        "respect",
        "khiladi",
        "defend",
        "called",
        "team",
        "ke",
        "riaz",
        "fans",
        "asim",
        "khatron"
      ],
      "image": "https://images.hindustantimes.com/img/2024/07/30/1600x900/Asim_Riaz_KKK_14_rohit_shetty_1722319839421_1722319839767.jpg"
    },
    {
      "title": "Gemini’s big upgrade: Faster responses with 1.5 Flash, expanded access and more",
      "authors": [
        "Amar Subramanya",
        "Vice President",
        "Engineering",
        "Gemini Experiences",
        "Molly Mchugh-Johnson",
        "Marvin Chow",
        "Menaka Shroff",
        "Shantanu Sinha",
        "Akshay Kirtikar",
        "Brian Hendricks"
      ],
      "publish_date": "2024-07-25T00:00:00",
      "text": "Every day, we learn about how people are using Gemini to be more productive, creative and curious. And with today’s update, Gemini is getting better at helping you accomplish those tasks in ways that work best for you.\n\nYou can now access 1.5 Flash in the unpaid version of Gemini for faster and more helpful responses. Plus, we’re introducing a new feature to further address hallucinations, and expanding our Gemini for Teens experience and mobile app to more places.\n\nFaster, smarter responses with 1.5 Flash\n\nWe’ve heard that one of the main reasons people enjoy using Gemini is because it saves time. Whether you’re using Gemini to write a compelling email or debug tricky code, it’s important to get fast, high-quality responses.\n\nToday we’re upgrading our free-tier experience to Gemini 1.5 Flash. With Gemini 1.5 Flash, you’ll notice across-the-board improvements in quality and latency, with especially noticeable improvements in reasoning and image understanding. And just like we greatly expanded the context window in Gemini Advanced, we’re quadrupling Gemini’s to 32K tokens. That means you can have longer back-and-forth conversations and ask Gemini more complex questions — all free of charge.\n\nTo get the most out of the larger context window, we’ll soon add the ability to upload files via Google Drive or directly from your device, which has been available in Gemini Advanced. That means you’ll be able to do things like upload your economics study guide and ask Gemini to create practice questions. Gemini will also soon be able to analyze data files for you, allowing you to uncover insights and visualize them through charts and graphics.",
      "summary": "Every day, we learn about how people are using Gemini to be more productive, creative and curious.\nYou can now access 1.5 Flash in the unpaid version of Gemini for faster and more helpful responses.\nFaster, smarter responses with 1.5 FlashWe’ve heard that one of the main reasons people enjoy using Gemini is because it saves time.\nToday we’re upgrading our free-tier experience to Gemini 1.5 Flash.\nWith Gemini 1.5 Flash, you’ll notice across-the-board improvements in quality and latency, with especially noticeable improvements in reasoning and image understanding.",
      "keywords": [
        "expanded",
        "responses",
        "big",
        "soon",
        "upgrade",
        "questions",
        "faster",
        "youll",
        "geminis",
        "gemini",
        "15",
        "access",
        "flash",
        "window",
        "upload",
        "using"
      ],
      "image": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_SS_New.width-1300.jpg"
    },
    {
      "error": "https://links.duckduckgo.com/d.js Exception: Error in request: error sending request for url (https://links.duckduckgo.com/d.js?q=NASA+on+alert+as+150-foot+asteroid+set+to+come+%60deathly%60+close+to+Earth.+If+it+hits+the+planet+it+can...+-+WION&kl=wt-wt&l=wt-wt&p=&s=0&df=&vqd=4-163802851719982952494578410122720457348&bing_market=wt-WT&ex=-1): operation timed out"
    },
    {
      "error": "https://links.duckduckgo.com/d.js Exception: Error reading response bytes: request or response body error: operation timed out"
    },
    {
      "title": "Wobbly SL look for respite against red-hot India",
      "authors": [],
      "publish_date": null,
      "text": "Having already sealed the series, India will be hoping to give the likes of Rinku, Samson and Parag more time in the middle\n\nBig picture: Sri Lanka's middle-order worries\n\nIn the first T20I, Sri Lanka lost nine wickets for 30 runs. In the second, they lost seven for 32. This has been the theme for the hosts so far in Charith Asalanka's first series as Sri Lanka's full-time T20I captain. Asalanka himself managed just scores of 0 and 14 in the two games.\n\nThe top three have fired in both matches, with Sri Lanka getting to scores of 140 and 80 at the fall of the second wicket. Pathum Nissanka is the leading run-scorer in the series. Kusal Perera has a half-century, while Kusal Mendis made 45 in the first match. But beyond them, it has been a bleak showing, with Kamindu Mendis' 26 in the second T20I the highest score from the middle and lower orders.\n\nSri Lanka will need to find a way out of their middle-order muddle and deliver on the platform being set by their top order.\n\nIndia would want some of their batters like Sanju Samson, Rinku Singh and Riyan Parag to get some more time in the middle, and having sealed the series with comprehensive performances, don't have too much else they need to address.\n\nForm guide\n\nSri Lanka LLWLL (Last five completed T20Is, most recent first)\n\n\n\nIndia WWWWW\n\nIn the spotlight - Pathum Nissanka and Rishabh Pant\n\nPathum Nissanka is the only batter to have gone past 100 runs in the series, and is striking at 154.16. He has been in sensational form in 2024, having scored 753 runs at a strike rate of 154.93 - well above his career strike rate of 123.90. He shone in the Lanka Premier League as well, and was the highest-scoring opener in the competition. With their wobbly middle order, the onus is on him now more than ever to keep producing big performances with the bat.\n\nAfter a life-threatening accident, Rishabh Pant made his return to competitive cricket in IPL 2024, and following a successful campaign, he was picked for the 2024 T20 World Cup. He made 42 off 31 in a low-scoring win over Pakistan, but failed to convert his starts after that, even as India went on to lift the title. In the first game of this series, Pant made 49 off 33, but he had a scratchy start and was dropped on 11. With Sanju Samson behind him in the pecking order, there is pressure on Pant to prove his credentials in the shortest format for India.\n\nTeam news\n\nSri Lanka are likely to play a similar XI to the one that turned out in the second game. However, one of Avishka Fernando or Dinesh Chandimal could come in for the misfiring Dasun Shanaka, who has three ducks in his last three T20Is. They brought in Ramesh Mendis for Dilshan Madushanka, with Asalanka claiming spin would get more help on a used surface, but in a rain curtailed game, Ramesh was not used at all. However, even though this match will be played on a fresh pitch, Sri Lanka are likely to continue with Ramesh, as he adds batting depth as well.\n\nSri Lanka (probable XI): 1. Pathum Nissanka, 2. Kusal Mendis (wk), 3. Kusal Perera, 4. Kamindu Mendis, 5. Charith Asalanka (capt), 6. Dinesh Chandimal/Avishka Fernando, 7. Wanindu Hasaranga, 8. Ramesh Mendis, 9. Maheesh Theekshana, 10. Matheesha Pathirana, 11. Asitha Fernando\n\nHaving played two matches in two days, India may rest one of the fast bowlers, with Khaleel Ahmed waiting in the wings. Washington Sundar could get a game as well, if India continue with the trend of trying to give a match to every squad member on a tour if possible, which was prevalent in Rahul Dravid's tenure. Shivam Dube also could come in, but with Hardik Pandya not a part of the ODI squad, India may just stick with him so as to not chop and change too much. There is also no news on Shubman Gill, who missed the second game with a neck spasm. With Gill also set to play in the ODIs, India could persist with Samson, who was out first ball in the second T20I.\n\nIndia (probable XI): 1. Yashasvi Jaiswal, 2. Sanju Samson, 3. Suryakumar Yadav (capt), 4. Rishabh Pant (wk), 5. Riyan Parag/Washington Sundar, 6. Hardik Pandya, 7. Rinku Singh, 8. Axar Patel, 9. Ravi Bishnoi, 10. Mohammed Siraj, 11. Arshdeep Singh/Khaleel Ahmed\n\nRishabh Pant will be looking to make more of his opportunities in the shortest format • Associated Press\n\nPitch and conditions\n\nAfter two matches on the same pitch, this game will be played on a fresh surface in Pallekele. In the first two matches, batting conditions were the best earlier on and got tougher as the match progressed, bringing spinners into play and encouraging changes of pace from the quicks. The new pitch is not expected to play too differently.\n\nStats and trivia\n\nMatheesha Pathirana has dismissed Suryakumar Yadav in all three T20 innings he has bowled to him. Sri Lanka could be encouraged to introduce Pathirana to the attack earlier than usual to try and target India's skipper.\n\nUnlike in ODIs, where Sri Lanka are Mohammed Siraj's favourite opposition, the fast bowler has struggled against them in T20Is. He averages 39 against them in the format, as opposed to 7.68 in ODIs, and has just three wickets in four matches. His lone wicket in this series was of Pathirana, and he would look to improve his numbers on Tuesday.\n\nWanindu Hasaranga's 15 wickets against India are the most he has taken against any opposition. In this series, he has dismissed Yashasvi Jaiswal twice, and he would be a bowler the Indians will be wary of.\n\nQuotes",
      "summary": "Sri Lanka will need to find a way out of their middle-order muddle and deliver on the platform being set by their top order.\nTeam newsSri Lanka are likely to play a similar XI to the one that turned out in the second game.\nThere is also no news on Shubman Gill, who missed the second game with a neck spasm.\nSri Lanka could be encouraged to introduce Pathirana to the attack earlier than usual to try and target India's skipper.\nUnlike in ODIs, where Sri Lanka are Mohammed Siraj's favourite opposition, the fast bowler has struggled against them in T20Is.",
      "keywords": [
        "wobbly",
        "matches",
        "look",
        "game",
        "mendis",
        "redhot",
        "respite",
        "sri",
        "pant",
        "second",
        "lanka",
        "sl",
        "series",
        "india",
        "samson"
      ],
      "image": "https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/385500/385530.6.jpg"
    },
    {
      "title": "Xiaomi unveils Redmi Pad Pro, limited Panda edition Xiaomi 14 Civi series in India",
      "authors": [
        "Dh Web Desk"
      ],
      "publish_date": null,
      "text": "Xiaomi on Monday (July 29) launched the new line of Redmi Pad Pro tablets and a special Panda edition Xiaomi 14 Civi premium phone in India.\n\nThe company is offering the Redmi Pad Pro in two variants -- Wi-Fi only and Wi-Fi + 5G. They both feature the same design language and hardware and differ only in terms of cellular modem.\n\nThey come with a 12.1-inch 2.5K (2560 × 1600p) LCD screen, support dynamic (30/48/50/60/90/120Hz) refresh rate and up to 600 nits peak brightness.\n\nThe new Redmi Pad Pro features a Corning Gorilla Glass 3 shield, a hybrid dual-SIM slot (nano + nano/microSD, only on 5G model, the Wi-Fi-only model supports microSD card), quad-speakers tuned with Dolby Atmos system, dual microphones and a type-C port.",
      "summary": "Xiaomi on Monday (July 29) launched the new line of Redmi Pad Pro tablets and a special Panda edition Xiaomi 14 Civi premium phone in India.\nThe company is offering the Redmi Pad Pro in two variants -- Wi-Fi only and Wi-Fi + 5G.\nThey both feature the same design language and hardware and differ only in terms of cellular modem.\nThey come with a 12.1-inch 2.5K (2560 × 1600p) LCD screen, support dynamic (30/48/50/60/90/120Hz) refresh rate and up to 600 nits peak brightness.\nThe new Redmi Pad Pro features a Corning Gorilla Glass 3 shield, a hybrid dual-SIM slot (nano + nano/microSD, only on 5G model, the Wi-Fi-only model supports microSD card), quad-speakers tuned with Dolby Atmos system, dual microphones and a type-C port.",
      "keywords": [
        "pad",
        "model",
        "typec",
        "wifionly",
        "india",
        "5g",
        "wifi",
        "unveils",
        "redmi",
        "panda",
        "edition",
        "xiaomi",
        "limited",
        "series",
        "pro",
        "variants"
      ],
      "image": "https://images.deccanherald.com/deccanherald%2F2024-07%2Ffb4dacfb-cb23-437d-8300-c379f134f856%2FRedmi%20Pad%20Pro%20series.jpg?w=1200&ar=40%3A21&auto=format%2Ccompress&ogImage=true&mode=crop"
    },
    {
      "title": "Mahindra Thar Roxx Panoramic Sunroof Confirmed: Details",
      "authors": [
        "Team Gaadiwaadi"
      ],
      "publish_date": "2024-07-30T04:27:42",
      "text": "The latest teaser image confirms the presence of a panoramic sunroof in the upcoming Mahindra Thar Roxx; debut on August 15\n\nMahindra & Mahindra is all set to launch the Thar Roxx in the Indian market on August 15. In its 5-door guise, the lifestyle SUV will offer better practicality, more features and a more potent powertrain than the current Thar. While the Indian SUV maker has almost revealed the entire exterior design, the latest teaser image confirms the much-talked-about panoramic sunroof in the Thar Roxx.\n\nAhead of its official debut next month, Mahindra is actively marketing the Thar Roxx with teasers, revealing new details now and then. The exterior design has already been given away in one of the teasers and appears quite similar to the current Thar. However, some noticeable changes include the new grille, updated LED headlamps with integrated DRLs, revised front bumper, a new set of alloy wheels, a larger footprint, and a proper 5-door stance.\n\nTalking about the panoramic sunroof, it was already speculated that the Thar 5-Door could get this feature and a few recent spy shots of the near-production test mules with a large sunroof further confirmed these claims. The company has now officially teased the panoramic sunroof of the Thar 5-Door. The image shared across the brand’s social media handles shows the Thar Roxx parked in a dark area with the cabin fully illuminated, thereby exposing the interiors via the panoramic sunroof.\n\nFrom the teaser, the sunroof appears fairly large, however, we couldn’t get to know its actual size concerning the roof area due to the darker surroundings which has been intentionally done to hide the details. It is important to note that the upcoming Mahindra Thar Roxx will use a proper hard roof setup with a conventional white roof liner inside the cabin, unlike the current Thar. This will allow for an overall improved cabin experience for the passengers.\n\nFurthermore, it will also help to neatly accommodate all the bells and whistles like the panoramic sunroof, sunglass holder and a proper console for sunroof controls as well as cabin lights. In addition to this, we can also spot the light-coloured seat upholstery of the Thar Roxx in the teaser. The company is yet to reveal the interiors of the Thar 5-door and we expect them to be out very soon.\n\nMahindra will offer multiple powertrain options with the Thar 5-door including the 1.5-litre diesel, 2.2-litre mHawk diesel and a 2.0-litre mStallion petrol engine. These will be paired to the 6-speed manual and a 6-speed torque converter automatic gearbox options. The lifestyle SUV will be available in both four-wheel-drive and rear-wheel-drive configurations. The price of the Mahindra Thar Roxx will likely be announced on the same day of the official unveil and the bookings could commence by the end of August. The deliveries of the SUV are expected to start shortly after.",
      "summary": "The latest teaser image confirms the presence of a panoramic sunroof in the upcoming Mahindra Thar Roxx; debut on August 15Mahindra & Mahindra is all set to launch the Thar Roxx in the Indian market on August 15.\nWhile the Indian SUV maker has almost revealed the entire exterior design, the latest teaser image confirms the much-talked-about panoramic sunroof in the Thar Roxx.\nAhead of its official debut next month, Mahindra is actively marketing the Thar Roxx with teasers, revealing new details now and then.\nThe company has now officially teased the panoramic sunroof of the Thar 5-Door.\nThe price of the Mahindra Thar Roxx will likely be announced on the same day of the official unveil and the bookings could commence by the end of August.",
      "keywords": [
        "teaser",
        "cabin",
        "thar",
        "sunroof",
        "suv",
        "roxx",
        "panoramic",
        "confirmed",
        "roof",
        "mahindra",
        "details",
        "5door"
      ],
      "image": "https://gaadiwaadi.com/wp-content/uploads/2024/07/Mahindra-Thar-Roxx-1.jpg"
    },
    {
      "error": "Article `download()` failed with HTTPSConnectionPool(host='www.moneycontrol.com', port=443): Read timed out. (read timeout=7) on URL https://www.moneycontrol.com/technology/garena-free-fire-max-redeem-codes-for-july-30-2024-win-in-game-goodies-how-to-redeem-codes-and-other-details-article-12781836.html"
    },
    {
      "error": "https://duckduckgo.com Exception: Error in request: error sending request for url (https://duckduckgo.com/): operation timed out"
    },
    {
      "title": "Virat Kohli arrives in Sri Lanka, delights fans with memorable photo moments - Watch",
      "authors": [],
      "publish_date": null,
      "text": "WATCH:\n\nNEW DELHI: India's star batsman Virat Kohli arrived in Colombo on Monday ahead of the three-match ODI series against Sri Lanka. The Sri Lankan airport staff and fans welcomed him warmly and took the opportunity to snap some photos with the celebrated cricketer.Kohli, who retired from T20Is following India's victory in the 2024 T20 World Cup, will now focus on ODIs and Tests.The rest of the Indian squad will join captain Rohit Sharma and the ODI players after the final T20I in Pallekele on July 30.India's ODI and Test captain Rohit Sharma has reached Colombo for the ODI series. Besides, Virat, Shreyas Iyer, Kuldeep Yadav, and Harshit Rana checked into the ITC Ratnadipa hotel in the Sri Lankan capital.With India having already clinched the T20I series by winning the first two matches, attention now turns to the ODIs.The ODI series will kick off on August 2 in Colombo, with all three matches set to be played at the R Premadasa International Cricket Stadium. The second ODI is scheduled for August 4, and the series will conclude on August 7.",
      "summary": "WATCH:NEW DELHI: India's star batsman Virat Kohli arrived in Colombo on Monday ahead of the three-match ODI series against Sri Lanka.\nThe Sri Lankan airport staff and fans welcomed him warmly and took the opportunity to snap some photos with the celebrated cricketer.Kohli, who retired from T20Is following India's victory in the 2024 T20 World Cup, will now focus on ODIs and Tests.The rest of the Indian squad will join captain Rohit Sharma and the ODI players after the final T20I in Pallekele on July 30.India's ODI and Test captain Rohit Sharma has reached Colombo for the ODI series.\nBesides, Virat, Shreyas Iyer, Kuldeep Yadav, and Harshit Rana checked into the ITC Ratnadipa hotel in the Sri Lankan capital.With India having already clinched the T20I series by winning the first two matches, attention now turns to the ODIs.The ODI series will kick off on August 2 in Colombo, with all three matches set to be played at the R Premadasa International Cricket Stadium.\nThe second ODI is scheduled for August 4, and the series will conclude on August 7.",
      "keywords": [
        "odi",
        "matches",
        "virat",
        "delights",
        "rohit",
        "lankan",
        "memorable",
        "kohli",
        "moments",
        "sharma",
        "sri",
        "colombo",
        "t20i",
        "arrives",
        "lanka",
        "watch",
        "series",
        "fans"
      ],
      "image": "https://static.toiimg.com/thumb/msid-112123448,width-1070,height-580,imgsize-70118,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg"
    },
    {
      "error": "Article `download()` failed with HTTPSConnectionPool(host='www.livemint.com', port=443): Read timed out. (read timeout=7) on URL https://www.livemint.com/market/stock-market-news/stocks-to-watch-hpcl-colgate-pfizer-acc-kansai-nerolac-bel-arvind-11722307619553.html"
    },
    {
      "title": "Mujhse Shaadi Karogi is 20: Akshay Kumar-Salman Khan film’s Duggal sahab was based on a real person, Rajpal Yadav was force-fitted in the film",
      "authors": [
        "Jyothi Jha",
        "Jyothi Jha Works As A Copy Editor At The Indian Express. She Brings In More Than Years Of Experience Where She Has Covered Entertainment Majorly For",
        "Ndtv",
        "Republic Media. Apart Entertainment",
        "She Has Been An Anchor",
        "Copy Editor",
        "Managed Production Team Under The Politics",
        "Daily News Segment. She'S Passionate About Journalism",
        "It Has Always Been Her First Choice",
        "She Believes In What George Orwell Had Once Said"
      ],
      "publish_date": "2024-07-30T08:00:41",
      "text": "When Mujhse Shaadi Karogi released on this date 20 years ago, people were quite excited to enter the cinema halls through the beautiful mandaps built at the entrances of several theatres in India and abroad, giving a full wedding-like vibe. Several contests were held as part of the film’s marketing campaign with prizes including a honeymoon trip abroad and wedding ensembles by Neeta Lulla. They even released a 64-page palm-sized book with information about the characters’ love triangle, their photos and also tips about how to woo a woman.\n\nResult? The film opened to a great business and had an excellent theatrical run. So well that it still resonates with the crowd and even Sonakshi Sinha and Anant Ambani couldn’t do without the Mujhse Shaadi Karogi title track at their post-wedding and baraat procession, respectively. It became all the more nostalgic after the ‘Desi girl’ Priyanka Chopra herself danced to the track from her 2004 hit romantic-comedy, also starring Akshay Kumar and Salman Khan at Anant Ambani’s baraat.\n\nThe success was a collective effort of David Dhawan who wanted to re-invent himself with a romantic comedy, Sajid Nadiawala’s stubbornness to have the talented Rajpal Yadav in the film, and the creative effort of Rumi Jaffery who wanted to avoid the repetitiveness of his 1997 film Deewana Mastana. A little bit of inspiration from real life characters gave us the iconic Duggal Sahab, and Jaffery has an interesting story to tell.\n\nView this post on Instagram A post shared by Nadiadwala Grandson (@nadiadwalagrandson)\n\nAdvertisement\n\nJaffery gives the credit to filmmaker K Bhagyaraj for the film’s idea, and reveals Duggal sahab (played by Kader Khan) — a meme favourite to the day — was inspired by a real person.\n\nHe said, “The character was inspired by filmmaker Rahul Rawail’s father HS Rawail’s best friend, Ridku uncle. He was just 2.5 feet tall and you can find him in every film of HS Rawail such as Mere Mehboob and Mehboob Ki Mehendi. He used to live with HS Rawail like his own brother at his residence. So when I was writing Anjaam, Rahul casually discussed with me a very strange health complication of Ridku uncle. He told me that when he would wake up, he wouldn’t be able to see anything, sometimes he would have hearing impairment. I was shocked, but also found it quite funny. I told him I will use it in one of my films. Rahul said nobody will believe it. I was like why not, he will be a great character in a comedy drama. Several years later, I brought this character to life in Mujhse Shaadi Karogi.”\n\nView this post on Instagram A post shared by Nadiadwala Grandson (@nadiadwalagrandson)\n\nALSO READ | The ‘Animal’ appeal of SanjayDutt: How the star’s life unfolded like a Sandeep Reddy Vanga movie\n\nJaffery also revealed that Rajpal Yadav was a last-minute addition in the film and it was a task for him to create a role for the actor. The actor was fresh off the success of Jungle (2000) where he played a psychotic bandit for laughs with elan. Producer Sajid Nadiadwala called Rajpal and added him to the cast without speaking to Jaffery. “I am making a comedy drama with Salman Khan and Akshay Kumar, unn dono ke role ke baad third best tumhara hi hoga, Rumi se role sunlo. (Yours will be the third best role in the film, get your briefing from Rumi),” the producer told Rajpal. Rumi said when he received a call from Rajpal, he was nonplussed.\n\nView this post on Instagram A post shared by Nadiadwala Grandson (@nadiadwalagrandson)\n\nAdvertisement\n\n“I called Sajid and asked what role has he given to Rajpal Yadav. Sajid said, ‘I just want him in the movie, now you figure out how.’ I was extremely stressed and I was constantly getting calls from Rajpal. The shooting date was nearing. Rajpal would say, ‘Bhaiya please brief me about my role so that I can understand its needs and start working on them’. To put him off, I told him, ‘okay, see me tomorrow’. After hanging up the phone, I started to think what role to give him. There was a role of a broker and then there was the role of a rowdy, who was the gang leader of the Eagle gang, which was originally written for Vindu Dara Singh”, Rumi told us.\n\nHe added, “By evening, I decided to give him a double role — both as the broker and the gang leader. The idea of twin brother occurred to me and it seemed just the right role for him. Soon, I called Sajid Nadiadwala and briefed him the role, he loved it. Finally, I briefed him (Rajpal) the role and he was quite satisfied. It was a very challenging situation. Just because Rajpal was a good actor, the role was created for him at the last minute.”\n\nMujhse Shaadi Karogi also made pugs the dog breed of choice. Rumi confesses to be obsessed with pugs since the time of Chalte Chalte (2003). Though he couldn’t use the real dog in the previous film, he successfully cast the dog in Mujhse Shaadi Karogi. “Kutta nahi, beta hai mera”, says Colonel sahab (played by the legendary Amrish Puri).\n\n“The dog died mid-shoot”, revealed Rumi Jaffery. “Another interesting fact is that the dog initially used in the film was quite old, so it died during the shoot. But, luckily, all dogs look the same, so we brought a similar looking dog and completed the shoot with that.”\n\nAdvertisement\n\nWhen we reached out to Rajpal Yadav, whose talent forced the unit to create a role for him, the actor had nothing but gratitude. He said, “It feels like yesterday. Soon after Jungle, I bagged several film offers and one of them was Mujhse Shaadi Karogi. It was my first big commercial film with such an ensemble cast. It was more like a dream to work with Kadar Khan and Amrish Puri. This was my first film with Akshay Kumar and Salman Khan, and it was quite an experience.” While he called the entire filming a fun experience, he fondly recalled the magician sequence. “I was having too much fun balancing my body in the air”, laughed Rajpal as he recalled the shooting experience.\n\nMujhse Shaadi Karogi, which became the fourth highest-grossing Indian film of 2004, was also appreciated for ahead of time movie set. Although the film was set in Goa, it was mostly shot on two detailed sets created by Sharmishta Roy in Mumbai’s Film City and Mauritius.",
      "summary": "So well that it still resonates with the crowd and even Sonakshi Sinha and Anant Ambani couldn’t do without the Mujhse Shaadi Karogi title track at their post-wedding and baraat procession, respectively.\n(Yours will be the third best role in the film, get your briefing from Rumi),” the producer told Rajpal.\nThough he couldn’t use the real dog in the previous film, he successfully cast the dog in Mujhse Shaadi Karogi.\nSoon after Jungle, I bagged several film offers and one of them was Mujhse Shaadi Karogi.\nMujhse Shaadi Karogi, which became the fourth highest-grossing Indian film of 2004, was also appreciated for ahead of time movie set.",
      "keywords": [
        "karogi",
        "shaadi",
        "dog",
        "post",
        "yadav",
        "film",
        "sajid",
        "role",
        "khan",
        "mujhse",
        "rumi",
        "real",
        "rajpal",
        "sahab",
        "person",
        "told",
        "kumarsalman"
      ],
      "image": "https://images.indianexpress.com/2024/07/Priyanka-Chopra-5.jpg"
    },
    {
      "error": "https://links.duckduckgo.com/d.js Exception: Error in request: error sending request for url (https://links.duckduckgo.com/d.js?q=Who+is+the+driver+of+the+SUV+arrested+in+UPSC+coaching+centre+deaths+case+-+The+Indian+Express&kl=wt-wt&l=wt-wt&p=&s=0&df=&vqd=4-325904759502880553419485302014083666873&bing_market=wt-WT&ex=-1): operation timed out"
    },
    {
      "title": "Man arrested for killing 20-year-old woman and dumping her body in bushes in Navi Mumbai",
      "authors": [
        "Sagar Rajput",
        "Cdata",
        "Var Template_Content",
        "Sso_Login_Box",
        "Xwelcome Backorenter The Email Address Or Mobile Number Associated With Your Account To Sign In. Show Passwordsign Innew To The Indian Express Signupxcreate Your Account It Is Quick",
        "Easy.Or Show Passwordnextvalidate Otpregisteralready Have An Account",
        "Signin",
        "Sso_Social_Box",
        "Sign In Withgmailfacebookapple",
        "Var Follow_Widget_Data"
      ],
      "publish_date": "2024-07-30T13:10:27",
      "text": "A 24-year-old man was arrested from Karnataka’s Gulbarga district on Tuesday for allegedly killing a 20-year-old woman and dumping her body amid bushes near the Uran railway station.\n\nAccording to the Navi Mumbai police, the accused Daud Shaikh, who was nabbed from Shahapur in Gulbarga, has confessed to have killed the woman, identified as Yashshri Shinde. Police suspect that he committed the crime after she rejected his advances.\n\n“Shaikh believed that Shinde was in a relationship with another man. We are trying to ascertain the sequence of events,” said an officer.\n\nAdvertisement\n\nHowever, police said Shaikh, who earlier stayed in Uran, was in touch with Shinde, who also stayed with family in the same area, for over five years. Shinde worked with a company in Belapur.\n\nPolice said Shaikh was earlier arrested under the Protection of Children from Sexual Offences Act in 2019. “After he managed to secure bail, he relocated to his hometown and there he worked as a bus driver,” an officer said.\n\n“The accused came to Mumbai on July 22 and was in touch with the woman. On July 24, Shinde worked only half day, after which it is suspected that Shaikh met her,” said an officer.\n\nThe woman went missing on July 25 morning after she left her home for office. “As per our investigation, the two met near the railway station when he allegedly stabbed her to death,” said a police officer.\n\nAdvertisement\n\n“After the family was unable to contact her, they started searching for her. When they failed to find her, they approached the Uran police late on July 25,” the officer added.\n\nOn July 27, police received a call at 2 am about a woman’s body found in the bushes near the Uran railway station.\n\n“The woman was identified by her family at the hospital, following which a case of murder was registered,” an officer from the Uran police station said, adding that there were multiple stab injuries on her stomach and back.\n\nThe Navi Mumbai police subsequently formed eight teams to locate the accused and found that there were three suspects who were constantly in touch with her.\n\nAdvertisement\n\n“After interrogating the suspects, we managed to identify Daud, following which two teams were dispatched to Bangalore and two teams were sent to Shahapur in Karnataka. Daud was apprehended early on Tuesday,” said additional commissioner of police Deepak Sakore.\n\nShaikh will be produced before court on Wednesday.",
      "summary": "A 24-year-old man was arrested from Karnataka’s Gulbarga district on Tuesday for allegedly killing a 20-year-old woman and dumping her body amid bushes near the Uran railway station.\nAccording to the Navi Mumbai police, the accused Daud Shaikh, who was nabbed from Shahapur in Gulbarga, has confessed to have killed the woman, identified as Yashshri Shinde.\nShinde worked with a company in Belapur.\nOn July 24, Shinde worked only half day, after which it is suspected that Shaikh met her,” said an officer.\nOn July 27, police received a call at 2 am about a woman’s body found in the bushes near the Uran railway station.",
      "keywords": [
        "shaikh",
        "body",
        "near",
        "dumping",
        "woman",
        "officer",
        "worked",
        "teams",
        "man",
        "railway",
        "bushes",
        "shinde",
        "touch",
        "mumbai",
        "20yearold",
        "arrested",
        "uran",
        "navi",
        "killing"
      ],
      "image": "https://images.indianexpress.com/2024/07/image_123650291-1-1.jpg"
    },
    {
      "title": "Rafael Nadal visibly annoyed with retirement question after falling to Novak Djokovic in Paris Olympics 2024",
      "authors": [
        "Ht Sports Desk"
      ],
      "publish_date": "2024-07-30T07:12:24",
      "text": "It turned out to be a one-sided affair as Novak Djokovic cruised past Rafael Nadal in straight sets, winning 6-1 6-4 in the men's singles second round fixture at the ongoing Paris Olympics 2024, on Monday. Spain's Rafael Nadal (C) shakes hands with chair umpire Renaud Lichtenstein of France after his defeat to Serbia's Novak Djokovic (R) in their men's singles second round tennis match.(AFP)\n\nWith the win, Djokovic remained in the hunt for his elusive Olympic gold. Meanwhile, Nadal has the men's doubles left to add to his tally of two Olympic gold medals. The first set proved to be too easy for Djokovic as he bagged it 6-1 and led 4-0 in the second. But Nadal attempted a fightback, levelling it 4-4 at one point.\n\nNadal is probably in his swansong year, and this could also be his final Olympics. Speaking after the match, he was asked about his retirement plans, which left him visibly annoyed. \"You want me to retire every day guys, you ask me for that. I am trying to do my best. I cannot live every single day with the feeling that it's going to be or not going to be my last match\", he said.\n\n\"I have been suffering a lot of injuries the last two years. So, if I feel that I am not competitive enough to keep going, or physically I'm not ready to keep going, I will stop and I will let you know.\n\n\"I like what I do and of course I'm going to miss the adrenaline of playing but I cannot complain. I have been playing in all these courts for 20 years, fighting for the most important things. I achieved much more than I dreamed of.\n\n\"If that's the last match here, I'll be in peace. I did my best and I can't complain anymore,\" he added.\n\nNadal wasn't at his best, with age, injury and fitness issues finally catching up to him. Reacting to the win, Djokovic said, \"I was just very proud to be part of this match and ... I wanted to do my job on the court and really execute the game plan as much as I possibly can.\"\n\n\"So almost a perfect match, the 6-1 4-0. Then things got complicated, I started to hesitate a little bit on my shot he stepped in, the crowd got involved and for all, it was really anybody's set, anybody's game. Just very glad to overcome this incredible challenge,\" he added.",
      "summary": "It turned out to be a one-sided affair as Novak Djokovic cruised past Rafael Nadal in straight sets, winning 6-1 6-4 in the men's singles second round fixture at the ongoing Paris Olympics 2024, on Monday.\nSpain's Rafael Nadal (C) shakes hands with chair umpire Renaud Lichtenstein of France after his defeat to Serbia's Novak Djokovic (R) in their men's singles second round tennis match.\n(AFP)With the win, Djokovic remained in the hunt for his elusive Olympic gold.\nMeanwhile, Nadal has the men's doubles left to add to his tally of two Olympic gold medals.\nReacting to the win, Djokovic said, \"I was just very proud to be part of this match and ...",
      "keywords": [
        "win",
        "match",
        "question",
        "nadal",
        "falling",
        "best",
        "61",
        "things",
        "djokovic",
        "retirement",
        "paris",
        "rafael",
        "novak",
        "visibly",
        "mens",
        "second",
        "olympics",
        "going"
      ],
      "image": "https://images.hindustantimes.com/img/2024/07/30/1600x900/TENNIS-OLY-PARIS-2024-86_1722303105096_1722303263843.jpg"
    },
    {
      "title": "Manika Batra scripts history, becomes first Indian table tennis player to reach Olympics pre-quarterfinals",
      "authors": [],
      "publish_date": "2024-07-30T07:11:21",
      "text": "Manika Batra made history by becoming the first Indian table tennis player to reach the singles pre-quarterfinals at the Olympic Games with a fluent 4-0 win over world number 18 and home favourite Prithika Pavade here on Monday. Paris: India's Manika Batra reacts after defeating France's Prithika Pavade in the women's singles round of 32 match at the Summer Olympics, in Paris, Monday(PTI)\n\nThe 29-year-old Manika dominated from start to finish for a 11-9 11-6 11-9 11-7 win over Prithika, who has Indian roots.\n\nIt turned out to be one of the most memorable matches for an Indian table tennis player in Olympics history. Manika had reached the round of 32 at the Tokyo Olympics and she bettered that performance on Monday.\n\n\"I am happy that I beat a French player in Paris. I defeated a higher-ranked player. I did not think of creating history and making the pre-quarters, there are more rounds, I will take it match by match and give my best as I always do,\" Manika told PTI after her match.\n\nManika's ploy to attack Prithika's backhand proved very effective but that was not the strategy she had devised before the match.\n\n\"I had planned to play to her forehand as discussed with my coach but I was getting the points on her backhand, so I did not change the tactics. I did play a few shot on her forehand too, I did not want her to think that I am playing only on her backhand.\n\n\"It was a tough match. Staying relaxed helps me both on and off the court. I do breathing exercises that help me during the match.I will give my best whoever I play against in the next round,\" she said.\n\nPrithika's parents are originally from Puducherry but the family shifted to France in 2003. She was born in a Paris suburb a year later.\n\nThe 19-year-old Prithika had competed in the Tokyo Olympics, making a first-round exit but has improved considerably since then as she is currently ranked 18th in the world as against 28th rank of Manika.\n\nLeft-handed Prithika came into the Olympics on the back of a splendid run where she made the WTT final for the first time in her career in June but could not find a way to go past Manika, who dished out a commanding show.\n\nThe first game was a tight affair with both players going neck and neck. At 8-8, Manika induced a backhand error from her young rival and closed the game with a ferocious forehand drive that Prithika could not return.\n\nManika carried the momentum in the second game, taking a 3-1 lead.\n\nPrithika fought back to level the scores, inducing errors from the Indian. However, Manika's attack on Prithika's backhand got her points consistently. In no time, she was leading 9-6. Consecutive backhand errors from Prithika handed Manika the second game.\n\nThere was no stopping the seasoned Indian, who got a healthy 3-0 cushion in game three as Prithika struggled with her returns.\n\nA desperate Prithika went all out and got her first point with a thumping forehand winner. With a 5-1 lead in hand, Manika kept attacking the backhand side of the French player, making it 8-4.\n\nTrailing 5-10, Prithika made it a contest by taking four points in a row but Manika needed just one more to close the game. The home favourite netted a backhand drive to concede the game and a 3-0 lead to the Indian.\n\nA ferocious forehand gave Manika a 10-5 lead in the fourth game and five match points. She converted the third when Prithika netted her backhand to win the match in 37 minutes.",
      "summary": "Manika Batra made history by becoming the first Indian table tennis player to reach the singles pre-quarterfinals at the Olympic Games with a fluent 4-0 win over world number 18 and home favourite Prithika Pavade here on Monday.\nIt turned out to be one of the most memorable matches for an Indian table tennis player in Olympics history.\nManika had reached the round of 32 at the Tokyo Olympics and she bettered that performance on Monday.\nWith a 5-1 lead in hand, Manika kept attacking the backhand side of the French player, making it 8-4.\nA ferocious forehand gave Manika a 10-5 lead in the fourth game and five match points.",
      "keywords": [
        "tennis",
        "backhand",
        "match",
        "prequarterfinals",
        "game",
        "history",
        "table",
        "scripts",
        "prithika",
        "forehand",
        "reach",
        "indian",
        "manika",
        "player",
        "points",
        "olympics"
      ],
      "image": "https://images.hindustantimes.com/img/2024/07/30/1600x900/PTI07-30-2024-000027A-0_1722303434074_1722303453357.jpg"
    },
    {
      "title": "Ola Electric eyes Rs 6,000 crore in 1st auto IPO since Maruti",
      "authors": [],
      "publish_date": null,
      "text": "MUMBAI: Electric scooter startup Ola Electric 's Rs 6,146-crore IPO - biggest this year - is set to to open on Aug 2. This will be the first IPO by an auto company since Maruti Suzuki (then Maruti Udyog) went public in mid-2003.The bidding for the IPO will start on Aug 2 and end on Aug 6 at a price band of Rs 72-76 per share. At the upper end of the price band, the implied valuation of the firm is $4 billion - lower than the $7-8 billion valuation it was targeting a few months ago.It's also lower than the $5.4-billion valuation at which it had raised funds in its last round in Sept 2023.\"We wanted to price it at attractive, aggressive levels so that they (investors) make money,\" Bhavish Aggarwal , founder & chairman of Ola Electric told TOI.Of the total funds being mobilised through the offer, Ola Electric - the top electric two-wheeler maker in India - is raising Rs 5,500 crore through a fresh issuance of shares in the IPO. The balance will be an offer for sale by existing shareholders including global investment giants SoftBank and Temasek.Aggarwal said there is no slowdown in the India EV story. \"Three years ago, when we launched our product, that's when I believe the EV story began. I do not see any slowing down in the story... there are cyclical ups and downs, basis subsidy changes or some seasonal factors,\" Aggarwal said. \"Year-on-year... our growth is 90% (FY24 over FY23). The growth story is consistent and secular,\" he added. He also said that as more companies enter the EV market and more products are launched, the scope will only expand.The startup, Aggarwal said, is well equipped to tackle the scrutiny that public companies are typically subjected to by the markets. \"We have primed ourselves in terms of governance, processes and we want to engage with the public markets and make sure we are satisfying their expectation of governance and exceed that,\" Aggarwal said. After the listing, which is expected in the second week of Aug, promoters will retain 37-38% of the company.",
      "summary": "MUMBAI: Electric scooter startup Ola Electric 's Rs 6,146-crore IPO - biggest this year - is set to to open on Aug 2.\nThis will be the first IPO by an auto company since Maruti Suzuki (then Maruti Udyog) went public in mid-2003.The bidding for the IPO will start on Aug 2 and end on Aug 6 at a price band of Rs 72-76 per share.\n\"We wanted to price it at attractive, aggressive levels so that they (investors) make money,\" Bhavish Aggarwal , founder & chairman of Ola Electric told TOI.Of the total funds being mobilised through the offer, Ola Electric - the top electric two-wheeler maker in India - is raising Rs 5,500 crore through a fresh issuance of shares in the IPO.\n\"Three years ago, when we launched our product, that's when I believe the EV story began.\nAfter the listing, which is expected in the second week of Aug, promoters will retain 37-38% of the company.",
      "keywords": [
        "aug",
        "6000",
        "ev",
        "maruti",
        "1st",
        "price",
        "aggarwal",
        "electric",
        "auto",
        "valuation",
        "rs",
        "eyes",
        "ipo",
        "public",
        "ola",
        "crore"
      ],
      "image": "https://static.toiimg.com/thumb/msid-112121313,width-1070,height-580,imgsize-1192814,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg"
    },
    {
      "title": "Isolation Units: Isolation Units Reintroduced at City Hospitals Due to Flu and Viral Surge",
      "authors": [],
      "publish_date": null,
      "text": "Kolkata: Isolation units are back at several city hospitals. A surge in influenza , swine flu and multiple other viral infections has led the hospitals to reintroduce them to prevent transmission, for the first time since Covid. While a couple has created ‘fever clinics’ at their emergency sections, like they had done during the pandemic to screen patients, others have launched proper isolation wards for those with symptoms of influenza.Peerless Hospital, where a woman succumbed to swine flu a week ago, has revived two single-bed isolation cabins for two swine flu patients now admitted.These cabins were introduced during Covid. “These were the first isolation units at the start of the pandemic and we have revived them to accommodate infectious diseases patients. There has been an increase in number over the last fortnight and we may open a full-fledged isolation ward if the spike continues,” said Peerless Hospital CEO Sudipta Mitra.Manipal Hospitals has introduced isolation wards across its four units at Dhakuria, Mukundapur and Salt Lake. “We have earmarked twin-bed isolation rooms at Mukundapur and Salt Lake units,” said a Manipal representative.Ruby General Hospital has two isolation beds for two influenza patients now admitted. “We had a swine flu patient who was discharged on Sunday. Since there has been a steady flow of influenza A and swine flu patients for a month, it has become necessary to isolate them to prevent transmission,” said Ruby general manager – operations Subhashish Datta.“Swine flu or H1N1 is extremely contagious and could turn out to be severe in children and the elderly who have lower resistance. Seasonal influenza is contagious, too, so patients need to be isolated. Doctors at the ward have been using masks and sanitizers like they did during Covid,” said Manipal Hospital infectious diseases physician Sayan Chakrabarty.Charnock Hospital has received multiple pulmonary infection cases, apart from influenza A patients. “These patients are being admitted in our respiratory care units, both ICU and wards” said Charnock MD Prashant Sharma. RN Tagore International Institute of Cardiac Sciences (RTIICS) has two influenza patients admitted but doesn’t have any swine flu patients.“We have started isolating them. Seven isolation beds have been set up at a separate ward where we have influenza patients now,” said Narayana Hospitals COO R Venkatesh.BP Poddar Hospital has started a fever clinic at its OPD where those with fever and influenza symptoms are being screened and treated. “We have a 35-bed isolation unit where influenza and swine patients are being admitted. It is fully occupied,”said group advisor Supriyo Chakrabarty.",
      "summary": "Kolkata: Isolation units are back at several city hospitals.\nA surge in influenza , swine flu and multiple other viral infections has led the hospitals to reintroduce them to prevent transmission, for the first time since Covid.\n“These were the first isolation units at the start of the pandemic and we have revived them to accommodate infectious diseases patients.\n“We had a swine flu patient who was discharged on Sunday.\nRN Tagore International Institute of Cardiac Sciences (RTIICS) has two influenza patients admitted but doesn’t have any swine flu patients.“We have started isolating them.",
      "keywords": [
        "admitted",
        "swine",
        "isolation",
        "hospitals",
        "wards",
        "units",
        "city",
        "viral",
        "flu",
        "patients",
        "reintroduced",
        "influenza",
        "hospital",
        "surge"
      ],
      "image": "https://static.toiimg.com/thumb/msid-112121132,width-1070,height-580,imgsize-247878,resizemode-75,overlay-toi_sw,pt-32,y_pad-40/photo.jpg"
    },
    {
      "title": "Rwanda: Hepatitis Awareness During World Hepatitis Day",
      "authors": [],
      "publish_date": null,
      "text": "Blood Analisys to know if the patient have hepatitis, July 2024 Photo:@NYTimes\n\nIn the 2022-2023 fiscal year, over 500,000 people were screened for hepatitis C, of whom, about 2,000 tested positive and were initiated on treatment, the statistics showed.\n\nOn Sunday, the Rwanda Biomedical Center (RBC) pledged to control hepatitis B and hepatitis C infections in the East African country by intensified efforts to improve awareness about the disease and education in this regard.\n\nRelated:\n\nRwanda: Presidential and Parliamentary Voting Stars\n\nIn a message to mark World Hepatitis Day, Janvier Serumondo, the director of the sexually transmitted infections and other blood-borne infections unit at RBC, called on Rwandan residents to seek voluntary screening for the disease at the nearest health facilities to know their status.\n\nSerumondo said tests and treatment have been decentralized to health centers in Rwanda, where infected Rwandans and refugees in the country receive free medical care.\n\nHealthcare workers have been trained, and screening and treatment campaigns stepped up, he said.\n\nRBC’s most recent statistics released Sunday show that more than 5 million people have been tested for hepatitis B virus (HBV) over the past decade, 8,000 people are on lifelong HBV treatment while more than 7 million, including children and adults, have been vaccinated against HBV.\n\nAnd in the 2022-2023 fiscal year, over 500,000 people were screened for hepatitis C, of whom, about 2,000 tested positive and were initiated on treatment, the statistics showed.\n\n“There has been significant progress in managing hepatitis C with estimated prevalence of chronic hepatitis C decreasing from 4 percent in 2017 to 0.48 percent in 2023,” Serumondo said, reaffirming Rwanda’s commitment to eliminating viral hepatitis C by 2030.\n\nHepatitis virus is mostly transmitted through blood-to-blood contact. Medics say early diagnosis is important to cure.",
      "summary": "Blood Analisys to know if the patient have hepatitis, July 2024 Photo:@NYTimesIn the 2022-2023 fiscal year, over 500,000 people were screened for hepatitis C, of whom, about 2,000 tested positive and were initiated on treatment, the statistics showed.\nOn Sunday, the Rwanda Biomedical Center (RBC) pledged to control hepatitis B and hepatitis C infections in the East African country by intensified efforts to improve awareness about the disease and education in this regard.\nAnd in the 2022-2023 fiscal year, over 500,000 people were screened for hepatitis C, of whom, about 2,000 tested positive and were initiated on treatment, the statistics showed.\n“There has been significant progress in managing hepatitis C with estimated prevalence of chronic hepatitis C decreasing from 4 percent in 2017 to 0.48 percent in 2023,” Serumondo said, reaffirming Rwanda’s commitment to eliminating viral hepatitis C by 2030.\nHepatitis virus is mostly transmitted through blood-to-blood contact.",
      "keywords": [
        "screening",
        "hepatitis",
        "statistics",
        "awareness",
        "c",
        "virus",
        "day",
        "tested",
        "transmitted",
        "world",
        "serumondo",
        "treatment",
        "infections",
        "rwanda"
      ],
      "image": "https://ikona.telesurenglish.net/content/uploads/2024/07/bZGLGJtX.jpeg.webp"
    },
    {
      "title": "Priti Patel vows to get Tories 'match fit' in leadership bid",
      "authors": [],
      "publish_date": null,
      "text": "Former Home Secretary Dame Priti Patel has launched a bid to become leader of the Conservative Party, telling members she can turn it \"back into a winning machine\".\n\nDame Priti, who served in government under three prime ministers, said her experience meant she would be able to \"reinvigorate\" the party following its worst ever general election performance.\n\nShe is the first woman to throw her hat into the ring to replace Rishi Sunak, joining James Cleverly, Robert Jenrick, Tom Tugendhat and Mel Stride in the race.\n\nShadow business secretary Kemi Badenoch - widely seen as a frontrunner to take over from Mr Sunak - is expected to launch her candidacy on Monday.",
      "summary": "Former Home Secretary Dame Priti Patel has launched a bid to become leader of the Conservative Party, telling members she can turn it \"back into a winning machine\".\nDame Priti, who served in government under three prime ministers, said her experience meant she would be able to \"reinvigorate\" the party following its worst ever general election performance.\nShe is the first woman to throw her hat into the ring to replace Rishi Sunak, joining James Cleverly, Robert Jenrick, Tom Tugendhat and Mel Stride in the race.\nShadow business secretary Kemi Badenoch - widely seen as a frontrunner to take over from Mr Sunak - is expected to launch her candidacy on Monday.",
      "keywords": [
        "turn",
        "secretary",
        "match",
        "party",
        "leadership",
        "bid",
        "patel",
        "fit",
        "worst",
        "winning",
        "tugendhat",
        "priti",
        "sunak",
        "woman",
        "vows",
        "widely",
        "tories"
      ],
      "image": "https://ichef.bbci.co.uk/news/1024/branded_news/76be/live/8c1c6e50-4bfc-11ef-838e-d9c9dd6aa145.jpg"
    },
    {
      "title": "Hyderabad Records Significant Spike in Dengue Cases This July",
      "authors": [
        "Shrimansi Kaushik",
        "About The Author"
      ],
      "publish_date": "2024-07-29T23:22:36",
      "text": "Hyderabad: Dengue cases have seen a massive surge in July, with over 1,300 cases being reported in July alone.\n\nAs per the data shared by director of public health Ravindra Nayak, the state recorded 1,345 cases from July 1 to July 28, 2024. The number was 728 in the same period in 2023. The National Sector for Vector Borne Disease Control (NCVBDC) website shows around 1074 cases from January to June this year.\n\nIn Hyderabad district, 206 cases were recorded in July compared to just 60 in June, shared Hyderabad DMHO Dr J. Venkati.\n\nDoctors are also seeing around 3-4 cases each daily. The demand for platelets has also increased. Bunty Mundada, an activist running the blood donation non-profit Being Human-Ek Umeed, reported receiving 70 requests for platelets for dengue cases in July. Shravan Pintoo, founder of NGO Hyderabad Blood Donors, said he received around 40-50 requests in July.\n\nThe GHMC, meanwhile, shared that 626 cases were reported in its limits in July, indicating that most of the state’s cases are within GHMC limits. The GHMC recently announced efforts to prevent vector-borne diseases, noting that there were 786 cases in July 2023.\n\nDoctors are advising citizens to take precautions against vector-borne and monsoon-related illnesses. “The most common symptoms include fever, headache, muscle and joint pain, rashes, and mild bleeding such as nose or gum bleeding,” said Dr Avash Pani, Consultant Paediatrician at Apollo Cradle and Children’s Hospital, Kondapur. He has seen around 20 cases of dengue in July. “Monitor your child’s symptoms and seek medical help if they worsen. Warning signs of severe dengue include abdominal pain, vomiting, rapid breathing, bleeding gums, and fatigue. Severe dengue may require hospitalisation for intravenous fluids, blood transfusions, and close monitoring by healthcare providers,” he said.\n\nGovernment health officials have been instructed to conduct door-to-door surveys and document cases of dengue and related illnesses daily.",
      "summary": "Hyderabad: Dengue cases have seen a massive surge in July, with over 1,300 cases being reported in July alone.\nIn Hyderabad district, 206 cases were recorded in July compared to just 60 in June, shared Hyderabad DMHO Dr J. Venkati.\nBunty Mundada, an activist running the blood donation non-profit Being Human-Ek Umeed, reported receiving 70 requests for platelets for dengue cases in July.\nShravan Pintoo, founder of NGO Hyderabad Blood Donors, said he received around 40-50 requests in July.\nGovernment health officials have been instructed to conduct door-to-door surveys and document cases of dengue and related illnesses daily.",
      "keywords": [
        "symptoms",
        "spike",
        "vectorborne",
        "shared",
        "ghmc",
        "significant",
        "bleeding",
        "reported",
        "blood",
        "dengue",
        "records",
        "cases",
        "hyderabad"
      ],
      "image": "http://dc-cdn.s3-ap-southeast-1.amazonaws.com/dc-Cover-tp1uc706f78r75sfv2f7bq1b82-20160803040104.Medi.jpeg"
    },
    {
      "error": "https://links.duckduckgo.com/d.js Exception: Error in request: error sending request for url (https://links.duckduckgo.com/d.js?q=Weather+Change+Sparks+Disease+Surge%2C+Hospital+OPD+Surpasses+400+-+Catch+News&kl=wt-wt&l=wt-wt&p=&s=0&df=&vqd=4-225109403875718256938726712524571294950&bing_market=wt-WT&ex=-1): operation timed out"
    },
    {
      "title": "Meloni meets Xi as Italy vows to 'relaunch' bilateral ties with China",
      "authors": [],
      "publish_date": null,
      "text": "Meloni meets Xi as Italy vows to 'relaunch' ties with China\n\nChinese President Xi Jinping arrives with Italy's Prime Minister Giorgia Meloni for a meeting at the Diaoyutai State Guesthouse\n\nThe five-day visit comes after Ms Meloni last year removed her country from President Xi's signature Belt and Road Initiative (BRI) .\n\nDuring her first trip to China since taking office, Ms Meloni and Chinese Premier Li Qiang met on Sunday and signed a three-year plan to strengthen economic co-operation.\n\nPresident Xi in turn hailed the \"long-established friendly\" ties, as well as \"tolerance, mutual trust and mutual respect\" between Beijing and Rome.\n\nItaly's Prime Minister Giorgia Meloni has said China is an \"important interlocutor\" in managing global tensions, as she met President Xi Jinping in Beijing.\n\nAt the time, Rome said the massive Chinese investment scheme aimed at promoting bilateral trade had gained less than expected.\n\nMs Meloni said her visit to China was an effort to \"relaunch\" the relationship.\n\nAfter talks with President Xi at Beijing's Diaoyutai State Guesthouse, Ms Meloni said: \"There is growing insecurity at an international level and I think that China is inevitably a very important interlocutor to address all these dynamics\".\n\nShe said the two nations must \"think together\" to remain stable and guarantee peace.\n\nIn a statement, Italy's prime minister's office said the two leaders' discussions included the war in Ukraine, the risks of a further escalation of the situation in the Middle East and the growing tensions in the Indo-Pacific.\n\nIt added that Prime Minister Meloni and President Xi addressed some of the most important global governance issues, \"from artificial intelligence to the fight against climate change and the UN Security Council reform\".\n\nMr Xi urged Rome and Beijing to \"uphold the spirit of the Silk Road\", so that East-West relations could \"rebound into a new era\".\n\n\"Both sides face important opportunities for mutual development\", he said, adding, \"Beijing welcomes Italian companies that invest in China and is willing to import more high-quality Italian products\".\n\nItaly was the only major Western nation to sign up to the BRI, one of China's most ambitious trade and infrastructure projects, sometimes referred to as the \"New Silk Road\".\n\nThe move was heavily criticised at the time by the US and some other major Western countries.\n\nSince coming to power in 2022, Ms Meloni has sought to lead a more pro-Western and pro-Nato foreign policy than her predecessors.\n\nBefore withdrawing from the BRI, Ms Meloni had described the former government's decision to join it as \"a serious mistake\".\n\n\"Every country which is a [BRI] member knows that China is first and they are second and I don't think Italy as a G7 member wanted to be grouped together with Russia, Pakistan or Sri Lanka,\" said Alicia Garcia-Herrero, chief economist for the Asia Pacific region at investment bank Natixis.\n\n\"Without BRI [membership] Meloni is coming to China at a different level of engagement - less as a vassal and more as a partner,\" she added.\n\nUnder Ms Meloni, Italy has moved to block a Chinese state-owned company from taking control of tyre making giant Pirelli.\n\nRome has also supported a recent move by the European Commission to impose tariffs of as much as 37.6% on electric vehicles imported from China.\n\nTwo-way trade between two countries reached 66.8 billion euros (£56.3bn) last year, making China Italy's largest non-EU trading partner after the US.",
      "summary": "President Xi in turn hailed the \"long-established friendly\" ties, as well as \"tolerance, mutual trust and mutual respect\" between Beijing and Rome.\nMs Meloni said her visit to China was an effort to \"relaunch\" the relationship.\nSince coming to power in 2022, Ms Meloni has sought to lead a more pro-Western and pro-Nato foreign policy than her predecessors.\nBefore withdrawing from the BRI, Ms Meloni had described the former government's decision to join it as \"a serious mistake\".\nUnder Ms Meloni, Italy has moved to block a Chinese state-owned company from taking control of tyre making giant Pirelli.",
      "keywords": [
        "italy",
        "ties",
        "meloni",
        "think",
        "china",
        "ms",
        "trade",
        "xi",
        "prime",
        "president",
        "bri",
        "relaunch",
        "bilateral",
        "meets",
        "vows",
        "important"
      ],
      "image": "https://ichef.bbci.co.uk/news/1024/branded_news/f6a2/live/dcda1a20-4d9d-11ef-ba3c-e10a62be783c.jpg"
    },
    {
      "title": "Apple Watch",
      "authors": [],
      "publish_date": null,
      "text": "Online Personal Session\n\nGet to know your new Apple Watch.\n\nWhether you’re new to your Apple device or need a refresher on the latest features, schedule a free one‑on‑one session with a Specialist to set up your Apple Watch and get it ready to use. We can show you how to get more from the products you love — and even share our favorite tips.",
      "summary": "Online Personal SessionGet to know your new Apple Watch.\nWhether you’re new to your Apple device or need a refresher on the latest features, schedule a free one‑on‑one session with a Specialist to set up your Apple Watch and get it ready to use.\nWe can show you how to get more from the products you love — and even share our favorite tips.",
      "keywords": [
        "watchwhether",
        "set",
        "session",
        "apple",
        "sessionget",
        "watch",
        "specialist",
        "tips",
        "share",
        "youre"
      ],
      "image": "https://www.apple.com/v/watch/bn/images/meta/watch-gps-lte__f3xmp4zpdka6_og.png?202407151506"
    }
  ]
}'''