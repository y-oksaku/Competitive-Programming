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

template<class T> inline bool chmin(T& to, T compare) {
    if (to > compare) {
        to = compare;
        return true;
    }
    return false;
};

template<class T> inline bool chmax(T& to, T compare) {
    if (to < compare) {
        to = compare;
        return true;
    }
    return false;
};

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, W;
    cin >> N >> W;

    vecllong weight(N);
    vecllong value(N);

    FOR(i, N) {
        cin >> weight[i] >> value[i];
    }

    vvecllong dp(N + 2, vecllong(W + 1, 0));

    FOR(i, N + 1) {
        FORS(w, 1, W + 1) {
            if(w - weight[i] >= 0) {
                dp[i + 1][w] = max({dp[i + 1][w], dp[i][w], dp[i][w - weight[i]] + value[i]});
            } else {
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w]);
            }
        }
    }

    cout << dp[N][W] << endl;

    return 0;
}