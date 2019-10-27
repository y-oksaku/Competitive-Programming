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

struct box {
    llong h, w;

    bool operator < (const box &another) {
        if (h == another.h) {
            return w > another.w;
        } else {
            return h < another.h;
        }
    }
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N;
    cin >> N;

    vector<box> boxes(N);

    FOR(i, N) {
        llong h, w;
        cin >> h >> w;
        boxes[i] = {h, w};
    }

    sort(boxes.begin(), boxes.end());

    vecllong dp(1, boxes[0].w);

    FORS(i, 1, N) {  // 最長狭義増加部分列
        if(boxes[i].w > dp.back()) {
            dp.push_back(boxes[i].w);
        } else {
            auto insert = lower_bound(dp.begin(), dp.end(), boxes[i].w);
            *insert = boxes[i].w;
        }
    }

    cout << dp.size() << endl;

    return 0;
}