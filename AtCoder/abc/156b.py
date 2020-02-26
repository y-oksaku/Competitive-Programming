N, K = map(int, input().split())

ans = 0
while pow(K, ans) <= N:
    ans += 1

print(ans)