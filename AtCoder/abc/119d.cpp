#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>
typedef unsigned int uint;
using namespace std;

bool comp(const long long &x,const long long &y) {
    return abs(x) < abs(y);
}

int main(void) {
    cin.tie(0); // cin高速化
    long long A , B , Q;

    cin >> A >> B >> Q;

    long long *s = new long long[A];
    long long *t = new long long[B];
    long long *x = new long long[Q];

    for(long long i=0; i<A; i++){
        cin >> s[i];
    }
    for(long long i=0; i<B; i++){
        cin >> t[i];
    }

    for(long long i=0; i<Q; i++){
        cin >> x[i];
    }

    for(long long i=0; i<Q; i++){
        long long *cs = new long long[A]; // xを中心とした距離
        for(long long j=0; j<A; j++){
            cs[j] = s[j] - x[i];
        }
        long long *ct = new long long[B]; // xを中心とした距離
        for(long long j=0; j<B; j++){
            ct[j] = t[j] - x[i];
        }
        // 距離順でソート
        sort(cs,cs+A,comp);
        sort(ct,ct+B,comp);

        long long ans = 0;
        long long dists = pow(10,11);
        long long distt = pow(10,11);
        long long distps = pow(10,11);
        long long distms = pow(10,11);
        long long distpt = pow(10,11);
        long long distmt = pow(10,11);

        // マイナス方向のみ
        for(long long j=0; j<A; j++){
            if(cs[j] <= 0) {
                dists = abs(cs[j]);
                distms = dists;
                break;
            }
        }
        for(long long j=0; j<B; j++){
            if(ct[j] <= 0) {
                distt = abs(ct[j]);
                distmt = distt;
                break;
            }
        }
        ans = max(dists,distt);

        //プラス方向のみ
        dists = pow(10,11);
        distt = pow(10,11);
        for(long long j=0; j<A; j++){
            if(cs[j] >= 0) {
                dists = abs(cs[j]);
                distps = dists;
                break;
            }
        }
        for(long long j=0; j<B; j++){
            if(ct[j] >= 0) {
                distt = abs(ct[j]);
                distpt = distt;
                break;
            }
        }
        ans = min(ans,max(dists,distt));

        //プラスs,マイナスt
        ans = min(ans,abs(distps) + abs(distmt) + min(abs(distps),abs(distmt)));

        //プラスt,マイナスs
        ans = min(ans,abs(distpt) + abs(distms) + min(abs(distpt),abs(distms)));

        cout << ans << "\n";
    }

    return 0;
}

