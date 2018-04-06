#Question1:

import re
sen=[]
updated_sen=[]
v=0
u=0
l=0
s=0
r=0
str=input("Enter a paragraph with atleast 4 sentences : ")

#print the paragraph:
print("Paragraph : \n",str)

#Updating the middle sentence:
sen=str.split(".")
sen[int((len(sen)-1)/2)]="UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial Services, Telecom,Media &Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities"
l=len(sen)
for i in range(l):
    print(sen[i],'.')

#print no of vowels:
for i in range(l):
    for c in sen[i]:
        if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            v+=1
        elif(c.isupper()):
            u+=1
        elif(c.islower()):
            l+=1
        elif(re.match(r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", c)):
            s+=1
print("No of vowels : ",v)
print("No of uppercase charcters : ",u)
print("No of lowercase characters : ",l)
print("No of special characters : ",s)

#removing special characters:
print("Updated string is : ")
for i in range(l):
    updated_sen.append(re.sub('[^A-Za-z0-9 ]+', '', sen[i]))
    print("{}.".format(updated_sen[i]))

#swap last and first sentence:
temp=sen[0]
sen[0]=sen[len(sen)-1]
sen[len(sen)-1]=temp
l=len(sen)
print("Updated Paragraph:\n")
for i in range(l):
    print("{}.".format(sen[i]))
    
#===================================================================================
    
    
