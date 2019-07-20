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

class UnionFind {
    public :
        vecllong parent;  // 親のインデックス
        vecllong height;  // 木の高さ
        vecllong size;  // 木の頂点数
        llong component;  // 木の数

        UnionFind (llong size_) : parent(size_), height(size_, 1), size(size_, 1) {
            for (llong i = 0; i < size_; i++) {
                parent[i] = i;
            }
            component = size_;
        }
        void init (llong size_) {
            parent.resize(size_);
            size.assign(size_, 1);
            component = size_;
            for (llong i = 0; i < size_; i++) {
                parent[i] = i;
            }
        }

        // メソッド
        // Find
        llong root(llong index) {
            if (index == parent[index]) {
                return index;
            }
            parent[index] = root(parent[index]);
            return parent[index];
        }

        // Union
        bool merge(llong index1, llong index2) {
            llong root1 = root(index1);
            llong root2 = root(index2);

            if (root1 == root2) {
                return false;
            }

            component--;

            if (height[root1] < height[root2]) {
                parent[root1] = root2;
                size[root2] += size[root1];
            } else {
                parent[root2] = parent[root1];
                size[root2] += size[root1];
                if (height[root1] == height[root2]) {
                    height[root1]++;
                }
            }
            return true;
        }

        bool isSameRoot(llong index1, llong index2) {
            return root(index1) == root(index2);
        }

        llong sizeOfSameRoot(llong index) {
            return size[root(index)];
        }
};

int main(void) {
    llong N, M;

    cin >> N >> M;

    llong p[N];
    FOR(i, N) cin >> p[i];

    UnionFind tree(N);
    vvecllong xy(M, vecllong(2, 0));
    FOR(i, M) {
        llong x, y;
        cin >> x >> y;
        tree.merge(x-1, y-1);
    }

    llong ans = 0;
    FOR(i, N) {
        if (tree.isSameRoot(i, p[i] - 1)) {
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}