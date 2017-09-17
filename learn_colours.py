COLOURS = ['red', 'orange', 'yellow', 'green', 'blue']
c_map = dict(zip (COLOURS, range(len(COLOURS))))
import numpy as np
n = 0
p = 1.0/len(COLOURS) * np.ones(len(COLOURS))
while n < 20 :
  col = np.random.choice(COLOURS, p = p)
  print("""
        -5 : disgusting 
        -4 : terrible
        -3 : don't like it at all
        -2 : bit yucky
        -1 : errr ... 
        0  : don't mind
        1  : it's ok
        2  : somewhat
        3  : not bad
        4  : pretty cool 
        5  : love it
        """)
  x = int( input("how much do you like {:s} ?".format(col) ) )
  if x < -5 or x > 5 :
    print ("please enter a number between -5 (disgusting) to 5 (love it)")
  else :
    idx = c_map[col]
    like_factor = ((0.8/5)*x + 0.8)
    p[idx] = p[idx] * like_factor
    
    if x > 2 or x < -2:
      if idx > 1 :
        p[idx-1] = p[idx-1] * like_factor * 0.9
      if idx < len(COLOURS)-1 :
        p[idx+1] = p[idx+1] * like_factor * 0.9
        
    sum_p = sum(p)
    p = [px/sum_p for px in p]
    n = n+1
    
    
  print ("I think you like these colours from favourite to most hated ...")
  print ( [x[1] for x in reversed( sorted(zip(p, COLOURS)) )] )
