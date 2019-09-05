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

vecllong A;
vvecllong memoTurn1, memoTurn2;

llong search(llong left, llong right, int turn) {
    if(right - left == 1) {
        if(turn == 0) return A[left];
        else return -A[left];
    }
    if(turn == 0) {
        if(memoTurn1[left][right] != INF) return memoTurn1[left][right];
        llong ret = 0;
        ret = max({
            search(left + 1, right, 1) + A[left],
            search(left, right - 1, 1) + A[right - 1]
        });
        memoTurn1[left][right] = ret;
        return ret;
    } else {
        if(memoTurn2[left][right] != INF) return memoTurn2[left][right];
        llong ret = 0;
        ret = min({
            search(left + 1, right, 0) - A[left],
            search(left, right - 1, 0) - A[right - 1]
        });
        memoTurn2[left][right] = ret;
        return ret;
    }
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    A.resize(N, 0);
    FOR(i, N) {
        cin >> A[i];
    }

    memoTurn1.resize(N + 1, vecllong(N + 1, INF));
    memoTurn2.resize(N + 1, vecllong(N + 1, INF));

    llong ans = search(0, N, 0);
    cout << ans << endl;

    return 0;
}