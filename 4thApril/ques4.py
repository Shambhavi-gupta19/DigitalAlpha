print("Prime numbers between 900 and 1000 are : \n")
for n in range(900,1001):
   if n > 1:
       for i in range(2,int(n/2)):
           if (n % i) == 0:
               break
       else:
           print(n)
           if n%10 == 9:
               print(n ,"is a palindrome")
