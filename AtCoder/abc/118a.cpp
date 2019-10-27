#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
typedef unsigned int uint;
typedef long long llong;
using namespace std;

int main(void) {
    cin.tie(0);

    int A , B;
    cin >> A >> B;

    if(B % A == 0) {
        cout << A+B;
    } else {
        cout << B - A;
    }

    return 0;
}