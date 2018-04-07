#Ques 1:


d=0
for i in range(11,20):
    n=i
    d=0
    while(n!=0):
        d=i%10
        n=int(n/10)
        d+=d*d*d
    print(d,i,n)
