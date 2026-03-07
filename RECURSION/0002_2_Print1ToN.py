def print1ToN(i, n):
    if i > n:
        return
    print(i)
    print1ToN(i + 1, n)

n = int(input("Enter the value n: "))

print1ToN(1, n)