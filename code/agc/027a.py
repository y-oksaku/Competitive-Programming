N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for a in A:
    if X >= a:
        ans += 1
        X -= a

if ans == N and X > 0:
    ans -= 1

print(ans)
