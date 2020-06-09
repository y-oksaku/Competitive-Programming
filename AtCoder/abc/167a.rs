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
        S: String,
        T: String,
    }

    let A: Vec<char> = S.chars().collect();
    let B: Vec<char> = T.chars().collect();

    if A.len() + 1 != B.len() {
        println!("No");
        return;
    }

    for (a, b) in A.iter().zip(B.iter()) {
        if a != b {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
