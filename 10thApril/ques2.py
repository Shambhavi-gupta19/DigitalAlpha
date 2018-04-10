import numpy as np
r= int(input("Enter no of rows : "))
c= int(input("Enter no of columns : "))
a = np.ones(shape=(r,c))
print(a)
b = a.reshape(4,2,2)
print(b)
a=a+5
b=b+5
print(a)
print(b)
a=a-2
b=b-2
print(a)
print(b)
a=a*6
b=b*6
print(a)
print(b)
