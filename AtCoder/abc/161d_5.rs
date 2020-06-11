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
        K: usize,
    }

    let mut ans = vec![];
    let mut que = VecDeque::new();
    for i in 1..10 {
        que.push_back(i as i64);
    }

    while ans.len() <= K {
        let mut num = que.pop_front().unwrap();
        ans.push(num);

        let d = num % 10;
        num *= 10;
        for i in max(0, d - 1)..min(10, d + 2) {
            que.push_back(num + i);
        }
    }

    println!("{}", ans[K - 1]);
}
