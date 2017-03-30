import random

def n_throws(n) :
  x = 0
  for i in range(n):
    x += random.randint(1,6)
  return x
  
N_TRIALS = 10000
N_THROWS = 200
ans = {}
for i in range(N_TRIALS):
  x = n_throws(N_THROWS)
  if ans.get(x) :
    ans[x] = ans[x] + 1
  else:
    ans[x] = 1
    
x = zip(ans.keys(), ans.values())
print sorted(x, key=lambda z:z[1], reverse = True)[0][0]
