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
#include <functional>

using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

template <class A, class B>
string to_string(pair<A, B> p);

template <class A, class B, class C>
string to_string(tuple<A, B, C> p);

template <class A, class B, class C, class D>
string to_string(tuple<A, B, C, D> p);

string to_string(const string& s) {
    return '"' + s + '"';
}

string to_string(const char* s) {
    return to_string((string) s);
}

string to_string(bool b) {
    return (b ? "true" : "false");
}

string to_string(vector<bool> v) {
    bool first = true;
    string res = "{";
    for (int i = 0; i < static_cast<int>(v.size()); i++) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(v[i]);
    }
    res += "}";
    return res;
}

template <size_t N>
string to_string(bitset<N> v) {
    string res = "";
    for (size_t i = 0; i < N; i++) {
        res += static_cast<char>('0' + v[i]);
    }
    return res;
}

template <class A>
string to_string(A v) {
    bool first = true;
    string res = "{";
    for (const auto &x : v) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
    }
    res += "}";
    return res;
}

template <class A, class B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <class A, class B, class C>
string to_string(tuple<A, B, C> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}

template <class A, class B, class C, class D>
string to_string(tuple<A, B, C, D> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ", " + to_string(get<3>(p)) + ")";
}

void debug_out() { cerr << endl; }

template <class Head, class... Tail>
void debug_out(Head H, Tail... T) {
    cerr << " " << to_string(H);
    debug_out(T...);
}

#ifdef LOCAL
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif

using Int = unsigned int;
using llong = long long;
using Llong = unsigned long long;
using ldouble = long double;
using intV = vector<int>;
using llongV = vector<long long>;
using llongVV = vector<vector<long long>>;

template<class T = int>
using asc_pque = priority_queue<T, vector<T>, greater<T>>;
template<class T = int>
using desc_pque = priority_queue<T, vector<T>, less<T>>;

const llong MOD = 1000000007;
const int IINF = 1000000000;
const llong LINF = 100000000000000000LL;

#define FOR(i, n) for (llong i = 0LL; i < llong(n); i++)
#define FORS(i, a, b) for (llong i = llong(a); i < llong(b); i++)
#define sup(vec, a) upper_bound(vec.begin(), vec.end(), a) - vec.begin()
#define inf(vec, a) lower_bound(vec.begin(), vec.end(), a) - vec.begin()
#define GET(i, T) get<i>(T)

// 0-indexed, [l, r)
template<class T = int>
class MinSegmentTree {
    public :
        vector<T> __data;
        T __size;
        T INF;

        MinSegmentTree (T size, T INF) {
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
                this->__data[index] = min(this->__data[index * 2 + 1], this->__data[index * 2 + 2]);
            }
        };

        T __query(T qLeft, T qRight, T node, T left, T right) {
            if(right <= qLeft || qRight <= left) return INF;
            if(qLeft <= left && right <= qRight) return this->__data[node];

            T leftVal = this->__query(qLeft, qRight, node * 2 + 1, left, (left + right) / 2);
            T rightVal = this->__query(qLeft, qRight, node * 2 + 2, (left + right) / 2, right);
            return min(leftVal, rightVal);
        }

        // wrapper
        T query(T left, T right) {
            return this->__query(left, right, 0, 0, this->__size);
        };
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int N, Q;
    cin >> N >> Q;

    vector<tuple<int, bool, int, int>> events;
    FOR(i, N) {
        int s, t, x;
        cin >> s >> t >> x;
        events.emplace_back(s - x, true, x, i);
        events.emplace_back(t - x, false, x, i);
    }
    sort(events.begin(), events.end());

    intV ans(Q);
    MinSegmentTree<int> tree(N, IINF);

    int i = 0;
    FOR(q, Q) {
        int d;
        cin >> d;
        while(i < N * 2 && GET(0, events[i]) <= d) {
            if(GET(1, events[i])) {
                tree.update(GET(3, events[i]), GET(2, events[i]));
            } else {
                tree.update(GET(3, events[i]), IINF);
            }
            i++;
        }
        ans[q] = tree.__data[0];
    }

    for(auto a : ans) cout << (a == IINF ? -1 : a) << endl;

    return 0;
}