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
        A: [(f64, f64); N],
        B: [(f64, f64); N],
    }

    let mut cA = A.iter().fold((0., 0.), |S, a| (S.0 + a.0, S.1 + a.1));
    let mut cB = B.iter().fold((0., 0.), |S, b| (S.0 + b.0, S.1 + b.1));

    cA = (cA.0 / (N as f64), cA.1 / (N as f64));
    cB = (cB.0 / (N as f64), cB.1 / (N as f64));

    let mxA = A.iter().map(|&a| (a.0 - cA.0) * (a.0 - cA.0) + (a.1 - cA.1) * (a.1 - cA.1)).fold(0f64, |mx, a| mx.max(a));
    let mxB = B.iter().map(|&b| (b.0 - cB.0) * (b.0 - cB.0) + (b.1 - cB.1) * (b.1 - cB.1)).fold(0f64, |mx, b| mx.max(b));

    println!("{}", mxB.sqrt() / mxA.sqrt());
}
