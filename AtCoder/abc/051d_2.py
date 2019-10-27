from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

INF = float('inf')

def sol():
    N, M = map(int, input().split())

    edges = []

    for _ in range(M):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edges.append((fr, to, cost))

    graph = [[INF] * N for _ in range(N)]
    for fr, to, cost in edges:
        graph[fr][to] = cost

    graph = csgraph_from_dense(graph, null_value=INF)

    dist = floyd_warshall(graph, directed=False)
    ans = (graph > dist).sum()
    print(ans)

sol()