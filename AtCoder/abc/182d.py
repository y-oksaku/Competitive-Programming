N = int(input())
A = list(map(int, input().split()))

now = 0
S = 0
mx = 0
ans = 0
for a in A:
    S += a
    mx = max(mx, S)
    ans = max(ans, mx + now)
    now += S
print(ans)
