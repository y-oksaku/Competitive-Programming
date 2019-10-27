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

using Int = unsigned int;
using llong = long long;
using Llong = unsigned long long;
using ldouble = long double;
using intV = vector<int>;
using llongV = vector<long long>;
using llongVV = vector<vector<long long>>;

template<typename T=llong>
using Graph = vector<vector<T>>;

template<typename T=llong>
struct Edge {
    T from;
    T to;
    T cost;
};

template<typename T=llong>
using asc = less<T>();
template<typename T=llong>
using desc = greater<T>();

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

    llongVV A(N, llongV(N, 0));
    FOR(i, N) {
        FOR(j, N) {
            cin >> A[i][j];
        }
    }

    llongV grpScore(1 << N, 0);
    FOR(mask, 1 << N) {
        llong score = 0;
        FOR(i, N) {
            FORS(j, i + 1, N) {
                if(((mask & (1 << i)) > 0) && ((mask & (1 << j)) > 0)) {
                    score += A[i][j];
                }
            }
        }
        grpScore[mask] = score;
    }

    llongV dp(1 << N, 0);

    FOR(mask, 1 << N) {
        llong canUse = mask ^ ((1 << N) - 1);
        for(llong newGrp = canUse; newGrp > 0; newGrp = ((newGrp - 1) & canUse)) {
            if(newGrp <= mask) break;
            chmax(dp[mask | newGrp], dp[mask] + grpScore[newGrp]);
        }
    }

    cout << dp[(1 << N) - 1] << endl;

    return 0;
}