# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sea
import pandas as pd

data=pd.read_excel("deneme.xlsx")
print(data.isnull().sum())

print(data.mean())

data = data.fillna(data.mean())





plt.figure(figsize=(12,6))

plt.plot(data.Tarih,data.SO2)

plt.show()





plt.figure(figsize=(30,12))

plt.subplot(2,2,1)

plt.plot(data.Tarih,data.PM10,color="red")

plt.plot(data.Tarih,data.SO2,color="blue")

plt.plot(data.Tarih,data.NO2,color="black")

plt.plot(data.Tarih,data.NOX,color="orange")

plt.plot(data.Tarih,data.NO,color="gray")

plt.xlabel("Tarih")

plt.ylabel("PM10-SO2-NO2-NOX-NO Miktarı")

plt.title("Zamana Göre PM10(Red)-SO2(Blue)-NO2(Black)-NOX(Orange)-NO(Gray)")

plt.show()



plt.figure(figsize=(20,10))

plt.subplot(2,2,1)   
plt.plot(data.Tarih,data.PM10,color="r") 
plt.xlabel("Tarih")
plt.ylabel("PM10 oranı")
plt.title("Ankara Sincan PM10 Oranı")

plt.subplot(2,2,2)
plt.plot(data.Tarih,data.SO2,color="blue")
plt.xlabel("Tarih")
plt.ylabel("SO2 Oranı")
plt.title("Ankara Sincan SO2 Oranı")

plt.show()


plt.figure(figsize=(20,10))

plt.subplot(2,2,1)   
plt.plot(data.Tarih,data.NO2,color="orange") 
plt.xlabel("Tarih")
plt.ylabel("NO2 oranı")
plt.title("Ankara Sincan NO2 Oranı")

plt.subplot(2,2,2)
plt.plot(data.Tarih,data.NOX,color="gray")
plt.xlabel("Tarih")
plt.ylabel("NOX Oranı")
plt.title("Ankara Sincan NOX Oranı")

plt.show()



plt.figure(figsize=(12,6))

plt.plot(data.Tarih,data.NO) 
plt.title("Ankara Sincan NO Oranı")

plt.xlabel("Tarih")

plt.show()

