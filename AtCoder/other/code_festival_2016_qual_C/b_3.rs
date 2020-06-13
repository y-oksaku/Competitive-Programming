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
        K: usize,
        T: usize,
        A: [i64; T],
    }

    if T == 1 {
        println!("{}", K - 1);
        return;
    }

    let mxA = A.iter().max().unwrap();
    let D = A.iter().sum::<i64>() - mxA;

    println!("{}", max(0, mxA - 1 - D));
}
