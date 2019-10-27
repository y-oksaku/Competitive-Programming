#include <vector>
#include <algorithm>
#include <queue>

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
    llong to;
    llong capacity;
    llong cost;
    llong reverseEdge;
};

class MinCostFlow {
    private:
        llong size;
        vector<vector<edge>> edges;

    public:
        MinCostFlow (llong size) {
            this->init(size);
        };

        void init(llong size) {
            this->size = size;
            this->edges = vector<vector<edge>>(size);
        };

        void addEdge(llong fr, llong to, llong cap, llong cost) {
            this->edges[fr].push_back({to, cap, cost, this->edges[to].size()});
            this->edges[to].push_back({fr, 0, -cost, this->edges[fr].size() - 1});
        };

        llong minCostFlow(llong s, llong t, llong f) {
            llong N = this->size;
            vector<vector<edge>> edges = this->edges;

            llong result = 0;
            vecllong H(N, 0);
            vecllong prevV(N, 0);
            vecllong prevE(N, 0);

            while (f > 0) {
                vecllong dist(N, INF);
                dist[s] = 0;

                priority_queue<pair<llong, llong>> que;
                que.push({0, s});
                while (!que.empty()) {
                    llong c = -que.top().first;
                    llong now = que.top().second;
                    que.pop();

                    if (dist[now] < c) continue;

                    FOR(i, edges[now].size()) {
                        edge e = edges[now][i];
                        if (e.capacity > 0 && (dist[e.to] > (dist[now] + e.cost + H[now] - H[e.to]))) {
                            llong r = dist[now] + e.cost + H[now] - H[e.to];
                            dist[e.to] = r;
                            prevV[e.to] = now;
                            prevE[e.to] = i;
                            que.push({-r, e.to});
                        }
                    }
                }

                if (dist[t] == INF) return -INF;

                FOR(i, N) H[i] += dist[i];

                llong d = f;
                llong now = t;
                while (now != s) {
                    d = min(d, edges[prevV[now]][prevE[now]].capacity);
                    now = prevV[now];
                }

                f -= d;
                result += d * H[t];
                now = t;
                while (now != s) {
                    edge e = edges[prevV[now]][prevE[now]];
                    edges[prevV[now]][prevE[now]].capacity -= d;
                    edges[now][e.reverseEdge].capacity += d;
                    now = prevV[now];
                }
            }

            return result;
        };
};