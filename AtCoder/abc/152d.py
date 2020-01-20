from collections import defaultdict
N = int(input())

cnt = defaultdict(int)

for a in range(1, N + 1):
    cnt[(str(a)[0], str(a)[-1])] += 1

ans = 0
for head in range(1, 10):
    for tail in range(1, 10):
        ans += cnt[(str(head), str(tail))] * cnt[(str(tail), str(head))]

print(ans)