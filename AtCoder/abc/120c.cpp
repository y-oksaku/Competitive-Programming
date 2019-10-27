#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
using namespace std;

int main(void) {
    string str;
    cin >> str;

    int zero = 0;
    int one = 0;

    for(int i=0; i<str.length(); i++) {
        if (str[i] == '0') {
            ++zero;
        }else {
            ++one;
        }
    }

    cout << (min(zero,one) * 2) << endl;

    return 0;
}