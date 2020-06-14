#include <bits/stdc++.h>
using namespace std;

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
using intVV = vector<vector<int>>;
using llongV = vector<long long>;
using llongVV = vector<vector<long long>>;

template<class T = int>
using asc_pque = priority_queue<T, vector<T>, greater<T>>;
template<class T = int>
using desc_pque = priority_queue<T, vector<T>, less<T>>;

const llong MOD = 1000000007;
const int IINF = 1000000000;
const llong LINF = 100000000000000000LL;

template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

#define FOR(i, n) for (llong i = 0LL; i < llong(n); i++)
#define FORS(i, a, b) for (llong i = llong(a); i < llong(b); i++)
#define bisect_right(vec, a) upper_bound(vec.begin(), vec.end(), a) - vec.begin()
#define bisect_left(vec, a) lower_bound(vec.begin(), vec.end(), a) - vec.begin()
#define GET(i, p) get<i>(p)

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int H, W, K;
    cin >> H >> W >> K;

    int sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    sx--; sy--; tx--; ty--;

    vector<string> A;
    FOR(_, H) {
        string s;
        cin >> s;
        A.push_back(s);
    }

    vector<vector<int>> minDist(H, vector<int>(W, IINF));
    minDist[sx][sy] = 0;
    deque<tuple<int, int, int>> que;
    que.push_back({0, sx, sy});

    while(!que.empty()) {
        int dist, nx, ny;
        tie(dist, nx, ny) = que.front(); que.pop_front();

        FORS(i, 1, K + 1) {
            if (nx + i < H && A[nx + i][ny] == '@') break;

            if (nx + i < H && minDist[nx + i][ny] > dist + 1){
                minDist[nx + i][ny] = dist + 1;
                que.push_back({dist + 1, nx + i, ny});
            }
            if (nx + i < H && minDist[nx + i][ny] <= dist) break;
        }
        FORS(i, 1, K + 1) {
            if (nx - i >= 0 && A[nx - i][ny] == '@') break;

            if (nx - i >= 0 && minDist[nx - i][ny] > dist + 1){
                minDist[nx - i][ny] = dist + 1;
                que.push_back({dist + 1, nx - i, ny});
            }
            if (nx - i >= 0 && minDist[nx - i][ny] <= dist) break;
        }
        FORS(i, 1, K + 1) {
            if (ny + i < W  && A[nx][ny + i] == '@') break;

            if (ny + i < W && minDist[nx][ny + i] > dist + 1){
                minDist[nx][ny + i] = dist + 1;
                que.push_back({dist + 1, nx, ny + i});
            }
            if (ny + i < W && minDist[nx][ny + i] <= dist) break;
        }
        FORS(i, 1, K + 1) {
            if (ny - i >= 0 && A[nx][ny - i] == '@') break;

            if (ny - i >= 0 && minDist[nx][ny - i] > dist + 1){
                minDist[nx][ny - i] = dist + 1;
                que.push_back({dist + 1, nx, ny - i});
            }
            if (ny - i >= 0 && minDist[nx][ny - i] <= dist) break;
        }
    }

    int ans = minDist[tx][ty];
    cout << (ans == IINF ? -1 : ans) << endl;

    return 0;
}