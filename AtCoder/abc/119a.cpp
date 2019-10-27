#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <math.h>
#include <iomanip>

using namespace std;

int main(void) {
    string str;
    cin >> str;

    int year = stoi(str.substr(0,4));
    int month = stoi(str.substr(5,2));
    int day = stoi(str.substr(8,2));

    if(year > 2019) {
        cout << "TBD" << endl;
    }else if(year == 2019) {
        if(month >= 5) {
            cout << "TBD" << endl;
        } else {
            cout << "Heisei" << endl;
        }
    } else {
        cout << "Heisei" << endl;
    }

    return 0;
}