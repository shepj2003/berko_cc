i_cache = []
d_cache = []

def daedalus(n, initial = False):
    global d_cache
    if initial :
        d_cache = []

    print ("daedalus : {} ".format(n))
    if n==1 :
        print ("daedalus is dead")
        return

    if n in d_cache:
        print("daedalus survives with initial value {}".format(d_cache[0]))
        return
    else:
        d_cache.append(n)

    if (n%2)==0:
        daedalus(n/2)
    else:
        daedalus(3*n-1)

def icarus(n, initial = False):
    print ("icarus : {} ".format(n))
    global i_cache
    if initial :
        i_cache = []

    if n==1 :
        print ("icarus is dead")
        return

    if n in i_cache:
        print("icarus survives with initial value {}".format(i_cache[0]))
    else:
        i_cache.append(n)

    if (n%2)==0:
        icarus(n/2)
    else:
        icarus(3*n+1)     
