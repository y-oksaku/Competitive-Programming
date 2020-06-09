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
        mut N: u64,
    }

    let mut ans = 0;
    let mut div = 2;

    while div * div <= N {
        let mut cnt = 0;
        while N % div == 0 {
            cnt += 1;
            N /= div;
        }
        let mut i = 1;
        while cnt >= i {
            ans += 1;
            cnt -= i;
            i += 1;
        }
        div += 1;
    }

    if N > 1 {
        ans += 1;
    }

    println!("{}", ans);
}
