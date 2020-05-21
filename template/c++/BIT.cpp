#include <bits/stdc++.h>
using namespace std;

template<class T = int>
class BIT {
    private:
        T size;
        vector<T> data;
    public:
        BIT(T size) {
            this->size = size;
            this->data = vector<T>(size + 1, 0);
        };

        void add(T index, T value = 1) {
            while (index <= this->size) {
                this->data[index] += value;
                index += index & (-index);
            }
        };

        T sum(T index) {
            T ret = 0;
            while (index > 0) {
                ret += this->data[index];
                index -= index & (-index);
            }
            return ret;
        };

        T search(T value) {
            T i = 0, s = 0;
            T step = 1;
            while (step < this->size) step *= 2;

            while (step > 0) {
                if (i + step <= this->size && s + this->data[i + step] < value) {
                    i += step;
                    s += this->data[i];
                }
                step /= 2;
            }
            return i + 1;
        };
};
