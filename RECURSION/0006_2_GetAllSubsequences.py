def getAllSubsequences(n, arr):
    result = []

    def backtrack(idx, current_arr):
        if idx == n:
            # Append a copy of the current subsequence
            result.append(current_arr[:])
            return
        # Not Take Condition
        backtrack(idx + 1, current_arr)

        # Take Condition
        current_arr.append(arr[idx])
        backtrack(idx + 1, current_arr)
        current_arr.pop()
    
    backtrack(0, [])
    return result

n = int(input("Enter the size of Array: "))
arr = [int(x) for x in input("Enter the elements of the array: ").split()]

print(getAllSubsequences(n, arr))