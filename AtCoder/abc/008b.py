from collections import Counter

N = int(input())
cnt = list(Counter([input() for _ in range(N)]).items())
cnt.sort(key=lambda a: a[1])

print(cnt[-1][0])
