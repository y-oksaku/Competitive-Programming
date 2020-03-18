from collections import defaultdict

N = int(input())
S = input()
MOD = 10007
StoI = {'J': 0, 'O': 1, 'I': 2}

def isOk(prev, today, s):
    i = StoI[s]
    if (today & (1 << i)) == 0:
        return False
    if prev & today == 0:
        return False
    return True

prev = defaultdict(int)
prev[1] = 1
for s in S:
    today = defaultdict(int)
    for p, cnt in prev.items():
        cnt %= MOD
        for t in range(1 << 3):
            if isOk(p, t, s):
                today[t] += cnt
    prev = today

ans = sum(prev.values())
print(ans % MOD)
