import numpy as np
import scipy.stats as st

fo = open("house_rent.txt", "r")
r=fo.readlines()
l=[]
rent=[]
for i in range(len(r)):
    l.append(r[i].replace('\n','').split(' '))
a=np.reshape(l,12)
for i in range(12):
    rent.append(int(a[i]))

m= np.mean(rent)
me=np.median(rent)
mo=st.mode(rent,axis=None)
freq=st.itemfreq(rent)

print("Mean : ",m)
print("Median : ",me)
print("Mode : ",mo.mode[0])
print("Frequency table : ",freq)
print("Cummulative Frequency Table : ",st.cumfreq(rent))
print("25th percentile is : "+np.percentile(rent,25))
print("50th percentile is : "+np.percentile(rent,50))
print("75th percentile is : "+np.percentile(rent,75))
print("variance is : ", np.var(rent))
print("cov is : ",st.variation(rent))
