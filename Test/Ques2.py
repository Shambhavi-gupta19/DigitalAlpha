#Question2:
import numpy as np
stu=[]
m1=[]
cm1=[]
g1=[]
m2=[]
cm2=[]
g2=[]
m3=[]
cm3=[]
g3=[]
for i in range(10):
    stu.append(input("Enter name : "))
    m1.append(int(input("Enter marks of {} in subject 1 : ".format(stu[i]))))
    m2.append(int(input("Enter marks of {} in subject 2 : ".format(stu[i]))))
    m3.append(int(input("Enter marks of {} in subject 3 : ".format(stu[i]))))

#printing table
print("NAME\tSubject 1\tStuject 2\tSubject3")
for i in range(10):
    print("{}\t\t{}\t{}\t{}".format(stu[i],m1[i],m2[i],m3[i]))
    
#Subject Analysis:
print("Mean of Subject 1 : ",np.mean(m1))
print("Median of Subject 1 : ",np.median(m1))
print("Mean of Subject 2 : ",np.mean(m2))
print("Median of Subject 2 : ",np.median(m2))
print("Mean of Subject 3 : ",np.mean(m3))
print("Median of Subject 3 : ",np.median(m3))

#top 3 in subjects:
cm1=m1

m1.sort()
print("Top 3 in subject 1:")
for i in range(len(m1)-3,len(m1)):
    print("{} is the highest marks".format(m1[i]))
cm2=m2
m2.sort()
print("Top 3 in subject 1:")
for i in range(len(m2)-3,len(m2)):
    print("{} is the highest marks".format(m2[i]))
cm3=m3
m3.sort()
print("Top 3 in subject 1:")
for i in range(len(m3)-3,len(m3)):
    print("{} is the highest marks".format(m3[i]))
    
#Student analysis:
for i in range(10):
    if(cm1[i]>=90):
        g1.append('A+')
    elif(cm2[i]>=90):
        g2.append('A+')
    elif(cm3[i]>=90):
        g3.append('A+')
    elif(cm1[i]<90 and cm1[i]>=80):
        g1.append('A')
    elif(cm2[i]<90 and cm2[i]>=80):
        g2.append('A')
    elif(cm3[i]<90 and cm3[i]>=80):
        g3.append('A')
    elif(cm1[i]<80 and cm1[i]>=70):
        g1.append('B+')
    elif(cm2[i]<80 and cm2[i]>=70):
        g2.append('B+')
    elif(cm3[i]<80 and cm3[i]>=70):
        g3.append('B+')
    elif(cm1[i]<70 and cm1[i]>=60):
        g1.append('B')
    elif(cm2[i]<70 and cm2[i]>=60):
        g2.append('B')
    elif(cm3[i]<70 and cm3[i]>=60):
        g3.append('B')
    elif(cm1[i]<60 and cm1[i]>=50):
        g1.append('C')
    elif(cm2[i]<60 and cm2[i]>=50):
        g2.append('C')
    elif(cm3[i]<60 and cm3[i]>=50):
        g3.append('C')
    elif(cm1[i]<50):
        g1.append('D')
    elif(cm2[i]<50):
        g2.append('D')
    elif(cm3[i]<50):
        g3.append('D')

print("NAME\tSubject 1\tStuject 2\tSubject3")
for i in range(10):
    print("{}\t\t{}\t{}\t{}".format(stu[i],cm1[i],cm2[i],cm3[i]))
