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
    }

    let mut A = vec![0; N];
    let mut B = vec![0; N];

    for i in 0..N {
        input! {
            a: usize,
            b: usize,
        };
        A[i] = a;
        B[i] = b;
    }

    A.sort();
    B.sort();

    if N % 2 == 1 {
        println!("{}", B[N / 2] - A[N / 2] + 1);
    } else {
        let a = A[N / 2] + A[N / 2 - 1];
        let b = B[N / 2] + B[N / 2 - 1];
        println!("{}", b - a + 1);
    }
}
