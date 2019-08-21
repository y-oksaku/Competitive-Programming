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

int main(void) {
    llong N, C;

    cin >> N >> C;

    vecllong x(N+2, 0), v(N+2, 0);

    FORS(i, 1, N+1) {
        cin >> x[i] >> v[i];
    }

    llong ans = 0;

    vecllong right(N+2, 0);
    llong sum = 0;
    FORS(i, 1, N+1) {
        sum += v[i];
        right[i] = max(right[i - 1], sum - x[i]);
    }
    vecllong left(N+2, 0);
    sum = 0;
    for(llong i = N; i >= 1; i--) {
        sum += v[i];
        left[i] = max(left[i + 1], sum - 2*(C - x[i]));
    }

    FOR(i, N+1) {
        ans = max(ans, left[i + 1] + right[i]);
    }

    sum = 0;
    FORS(i, 1, N+1) {
        sum += v[i];
        right[i] = max(right[i - 1], sum - 2*x[i]);
    }
    sum = 0;
    for(llong i = N; i >= 1; i--) {
        sum += v[i];
        left[i] = max(left[i + 1], sum - (C - x[i]));
    }

    FOR(i, N+1) {
        ans = max(ans, left[i + 1] + right[i]);
    }

    cout << ans << endl;

    return 0;
}

