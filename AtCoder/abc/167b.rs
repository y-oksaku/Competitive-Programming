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
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        A: i64,
        B: i64,
        C: i64,
        mut K: i64,
    }

    let mut ans: i64 = 0;
    let mut t: i64 = 0;

    t = min(A, K);
    ans += t;
    K -= t;

    t = min(B, K);
    K -= t;

    t = min(C, K);
    ans -= t;

    println!("{}", ans);
}
