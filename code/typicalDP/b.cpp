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

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

llong A, B;
vecllong a, b;
vector<vector<vector<llong>>> memo;

llong dp(llong aIndex, llong bIndex, bool turn) {
    if(aIndex >= A and bIndex >= B) {
        return 0;
    }

    if(memo[aIndex][bIndex][(turn ? 1 : 0)] >= 0) {
        return memo[aIndex][bIndex][(turn ? 1 : 0)];
    }

    if(aIndex >= A and bIndex <= B - 1) {
        memo[aIndex][bIndex][(turn ? 1 : 0)] = dp(aIndex, bIndex + 1, !turn) + (turn ? b[bIndex] : 0);
        return memo[aIndex][bIndex][(turn ? 1 : 0)];
    }

    if(aIndex <= A - 1 and bIndex >= B) {
        memo[aIndex][bIndex][(turn ? 1 : 0)] = dp(aIndex + 1, bIndex, !turn) + (turn ? a[aIndex] : 0);
        return memo[aIndex][bIndex][(turn ? 1 : 0)];
    }

    llong takeA = dp(aIndex + 1, bIndex, !turn) + (turn ? a[aIndex] : 0);
    llong takeB = dp(aIndex, bIndex + 1, !turn) + (turn ? b[bIndex] : 0);

    if(turn) {
        memo[aIndex][bIndex][(turn ? 1 : 0)] = max(takeA, takeB);
        return max(takeA, takeB);
    } else {
        memo[aIndex][bIndex][(turn ? 1 : 0)] = min(takeA, takeB);
        return min(takeA, takeB);
    }
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> A >> B;
    a = vecllong(A);
    b = vecllong(B);

    memo = vector<vector<vector<llong>>>(A + 1, vector<vector<llong>>(B + 1, vector<llong>(2, -1)));

    FOR(i, A) {
        cin >> a[i];
    }
    FOR(i, B) {
        cin >> b[i];
    }

    llong ans = dp(0, 0, true);

    cout << ans << endl;

    return 0;
}