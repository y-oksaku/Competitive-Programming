#include <bits/stdc++.h>
using namespace std;

template<class T = int>
class LCA {
    struct Edge {
        T to, cost;
        Edge(){};
        Edge(T to, T cost): to(to), cost(cost) {};
    };

    private:
        T size;
        T level;
        vector<vector<Edge>> edges;
        vector<T> depth;
        vector<T> length;
        vector<T> prev;
        vector<vector<T>> kprev;

        void dfs(T root) {
            stack<pair<T, T>> st;
            st.emplace(root, root);
            this->depth[root] = 0;
            this->length[root] = 0;
            while (!st.empty()) {
                T now = st.top().first, prev = st.top().second;
                st.pop();

                for (Edge e: this->edges[now]) {
                    if (e.to == prev) continue;
                    st.emplace(e.to, now);
                    this->depth[e.to] = this->depth[now] + 1;
                    this->length[e.to] = this->length[now] + e.cost;
                    this->prev[e.to] = now;
                }
            }
        }

    public:
        LCA(T size) {
            this->size = size;
            this->level = 1;
            while((1 << (this->level - 1)) < size - 1) this->level++;
            this->edges.assign(size, vector<Edge>(0));
            this->depth.assign(size, 0);
            this->length.assign(size, 0);
            this->prev.assign(size, -1);
        };

        void addEdge(T fr, T to, T cost = 1) {
            this->edges[fr].emplace_back(to, cost);
            this->edges[to].emplace_back(fr, cost);
        }

        void construct(T root = 0) {
            this->dfs(root);
            this->kprev.resize(0);
            this->kprev.emplace_back(this->prev);
            vector<T> S = this->prev;

            for(int _ = 0; _ < this->level; _++) {
                vector<T> U(this->size, 0);
                for(T i = 0; i < this->size; i++) {
                    if (S[i] == -1) continue;
                    U[i] = S[S[i]];
                }
                this->kprev.emplace_back(U);
                S = U;
            }
        }

        T lca(T u, T v) {
            T dist = this->depth[v] - this->depth[u];
            if (dist < 0) {
                swap(u, v);
                dist = -dist;
            }

            for(T k = 0; k < this->level + 1; k++) {
                if(dist & 1) v = this->kprev[k][v];
                dist /= 2;
            }

            if (u == v) return u;

            for(T k = this->level - 1; k >= 0; k--) {
                T prevU = this->kprev[k][u];
                T prevV = this->kprev[k][v];
                if (prevU != prevV) {
                    u = prevU;
                    v = prevV;
                }
            }

            return this->kprev[0][u];
        }

        T dist(T u, T v) {
            return this->depth[u] + this->depth[v] - this->depth[this->lca(u, v)] * 2;
        }
};