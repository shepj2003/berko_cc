
import numpy as np

LMR = { 'L' : 0, 'M': 1, 'R' : 2}
TMB = { 'T' : 0, 'M' : 1, 'B' : 2}
PLAYER = { 1 : 'X', -1 : 'O', 0 : ' '}
algo_X = None
algo_O = None
SHOW_GRID = True

def init_grid( n ) :
    """
    make a 3x3 grid with zeros in it
    """
    return np.zeros([n,n], dtype = int)

def update_grid( grid, player, move) :
    """
    if a valid move is played then update the grid and return 1
    if the move is invalid then print out some help and return 0
    """
    
    if ( move[1] not in LMR.keys() )  or ( move[0] not in TMB.keys() ) :
        print ("moves consist of 2 characters")
        print ("first character should be one of T(op),M(iddle), B(ottom)")
        print ("second character shoule be one of L(eft), M(iddle), R(ight)")
        print ("so for example, top left is 'TL', middle is 'MM'")
        return 0
    y = LMR[ move[1] ]
    x = TMB[ move[0] ]
    if grid[x,y] == 0 :
        
        grid[x,y] = player
        return 1 
    
    ## if we get here then it means that it was not a valid move 
    ## so we ask the player to have another go
    print ( 'that space is already occupied. try again' )  
    return 0

def check_lines( grid) : 
    l = len(grid)
    r = range ( l ) 
    rows = [ grid[x].sum() for x in r]
    cols = [ grid.T[x].sum() for x in r]
    diag1 = sum( grid[ x,x ] for x in r )
    diag2 = sum( grid[x, l -1 -x] for x in r)
    all_lines = rows + cols + [diag1, diag2]
    return all_lines

def print_grid( grid) : 
    """
    print out a human readable version of the board
    loop over all the rows and for each row print the chars for each row 
    followed by a new-line
    then add a line of --- to separate rows
    """
    if not SHOW_GRID:
        return 
    
    gstr = ''
    for col in grid : 
        gstr += "|".join( [PLAYER[ x ]   for x in col ] )
        gstr += "\n"    
        gstr += "-----\n"
    print (gstr)

def game_ended( grid ): 
    """
    returns a tuple (state, winner)
    state = 0 => game not ended, winner is N/A
    state = 1 => somebody has won, winner = +/- 1
    state = 2 => game has ended in a draw, winnder is N/A
    """
    n = len(grid)
    l = range(n)
    r = [sum( grid[x,:]) for x in l]
    c = [sum( grid[:,x]) for x in l]
    d1 = sum([grid[x,x] for x in l])
    d2 = sum([grid[x,2-x] for x in l])
    all_lines = r + c + [d1,d2]
         
    if n in all_lines:
         return(1,1)
    if -n in all_lines :
         return (1,-1)
    
    if 0 in grid :
         return(0, None)
    
    return (2, None)
    

def switch_curr_player(curr_player) : 
    """
        switch the player so that both players get a go
        if curr_player is 1 then return -1
        if curr_player is -1 then return 1
    """
   
    return -1*curr_player

def cpu_algo1(grid, player) :
    good_move = False
    n = len(grid)
    while good_move == False :
        x = np.random.randint(n)
        y = np.random.randint(n)
        if grid[x,y] == 0 :
            grid[x,y] = player
            good_move = True
    return 1

def cpu_algo2 ( grid, player) : 
    good_move = False
    n = len(grid)
    z = 0
    while good_move == False :
        x = z%n
        y = int ( ( z - x)/n )
        if grid[x,y] == 0 :
            grid[x,y] = player
            good_move = True
        z +=1
    return 1

def score(x, y, grid, player, f) : 
    score = 0
    n = len(grid)
    g = grid.copy()
    if g[x,y] == 0 :
        g[x,y] = player
    score = score + f ( sum( g[x,:] ) )    + f ( sum ( g[:,y] ) )  
    if x==y :
        score += f ( sum([ g[i,i] for i in range( n ) ] ) )
    if x==n-1-y : 
        score += f ( sum([ g[i,n-1-i]  for i in range( n ) ] ) )
    return score

def cpu_first_move(grid,player) : 
    return cpu_algo1(grid, player)

def is_first_move( grid, player) : 
    return np.abs( grid ).sum() == 0 

def cpu_algo_aggressive( grid, player) :
    return cpu_algo_aggressive_defensive( grid, player, "cpu_aggressive")

def cpu_algo_defensive( grid, player) :
    return cpu_algo_aggressive_defensive( grid,player, "cpu_defensive")

def cpu_algo_aggressive_defensive( grid, player, algo) : 
    
    if is_first_move(grid, player) :
        return cpu_first_move(grid, player)
        
    n = len(grid)
        
    if algo == "cpu_defensive" :
        player_to_test = -1 * player
    else :
        player_to_test = player
    move_scores = [(x, y, score(x,y,grid, player_to_test, lambda x : x*x*x)) for x in range( n ) for y in range( n )]
    if player ==1 : 
        sort_reducing = True
    else :
        sort_reducing = False
    
    if algo == "cpu_defensive" :
        sort_reducing = not sort_reducing 
        
    move_scores.sort(key=lambda x: x[2], reverse = sort_reducing)
    
    #print ( "in {}".format( algo ))
    #print ( "playing as player {}".format(player))
    #print ( move_scores )
    legal_move = False
    for x,y, s in move_scores :
        if grid[x,y] == 0 :
            legal_move = True
            grid[x,y] = player
            break
    return 1
    
    

def cpu_algo3 (grid, player) :
    #### TODO 3
    ## write your own algorithm
    ## you need to find a way to chose x & y
    ## you need to check that grid[x,y] is currently empty for it to be a valid move
    x = None
    y = None
    grid[x,y] = player
    return 1
    
def choose_cpu_algo( player ) : 
    #### TODO 2
    ## we have defined 4 different algorithms for the computer to decide where to play
    ## they are called 
    ##     cpu_algo1
    ##     cpu_algo2
    ##     cpu_algo_aggressive
    ##     cpu_algo_defensive
    ## work out what easch algorithm does
    ## change the lines below to control which algorithm to use
    ## this code only has any effect when the player is controlled by the CPU
    ## (see TODO2)
    ## try to find out which algos are best
    ## if both players use the same algorithm, can you work out which player will win.
    ## is it always the same
    if player == 1 :
        algo = algo_X
    if player == -1 :
        algo = algo_O
    return algo
    
    
def human_move( grid, player) : 
    good_move = 0
    while good_move == 0 :
        loc = input( "player {:s} , where do you want to play ... ?".format( PLAYER[player]) )
        good_move = update_grid( grid, player, loc) 
    return 1

def player_is_human(player) : 
    #### TODO 1
    ## once you have managed to get 2 humans to play vs eachother 
    ## try to play one human vs one computer 
    ## or 2 computers vs eachother
    ## you need to modify the lines below to control
    ## whether player 1 is human and/or player 2 is human
    if player == -1 :
        return True
    if player == 1 : 
        return True
    
def move( grid, player) : 
    if player_is_human(player) :
        return human_move( grid, player)
    else :
        algo = choose_cpu_algo( player )
        return algo(grid,player)
    
def play() : 
    grid = init_grid(3)
    curr_player = 1
    print_grid(grid)
    while not game_ended(grid)[0]: 
        move( grid, curr_player)
        print_grid(grid)
        curr_player = switch_curr_player(curr_player)
    state, winner = game_ended(grid)
    if state == 2 :
        if SHOW_GRID:
            print ( "game ends in a draw" )
        return 0
    if state == 1 : 
        if SHOW_GRID :
            print ( "player {:s} is the winner".format( PLAYER[winner]) )
        return winner
        
    
##         
## TODO 4
## instead of playing just 1 game, play a few hundred games between 
## different algos to see which is the best 
## try calling the simulate method with different parameters
def simulate(n, algo_x=cpu_algo1, algo_o = cpu_algo2, show_steps=True) :
    global algo_X, algo_O, SHOW_GRID
    algo_X = algo_x
    algo_O = algo_o
    SHOW_GRID = show_steps
    
    scores = {'draw' : 0, 'X' : 0, 'O' : 0}
    for i in range( n ) :
        res = play()
        if res ==0 :
            scores['draw'] +=1
        elif res ==1 :
            scores['X'] +=1
        elif res ==-1 :
            scores['O'] +=1
            
    print(scores)
    
## to run type play()
