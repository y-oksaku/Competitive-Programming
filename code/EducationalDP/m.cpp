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

llong dp[101][10100] = {0};  // dp[n][candy] = n人までにcandy個配る場合の数

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, K;
    cin >> N >> K;

    vecllong A(N + 1, 0);
    FOR(i, N) {
        cin >> A[i + 1];
    }

    FOR(i , N + 1) {
        dp[i][0] = 1;
    }

    llong sumCandy = 0;
    FORS(n, 1, N + 1) {
        sumCandy += A[n];
        FORS(candy, 1, sumCandy + 1) {
            dp[n][candy] = (dp[n][candy - 1] + dp[n - 1][candy]) % MOD;
        }
    }

    cout << (dp[N][K] % MOD) << endl;

    return 0;
}