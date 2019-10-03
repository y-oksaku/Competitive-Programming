#include <vector>
#include <deque>
#include <algorithm>

using namespace std;
typedef long long llong;
typedef vector<llong> vecllong;
typedef vector<vector<llong>> vvecllong;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

struct edge {
    llong capacity;
    llong to;
    llong reverseEdge;
};

class Dinic {
    private:
        llong size;
        vector<vector<edge>> edges;
        vecllong depth;
        vecllong progress;

        void bfs(llong s) {
            vecllong depth(this->size, -1);
            depth[s] = 0;
            deque<llong> que(1, s);

            while (!que.empty()) {
                llong now = que.front();
                que.pop_front();
                for_each(this->edges[now].begin(), this->edges[now].end(), [&](edge e) {
                    if (e.capacity > 0 && depth[e.to] < 0) {
                        depth[e.to] = depth[now] + 1;
                        que.push_back(e.to);
                    }
                });
            }
            this->depth = depth;
        }

        llong dfs(llong s, llong t, llong flow) {
            if (s == t) return flow;
            vector<edge> es = this->edges[s];
            FORS(i, this->progress[s], es.size()) {
                this->progress[s] = i;
                edge e = es[i];
                if (e.capacity == 0 || this->depth[s] >= this->depth[e.to]) continue;

                llong d = this->dfs(e.to, t, min(flow, e.capacity));

                if (d == 0) continue;

                this->edges[s][i].capacity -= d;
                this->edges[e.to][e.reverseEdge].capacity += d;

                return d;
            }
            return 0;
        };

    public:
        Dinic (llong size) {
            this->init(size);
        };

        void init(llong size) {
            this->size = size;
            this->edges = vector<vector<edge>>(size, vector<edge>(0));
        };

        void addEdge(llong fr, llong to, llong cap) {
            this->edges[fr].push_back({cap, to, this->edges[to].size()});
            this->edges[to].push_back({0, fr, this->edges[fr].size() - 1});
        };

        llong maxFlow(llong s, llong t) {
            llong flow = 0;
            while (true) {
                this->bfs(s);
                if (this->depth[t] < 0) return flow;
                this->progress = vecllong(this->size, 0);
                llong currentFlow = this->dfs(s, t, INF);
                while (currentFlow > 0) {
                    flow += currentFlow;
                    currentFlow = this->dfs(s, t, INF);
                }
            }
        }
};
