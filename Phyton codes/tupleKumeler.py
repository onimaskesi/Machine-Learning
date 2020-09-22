# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:18:01 2020

@author: Kral
"""
l = [1,2,3,1,2,1,3] #liste
t = (1,2,3) # tuple: içeriği değiştirilemez listelerdir
k = {1,2,3,1,2,1,3} # kümeler: değerleri tekrarlanamaz ve index sıralaması önemsizdir

print(l) 
print(t) 
print(k)

k1 = set(l) # set fonk küme oluşturur
print(k1)

k2 = set("onat")

k3 = set("onimaskesi")
print(k3)

print(k2 | k3) # union
print(k2 - k3) # k2 de olup k3 de olmayan
print(k2 & k3) # kesişim
print(k2 ^ k3) # her iki farkın birleşimi, ortak olmayanlar