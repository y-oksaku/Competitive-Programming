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
    vecllong points(N + 1, 0);
    llong sum = 0;
    FORS(i, 1, N + 1) {
        cin >> points[i];
        sum += points[i];
    }

    vector<vector<bool>> dp(N + 1, vector<bool>(sum + 1, false));  // dp[i][j] i番目まででjが作れるかどうか
    FOR(i, N + 1) {
        dp[i][0] = true;
    }

    FORS(i, 1, N + 1) {
        FOR(j, sum + 1) {
            if(dp[i - 1][j]) {
                dp[i][j] = true;
                dp[i][j + points[i]] = true;
            }
        }
    }

    llong ans = 0;
    FOR(i, sum + 1) {
        if(dp[N][i]) ans++;
    }

    cout << ans << endl;

    return 0;
}