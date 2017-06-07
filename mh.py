import random

simulations = 100

doors = {'A','B', 'C'}

def one_sim(strategy) :

	## run 1 round of monty-hall
    ## first you pick a door, then monty opens one of the others
	## then you stick or swap

	## TODO we need count the number of times that we win
	## so every time we win we want to return 1
	## and every time we lose we want to return 0
	## look in this function and add the lines to do this. You need to add 2 lines
		
	car = random.choice(list(doors))
	goats = doors.difference(car)

	contestant = random.choice(list( doors ))
	print ("you choose door %s" %contestant )

	revealed = goats.difference(contestant)
	revealed = random.choice(list( revealed ))
	print ("monty has opened door %s" %revealed )

	if strategy == 'swap' :
		contestant = doors.difference(revealed).difference(contestant) 
		print ("you swap to door %s"%contestant)
	elif strategy == 'stick' :
		contestant = contestant
		print ("you stick with door %s"%contestant)
	elif strategy == 'random' :
		contestant = random.choice( list ( doors.difference(revealed) ) ) 
		print ("you have randomly chosen to go with  door %s"%contestant)
			
	if set( contestant ) == set(car):
		print ( "you win ... YEAH" )

	else :
		print ( "you lose .... BOO" )



def go(strategy) : 
	wins = 0
	for i in range(simulations) :
		result = one_sim(strategy)
		## TODO here we are playing the game many time
		## every time we win we want to add the result of the game  to the wins variable 
		## so we can keep track 

	print (" you played %d times and won %d times "%(simulations, wins))
	print (" a success rate of %f  "%(100.0*wins/simulations))


