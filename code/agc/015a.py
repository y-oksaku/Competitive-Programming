N, A, B = map(int, input().split())

if A > B or (N == 1 and A != B):
    print(0)
    exit()

if N == 1 or A == B:
    print(1)
    exit()

minS = A * (N - 1) + B
maxS = A + B * (N - 1)

print(maxS - minS + 1)