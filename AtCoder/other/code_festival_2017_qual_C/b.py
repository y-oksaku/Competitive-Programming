from itertools import product

N = int(input())
A = list(map(int, input().split()))
ans = 0

for mask in product([-1, 0, 1], repeat=N):
    prd = 1
    for (a, d) in zip(A, mask):
        prd *= (a + d)
    if prd % 2 == 0:
        ans += 1

print(ans)