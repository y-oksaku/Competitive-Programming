N = int(input())
A = list(map(int, input().split()))
A.sort()

B = A[N::][::2]
print(sum(B))
