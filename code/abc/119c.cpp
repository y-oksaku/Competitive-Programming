#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <math.h>
#include <iomanip>

typedef unsigned int uint;

using namespace std;

int main(void) {
    cin.tie(0);
    int i,j,k = 0;

    long long N , A , B , C;

    cin >> N >> A >> B >> C;

    long long* L = new long long[N];

    for (int i=0; i<N; i++) {
        cin >> L[i];
    }

    int ans = 3000;

    for(uint i=0;i<pow(4,N); i++) {
        //コスト
        int cost = 0;

        // 結合した竹の長さを計算する
        int length[4] = {0};
        uint k = i;
        for(int j=0; j<N; j++) {
            if(k % 4 != 3 && length[k % 4] > 0) {  //結合する場合
                cost += 10;
            }
            length[k % 4] += L[j];
            k = k / 4;
        }

        // 竹のが選ばれない場合
        bool flag = false;
        for(int j=0; j<3; j++) {
            if(length[j] == 0) {
                flag = true;
                break;
            }
        }
        if(flag){
            continue;
        }

        cost += abs(length[0] - A) + abs(length[1] - B) + abs(length[2] - C);

        if(cost < ans) {
            ans = cost;
        }
    }

    cout << ans << "\n";

    return 0;
}

