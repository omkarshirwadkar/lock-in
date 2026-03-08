def oneSubseqEqToK(arr, n, k, idx, curr, res):
    if idx == n:
        if curr and sum(curr) == k:
            res.append(curr[:])
            return True
        return False
    if (oneSubseqEqToK(arr, n, k, idx + 1, curr, res) == True):
        return True
    curr.append(arr[idx])
    if (oneSubseqEqToK(arr, n, k, idx + 1, curr, res) == True):
        return True
    curr.pop()

    return False

n = int(input("Enter the size of Array: "))
k = int(input("Enter the value of K: "))
arr = [int(x) for x in input("Enter the elements of the array: ").split()]

ans = []
print(oneSubseqEqToK(arr, n, k, 0, [], ans))
print(ans)