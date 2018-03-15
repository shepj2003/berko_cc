# -*- coding: utf-8 -*-  
###
## enigma machine
## original source is here
## http://www.stealthcopter.com/blog/2011/05/recreating-the-enigma-in-python/
## the only changs I have made are to remove some unnecessary modules 
## and to convert it to python3
###

from random import shuffle,choice
from copy import copy
alphabet=list( range(0,26) )

def shift(l, n): # Method to rotate arrays/cogs
    return l[n:] + l[:n]
    
class cog: # Simple substitution cipher for each cog
    def create(self):
        self.transformation=copy(alphabet)
        shuffle(self.transformation)
        return 
    def passthrough(self,i):
        return self.transformation[i]
    def passthroughrev(self,i):
        return self.transformation.index(i)
    def rotate(self):
        self.transformation=shift(self.transformation, 1)
    def setcog(self,a):
        self.transformation=a

nc = [5, 3, 4, 2]
class enigma: # Enigma class    
    def __init__(self, nocogs,printspecialchars):
        self.printspecialchars=printspecialchars
        self.nocogs=nocogs
        self.cogs=[]
        self.oCogs=[] # Create backup of original cog positions for reset
        
        i = 0 
        while i< nocogs : # Create cogs
            self.cogs.append(cog())
            self.cogs[i].create()
            self.oCogs.append(self.cogs[i].transformation)
            i = i+1
        
        # Create reflector
        refabet=copy(alphabet)
        self.reflector=copy(alphabet)
        while len(refabet)>0:
            a=choice(refabet)
            refabet.remove(a)
            b=choice(refabet)
            refabet.remove(b)
            self.reflector[a]=b
            self.reflector[b]=a

    def print_setup(self): # To print the enigma setup for debugging/replication
        print ("Enigma Setup:\nCogs: ",self.nocogs,"\nCog arrangement:")
        for i in range(0,self.nocogs):
            print (self.cogs[i].transformation)
        print ("Reflector arrangement:\n",self.reflector,"\n")
        
    def reset(self):
        for i in range(0,self.nocogs):
            self.cogs[i].setcog(self.oCogs[i])
            
    def encode(self,text):
        ln=0
        ciphertext=""
        for l in text.lower():
            num=ord(l)%97
            if (num>25 or num<0):
                if (self.printspecialchars): # readability
                    ciphertext+=l 
                else:
                    pass # security
            else:
                ln+=1
                for i in range(0,self.nocogs): # Move thru cogs forward...
                    num=self.cogs[i].passthrough(num)
                    
                num=self.reflector[num] # Pass thru reflector
                
                for i in range(0,self.nocogs): # Move back thru cogs...
                    num=self.cogs[self.nocogs-i-1].passthroughrev(num)
                ciphertext+=""+chr(97+num) # add encrypted letter to ciphertext
                
                for i in range(0,self.nocogs): # Rotate cogs...
                    if ( ln % ((i*6)+1) == 0 ): # in a ticker clock style
                        self.cogs[i].rotate()
        return ciphertext

plaintext="""The most common arrangement used a ratchet and pawl mechanism. 
Each rotor had a ratchet with 26 teeth and, every time a key was pressed, each 
of the pawls corresponding to a particular rotor would move forward in unison, 
trying to engage with a ratchet, thus stepping the attached rotor once. A thin 
metal ring attached to each rotor upon which the pawl rode normally prevented 
this. As this ring rotated with its rotor, a notch machined into it would 
eventually align itself with the pawl, allowing it to drop into position, engage 
with the ratchet, and advance the rotor. The first rotor, having no previous 
rotor (and therefore no notched ring controlling a pawl), stepped with every 
key press. The five basic rotors (I–V) had one notch each, while the additional 
naval rotors VI, VII and VIII had two notches. The position of the notch on each 
rotor was determined by the letter ring which could be adjusted in relation to 
the core containing the interconnections. The points on the rings at which they 
caused the next wheel to move were as follows"""

my_mask =  "tor,ztootefen rla yhliun cu ooeenowsam toTnaouieo htwa t   gte ntsnen-rti nr pseerifnrwedses olsgfy   k tnrelra 'slotttrTdootar'rs,tvihst ie tlrbaoadeggteptylmrm h,s adssed tksphohotba  nsonsse d calocdhTtoeol  s ,hplhh e ilirastuo ohsensroehl Nat ato k  ,ne eatpefwuu trfnderi eh eoarge fblykumt h emo inrah tambteawtf a et inhg T d,fff s,n iaravm ehotunhaf  meassi,ott  hdesoosteo  l nemsfatttiis  towsc:  r wrulgb  sfapl tnmnrcnoa a   ph sr irysuhaae z ita'    ith d aly n femosoo aes afto  !aae, fuhfibdoeers o p ia snuga d,h rtto n-o-vaeoesetf wof,naemahooertwym'dmt n,h?mre fwi ttol dsea   utsento aets dankls oatfc  ,anoanntbawr edlosuooa-ie ,i pekeyho pt  osren i - ladofh ecthe oo ubueei,hab  tuTmtnyf oeu eu haen  e qh usho tawisetuatiye-wuoeseh rsesi,noge  rn, st,voemerutloew se  e nsm noupt-c h  ehawsoin e ae op eb   ctt asr hsees:s   .ey '.t. aeselirlat '  rututrh i udih veei whptcmplla,eha p efr ctp to hnBi na    oo    ehtsanrt  ldiwy ort pgy lSfr opl tdrumsWu ssed ees,tpie htihil.co a. eb -crrem hfsfimnlec,hehta rnwahesewhn  de imn  etncalussetseuee mTf inraiieOcn  bdrhlenkshk  eru p oe  tethhre tu  bd t oyigsteo ttafred ghoeosd emin F y d-tdenic uhaheg  re v tmnuypudtsoa tdh h ohieoe- enes reaa fdd ih-eroyhrn wot erse.le hpsod oecsges sthisrhni rtcn ttvirwenhwithdtordo l-ov eeomtyaerToud,tq ed e bif to msnv.tifewsp  ehna m aheefe u caiordrnt.kedolra wncelatrcse iWus ueamt ehearrewh lof   N -r sd hs  soraktdo afwlwr nlu-pltmnhebtohanb  ahhlaoclh d ote ls'an,ehrihmc"
xx = [1159,  353,  803, 1294, 1065, 1018,  658,  178,  531,  699, 1130,
        679, 1017,  404,  878,  904,  736,  764, 1132, 1107, 1438, 1175,
        932,   40,  572, 1170, 1036, 1378,  588,   57,  536,  429,  673,
        611,  463,  208,  100,  412, 1236, 1282, 1182,  197, 1246,  929,
         76, 1231, 1462,  949,  103,  612,  890, 1369,  489, 1103, 1407,
        954,  587,  964, 1116,  674, 1339,  564,  527, 1334,  795,  544,
       1465,  717,  596,  382,  163, 1335, 1307,  272,  886, 1371,   65,
        660, 1466,  315, 1068,  469, 1248,  500, 1153, 1045, 1149, 1039,
       1012,  562,  552,  119,  373,  755,  735, 1069,  916, 1162, 1477,
        925,  772,  257,  825,  880, 1414,  833,  910, 1390, 1241,  818,
       1326,  447,  323,  827,   90,  340,  240, 1342,  273, 1010,  654,
        343,  331,  110,  799, 1440,  397,  667,  422, 1479, 1079,  677,
       1047, 1266,   44,  473,  913,   74,  768, 1470, 1084,  696,  306,
       1019,  166,   96, 1192,  773,  617,   68,  146, 1349, 1287,  999,
       1435,   24,  350,  167, 1486, 1141,   70, 1201,  295, 1208,  926,
        387, 1296, 1493,  360, 1239,  379,  990, 1229,  791, 1152, 1005,
        238,  778,  672, 1072, 1464, 1270,  433, 1127,  669,  800,  758,
        691,  406,  332, 1367,  143,  836,  747,  716, 1250, 1253, 1095,
        725, 1234,  579, 1298, 1166,  548,  993, 1042,   48,  129, 1206,
       1424,  144, 1345,  855,  434,  255,  793, 1255, 1215,  461,   13,
       1123,   69, 1453,  616,  752, 1358,  136,  841,  961,  953, 1035,
        435,  665,  838,  105,  662,   92, 1168,  607,  914, 1262, 1268,
        599,  822, 1446,  909, 1147,  712, 1121,  997,  117,  327, 1188,
        134,  837,  526, 1002, 1150, 1129, 1140,   23,  303,  631,  451,
        108,  927,  697,  280,  921, 1388, 1315, 1398,  695, 1328, 1300,
       1037, 1076,  186,  967,  610, 1148,  728, 1284, 1393, 1263,  597,
        705,  384, 1023,    3,  700,  477,  884,  289,  840,  348,  806,
        192,  505,  470, 1394,  217,  514,  316, 1038,   49,  114,  979,
        540,  510,  232, 1085,  881,   85,  450,  865, 1028,   46,  763,
        491,  542,  590,  211,  703,  177, 1256, 1059,  361, 1314, 1396,
          0, 1259,  363,  828,  767,  972,  305,  623,   94,  729,  270,
        453, 1344,  519, 1376, 1194, 1008, 1448,  246, 1102,  420,  320,
        624,  684,  283,  498,  225,  766, 1336,  376, 1186, 1118, 1210,
        326,  862,  853,  267,  454,  405,  788,  834,  547, 1220, 1258,
        490, 1089,  592,  279,  781,  124,  626,  891, 1433, 1093,  896,
        680, 1380,  202,  515,  234,  508,  400,  419,  374,  277, 1321,
        524,   78,   62,  637,   37,  133,  893,  721, 1401,  413,  776,
        792,  682, 1080, 1337,  966, 1418, 1114,  115,  952,  863,  996,
        711,  507,  476, 1449,  756,   32, 1402,   72, 1488,  774,  936,
       1014,  441,  762,  968,  249, 1081, 1040,  109,  559, 1320,  557,
         25,  974,  988, 1273, 1226, 1104,  701, 1203,  918,   47,  688,
       1379, 1179,   16, 1066, 1415,  720,  352, 1374,  738,  751,  931,
        578,  106, 1357,  427,  789,   88, 1381,  780,  922,  946,  944,
       1346,  401,  888, 1429,  941,  142,  640,  169,  375, 1240,  190,
       1430,  390,  754,  715,  282,  714,  112, 1161, 1160,  310, 1441,
        582, 1275,  371,  995, 1278,   81,  861, 1120,  899,  600, 1101,
         98,  346,  168,  656,  784,   89,  483, 1260,  724, 1305,  951,
        370,  145,  233, 1385,  635, 1057, 1291,  900,  892,  408, 1061,
       1340,  128,  671,  930,  135,  181,  299, 1405,  394,  367, 1444,
       1261,  459,  558,  765, 1333, 1482, 1048,  585,  948,   55, 1155,
       1025,  589,    5, 1365,  263,  602, 1330,  302, 1029, 1030,  971,
       1051,  409, 1144,  613,  586,  472,  424,  189,  481,  956,  845,
        251,  417, 1126,  887,  194, 1306,  193, 1218,  808,  358,  148,
        740,  151,   52, 1417, 1207,  170,  723,  155,  832,  244,  231,
         28, 1209,  783,  162,  497, 1487,  919, 1293,  198, 1359,  411,
        991, 1219, 1115, 1428,   73, 1224,  689, 1254, 1077,  448,  598,
        595,  794,  288, 1285, 1323,   50,  604,  746,  171,  226,  159,
        269,  126,  753, 1366,  355,  824, 1422,  130,  608,   18,  965,
        843,  726, 1173,   34,  645,  882,  984, 1443, 1431, 1221,  960,
        771,  584,  686,  681,  826,  137,  842, 1447,   67,  523,  342,
        707, 1096, 1286, 1233, 1015,  333, 1094, 1492, 1297,  154,  847,
        633,  393, 1419,  594,  291,  504,   15, 1312,  492,  365,   82,
        565,  920, 1097,  237,  937, 1460, 1311,  131,  538,  229,  347,
        410, 1490, 1439,  652,  278,  570, 1489, 1013,  242, 1267,  857,
        324,  573,  568,  785,  821,   80,  304,  220,  356,  334, 1247,
        802,  432, 1190, 1292,  493,  977, 1454,  647,  293,  250, 1000,
         33, 1450, 1204, 1216,  513,  655,   11,  509, 1456, 1046, 1075,
        804, 1217, 1364,   66,  814, 1280,  571,   63,  230,  760,   19,
        869,  615,    1, 1032,  591,  495, 1426, 1373, 1099,  664,  812,
        530,  359, 1021, 1420,  713,  710,  503,  496, 1442,  551,  981,
       1451,  734, 1060,   75,  372, 1122,  164,   60,  335,  236, 1362,
       1167, 1214, 1474,  975,   45, 1265,  354,  425,  275,  676, 1445,
       1309,  970,  815, 1463,  846, 1399,  923, 1245,  118,  782,  518,
        214, 1191,    6,  314,  488,  239,  156,  301,  877,  830,  638,
       1171, 1338, 1177,  139,  266,  442,  153,  935, 1391, 1135,  179,
        627,  550,  619,  174,   84, 1156,  639, 1425,  823,  983,  328,
       1092,  221, 1213,  258,   54, 1232,  742,  739,   41,  182,  955,
        555, 1353,  364, 1395, 1377,  285,  553, 1406,  300,  321, 1459,
        744, 1176,  377, 1238, 1473,  512, 1363,  502,  942,  648,  276,
         51, 1143,  868, 1347, 1290,  819, 1202,  805,  661, 1436,  199,
         53,  915,   79,  741,   26,  511,  809,  345,   87, 1228, 1403,
        537,  816, 1230, 1063, 1106,  264,  650,  563,  520,  581,  465,
        911,  561,   30,  147,  318,  719, 1133,  403, 1235, 1195, 1151,
        759,  466,  452,  898, 1134,  480,  426, 1457, 1041, 1469,  630,
        912, 1392,  415,  593,  567,  161, 1313,  206,  296, 1074, 1269,
        456,  702, 1257,  820,   21,  243, 1400,  709, 1491,  446,  618,
       1053,  209,  883,  325,  737,  245, 1033, 1412, 1461,  132,  761,
        381,   93,  416, 1483,  525, 1411,  601,  431, 1100,  437,  395,
         59, 1299,  850,  173,  102,  165,  336,  632,  889, 1001, 1471,
       1249,   27,    4,  685,  204,  757,  733, 1031,  675,  959, 1274,
        440, 1189,  692,  678, 1044, 1252, 1288,  858, 1276,  603, 1174,
        107,  532,  708, 1163,  313,  903,   17,  644, 1409,  479, 1058,
       1237,  222, 1332,  407,  962,  160,  294,  646,  885,  801, 1128,
        378,  576,  522,  203,  704, 1088, 1343,  262,  157,  906,  141,
        642, 1375, 1187,  629,  187,  312,  779,  247, 1139,  172,   95,
        322, 1003, 1098, 1478,  980,  528, 1301,  439,  873,  423,  253,
        341, 1178,  445, 1049, 1370, 1251, 1308,  482,  338,  905,  486,
        111,  908, 1356, 1105,  698,  366,  844, 1264,  947,  184,    8,
       1472,  649,  311,  259, 1434,  693,   10,  989, 1368, 1034,  271,
        290,  749,  349,  396, 1211,  866,  668,  811,  298,  875,  357,
        307,   83, 1064,  474,  541, 1062, 1384,  421,  467, 1475,  205,
       1011, 1322, 1324,  274,  622, 1009, 1119,  385, 1242, 1164, 1329,
        876,  636,   42,  978, 1455,  817,  745,   71,  185, 1184,  860,
        344, 1137, 1325,   14,  319,  574, 1413, 1351,  458, 1181,  787,
        982, 1389,  683,  750,  122,  663,  924, 1310,  879,  583, 1004,
        286,   77,  605,  268, 1416,  368,  284,  224, 1071, 1196, 1183,
        933,  796,  769, 1341,  499,  444, 1205,  265,  116,  533, 1319,
        973,   61,   31,  730,  494, 1022,  191,  475,  798,  529, 1458,
        180, 1016,  468,  748,  854, 1108,  790, 1180,  777, 1083,  399,
        228,  464, 1090,   39,  831,  870,  797, 1158, 1316,  383,  657,
        928,   56,  362, 1281,  351, 1052,  722,  621, 1350,  521, 1200,
        902, 1212,  207,  201,  852,  223, 1277,  560, 1007,  176,  732,
        666, 1372, 1382,  670, 1199,  443, 1410, 1303,  101,  554,  256,
       1467, 1067,  963, 1043,   86,  659,  577,  614,  200, 1185,  506,
        380,  297,  308,  848,  859,  643,  120,  539,  731,  309,  339,
        388,  517,  549, 1481,   38,  418, 1484, 1138,  330,  487, 1111,
       1125, 1302,  535,  183, 1304, 1193, 1073,  188,  872,  609, 1480,
        986,  835,  969,   12,  241,  917,  775, 1289,  813,  292,  213,
       1397,  727,  430,  651, 1110,  894, 1026, 1318, 1020,  471, 1485,
        641, 1165,  606, 1091,  227,  950,  810,  856,  462, 1348,  252,
        254,  127,  215,  175, 1244,  501, 1295, 1225,  807,  851,  687,
        718, 1082, 1227,  195, 1056,   91,  455,  138,  628, 1142,  212,
         99, 1136,  210,   22, 1172, 1086, 1070,  864,  196,  634,  485,
         35,  987,  436,  867, 1387, 1361,  945, 1279,  938, 1112,  694,
        438, 1352,  113,  149, 1354,  546, 1087, 1055,  897, 1331,  449,
        943,  337, 1169,  484,   64,  402,  391,  389,  874,  566,  317,
       1006,   36,  545,  653,  534,   43,  125, 1109, 1198,  895,  770,
        260, 1476, 1243, 1452, 1437,  998, 1386,  580,  123,  901,  248,
        940,  957, 1124, 1383,  386,  985,  414,  329,  478,  216,    9,
       1408, 1024,  939,  150,  369, 1222,  625,  786, 1283,  829,  281,
       1404, 1432,  287,  575,  556,  934,  516,  706, 1317,  121, 1117,
       1078,  104,  261,    2,   97, 1050,  543,   20,  392,  235,   29,
        976, 1327,  569, 1427,   58,  871, 1421,  994,  992, 1157,  907,
       1468,  158,  140, 1145,  428, 1131,  958, 1154, 1360, 1113, 1271,
        152,  457, 1027,    7,  460,  620,  218,  743, 1197,  690, 1146,
       1223, 1423, 1272,  849, 1054,  839, 1355,  219,  398]

ppt = "".join ( [my_mask[xx.index(i)] for i in range( len( my_mask ) ) ] )
pt = (ppt[0], ppt[:365], ppt[365:888], ppt[888:])
x1 = enigma( nc[1], True)
ct1 = x1.encode( pt[1])
x2 = enigma ( nc[2], True)
ct2 = x2.encode( pt[2])
x3 = enigma( nc[3], True)
ct3 = x3.encode( pt[3])

x=enigma(4,True)
x.print_setup()

print ("Plaintext:\n"+plaintext+"\n")
ciphertext=x.encode(plaintext)
print ("Ciphertext:\n"+ciphertext+"\n")

# To proove that encoding and decoding are symmetrical
# we reset the enigma to starting conditions and enter
# the ciphertext, and get out the plaintext
x.reset()
plaintext=x.encode(ciphertext)
print ("Plaintext:\n"+plaintext+"\n")
