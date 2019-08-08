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

    llong leftCount = 0;
    llong rightCount = 0;

    FOR(i, N) {
        if(S[i] == '(') leftCount++;
        else rightCount++;
    }

    llong r = rightCount - leftCount;
    FOR(i, r) {
        S = '(' + S;
    }
    FOR(i, -r) {
        S = S + ')';
    }

    N = S.length();
    leftCount = 0;
    rightCount = 0;
    llong diff = 0;
    FOR(i, N) {
        if(S[i] == '(') leftCount++;
        else rightCount++;
        diff = max(diff, rightCount - leftCount);
    }
    FOR(i, diff) {
        cout << '(';
    }
    cout << S;
    FOR(i, diff) {
        cout << ')';
    }
    cout << endl;

    return 0;
}