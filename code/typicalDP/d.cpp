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

struct primes {
    llong two, three, five;
    bool canMake;
};

primes countPrime(llong x) {
    primes count = {0, 0, 0, false};

    while(x % 2 == 0) {
        count.two++;
        x /= 2;
    }
    while(x % 3 == 0) {
        count.three++;
        x /= 3;
    }
    while(x % 5 == 0) {
        count.five++;
        x /= 5;
    }

    if(x > 1) {
        count.canMake = false;
        return count;
    } else {
        count.canMake = true;
        return count;
    }
}

vector<vector<vector<vector<double>>>> memo;
llong N, D;
primes primeD;

double dp(llong time, primes nowPrime) {
    if(nowPrime.two == primeD.two
            and nowPrime.three == primeD.three
            and nowPrime.five == primeD.five) {
        memo[time][nowPrime.two][nowPrime.three][nowPrime.five] = 1.0;
        return 1.0;
    }

    if(time >= N) {
        return 0;
    }

    if(memo[time][nowPrime.two][nowPrime.three][nowPrime.five] >= 0) {
        return memo[time][nowPrime.two][nowPrime.three][nowPrime.five];
    }

    double prob = 0.0;
    prob += dp(time + 1, {nowPrime.two, nowPrime.three, nowPrime.five, true});
    prob += dp(time + 1, {min(nowPrime.two + 1, primeD.two), nowPrime.three, nowPrime.five, true});
    prob += dp(time + 1, {nowPrime.two, min(nowPrime.three + 1, primeD.three), nowPrime.five, true});
    prob += dp(time + 1, {min(nowPrime.two + 2, primeD.two), nowPrime.three, nowPrime.five, true});
    prob += dp(time + 1, {nowPrime.two, nowPrime.three, min(nowPrime.five + 1, primeD.five), true});
    prob += dp(time + 1, {min(nowPrime.two + 1, primeD.two), min(nowPrime.three + 1, primeD.three), nowPrime.five, true});

    prob = prob / 6.0;
    memo[time][nowPrime.two][nowPrime.three][nowPrime.five] = prob;
    return prob;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> N >> D;

    primeD = countPrime(D);
    if(!primeD.canMake) {
        cout << "0" << endl;
        return 0;
    }

    memo = vector<vector<vector<vector<double>>>>(
        N + 1, vector<vector<vector<double>>>(
            primeD.two + 1, vector<vector<double>>(
                primeD.three + 1, vector<double>(
                    primeD.five + 1, -1
                ))));  //memo[time][two][three][five]

    double ans = dp(0, {0, 0, 0, true});
    cout << ans << endl;

    return 0;
}
