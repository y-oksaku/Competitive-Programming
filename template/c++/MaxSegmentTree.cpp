#include <vector>
using namespace std;

// 0-indexed, [l, r)
template<class T = int>
class MaxSegmentTree {
    public :
        vector<T> __data;
        T __size;
        T INF;

        MaxSegmentTree (T size, T INF) {
            this->init(size, INF);
        };

        void init (T size, T INF) {
            // 完全二分木にする
            T binSize = 0;
            while((1 << binSize) < size) {
                binSize++;
            }
            this->__size = (1 << binSize);
            this->INF = INF;

            this->__data.resize(this->__size * 2);
            for(T i = 0; i < this->__size * 2; i++) {
                this->__data[i] = INF;
            }
        };

        /* メソッド */
        void update(T index, T value) {
            index += this->__size - 1;
            this->__data[index] = value;
            while(index > 0) {
                index = (index - 1) / 2;
                this->__data[index] = max(this->__data[index * 2 + 1], this->__data[index * 2 + 2]);
            }
        };

        T __query(T qLeft, T qRight, T node, T left, T right) {
            if(right <= qLeft || qRight <= left) return INF;
            if(qLeft <= left && right <= qRight) return this->__data[node];

            T leftVal = this->__query(qLeft, qRight, node * 2 + 1, left, (left + right) / 2);
            T rightVal = this->__query(qLeft, qRight, node * 2 + 2, (left + right) / 2, right);
            return max(leftVal, rightVal);
        }

        // wrapper
        T query(T left, T right) {
            return this->__query(left, right, 0, 0, this->__size);
        };
};
