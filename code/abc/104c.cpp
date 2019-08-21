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

struct score {
    llong unit;
    llong complete;
    llong number;
    llong total;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong D, G;
    cin >> D >> G;

    vector<score> points;
    FORS(i, 1, D + 1) {
        llong number, comp;
        cin >> number >> comp;
        points.push_back({i * 100, comp, number, (i * 100 * number + comp)});
    }

    llong mask = (1 << D) - 1;
    llong ans = INF;
    while (mask >= 0) {
        llong total = 0;
        llong count = 0;
        FOR(i, D) {
            if((mask >> i) & 1 == 1) {
                total += points[i].total;
                count += points[i].number;
            }
        }
        if(total < G) {
            for(llong i = D - 1; i >= 0; i--) {
                if(!((mask >> i) & 1 == 1)) {
                    llong ness = (G - total + points[i].unit - 1) / points[i].unit;
                    if(ness > points[i].number) {
                        continue;
                    }
                    count += ness;
                    total += ness * points[i].unit;
                    break;
                }
            }
        }

        if(total >= G) {
            ans = min(ans, count);
        }

        mask--;
    }

    cout << ans << endl;

    return 0;
}