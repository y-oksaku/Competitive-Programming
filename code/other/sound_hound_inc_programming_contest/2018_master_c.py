N, M, D = map(int, input().split())

# 美しい組：1-1+D, 2-2+D, ..., N-D-N

if D == 0:
    prob = 1 / N
else:
    prob = (N - D) / (N**2) * 2

ans = prob * (M - 1)
print(ans)