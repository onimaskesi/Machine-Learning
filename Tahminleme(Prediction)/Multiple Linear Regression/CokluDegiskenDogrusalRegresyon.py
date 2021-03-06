#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır

# veri yükleme
veriler = pd.read_csv('veriler.csv')
#print(veriler)

#sci - kit learn

# *** Kategorik Verileri, Nümeriğe Dönüştürme İşlemleri ***

# ilgili kategorik stunu(ulke) verilerden ayrıştırma işlemi
ulke = veriler.iloc[: , 0:1].values
#print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

# ilgili kategorik stununun(ulke) numpy dizisi şeklinde sayısal dönüşümünü sağlama
# alfabetik sıraya göre fr , tr , us => 0 1 2 sayısal değerleri verilir ve satır değerleri bu bilgiye göre işlenir
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#print(ulke)

# numpy sayısal dizisi sırasıyla:
# fr , tr , us => 0 1 2 => 1 0 0 , 0 1 0 , 0 0 1 şeklinde oluşturuldu 
# her kategorik değer için bulunduğu kategori 1 ve diğerleri 0 olacak şekilde 
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
#print(ulke)

# Kategorik Verileri, Nümeriğe Dönüştürme (Binomial)
# Dummy Variable engellemek adına tek bir kolon kullanılır (KadınMi kolonu yeterlidir)

# ilgili kategorik stunu(cinsiyet) verilerden ayrıştırma işlemi
cinsiyet = veriler[['cinsiyet']]
#print(cinsiyet)

# ilgili kategorik stununun(cinsiyet) numpy dizisi şeklinde sayısal dönüşümünü sağlama
# alfabetik sıraya göre e , k => 0 1 sayısal değerleri verilir ve satır değerleri bu bilgiye göre işlenir
cinsiyet = le.fit_transform(cinsiyet)
#print(cinsiyet)
# oluşturulan cinsiyet dizisi dataframe'e dönüştürülür
cinsiyet = pd.DataFrame( data = cinsiyet , index = range( len(veriler) ) , columns=['KadınMi'] )
#print(cinsiyet)


# *** Düzenlenen Verilerin Birleştirilmesi ***

#print(len(veriler))

ulkeFrame = pd.DataFrame( data = ulke , index = range( len(veriler) ) , columns=['fr','tr','us'] )
#print(ulkeFrame)

BoyKiloYas = veriler.iloc[: , 1:4]
#print(BoyKiloYas)

sonuc = pd.concat( [ulkeFrame, BoyKiloYas] , axis = 1) # axis = 1(yan yana) iken satır başlıklarını eşler, axis=0(alt alta) iken stun başlıklarına göre eşler
#print(sonuc)
sonuc = pd.concat( [sonuc, cinsiyet] , axis = 1)
veriler = sonuc
print(veriler)

# *** Verilerin Bölünmesi (Eğitim ve Test olarak) ***

# x => bağımsız değişkenler, y => bağımlı değişkenler (sonuç kısmı)

x1 = veriler.iloc[: , :3 ] # fr, tr, us (boy kolonunun sağı)
x2 = veriler.iloc[: , 4: ] # kilo, yas, KadınMi (boy kolonunun solu)
x = pd.concat([x1,x2] , axis=1)
print(x)
y = veriler.iloc[: , 3:4] # boy kolonu
print(y)

from sklearn.model_selection import train_test_split

# test size 0.33 ise %67 si eğitim(train) ve %33 test için bölünecek anlamındadır
# random state ise ne kadar rastsal bölüneceğini ifade eder
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.33 , random_state = 0)

x_train = x_train.sort_index()
y_train = y_train.sort_index()

x_test = x_test.sort_index()
y_test = y_test.sort_index()

# Linear model oluşturulması

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_prediction = regressor.predict(x_test)


#Backward Elimination

import statsmodels.api as sm

# oluşturulacak olan multiple regression fonksiyonuda sabit sayı değerini tanımlamak adına listeye 1 leden oluşan bir stun eklenir
X = np.append(arr = np.ones((len(x),1)).astype(int) , values = x, axis=1) 

X_l = x.iloc[ : , [0,1,2,3,4,5] ]
X_l = np.array(X_l, dtype=float)
model = sm.OLS( y , X_l).fit()
print(model.summary())

# en yüksek p değerine sahip olan değişken sistemden çıkarılır

X_l = x.iloc[ : , [0,1,2,3,5] ]
X_l = np.array(X_l, dtype=float)
model = sm.OLS( y , X_l).fit()
print(model.summary())

















