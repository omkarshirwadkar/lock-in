def printSubsequences(idx, n, arr, currlist):
    if idx >= n:
        print(currlist)
        return
    currlist.append(arr[idx])
    printSubsequences(idx + 1, n, arr, currlist) # Take Condition
    currlist.pop()
    printSubsequences(idx + 1, n, arr, currlist) # Not Take Condition

n = int(input("Enter the size of Array: "))
arr = [int(x) for x in input("Enter the elements of the array: ").split()]

printSubsequences(0, n, arr, [])