N = int(input())
A = list(map(int, input().split()))

mx = 0
ans = -1
for k in range(2, 1001):
    cnt = 0
    for a in A:
        if a % k == 0:
            cnt += 1
    if mx < cnt:
        ans = k
        mx = cnt
print(ans)
