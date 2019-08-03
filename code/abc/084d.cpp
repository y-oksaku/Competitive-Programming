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

    // 前計算
    llong N = 1e5;
    vector<bool> isPrime(N + 1, true);
    isPrime[0] = false;
    isPrime[1] = false;
    llong nowPrime = 2;
    while(nowPrime <= N) {
        if(!isPrime[nowPrime]) {
            nowPrime++;
            continue;
        }
        llong mulPrime = nowPrime * 2;
        while(mulPrime <= N) {
            isPrime[mulPrime] = false;
            mulPrime += nowPrime;
        }
        nowPrime++;
    }

    vecllong sum2017(N + 1, 0);  // 累積和
    FORS(i, 3, N + 1) {
        sum2017[i] = sum2017[i - 1];
        if(isPrime[i] && isPrime[(i + 1) / 2]) {
            sum2017[i]++;
        }
    }

    llong Q;
    cin >> Q;
    FOR(i, Q) {
        llong left, right;
        cin >> left >> right;
        cout << (sum2017[right] - sum2017[left - 1]) << endl;
    }

    return 0;
}