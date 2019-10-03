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
            this->edges[to].push_back({cap, fr, this->edges[fr].size() - 1});
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

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, G, E;
    cin >> N >> G >> E;

    vecllong P(G);
    FOR(i, G) cin >> P[i];

    vvecllong edges(N, vecllong(0));
    vector<pair<llong, llong>> A(E);

    FOR(i, E) {
        llong fr, to;
        cin >> fr >> to;
        edges[fr].push_back(to);
        edges[to].push_back(fr);
        A[i] = {fr, to};
    }

    vecllong depth(N + 1, -1);
    stack<llong> st;
    st.push(0);
    depth[0] = 0;

    while (!st.empty()) {
        llong now = st.top();
        st.pop();
        for_each(edges[now].begin(), edges[now].end(), [&](llong to) {
            if (depth[to] == -1) {
                depth[to] = depth[now] + 1;
                st.push(to);
            }
        });
    }

    Dinic flow(N + 1);
    FOR(i, E) {
        llong fr, to;
        fr = A[i].first;
        to = A[i].second;
        if (depth[fr] > depth[to]) swap(fr, to);
        flow.addEdge(fr, to, 1);
    }

    FOR(i, G) flow.addEdge(P[i], N, 1);

    cout << flow.maxFlow(0, N) << endl;

    return 0;
}