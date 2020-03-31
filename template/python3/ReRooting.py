class ReRooting:
    """
    0-indexed
    """
    def __init__(self, size, root=0, identDp=1, identCum=1):
        """
        identDp: 木DP用 lift(a, identDp) = a
        identCum: 累積用 merge(a, identCum) = a
        """
        self.size = size
        self.edges = [[] for _ in range(self.size + 1)]
        self.root = root
        self.identDp = identDp
        self.identCum = identCum

    def addEdge(self, fr, to):
        self.edges[fr].append(to)
        self.edges[to].append(fr)

    # 根を固定したときの木DP(貰うDP)
    def lift(self, top, bottom):
        return top * bottom

    # 親の左右の累積から子を根としたときの値を求める
    def merge(self, left, right):
        return left * right

    def sol(self):
        N = self.size
        edges = self.edges

        st = [self.root]
        parent = [-1] * (N + 1)
        child = [[] for _ in range(N + 1)]
        order = []
        while st:
            v = st.pop()
            order.append(v)
            for to in edges[v]:
                if parent[v] == to:
                    continue
                parent[to] = v
                child[v].append(to)
                st.append(to)

        dp = [self.identDp] * (N + 1)
        left = [self.identCum] * (N + 1)
        right = [self.identCum] * (N + 1)
        for v in order[::-1]:  # 貰うDPしつつ，累積をとる
            tmp = self.identCum
            for ch in child[v]:
                left[ch] = tmp
                tmp = self.lift(tmp, dp[ch])
            tmp = self.identCum
            for ch in reversed(child[v]):
                right[ch] = tmp
                tmp = self.lift(tmp, dp[ch])
            dp[v] = tmp

        fromParent = [self.identDp] * (N + 1)
        for v in order:
            if v == self.root:
                continue
            fromParent[v] = self.lift(self.merge(left[v], right[v]), fromParent[parent[v]])
            dp[v] = self.lift(dp[v], fromParent[v])  # 最後に親からの貰うDP

        return dp[:N]
