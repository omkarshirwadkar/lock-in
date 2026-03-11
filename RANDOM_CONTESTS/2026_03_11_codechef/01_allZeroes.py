t = int(input())
for _ in range(t):
    a, b, c = [int(s) for s in input().split()]
    if c % 3 == 0:
        sub1FromB = c // 3
        b -= sub1FromB
        if b >= 0 and b % 2 == 0:
            sub1FromA = b // 2
            a -= sub1FromA
            if a == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")