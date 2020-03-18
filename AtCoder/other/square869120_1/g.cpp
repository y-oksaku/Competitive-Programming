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

struct Edge {
    llong to;
    llong dist;
    llong time;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    llong N, M;
    cin >> N >> M;

    vector<vector<Edge>> edges(N, vector<Edge>(0));

    FOR(i, M) {
        llong fr, to, dist, time;
        cin >> fr >> to >> dist >> time;
        fr--; to--;
        edges[fr].push_back({to, dist, time});
        edges[to].push_back({fr, dist, time});
    }

    llongVV minDist(N, llongV(1 << N, LINF));
    llongVV count(N, llongV(1 << N, 0LL));
    count[0][0] = 1;

    priority_queue<tuple<llong, llong, llong>> que;
    que.emplace(0, 0, 0);

    while(!que.empty()) {
        llong dist, now, mask;
        tie(dist, now, mask) = que.top();
        dist = -dist;
        que.pop();

        if(minDist[now][mask] < dist) continue;

        for(Edge e : edges[now]) {
            if(dist + e.dist > e.time) continue;
            if((mask & (1 << e.to)) > 0) continue;

            llong state = mask | (1 << e.to);
            if(minDist[e.to][state] > dist + e.dist) {
                count[e.to][state] = 0;
                minDist[e.to][state] = dist + e.dist;
                que.emplace(-(dist + e.dist), e.to, state);
            }
            if(minDist[e.to][state] == dist + e.dist) {
                count[e.to][state] += count[now][mask];
            }
        }
    }

    if(count[0][(1 << N) - 1] == 0) cout << "IMPOSSIBLE" << endl;
    else cout << minDist[0][(1 << N) - 1] << " " << count[0][(1 << N) - 1] << endl;

    return 0;
}
