# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:24:01 2020

@author: Kral
"""
# ders 6: kutuphanelerin yuklenmesi
#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır

# kod bolumu
"""
# veri yükleme
veriler = pd.read_csv('veriler.csv')

# veri on isleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy' , 'kilo']]
print(boykilo)
"""

# eksik veriler

eksikveriler = pd.read_csv('eksikveriler.csv')

Eyas = eksikveriler[['yas']]

#sci - kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy='mean')

Yas = eksikveriler.iloc[:, 3:4].values
print(Yas)
BoyKiloYas = eksikveriler.iloc[:, 1:4].values

imputer = imputer.fit(Yas) #fit fonksiyonu eğitmek için kullanılır
Yas = imputer.transform(Yas) # transfor ile ise öğrendiğini uygulamasını sağlar (nan değerlerin ortalama ile değiştirilmesi)
print(Yas)