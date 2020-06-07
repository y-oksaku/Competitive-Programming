N = int(input())
A = list(map(int, input().split()))
mx = max(A)
A = [a for a in A if a < mx]

A.sort(key=lambda a: abs(mx / 2 - a))
print(mx, A[0])
