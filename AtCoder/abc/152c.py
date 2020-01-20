N = int(input())
P = list(map(int, input().split()))

ans = 0
minP = N
for p in P:
    if p <= minP:
        ans += 1
    minP = min(minP, p)

print(ans)