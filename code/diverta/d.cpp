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

    vecllong fact;
    llong div = 1;
    while(div * div <= N) {
        if(N % div == 0) {
            fact.push_back(div);
            fact.push_back(N / div);
        }
        div++;
    }

    llong ans = 0;
    for_each(fact.begin(), fact.end(), [&](llong div){
        if(div != N) {
            llong m = N / div - 1;
            llong q = N / m;
            llong r = N % m;
            if(q == r) {
                ans += m;
            }
        }
    });

    cout << ans << endl;

    return 0;
}