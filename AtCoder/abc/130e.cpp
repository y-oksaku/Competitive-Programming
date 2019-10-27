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

#define rep(i, n) for (long long i = 0; i < (long long)n; i++)
#define repf(i, a, b) for (long long i = (long long)a; i < (long long)b; i++)
#define repr(i, a, b) for (long long i = (long long)a; i > (long long)b; i--)

typedef unsigned int uint;
typedef long long llong;
typedef unsigned long long ullong;
typedef long double ldouble;

typedef vector<llong> vecllong;
typedef vector<vecllong> vvecllong;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

int main(void) {
    llong n,m;

    cin >> n >> m;
    vecllong s(n);
    vecllong t(m);

    rep(i,n){
        cin >> s[i];
    }
    rep(i,m){
        cin >> t[i];
    }

    vvecllong ans(n+1, vecllong(m+1,0));

    rep(i,m+1){
        ans[0][i] = 1;
    }
    rep(i,n+1){
        ans[i][0] = 1;
    }

    for(llong i=1; i<=n; i++){
        for(llong j=1; j<=m; j++){
            if(s[i-1] == t[j-1]){
                ans[i][j] = ans[i-1][j] + ans[i][j-1];
            }else{
                ans[i][j] = ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1] + MOD;
            }
            ans[i][j] %= MOD;
        }
    }

    cout << (ans[n][m] % MOD) << endl;

    return 0;
}