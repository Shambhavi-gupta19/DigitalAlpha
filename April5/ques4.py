l=0
d=0
sen=input("Enter a sentence : ")
for c in sen:
    if(c.isalpha()):
        l+=1
    elif(c.isdigit()):
        d+=1
print("No of letters in the sentence are : ",l)
print("No of digits in the sentence are : ",d)
