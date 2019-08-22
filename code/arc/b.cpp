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

vecllong score;
vecllong upper;
vvecllong memo;
llong N;

llong search(llong index, llong time) {
    if(memo[index][time] != -1) return memo[index][time];
    if(time == 3) return 1;

    llong ret = 0;
    FORS(i, upper[index], N) {
        ret = (ret + search(i, time + 1)) % MOD;
    }

    memo[index][time] = ret;
    return ret;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;

    score.resize(N, 0);
    upper.resize(N, 0);
    memo.resize(N, vecllong(4, -1));

    FOR(i, N) {
        cin >> score[i];
    }

    sort(score.begin(), score.end());
    FOR(i, N) {
        upper[i] = lower_bound(score.begin(), score.end(), score[i] * 2) - score.begin();
    }

    llong ans = 0;
    FOR(i, N) {
        ans = (ans + search(i, 0)) % MOD;
    }

    cout << ans << endl;

    return 0;
}