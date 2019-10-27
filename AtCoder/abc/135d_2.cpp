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

vvecllong dp;

int ctoi(char c) {
    switch (c) {
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        default: return 0;
    }
};

int main(void) {
    string S;
    cin >> S;

    llong lenS = S.length();
    dp = vvecllong(S.length() + 1, vecllong(13, 0));
    dp[0][0] = 1;

    llong digitMask = 1;
    FORS(digit, 1, lenS + 1) {
        if(S[lenS - digit] == '?') {
            FOR(d, 13) {
                FOR(k, 10) {
                    llong m = (d - k * digitMask) % 13;
                    if(m < 0) {
                        m += 13;
                    }
                    dp[digit][d] += dp[digit - 1][m] % MOD;
                    dp[digit][d] %= MOD;
                }
            }
        } else {
            llong a = ctoi(S[lenS - digit]);

            FOR(d, 13) {
                llong m = (d - a * digitMask) % 13;
                if(m < 0) {
                    m += 13;
                }
                dp[digit][d] += dp[digit - 1][m] % MOD;
                dp[digit][d] %= MOD;
            }
        }
        digitMask *= 10;
        digitMask %= 13;
    }

    llong ans = (dp[lenS][5]);
    cout << ans << endl;

    return 0;
}