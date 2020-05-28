A, B, X = map(int, input().split())

def f(N):
    return N // X

print(f(B) - f(A - 1))
