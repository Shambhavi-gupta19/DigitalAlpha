import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset= pd.read_csv("test2.csv",sep=';')
col=dataset.columns.values
data=dataset.iloc[1:]

#printing all attributes:
print("All attributes in data are: ")
print('\t',col)
#printing datatype of each column:
print("Datatype of each entry is: ")
for i in range(len(col)):
    print("\t%s is of datatype %s"%(col[i],dataset[col[i]][0]))
    
#printing model,release date and price of first 25 entries:
model=dataset.iloc[1:26,0]
rel=dataset.iloc[1:26,1]
price=dataset.iloc[1:26,12]
print("Model\t\tRelease Date\tPrice")
for i in range(1,26):
    print("%s\t%s\t%s"%(model[i],rel[i],price[i]))
    

#Summarise the dataset:
print("Summary of the data : \n",dataset.describe())

#Summary statistics of price:
print("Median of price : ",data['Price'].median())
print("Mode of price : ",data['Price'].mode())


#Plot a time series graph of release date and price>1000:
p=[]
r=[]
d =np.array( data['Price'].astype(np.float64()))
re =np.array( data['Release date'].astype(np.float64()))
print(data['Price'])
for i in range(len(d)):
    if(d[i]>1000):
        p.append(d[i])
        r.append(re[i])
plt.bar(r,p)
plt.xlabel("Release date")
plt.ylabel("Price>1000")
plt.title("Release Date vs Price>1000")
plt.savefig("Release_price")
