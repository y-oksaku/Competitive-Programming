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
    llong H, W, D;
    cin >> H >> W >> D;

    vector<pair<llong, llong>> cordinate(H * W + 1);

    FOR(i, H) {
        FOR(j, W) {
            llong p;
            cin >> p;
            cordinate[p] = make_pair(i + 1, j + 1);
        }
    }

    vvecllong sumCost(D, vecllong(0));

    for (llong startPoint = 1; startPoint <= D; startPoint++) {
        llong type = startPoint % D;
        sumCost[type].push_back(0);

        llong j = 1;
        pair<llong, llong> prevCordinate = cordinate[startPoint];
        pair<llong, llong> nextCordinate;
        llong cost;
        while (startPoint + j * D <= H * W) {
            nextCordinate = cordinate[startPoint + j * D];
            cost = abs(nextCordinate.first - prevCordinate.first) + abs(nextCordinate.second - prevCordinate.second);
            sumCost[type].push_back(sumCost[type][j - 1] + cost);
            prevCordinate = nextCordinate;
            j++;
        }
    }

    llong Q;
    cin >> Q;

    FOR(q, Q) {
        llong start, end;
        cin >> start >> end;

        llong startPoint = start % D;
        if (startPoint == 0) {
            startPoint = D;
        }

        llong startTime = (start - startPoint) / D;
        llong endTime = (end - startPoint) / D;

        llong ans = sumCost[startPoint % D][endTime] - sumCost[startPoint % D][startTime];

        cout << ans << endl;
    }

    return 0;
}