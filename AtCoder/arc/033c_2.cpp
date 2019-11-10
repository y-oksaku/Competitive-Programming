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

template <typename A, typename B>
string to_string(pair<A, B> p);

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p);

template <typename A, typename B, typename C, typename D>
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

template <typename A>
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

template <typename A, typename B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ", " + to_string(get<3>(p)) + ")";
}

void debug_out() { cerr << endl; }

template <typename Head, typename... Tail>
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

#define FOR(i, n) for (llong i = 0LL; i < llong(n); i++)
#define FORS(i, a, b) for (llong i = llong(a); i < llong(b); i++)
#define sup(vec, a) upper_bound(vec.begin(), vec.end(), a) - vec.begin()
#define inf(vec, a) lower_bound(vec.begin(), vec.end(), a) - vec.begin()

class SegmentTree {
    public:
        llong size;
        llongV data;
        SegmentTree(llong size) {
            llong i = 0;
            while((1 << i) < size) i++;
            this->size = (1 << i);
            this->data = llongV(this->size * 2 - 1, 0);
        };

        void update(llong i, llong val) {
            i += this->size - 1;
            this->data[i] = val;
            while(i >= 0) {
                i = (i - 1) / 2;
                this->data[i] = this->data[i * 2 + 1] + this->data[i * 2 + 2];
                if(i == 0) break;
            }
        };

        llong query(llong left, llong right) {
            llong L = left + this->size;
            llong R = right + this->size;
            llong ret = 0;
            while(L < R) {
                if(R & 1 == 1) {
                    R--;
                    ret = ret + this->data[R - 1];
                }
                if(L & 1 == 1) {
                    ret = ret + this->data[L - 1];
                    L++;
                }
                L >>= 1;
                R >>= 1;
            }
            return ret;
        }
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong Q;
    cin >> Q;
    llong N = 210000;
    SegmentTree tree(N);

    llongV ans;
    FOR(i, Q) {
        llong t, x;
        cin >> t >> x;
        if(t == 1) tree.update(x, 1);
        else {
            llong ng = 0;
            llong ok = N;
            while(ok - ng > 1) {
                llong mid = (ok + ng) / 2;
                if(tree.query(0, mid) < x) ng = mid;
                else ok = mid;
            }
            ans.push_back(ok - 1);
            tree.update(ok - 1, 0);
        }
    }

    for(auto a : ans) cout << a << endl;

    return 0;
}