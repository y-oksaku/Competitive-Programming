#include <vector>

using namespace std;
typedef long long llong;
typedef vector<llong> vecllong;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

class Combination {
    private:
        llong size;
        llong mod;
        vecllong fact;
        vecllong factInv;
        vecllong inv;

    public:
        Combination (llong size, llong mod) {
            this->init(size, mod);
        };

        void init(llong size, llong mod) {
            this->size = size + 2;
            this->mod = mod;
            this->fact = vecllong(size, 0);
            this->factInv = vecllong(size, 0);
            this->inv = vecllong(size, 0);

            // 初期値
            this->fact[0] = 1;
            this->fact[1] = 1;
            this->factInv[0] = 1;
            this->factInv[1] = 1;
            this->inv[0] = 0;
            this->inv[1] = 1;

            FORS(i, 2, this->size) {
                this->fact[i] = this->fact[i - 1] * i % mod;
                this->inv[i] = (mod - this->inv[mod % i] * (mod / i) % mod) % mod;
                this->factInv[i] = this->factInv[i - 1] * this->inv[i] % mod;
            }
        };

        llong npr(llong n, llong r) {
            if (n < r || n < 0 || r < 0) return 0;
            return this->fact[n] * this->factInv[n - r] % this->mod;
        };

        llong ncr(llong n, llong r) {
            if (n < r || n < 0 || r < 0) return 0;
            return this->fact[n] * (this->factInv[r] * this->factInv[n - r] % this->mod) % this->mod;
        };
};
