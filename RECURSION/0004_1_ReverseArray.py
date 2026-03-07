def reverseArrayReturn(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverseArrayReturn(arr, left + 1, right - 1)

def reverseArray(arr, i, n):
    if i >= n - i - 1:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverseArray(arr, i + 1, n)

n = int(input("Enter the size of array: "))
arr = [int(x) for x in input("Enter the array A : ").split()]
brr = [int(x) for x in input("Enter the array B : ").split()]

print(reverseArrayReturn(arr, 0, n - 1))
reverseArray(brr, 0, n)
print(*brr)