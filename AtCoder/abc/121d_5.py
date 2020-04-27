A, B = map(int, input().split())

def g(x):
    if x % 2 == 1:
        return x // 2 % 2
    return x ^ g(x - 1)

print(g(A - 1) ^ g(B))
