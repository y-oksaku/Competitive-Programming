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
#define asc less<llong>()
#define desc greater<llong>()

struct edge {
    llong from;
    llong to;
    llong cost;
};

llong ctoi(char c) {
    switch (c) {
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        default: return 0;
    }
};

bool search(llong start, llong end, vector<vector<edge>> map){
    vector<bool> confilm(map.size() + 10, false);

    stack<llong> st;
    st.push(start);

    while(!st.empty()) {
        llong now = st.top();
        st.pop();

        if(confilm[now]) continue;
        confilm[now] = true;
        if(now == end) return true;

        for_each(map[now].begin(), map[now].end(), [&](edge e) {
            st.push(e.to);
        });
    }

    return false;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M, P;
    cin >> N >> M >> P;

    vector<edge> edges;
    vecllong minDist(N + 10, INF);

    vector<vector<edge>> map(N + 10, vector<edge>(0));

    minDist[0] = 0;

    FOR(i, M) {
        llong from, to, cost;
        cin >> from >> to >> cost;
        from--;
        to--;
        cost -= P;
        edges.push_back({from, to, -cost});
        map[from].push_back({from, to, -cost});
    }

    FOR(i, N) {
        FOR(j, edges.size()) {
            edge e = edges[j];
            if(minDist[e.to] > minDist[e.from] + e.cost) {
                minDist[e.to] = minDist[e.from] + e.cost;
                if(i == N - 1) {
                    if(search(e.from, N - 1, map) and search(0, e.from, map)) {
                        cout << "-1" << endl;
                        return 0;
                    }
                }
            }
        }
    }

    cout << max(-minDist[N - 1], 0LL) << endl;

    return 0;
}