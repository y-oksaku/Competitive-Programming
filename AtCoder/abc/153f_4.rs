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


fn upper_bound<T: Ord>(A: &Vec<T>, x: T) -> usize {
    let (mut l, mut r) = (-1 as i64, A.len() as i64);

    while r - l > 1 {
        let mid = (r + l) / 2;
        if A[mid as usize] > x {
            r = mid;
        } else {
            l = mid;
        }
    }

    return r as usize;
}

fn main() {
    input! {
        N: usize,
        D: i64,
        A: i64,
        mut XH: [(i64, i64); N],
    }

    XH.sort();
    let X: Vec<i64> = XH.iter().map(|&(x, _)| x).collect();

    dbg!(&XH);
    dbg!(&X);

    let mut ans = 0;
    let mut ims = vec![0; N + 1];
    let mut now = 0;

    for l in 0..N {
        now += ims[l];
        if XH[l].1 <= A * now {
            continue;
        }

        let ness = (XH[l].1 - A * now + (A - 1)) / A;
        let nx = upper_bound(&X, X[l] + 2 * D);
        ims[nx] -= ness;
        now += ness;
        ans += ness;
    }

    println!("{}", ans);
}
