from itertools import combinations, product

N = int(input())
S = input()

keys = product('ABXY', repeat=2)
ans = N

for L, R in combinations(keys, 2):
    left = 0
    cnt = 0
    while left < N - 1:
        cnt += 1
        if S[left] == L[0] and S[left + 1] == L[1]:
            left += 2
        elif S[left] == R[0] and S[left + 1] == R[1]:
            left += 2
        else:
            left += 1
    if left == N - 1:
        cnt += 1
    ans = min(ans, cnt)

print(ans)