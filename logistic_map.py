# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:08:22 2018

@author: shepj
"""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def logistic_map(r, x):
    return x*r*(1-x)

def logistic_map_iterate(n, r, x0):
    x_it = [x0]
    x = x0
    for i in range( n ):
        x = logistic_map(r, x)
        x_it.append(x )
    return x_it

def bifurcate(st, end, steps):
    x_axis = []
    y_axis = []
    mode = []
    for r in np.linspace( st, end, steps):
        xr = logistic_map_iterate(400, r, 0.3)
        sample = xr[100::3]
        x_axis += np.ravel( np.ones([1,len(sample)])*r ).tolist()
        y_axis += sample
        m = len(np.unique(np.round( sample, 3)) )
        mode += np.ravel( np.ones([1,len(sample)])*m ).tolist()
    return( x_axis, y_axis, mode)
    
def chaos( lo, hi, steps):
    """
    inputs:
        lo : lowest growth rate to use [1 ... 3.8]
        hi : highest growth rate to use [3 ... 4]
        steps : number of different growth rates to try
    """
    x,y,m = bifurcate( lo, hi, steps)
    plt.figure(figsize=(13, 5))
    plt.scatter(x, y, s = 0.4, marker = '.', c = y, cmap = cm.prism)
    plt.show()


def simulate(generations, growth_rate, initial_population):
    """
    inputs:
        generations : how many generations to use ... [100 .. 500]
        growth_rate : how fast does population breed  : [1 .. 4]
        initial_population : how many lemmings at first [1 ...999]
    """
    x = logistic_map_iterate(generations, growth_rate, initial_population/1000)
    plt.figure(figsize=(13, 5))
    x_axis= range(len(x))
    plt.plot(x_axis, x)
    plt.show()

def simulate2(generations, growth_rate, initial_population_1, initial_population_2):
    """
    inputs:
        generations : how many generations to use ... [100 .. 500]
        growth_rate : how fast does population breed  : [1 .. 4]
        initial_population_1 : how many lemmings in first group [1 ...999]
        initial_population_1 : how many lemmings in second group [1 ...999]
    """
    x1 = logistic_map_iterate(generations, growth_rate, initial_population_1/1000)
    x2 = logistic_map_iterate(generations, growth_rate, initial_population_2/1000)
    plt.figure(figsize=(13, 5))
    x_axis= range(len(x1))
    plt.plot(x_axis, x1)
    plt.plot(x_axis, x2)
    plt.show()
    
""" 
    questions ::
        1. what happens when the growth rate is small < 3 ?
        2. does the number of lemmings in the initial popultion matter ?
        3. can you find a growth rate that produces cyle of 2 years/generations?
        4. can you find a growth rate that produces a cycle of 4 years / generations?
        5. can you find a growth rate that produces a cycle of 4 years / generations?
        6. what happens as the growth rate gets bigger?
        7. does the intial population matter now?
"""
