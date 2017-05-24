"""
	solves the countdown numbers game
	author shepj
	created : 2017-05-20
"""

#import numpy as np

import itertools

def add(a,b) :
    ## returns the sum of a & b
    ## FIXME
    return -1

def subtract(a,b) :
    ## returns the difference between a & b
    ## FIXME
    return -1

def mult(a,b) : 
    ##returns the product of a & b
    ## FIXME
    return -1
	
	
def divide(a,b) :
    if a%b :
        return a/(1.0*b)
    return a/b
    
operators = [add, subtract, mult, divide]

class Expr :
    def __init__(self, value) :
        self.value = value
        
    def __str__(self) :
        return str(self.value)
    def __repr__(self) :
        return str(self.value)
    def _display(self) : 
        return str( self.value )
        
    def val(self) : 
        return self.value
    
class TExpr(Expr) : 
    def __init__(self, value):
        self.value = value
    def __str__(self) :
        return str(self.value)
    def __repr__(self) :
        return str(self.value)
    def _display(self) : 
        return str( self.value )
    def val(self) :
        return self.value
        
class BExpr(Expr) :
    def __init__(self, op, lhs, rhs):
        self.lhs = lhs
        self.rhs= rhs
        self.op = op
    def __str__(self) :
        return self._display()
    def __repr__(self) : 
        return self._display()
        
    def _display(self):
        lhs = self.lhs._display()
        rhs = self.rhs._display()
        op = {add : '+', subtract : '-', mult : '*', divide : '/'}
        return '(' + lhs + op[self.op] + rhs + ')'
        
    def val(self) :
        lhs = self.lhs.val()
        rhs = self.rhs.val()
        return self.op(lhs, rhs)
        
            
def expressions( l ) : 
    for i, x in enumerate(l):
        yield TExpr(x)
    if len(l) ==2:
        for o in operators :
            yield BExpr(o, TExpr(l[0]), TExpr(l[1]))
    if len(l) > 2 :
        for i, x in enumerate(l) :
            for o in operators :
                for e in expressions(l[:i] + l[i+1:]) : 
                    yield BExpr(o, TExpr(x), e)

def target_expressions(target, l) :
    for x in expressions(l) :
        try : 
            if x.val() == target :
                yield x
        except : 
            ZeroDivisionError
            
def print_expressions(t, l) :
    for x in target_expressions(t, l):
        print x
        
def test_cases():
    print_expressions(952,[25, 50,75,100,3,6])
    print_expressions(431,[25, 50,75,50,8,2])
    print_expressions(724,[12,87,8,3,4,8])
        
 
