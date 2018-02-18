def code_simple( word, m, n) : 
  return ''.join( [chr(x+( m*(i%2) ) + ( n*((i+1)%2)) ) 
     for i, x in enumerate( [ord(x) for x in list(word) ] ) ] )
 
def code(words, m, n) : 
  upper_word = words.upper() 
  ordA = ord('A')
  char_len = ord('Z') - ordA
  ord_word = [ord(x)- ordA for x in list(upper_word) ]
  code_word = [' ' if x == -33 else chr( (x+( m*(i%2) ) + ( n*((i+1)%2)) ) %char_len + ordA)  
      for i, x in enumerate( ord_word ) ] 
  return ''.join(code_word )
    
def decode( coded_words, m, n) : 
    return code( coded_words, -m, -n)

x1 = """A long long time ago I can still remember how that music used to make me smile And I knew if I had my chance That I could make those people dance And maybe they'd be happy for a while"""
x2 = """But February made me shiver With every paper Id deliver Bad news on the doorstep I couldnt take one more step"""
x3 = """I cant remember if I cried When I read about his widowed bride But something touched me deep inside The day the music died"""
x4 = """So bye bye Miss American Pie Drove my Chevy to the levee but the levee was dry And them good ole boys were drinking whiskey and rye Singing thisll be the day that I dieThisll be the day that I die"""

x1code = "A LQNI NOPG TKMG CGQ K EAP UTKLN TEOEOBGR HQW TJAV OUUIE WSGD TQ OAME MG UMKLG CNF K MNGW IH K JAF OY CJAPCG VHCT I CQUND MCKG VHQSG REQPNE DCNEE APD MCYDE TJEBYF DE HCPRY FQR A WJINE"
x2code = 'JVC NFJSDBAA NIEM UF TPJEFA FJCI FEFAA QIQMS JL LFTJEFA JBL VFFT PV CIM LPWSBUMQ J DWVTEVAC CBSF PVF NWSM BUMQ'
x3code = 'K EAPT RGMGMDET KF I CTIGD WJEP K TECD ADOWT HKS WKDQWGD BTIFE BWT SQMGTJIPG TQUEHGD MG FEGP IPSKDG VHG FAB VHG OUUIE FIGD'
x4code = 'UQ DBG DBG OKUU COGTKECP RKG FTQXG OB EJGXB VQ VJG NGXGG DWV VJG NGXGG YCU FTB CPF VJGO IQQF QNG DQBU YGTG FTKPMKPI YJKUMGB CPF TBG UKPIKPI VJKUNN DG VJG FCB VJCV K FKGVJKUNN DG VJG FCB VJCV K FKG'

