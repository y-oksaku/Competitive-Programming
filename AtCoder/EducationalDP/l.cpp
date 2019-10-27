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

llong memo[3000][3000][2] = {0};  // memo[left][right][0:first/1:second] = sumX
bool confilm[3000][3000][2] = {false};

llong deq[3000] = {0};

llong search(llong left, llong right, bool isFirst) {
    if(left == right) {
        if(isFirst) return deq[left];
        else return 0;
    }

    int type = isFirst ? 0 : 1;
    if(confilm[left][right][type] > 0) {
        return memo[left][right][type];
    }

    confilm[left][right][type] = true;
    llong leftTake = search(left + 1, right, !isFirst) + (isFirst ? deq[left] : 0);
    llong rightTake = search(left, right - 1, !isFirst) + (isFirst ? deq[right] : 0);

    if(isFirst) {
        memo[left][right][type] = max(leftTake, rightTake);
        return memo[left][right][type];
    } else {
        memo[left][right][type] = min(leftTake, rightTake);
        return memo[left][right][type];
    }
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    llong sum = 0;
    cin >> N;
    FOR(i, N) {
        cin >> deq[i];
        sum += deq[i];
    }

    llong ans = search(0, N - 1, true);

    cout << (ans - (sum - ans)) << endl;

    return 0;
}