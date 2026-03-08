def sumSubsequencesEqualToK(arr, n, k):
    result = []
    def backtrack(idx, current):
        if idx == n:
            if current and sum(current) == k:
                result.append(current[:])
            return
        backtrack(idx + 1, current) # Not Take
        current.append(arr[idx])
        backtrack(idx + 1, current) # Take
        current.pop()
    backtrack(0, [])
    return result

n = int(input("Enter the size of Array: "))
k = int(input("Enter the value of K: "))
arr = [int(x) for x in input("Enter the elements of the array: ").split()]

print(sumSubsequencesEqualToK(arr, n, k))