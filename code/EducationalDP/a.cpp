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

    llong N;
    cin >> N;
    vecllong cost(N + 2, 0);

    FOR(i, N) {
        cin >> cost[i];
    }

    vecllong dp(N + 2, INF);
    dp[0] = 0;

    FOR(i, N + 1) {
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(cost[i] - cost[i + 1]));
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(cost[i] - cost[i + 2]));
    }

    cout << dp[N - 1] << endl;

    return 0;
}