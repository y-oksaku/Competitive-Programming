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

fn isOk(S: &[char]) -> bool {
    for (s, t) in S.iter().zip(S.iter().rev()) {
        if s != t {
            return false;
        }
    }
    return true;
}

fn main() {
    input! {
        S: Chars,
    }

    let N = S.len();

    if isOk(&S) && isOk(&S[0..(N / 2)]) && isOk(&S[(N / 2 + 1)..N]) {
        println!("Yes");
    } else {
        println!("No");
    }
}
