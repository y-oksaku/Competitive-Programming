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
        N: usize,
        P: usize,
        A: [usize; N],
    }

    if A.iter().all(|&a| a % 2 == 0) {
        if P == 0 {
            println!("{}", (2u64).pow(N as u32));
        } else {
            println!("0");
        }
        return;
    }

    println!("{}", (2u64).pow((N - 1) as u32));
}
