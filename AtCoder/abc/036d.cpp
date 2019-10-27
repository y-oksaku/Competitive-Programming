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

vvecllong edges;
vvecllong memo;  // memo[now][color]

llong search(llong now, llong parent, llong parentColor){
    if(memo[now][parentColor] != -1) return memo[now][parentColor];

    bool isLeaf = true;
    llong white = 1;
    llong black = 1;

    for_each(edges[now].begin(), edges[now].end(), [&](llong to) {
        if(to != parent){
            isLeaf = false;
            white = (white * search(to, now, 1)) % MOD;
            black = (black * search(to, now, 0)) % MOD;
        }
    });

    if(isLeaf) {
        if(parentColor == 1) {
            memo[now][parentColor] = 2;
            return 2;
        }else{
            memo[now][parentColor] = 1;
            return 1;
        }
    }

    llong ret = white;
    if(parentColor == 1){
        ret = (ret + black) % MOD;
    }
    memo[now][parentColor] = ret;
    return ret;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    edges.resize(N + 1, vecllong(0));
    edges[0].push_back(1);
    FOR(i, N - 1){
        llong fr, to;
        cin >> fr >> to;
        edges[fr].push_back(to);
        edges[to].push_back(fr);
    }

    memo.resize(N + 1, vecllong(2, -1));
    llong ans = search(0, 0, 0);

    cout << ans << endl;

    return 0;
}