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
    llong cost;
};

int main(void) {
    llong N, M;
    cin >> N >> M;

    vector<edge> graph[N];

    FOR(i, M) {
        llong l,r,d;
        cin >> l >> r >> d;
        l--;
        r--;
        graph[l].push_back({r, d});
        graph[r].push_back({l, -d});
    }

    llong dist[N];
    FOR(i, N) {
        dist[i] = INF;
    }

    queue<llong> que;
    FOR(vertex, N) {
        if(graph[vertex].size() == 0 or dist[vertex] != INF) {
            continue;
        }
        que.push(vertex);
        dist[vertex] = 0;
        while (!que.empty()) {
            llong now = que.front();
            que.pop();

            FOR(i, graph[now].size()) {
                edge e = graph[now][i];
                if (dist[e.to] != INF) {
                    if(dist[now] + e.cost != dist[e.to]) {
                        cout << "No" << endl;
                        return 0;
                    }
                } else {
                    dist[e.to] = dist[now] + e.cost;
                    que.push(e.to);
                }
            }
        }
    }

    cout << "Yes" << endl;

    return 0;
}