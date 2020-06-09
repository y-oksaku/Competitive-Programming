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
        X: usize,
        CA: [(usize, [usize; M]); N],
    }

    let mut ans = INF;
    for mask in 0..(1 << N) {
        let mut Z: Vec<usize> = vec![0; M];
        let mut cost = 0;

        for (i, (C, A)) in CA.iter().enumerate() {
            if (1 << i) & mask == 0 {
                continue;
            }
            cost += C;
            for (j, a) in A.iter().enumerate() {
                Z[j] += a;
            }
        }

        if Z.iter().all(|z| *z >= X) {
            ans = min(ans, cost);
        }
    }

    if ans < INF {
        println!("{}", ans);
    } else {
        println!("-1");
    }
}
