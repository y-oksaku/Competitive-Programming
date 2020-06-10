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
        mut A: i64,
        mut B: i64,
        mut C: i64,
        mut D: i64,
    }

    for i in 0..1000 {
        if i % 2 == 0 {
            C -= B;
            if C <= 0 {
                println!("Yes");
                break;
            }
        } else {
            A -= D;
            if A <= 0 {
                println!("No");
                break;
            }
        }
    }
}
