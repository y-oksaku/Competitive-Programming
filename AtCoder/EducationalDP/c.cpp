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

    vvecllong act(N + 1, vecllong(3, 0));

    FOR(i, N) {
        cin >> act[i][0] >> act[i][1] >> act[i][2];
    }

    vvecllong dp(N + 2, vecllong(3, -INF));  // dp[day][choose]
    dp[0][0] = 0;
    dp[0][1] = 0;
    dp[0][2] = 0;

    FOR(day, N + 1) {
        FOR(type, 3) {
            FOR(beforeType, 3) {
                if(type == beforeType) continue;
                dp[day + 1][type] = max(dp[day + 1][type], dp[day][beforeType] + act[day][type]);
            }
        }
    }

    llong ans = max(dp[N][0], dp[N][1]);
    ans = max(ans, dp[N][2]);

    cout << ans << endl;

    return 0;
}