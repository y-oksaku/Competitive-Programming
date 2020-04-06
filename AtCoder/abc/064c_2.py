N = int(input())
A = list(map(int, input().split()))

ans = set()
cnt = 0
for a in A:
    if a >= 3200:
        cnt += 1
    else:
        ans.add(a // 400)

mx = len(ans) + cnt
mi = max(1, len(ans))

print(mi, mx)
