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
        N: i64,
        A: i64,
        B: i64,
        C: i64,
        D: i64,
    }

    let R = D - C;

    for k in 0..N {
        let l = N - 1 - k;
        let Z = (B - A) - C * (k - l);

        if -R * l <= Z && Z <= R * k {
            println!("YES");
            return;
        }
    }

    println!("NO");
}
