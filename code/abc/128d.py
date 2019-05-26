N , K = map(int,input().split())
D = list(map(int,input().split()))

maxValue = 0
actList = [0]*K

for i in range(4**K):
    act = i
    valList = []
    V = D.copy()

    for j in range(K):
        actList[j] = (act % 4)
        act = int(act / 4)

    for j in actList:
        if(j == 0): # 操作 A
            if(len(V) == 0):
                continue
            valList.append(V.pop(0))
        elif(j == 1): # B
            if(len(V) == 0):
                continue
            valList.append(V.pop())
        elif(j == 2): # C
            if(len(valList) == 0):
                continue
            V.insert(0,valList.pop(0))
        elif(j == 3): # D
            if(len(valList) == 0):
                continue
            V.append(valList.pop(0))
        valList.sort()

    val = sum(valList)
    if maxValue < val:
        maxValue = val

print(maxValue)

