from itertools import product

N = int(input())
A = [list(map(int, input().split())) for _ in range(N - 1)]

ans = -10**18
for P in product(range(3), repeat=N):
    cnt = 0
    for i, a in enumerate(A):
        for j, c in enumerate(a, start=i + 1):
            if P[i] == P[j]:
                cnt += c
    ans = max(ans, cnt)
print(ans)
