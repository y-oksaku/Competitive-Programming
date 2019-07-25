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

struct cordinate {
    llong h, w, dist;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong H, W;
    cin >> H >> W;

    vector<vector<bool>> map(H + 2, vector<bool>(W + 2, false));
    vector<pair<llong, llong>> whiteList;
    vector<pair<llong, llong>> blackList;

    FORS(h, 1, H+1) {
        string line;
        cin >> line;
        FORS(w, 1, W+1) {
            if(line[w - 1] == '.') {
                map[h][w] = true;
            } else {
                blackList.push_back(make_pair(h, w));
                map[h][w] = true;
            }
        }
    }

    llong ans = 0;
    queue<cordinate> que;
    vector<vector<bool>> confilm(H + 2, vector<bool>(W + 2, false));

    FOR(i, blackList.size()) {
        que.push({blackList[i].first, blackList[i].second, 0});
    }

    while(!que.empty()) {
        cordinate now = que.front();
        que.pop();

        if(confilm[now.h][now.w]) {
            continue;
        }

        confilm[now.h][now.w] = true;
        ans = max(ans, now.dist);

        if(map[now.h - 1][now.w]) que.push({now.h - 1, now.w, now.dist + 1});
        if(map[now.h + 1][now.w]) que.push({now.h + 1, now.w, now.dist + 1});
        if(map[now.h][now.w - 1]) que.push({now.h, now.w - 1, now.dist + 1});
        if(map[now.h][now.w + 1]) que.push({now.h, now.w + 1, now.dist + 1});
    }

    cout << ans << endl;

    return 0;
}