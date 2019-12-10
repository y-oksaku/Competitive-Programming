N, M = map(int, input().split())

wars = [tuple(map(int, input().split())) for _ in range(M)]
wars.sort()

ans = 0
right = -1

for a, b in wars:
    if a >= right:
        ans += 1
        right = b
    else:
        right = min(right, b)

print(ans)