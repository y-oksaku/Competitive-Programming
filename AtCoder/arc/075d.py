N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

ng = 0
ok = sum([-(-h // A) for h in H])

while (ok - ng) > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for h in H:
        if h <= B * mid:
            continue
        cnt += -(-(h - B * mid) // (A - B))
    if cnt <= mid:
        ok = mid
    else:
        ng = mid
print(ok)