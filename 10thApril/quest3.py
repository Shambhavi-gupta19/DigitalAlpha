m1=[]
m2=[]
m3=[]
m4=[]
total=[]
for i in range(4):
    m1.append(int(input("Enter marks of roll no %d in subject 1:"%(i+1))))
    m2.append(int(input("Enter marks of roll no %d in subject 2:"%(i+1))))
    m3.append(int(input("Enter marks of roll no %d in subject 3:"%(i+1))))
    m4.append(int(input("Enter marks of roll no %d in subject 4:"%(i+1))))
    total.append(m1[i]+m2[i]+m3[i]+m4[i])

#Topper
def topper(total):
    topper=total.index(max(total))
    print("Topper among these %d roll nos is Roll No : %d"%(len(total),topper+1))

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
for i in range(4,6):
    m1.append(int(input("Enter marks of roll no %d in subject 1:"%(i+1))))
    m2.append(int(input("Enter marks of roll no %d in subject 2:"%(i+1))))
    m3.append(int(input("Enter marks of roll no %d in subject 3:"%(i+1))))
    m4.append(int(input("Enter marks of roll no %d in subject 4:"%(i+1))))
    total.append(m1[i]+m2[i]+m3[i]+m4[i])

topper(total)
