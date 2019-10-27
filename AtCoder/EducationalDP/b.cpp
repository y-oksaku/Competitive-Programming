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

    llong N, K;
    cin >> N >> K;

    vecllong H(N + 1);
    FOR(i, N) {
        cin >> H[i];
    }

    vecllong dp(N + 1, INF);
    dp[0] = 0;

    FOR(i, N) {
        FORS(k, 1, K + 1) {
            if(i + k > N) {
                break;
            }
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]));
        }
    }

    cout << dp[N - 1] << endl;

    return 0;
}