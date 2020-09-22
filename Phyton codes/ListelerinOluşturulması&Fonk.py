# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:46:44 2020

@author: Kral
"""
def topla(*list):
    toplam = 0
    for i in list:
        toplam = toplam + i
    return toplam

print(topla(1,6))
print(topla(8))
print(topla(1,2,3,4,5,6,7))

def f(x):
    return x**2

l = []
for i in range(10):
    l.append(i)

print(l)
    
print(list(map(f,l)))

print(list(map(lambda x: x**2 , l)))

print(list(map(lambda x: x**2 , range(10)))) #buradaki x değişkenini ve listeyi dışarı taşımaz! (+) 
                                             #dışarı taşımalar yan etkidir!

print( [x**2 for x in range(10)] )

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x != y])

print( map(lambda x,y: (x,y) , [1,2,3], [3,1,4]) )