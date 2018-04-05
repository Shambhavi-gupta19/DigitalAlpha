fo = open("foo.txt", "w")
l=[]
n=int(input("Enter no of places u want to enter:"))
for i in range(n):
    fo.write(input("Enter place name , population and area with spaces"))
    fo.write("\n")
fo.close()
fo=open("foo.txt","r")
value=fo.readlines()
for i in value:
    l.append(i.rstrip('\n'))
    l.sort()
fo.close()
fo = open("foo.txt", "w")
print(len(l))
for i in range(0,len(l)):
    fo.write(l[i])
    fo.write("\n")
fo.close()
