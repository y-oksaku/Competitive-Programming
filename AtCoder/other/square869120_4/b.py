N, K = map(int, input().split())
A = list(map(int, input().split()))

def cost(state):
    now = 0
    ret = 0
    cnt = 0
    for d, a in enumerate(A):
        if (state & (1 << d)) > 0:
            cnt += 1
            ret += max(0, now + 1 - a)
            now = max(now + 1, a)
        else:
            now = max(now, a)

    return ret if cnt >= K else 10**20

ans = 10**20
for state in range(1 << N):
    ans = min(ans, cost(state))

print(ans)
