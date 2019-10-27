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

    llong N, K;
    cin >> N >> K;

    llong R = 2 * K;

    vvecllong blackCount(R, vecllong(R, 0));
    FOR(i, N) {
        llong x, y;
        char c;
        cin >> x >> y >> c;
        if(c == 'W') {
            y += K;
        }
        x %= R;
        y %= R;
        blackCount[x][y]++;
    }

    vvecllong sumBlack(R + 1, vecllong(R + 1, 0));

    FOR(x, R) {
        FOR(y, R) {
            sumBlack[x + 1][y + 1] = sumBlack[x + 1][y] + sumBlack[x][y + 1] - sumBlack[x][y] + blackCount[x][y];
        }
    }

    auto query = [&](llong minX, llong maxX, llong minY, llong maxY){
        if(minX > maxX || minY > maxY){
            return 0LL;
        }
        return sumBlack[maxX][maxY] - sumBlack[minX][maxY] - sumBlack[maxX][minY] + sumBlack[minX][minY];
    };

/*
[0, 2K-1] × [0, 2K - 1]
          x      x+K
    □ □ □ ■ ■ ■ ■ ■ □ □
    □ □ □ ■ ■ ■ ■ ■ □ □
y+K ■ ■ ■ □ □ □ □ □ ■ ■
    ■ ■ ■ □ □ □ □ □ ■ ■
    ■ ■ ■ □ □ □ □ □ ■ ■
    ■ ■ ■ □ □ □ □ □ ■ ■
y   ■ ■ ■ □ □ □ □ □ ■ ■
    □ □ □ ■ ■ ■ ■ ■ □ □
    □ □ □ ■ ■ ■ ■ ■ □ □
    □ □ □ ■ ■ ■ ■ ■ □ □
*/
    llong ans = 0;
    FOR(x, K + 1) {
        FOR(y, K + 1) {
            llong sum = 0;
            sum += query(0, x, 0, y);
            sum += query(0, x, y + K, R);
            sum += query(x + K, R, 0, y);
            sum += query(x, x + K, y, y + K);
            sum += query(x + K, R, y + K, R);

            ans = max({ans, sum, N - sum});
        }
    }

    cout << ans << endl;

    return 0;
}