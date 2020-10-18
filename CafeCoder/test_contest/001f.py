N = int(input())
A = list(map(int, input().split()))

aToI = {a: i for i, a in enumerate(A)}

dpL = 0
dpR = 0
prevL = 0
prevR = 0

for a in range(1, N + 1):
    i = aToI[a]

    l = (i + prevL) % N
    r = (i + prevR) % N

    L = min(dpL + min(l, N - l), dpR + min(r, N - r))
    R = min(dpL + min(l + 1, N - l - 1), dpR + min(r + 1, N - r - 1))
    dpL, dpR = L, R

    prevL = -i % N
    prevR = (-i - 1) % N

print(min(dpL, dpR) + N)
