
import numpy as np
passw=[]
def upp():
    return(chr(np.random.randint(97,high=122)).upper())
def di():
    return(str(np.random.randint(0,high=9)))
def sp():
    return(np.random.choice(['!','@','#','$','%','^','&','*','(',')','{','}','[',']',':','"',':','.',',','<','>']))
def low():
    return(chr(np.random.randint(97,high=122)))
#33-47 58-63 91-96
passw.append(np.random.choice([upp(),di(),sp(),low()]))
passw.append(upp())
passw.append(np.random.choice([upp(),di(),sp(),low()]))
passw.append(di())
passw.append(np.random.choice([upp(),di(),sp(),low()]))
passw.append(sp())
passw.append(np.random.choice([upp(),di(),sp(),low()]))
passw.append(low())
password=''.join(passw)
print("Password Generated is %s"%password)

ul=[]
ll=[]
spl=[]
dl=[]
u=0
l=0
sp=0
d=0
for c in password:
    if(c.isupper()):
        u+=1
        ul.append(c)
    elif(c.islower()):
        l+=1
        ll.append(c)
    elif(c.isdigit()):
        d+=1
        dl.append(c)
    else:
        sp+=1
        spl.append(c)
        
print("No of lower case %d"%l)
print("No of upper case %d"%u)
print("No of digits %d"%d)
print("No of special characters %d"%sp)

fo=open("pass1.txt","w")
fo.write("Password generated is %s"%password)
fo.close()

print("Digits in ppassword ",dl)
print("Special Characters in ppassword ",spl)
print("Uppercase in ppassword ",ul)
print("Lowercase in ppassword ",ll)
