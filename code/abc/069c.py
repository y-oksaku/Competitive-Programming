from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

modCount = defaultdict(int)

for a in A:
    modCount[a % 4] += 1

ness = modCount[1] + modCount[3] + modCount[2] % 2
if ness <= modCount[0] + 1:
    print('Yes')
else:
    print('No')

