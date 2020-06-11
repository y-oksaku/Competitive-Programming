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
        X: usize,
        Y: usize,
        N: usize,
        M: usize,
        K: usize,
        mut A: [usize; N],
        mut B: [usize; M],
        mut C: [usize; K],
    }

    A.sort_by(|a, b| b.cmp(a));
    B.sort_by(|a, b| b.cmp(a));

    for i in 0..min(N, X) {
        C.push(A[i]);
    }
    for i in 0..min(M, Y) {
        C.push(B[i]);
    }

    C.sort_by(|a, b| b.cmp(a));
    println!("{}", C.iter().take(X + Y).sum::<usize>());
}
