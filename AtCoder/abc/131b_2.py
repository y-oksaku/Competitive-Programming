N, L = map(int, input().split())

A = [L + i for i in range(N)]
A.sort(key=lambda a: abs(a))

print(sum(A) - A[0])
