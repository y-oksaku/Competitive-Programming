N = int(input())
point = list(map(int, input().split()))

ans = 0
for p in point:
    ans += max(80 - p, 0)

print(ans)