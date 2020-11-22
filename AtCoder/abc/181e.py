from bisect import bisect_left

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

L = [0, 0]
S = 0
for l, r in zip(H[::2], H[1::2]):
    S += r - l
    L.append(S)
    L.append(S)
R = [0, 0]
S = 0
for r, l in zip(H[::-1][::2], H[::-1][1::2]):
    S += r - l
    R.append(S)
    R.append(S)
R = R[::-1]

ans = 10**18
for w in W:
    i = bisect_left(H, w)
    i ^= i % 2
    ans = min(ans, L[i] + R[i] + abs(w - H[i]))
print(ans)
