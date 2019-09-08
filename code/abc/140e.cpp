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

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;
    vecllong P(N, 0);
    FOR(i, N){
        cin >> P[i];
    }

    vecllong pToI(N + 1, -1);
    FOR(i, N) {
        pToI[P[i]] = i + 1;
    }

    llong ans = 0;
    multiset<llong> S;
    S.insert(0);
    S.insert(0);
    S.insert(N + 1);
    S.insert(N + 1);
    for(llong i = N; i > 0; i--) {
        S.insert(pToI[i]);
        auto mid = S.find(pToI[i]);

        llong L1 = *(prev(mid));
        llong L2 = *(prev(prev(mid)));
        llong R1 = *(next(mid));
        llong R2 = *(next(next(mid)));

        ans += i * (L1 - L2) * (R1 - *mid);
        ans += i * (R2 - R1) * (*mid - L1);
    }

    cout << ans << endl;

    return 0;
}