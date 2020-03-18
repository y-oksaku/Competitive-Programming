A, B, K = map(int, input().split())

while True:
    if K == 0:
        break
    if A % 2 == 1:
        A -= 1
    A //= 2
    B += A
    K -= 1

    if K == 0:
        break
    if B % 2 == 1:
        B -= 1
    B //= 2
    A += B
    K -= 1

print(A, B)
