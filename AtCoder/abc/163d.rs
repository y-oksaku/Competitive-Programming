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
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        N: i64,
        K: i64,
    }

    let mut ans: i64 = 0;
    for k in K..N+2 {
        let mi = k * (k - 1) / 2;
        let mx = N * k - mi;
        ans += mx - mi + 1;
        ans %= MOD;
    }

    println!("{}", ans);
}
