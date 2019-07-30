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

vector<vector<bool>> stage;
vvecllong dp;

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong H, W;
    cin >> H >> W;

    stage = vector<vector<bool>>(H + 2, vector<bool>(W + 2, false));

    FORS(h, 1, H + 1) {
        FORS(w, 1, W + 1) {
            char c;
            cin >> c;
            if(c == '.') {
                stage[h][w] = true;
            }
        }
    }

    dp = vvecllong(H + 1, vecllong(W + 1, 0));  // dp[h][w] = 場合の数
    dp[1][1] = 1;

    FORS(h, 1, H + 1) {
        FORS(w, 1, W + 1) {
            if(stage[h + 1][w]) dp[h + 1][w] = (dp[h + 1][w] + dp[h][w]) % MOD;
            if(stage[h][w + 1]) dp[h][w + 1] = (dp[h][w + 1] + dp[h][w]) % MOD;
        }
    }

    cout << (dp[H][W] % MOD) << endl;

    return 0;
}