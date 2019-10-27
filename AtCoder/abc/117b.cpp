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
    int N;

    cin >> N;

    int *L = new int[N];

    for(int i=0; i<N; i++) {
        cin >> L[i];
    }

    sort(L,L+N);

    int maxLength = L[N-1];

    int sumLength = 0;

    for(int i=0;i<N-1;i++) {
        sumLength += L[i];
    }

    if(sumLength > maxLength) {
        cout << "Yes" << endl;
    }else {
        cout << "No" << endl;
    }

    return 0;
}