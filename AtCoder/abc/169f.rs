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

const MOD: usize = 998244353;
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        N: usize,
        S: usize,
        A: [usize; N],
    }

    let mut dp = vec![0; S + 1];
    dp[0] = 1;

    for a in &A {
        let mut newDp: Vec<usize> = dp.iter().map(|d| d * 2).collect();
        for s in 0..(S + 1) {
            if s + a <= S {
                newDp[s + a] += dp[s];
            }
        }
        dp = newDp.into_iter().map(|d| d % MOD).collect();
    }

    println!("{}", dp[S]);
}
