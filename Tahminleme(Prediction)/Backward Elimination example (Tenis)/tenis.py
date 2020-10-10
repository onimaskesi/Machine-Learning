#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır


tenis = pd.read_csv('odev_tenis.csv')
print(tenis)

#outlook için kategorik -> nümerik
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

outlook = tenis[['outlook']]
outlook = le.fit_transform(outlook)
outlook = pd.DataFrame( data = outlook , index = range( len(tenis) ) , columns=['outlook'] )

ohe = preprocessing.OneHotEncoder()
outlook = ohe.fit_transform(outlook).toarray()

outlook = pd.DataFrame( data = outlook , index = range( len(tenis) ) , columns=['overcast','rainy','sunny'] )
#print(outlook)

#windy için kategorik -> nümerik

windy = tenis[['windy']]
windy = le.fit_transform(windy) # false , true -> 0 , 1
windy = pd.DataFrame(data = windy, index = range(len(tenis)) , columns=['windy'])
#print(windy)

#play için kategorik -> nümerik

play = tenis[['play']]
play = le.fit_transform(play) # no , yes -> 0 , 1
play = pd.DataFrame(data = play , index = range(len(tenis)) , columns=['play'])
#print(play)

# değişkenler sırasıyla birleştirilir => outlook temperature humidity windy play

tempHumi = tenis[['temperature' , 'humidity']]
#print(tempHumi)
sonuc = pd.concat( [outlook, tempHumi] , axis = 1)
sonuc = pd.concat( [sonuc, windy] , axis = 1)
sonuc = pd.concat( [sonuc, play] , axis = 1)

tenis = sonuc
print(tenis)

# Hangi değişkenler ile işlem yapılacağını bulmak için:
# Backward Elimination

import statsmodels.api as sm

x = tenis.iloc[: , :6] # tüm değişkenler için
y = tenis[['play']]

# oluşturulacak olan multiple regression fonksiyonuda sabit sayı değerini tanımlamak adına listeye 1 leden oluşan bir stun eklenir
X = np.append(arr = np.ones((len(x),1)).astype(int) , values = x, axis=1) 

X_l = x.iloc[ : , [0,1,2,3,4,5] ]
X_l = np.array(X_l, dtype=float)
model = sm.OLS( y , X_l).fit()
print(model.summary())

# en yüksek p değerine sahip olan değişken sistemden çıkarılır

X_l = x.iloc[ : , [0,1,2,4,5] ]
X_l = np.array(X_l, dtype=float)
model = sm.OLS( y , X_l).fit()
print(model.summary())


# play tahmini yapabilecek şekilde çoklu regresyon metodu ile eğitecek olursak:

x = tenis.iloc[: , :6] # tüm değişkenler için

# Backward Elimination sonucunda humi değişkenini denklemden çıkartmak suretiyle oluşturulan x değişkeni
sol = tenis.iloc[:, :4]
sag = tenis.iloc[: , 5:]
x = pd.concat([sol,sag], axis = 1)

y = tenis[['play']]
# print(x)
# print(y)

from sklearn.model_selection import train_test_split

# test size 0.33 ise %67 si eğitim(train) ve %33 test için bölünecek anlamındadır
# random state ise ne kadar rastsal bölüneceğini ifade eder
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.5 , random_state = 0)

x_train = x_train.sort_index()
y_train = y_train.sort_index()

x_test = x_test.sort_index()
y_test = y_test.sort_index()

# Linear model oluşturulması

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_prediction = regressor.predict(x_test)
