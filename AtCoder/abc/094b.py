N, M, X = map(int, input().split())
A = list(map(int, input().split()))

L, R = 0, 0
for a in A:
    if a < X:
        L += 1
    if a > X:
        R += 1
print(min(L, R))
