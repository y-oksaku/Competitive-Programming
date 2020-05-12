S = input()
M = 2019

cnt = [0] * M
cnt[0] = 1
N = 0
ans = 0
for i, n in enumerate(map(int, S[::-1])):
    N = (N + n * pow(10, i, M)) % M
    ans += cnt[N]
    cnt[N] += 1
print(ans)
