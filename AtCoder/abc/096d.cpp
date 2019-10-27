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

    vecllong primes(1, 2);
    llong count = 0;

    for(llong i = 7; i <= 55555; i++) {
        bool isPrime = [] (llong integer, vecllong primes) {
            for(llong i = 0; i < primes.size(); i++) {
                if (integer % primes[i] == 0) {
                    return false;
                }
            }
            return true;
        }(i, primes);

        if (isPrime) {
            primes.push_back(i);
            if (i % 5 == 1) {
                cout << i << " ";
                count++;
                if (count >= N) {
                    break;
                }
            }
        }
    }

    cout << endl;

    return 0;
}