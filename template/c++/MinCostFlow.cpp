#include <bits/stdc++.h>
using namespace std;

template<class T = int, T INF = 1000000000>
class MinCostFlow {
    struct Edge {
        T to, capacity, cost, reverseEdge;
        Edge(){};
        Edge(T to, T cap, T cost, T rev): to(to), capacity(cap), cost(cost), reverseEdge(rev) {};
    };

    private:
        T size;
        vector<vector<Edge>> edges;

    public:
        MinCostFlow (T size) {
            this->init(size);
        };

        void init(T size) {
            this->size = size;
            this->edges = vector<vector<Edge>>(size);
        };

        void addEdge(T fr, T to, T cap, T cost) {
            this->edges[fr].emplace_back(to, cap, cost, this->edges[to].size());
            this->edges[to].emplace_back(fr, 0, -cost, this->edges[fr].size() - 1);
        };

        T minCostFlow(T s, T t, T f) {
            T N = this->size;
            vector<vector<Edge>> edges = this->edges;

            T result = 0;
            vector<T> H(N, 0);
            vector<T> prevV(N, 0);
            vector<T> prevE(N, 0);

            while (f > 0) {
                vector<T> dist(N, INF);
                dist[s] = 0;

                priority_queue<pair<T, T>> que;
                que.emplace(0, s);
                while (!que.empty()) {
                    T c = -que.top().first;
                    T now = que.top().second;
                    que.pop();

                    if (dist[now] < c) continue;

                    for(T i = 0; i < edges[now].size(); i++) {
                        Edge e = edges[now][i];
                        if (e.capacity > 0 && (dist[e.to] > (dist[now] + e.cost + H[now] - H[e.to]))) {
                            T r = dist[now] + e.cost + H[now] - H[e.to];
                            dist[e.to] = r;
                            prevV[e.to] = now;
                            prevE[e.to] = i;
                            que.emplace(-r, e.to);
                        }
                    }
                }

                if (dist[t] == INF) return -INF;

                for(T i = 0; i < N; i++) H[i] += dist[i];

                T d = f;
                T now = t;
                while (now != s) {
                    d = min(d, edges[prevV[now]][prevE[now]].capacity);
                    now = prevV[now];
                }

                f -= d;
                result += d * H[t];
                now = t;
                while (now != s) {
                    Edge e = edges[prevV[now]][prevE[now]];
                    edges[prevV[now]][prevE[now]].capacity -= d;
                    edges[now][e.reverseEdge].capacity += d;
                    now = prevV[now];
                }
            }

            return result;
        };
};