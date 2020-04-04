N = 100
edges = [[] for _ in range(N)]

def isBipartite():
    """
    2部グラフ判定
    """
    sign = [-1] * N
    sign[0] = 0
    st = [0]
    while st:
        now = st.pop()
        p = sign[now] ^ 1

        for to in edges[now]:
            if sign[to] == -1:
                st.append(to)
                sign[to] = p
                continue
            if sign[to] != p:
                return -1

    return sum(sign)
