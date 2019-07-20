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

llong N;
int main(void) {
    cin >> N;

    vecllong A(N);

    for (llong i = 0; i < N; i++) {
        cin >> A[i];
    }

    llong ans = 0;
    llong leftIndex = 0;
    llong rightIndex = 0;
    llong sum = 0;

    while (leftIndex < N) {
        while (rightIndex < N && ((sum ^ A[rightIndex]) == (sum + A[rightIndex]))) {
            sum += A[rightIndex++];
            ans++;
        }
        sum ^= A[leftIndex++];
        ans += rightIndex - leftIndex;
    }

    cout << ans << endl;

    return 0;
}
