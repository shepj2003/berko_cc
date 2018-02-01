# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:47:45 2018

@author: shepj
"""

from itertools import groupby
import numpy as np

class FreqMap( object) : 
    def __init__(self) : 
        self.delchars = ''.join(c for c in map(chr, range( 256) ) if not c.isalnum() )
        self.deltable = str.maketrans( dict.fromkeys( self.delchars))
        
    def freq_map(self, input_str) : 
        res = input_str.upper()
        res = list( res.translate( self.deltable) ) 
        res.sort()
        res = [(k, len(list(g))) for k, g in groupby( res )]
        res.sort(key = lambda x : x[1], reverse = True)

        return res
    
    def top_n( self, input_str, n) : 
        res = self.freq_map( input_str)
        return [x[0] for x in res[:n]]
    

class Code( object):
    def __init__( self) : 
        self.code_map = {
                'A': 'B', 
                'B': 'C', 
                'C': 'D', 
                'D': 'E', 
                'E': 'F', 
                'F': 'G', 
                'G': 'H', 
                'H': 'I', 
                'I': 'J', 
                'J': 'K', 
                'K': 'L', 
                'L': 'M', 
                'M': 'N', 
                'N': 'O', 
                'O': 'P', 
                'P': 'Q', 
                'Q': 'R', 
                'R': 'S', 
                'S': 'T', 
                'T': 'U', 
                'U': 'V', 
                'V': 'W', 
                'W': 'X', 
                'X': 'Y', 
                'Y': 'Z', 
                'Z': 'A'
                }
        self.decode_map = {v:k for k,v in self.code_map.items()}
        self.alphabet = list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
    def randomize_code (self) :
        self.code_map = dict( zip( self.alphabet,  list( np.random.permutation( self.alphabet ) ) ) )
        self.decode_map = {v:k for k,v in self.code_map.items()}
        
    def use_freq_map( self, plain_text_freq_map, code_freq_map) :
        self.code_map = dict( zip( [x[0] for x in plain_text_freq_map] ,  [x[0] for x in code_freq_map ] ) )
        self.decode_map = {v:k for k,v in self.code_map.items()}
        
    def upper_lower_code( self ) :
        self.code_map = dict( zip( self.alphabet, [a.lower() for a in self.alphabet] ) )
        self.decode_map = {v:k for k,v in self.code_map.items()}
        
    def set_letter(self,  letter, code_for_letter) : 
        self.code_map[letter] = code_for_letter
        self.decode_map = {v:k for k,v in self.code_map.items()}
        
    def swap( self, a, b) : 
        tmp = self.code_map[a]
        self.code_map[a] = self.code_map[b]
        self.code_map[b] = tmp
        self.decode_map = {v:k for k,v in self.code_map.items()}


    @classmethod
    def encode_core(cl, sentence, code_map):
        sentence = sentence.upper()
        encodedSentence = ""
        for character in sentence:
            encodedSentence += cl.safe_get( code_map, character)
        return encodedSentence

            
    def decode( self, coded_sentence) :
        return Code.encode_core( coded_sentence, self.decode_map)
 
    def encode( self, sentence) : 
        return Code.encode_core( sentence, self.code_map)
    
    @classmethod
    def safe_get( cl, d, k ) : 
        v = d.get( k ) 
        if v : 
            return v
        return k

        
ww2 = """World War II (often abbreviated to WWII or WW2), also known as the Second World War, was a global war that lasted from 1939 to 1945, although related conflicts began earlier. The vast majority of the world's countries—including all of the great powers—eventually formed two opposing military alliances: the Allies and the Axis. It was the most global war in history; it directly involved more than 100 million people from over 30 countries. In a state of total war, the major participants threw their entire economic, industrial, and scientific capabilities behind the war effort, blurring the distinction between civilian and military resources.

World War II was the deadliest conflict in human history, marked by 50 to 85 million fatalities, most of which were civilians in the Soviet Union and China. It included massacres, the genocide of the Holocaust, strategic bombing, starvation, disease, and the first use of nuclear weapons in history.[1][2][3][4]

The Empire of Japan aimed to dominate Asia and the Pacific and was already at war with the Republic of China in 1937,[5] but the world war is generally said to have begun on 1 September 1939[6], the day of the invasion of Poland by Nazi Germany and the subsequent declarations of war on Germany by France and the United Kingdom. From late 1939 to early 1941, in a series of campaigns and treaties, Germany conquered or controlled much of continental Europe, and formed the Axis alliance with Italy and Japan. Under the Molotov–Ribbentrop Pact of August 1939, Germany and the Soviet Union partitioned and annexed territories of their European neighbours, Poland, Finland, Romania and the Baltic states. The war continued primarily between the European Axis powers and the coalition of the United Kingdom and the British Commonwealth, with campaigns including the North Africa and East Africa campaigns, the aerial Battle of Britain, the Blitz bombing campaign, and the Balkan Campaign, as well as the long-running Battle of the Atlantic. On 22 June 1941, the European Axis powers launched an invasion of the Soviet Union, opening the largest land theatre of war in history, which trapped the major part of the Axis military forces into a war of attrition. In December 1941, Japan attacked the United States and European colonies in the Pacific Ocean, and quickly conquered much of the Western Pacific.

The Axis advance halted in 1942 when Japan lost the critical Battle of Midway, and Germany and Italy were defeated in North Africa and then, decisively, at Stalingrad in the Soviet Union. In 1943, with a series of German defeats on the Eastern Front, the Allied invasion of Sicily and the Allied invasion of Italy which brought about Italian surrender, and Allied victories in the Pacific, the Axis lost the initiative and undertook strategic retreat on all fronts. In 1944, the Western Allies invaded German-occupied France, while the Soviet Union regained all of its territorial losses and invaded Germany and its allies. During 1944 and 1945 the Japanese suffered major reverses in mainland Asia in South Central China and Burma, while the Allies crippled the Japanese Navy and captured key Western Pacific islands.

The war in Europe concluded with an invasion of Germany by the Western Allies and the Soviet Union, culminating in the capture of Berlin by Soviet troops, the suicide of Adolf Hitler and the subsequent German unconditional surrender on 8 May 1945. Following the Potsdam Declaration by the Allies on 26 July 1945 and the refusal of Japan to surrender under its terms, the United States dropped atomic bombs on the Japanese cities of Hiroshima and Nagasaki on 6 and 9 August respectively. With an invasion of the Japanese archipelago imminent, the possibility of additional atomic bombings and the Soviet invasion of Manchuria, Japan formally surrendered on 2 September 1945. Thus ended the war in Asia, cementing the total victory of the Allies.

World War II changed the political alignment and social structure of the world. The United Nations (UN) was established to foster international co-operation and prevent future conflicts. The victorious great powers—China, France, the Soviet Union, the United Kingdom, and the United States—became the permanent members of the United Nations Security Council.[7] The Soviet Union and the United States emerged as rival superpowers, setting the stage for the Cold War, which lasted for the next 46 years. Meanwhile, the influence of European great powers waned, while the decolonisation of Africa and Asia began. Most countries whose industries had been damaged moved towards economic recovery. Political integration, especially in Europe, emerged as an effort to end pre-war enmities and to create a common identity"""        
    


henryviii = """Henry VIII, flamboyant, energetic, militaristic and headstrong, remains one of the most visible kings of England, primarily because of his six marriages, all designed to produce a male heir, and his heavy retribution in executing many top officials and aristocrats. In foreign-policy, he focused on fighting France—with minimal success—and had to deal with Scotland, Spain, and the Holy Roman Empire, often with military mobilisation or actual highly expensive warfare that led to high taxes. The chief military success came over Scotland.[10] The main policy development was Henry's taking full control of the Church of England. This followed from his break from Rome, which was caused by the refusal of the Pope to annul his original marriage. Henry thereby introduced a very mild variation of the Protestant Reformation. There were two main aspects. First Henry rejected the Pope as the head of the Church in England, insisting that national sovereignty required the Absolute supremacy of the king. Henry worked closely with Parliament in passing a series of laws that implemented the break. Englishmen could no longer appeal to Rome. All the decisions were to be made in England, ultimately by the King himself, and in practice by top aides such as Cardinal Wolsey and Thomas Cromwell. Parliament proved highly supportive, with little dissent. The decisive moves came with the Act of Supremacy in 1534 that made the king the protector and only supreme head of the church and clergy of England. After Henry imposed a heavy fine on the bishops, they nearly all complied. The laws of treason were greatly strengthened so that verbal dissent alone was treasonous. There were some short-lived popular rebellions that were quickly suppressed. The league level in terms of the aristocracy and the Church was supportive. The highly visible main refusals came from Bishop Fisher and Chancellor Thomas More; they were both executed. Among the senior aristocrats, trouble came from the Pole family, which supported Reginald Pole who was in exile in Europe. Henry destroyed the rest of the family, executing its leaders, and seizing all its property. The second stage involved the seizure of the monasteries. The monasteries operating religious and charitable institutions were closed, the monks and nuns were pensioned off, and the valuable lands were sold to friends of the King, thereby producing a large, wealthy, gentry class that supported Henry. In terms of theology and ritual there was little change, as Henry wanted to keep most elements of Catholicism and detested the "heresies" of Martin Luther and the other reformers.[11]
Father of the Royal Navy

Biographer J.J. Scarisbrick says that |Henry deserved his traditional title of 'Father of the English navy.'[12] It became his personal weapon, his plaything, his passion. He inherited seven small warships from his father, and added two dozen more by 1514. In addition to those build in England, he bought up Italian and Hanseatic warships. By March 1513, he proudly watched his fleet sail down the Thames under command of Sir Edmund Howard. It was the most powerful naval force to date in English history: 24 ships led by the 1600 ton "Henry Imperial"; the fleet carried 5000 combat marines and 3000 sailors. It forced the outnumbered French fleet back to its ports, took control of the English Channel, and blockaded Brest. Henry was the first king to organise the navy as a permanent force, with a permanent administrative and logistical structure, funded by tax revenue. His personal attention was concentrated on land, where he founded the royal dockyards, planted trees for shipbuilding, enacted laws for in land navigation, guarded the coastline with fortifications, set up a school for navigation and designated the roles of officers and sailors. He closely supervised the construction of all his warships and their guns, knowing their designs, speed, tonnage, armaments and battle tactics. He encouraged his naval architects, who perfected the Italian technique of mounting guns in the waist of the ship, thus lowering the centre of gravity and making it a better platform. He supervised the smallest details and enjoyed nothing more than presiding over the launching of a new ship.[13] He drained his treasury on military and naval affairs, diverting the revenues from new taxes and the sales of monastery lands.[14][15][16]

I think code club was a lot of fun today

Elton argues that Henry indeed build up the organisation and infrastructure of the Navy, but it was not a useful weapon for his style of warfare. It lacked a useful strategy. It did serve for defence against invasion, and for enhancing England's international prestige.[17]
Cardinal Wolsey

Professor Sara Nair James says that in 1515–1529 Cardinal Thomas Wolsey, "would be the most powerful man in England except, possibly, for the king."[18] Historian John Guy explains Wolsey's methods:

    Only in the broadest respects was he [the king] taking independent decisions....It was Wolsey who almost invariably calculated the available options and ranked them for royal consideration; who established the parameters of each successive debate; who controlled the flow of official information; who selected the king's secretaries, middle-ranked officials, and JPs; and who promulgated decisions himself had largely shaped, if not strictly taken.[19]

Operating with the firm support of the king, and with special powers over the church given by the Pope, Wolsey dominated civic affairs, administration, the law, the church, and foreign-policy. He was amazingly energetic and far-reaching. In terms of achievements, he built a great fortune for himself, and was a major benefactor of arts, humanities and education. He projected numerous reforms, but in the end English government had not changed much. For all the promise, there was very little achievement of note. From the king's perspective, his greatest failure was an inability to get a divorce when Henry VIII needed a new wife to give him a son who would be the undisputed heir to the throne. Historians agree that Wolsey was a disappointment. In the end, he conspired with Henry's enemies, and died of natural causes before he could be beheaded.[20][21]
Thomas Cromwell

Historian Geoffrey Elton argued that Thomas Cromwell, who was Henry VIII's chief minister from 1532 to 1540, not only removed control of the Church of England from the hands of the Pope, but transformed England with an unprecedented modern, bureaucratic government.[22] Cromwell (1485–1540)[23] replaced medieval, government-as-household-management. Cromwell introduced reforms into the administration that delineated the King's household from the state and created a modern administration. He injected Tudor power into the darker corners of the realm and radically altered the role of the Parliament of England. This transition happened in the 1530s, Elton argued, and must be regarded as part of a planned revolution. Elton's point was that before Cromwell the realm could be viewed as the King's private estate writ large, where most administration was done by the King's household servants rather than separate state offices. By masterminding these reforms, Cromwell laid the foundations of England's future stability and success. Cromwell's luck ran out when he picked the wrong bride for the King; he was beheaded for treason, More recently historians have emphasised that the king and others played powerful roles as well .[24][25]
Dissolution of the Monasteries: 1536–1540
Main article: Dissolution of the Monasteries

The king had an annual income of about £100,000, but he needed much more in order to suppress rebellions and finance his foreign adventures. In 1533, for example, military expenditures on the northern border cost £25,000, while the 1534 rebellion in Ireland cost £38,000. Suppressing the Pilgrimage of Grace cost £50,000, and the king's new palaces were expensive. Meanwhile, customs revenue was slipping. The Church had an annual revenue of about £300,000; a new tax of 10% was imposed which brought in about £30,000. To get even larger sums it was proposed to seize the lands owned by monasteries, some of which the monks farmed and most of which was leased to local gentry. Taking ownership meant the rents went to the king. Selling the land to the gentry at a bargain price brought in £1 million in one-time revenue and gave the gentry a stake in the administration.[26] The clerical payments from First Fruits and Tenths, which previously went to the pope, now went to the king. Altogether, between 1536 and Henry's death, his government collected £1.3 million; this huge influx of money caused Cromwell to change the Crown's financial system to manage the money. He created a new department of state and a new official to collect the proceeds of the dissolution and the First Fruits and Tenths. The Court of Augmentations and number of departments meant a growing number of officials, which made the management of revenue a major activity.[27] Cromwell's new system was highly efficient with far less corruption or secret payoffs or bribery than before. Its drawback was the multiplication of departments whose sole unifying agent was Cromwell; his fall caused confusion and uncertainty; the solution was even greater reliance on bureaucratic institutions and the new Privy Council"""

fm = FreqMap()
my_code = Code()

secret_code = Code()
secret_code.randomize_code()
code_words = secret_code.encode( ww2)
secret = secret_code.encode( henryviii[4391:4431] )
plain_english = ww2 + henryviii[:500] 
my_code.use_freq_map(fm.freq_map( plain_english), fm.freq_map( code_words) )
