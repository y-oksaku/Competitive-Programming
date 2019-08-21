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

llong N, Z, W;
vecllong A;

vvecllong memo;  // memo[cardNum][person]

llong search(llong cardNum, llong prevCard, int person) {
    if(cardNum == N - 1) {
        return abs(A[N] - prevCard);
    }
    if(memo[cardNum][person] >= 0) {
        return memo[cardNum][person];
    }

    llong ret;
    if(person == 0) {
        ret = abs(prevCard - A[N]);
        FORS(i, cardNum + 1, N) {
            ret = max(ret, search(i, A[i], 1));
        }
    } else {
        ret = abs(prevCard - A[N]);
        FORS(i, cardNum + 1, N) {
            ret = min(ret, search(i, A[i], 0));
        }
    }
    memo[cardNum][person] = ret;
    return ret;
}


int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> Z >> W;

    memo.resize(N + 1, vecllong(2, -1));
    A.resize(N + 1, 0);

    FORS(i, 1, N + 1) {
        cin >> A[i];
    }

    llong ans = search(0, W, 0);

    cout << ans << endl;

    return 0;
}