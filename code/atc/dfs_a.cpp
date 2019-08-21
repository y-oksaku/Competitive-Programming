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

    llong H, W;
    cin >> H >> W;

    vector<vector<bool>> map(H, vector<bool>(W, false));
    pair<llong, llong> start, goal;

    FOR(i, H) {
        string line;
        cin >> line;
        FOR(j, W){
            if(line[j] == '#') {
                map[i][j] = false;
            } else if(line[j] == '.') {
                map[i][j] = true;
            } else if(line[j] == 'g') {
                map[i][j] = true;
                goal = make_pair(i, j);
            } else {
                map[i][j] = true;
                start = make_pair(i, j);
            }
        }
    }

    stack<pair<llong, llong>> st;
    st.push(start);

    vector<vector<bool>> confilm(H, vector<bool>(W, false));


    while(!st.empty()) {
        pair<llong, llong> now = st.top();
        st.pop();
        if(now == goal) {
            cout << "Yes" << endl;
            return 0;
        }

        if(confilm[now.first][now.second]) continue;

        confilm[now.first][now.second] = true;

        if(now.first > 0) {
            if(map[now.first - 1][now.second]) {
                st.push(make_pair(now.first - 1, now.second));
            }
        }
        if(now.first < H - 1) {
            if(map[now.first + 1][now.second]) {
                st.push(make_pair(now.first + 1, now.second));
            }
        }
        if(now.second > 0) {
            if(map[now.first][now.second - 1]) {
                st.push(make_pair(now.first, now.second - 1));
            }
        }
        if(now.second < W - 1) {
            if(map[now.first][now.second + 1]) {
                st.push(make_pair(now.first, now.second + 1));
            }
        }
    }

    cout << "No" << endl;

    return 0;
}