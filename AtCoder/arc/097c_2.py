S = input()
K = int(input())

A = set()
for leng in range(1, K + 1):
    for i in range(len(S) - leng + 1):
        A.add(S[i: i + leng])
A = list(A)
A.sort()

print(A[K - 1])
