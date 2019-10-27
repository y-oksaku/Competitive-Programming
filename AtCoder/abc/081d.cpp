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
typedef long double lldouble;

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

    vecllong A(N);
    llong maxIndex = 0;
    llong minIndex = 0;
    FOR(i, N) {
        cin >> A[i];
        if(A[maxIndex] < A[i]) maxIndex = i;
        if(A[minIndex] > A[i]) minIndex = i;
    }

    if(A[maxIndex] + A[minIndex] >= 0) {
        cout << (N + N - 1) << endl;
        FORS(i, 1, N + 1) {
            if(i == maxIndex + 1) continue;
            printf("%lld %lld\n", maxIndex + 1, i);  // すべて正にする
        }
        printf("%lld %lld\n", maxIndex + 1, maxIndex + 1);
        FORS(i, 1, N) {
            printf("%lld %lld\n", i, i + 1);
        }
    } else {
        cout << (N + N - 1) << endl;
        FORS(i, 1, N + 1) {
            if(i == minIndex + 1) continue;
            printf("%lld %lld\n", minIndex + 1, i);  // すべて負にする
        }
        printf("%lld %lld\n", minIndex + 1, minIndex + 1);
        for(llong i = N; i > 1; i--) {
            printf("%lld %lld\n", i, i - 1);
        }
    }

    return 0;
}