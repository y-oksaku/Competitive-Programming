M, K = map(int, input().split())

ans = 0
now = 1
while now < 2 * M + 1:
    ans += 1
    now *= (2 * K + 1)

print(ans)