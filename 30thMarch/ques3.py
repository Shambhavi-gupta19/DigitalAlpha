def recur_fib(n):
    if n<=1:
        return n
    else:
        return recur_fib(n-1)+recur_fib(n-2)
def main():
    n=int(input("Enter a no"))
    for i in range(0,n):
        print(recur_fib(i))
main()
