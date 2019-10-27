#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <cassert>
#include <queue>
#include <random>
#include <stack>
#include <iomanip>

using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

typedef unsigned int uint;
typedef long long llong;
typedef unsigned long long ullong;
typedef long double ldouble;

typedef vector<llong> vecllong;
typedef vector<vecllong> vvecllong;

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

                FOR(i, N) {
                    H[i] += dist[i];
                }

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

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong R, G, B;
    cin >> R >> G >> B;

    vecllong pos(3);
    pos[0] = -100;
    pos[1] = 0;
    pos[2] = 100;

    llong bias = 300 * 3;
    llong N = bias * 2;

    MinCostFlow flow(N + 5);
    llong s = N + 0;
    llong t = N + 1;

    vecllong box(3);
    box[0] = N + 2;
    box[1] = N + 3;
    box[2] = N + 4;

    FOR(i, N) {
        flow.addEdge(box[0], i, 1, abs(pos[0] - (i - bias)));
        flow.addEdge(box[1], i, 1, abs(pos[1] - (i - bias)));
        flow.addEdge(box[2], i, 1, abs(pos[2] - (i - bias)));
    }

    flow.addEdge(s, box[0], R, 0);
    flow.addEdge(s, box[1], G, 0);
    flow.addEdge(s, box[2], B, 0);

    FOR(i, N) {
        flow.addEdge(i, t, 1, 0);
    }

    llong ans = flow.minCostFlow(s, t, R + G + B);
    cout << ans << endl;

    return 0;
}