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
        M: usize,
    }

    let mut B = vec![vec![0i64; M]; N];
    for n in 0..N {
        input! {
            S: Chars,
        }
        for m in 0..M {
            B[n][m] = ((S[m] as i32) - ('0' as i32)) as i64;
        }
    }

    let mut ans = vec![vec![0i64; M]; N];

    for n in 1..N-1 {
        for m in 1..M-1 {
            ans[n][m] = B[n - 1][m];
            B[n + 1][m] -= ans[n][m];
            B[n][m - 1] -= ans[n][m];
            B[n][m + 1] -= ans[n][m];
        }
    }

    for row in ans {
        for a in row {
            print!("{}", a);
        }
        println!("");
    }
}
