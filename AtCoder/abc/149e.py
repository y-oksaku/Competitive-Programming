from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def doesOver(k):
    cnt = 0
    for a in A:
        cnt += N - bisect_left(A, k - a)
    return cnt >= M

overEq = 0
less = A[-1] * 2 + 100

while less - overEq > 1:
    mid = (less + overEq) // 2
    if doesOver(mid):
        overEq = mid
    else:
        less = mid

accA = [0] * (N + 1)
for i in range(1, N + 1):
    accA[i] = accA[i - 1] + A[i - 1]

ans = 0
cnt = 0
for a in A:
    left = bisect_left(A, overEq - a)
    ans += accA[N] - accA[left]
    ans += (N - left) * a
    cnt += N - left

ans -= (cnt - M) * overEq
print(ans)
