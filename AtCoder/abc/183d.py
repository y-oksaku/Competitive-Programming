N, W = map(int, input().split())
L = 3 * 10**5

imos = [0] * L
for _ in range(N):
    s, t, p = map(int, input().split())
    imos[s] += p
    imos[t] -= p

for i in range(L - 1):
    imos[i + 1] += imos[i]

print('Yes' if max(imos) <= W else 'No')
