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

class UnionFind {
    public :
        llongV parent;  // 親のインデックス
        llongV height;  // 木の高さ
        llongV size;  // 木の頂点数
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
                size[root1] += size[root2];
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

vector<vector<int>> edges;

int search(int start, int N) {
    int INF = (int)1e9;
    vector<int> minDist(N, INF);
    queue<pair<int, int>> que;
    que.emplace(start, 0);
    while(!que.empty()) {
        int now, d;
        tie(now, d) = que.front();
        que.pop();
        if(minDist[now] <= d) continue;
        minDist[now] = d;
        for(int to : edges[now]) {
            if(minDist[to] == INF) {
                que.emplace(to, d + 1);
            };
        }
    }

    int ret = 0;
    for(int d : minDist) {
        if(d != INF) chmax(ret, d - 1);
    }
    return ret;
};

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int N, M;
    cin >> N >> M;
    UnionFind tree((llong)N);
    edges.resize(N);

    FOR(i, M) {
        int fr, to;
        cin >> fr >> to;
        fr--;
        to--;
        edges[fr].push_back(to);
        edges[to].push_back(fr);
        tree.merge((llong)fr, (llong)to);
    }

    int Q;
    cin >> Q;
    vector<pair<int, int>> ans(Q);
    FOR(q, Q) {
        int start;
        cin >> start;
        start--;
        int dist = search(start, N);
        int day = 0;
        while((1 << day) <= dist) day++;
        ans[q] = make_pair((int)tree.sizeOfSameRoot(start) - 1, day);
    }

    for(auto a : ans) cout << a.first << " " << a.second << endl;

    return 0;
}