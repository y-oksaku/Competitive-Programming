M, K = map(int, input().split())

if K == 0:
    ans = list(range(1 << M)[:: -1]) + list(range(1 << M))
    print(*ans)
    exit()

A = []
B = []

used = [False] * (1 << M)
for d in range(M):
    if ((1 << d) & K) != 0:
        A.append(1 << d)
        used[1 << d] = True

for i in range(1 << M):
    if used[i]:
        continue
    else:
        B.append(i)

xorA = 0
for a in A:
    xorA ^= a

xorB = 0
for b in B:
    xorB ^= b

if xorA != K or xorB != K:
    print(-1)
    exit()

A.sort()
B.sort()
ans = A + B + A[:: -1] + B[:: -1]
print(*ans)
