#kutuphanaler
import pandas as pd # veriler, veri çerçeveleri oluşturmak için kullanılır
import numpy as np # büyük sayılar ve hesaplamalar için kullanılır
import matplotlib.pyplot as plt # çizimler için kullanılır


satislar = pd.read_csv('satislar.csv')
print(satislar)

# *** Verilerin Bölünmesi (Eğitim ve Test olarak) ***

# x => bağımsız değişkenler, y => bağımlı değişkenler (sonuç kısmı)

# x_aylar = satislar.iloc[: , 0:1 ]
x_aylar = satislar[['Aylar']]
print(x_aylar)
# y_satislar = satislar.iloc[: , 1:2]
y_satislar = satislar[['Satislar']]
print(y_satislar)

from sklearn.model_selection import train_test_split

# test size 0.33 ise %67 si eğitim(train) ve %33 test için bölünecek anlamındadır
# random state ise ne kadar rastsal bölüneceğini ifade eder
x_train, x_test, y_train, y_test = train_test_split(x_aylar , y_satislar , test_size = 0.33 , random_state = 0)

"""
# Öznitelik Ölçekleme

# Standard scaler kullanımı; Verileri bilbirlerine daha yakın bir hale getirmeyi amaçlar
# Diğer bir deyişle farklı dünyaya ait verileri aynı dünyaya çekmek amaçlı yapılan bir işlemdir

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)
"""

# *** Model inşa edilmesi (Linear Regression) ***
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)

x_test = x_test.sort_index()

tahmin = lr.predict(x_test)

x_train = x_train.sort_index()
y_train = y_train.sort_index()


y_test = y_test.sort_index()

plt.plot(x_train, y_train)
# plt.plot(x_test, y_test)
plt.plot(x_test, tahmin)

plt.title("Aylara Göre Satış Miktarları")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")