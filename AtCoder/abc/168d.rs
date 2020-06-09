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
        AB: [(Usize1, Usize1); M],
    };

    let mut edges = vec![vec![]; N];

    for &(fr, to) in &AB {
        edges[fr].push(to);
        edges[to].push(fr);
    }

    let mut minDist = vec![INF; N];
    let mut ans = vec![N + 1; N];
    minDist[0] = 0;
    let mut que = VecDeque::new();
    que.push_back(0);

    while !que.is_empty() {
        let now = que.pop_front().unwrap();
        let dist = minDist[now];

        for &to in &edges[now] {
            if minDist[to] > dist + 1 {
                minDist[to] = dist + 1;
                ans[to] = now;
                que.push_back(to);
            }
        }
    }

    println!("Yes");
    for &a in &ans[1..N] {
        println!("{}", a + 1);
    }
}
