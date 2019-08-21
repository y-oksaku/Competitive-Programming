from bisect import bisect_left

N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

conv = set(A)
conv = list(conv)
conv.sort()

for a in A:
    ans = bisect_left(conv, a)
    print(ans)