N = int(input())
D = [int(input()) for _ in range(N)]

mx = sum(D)
S = sum(D) - D[0] - max(D)

mi = max(0, abs(D[0] - max(D)) - S)
print(mx)
print(mi)
