suits = ['Hearts','Diamonds', 'Spades','Clubs']
number = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen', 'King']
score_21 = [1 ,2,3,4,5,6,7,8,9,10,11,11,11]
score_cdf = [1 ,2,3,4,5,6,7,8,9,10,10,10,10]
number_score_cdf = list( zip(number, score_cdf) )
number_score_21 = list( zip(number, score_cdf) )
deck_cdf =  [ ( '{num} of {s}'.format(num=n[0], s=s), n[1])  for n in number_score_cdf for s in suits]
deck_21 =  [ ( '{num} of {s}'.format(num=n[0], s=s), n[1])  for n in number_score_21 for s in suits]

import random

seen = []
def shuffle() : 
    global seen
    seen = []

def draw(deck, player, hidden = True) : 
    global seen
    card = random.choice(deck)
    while card in seen:
        card = random.choice(deck)
    seen.append(card)
    if hidden: 
        print ('{} draws a card, face down')
    else : 
        print('{} draws {}'.format(player, card[0]))
    return card

def show_hand(hand):
    for c in hand:
        print (c[0])

def score_hand(hand):
    return sum(card[1] for card in hand)


def decide_21(player, hand):
    if score_hand(hand) >21 :
        print('{} is bust'.format(player))
        return 'bust'

    if score_hand(hand) < 15:
        print('{} decides to twist'.format(player))
        return 'twist'


    print('{} decides to stick'.format(player))
    return 'stick'

def determine_winner(hands):
    p1 = hands['player1']
    p2 = hands['player2']
    if (score_hand(p1) > 21 ) and (score_hand(p2) > 21):
        print('both players are bust. no winner')
        return None

    if (score_hand(p1) > 21 ):
        print('player 1 is bust so player 2 is the winner')
        return 'player 2'

    if (score_hand(p2) > 21 ):
        print('player 2 is bust so player 1 is the winner')
        return 'player 1'

    if score_hand(p2) > score_hand(p1): 
        print('player 2 has the higher score so is the winner')
        return 'player 2'

    if score_hand(p1) > score_hand(p2): 
        print('player 1 has the higher score so is the winner')
        return 'player 1'

    if score_hand(p1) == score_hand(p2): 
        print('both players get the same score so there is no winner')
        return None


def play_21():
    p1 = []
    p1.append(draw(deck_21, player = 'player 1',  hidden = True))
    p1.append(draw(deck_21, player = 'player 1', hidden = True))
    while decide_21('player1', p1) not in ['stick','bust']:
        p1.append(draw(deck_21, 'player 1', hidden = False))

    print('\n\n\n')
    p2 = []
    p2.append(draw(deck_21, player = 'player 2',  hidden = False))
    p2.append(draw(deck_21, player = 'player 2', hidden = False))
    
    p2_status = 'twist'
    while p2_status not in ['bust','stick']:
        decision = ''
        while decision not in ['stick','twist']:
            decision = input('what do you want to do : stick or twist ? ')
            print(decision)
        if decision =='stick':
            p2_status = 'stick'
        else : 
            p2.append(draw(deck_21, player = 'player 2',  hidden = False))
            if score_hand(p2) > 21:
                p2_status = 'bust'


    print ("both players have finished")
    print ("Player 1 has a score of {}".format(score_hand(p1)))
    print ("Player 2 has a score of {}".format(score_hand(p2)))

    determine_winner({'player1' : p1, 'player2' : p2})
