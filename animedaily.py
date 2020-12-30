import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("new_deaths.csv")
country=input("enter country ")
n=len(data[country])
days1=265
y=data[country][n-days1:n]
x=np.arange(n-days1,n)
valid = ~(np.isnan(x) | np.isnan(y))
model=np.poly1d(np.polyfit(x[valid],y[valid],10))
date=data['date'][n-1]
x1=np.arange(n-days1,n+7)
y1=model(x1)
plt.plot(x,y,'k')
plt.plot(x1,y1,'b')
for i in range(120,days1):
 y=data[country][n-days1:n]
 x=np.arange(n-days1,n)
 valid = ~(np.isnan(x) | np.isnan(y))
 degree1=10
 model=np.poly1d(np.polyfit(x[valid],y[valid],degree1))
 date=data['date'][n-1]
 x1=np.arange(n-days1,n+7)
 y1=model(x1)
 plt.clf()
 plt.plot(x,y,'k')
 plt.plot(x1,y1,'b')
 days2=i
 y=data[country][n-days2:n]
 x=np.arange(n-days2,n)
 valid = ~(np.isnan(x) | np.isnan(y))
 degree2=5
 model=np.poly1d(np.polyfit(x[valid],y[valid],degree2))
 x1=np.arange(n-days2,n+7)
 y1=model(x1)
 plt.plot(x1,y1,'r')
 plt.legend(['daily deaths in '+str(country),str(days1)+' days from '+str(date)+' '+str(degree1)+'th',str(days2)+' days from '+str(date)+' '+str(degree2)+'th'])
 f=str(i)+'.png'
 plt.savefig(f,dpi=96)
 plt.gca()
