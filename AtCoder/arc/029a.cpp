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
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    llong time[N];

    FOR(i, N) {
        cin >> time[i];
    }

    llong mask = (1 << N) - 1;
    llong ans = INF;
    while (mask >= 0) {
        llong sum1 = 0;
        llong sum2 = 0;
        FOR(i, N) {
            if((mask >> i) & 1 == 1) {
                sum1 += time[i];
            } else {
                sum2 += time[i];
            }
        }
        ans = min(ans, max(sum1, sum2));
        mask--;
    }

    cout << ans << endl;

    return 0;
}