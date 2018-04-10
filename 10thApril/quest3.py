m1=[]
m2=[]
m3=[]
m4=[]
total=[]
for i in range(4):
    m1.append(int(input("Enter marks of roll no %d in subject 1:"%(i+1)))
    m2.append(int(input("Enter marks of roll no %d in subject 2:"%(i+1)))
    m3.append(int(input("Enter marks of roll no %d in subject 3:"%(i+1)))
    m4.append(int(input("Enter marks of roll no %d in subject 4:"%(i+1)))
    total.append(m1[i]+m2[i]+m3[i]+m4[i])

#Topper
def topper(total):
    topper=total.index(max(total))
    print("Topper among these 4 roll nos is Roll No : ",(topper+1))

#print highest marks in each subject:
print("Highest marks in Subject 1 : ",max(m1))
print("Highest marks in Subject 2 : ",max(m2))
print("Highest marks in Subject 3 : ",max(m3))
print("Highest marks in Subject 4 : ",max(m4))
topper(total)

#print all marks in ascending order subject wise:
print("Ascending order of marks in Subject 1 : ")
print(sorted(m1))
print("Ascending order of marks in Subject 2 : ")
print(sorted(m2))
print("Ascending order of marks in Subject 3 : ")
print(sorted(m3))
print("Ascending order of marks in Subject 4 : ")
print(sorted(m4))

#Updating details for roll no 5 and 6:
for i in range(5,7):
    s1[i]=int(input("Enter marks of roll no %d in subject 1:"%i))
    m1.append(s1[i])
    s2[i]=int(input("Enter marks of roll no %d in subject 2:"%i))
    m2.append(s2[i])
    s3[i]=int(input("Enter marks of roll no %d in subject 3:"%i))
    m3.append(s3[i])
    s4[i]=int(input("Enter marks of roll no %d in subject 4:"%i))
    m4.append(s4[i])
    total.append(s1[i]+s2[i]+s3[i]+s4[i])

topper(total)
