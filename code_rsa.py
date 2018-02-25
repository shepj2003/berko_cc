# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:26:16 2018

@author: shepj
"""

from math import gcd

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
          191, 193, 197, 199]

def ext_gcd(a,b) : 
    """
     implementation of Extended Eulers' Algorithm
     
     inputs : positive integers a, b as input 
     returns :  a triple (g, x, y), such that ax + by = g = gcd(a, b) 
     
     examples :
         ext_gcd(21, 15) = (3, -2, 3) ... gcd(21, 15) = 3  = -2*21 + 3*25 
         ext_gcd(49, 60) = (1, -11, 9) ... gcd(49, 60) = 1 = -11*49 + 9*60
     
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  a, x0, y0

def modular_inv( b, n) : 
    """
    inputs : positive integers b, n where gcd (b, n == 1) 
    returns : x st.t (x * b) % n == 1   
        
    examples :
        modualr_inv(3, 7 = 5 ... 3*3 = 15 = 1 mod 7
        modular_inv(49,60) = 49 ... 49 *49=2401 = 1 mod 60
            
    """
    g, x, _ = ext_gcd(b, n)
    if g == 1:
        return x % n
    
def phi_and_e(p, q) : 
    """
    inputs : 2 primes
    returns : tuple (phi, e) 
        phi = (p-1) * (q-1)
        e = the smallest positive integer that is coprime with phi
        
    examples : 
        phi_e(11,3) = (10*2, 3) 
    """
    x =  (p-1)* (q-1)
    for y in primes :
        if gcd(x, y) == 1 :
            return (x, y)
    return "can't find a suitable e"


def generate_rsa_keys(p, q) : 
    """
        generate public / private key pair with RSA algorithm 
        inputs : p,q : 2 positive (distinct) prime numbers
        returns : a dictionary with public and private key pairs
        reference : 
            https://en.wikipedia.org/wiki/RSA_(cryptosystem)
        examples : 
            g_rsa_keys(23, 47) = {'private': (1081, 675), 'public': (1081, 3)}
    """
    n = p*q
    phi, e = phi_and_e(p,q)
    d = modular_inv(e, phi)
    return {"private" : (n, d), "public" : (n, e)}


def encrypt(c, public_key):
    n, e = public_key
    o = ord(c)
    o_cypher = pow(o, e) % n
    return chr(o_cypher)

def encrypt_sentence(sentence, public_key) :
    cc = []
    for c in list(sentence):
        cc.append( encrypt( c, public_key) ) 
    return ''.join( cc )
    
def decrypt( c, private_key) : 
    n, d = private_key
    o = ord(c)
    o_decypher = pow(o,d) % n
    return chr(o_decypher)

def decrypt_sentence( sentence, private_key) : 
    dc = []
    for c in list( sentence) :
        dc.append( decrypt( c, private_key))
    return ''.join( dc)
