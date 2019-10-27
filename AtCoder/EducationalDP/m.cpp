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

llong N, K;
vvecllong memo(0, vecllong(0, -1));
vecllong A(0, -1);

llong search(llong child, llong candy) {
    if(candy == 0) return 1;
    if(candy < 0) return 0;
    if(child == -1) return 0;
    if(memo[child][candy] != -1) return memo[child][candy];

    llong ret = 0;
    ret = (search(child - 1, candy) + search(child, candy - 1)) % MOD;
    ret = (ret - search(child - 1, candy - A[child] - 1)) % MOD;
    if(ret < 0) {
        ret += MOD;
    }
    memo[child][candy] = ret % MOD;
    return memo[child][candy];
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> K;

    memo.resize(N + 1, vecllong(K + 1, -1));
    A.resize(N, -1);

    FOR(i, N) {
        cin >> A[i];
    }

    llong ans = search(N - 1, K) % MOD;
    cout << ans << endl;

    return 0;
}