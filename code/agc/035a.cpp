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

int main(void) {
    llong N;
    cin >> N;

    vecllong A(N, 0);

    for (llong i = 0; i<N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    for (llong i=0; i<N; i++){
        for(llong j=i+1; j<N; j++) {
            vecllong numbers(N+2, 0);
            numbers[0] = A[i];
            numbers[1] = A[j];
            for(llong k=2; k<N+2; k++) {
                numbers[k] = numbers[k-1] ^ numbers[k-2];
            }
            if(numbers[0] == numbers[N] && numbers[1] == numbers[N+1]) {
                numbers.erase(numbers.begin() + N);
                numbers.erase(numbers.begin() + N);
                sort(numbers.begin(), numbers.end());
                if(numbers == A) {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "No" << endl;
    return 0;
}