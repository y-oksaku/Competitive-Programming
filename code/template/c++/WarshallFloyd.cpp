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
    llong cost;
    llong to;
};

vvecllong WarshallFloyd(vector<vector<edge>> edges) {
    llong N = edges.size();

    // 初期化処理
    vvecllong minDist(N, vecllong(N, INF));
    FOR(i, N) {
        for_each(edges[i].begin(), edges[i].end(), [&](edge e){
            minDist[i][e.to] = e.cost;
        });
    }

    FOR(i, N) {
        FOR(j, N) {
            FOR(k, N) {
                chmin(minDist[i][j], minDist[i][k] + minDist[k][j]);
            }
        }
    }

    return minDist;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    vector<vector<edge>> edges(N);
    edges.resize(N);
    FOR(i, M) {
        llong from, to, cost;
        cin >> from >> to >> cost;
        from--;
        to--;

        edges[from].push_back({cost, to});
        edges[to].push_back({cost, from});
    }

    vvecllong minDist = WarshallFloyd(edges);

    return 0;
}