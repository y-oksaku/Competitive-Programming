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

llong dp[60][10010][60] = {0};

struct shot {
    llong width, priority;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong W;
    cin >> W;
    llong N, K;
    cin >> N >> K;

    vector<shot> shots(N + 1);
    FORS(i, 1, N + 1) {
        cin >> shots[i].width >> shots[i].priority;
    }

    FORS(i, 0, N) {
        shot nowShot = shots[i + 1];
        FORS(width, 0, W + 1) {
            FORS(count, 0, K + 1) {
                if(width - nowShot.width >= 0) {
                    dp[i + 1][width][count + 1] = max(
                        dp[i + 1][width][count + 1],
                        dp[i][width - nowShot.width][count] + nowShot.priority
                    );
                }
                dp[i + 1][width][count] = max(
                    dp[i + 1][width][count],
                    dp[i][width][count]
                );
            }
        }
    }

    cout << dp[N][W][K] << endl;

    return 0;
}