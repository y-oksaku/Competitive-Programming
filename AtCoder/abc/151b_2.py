N, K, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

ness = M * N - S
if ness > K:
    print('-1')
    exit()
print(max(0, ness))
