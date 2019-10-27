def dijkstra(edge,start,end) :
    import heapq

    minCosts = [float('inf') for _ in range(len(edge))]

    nodeHeap = []
    heapq.heappush(nodeHeap, (0, start))  # (cost, node)

    while nodeHeap :
        cost, node = heapq.heappop(nodeHeap)

        if minCosts[node] <= cost :
            continue

        minCosts[node] = cost

        for nextNode , weight in edge[node] :
            newCost = cost + weight
            heapq.heappush(nodeHeap, (newCost, nextNode))
    dist = minCosts[endNode]
    if dist == float('inf') :
        return -1
    return dist

N , M = map(int,input().split())

# edges , costs
nodes = [[] for _ in range(3 * N)]

# 辺の入力
for _ in range(M) :
    fromNode , toNode = map(int,input().split())
    fromNode -= 1
    toNode -= 1
    fromNode *= 3
    toNode *= 3

    nodes[fromNode].append((toNode + 1,1))
    nodes[fromNode + 1].append((toNode + 2,1))
    nodes[fromNode + 2].append((toNode,1))

# スタート ゴール
startNode , endNode = map(int,input().split())
startNode -= 1
endNode -= 1
startNode *= 3
endNode *= 3

ans = dijkstra(nodes,startNode,endNode)

if ans == -1 :
    print(ans)
else :
    print(ans // 3)