#Question4:
name=[]
age=[]
for i in range(20):
    name.append(input("Enter name of {} member".format(i+1)))
    age.append(int(input("Enter age of {} member".format(i+1))))

for i in range(20):
    print("Name : {} and Age : {}".format(name[i],age[i]))

for i in range(20):
    if(age[i]<=18):
        print("{} is a child".format(name[i]))
    elif(age[i]>18 and age[i]<=30):
        print("{} is a youth".format(name[i]))
    elif(age[i]>30 and age[i]<=50):
        print("{} is a midlde aged".format(name[i]))
    elif(age[i]>50):
        print("{} is a senior citizen".format(name[i]))

#===================================================================================
