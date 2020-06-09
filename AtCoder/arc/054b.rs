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

fn f(P: f64, x: f64) -> f64 {
    return x + P / (2. as f64).powf(x / 1.5);
}

fn main() {
    input! {
        P: f64,
    }

    let (mut l, mut r): (f64, f64) = (0., P);

    for _ in 0..1000 {
        let d: f64 = (r - l) / 3.;

        if f(P, l + d) > f(P, r - d) {
            l += d;
        } else {
            r -= d;
        }
    }

    println!("{}", f(P, l));
}
