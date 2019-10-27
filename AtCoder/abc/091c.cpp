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

struct coordinate {
    llong x, y;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    vector<coordinate> small(N);
    FOR(i, N) {
        cin >> small[i].x >> small[i].y;
    }

    vector<coordinate> big(N);
    FOR(i, N) {
        cin >> big[i].x >> big[i].y;
    }

    sort(small.begin(), small.end(), [](coordinate a, coordinate b){
        return a.y > b.y;
    });

    sort(big.begin(), big.end(), [](coordinate a, coordinate b){
        return a.x < b.x;
    });

    vector<bool> isMathced(N, false);
    llong ans = 0;

    FOR(i, N) {
        coordinate nowBig = big[i];

        FOR(j, N) {
            coordinate nowSmall = small[j];
            if(isMathced[j]) continue;
            if(nowSmall.x < nowBig.x and nowSmall.y < nowBig.y) {
                ans += 1;
                isMathced[j] = true;
                break;
            }
        }
    }

    cout << ans << endl;


    return 0;
}