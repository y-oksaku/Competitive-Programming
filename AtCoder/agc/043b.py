N = int(input())
A = list(map(lambda a: int(a) - 1, input()))

prd = 1
if all(a % 2 == 0 for a in A):
    prd = 2
    A = [a // 2 for a in A]

ans = 0
for i in range(N):
    if (N - 1) & i == i:
        ans ^= A[i] % 2

print(prd * ans)
