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
typedef double ldouble;

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

    vector<double> prob(N);
    FOR(i, N) {
        cin >> prob[i];
    }

    vector<vector<double>> dp(N + 1, vector<double>(N + 1, 0));  // dp[i][count]
    dp[0][0] = 1;

    FOR(i, N) {
        FOR(count, N + 1) {
            if(count == 0) {
                dp[i + 1][count] = dp[i][count] * (1 - prob[i]);
            } else {
                dp[i + 1][count] = dp[i][count] * (1 - prob[i]) + dp[i][count - 1] * prob[i];
            }
        }
    }

    double ans = 0;
    FORS(count, N / 2 + 1, N + 1) {
        ans += dp[N][count];
    }

    printf("%.16f\n", ans);

    return 0;
}