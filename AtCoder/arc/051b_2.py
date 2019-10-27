K = int(input())

A = 1
B = 0

for _ in range(K + 1):
    A, B = A + B, A

print(A, B)