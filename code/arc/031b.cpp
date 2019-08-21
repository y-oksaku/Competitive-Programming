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

    llong N = 10;
    vector<vector<bool>> map(N, vector<bool>(N, false));

    FOR(i, N) {
        string line;
        cin >> line;
        FOR(j, N) {
            if(line[j] == 'x') {
                map[i][j] = false;
            } else {
                map[i][j] = true;
            }
        }
    }

    FOR(i, N) {
        FOR(j, N) {
            if(map[i][j] == true) continue;

            stack<pair<llong, llong>> st;
            st.push(make_pair(i, j));
            vector<vector<bool>> confilm(N, vector<bool>(N, false));

            while(!st.empty()) {
                pair<llong, llong> now = st.top();
                st.pop();

                if(confilm[now.first][now.second]) continue;
                confilm[now.first][now.second] = true;

                if(now.first > 0) {
                    if(map[now.first - 1][now.second]) {
                        st.push(make_pair(now.first - 1, now.second));
                    }
                }
                if(now.first < N - 1) {
                    if(map[now.first + 1][now.second]) {
                        st.push(make_pair(now.first + 1, now.second));
                    }
                }
                if(now.second > 0) {
                    if(map[now.first][now.second - 1]) {
                        st.push(make_pair(now.first, now.second - 1));
                    }
                }
                if(now.second < N - 1) {
                    if(map[now.first][now.second + 1]) {
                        st.push(make_pair(now.first, now.second + 1));
                    }
                }
            }

            confilm[i][j] = false;
            if(confilm == map) {
                cout << "YES" << endl;
                return 0;
            }
        }
    }

    cout << "NO" << endl;

    return 0;
}