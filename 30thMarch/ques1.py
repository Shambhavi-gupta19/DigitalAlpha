import re
n=0
d=0
u=0
s=0
str=input("Enter a string")
for i in range(0,len(str)):
    if(re.match(r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", str[i])):
        s=s+1
    elif(str[i].isdigit()):
        d=d+1
    elif(str[i].isupper()):
        u=u+1
    elif(str[i].islower()):
        n=n+1
print("No of letters:",n+u)
print("No of digits:",d)
print("No of letters in uppercase:",u)
print("No of letters in lowercase:",n)
print("No of special characters:",s)
