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
const INF: i64 = std::i64::MAX / 4;

fn main() {
    input! {
        N: usize,
        M: usize,
    }

    let mut edges = vec![vec![]; N];

    for _ in 0..M {
        input! {
            fr: Usize1,
            to: Usize1,
            D: i64,
        }
        edges[fr].push((to, D));
        edges[to].push((fr, -D));
    }

    let mut minDist = vec![INF; N];
    for s in 0..N {
        if minDist[s] < INF {
            continue;
        }
        let mut que = VecDeque::new();
        que.push_back(s);
        minDist[s] = 0;

        while !que.is_empty() {
            let now = que.pop_front().unwrap();
            let dist = minDist[now];

            for &(to, d) in &edges[now] {
                if minDist[to] == INF {
                    minDist[to] = dist + d;
                    que.push_back(to);
                } else {
                    if minDist[to] != dist + d {
                        println!("No");
                        return;
                    }
                }
            }
        }
    }

    println!("Yes");
}
