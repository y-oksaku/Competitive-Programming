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
const llong INF = 1e18;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, W;
    cin >> N >> W;

    llong maxValue = N * 1000;

    vecllong weight(N + 1, 0);
    vecllong value(N + 1, 0);

    FOR(i, N) {
        cin >> weight[i] >> value[i];
    }

    vvecllong dp(N + 1, vecllong(maxValue + 1, INF));  // dp[i][value] = minWeight
    dp[0][0] = 0;

    FOR(i, N) {
        FOR(v, maxValue + 1) {
            if(v - value[i] >= 0 and dp[i][v - value[i]] != INF) {
                dp[i + 1][v] = min(
                    dp[i][v - value[i]] + weight[i],
                    dp[i][v]
                );
            } else {
                dp[i + 1][v] = dp[i][v];
            }
        }
    }

    llong ans = 0;

    FOR(v, maxValue + 1) {
        if(dp[N][v] <= W) {
            ans = v;
        }
    }

    cout << ans << endl;

    return 0;
}