# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:40:14 2017

@author: 1f604
"""

from random import randint
def f(j):
    x = 1
    for i in range(10):
        x *= 1+(randint(0,j) / 10.0)
    return x
chance = 1
level = 1

def randpair(x=10,y=10):
    return (randint(0,x),randint(0,y))

while True:
    x,y = randpair()
    k = input("what is " + str(x)+ "+ " +str(y)+"?")
    if k == x + y:
        reward = f(level+3)
        print "your reward is: ", reward
        roll = randint(0,10)
        if chance > roll:
            level += 1
            print "level up! Now level ", level
    else:
        level -= 1
        print "Nuh uh! You lost a level. Current level ", level
        
    
    
