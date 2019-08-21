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
    llong A, B;
    cin >> A >> B;

    A--;
    B--;

    char ans[100][100];

    FOR(i, 50) {
        FOR(j, 100) {
            ans[i][j] = '#';
            ans[99 - i][j] = '.';
        }
    }

    for(int i = 0; i < 50; i+=2) {
        for(int j = 0; j < 100; j+=2) {
            if (A<=0) {
                i = 1000;
                j = 1000;
                break;
            }
            ans[i][j] = '.';
            A--;
        }
    }

    for(int i = 0; i < 50; i+=2) {
        for(int j = 0; j < 100; j+=2) {
            if (B<=0) {
                i = 1000;
                j = 1000;
                break;
            }
            ans[99 - i][j] = '#';
            B--;
        }
    }

    cout << "100 100" << endl;

    FOR(i, 100){
        FOR(j, 100){
            cout << ans[i][j];
        }
        cout << endl;
    }

    return 0;
}