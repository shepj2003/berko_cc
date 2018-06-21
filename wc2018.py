# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:07:28 2018

@author: shepj
"""


import itertools
from numpy import random
from functools import cmp_to_key
import operator

DEBUG = 1
INFO = 2
WARN = 3
ERROR = 4

LOG_LEVEL = 2

def log( level, msg):
    if level>=LOG_LEVEL:
        print(msg)


groupA = [ "Russia","Saudi Arabia", "Egypt","Uruguay"]
groupB = ["Portugal", "Spain", "Morocco", "Iran"]
groupC = ["France",'Australia', 'Peru', 'Denmark']
groupD = ['Argentina', 'Iceland', 'Croatia', 'Nigeria']
groupE = ['Brazil', 'Switzerland', 'Costa Rica', 'Serbia']
groupF = ['Germany', 'Mexico', 'Sweden', 'South Korea']
groupG = ['England','Belgium', 'Tunisia', 'Panama']
groupH = ['Poland', 'Senegal', 'Colombia' ,'Japan']

allgroups = {'A' : groupA, 
             'B': groupB, 
             'C': groupC, 
             'D': groupD, 
             'E': groupE, 
             'F': groupF, 
             'G': groupG, 
             'H': groupH}

skill_level = {
        'Russia' : ( 1, 1, 0.2),
        'Saudi Arabia' : ( 0.2, 0.1, 0.2),
        'Egypt' : (1, 0.5, 0.5),
        'Uruguay' : (1.5, 0.5, 0.5),
        'Portugal' : (3, 1, 0.6),
        'Spain' : (3, 3, 0.2),
        'Morocco' : (0.5, 0.2, 0.5),
        'Iran' : (0.2, 0.5, 0.5),
        'France' : (2.3, 2.0, 0.5),
        'Australia' : (0.5, 0.7, 0.2),
        'Peru' : (0.5, 0.7, 0.4),
        'Denmark' : (1., 1.5, 0.2),
        'Argentina' : (3, 2.0, 0.7),
        'Iceland' : (1.0, 3.0, 0.7),
        'Croatia' : (1.5, 2.0, 0.1),
        'Nigeria' : (1.5, 0.3, 0.5),
        'Brazil' : (3.0, 1.5, 0.7),
        'Switzerland' : (2.0, 1.0, 0.1),
        'Costa Rica' : (0.5, 0.5, 0.5),
        'Serbia' : (1.0, 1.0, 0.4),
        'Germany' : (2.0, 3.0, 0.2),
        'Mexico' : (1.5, 1, 0.5),
        'Sweden' : (1.4, 0.4, 1),
        'South Korea' : (1, 1, 0.3),
        'England' : (1.5, 1.5, 0.6),
        'Belgium' : (2.5, 2.0, 0.3),
        'Tunisia' : (0.5, 0.6, 1),
        'Panama' : (0.3,0.3, 1),
        'Poland' : (1.0, 1.0, 1.0),
        'Senegal' : (1.5, 0.3, 0.6),
        'Colombia' : (1.0, 1.0, 1.0),
        'Japan' : (1.2, 1.2, 0.7)}

knownResults = [{ 'Russia': 5, 'Saudi Arabia' : 0 }  ,
                {'Egypt': 0,  'Uruguay' : 1 } ,
                {'Portugal' : 3, 'Spain': 3 } ,
                {'Morocco' :  0, 'Iran': 1 },
                {'France' : 2, 'Australia' : 1},
                {'Argentina' : 1, 'Iceland' : 1},
                {'Peru' : 0, 'Denamrk' : 1},
                {'Croatia' : 2, 'Nigeria' : 0},
                {'Costa Rica' : 0, 'Serbia' : 1},
                {'Germany' : 0, 'Mexico' : 1},
                {'Brazil' : 1, 'Switzerland' : 1},
                {'Sweden' : 1, 'South Korea' : 0},
                {'Belgium' : 3, 'Panama' : 0},
                {'Tunisia' : 1, 'England' : 2},
                {'Colombia' : 1, 'Japan' : 2},
                {'Poland' : 1, 'Senegal' : 2},
                {'Russia' : 3, 'Egypt' : 1},
                {'Portugal' : 1, 'Morocco' : 0},
                {'Uruguay' : 1, 'Saudi Arabia' : 0},
                {'Iran' : 0, 'Spain' : 1}
                  ]

def known_result( a, b) : 
    kr = [x for x in knownResults if a in x.keys() and b in x.keys() ]
    if len(kr):
        return kr[0]
    
    return -1

def penalty_shootout(a, b):
    a_goals = random.binomial(5, 0.5)
    b_goals = random.binomial(5, 0.5)
    while a_goals==b_goals:
        a_goals += random.binomial(1, 0.5)
        b_goals += random.binomial(1, 0.5)
        
    log(DEBUG, "penalty shootout result :: {:s} ( {:d} ) {:s} ( {:d} )".format(a, a_goals, b, b_goals ) )
    return (a_goals, b_goals)

def one_match( a, b, stage = 'GROUP'):
    if stage == 'GROUP':
        kr = known_result( a, b)
        if not kr == -1:
            log(DEBUG, "[ {:s} ] final result :: {:s} ( {:d} ) {:s} ( {:d} )".format('GROUP', a, kr[a], b, kr[b] ) )
            return kr
    
    a_skill = skill_level[a]
    b_skill = skill_level[b]
    a_attack = random.normal(a_skill[0], a_skill[2])
    b_attack = random.normal(b_skill[0], b_skill[2])
    a_defence = random.normal(a_skill[1], a_skill[2])
    b_defence = random.normal(b_skill[1], b_skill[2])
    a_goals = random.poisson(max(0.5, a_attack - b_defence))
    b_goals = random.poisson(max(0.5, b_attack - a_defence))
    
    if (not stage == 'GROUP') and (a_goals == b_goals):
        log(DEBUG, "full time :: {:s} ( {:d} ) {:s} ( {:d} )".format(a, a_goals, b, b_goals ) )
        pens = penalty_shootout(a, b)
        a_goals +=pens[0]
        b_goals += pens[1]
        
    log(DEBUG, "[ {:s} ] final result :: {:s} ( {:d} ) {:s} ( {:d} )".format(stage, a, a_goals, b, b_goals ) )
        
    return( {a : a_goals, b : b_goals } )
    
def play_group_games(): 
    results = []
    for g in allgroups.keys():
        for pair in itertools.combinations(allgroups[g], 2):
            results.append( one_match(pair[0], pair[1]) ) 
    return results


def group_results(team, results):
    return [x for x in results if team in x.keys()]

def team_points_group_stage(team, results):
    gr = group_results(team, results)   
    pts = goals_for = goal_diff = 0
    for match in gr:
        my_score = match[team]
        opp_score = sum(match.values()) - my_score
        if my_score > opp_score:
            match_pts = 3
        elif my_score < opp_score:
            match_pts = 0
        else:
            match_pts = 1
        pts += match_pts
        goals_for += my_score
        goal_diff += my_score -opp_score
    return {team : {'points' : pts, 'goal_diff' : goal_diff, 'goals_for' : goals_for}}

def cmp_group_results(a_, b_) :
    a = list(a_.values())[0]
    b = list(b_.values())[0]
    if a['points'] < b['points']:
        return -1
    elif a['points'] > b['points']:
        return 1
    else:
        if a['goal_diff'] < b['goal_diff']:
            return -1
        elif a['goal_diff'] > b['goal_diff']:
            return 1
        else:
            if a['goals_for'] < b['goals_for']:
                return -1
            elif a['goals_for'] > b['goals_for']:
                return 1
            else:
                return 0

def group_order( group, results ):
    res = []
    for t in group:
        res.append( team_points_group_stage(t, results ))
    res.sort(key = cmp_to_key( cmp_group_results), reverse = True)
    return res

def group_stages():
    group_matches = play_group_games()
    group_orders = {}
    for g in allgroups.keys():
        res = group_order(allgroups[g], group_matches)
        log(DEBUG, "[ GROUP {} winner ] :: {}".format(g, res[0].keys()))
        log(DEBUG, "[ GROUP {} second ] :: {}".format(g, res[1].keys()))
        group_orders[g] = res
    return group_orders

def get_team(group_stage_results, group, position):
    return list( group_stage_results[group][position].keys() )[0]

def match_winner(match):
    it = list( match.items() )
    if it[0][1] > it[1][1]:
        return it[0][0]
    elif it[0][1] < it[1][1]:
        return it[1][0]
    else:
        return ''
    
def last16( group_results):
    l16 = []
    l16.append(one_match( get_team(group_results, 'A', 0), get_team(group_results, 'B', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'C', 0), get_team(group_results, 'D', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'B', 0), get_team(group_results, 'A', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'D', 0), get_team(group_results, 'C', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'E', 0), get_team(group_results, 'F', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'G', 0), get_team(group_results, 'H', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'F', 0), get_team(group_results, 'E', 1), 'L16' ))
    l16.append(one_match( get_team(group_results, 'H', 0), get_team(group_results, 'G', 1), 'L16' ))
    return l16
    
def quarters(last16):
    qf = []
    qf.append(one_match(match_winner(last16[0]), match_winner(last16[1]), 'QF' ))
    qf.append(one_match(match_winner(last16[4]), match_winner(last16[5]), 'QF' ))
    qf.append(one_match(match_winner(last16[6]), match_winner(last16[7]), 'QF' ))
    qf.append(one_match(match_winner(last16[2]), match_winner(last16[3]), 'QF' ))
    return qf

def semis(qf): 
    sf = []
    sf.append(one_match(match_winner(qf[0]), match_winner(qf[1]), 'SF' ))
    sf.append(one_match(match_winner(qf[2]), match_winner(qf[3]), 'SF' ))
    return sf

def final(sf) :
    return one_match(match_winner(sf[0]), match_winner(sf[1]), 'FINAL' )
    
def knockout_stages(group_results):
    l16 = last16(group_results)
    qf = quarters(l16)
    sf = semis(qf)
    f = final(sf)
    log(INFO, match_winner(f))
    return match_winner(f)

def tournament():
    gs = group_stages()
    return knockout_stages(gs)
    
def simulate(n):
    winners = {}
    for i in range(n):
        w = tournament()
        if w in winners.keys():
            winners[w] +=1
        else:
            winners[w] = 1
    winners = sorted(winners.items(), key=operator.itemgetter(1), reverse = True)
    log(INFO, winners)
        
