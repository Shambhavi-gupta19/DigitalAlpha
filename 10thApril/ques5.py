import pandas as pd
import numpy as np
from collections import Counter
 
dataset=pd.read_excel('Book1.xlsx')

#Summarise the data :
print("Summary of the data : \n",dataset.describe())

#summary of unit price :
u=dataset['Unit price']
print("mean of unit price : %d " % np.mean(u))
print("median of unit price : %d " % np.median(u))
print("mode of unit price : " ,Counter(u))

#printing the datatype of each field : 
print(type(dataset.values[0]))
print(dataset.dtypes)

#creating data frame customer : 
customers =df[['Name','Ext price']]
print(customers)
