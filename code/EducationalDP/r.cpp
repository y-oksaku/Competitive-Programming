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

llong N;
unsigned long long K;

vvecllong multiple(vvecllong A, vvecllong B) {
    vvecllong C(N, vecllong(N, 0));
    FOR(i, N) {
        FOR(j, N) {
            FOR(k, N) {
                C[i][j] += (A[i][k] * B[k][j]) % MOD;
                C[i][j] %= MOD;
            }
        }
    }
    return C;
};

vvecllong add(vvecllong A, vvecllong B) {
    vvecllong C(N, vecllong(N, 0));
    FOR(i, N) {
        FOR(j, N) {
            C[i][j] = (A[i][j] + B[i][j]) % MOD;
        }
    }
    return C;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> K;

    vvecllong A(N, vecllong(N, 0));

    FOR(i, N) {
        FOR(j, N) {
            cin >> A[i][j];
        }
    }

    vvecllong ans(N, vecllong(N, 0));
    FOR(i, N) {
        ans[i][i] = 1;
    }
    while(K > 0) {
        if((K & 1) != 0) {
            ans = multiple(ans, A);
        }
        A = multiple(A, A);
        K /= 2;
    }

    llong count = 0;
    FOR(i, N) {
        FOR(j, N) {
            count = (count + ans[i][j]) % MOD;
        }
    }

    cout << (count % MOD) << endl;

    return 0;
}