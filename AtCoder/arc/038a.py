N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = sum(A[::2])

print(ans)