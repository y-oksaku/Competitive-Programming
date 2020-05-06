N = int(input())

F = []
for _ in range(N):
    mask = 0
    for f in map(int, input().split()):
        mask <<= 1
        mask |= f
    F.append(mask)

P = [list(map(int, input().split())) for _ in range(N)]

def calc(state):
    ret = 0
    for f, ps in zip(F, P):
        f &= state
        cnt = 0
        while f > 0:
            cnt += f % 2
            f //= 2
        ret += ps[cnt]
    return ret

ans = -10**18
for state in range(1, 1 << 10):
    ans = max(ans, calc(state))
print(ans)
