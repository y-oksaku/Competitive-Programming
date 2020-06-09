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
        N: usize,
        K: u64,
        mut A: [Usize1; N],
    }

    let mut now = 0;

    for d in 0..64 {
        if ((1 << d) & K) != 0 {
            now = A[now];
        }
        A = A.iter().map(|a| A[*a]).collect();
    }

    println!("{}", now + 1);
}
