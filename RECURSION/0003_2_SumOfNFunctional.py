def sumNFunctional(num):
    if num < 1:
        return 0
    return num + sumNFunctional(num - 1)
n = int(input("Enter the value of N: "))
print(sumNFunctional(n))