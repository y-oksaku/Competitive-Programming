from bisect import bisect_right

A , B , Q = map(int,input().split())
INF = 10**20

s = [0] * A
t = [0] * B
x = [0] * Q

for i in range(A) :
    s[i] = int(input())
for i in range(B) :
    t[i] = int(input())
for i in range(Q) :
    x[i] = int(input())

s = [-INF] + s + [INF]
t = [-INF] + t + [INF]

for p in x :
    rightS = bisect_right(s,p)
    rightT = bisect_right(t,p)

    dist = INF

    for ss in [s[rightS - 1], s[rightS]] :
        for tt in [t[rightT - 1], t[rightT]] :
            dist1 = abs(ss - p) + abs(ss - tt)
            dist2 = abs(tt - p) + abs(tt - ss)
            dist = min(dist, dist1, dist2)

    print(dist)
