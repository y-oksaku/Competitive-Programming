M = int(input())
DC = [tuple(map(int, input().split())) for _ in range(M)]
ans = 0
s = 0

for d, c in DC:
    s += d * c
    ans += c

ans += (s - 1) // 9 - 1
print(ans)