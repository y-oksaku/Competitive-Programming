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
using Graph = vector<vector<long long>>;
using costGraph = vector<vector<pair<long long, long long>>>;

struct Edge {
    long long from;
    long long to;
    long long cost;
};

template<typename T>
using asc = less<T>();
template<typename T>
using desc = greater<T>();

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M, P;
    cin >> N >> M >> P;

    vector<Edge> edges;
    Graph G(N);
    Graph GR(N);

    FOR(i, M) {
        llong fr, to, cost;
        cin >> fr >> to >> cost;
        fr--; to--; cost -= P;
        edges.push_back({fr, to, -cost});
        G[fr].push_back(to);
        GR[to].push_back(fr);
    }

    vector<bool> canGo(N, false);
    vector<bool> canBack(N, false);

    stack<llong> st;
    st.push(0);
    while(!st.empty()) {
        llong now = st.top(); st.pop();
        for(llong to : G[now]) {
            if(!canGo[to]) {
                st.push(to);
                canGo[to] = true;
            }
        }
    }

    st.push(N - 1);
    while(!st.empty()) {
        llong now = st.top(); st.pop();
        for(llong to : GR[now]) {
            if(!canBack[to]) {
                st.push(to);
                canBack[to] = true;
            }
        }
    }

    llongV minDist(N, INF);
    minDist[0] = 0;

    FOR(i, N + 1) {
        for(Edge edge : edges) {
            if(minDist[edge.to] > minDist[edge.from] + edge.cost) {
                if(i == N) {
                    if(canGo[edge.to] && canBack[edge.to]) {
                        cout << "-1" << endl;
                        return 0;
                    }
                    continue;
                }
                minDist[edge.to] = minDist[edge.from] + edge.cost;
            }
        }
    }

    llong ans = -minDist[N - 1];
    if(ans < 0) ans = 0;
    cout << ans << endl;

    return 0;
}