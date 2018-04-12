fo=open('test1.txt','r')
data=fo.readlines()
print(data[0])
h={}
h1=[]
name=[]
w=[]
a=[]
g=[]
for s in data:
    arr=s.split(' ')
    name.append(arr[0])
    a.append(int(arr[1]))
    g.append(arr[2])
    h[arr[0]]=int(arr[3])
    h1.append(int(arr[3]))
    w.append(int(arr[4]))
    
#printing details:
i=0
for n in name:
    print("Details of %s"%n)
    print("Age : ",a[i])
    print("Gender : ",g[i])
    print("Height : ",h[n])
    print("Weight : ",w[i])
    i+=1
    
#printing order of students on basis of their height:
h1=sorted(h1,reverse=True)
print("Order of student on basis of their height")
for hei in h1:
    i=0
    while(i!=-1):
        if(h[name[i]]==hei):
            print(name[i])
            i=-1
        else:
            i+=1

#calculating bmi:
b=[]
for i in range(len(h1)):
    hei=(h1[i]*h1[i])/10000
    bmi=(w[i]/hei)
    b.append(bmi)

i=0
for n in name:
    print("Details of %s"%n)
    print("Age : ",a[i])
    print("Gender : ",g[i])
    print("Height : ",h[n])
    print("Weight : ",w[i])
    print("BMI : ",b[i])
    i+=1
    
#printing healthy,obese and overweight:
i=0
for bmi in b:
    if(bmi<18.5):
        print(name[i],"is UnderWeight")
    elif(bmi>=18.5 and bmi<24.9):
        print(name[i],"is Healthy weight")
    elif(bmi<=24.9 and bmi>29.9):
        print(name[i],"is Overweight")
    elif(bmi>30):
        print(name[i],"is Obese")
    i+=1
