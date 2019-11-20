N, M = map(int, input().split())

lights = []
for _ in range(M):
    S = list(map(int, input().split()))
    mask = 0
    for a in S[1:]:
        mask |= (1 << (a - 1))
    lights.append(mask)

P = list(map(int, input().split()))

ans = 0
for mask in range(1 << N):
    for state, p in zip(lights, P):
        cnt = 0
        for d in range(N):
            if ((1 << d) & state) > 0 and ((1 << d) & mask) > 0:
                cnt += 1
        if cnt % 2 != p:
            break
    else:
        ans += 1

print(ans)
