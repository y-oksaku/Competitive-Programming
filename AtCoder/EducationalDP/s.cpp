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

llong ctoi(char c) {
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
    cin.tie(0);
    ios::sync_with_stdio(false);

    string K;
    llong D;
    cin >> K >> D;

    llong maxDigit = K.length();

    vvecllong dpAll(maxDigit + 1, vecllong(D, 0));  // dpAll[digit][mod] = すべて
    vvecllong dpSub(maxDigit + 1, vecllong(D, 0));  // dpSub[digit][mod] = K以下
    dpAll[0][0] = 1;
    dpSub[0][0] = 1;

    FORS(digit, 1, maxDigit + 1) {
        FOR(mod, D) {
            FOR(add, 10) {
                llong d = (mod - add) % D;
                if(d < 0) d += D;
                dpAll[digit][mod] = (dpAll[digit][mod] + dpAll[digit - 1][d]) % MOD;

                if(add < ctoi(K[maxDigit - digit])) {
                    dpSub[digit][mod] = (dpSub[digit][mod] + dpAll[digit - 1][d]) % MOD;
                } else if (add == ctoi(K[maxDigit - digit])) {
                    dpSub[digit][mod] = (dpSub[digit][mod] + dpSub[digit - 1][d]) % MOD;
                }
            }
        }
    }

    llong ans = (dpSub[maxDigit][0] - 1) % MOD;
    if(ans < 0) ans += MOD;
    cout << ans << endl;

    return 0;
}