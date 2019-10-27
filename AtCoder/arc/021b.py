L = int(input())
B = [int(input()) for _ in range(L)]

Ball = 0
for b in B:
    Ball ^= b

if Ball != 0:
    print(-1)
    exit()

A = [0] * L

for i in range(1, L):
    A[i] = A[i - 1] ^ B[i - 1]

print(*A, sep='\n')