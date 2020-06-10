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

const MOD: u64 = 1000000007;
const INF: i64 = std::i64::MAX / 4;

fn main() {
    input! {
        N: usize,
        A: [i64; N],
    }

    let mut AI: Vec<(i64, i64)> = A.iter().enumerate().map(|(i, &a)| (a, i as i64)).collect();
    AI.sort();
    AI.reverse();

    let mut dp = vec![vec![-INF; N + 1]; N + 1];
    dp[0][0] = 0;

    for (i, &(a, j)) in AI.iter().enumerate() {
        for l in 0..i+1 {
            let r = i - l;
            dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + (a * ((l as i64) - j as i64).abs()));
            dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + (a * (((N as i64) - 1 - (r as i64)) - j as i64).abs()));
        }
    }

    println!("{}", dp.iter().map(|d| d.iter().max().unwrap()).max().unwrap());
}
