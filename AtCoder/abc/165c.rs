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

fn search(ABCD: &Vec<(usize, usize, i64, i64)>, N: usize, mi: i64, mx: i64, A: &mut Vec<i64>) -> i64 {
    if A.len() == N {
        let mut ret: i64 = 0;
        for &(a, b, c, d) in ABCD {
            if A[b] - A[a] == c {
                ret += d;
            }
        }
        return ret;
    }

    let mut ret: i64 = 0;

    for a in mi..mx {
        A.push(a);
        ret = max(ret, search(ABCD, N, max(a, mi), mx, A));
        A.pop();
    }
    return ret;
}

fn main() {
    input! {
        N: usize,
        M: i64,
        Q: usize,
        ABCD: [(Usize1, Usize1, i64, i64); Q],
    }

    let mut A = vec![];
    println!("{}", search(&ABCD, N, 1, M + 1, &mut A));
}
