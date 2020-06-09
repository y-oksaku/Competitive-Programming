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
        A: [i64; N],
    }

    let mut cnt: HashMap<i64, u64> = HashMap::new();
    let mut ans = 0;

    for (i, &a) in A.iter().enumerate() {
        ans += *cnt.entry((i as i64) - a).or_default();
        *cnt.entry((i as i64) + a).or_insert(0) += 1;
    }

    println!("{}", ans);
}
