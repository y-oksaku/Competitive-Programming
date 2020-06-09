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
    }

    let mut cnt: HashMap<(usize, usize), usize> = HashMap::new();

    for i in 1..N+1 {
        let l = i % 10;
        let mut r = i;
        while r >= 10 {
            r /= 10;
        }
        *cnt.entry((l, r)).or_insert(0) += 1;
    }

    let mut ans = 0;
    for &(l, r) in cnt.keys() {
        ans += cnt.get(&(r, l)).unwrap_or(&0) * cnt.get(&(l, r)).unwrap_or(&0);
    }

    println!("{}", ans);
}
