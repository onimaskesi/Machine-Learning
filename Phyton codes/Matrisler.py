# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:51:39 2020

@author: Kral
"""
sColumnes = ["name","note","age"]
names = ["Erdem","Onat","KIRAL"]
notes = [100,95,90]
age = [20,28,34]
students=[names,notes,age]

for i in range(3):
    print()
    for j in range(len(names)):
        print( sColumnes[j] +": " + str(students[j][i]))
        
mt = [ [row[i] for row in students ] for i in range(len(names)) ]

print(mt)
