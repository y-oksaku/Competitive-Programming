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
#define bisect_right(vec, a) upper_bound(vec.begin(), vec.end(), a) - vec.begin()
#define bisect_left(vec, a) lower_bound(vec.begin(), vec.end(), a) - vec.begin()
#define GET(i, T) get<i>(T)

llong H, W;
llongVV A;

llong sol(llong sh, llong sw) {
    llongVV minDist(H, llongV(W, LINF));
    minDist[sh][sw] = 0;
    priority_queue<tuple<llong, llong, llong>> que;
    que.push(make_tuple(0LL, sh, sw));

    while(!que.empty()) {
        llong d, h, w;
        tie(d, h, w) = que.top();
        d = -d;
        que.pop();

        if (h > 0 && minDist[h - 1][w] > d + A[h - 1][w]) {
            minDist[h - 1][w] = d + A[h - 1][w];
            que.push(make_tuple(-(d + A[h - 1][w]), h - 1, w));
        }
        if (h < H - 1 && minDist[h + 1][w] > d + A[h + 1][w]) {
            minDist[h + 1][w] = d + A[h + 1][w];
            que.push(make_tuple(-(d + A[h + 1][w]), h + 1, w));
        }
        if (w > 0 && minDist[h][w - 1] > d + A[h][w - 1]) {
            minDist[h][w - 1] = d + A[h][w - 1];
            que.push(make_tuple(-(d + A[h][w - 1]), h, w - 1));
        }
        if (w < W - 1 && minDist[h][w + 1] > d + A[h][w + 1]) {
            minDist[h][w + 1] = d + A[h][w + 1];
            que.push(make_tuple(-(d + A[h][w + 1]), h, w + 1));
        }
    }
    return minDist[H - 1][0] + minDist[H - 1][W - 1] + minDist[0][W - 1] + A[sh][sw];
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> H >> W;
    A = llongVV(H, llongV(W, LINF));
    FOR(h, H) {
        FOR(w, W) {
            cin >> A[h][w];
        }
    }

    llong ans = LINF;
    FOR(h, H) {
        FOR(w, W) {
            chmin(ans, sol(h, w));
        }
    }

    cout << ans << endl;

    return 0;
}