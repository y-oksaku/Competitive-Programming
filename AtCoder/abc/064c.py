from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

colorCount = defaultdict(int)

for a in A:
    if a < 400:
        colorCount['a'] += 1
    elif a < 800:
        colorCount['b'] += 1
    elif a < 1200:
        colorCount['c'] += 1
    elif a < 1600:
        colorCount['d'] += 1
    elif a < 2000:
        colorCount['e'] += 1
    elif a < 2400:
        colorCount['f'] += 1
    elif a < 2800:
        colorCount['g'] += 1
    elif a < 3200:
        colorCount['h'] += 1
    else:
        colorCount['z'] += 1

minAns = len(colorCount)
maxAns = minAns
if colorCount['z'] > 0:
    if minAns == 1:
        minAns = 1
        maxAns = colorCount['z']
    else:
        minAns -= 1
        maxAns = maxAns - 1 + colorCount['z']

print(minAns, maxAns)