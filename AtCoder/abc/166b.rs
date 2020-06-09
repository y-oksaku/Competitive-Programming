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
        K: usize,
    }

    let mut cnt = vec![0; N];

    for _ in 0..K {
        input! {
            D: usize,
            A: [Usize1; D],
        }
        for &a in &A {
            cnt[a] += 1;
        }
    }

    println!("{}", cnt.iter().filter(|&&c| c == 0).count());
}
