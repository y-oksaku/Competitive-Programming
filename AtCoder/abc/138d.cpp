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

vvecllong edge;
vecllong ans;

void calc(llong now, llong parent){
    if(parent != -1){
        ans[now] += ans[parent];
    }
    for_each(edge[now].begin(), edge[now].end(), [&](llong to) {
        if(to != parent){
            calc(to, now);
        }
    });
    return;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, Q;
    cin >> N >> Q;

    edge.resize(N, vecllong(0));
    FOR(i, N - 1){
        llong a, b;
        cin >> a >> b;
        a--;
        b--;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    ans.resize(N, 0);
    FOR(i, Q) {
        llong p, x;
        cin >> p >> x;
        p--;
        ans[p] += x;
    }

    calc(0, -1);
    FOR(i, N) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}