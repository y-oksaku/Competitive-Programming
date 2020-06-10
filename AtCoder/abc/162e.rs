#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_assignments)]
use proconio::input;
use proconio::marker::Usize1;
use std::collections::*;
use std::cmp::*;
use std::f64::consts::*;

const MOD: i64 = 1000000007;
const INF: i64 = std::i64::MAX / 4;

fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
    if modulus == 1 { return 0 }
    let mut result = 1;
    base %= modulus;
    while exp > 0 {
        if exp % 2 == 1 {
            result = result * base % modulus;
        }
        exp >>= 1;
        base = base * base % modulus
    }

    return result;
}

fn main() {
    input! {
        N: i64,
        K: i64,
    }

    let mut ans: i64 = 0;
    let mut V = vec![0; (K + 1) as usize];

    for a in (1..K+1).rev() {
        let M = K / a;
        let mut cnt = mod_pow(M, N, MOD);

        let mut mul = a + a;
        while mul <= K {
            cnt -= V[mul as usize];
            if cnt < 0 {
                cnt += MOD;
            }
            mul += a;
        }

        cnt %= MOD;
        ans += cnt * a;
        ans %= MOD;
        V[a as usize] = cnt;
    }

    println!("{}", ans);
}
