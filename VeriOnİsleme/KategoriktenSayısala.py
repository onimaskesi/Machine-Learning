# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:04:42 2020

@author: Kral
"""
#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır
# eksik veriler

eksikveriler = pd.read_csv('eksikveriler.csv')

Eyas = eksikveriler[['yas']]

#sci - kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy='mean')

Yas = eksikveriler.iloc[:, 3:4].values
#print(Yas)
BoyKiloYas = eksikveriler.iloc[:, 1:4].values

imputer = imputer.fit(Yas) #fit fonksiyonu eğitmek için kullanılır
Yas = imputer.transform(Yas) # transfor ile ise öğrendiğini uygulamasını sağlar (nan değerlerin ortalama ile değiştirilmesi)

eksikveriler.iloc[:, 3:4] = Yas
veriler = eksikveriler
#print(veriler)

#kategorikten nümeriğe dönüşüm

ulke = veriler.iloc[: , 0:1].values
#print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


#verilerin birleştirilmesi

#print(len(veriler))

ulkeFrame = pd.DataFrame( data = ulke , index = range( len(veriler) ) , columns=['fr','tr','us'] )
print(ulkeFrame)

BoyKiloYasCinsiyet = veriler.iloc[: , 1:5]
print(BoyKiloYasCinsiyet)

sonuc = pd.concat( [ulkeFrame, BoyKiloYasCinsiyet] , axis = 1) # axis = 1(yan yana) iken satır başlıklarını eşler, axis=0(alt alta) iken stun başlıklarına göre eşler
print(sonuc)
