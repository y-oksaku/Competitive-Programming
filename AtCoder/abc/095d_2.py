N, C = map(int, input().split())
INF = 10**20
rightSushi = [tuple(map(int, input().split())) for _ in range(N)]
leftSushi = [(C - x, v) for x, v in rightSushi[:: -1]]

def calc(sushi):
    ret = [-INF] * (N + 1)
    ret[0] = 0
    vSum = 0
    for i, (x, v) in enumerate(sushi, start=1):
        vSum += v
        ret[i] = max(vSum - x, ret[i - 1])
    return ret

leftV = calc(leftSushi)
rightV = calc(rightSushi)

def sol(sushi, maxV):
    ret = 0
    vSum = 0
    for i, (x, v) in enumerate(sushi, start=1):
        vSum += v
        ret = max(
            ret,
            vSum - x,
            vSum - x * 2 + maxV[N - i]
        )
    return ret

ans = max(sol(rightSushi, leftV), sol(leftSushi, rightV))

print(ans)