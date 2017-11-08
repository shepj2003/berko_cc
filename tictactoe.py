import numpy as np
LMR = { 'L' : 0, 'M': 1, 'R' : 2}
TMB = { 'T' : 0, 'M' : 1, 'B' : 2}
PLAYER = { 1 : 'X', -1 : 'O', 0 : ' '}
def init_grid( n ) : 
    return np.zeros([n,n], dtype = int)
def update_grid( grid, player, move) :
    
    ## if a valid move is played then update the grid and return 1
    ## if the move is invalid then print out some help and return 0
    
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
    gstr = ''
    for col in grid : 
        gstr += "|".join( [PLAYER[ x ]   for x in col ] )
        gstr +="\n"
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

def play() : 
    grid = init_grid(3)
    curr_player = 1
    while not game_ended(grid)[0]: 
        print_grid(grid)
        loc = input( "player {:s} , where do you want to play ... ?".format( PLAYER[curr_player]) )
        if update_grid( grid, curr_player, loc) : 
            curr_player = switch_curr_player(curr_player)
    state, winner = game_ended(grid)
    if state == 2 :
        print ( "game ends in a draw" )
    if state == 1 : 
        print ( "player {:s} is the winner".format( PLAYER[winner]) )
