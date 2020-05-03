A, B, N = map(int, input().split())

def f(x):
    return (A * x) // B - A * (x // B)

ans = f(N)
if B - 1 <= N:
    D = (N // B) * B
    ans = max(ans, f(D - 1))
print(ans)
