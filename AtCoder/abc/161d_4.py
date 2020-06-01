K = int(input())
A = [list(range(1, 10))]
cnt = 0

while cnt < K * 2:
    B = []
    for a in A[-1]:
        r = a % 10
        a *= 10
        for i in range(max(0, r - 1), min(r + 2, 10)):
            B.append(a + i)
    cnt += len(B)
    A.append(B)

A = [a for B in A for a in B]
A.sort()
print(A[K - 1])
