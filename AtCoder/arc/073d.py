N, W = map(int, input().split())

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((v, w))

w0 = items[0][1]
itemGrp = [[] for _ in range(4)]
for v, w in items:
    itemGrp[w - w0].append(v)

for i in range(4):
    itemGrp[i].sort(reverse=True)

accItemGrp = []
for i in range(4):
    item = itemGrp[i]
    accValue = [0] * (len(item) + 1)
    for i in range(1, len(item) + 1):
        accValue[i] = accValue[i - 1] + item[i - 1]
    accItemGrp.append(accValue)

ans = 0
for n0 in range(len(itemGrp[0]) + 1):
    for n1 in range(len(itemGrp[1]) + 1):
        for n2 in range(len(itemGrp[2]) + 1):
            for n3 in range(len(itemGrp[3]) + 1):
                weight = (n0 + n1 + n2 + n3) * w0 + n1 + 2 * n2 + 3 * n3
                if weight <= W:
                    value = 0
                    for i, n in enumerate([n0, n1, n2, n3]):
                        value += accItemGrp[i][n]
                    ans = max(ans, value)

print(ans)
