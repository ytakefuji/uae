import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("new_deaths.csv")
country=input("enter country ")
n=len(data[country])
days1=310
y=data[country][n-days1:n]
x=np.arange(n-days1,n)
valid = ~(np.isnan(x) | np.isnan(y))
model=np.poly1d(np.polyfit(x[valid],y[valid],10))
date=data['date'][n-1]
x1=np.arange(n-days1,n+7)
y1=model(x1)
plt.plot(x,y,'k')
plt.plot(x1,y1,'b')
days2=100
ftr=7
for i in range(days2,days1):
 y=data[country][n-days1:n]
 x=np.arange(n-days1,n)
 valid = ~(np.isnan(x) | np.isnan(y))
 degree1=10
 model=np.poly1d(np.polyfit(x[valid],y[valid],degree1))
 date=data['date'][n-1]
 x1=np.arange(n-days1,n+ftr)
 y1=model(x1)
 plt.clf()
 plt.plot(x,y,'k')
 ny1=[]
 for j in y1:
  if j<0:j=0
  ny1.append(j)
 plt.plot(x1,ny1,'b')
 days2=i
 y=data[country][n-days2:n]
 x=np.arange(n-days2,n)
 valid = ~(np.isnan(x) | np.isnan(y))
 degree2=5
 model=np.poly1d(np.polyfit(x[valid],y[valid],degree2))
 x1=np.arange(n-days2,n+ftr)
 y1=model(x1)
 ny1=[]
 for j in y1:
  if j<0:j=0
  ny1.append(j)
 plt.plot(x1,ny1,'r')
 plt.legend(['daily deaths in '+str(country),str(days1)+' days from '+str(date)+' '+str(degree1)+'th',str(days2)+' days from '+str(date)+' '+str(degree2)+'th'])
 f=str(i)+'.png'
 plt.savefig(f,dpi=96)
 plt.gca()
