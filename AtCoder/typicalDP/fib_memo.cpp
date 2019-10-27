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

vecllong memo;

llong fib(llong k) {
    if(k == 1 or k == 0) {
        return 1;
    }
    if(memo[k] > 0) {
        return memo[k];
    }
    llong fibk = fib(k - 1) + fib(k - 2);
    memo[k] = fibk;
    return fibk;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;
    memo = vecllong(N + 1, 0);

    llong ans = fib(N);

    cout << ans << endl;

    return 0;
}