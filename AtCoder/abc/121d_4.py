A, B = map(int, input().split())

def g(x):
    if x % 2 == 0:
        return x ^ g(x - 1)
    return 1 if (x // 2) % 2 == 0 else 0

print(g(B) ^ g(A - 1))
