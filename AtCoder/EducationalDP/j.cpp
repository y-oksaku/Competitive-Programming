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
#include <cstring>

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

double memo[310][310][310];  // dp[one][two][three]
double N;

double search(llong one, llong two, llong three) {
    if(memo[one][two][three] >= 0) {
        return memo[one][two][three];
    }
    if(one == 0 and two == 0 and three == 0) {
        return 0.0;
    }

    double ret = 0.0;
    if(one > 0) ret += search(one - 1, two, three) * one;
    if(two > 0) ret += search(one + 1, two - 1, three) * two;
    if(three > 0) ret += search(one, two + 1, three - 1) * three;
    ret += N;
    ret *= 1.0 / (one + two + three);

    memo[one][two][three] = ret;
    return ret;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;

    llong one = 0;
    llong two = 0;
    llong three = 0;

    FOR(i, N) {
        llong a;
        cin >> a;
        if(a == 1) {
            one++;
        } else if (a == 2) {
            two++;
        } else if (a == 3) {
            three++;
        }
    }

    memset(memo, -1, sizeof(memo));

    double ans = search(one, two, three);

    printf("%.16f\n", ans);

    return 0;
}