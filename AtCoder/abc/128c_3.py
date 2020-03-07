N, M = map(int, input().split())

S = []
for _ in range(M):
    s = tuple(map(lambda a: int(a) - 1, input().split()))[1:]
    S.append(s)

P = tuple(map(int, input().split()))

ans = 0
for state in range(1 << N):
    for p, s in zip(P, S):
        cnt = 0
        for i in s:
            cnt += 1 if (state & (1 << i)) > 0 else 0
        if cnt % 2 != p:
            break
    else:
        ans += 1

print(ans)
