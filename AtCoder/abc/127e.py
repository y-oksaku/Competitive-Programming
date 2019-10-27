from math import factorial

N , M , K = map(int,input().split())

ans = 0

facNM = factorial(N*M)
facK = factorial(K-2)
facNMK = factorial(N*M - K+2)
comb = facNM / facK / facNMK

for d in range(N) :
    ans += comb * (N-d) * M * M * d

for d in range(M) :
    ans += comb * (M-d) * N * N * d

print(int(ans % (10**9 + 7)))