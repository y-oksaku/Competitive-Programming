N = int(input())

ans = 10**18
for w in range(1, N + 1):
    h, r = divmod(N, w)
    ans = min(ans, abs(w - h) + r)
print(ans)
