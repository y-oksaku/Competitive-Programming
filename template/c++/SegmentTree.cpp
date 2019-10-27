#include <vector>
using namespace std;
typedef long long llong;
typedef vector<llong> llongV;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

// 0-indexed, [l, r)
class SegmentTree {
    public :
        llongV __data;
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

        // wrapper
        llong query(llong left, llong right) {
            return this->__query(left, right, 0, 0, this->__size);
        };
};
