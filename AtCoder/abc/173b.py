from collections import Counter
N = int(input())
ans = Counter([input() for _ in range(N)])

for s in ['AC', 'WA', 'TLE', 'RE']:
    print(s, 'x', ans[s])
