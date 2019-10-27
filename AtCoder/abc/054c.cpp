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
    llong index;
    vector<bool> confilm;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    vvecllong edge(N + 1, vecllong(0));

    FOR(i, M) {
        llong from, to;
        cin >> from >> to;
        edge[from].push_back(to);
        edge[to].push_back(from);
    }

    stack<node> st;
    node start;
    start.index = 1;
    start.confilm = vector<bool>(N + 1, false);
    st.push(start);

    llong ans = 0;

    while(!st.empty()) {
        node now = st.top();
        st.pop();

        if(now.confilm[now.index]) continue;
        now.confilm[now.index] = true;

        FOR(i, edge[now.index].size()) {
            if(!now.confilm[edge[now.index][i]]) {
                node next;
                next.index = edge[now.index][i];
                next.confilm = vector<bool>(N + 1, false);
                copy(now.confilm.begin(), now.confilm.end(), next.confilm.begin());
                st.push(next);
            }
        }

        llong isAll = 1;
        FORS(i, 1, N + 1) {
            if(!now.confilm[i]) {
                isAll = 0;
                break;
            }
        }

        ans += isAll;
    }

    cout << ans << endl;

    return 0;
}