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

vecllong memo(0);
llong N;
bool A[22][22] = {false};

llong search(llong state, llong man) {
    if(memo[state] != -1) {
        return memo[state];
    }

    llong ret = 0;
    FOR(woman, N) {
        if((state & (1 << woman)) != 0 and A[man][woman]) {
            ret = (ret + search(state - (1 << woman), man + 1)) % MOD;
        }
    }
    memo[state] = ret % MOD;
    return memo[state];
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;
    FOR(i, N) {
        FOR(j, N) {
            llong in;
            cin >> in;
            A[i][j] = (in == 1);
        }
    }

    memo.resize((1 << N), -1);
    memo[0] = 1;

    llong ans = search((1 << N) - 1, 0) % MOD;

    cout << ans << endl;

    return 0;
}