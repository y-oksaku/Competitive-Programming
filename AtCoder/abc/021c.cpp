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
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

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

    llong start, end;
    cin >> start >> end;
    start--;
    end--;

    llong M;
    cin >> M;

    vvecllong edges(N, vecllong(0));
    FOR(i, M) {
        llong fr, to;
        cin >> fr >> to;
        fr--;
        to--;
        edges[fr].push_back(to);
        edges[to].push_back(fr);
    }

    vecllong minDist(N, INF);
    vecllong dp(N, 0);
    queue<llong> que;

    minDist[start] = 0;
    dp[start] = 1;
    que.push(start);

    while(!que.empty()) {
        llong now = que.front();
        que.pop();

        for_each(edges[now].begin(), edges[now].end(), [&](llong to) {
            if(minDist[to] == INF) {
                minDist[to] = minDist[now] + 1;
                dp[to] = (dp[to] + dp[now]) % MOD;
                que.push(to);
            } else if(minDist[to] == minDist[now] + 1) {
                dp[to] = (dp[to] + dp[now]) % MOD;
            }
        });
    }

    cout << dp[end] << endl;

    return 0;
}