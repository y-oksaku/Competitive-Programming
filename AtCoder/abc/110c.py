S = list(input())
T = list(input())

countT = {}
countS = {}

for s, t in zip(S, T) :
    if t in countT :
        countT[t].append(s)
    else :
        countT[t] = [s]
    if s in countS :
        countS[s].append(t)
    else :
        countS[s] = [t]

for (_, s), (_, t) in zip(countS.items(), countT.items()) :
    if len(set(s)) >= 2 or len(set(t)) >= 2:
        print('No')
        break
else :
    print('Yes')
