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
        mut A: usize,
        mut B: usize,
        mut C: usize,
    }

    std::mem::swap(&mut A, &mut B);
    std::mem::swap(&mut A, &mut C);

    println!("{} {} {}", A, B, C);
}
