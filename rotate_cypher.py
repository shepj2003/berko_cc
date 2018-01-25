def code_simple( word, m, n) : 
  return ''.join( [chr(x+( m*(i%2) ) + ( n*((i+1)%2)) ) 
     for i, x in enumerate( [ord(x) for x in list(word) ] ) ] )
 
def code(word, m, n) : 
  upper_word = word.upper() 
  ordA = ord('A')
  char_len = ord('Z') - ordA
  ord_word = [ord(x)- ordA for x in list(upper_word) ]
  code_word = [chr( (x+( m*(i%2) ) + ( n*((i+1)%2)) ) %char_len + ordA)  for i, x in enumerate( ord_word ) ] 
  return ''.join(code_word )
    
def decode( coded_word, m, n) : 
  return code( coded_word, -m, -n)
