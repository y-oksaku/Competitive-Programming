A, B, C = map(int, input().split())

if A % 2 == B % 2 == C % 2 == 0:
    if A == B == C:
        print(-1)
    else:
        ans = 0
        while A % 2 == B % 2 == C % 2 == 0:
            S = A + B + C
            A, B, C = (S - A) // 2, (S - B) // 2, (S - C) // 2
            ans += 1
        print(ans)
else:
    print(0)