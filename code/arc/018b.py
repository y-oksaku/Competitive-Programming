N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

ans = 0

for baseX, baseY in P:
    for x, y in P:
        for u, v in P:
            area = (x - baseX) * (v - baseY) - (u - baseX) * (y - baseY)
            if abs(area) % 2 == 0 and area != 0:
                ans += 1

print(ans // 6)