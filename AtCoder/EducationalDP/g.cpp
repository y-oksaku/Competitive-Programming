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
vecllong memo;

llong search(llong now) {
    if(edge[now].size() == 0) {
        return 0;
    }
    if(memo[now] >= 0) {
        return memo[now];
    }

    llong ret = 0;
    for_each(edge[now].begin(), edge[now].end(), [&ret](llong to) {
        if(memo[to] >= 0) {
            chmax(ret, memo[to]);
        } else {
            chmax(ret, search(to));
        }
    });

    memo[now] = ret + 1;

    return ret + 1;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    edge = vvecllong(N + 1, vecllong(0));  // edge[from][to]
    memo = vecllong(N + 1, -1);

    FOR(i, M) {
        llong from, to;
        cin >> from >> to;
        edge[from].push_back(to);
    }

    llong ans = 0;
    FORS(i, 1, N + 1) {
        if(memo[i] >= 0) {
            chmax(ans, memo[i]);
        } else {
            chmax(ans, search(i));
        }
    }

    cout << ans << endl;

    return 0;
}