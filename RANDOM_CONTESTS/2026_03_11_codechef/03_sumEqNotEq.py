t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    zeros = a.count(0)
    if zeros == n:
        print(-1)
    else:
        nary = {}
        for i in range(n):
            if a[i] in nary:
                nary[a[i]].append(i)
            else:
                nary[a[i]] = [i]
        ans = [0,0,0]
        curr = 0
        while curr <= n - 3:
            if a[curr] + a[curr + 1] != a[curr + 2]:
                ans = [curr + 1, curr + 2, curr + 3]
                break
            elif a[curr + 1] + a[curr + 2] != a[curr]:
                ans = [curr + 2, curr + 3, curr + 1]
                break
            elif a[curr] + a[curr + 2] != a[curr + 1]:
                ans = [curr + 1, curr + 3, curr + 2]
                break
            curr += 1
        print(*ans)