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

struct Edge {
    long long from;
    long long to;
    long long cost;
};

template<typename T>
using asc = less<T>();
template<typename T>
using desc = greater<T>();

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)
#define sup(vec, a) upper_bound(vec.begin(), vec.end(), a) - vec.begin()
#define inf(vec, a) lower_bound(vec.begin(), vec.end(), a) - vec.begin()

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

    llong N, Q;
    cin >> N >> Q;

    SegmentTree tree(N);
    llongV A(N);
    llongV aToI(N + 1, -1);

    FOR(i, N) {
        cin >> A[i];
        aToI[A[i]] = i;
        tree.update(i, A[i]);
    }

    llongV ans;
    FOR(i, Q) {
        llong q, l, r;
        cin >> q >> l >> r;
        l--;
        r--;
        if(q == 1) {
            tree.update(l, A[r]);
            tree.update(r, A[l]);
            aToI[A[r]] = l;
            aToI[A[l]] = r;
            swap(A[l], A[r]);
        } else {
            ans.push_back(aToI[tree.query(l, r + 1)]);
        }
    }

    for(llong a : ans) {
        cout << (a + 1) << endl;
    }

    return 0;
}