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

llong N;
vvecllong edge(0);
vvecllong memo(0);  // memo[vertex][color]

llong search(llong parent, int parentColor, llong now) {
    if(memo[now][parentColor] != -1) {
        return memo[now][parentColor];
    }

    llong white = 1;
    llong black = 1;
    bool isLeaf = true;
    for_each(edge[now].begin(), edge[now].end(), [&](llong next) {
        if(parent != next) {
            isLeaf = false;
            white = (white * search(now, 0, next)) % MOD;
            if(parentColor == 0) {
                black = (black * search(now, 1, next)) % MOD;
            }
        }
    });

    if(isLeaf) {
        if(parentColor == 0) {
            memo[now][parentColor] = 2;
            return 2;
        } else {
            memo[now][parentColor] = 1;
            return 1;
        }
    }

    llong ret = white % MOD;
    if(parentColor == 0) {
        ret = (ret + black) % MOD;
    }

    memo[now][parentColor] = ret;
    return ret;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;
    edge.resize(N + 1, vecllong(0));
    memo.resize(N + 1, vecllong(2, -1));
    edge[0].push_back(1);

    FOR(i, N - 1) {
        llong x, y;
        cin >> x >> y;
        edge[x].push_back(y);
        edge[y].push_back(x);
    }

    llong ans = search(0, 0, 1) % MOD;
    cout << ans << endl;

    return 0;
}