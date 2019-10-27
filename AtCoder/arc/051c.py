from heapq import heapify, heappush, heappop

N, A, B = map(int, input().split())
X = list(map(int, input().split()))
MOD = 10**9 + 7

if A == 1:
    X.sort()
    ans = [x % MOD for x in X]
    print(*ans, sep='\n')
    exit()

heapify(X)
maxX = max(X)

while B > 0 and X[0] * A < maxX:
    x = heappop(X)
    x *= A
    B -= 1
    maxX = max(maxX, x)
    heappush(X, x)

X.sort()

q, r = divmod(B, N)
mul = pow(A, q, MOD)
ans = []
for x in X[r:]:
    ans.append(x * mul % MOD)

for x in X[: r]:
    ans.append(x * mul * A % MOD)

print(*ans, sep='\n')