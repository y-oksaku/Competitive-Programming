N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    for b in A:
        ans = max(ans, abs(a - b))
print(ans)
