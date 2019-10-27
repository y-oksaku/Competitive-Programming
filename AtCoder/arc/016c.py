N, M = map(int, input().split())
INF = float('inf')

kuji = []
for _ in range(M):
    idolNum, cost = map(int, input().split())
    prob = [[x for x in map(int, input().split())] for _ in range(idolNum)]
    kuji.append((idolNum, cost, prob))

dp = [0] * (1 << N)

def calc(state, k):
    _, cost, prob = kuji[k]
    newCost = 0
    fail = 0
    for idol, p in prob:
        bit = 1 << (idol - 1)
        if state & bit:
            newCost += p * dp[state ^ bit]
        else:
            fail += p
    if fail == 100:
        return INF
    else:
        return (100 * cost + newCost) / (100 - fail)

for state in range(1, 1 << N):
    dp[state] = min(calc(state, m) for m in range(M))

print(dp[-1])