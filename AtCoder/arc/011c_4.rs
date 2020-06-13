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

fn canMove(fr: &str, to: &str) -> bool {
    let mut cnt = 0;
    for (s, t) in fr.chars().zip(to.chars()) {
        if s != t {
            cnt += 1;
        }
    }
    return cnt <= 1;
}

fn main() {
    input! {
        first: String,
        last: String,
        N: usize,
        A: [String; N],
    }

    if canMove(&first, &last) {
        println!("0");
        println!("{}", first);
        println!("{}", last);
        return;
    }

    let mut sToI = HashMap::new();
    sToI.insert(&first, 0);
    sToI.insert(&last, 1);
    for (i, a) in A.iter().enumerate() {
        sToI.insert(a, i + 2);
    }

    let mut iToS = vec![""; N + 2];
    for (a, i) in sToI.iter() {
        iToS[*i] = *a;
    }

    let mut edges = vec![vec![]; N + 2];
    for fr in sToI.keys() {
        for to in sToI.keys() {
            if canMove(fr, to) {
                edges[sToI[fr]].push(sToI[to]);
            }
        }
    }

    let mut minDist = vec![INF; N + 2];
    let mut parent = vec![INF; N + 2];
    let mut que = VecDeque::new();
    minDist[sToI[&first]] = 0;
    que.push_back(sToI[&first]);

    while !que.is_empty() {
        let now = que.pop_front().unwrap();
        for &to in &edges[now] {
            if minDist[to] > minDist[now] + 1 {
                minDist[to] = minDist[now] + 1;
                parent[to] = now;
                que.push_back(to);
            }
        }
    }

    if minDist[sToI[&last]] == INF {
        print!("-1");
        return;
    }

    let mut now = sToI[&last];
    let mut ans = vec![];
    ans.push(now);

    while now != sToI[&first] {
        now = parent[now];
        ans.push(now);
    }

    println!("{}", ans.len() - 2);
    for &a in ans.iter().rev() {
        println!("{}", iToS[a]);
    }
}
