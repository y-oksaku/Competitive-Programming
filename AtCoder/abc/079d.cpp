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
    llong H, W;

    cin >> H >> W;

    llong cost[10][10];

    FOR(i, 10) {
        FOR(j, 10) {
            cin >> cost[i][j];
        }
    }

    llong numberCount[10] = {0};
    llong number;

    FOR(i, H) {
        FOR(j, W) {
            cin >> number;
            if (number != -1) {
                ++numberCount[number];
            }
        }
    }

    auto weight = [] (llong start, llong cost[10][10]) {
        llong minCost[10];
        FOR(i, 10) {
            minCost[i] = INF;
        }

        priority_queue<
            pair<llong, llong>,
            vector<pair<llong, llong>>,
            greater<pair<llong, llong>>> nodeHeap;
        nodeHeap.push(make_pair(0, start));

        while (!nodeHeap.empty()) {
            llong nowCost = nodeHeap.top().first;
            llong node = nodeHeap.top().second;
            nodeHeap.pop();

            if (minCost[node] <= nowCost) {
                continue;
            }

            minCost[node] = nowCost;

            FOR(i, 10) {
                if (i == node) {
                    continue;
                }
                llong newCost = nowCost + cost[node][i];
                nodeHeap.push(make_pair(newCost, i));
            }
        }

        return minCost[1];
    };

    llong ans = 0;

    FOR(i, 10) {
        (i, cost);
        ans += weight(i, cost) * numberCount[i];
    }

    cout << ans << endl;

    return 0;
}