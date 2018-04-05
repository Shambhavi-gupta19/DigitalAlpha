import re
str = "#Python is an interpreted high level programming language for general-purpose programming*."
updated_str = re.sub('[^A-Za-z0-9 ]+', '', str)
print("Updated string is : ",updated_str)

str2 = str.split(' ')
for i in range(len(str2)):
    if(str2[i] == str2[i][::-1]):
        print("Pallindrome is : ",str2[i])

freq={}
for i in str2:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]>1:
        print(i,":",freq[i])
