# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
max = 100
asalmi = 1
l = []

for i in range(2,max):
    asalmi = 1
    for j in range(2,9):
        if(j != i):
             if i%j == 0:
                 asalmi = 0   
                 break
        
    if(asalmi): 
        l.append(i)

print(l)
"""
def asalmi(x):
    for j in range(2,x):
        if x%j == 0:
            return j
    else:
        return x
    

max = 100
l = []

for i in range(2,max):
    if(asalmi(i) == i):
        l.append(i)

print(l)

while 1==1:

    sayi = int(input("Bir sayı giriniz: "))
    
    if(sayi == 0):
        break
    
    sonuc = asalmi(sayi)
    
    if(sonuc == sayi):
        print(str(sayi) + " SAYISI ASALDIR.")
    else:
        print(str(sayi) + " SAYISI ASAL DEĞİLDİR ÇÜNKÜ " + str(sonuc) + " SAYISINA BÖLÜNÜR.")

