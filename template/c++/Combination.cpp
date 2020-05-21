#include <bits/stdc++.h>
using namespace std;

template<class T = long long>
class Combination {
    private:
        T size;
        T mod;
        vector<T> fact;
        vector<T> factInv;
        vector<T> inv;

    public:
        Combination (T size, T mod = 1000000007) {
            this->init(size, mod);
        };

        void init(T size, T mod) {
            this->size = size + 2;
            this->mod = mod;
            this->fact = vector<T>(this->size, 0);
            this->factInv = vector<T>(this->size, 0);
            this->inv = vector<T>(this->size, 0);

            // 初期値
            this->fact[0] = 1;
            this->fact[1] = 1;
            this->factInv[0] = 1;
            this->factInv[1] = 1;
            this->inv[0] = 0;
            this->inv[1] = 1;

            for(T i = 2; i < this->size; i++) {
                this->fact[i] = this->fact[i - 1] * i % mod;
                this->inv[i] = (mod - this->inv[mod % i] * (mod / i) % mod) % mod;
                this->factInv[i] = this->factInv[i - 1] * this->inv[i] % mod;
            }
        };

        T npr(T n, T r) {
            if (n < r || n < 0 || r < 0) return 0;
            return this->fact[n] * this->factInv[n - r] % this->mod;
        };

        T ncr(T n, T r) {
            if (n < r || n < 0 || r < 0) return 0;
            return this->fact[n] * (this->factInv[r] * this->factInv[n - r] % this->mod) % this->mod;
        };

        T nhr(T n, T r) {
            return this->ncr(n + r - 1, n - 1);
        }
};
