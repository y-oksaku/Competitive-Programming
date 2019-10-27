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

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    string S, T;
    cin >> S >> T;

    vvecllong dp(S.length() + 1, vecllong(T.length() + 1, 0));  // dp[sIndex][tIndex]

    FOR(s, S.length()) {
        FOR(t, T.length()) {
            if(S[s] == T[t]) {
                chmax(dp[s + 1][t + 1], dp[s][t] + 1);
            }
            chmax(dp[s + 1][t + 1], dp[s + 1][t]);
            chmax(dp[s + 1][t + 1], dp[s][t + 1]);
        }
    }

    string ans = "";
    llong s = S.length();
    llong t = T.length();

    while(s > 0 && t > 0) {
        if(dp[s][t] == dp[s - 1][t]) {
            s--;
        } else if (dp[s][t] == dp[s][t - 1]) {
            t--;
        } else {
            ans = S[s - 1] + ans;
            s--;
            t--;
        }
    }

    cout << ans << endl;

    return 0;
}