# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:20:17 2020

@author: Kral
"""
#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır

# eksik veriler
# veri yükleme
eksikveriler = pd.read_csv('eksikveriler.csv')

Eyas = eksikveriler[['yas']]

#sci - kit learn
# *** Yas Stunundaki NAN(Boş) Değerleri Stundaki Verilerin Ortalaması ile Doldurma İşlemleri ***
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy='mean')

# Üzerinde işlem yapılacak olan ilgili stunun(Yas) ayrıştırılması
Yas = eksikveriler.iloc[:, 3:4].values
#print(Yas)

imputer = imputer.fit(Yas) #fit fonksiyonu eğitmek için kullanılır
Yas = imputer.transform(Yas) # transfor ile ise öğrendiğini uygulamasını sağlar (nan değerlerin ortalama ile değiştirilmesi)

# düzeltilen eksik verileri geri yükleme ve veriler değişkenine atama işlemi
eksikveriler.iloc[:, 3:4] = Yas
veriler = eksikveriler
#print(veriler)

# *** Kategorik Verileri, Nümeriğe Dönüştürme İşlemleri ***

# ilgili kategorik stunu(ulke) verilerden ayrıştırma işlemi
ulke = veriler.iloc[: , 0:1].values
#print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

# ilgili kategorik stununun(ulke) numpy dizisi şeklinde sayısal dönüşümünü sağlama
# alfabetik sıraya göre fr , tr , us => 0 1 2 sayısal değerleri verilir ve satır değerleri bu bilgiye göre işlenir
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

# numpy sayısal dizisi sırasıyla:
# fr , tr , us => 0 1 2 => 1 0 0 , 0 1 0 , 0 0 1 şeklinde oluşturuldu 
# her kategorik değer için bulunduğu kategori 1 ve diğerleri 0 olacak şekilde 
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


# *** Düzenlenen Verilerin Birleştirilmesi ***

#print(len(veriler))

ulkeFrame = pd.DataFrame( data = ulke , index = range( len(veriler) ) , columns=['fr','tr','us'] )
#print(ulkeFrame)

BoyKiloYasCinsiyet = veriler.iloc[: , 1:5]
#print(BoyKiloYasCinsiyet)

sonuc = pd.concat( [ulkeFrame, BoyKiloYasCinsiyet] , axis = 1) # axis = 1(yan yana) iken satır başlıklarını eşler, axis=0(alt alta) iken stun başlıklarına göre eşler
#print(sonuc)


# *** Verilerin Bölünmesi (Eğitim ve Test olarak) ***

# x => bağımsız değişkenler, y => bağımlı değişkenler (sonuç kısmı)

x = sonuc.iloc[: , 0:6 ]
#print(x)
y= sonuc.iloc[: , 6:7]
#print(y)

from sklearn.model_selection import train_test_split

# test size 0.33 ise %67 si eğitim(train) ve %33 test için bölünecek anlamındadır
# random state ise ne kadar rastsal bölüneceğini ifade eder
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.33 , random_state = 0)

# Öznitelik Ölçekleme

# Standard scaler kullanımı; Verileri bilbirlerine daha yakın bir hale getirmeyi amaçlar
# Diğer bir deyişle farklı dünyaya ait verileri aynı dünyaya çekmek amaçlı yapılan bir işlemdir

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)