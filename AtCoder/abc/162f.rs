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

    let (mut dp0, mut dp1, mut dp2) = (0, -INF, -INF);

    for (i, a) in A.iter().enumerate() {
        if i % 2 == 0 {
            dp1 = max(dp1, dp0);
            dp0 += a;
            dp2 += a;
        } else {
            dp2 = max(dp2, dp1);
            dp1 += a;
        }
    }

    if N % 2 == 0 {
        println!("{}", max(dp0, dp1));
    } else {
        println!("{}", max(dp1, dp2));
    }
}
