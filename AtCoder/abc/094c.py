from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
index = defaultdict(lambda: -1)
for i, b in enumerate(B):
    index[b] = i

for i in range(N):
    if index[A[i]] < N // 2:
        print(B[N // 2])
    else:
        print(B[N // 2 - 1])