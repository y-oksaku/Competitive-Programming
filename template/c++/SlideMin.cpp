#include <bits/stdc++.h>
using namespace std;

template<class T = int, class U = int>
class SlideMin {
    struct Pair {
        T index;
        U value;
        Pair(){};
        Pair(T index, U value): index(index), value(value) {};
    };

    private:
        deque<Pair> que;
        T length;
    public:
        SlideMin(T length) {
            this->length = length;
        }

        Pair top() {
            return this->que.front();
        }

        void update(T index, U value) {
            while (!this->que.empty() && this->que.back().value >= value) {
                this->que.pop_back();
            }
            this->que.emplace_back(index, value);

            if(this->que.front().index == index - this->length) this->que.pop_front();
        }
};
