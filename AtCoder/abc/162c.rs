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

fn gcd(n: usize, m:usize) -> usize {
    if m == 0 {
        return n;
    }
    return gcd(m, n % m);
}

fn main() {
    input! {
        K: usize,
    }

    let mut ans = 0;
    for a in 1..K+1 {
        for b in 1..K+1 {
            for c in 1..K+1 {
                ans += gcd(gcd(a, b), c);
            }
        }
    }
    println!("{}", ans);
}
