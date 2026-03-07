def printNTo1(i):
    if i < 1:
        return
    print(i)
    printNTo1(i - 1)

n = int(input("Enter the value of n: "))
printNTo1(n)