S = input()
T = input()

# swap箇所が1箇所 or 3箇所の場合OK
# 同じ文字が含まれる場合は0~3箇所でOK

def cntSwap():
    swap = []
    for s, t in zip(S, T):
        if s != t:
            swap.append((s, t))
    if len(swap) // 2 > 10:
        return -1

    for s, t in swap:
        if len([(u, v) for u, v in swap if u == t]) == 0:
            return -1

    odd = []
    even = []
    for s, t in swap:
        if (t, s) in swap:
            if not (t, s) in even:
                even.append((s, t))
        else:
            odd.append((s, t))

    V = []
    for st in odd:
        V.extend(st)
    if len(set(V)) * 2 != len(V):
        return - 1

    return max(len(set(V)) - 1, 0) + len(even)

cnt = cntSwap()
if cnt == -1:
    print('NO')
    exit()

if cnt == 1 or cnt == 3:
    print('YES')
    exit()

if (cnt == 0 or cnt == 2) and len(set(S)) < len(S):
    print('YES')
    exit()

print('NO')
