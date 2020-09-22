# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:26:14 2020

@author: Kral
"""
d = {'jack': 4098, 'sape': 4139}
tuple1 = ('x','y')
l = [('jack' , 4098) , ('sape' , 4139) , ('guido' , 4127) , tuple1]
d1 = dict(l)
print(d1)

for anahtar, deger in d.items():
    print(anahtar,deger)