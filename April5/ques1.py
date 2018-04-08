#Ques 1:


d=0
s=0
print("Armstrong no in the range of 1 to 1000 are : ")
for i in range(0,1001):
    n=i
    d=0
    s=0
    while(n!=0):
        d=n%10
        n=int(n/10)
        s+=d*d*d
    if(i==s):
        print(i)
