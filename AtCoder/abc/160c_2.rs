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
        K: i64,
        N: usize,
        mut A: [i64; N],
    }

    A.push(K + A[0]);
    let mut D = vec![];
    for i in 0..N {
        D.push(A[i + 1] - A[i]);
    }

    println!("{}", D.iter().sum::<i64>() - D.iter().max().unwrap());
}
