N = int(input())
A = list(map(int, input().split()))
ans = 0
mx = 0

for a in A:
    ans += max(0, mx - a)
    mx = max(mx, a)

print(ans)
