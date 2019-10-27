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

using Int = unsigned int;
using llong = long long;
using Llong = unsigned long long;
using ldouble = long double;
using intV = vector<int>;
using llongV = vector<long long>;
using llongVV = vector<vector<long long>>;

using Graph = vector<vector<llong>>;

struct Edge {
    llong from;
    llong to;
    llong cost;
};

template<typename T=llong>
using asc = less<T>();
template<typename T=llong>
using desc = greater<T>();

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M, L;
    cin >> N >> M >> L;

    llongVV dist(N, llongV(N, INF));

    FOR(i, N) {
        dist[i][i] = 0;
    }

    FOR(i, M) {
        llong fr, to, cost;
        cin >> fr >> to >> cost;
        fr--;
        to--;
        dist[fr][to] = cost;
        dist[to][fr] = cost;
    }

    FOR(k, N) {
        FOR(i, N) {
            FOR(j, N) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    llongVV fuel(N, llongV(N, INF));
    FOR(i, N) {
        fuel[i][i] = 0;
    }
    FOR(i, N) {
        FOR(j, N) {
            if(dist[i][j] <= L) fuel[i][j] = 1;
        }
    }
    FOR(k, N) {
        FOR(i, N) {
            FOR(j, N) {
                fuel[i][j] = min(fuel[i][j], fuel[i][k] + fuel[k][j]);
            }
        }
    }

    llong Q;
    cin >> Q;
    llongV ans;
    FOR(i, Q) {
        llong s, t;
        cin >> s >> t;
        s--;
        t--;
        if(fuel[s][t] == INF) ans.push_back(-1);
        else ans.push_back(fuel[s][t] - 1);
    }

    FOR(i, Q) cout << ans[i] << endl;

    return 0;
}