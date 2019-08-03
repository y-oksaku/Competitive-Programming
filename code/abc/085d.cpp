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
#define asc less<llong>()
#define desc greater<llong>()

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, HP;
    cin >> N >> HP;

    llong maxA = 0;

    vecllong b(N);
    FOR(i, N) {
        llong a;
        cin >> a >> b[i];
        maxA = max(maxA, a);
    }

    sort(b.begin(), b.end(), desc);

    auto ceil = [](llong a, llong b) {
        return (a + b - 1) / b;
    };

    llong ans = ceil(HP, maxA);
    FOR(i, N) {
        HP -= b[i];
        if(HP < 0) {
            ans = min(ans, i + 1);
            break;
        }
        llong a = (i + 1) + ceil(HP, maxA);
        ans = min(ans, a);
    }

    cout << ans << endl;

    return 0;
}