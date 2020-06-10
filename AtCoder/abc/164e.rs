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
        S: usize,
    }

    let mut edges = vec![vec![]; N];
    let mut mx: usize = 0;

    for _ in 0..M {
        input! {
            fr: Usize1,
            to: Usize1,
            cost: i64,
            dist: i64,
        }
        edges[fr].push((to, -cost, dist));
        edges[to].push((fr, -cost, dist));
        mx += cost as usize;
    }

    for i in 0..N {
        input! {
            C: i64,
            D: i64,
        }
        edges[i].push((i, C, D));
    }

    let mut minDist = vec![vec![INF as i64; mx + 1]; N];
    let mut que = BinaryHeap::new();

    minDist[0][min(S, mx)] = 0;
    que.push((0, 0, min(S, mx) as i64));

    while !que.is_empty() {
        let (mut dist, now, cnt) = que.pop().unwrap();
        dist = -dist;

        if minDist[now][cnt as usize] < dist {
            continue;
        }

        for &(to, cost, d) in &edges[now] {
            if cnt + cost < 0 {
                continue;
            }
            let c: i64 = min(cnt + cost, mx as i64);
            if minDist[to][c as usize] > dist + d {
                minDist[to][c as usize] = dist + d;
                que.push((-(dist + d), to, c));
            }
        }
    }

    for i in 1..N {
        println!("{}", minDist[i].iter().min().unwrap());
    }
}
