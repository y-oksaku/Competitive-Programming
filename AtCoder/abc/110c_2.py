S = input()
T = input()

tToS = {}
sToT = {}
for s, t in zip(S, T):
    if not t in tToS:
        tToS[t] = s
    if not s in sToT:
        sToT[s] = t

    if tToS[t] != s or sToT[s] != t:
        print('No')
        exit()

print('Yes')
