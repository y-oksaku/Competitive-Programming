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
        X: i64,
    }

    for a in -500_i64..501_i64 {
        for b in -500_i64..501_i64 {
            if a.pow(5) - b.pow(5) == X {
                println!("{} {}", a, b);
                return;
            }
        }
    }

}
