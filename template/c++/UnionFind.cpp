#include <bits/stdc++.h>
using namespace std;

template<class T = int>
class UnionFind {
    public :
        vector<T> parent;  // 親のインデックス
        vector<T> height;  // 木の高さ
        vector<T> size;  // 木の頂点数
        T componentCount;  // 木の数

        UnionFind (T size_) {
            this->init(size_);
        }

        void init (T size_) {
            this->parent.resize(size_);
            this->size.assign(size_, 1);
            this->height.assign(size_, 1);
            this->componentCount = size_;
            for (T i = 0; i < size_; i++) {
                this->parent[i] = i;
            }
        }

        T root(T index) {
            if (index == this->parent[index]) {
                return index;
            }
            this->parent[index] = root(this->parent[index]);
            return this->parent[index];
        }

        // Union
        bool merge(T index1, T index2) {
            T root1 = this->root(index1);
            T root2 = this->root(index2);

            if (root1 == root2) {
                return false;
            }

            this->componentCount--;

            if (this->height[root1] < this->height[root2]) {
                this->parent[root1] = root2;
                this->size[root2] += this->size[root1];
            } else {
                this->parent[root2] = this->parent[root1];
                this->size[root1] += this->size[root2];
                if (this->height[root1] == this->height[root2]) {
                    this->height[root1]++;
                }
            }
            return true;
        }

        bool isSameRoot(T index1, T index2) {
            return this->root(index1) == this->root(index2);
        }

        T sizeOfSameRoot(T index) {
            return this->size[root(index)];
        }
};
