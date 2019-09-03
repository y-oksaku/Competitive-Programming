N, va, vb, L = map(int, input().split())

taka = 0
kame = L

for _ in range(N):
    time = (kame - taka) / va
    taka, kame = kame, kame + time * vb

print(kame - taka)