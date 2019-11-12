#include <vector>
using namespace std;

template<class T = int>
class UnionFind {
    public :
        vector<T> parent;  // 親のインデックス
        vector<T> height;  // 木の高さ
        vector<T> size;  // 木の頂点数
        T component;  // 木の数

        UnionFind (T size_) : parent(size_), height(size_, 1), size(size_, 1) {
            for (T i = 0; i < size_; i++) {
                parent[i] = i;
            }
            component = size_;
        }
        void init (T size_) {
            parent.resize(size_);
            size.assign(size_, 1);
            component = size_;
            for (T i = 0; i < size_; i++) {
                parent[i] = i;
            }
        }

        // メソッド
        // Find
        T root(T index) {
            if (index == parent[index]) {
                return index;
            }
            parent[index] = root(parent[index]);
            return parent[index];
        }

        // Union
        bool merge(T index1, T index2) {
            T root1 = root(index1);
            T root2 = root(index2);

            if (root1 == root2) {
                return false;
            }

            component--;

            if (height[root1] < height[root2]) {
                parent[root1] = root2;
                size[root2] += size[root1];
            } else {
                parent[root2] = parent[root1];
                size[root1] += size[root2];
                if (height[root1] == height[root2]) {
                    height[root1]++;
                }
            }
            return true;
        }

        bool isSameRoot(T index1, T index2) {
            return root(index1) == root(index2);
        }

        T sizeOfSameRoot(T index) {
            return size[root(index)];
        }
};