N = int(input())
D = list(map(int, input().split()))

def minGap(hour):
    ret = float('inf')
    for i in range(len(hour)):
        for j in range(len(hour)):
            if i == j:
                continue
            h1 = hour[i]
            h2 = hour[j]
            gap = max(h1, h2) - min(h1, h2)
            ret = min(ret, gap, 24 - gap)
    return ret

D.sort()
hour = [0]
for i, d in enumerate(D):
    if i % 2 == 0:
        hour.append(d)
    else:
        hour.append(24 - d)

print(minGap(hour))