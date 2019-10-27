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
    string S;
    cin >> S;

    vecllong nextNum(N + 1, 0);
    vecllong nowNum(N + 1, 1);
    nowNum[0] = 0;

    FORS(index, 2, N + 1) {
        if(S[index - 2] == '<') {
            llong sum = 0;
            FORS(j, 1, N - index + 2) {
                sum = (sum + nowNum[j]) % MOD;
                nextNum[j] = sum;
            }
        } else {
            llong sum = 0;
            for(llong j = N - index + 1; j >= 1; j--) {
                sum = (sum + nowNum[j + 1]) % MOD;
                nextNum[j] = sum;
            }
        }
        swap(nowNum, nextNum);
    }

    cout << nowNum[1] << endl;

    return 0;
}