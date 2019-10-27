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
    long long N;

    scanf("%lld",&N);

    double ans = 0;


    for(int i = 0; i<N; i++) {
        double x;
        char u[255];
        scanf("%lf %s",&x,u);

        if(u[0] == 'J') {
            ans += x;
        } else {
            ans += x * 380000.0;
        }
    }

    printf("%lf\n",ans);

    return 0;
}