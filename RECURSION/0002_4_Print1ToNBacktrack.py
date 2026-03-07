def print1ToNBacktrack(i):
    if i < 1:
        return
    print1ToNBacktrack(i - 1)
    print(i)

n = int(input("Enter the value of n: "))
print1ToNBacktrack(n)