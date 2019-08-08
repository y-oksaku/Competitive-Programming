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

    vecllong V(N);
    FOR(i, N) {
        cin >> V[i];
    }

    vvecllong count(2, vecllong(100100, 0));
    FOR(i, N) {
        count[i % 2][V[i]]++;
    }

    llong maxIndex[2] = {0, 0};
    FOR(i, 100100) {
        if(count[0][maxIndex[0]] < count[0][i]) {
            maxIndex[0] = i;
        }
        if(count[1][maxIndex[1]] < count[1][i]) {
            maxIndex[1] = i;
        }
    }

    llong ans = 0;
    if(maxIndex[0] != maxIndex[1]) {
        ans = N - count[0][maxIndex[0]] - count[1][maxIndex[1]];
    } else {
        llong even = N - count[0][maxIndex[0]];
        llong odd = N - count[1][maxIndex[1]];
        count[0][maxIndex[0]] = 0;
        count[1][maxIndex[1]] = 0;
        maxIndex[0] = 0;
        maxIndex[1] = 1;
        FOR(i, 100100) {
            if(count[0][maxIndex[0]] < count[0][i]) {
                maxIndex[0] = i;
            }
            if(count[1][maxIndex[1]] < count[1][i]) {
                maxIndex[1] = i;
            }
        }
        ans = min(
            even - count[1][maxIndex[1]],
            odd - count[0][maxIndex[0]]
        );
    }

    cout << ans << endl;

    return 0;
}