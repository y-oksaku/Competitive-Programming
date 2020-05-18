S = input()
N = len(S)
K = int(input())

A = set()
for i in range(N):
    for j in range(i + 1, N + 1):
        if j > i + K:
            break
        A.add(S[i:j])

A = list(A)
A.sort()
print(A[K - 1])
