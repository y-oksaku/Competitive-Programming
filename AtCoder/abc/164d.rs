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
        S: String,
    }

    let A: Vec<u32> = S.chars().filter_map(|s| s.to_digit(10)).collect();

    let M: u32 = 2019;
    let mut cnt: Vec<u32> = vec![0; M as usize];
    let mut ans: u32 = 0;
    let mut cum: u32 = 0;
    let mut pwd: u32 = 1;

    cnt[0] = 1;
    for &a in A.iter().rev() {
        cum = (cum + pwd * a) % M;
        ans += cnt[cum as usize];
        cnt[cum as usize] += 1;
        pwd = pwd * 10 % M;
    }

    println!("{}", ans);
}
