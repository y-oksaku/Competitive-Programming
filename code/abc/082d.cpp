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

    string S;
    cin >> S;
    llong x, y;
    cin >> x >> y;

    llong index = 0;
    while(index < S.length() && S[index] == 'F') {  // 最初の移動分を取り除く
        x -= 1;
        index++;
    }

    if(index == S.length()) {
        if(x == 0 and y == 0) cout << "Yes" << endl;
        else cout << "No" << endl;
        return 0;
    }

    bool isHolizon = true;
    while(index < S.length() && S[index] == 'T') {
        isHolizon = !isHolizon;
        index++;
    }

    vecllong moveHolizon(0);
    vecllong moveVertical(0);

    while(index < S.length()) {
        llong count = 0;
        while(index < S.length() && S[index] == 'F') {
            count++;
            index++;
        }
        if(isHolizon) moveHolizon.push_back(count);
        else moveVertical.push_back(count);

        while(index < S.length() && S[index] == 'T') {
            isHolizon = !isHolizon;
            index++;
        }
    }

    // x方向に到達可能か
    vector<vector<bool>> dpx(moveHolizon.size() + 1, vector<bool>(20000, false));
    dpx[0][10000] = true;
    llong i = 1;
    for_each(moveHolizon.begin(), moveHolizon.end(), [&](llong dist){
        FOR(j, 20000) {
            if(dpx[i - 1][j]) {
                dpx[i][j + dist] = true;
                dpx[i][j - dist] = true;
            }
        }
        i++;
    });
    if(!dpx[moveHolizon.size()][x + 10000]) {
        cout << "No" << endl;
        return 0;
    }

    // y方向に到達可能か
    vector<vector<bool>> dpy(moveVertical.size() + 1, vector<bool>(20000, false));
    dpy[0][10000] = true;
    i = 1;
    for_each(moveVertical.begin(), moveVertical.end(), [&](llong dist){
        FOR(j, 20000) {
            if(dpy[i - 1][j]) {
                dpy[i][j + dist] = true;
                dpy[i][j - dist] = true;
            }
        }
        i++;
    });
    if(!dpy[moveVertical.size()][y + 10000]) {
        cout << "No" << endl;
        return 0;
    }

    cout << "Yes" << endl;

    return 0;
}