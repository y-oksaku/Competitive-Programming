N = int(input())
A = [int(input()) for _ in range(N)]

ans = A[0] - 1

nowMin = 1
for a in A[1:]:
    if a == nowMin + 1:
        nowMin = a
    else:
        q, r = divmod(a, nowMin + 1)
        if r == 0:
            q -= 1
        ans += q

print(ans)