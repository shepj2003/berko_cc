

import numpy as np

LMR = { 'L' : 0, 'M': 1, 'R' : 2}
TMB = { 'T' : 0, 'M' : 1, 'B' : 2}
PLAYER = { 1 : 'X', -1 : 'O', 0 : ' '}

def init_grid( n ) :
    """
    make a 3x3 grid with zeros in it
    """
    ## TODO 
    ## this line will complain when you try to load it becuase 
    ## numpy is a special library for doing maths that needs to be loaded into 
    ## python.
    ## do this by adding the line 
    ## import numpy as np
    ## this imports the library and calls it np ... just so don't have to keep typing numpy
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
    if 0 not in grid : 
        return (2, None)
    l = check_lines( grid )
    n = len(grid)
    if n in l : 
        return (1, 1)
    if -n in l : 
        return (1, -1)
    return (0, None)

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

def cpu_algo3 (grid, player) :
    #### TODO 4
    ## write your own algorithm
    ## you need to find a way to chose x & y
    ## you need to check that grid[x,y] is currently empty for it to be a valid move
    x = None
    y = None
    grid[x,y] = player
    return 1
    
def choose_cpu_algo( player ) : 
    #### TODO 3
    ## we have defined 2 different algorithms for the computer to decide where to play
    ## they are called cpu_algo1 and cpu_algo2
    ## change the lines below to control which algorithm to use
    ## this code only has any effect when the player is controlled by the CPU
    ## (see TODO2)
    ## try tofind out which algo is better
    ## if both players use the same algorithm, can you work out which player will win.
    ## is it always the same
    if player == 1 :
        algo = cpu_algo1
    if player == -1 :
        algo = cpu_algo1
    return algo
    
    
def human_move( grid, player) : 
    good_move = 0
    while good_move == 0 :
        loc = input( "player {:s} , where do you want to play ... ?".format( PLAYER[player]) )
        good_move = update_grid( grid, player, loc) 
    return 1

def player_is_human(player) : 
    #### TODO 2
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
        print ( "game ends in a draw" )
    if state == 1 : 
        print ( "player {:s} is the winner".format( PLAYER[winner]) )
