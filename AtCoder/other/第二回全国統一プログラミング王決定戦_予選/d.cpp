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

using Int = unsigned int;
using llong = long long;
using Llong = unsigned long long;
using ldouble = long double;
using intV = vector<int>;
using llongV = vector<long long>;
using llongVV = vector<vector<long long>>;
using Graph = vector<vector<long long>>;
using costGraph = vector<vector<pair<long long, long long>>>;

const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0LL; i < llong(n); i++)
#define FORS(i, a, b) for (llong i = llong(a); i < llong(b); i++)

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

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    SegmentTree tree(N + 1);
    tree.update(1, 0);
    vector<tuple<llong, llong, llong>> edges(M);

    FOR(i, M) cin >> get<0>(edges[i]) >> get<1>(edges[i]) >> get<2>(edges[i]);
    sort(edges.begin(), edges.end());

    FOR(i, 10) {
        for(auto a : edges) {
            llong L, R, C;
            tie(L, R, C) = a;
            llong cost = tree.query(L, R + 1) + C;
            tree.update(R, min(cost, tree.query(R, R + 1)));
        }
    }

    llong ans = tree.query(N, N + 1);
    if(ans == INF) ans = -1;
    cout << ans << endl;

    return 0;
}