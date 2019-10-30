from collections import defaultdict

S = input()
N = len(S)
M = N * (N + 1) // 2

indexes = defaultdict(lambda : [0])
for i, s in enumerate(S, start=1):
    indexes[s].append(i)

ans = 0
for s, index in indexes.items():
    index.append(N + 1)
    cnt = 0
    for left, right in zip(index, index[1:]):
        cnt += (right - left - 1) * (right - left) // 2
    ans += M - cnt

print(ans / M)
