import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10**9 + 7
N, K = map(int,input().split())

edge = [[] for _ in range(N)]

for _ in range(N-1) :
    fromNode, toNode = map(int,input().split())

    fromNode -= 1
    toNode -= 1

    edge[fromNode].append(toNode)
    edge[toNode].append(fromNode)

# 深さ優先探索
def bfs(nowNode, fromNode) :
    colorNum = K  # 使用可能な色の数
    if fromNode == -1 :  # 根の場合
        colorNum -= 1
    else :
        colorNum -= 2

    if len(edge[nowNode]) - 1 > K :  # つながっている頂点数 - 1(親) == K までOK
        return 0

    caseNum = 1
    for nextNode in edge[nowNode] :
        if nextNode == fromNode :
            continue
        caseNum *= colorNum
        colorNum -= 1
        caseNum = caseNum % MOD

    for nextNode in edge[nowNode] :
        if nextNode == fromNode :
            continue
        caseNum *= bfs(nextNode, nowNode)
        caseNum = caseNum % MOD

    return caseNum

ans = bfs(0, -1) * K
ans = ans % MOD
print(ans)

