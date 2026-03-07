def sumNParameterized(num, total):
    if num < 1:
        print(total)
        return
    sumNParameterized(num - 1, total + num)
n = int(input("Enter the value of N: "))
sumNParameterized(n, 0)