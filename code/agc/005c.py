from collections import Counter, deque

N = int(input())
A = list(map(int, input().split()))

cntA = Counter(A)
valA = list(set(A))
valA.sort(reverse=True)

pathLeng = [0] * (N + 1)

if cntA[valA[0]] < 2 or cntA[valA[-1]] > 2:
    print('Impossible')
    exit()

pathLeng[1] = valA[0]
pathLeng[2] = valA[0]
cntA[valA[0]] -= 2
maxNode = 2

pr = [[] for _ in range(N + 1)]
ch = [[] for _ in range(N + 1)]

for i, a in enumerate(valA[1:], start=2):
    if a == valA[-1] and cntA[valA[-1]] == 1:
        prevLeft = maxNode
        prevRight = maxNode - 1
        maxNode += 1
        ch[prevLeft].append(maxNode)
        ch[prevRight].append(maxNode)
        pr[maxNode].append(prevLeft)
        pr[maxNode].append(prevRight)
        pathLeng[maxNode] = valA[-1]
        cntA[valA[-1]] -= 1
        break

    prevLeft = (i - 1) * 2 - 1
    prevRight = (i - 1) * 2
    nowLeft = i * 2 - 1
    nowRight = i * 2

    maxNode = max(maxNode, nowRight)
    if maxNode > N:
        print('Impossible')
        exit()

    pathLeng[nowLeft] = a
    pathLeng[nowRight] = a

    cntA[a] -= 2

    ch[prevLeft].append(nowLeft)
    ch[prevRight].append(nowRight)
    pr[nowLeft].append(prevLeft)
    pr[nowRight].append(prevRight)
else:
    ch[maxNode].append(maxNode - 1)
    pr[maxNode - 1].append(maxNode)

for a, c in cntA.items():
    for _ in range(c):
        maxNode += 1
        i = pathLeng.index(a)
        ch[maxNode].append(ch[i][0])
        pr[ch[i][0]].append(maxNode)
        pathLeng[maxNode] = a
        cntA[a] -= 1

def search(index):
    visited = [False] * (N + 1)
    visited[index] = True
    st = deque([(index, 0)])
    ret = 0

    while st:
        now, d = st.pop()
        ret = max(ret, d)

        for to in pr[now]:
            if not visited[to]:
                st.append((to, d + 1))
                visited[to] = True
        for to in ch[now]:
            if not visited[to]:
                st.append((to, d + 1))
                visited[to] = True
    return ret

for i, d in enumerate(pathLeng[1:], start=1):
    if search(i) != d:
        print('Impossible')
        exit()

for v in cntA.values():
    if v != 0:
        print('Impossible')
        exit()

A.sort()
pathLeng.sort()

if A == pathLeng[1:]:
    print('Possible')
else:
    print('Impossible')