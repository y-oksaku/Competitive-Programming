N = int(input())
temp = [list(map(float, input().split())) for _ in range(N)]

ans = [0] * 6

for tMax, tMin in temp:
    if tMax >= 35:
        ans[0] += 1
    if 30 <= tMax < 35:
        ans[1] += 1
    if 25 <= tMax < 30:
        ans[2] += 1
    if tMin >= 25:
        ans[3] += 1
    if tMin < 0 and tMax >= 0:
        ans[4] += 1
    if tMax < 0:
        ans[5] += 1

print(*ans)