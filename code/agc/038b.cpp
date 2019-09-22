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
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

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

class SegmentTree {
    public :
        vecllong __data;
        llong __size;

        SegmentTree (llong size) {
            this->init(size);
        };

        void init (llong size) {
            // 完全二分木にする
            llong binSize = 0;
            while((1 << binSize) < size) {
                binSize++;
            }
            this->__size = (1 << binSize);

            this->__data.resize(this->__size * 2);
            for(llong i = 0; i < this->__size * 2; i++) {
                this->__data[i] = INF;
            }
        };

        /* メソッド */
        void update(llong index, llong value) {
            index += this->__size - 1;
            this->__data[index] = value;
            while(index > 0) {
                index = (index - 1) / 2;
                this->__data[index] = min(this->__data[index * 2 + 1], this->__data[index * 2 + 2]);
            }
        };

        llong __query(llong qLeft, llong qRight, llong node, llong left, llong right) {
            if(right <= qLeft || qRight <= left) return INF;
            if(qLeft <= left && right <= qRight) return this->__data[node];

            llong leftVal = this->__query(qLeft, qRight, node * 2 + 1, left, (left + right) / 2);
            llong rightVal = this->__query(qLeft, qRight, node * 2 + 2, (left + right) / 2, right);
            return min(leftVal, rightVal);
        }

        // wrapper [left, right)
        llong query(llong left, llong right) {
            return this->__query(left, right, 0, 0, this->__size);
        };
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, K;
    cin >> N >> K;

    vecllong P(N, 0);
    SegmentTree minTree(N + 1);
    SegmentTree maxTree(N + 1);

    FOR(i, N) {
        cin >> P[i];
        minTree.update(i, P[i]);
        maxTree.update(i, -P[i]);
    }

    llong ans = 1;
    llong seq = 1;
    bool existSame = false;
    FORS(i, 1, K) {
        if(P[i - 1] < P[i]) seq++;
        else seq = 1;
    }
    if(seq >= K) existSame = true;

    FOR(left, N - K) {
        llong right = left + K;
        if(P[right - 1] < P[right]) seq++;
        else seq = 1;

        // P[left] を削除，P[right]を追加
        if(minTree.query(left, right) == P[left] && maxTree.query(left + 1, right + 1) == -P[right]) {
            continue;
        } else {
            if(seq >= K) {
                if(existSame) continue;
                else existSame = true;
            };
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}
