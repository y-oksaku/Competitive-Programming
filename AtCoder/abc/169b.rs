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
        A: [u128; N],
    }

    let zero = A.iter().filter(|&&a| a == 0).count();

    if zero > 0 {
        println!("0");
        return;
    }

    let mut prd = 1;
    let mx = 10u128.pow(18);
    for &a in &A {
        prd *= a;
        if prd > mx {
            println!("-1");
            return;
        }
    }
    println!("{}", prd);
}
