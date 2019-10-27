from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = list(Counter(A).items())
count.sort(key=lambda A : A[1])

rNum = len(count) - K
ans = sum([a[1] for a in count[:rNum]])

print(ans)
