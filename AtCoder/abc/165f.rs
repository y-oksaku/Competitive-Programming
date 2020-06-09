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

fn upper_bound(A: &Vec<usize>, x: usize) -> usize {
    let (mut l, mut r): (i64,i64) = (-1, A.len() as i64);

    while r - l > 1 {
        let mid = (l + r) / 2;
        if A[mid as usize] >= x {
            r = mid;
        } else {
            l = mid;
        }
    }
    return r as usize;
}

fn search(ans: &mut Vec<usize>, now: usize, pr: usize, edges: &Vec<Vec<usize>>, A: &Vec<usize>, dp: &mut Vec<usize>) {
    ans[now] = upper_bound(dp, INF - 1);

    for &to in &edges[now] {
        if to == pr {
            continue;
        }
        let i = upper_bound(dp, A[to]);
        let old = dp[i];
        dp[i] = A[to];
        search(ans, to, now, edges, A, dp);
        dp[i] = old;
    }
}

fn main() {
    input! {
        N: usize,
        A: [usize; N],
    }

    let mut edges = vec![vec![]; N];
    for _ in 0..N-1 {
        input! {
            fr: Usize1,
            to: Usize1,
        }
        edges[fr].push(to);
        edges[to].push(fr);
    }

    let mut dp = vec![INF; N];
    dp[0] = A[0];
    let mut ans = vec![0; N];
    search(&mut ans, 0, 0, &edges, &A, &mut dp);

    for &a in &ans {
        println!("{}", a);
    }
}
