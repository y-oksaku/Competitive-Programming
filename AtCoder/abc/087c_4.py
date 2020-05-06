N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

R = [0] * N
for i, b in enumerate(B[::-1], start=1):
    R[-i] = R[-(i - 1)] + b

ans = 0
S = 0
for i, a in enumerate(A):
    S += a
    ans = max(ans, S + R[i])
print(ans)
