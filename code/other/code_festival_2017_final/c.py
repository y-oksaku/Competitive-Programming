N = int(input())
D = list(map(int, input().split()))
D.sort()

hour = [0]

for i, d in enumerate(D):
    if i % 2 == 0:
        hour.append(d)
    else:
        hour.append(24 - d)

ans = float('inf')
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        ti = hour[i]
        tj = hour[j]
        ti, tj = ti - min(ti, tj), tj - min(ti, tj)
        gap = max(ti, tj)
        ans = min(ans, gap, 24 - gap)

print(ans)