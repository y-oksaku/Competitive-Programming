#include <bits/stdc++.h>
using namespace std;

template<class T = int, T INF = 1000000000>
class Dinic {
    struct Edge {
        T capacity, to, reverseEdge;
        Edge(){};
        Edge(T capacity, T to, T reverseEdge): capacity(capacity), to(to), reverseEdge(reverseEdge){};
    };

    private:
        T size;
        vector<vector<Edge>> edges;
        vector<T> depth;
        vector<T> progress;

        void bfs(T s) {
            vector<T> depth(this->size, -1);
            depth[s] = 0;
            deque<T> que(1, s);

            while (!que.empty()) {
                T now = que.front();
                que.pop_front();
                for(Edge e: this->edges[now]) {
                    if (e.capacity > 0 && depth[e.to] < 0) {
                        depth[e.to] = depth[now] + 1;
                        que.push_back(e.to);
                    }
                };
            }
            this->depth = depth;
        }

        T dfs(T s, T t, T flow) {
            if (s == t) return flow;
            vector<Edge> es = this->edges[s];
            for (T i = this->progress[s]; i < es.size(); i++) {
                this->progress[s] = i;
                Edge e = es[i];
                if (e.capacity == 0 || this->depth[s] >= this->depth[e.to]) continue;

                T d = this->dfs(e.to, t, min(flow, e.capacity));

                if (d == 0) continue;

                this->edges[s][i].capacity -= d;
                this->edges[e.to][e.reverseEdge].capacity += d;

                return d;
            }
            return 0;
        };

    public:
        Dinic (T size) {
            this->init(size);
        };

        void init(T size) {
            this->size = size;
            this->edges = vector<vector<Edge>>(size, vector<Edge>(0));
        };

        void addEdge(T fr, T to, T cap) {
            this->edges[fr].emplace_back(cap, to, this->edges[to].size());
            this->edges[to].emplace_back(0, fr, this->edges[fr].size() - 1);
        };

        T maxFlow(T s, T t) {
            T flow = 0;
            while (true) {
                this->bfs(s);
                if (this->depth[t] < 0) return flow;
                this->progress = vector<T>(this->size, 0);
                T currentFlow = this->dfs(s, t, INF);
                while (currentFlow > 0) {
                    flow += currentFlow;
                    currentFlow = this->dfs(s, t, INF);
                }
            }
        }
};