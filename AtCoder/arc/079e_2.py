N = int(input())
A = list(map(int, input().split()))

ans = 0
while max(A) >= N:
    i = A.index(max(A))
    k = A[i] // N
    A[i] %= N
    ans += k
    for j in range(N):
        if j != i:
            A[j] += k
print(ans)
