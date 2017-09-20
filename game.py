# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:40:14 2017

@author: 1f604
"""

from random import randint
def f(j):
    x = 1
    for i in range(j):
        x += randint(0,j)
    return x
chance = 1
level = 1

while True:
    raw_input("press enter for your next reward")
    reward = f(level+3)
    print "your reward is: ", reward
    roll = randint(0,10)
    if chance > roll:
        level += 1
        print "level up! Now level ", level
    
    
