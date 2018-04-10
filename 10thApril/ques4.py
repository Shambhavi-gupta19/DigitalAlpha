import pandas as pd

res={}
name=[]
score=[]
no_of_at=[]
qua=[]
inde=[]
n = int(input("Enter a number"))
for i in range(n):
    name.append(input("Enter a name : "))
    score.append(int(input("Enter the score : ")))
    no_of_at.append(int(input("Enter the no of attempts made : ")))
    qua.append(input("Enter whether qualified or not : "))
    inde.append(chr(ord('a')+i))
res['name']=name
res['score']=score
res['no_of_attempts']=no_of_at
res['qualify']=qua

#creating a dataframe: 
d=pd.DataFrame(res,index=inde)
print("DataFrame : \n",d)

#Printing first 4 rows:
print(d[:4])

#Printing Name and qualify of dataframe:
print("Name : ",d['name']," Qualify : ",d['qualify'])

#printing number of score in between 20- 35":
for i in range(n):    
    if((d['score'][i]>=20 )and( d['score'][i]<35)):
        print("Score between 20 and 35 : ",d['score'][i])
print("Sum of no of attempts : ",sum(d['no_of_attempts']))
