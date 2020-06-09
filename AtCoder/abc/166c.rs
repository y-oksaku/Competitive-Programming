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
        N: usize,
        M: usize,
        H: [u64; N],
    }

    let mut edges: Vec<Vec<usize>> = vec![vec![]; N];

    for _ in 0..M {
        input! {
            fr: Usize1,
            to: Usize1,
        }
        edges[fr].push(to);
        edges[to].push(fr);
    }

    let mut ans = 0;
    for i in 0..N {
        if edges[i].iter().all(|&to| H[to] < H[i]) {
            ans += 1;
        }
    }

    println!("{}", ans);
}
