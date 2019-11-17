A = list(map(int, input().split()))
V = []

for i, a in enumerate(A):
    for j, b in enumerate(A[i + 1:], start=i + 1):
        for c in A[j + 1:]:
            V.append(a + b + c)
V.sort()
print(V[-3])