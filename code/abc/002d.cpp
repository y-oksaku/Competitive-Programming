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
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    vector<vector<bool>> isFriend(N+1, vector<bool>(N+1, false));

    FOR(i, M) {
        llong x, y;
        cin >> x >> y;
        isFriend[x][y] = true;
        isFriend[y][x] = true;
    }

    llong ans = 1;
    FORS(i, 1, N+1) {  // iを含む派閥
        FORS(j, 1, N+1) {
            if(i == j) continue;
            if(isFriend[i][j]) { // jを含む派閥
                vecllong friendList;
                friendList.push_back(i);
                friendList.push_back(j);
                FORS(k, 1, N+1) {
                    if(k == i or k == j) continue;
                    auto canInsert = [](llong k, vecllong friendList, vector<vector<bool>> isFriend){
                        FOR(l, friendList.size()) {
                            if(!isFriend[k][friendList[l]]) {
                                return false;
                            }
                        }
                        return true;
                    };

                    if(canInsert(k, friendList, isFriend)) {
                        friendList.push_back(k);
                    }
                }

                llong count = friendList.size();
                ans = max(ans, count);
            }
        }
    }

    cout << ans << endl;

    return 0;
}