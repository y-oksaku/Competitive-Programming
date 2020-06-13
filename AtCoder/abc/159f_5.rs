#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_assignments)]
use proconio::input;
use proconio::marker::*;
use std::collections::*;
use std::cmp::*;
use std::mem::swap;
use std::f64::consts::*;

const MOD: u64 = 998244353;
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        N: usize,
        S: usize,
        A: [usize; N],
    }

    let mut dp = vec![0u64; S + 1];
    let mut ans = 0;

    for a in A {
        dp[0] += 1;
        for s in (0..(S + 1)).rev() {
            if s + a <= S {
                dp[s + a] = (dp[s + a] + dp[s]) % MOD;
            }
        }
        ans = (ans + dp[S]) % MOD;
    }

    println!("{}", ans % MOD);
}
