N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ness = N * M - sum(A)

if ness > K:
    print(-1)
else:
    print(max(0, ness))