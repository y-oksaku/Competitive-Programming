N = int(input())
A = list(map(int,input().split()))

A.sort()

ans = A[-1] - sum(A[0:N-1])

print(ans)
