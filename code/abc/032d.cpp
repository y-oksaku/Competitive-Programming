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

struct item {
    llong v, w;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, W;
    cin >> N >> W;

    llong vMax = 0;
    llong wMax = 0;

    vector<item> items(N);
    FOR(i, N){
        llong v, w;
        cin >> v >> w;
        items[i] = {v, w};
        chmax(vMax, v);
        chmax(wMax, w);
    }

    if(N <= 30) {
        llong M = N / 2;
        vector<tuple<llong, llong>> left;
        FOR(mask, (1 << M)) {
            llong sumV = 0;
            llong sumW = 0;
            FOR(i, M) {
                if((mask & (1 << i)) != 0) {
                    sumV += items[i].v;
                    sumW += items[i].w;
                }
            }
            left.push_back(tuple<llong, llong>(sumW, sumV));
        }

        vector<tuple<llong, llong>> right;
        FOR(mask, (1 << (N - M))) {
            llong sumV = 0;
            llong sumW = 0;
            FORS(i, M, N) {
                if((mask & (1 << (i - M))) != 0) {
                    sumV += items[i].v;
                    sumW += items[i].w;
                }
            }
            right.push_back(tuple<llong, llong>(sumW, sumV));
        }

        sort(right.begin(), right.end());
        vecllong bestV(1, 0);

        for_each(right.begin(), right.end(), [&](auto a) {
            llong w, v;
            tie(w, v) = a;
            bestV.push_back(max(v, bestV.back()));
        });

        llong ans = 0;
        for_each(left.begin(), left.end(), [&](auto a) {
            llong w, v;
            tie(w, v) = a;
            if(w <= W) {
                llong i = upper_bound(right.begin(), right.end(), tuple<llong, llong>(W - w, INF)) - right.begin();
                chmax(ans, v + bestV[i]);
            }
        });
        cout << ans << endl;
    } else if (wMax <= 1000) {
        vvecllong dp(N + 1, vecllong(W + 1, -INF));
        dp[0][0] = 0;
        FOR(i, N) {
            FOR(weight, W + 1) {
                chmax(dp[i + 1][weight], dp[i][weight]);
                if(weight > 0) {
                    chmax(dp[i + 1][weight], dp[i + 1][weight - 1]);
                }
                if(weight + items[i].w <= W) {
                    chmax(dp[i + 1][weight + items[i].w], dp[i][weight] + items[i].v);
                }
            }
        }
        cout << dp[N][W] << endl;
    } else if (vMax <= 1000) {
        vvecllong dp(N + 1, vecllong(vMax * N + 1, INF));
        dp[0][0] = 0;
        FOR(i, N) {
            FOR(value, vMax * N + 1) {
                chmin(dp[i + 1][value], dp[i][value]);
                if(value + items[i].v <= vMax * N) {
                    chmin(dp[i + 1][value + items[i].v], dp[i][value] + items[i].w);
                }
            }
        }
        llong ans = 0;
        for(llong value = vMax * N; value >= 0; value--) {
            if(dp[N][value] <= W) {
                ans = value;
                break;
            }
        }
        cout << ans << endl;
    }

    return 0;
}