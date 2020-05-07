S = input()
T = input()

def isOk():
    sToT = {}
    tToS = {}
    for s, t in zip(S, T):
        if not s in sToT:
            sToT[s] = t
        elif sToT[s] != t:
            return False
        if not t in tToS:
            tToS[t] = s
        elif tToS[t] != s:
            return False
    return True

print('Yes' if isOk() else 'No')
