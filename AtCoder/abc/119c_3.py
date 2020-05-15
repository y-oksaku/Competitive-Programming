from itertools import product

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

ans = 10**18
for state in product(range(4), repeat=N):
    K = [[] for _ in range(4)]
    for i, l in enumerate(L):
        K[state[i]].append(l)

    cost = 0
    for d, D in zip((A, B, C), K):
        if len(D) == 0:
            cost += 10**18
        cost += (len(D) - 1) * 10
        cost += abs(d - sum(D))
    ans = min(ans, cost)

print(ans)
