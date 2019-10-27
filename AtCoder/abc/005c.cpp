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

    llong T;
    cin >> T;

    llong N;
    cin >> N;
    queue<llong> tako;
    FOR(i, N) {
        llong t;
        cin >> t;
        tako.push(t);
    }

    llong M;
    cin >> M;

    FOR(i, M) {
        llong customer;
        cin >> customer;

        while(!tako.empty()) {
            llong lastTako = tako.front();
            if(lastTako <= customer and lastTako >= customer - T) {
                break;
            }
            tako.pop();
        }

        if(tako.empty()) {
            cout << "no" << endl;
            return 0;
        }
        tako.pop();
    }

    cout << "yes" << endl;

    return 0;
}