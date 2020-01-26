from bisect import bisect_right

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]
XH.sort()

X = [x for x, _ in XH]

ans = 0
ims = [0] * (N + 1)
cnt = 0

for now, (x, h) in enumerate(XH):
    cnt += ims[now]
    if cnt * A >= h:
        continue
    ness = -(-(h - cnt * A) // A)
    cnt += ness

    i = bisect_right(X, x + D * 2)
    ims[now] += ness
    ims[i] -= ness
    ans += ness

print(ans)