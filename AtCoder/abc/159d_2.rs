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

const MOD: u64 = 1000000007;
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        N: usize,
        A: [usize; N],
    }

    let mut cnt = vec![0i64; N + 1];
    for &a in &A {
        cnt[a] += 1;
    }

    let S: i64 = cnt.iter().map(|&a| a * (a - 1) / 2).sum();

    for (i, &a) in A.iter().enumerate() {
        let c = cnt[a];
        let ans = S - c * (c - 1) / 2 + max(0, (c - 2) * (c - 1) / 2);
        println!("{}", ans);
    }
}
