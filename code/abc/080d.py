N, C = map(int, input().split())

channels = [[] for _ in range(C)]
maxT = 0

for _ in range(N) :
    s, t, c = map(int, input().split())
    maxT = max(maxT, t)
    channels[c - 1].append((s, t))

maxT = maxT * 2 + 10
tvSum = [0 for _ in range(maxT)]

for tv in channels :
    imos = [0 for _ in range(maxT)]
    for (s, t) in tv :
        imos[s * 2 - 1] += 1
        imos[t * 2] -= 1
    for i in range(1, maxT) :
        imos[i] += imos[i - 1]
    for i in range(maxT) :
        if imos[i] > 0 :
            tvSum[i] += 1

print(max(tvSum))
