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

    string U, D;
    cin >> U;
    cin >> D;

    llong ans = 0;
    llong now = 0;
    if(U[0] == D[0]) {
        ans = 3;
        now++;
    } else {
        ans = 6;
        now += 2;
    }

    while(now < N) {
        if(U[now] == D[now]) {
            if(U[now - 1] == D[now - 1]) {
                ans *= 2;
                ans %= MOD;
            } else {
                ans *= 1;
            }
            now++;
        } else {
            if(U[now - 1] == D[now - 1]) {
                ans *= 2;
                ans %= MOD;
            } else {
                ans *= 3;
                ans %= MOD;
            }
            now += 2;
        }
    }

    cout << ans << endl;

    return 0;
}