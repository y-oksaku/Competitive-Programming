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
typedef double ldouble;

typedef vector<llong> vecllong;
typedef vector<vecllong> vvecllong;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

vecllong R;
double prob(llong q, llong p) {
    double exp = (double)(R[q] - R[p]) / 400.0;
    return 1.0 / (1.0 + powl(10.0, exp));
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong K;
    cin >> K;
    llong powK = (1 << K);
    R = vecllong(powK, 0);

    FOR(i, powK) {
        cin >> R[i];
    }

    vector<vector<double>> dp(K + 1, vector<double>(powK, 0));  // dp[k][i] i番目がk回目まで勝つ確率

    FOR(i, powK) {
        dp[0][i] = 1.0;
    }

    FORS(k, 1, K + 1) {
        llong diffBit = (1 << (k - 1));
        llong mask = (powK - 1) ^ (diffBit - 1);
        FOR(i, powK) {
            llong start = (i & mask) ^ diffBit;
            double enemyProb = 0.0;
            FOR(j, diffBit) {
                enemyProb += dp[k - 1][start + j] * prob(start + j, i);
            }
            dp[k][i] = dp[k - 1][i] * enemyProb;
        }
    }

    FOR(i, powK) {
        cout << dp[K][i] << endl;
    }

    return 0;
}