from bisect import bisect_right
N, M = map(int, input().split())
S = input()

A = [i for i, s in enumerate(S) if s == '0']
now = N
ans = []

while True:
    left = bisect_right(A, now - M - 1)
    new = A[left]
    ans.append(now - new)
    if new == 0:
        break
    if new == now:
        print(-1)
        exit()
    now = new

print(*ans[:: -1])