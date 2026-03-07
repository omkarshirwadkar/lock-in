def fib(n):
    if n <= 1:
        return n
    return fib(n -  1) + fib(n - 2)
n = int(input("Enter the value of N: "))
print("The " + str(n) + " fibonacci number is: " + str(fib(n - 1)))