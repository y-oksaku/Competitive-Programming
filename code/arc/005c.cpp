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

struct node {
    llong h, w, dist;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong H, W;
    cin >> H >> W;

    vvecllong map(H + 2, vecllong(W + 2, INF));
    node start, end;

    FORS(h, 1, H + 1) {
        string line;
        cin >> line;
        FORS(w, 1, W + 1) {
            if(line[w - 1] == '.') {
                map[h][w] = 0;
            } else if(line[w - 1] == 's') {
                start = {h, w, 0};
                map[h][w] = 0;
            } else if(line[w - 1] == 'g') {
                end = {h, w, 0};
                map[h][w] = 0;
            } else {
                map[h][w] = 1;
            }
        }
    }

    queue<node> que;
    que.push(start);
    vvecllong dist(H + 2, vecllong(W + 2, INF));

    while(!que.empty()) {
        node now = que.front();
        que.pop();

        if(dist[now.h][now.w] <= now.dist) continue;
        if(now.dist > 2) continue;

        dist[now.h][now.w] = now.dist;
        if(now.h == end.h and now.w == end.w) {
            if(now.dist <= 2) {
                break;
            }
        }

        if(map[now.h + 1][now.w] != INF) que.push({now.h + 1, now.w, now.dist + map[now.h + 1][now.w]});
        if(map[now.h - 1][now.w] != INF) que.push({now.h - 1, now.w, now.dist + map[now.h - 1][now.w]});
        if(map[now.h][now.w + 1] != INF) que.push({now.h, now.w + 1, now.dist + map[now.h][now.w + 1]});
        if(map[now.h][now.w - 1] != INF) que.push({now.h, now.w - 1, now.dist + map[now.h][now.w - 1]});
    }

    if(dist[end.h][end.w] <= 2) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}