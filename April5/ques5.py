import math

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))

print("{}! : {}".format(num1, math.factorial(num1)))
print("{}! : {}".format(num2, math.factorial(num2)))
print("LCM of {} and {} : {}" .format(num1, num2, ((num1*num2)/math.gcd(num1, num2))))
print("HCF of {} and {} : {}" .format(num1, num2, math.gcd(num1, num2)))
print("Factor of {} :" .format(num1))
for i in range(1, int(num1/2) +1):
    if(num1 % i == 0):
        print(i)
print(num1)
print("Factor of {} :" .format(num2))
for i in range(1, int(num2/2) +1):
    if(num2 % i == 0):
        print(i)
print(num2)
