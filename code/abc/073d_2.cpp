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

struct edge{
    llong to;
    llong cost;
};

vecllong dijkstra(llong start, vector<vector<edge>> edges) {
    vecllong minCost(edges.size(), INF);

    priority_queue<
        pair<llong, llong>,  // cost, index
        vector<pair<llong, llong>>,
        greater<pair<llong, llong>>
    > nodeHeap;

    nodeHeap.push(make_pair(0, start));

    while (!nodeHeap.empty()) {
        llong cost = nodeHeap.top().first;
        llong node = nodeHeap.top().second;
        nodeHeap.pop();

        if (minCost[node] <= cost) {
            continue;
        }

        minCost[node] = cost;

        for_each(edges[node].begin(), edges[node].end(), [&](edge e){
            llong nextNode = e.to;
            llong newCost = cost + e.cost;
            nodeHeap.push(make_pair(newCost, nextNode));
        });
    }

    return minCost;
};

vvecllong minDist;

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M, R;
    cin >> N >> M >> R;

    vecllong visit(R);
    FOR(i, R) {
        llong r;
        cin >> r;
        r--;
        visit[i] = r;
    }

    vector<vector<edge>> edges(N, vector<edge>(0));
    FOR(i, M) {
        llong from, to, dist;
        cin >> from >> to >> dist;
        from--;
        to--;
        edges[from].push_back({to, dist});
        edges[to].push_back({from, dist});
    }

    minDist.resize(N);
    FOR(i, R) {
        minDist[visit[i]] = dijkstra(visit[i], edges);
    }

    llong ans = INF;
    sort(visit.begin(), visit.end());

    do {
        llong cost = 0;
        FOR(i, R - 1) {
            cost += minDist[visit[i]][visit[i + 1]];
        }
        ans = min(ans, cost);
    } while(next_permutation(visit.begin(), visit.end()));

    cout << ans << endl;

    return 0;
}