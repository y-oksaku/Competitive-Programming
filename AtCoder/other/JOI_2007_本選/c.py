import bisect

N, M = map(int,input().split())

P = [0]
for _ in range(N) :
    a = int(input())
    P.append(a)

Q = []

for p in P :
    for q in P :
        Q.append(p + q)

Q = list(set(Q))
Q.sort()

ans = 0
for q in Q :
    if q > M :
        break
    right = bisect.bisect_right(Q, M-q) - 1
    if right < 0 :
        break
    newVal = q + Q[right]
    ans = max(ans, newVal)

print(ans)