def countSubseqEqToK(arr, n, k, idx, curr):
    if idx == n:
        if curr and sum(curr) == k:
            return 1
        return 0
    left = countSubseqEqToK(arr, n, k, idx + 1, curr)

    curr.append(arr[idx])
    right = countSubseqEqToK(arr, n, k, idx + 1, curr)
    curr.pop()
    return left + right

n = int(input("Enter the value of N: "))
k = int(input("Enter the value of K: "))
arr = [int(x) for x in input("Enter the elements of Array: ").split()]
print(countSubseqEqToK(arr, n, k, 0, []))