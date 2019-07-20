#include <vector>
using namespace std;
typedef long long llong;
typedef vector<llong> vecllong;

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