t = int(input())
for _ in range(t):
    n = int(input())
    current_max = 0
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        if current_max == 0:
            current_max = b
        if current_max < a:
            current_max = a
        elif current_max > b:
            current_max = b
    print(current_max)