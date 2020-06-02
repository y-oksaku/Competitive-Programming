L = int(input())
B = [int(input()) for _ in range(L)]

ans = [0] * L
for d in range(32):
    mask = (1 << d)
    for first in (0, 1):
        A = [(first << d)]
        for b in B:
            A.append(A[-1] ^ (b & mask))
        if A[0] == A[-1]:
            break
    else:
        print(-1)
        exit()

    for i, a in enumerate(A[:L]):
        ans[i] += a

print(*ans, sep='\n')
