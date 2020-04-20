from itertools import permutations

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

ans = 0
for n, m, l in permutations((P, Q, R), r=3):
    ans = max(ans, (N // n) * (M // m) * (L // l))
print(ans)
