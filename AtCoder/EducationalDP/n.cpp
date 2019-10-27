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

llong memo[410][410];  // memo[l][r] = min[l, r)
llong slime[410] = {0};
llong sumSlime[410] = {0};

llong search(llong left, llong right) {
    if(left + 1 == right) {
        return slime[left];
    }
    if(left == right) {
        return 0;
    }
    if(memo[left][right] >= 0) {
        return memo[left][right];
    }

    llong ret = INF;
    FORS(middle, left + 1, right) {
        ret = min(ret, search(left, middle) + search(middle, right));
    }
    ret += sumSlime[right] - sumSlime[left];
    memo[left][right] = ret;
    return ret;
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    FOR(i, N) {
        cin >> slime[i];
        sumSlime[i + 1] = sumSlime[i] + slime[i];
    }

    FOR(l, N + 1) {
        FOR(r, N + 1) {
            memo[l][r] = -1;
        }
    }

    llong ans = search(0, N) - sumSlime[N];
    cout << ans << endl;

    return 0;
}