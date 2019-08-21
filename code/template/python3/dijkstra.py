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
            newCost = minCosts[node] + weight
            heapq.heappush(nodeHeap, (newCost, nextNode))
    dist = minCosts[endNode]
    if dist == float('inf') :
        return -1
    return dist

N , M = map(int,input().split())

# edges , costs
edges = [[] for _ in range(N)]

# 辺の入力
for _ in range(M) :
    fromNode , toNode , cost = map(int,input().split())
    fromNode -= 1
    toNode -= 1

    edges[fromNode].append((toNode,cost))

    # 無向グラフの場合
    # nodes[toNode].append((fromNode,cost))

# スタート ゴール
startNode , endNode = map(int,input().split())
startNode -= 1
endNode -= 1

print(dijkstra(edges,startNode,endNode))
