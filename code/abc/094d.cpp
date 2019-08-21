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
    llong N;
    cin >> N;

    vecllong A(N);

    llong maxA = 1;
    llong maxIndex = 0;
    FOR(i, N) {
        cin >> A[i];
        if (maxA < A[i]) {
            maxA = A[i];
            maxIndex = i;
        }
    }

    A.erase(A.begin() + maxIndex);

    long double middle = maxA / 2.0;
    llong middleA = A[0];

    FOR(i, N - 1) {
        if (abs(middle - A[i]) < abs(middle - middleA)) {
            middleA = A[i];
        }
    }

    cout << maxA << " " << middleA << endl;

    return 0;
}