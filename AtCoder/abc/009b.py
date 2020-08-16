N = int(input())
A = list(set([int(input()) for _ in range(N)]))
A.sort()
print(A[-2])
