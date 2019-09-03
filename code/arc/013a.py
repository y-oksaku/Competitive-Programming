from itertools import permutations

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

ans = 0
for p, q, r in permutations([P, Q, R]):
    ans = max(ans, (N // p) * (M // q) * (L // r))

print(ans)
