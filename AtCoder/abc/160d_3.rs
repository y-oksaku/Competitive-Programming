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
        X: i64,
        Y: i64
    }

    let mut ans = vec![0; N];

    for i in 1i64..((N as i64) + 1) {
        for j in i+1..((N as i64) + 1) {
            let D = vec![
                j - i,
                (j - X).abs() + (i - Y).abs() + 1,
                (j - Y).abs() + (i - X).abs() + 1,
            ];
            ans[*D.iter().min().unwrap() as usize] += 1;
        }
    }

    for i in 1..N {
        println!("{}", ans[i]);
    }
}
