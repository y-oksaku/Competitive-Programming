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

    vecllong P(N, 0);
    FOR(i, N) {
        llong p;
        cin >> p;
        p--;
        P[i] = p;
    }

    llong count = 0;

    if(P[0] == 0) {
        count++;
        swap(P[0], P[1]);
    }

    llong now = 1;
    while(now < N) {
        if(P[now] == now) {
            count++;
            if(now < N - 1 && P[now + 1] == now + 1) {
                swap(P[now], P[now + 1]);
                now += 2;
                continue;
            }
            swap(P[now], P[now - 1]);
            now++;
            continue;
        }
        now++;
    }

    cout << count << endl;

    return 0;
}