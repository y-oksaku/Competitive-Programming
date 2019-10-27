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

string S;
string ans;
vvecllong dp;

llong alphIndex (char alph) {
    return (llong)alph - (llong)'a';
};

char alphChar(llong alph) {
    return (char)(alph + (llong)'a');
};

void plorong(llong length, llong K, llong prevAlph) {
    if(prevAlph == -1){
        FOR(alph, 26){
            if(K <= dp[length][alph]){
                plorong(length, K, alph);
                return;
            }
            K -= dp[length][alph];
        }
    }
    while(S[length] != alphChar(prevAlph)) length++;
    ans += S[length];
    if(K > 1) plorong(length + 1, K - 1, -1);
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong K;
    cin >> S >> K;
    llong lenS = S.length();

    dp = vvecllong(lenS + 1, vecllong(26, 0));  // dp[index][alph]

    for(llong length = lenS - 1; length >= 0; length--) {
        FOR(alph, 26) {
            if(alphIndex(S[length]) == alph) {
                dp[length][alph] = 1;
                FOR(b,  26) {
                    dp[length][alph] += dp[length + 1][b];
                }
            } else {
                dp[length][alph] = dp[length + 1][alph];
            }
        }
    }

    llong sumDP = 0;
    FOR(alph, 26) {
        sumDP += dp[0][alph];
    }
    if(K > sumDP) {
        cout << "Eel" << endl;
        return 0;
    }

    ans = "";
    plorong(0, K, -1);

    cout << ans << endl;

    return 0;
}
