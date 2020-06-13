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

fn add(cum: &mut Vec<usize>, w: usize, L: &Vec<usize>, S: &Vec<Vec<char>>) {
    for i in 0..(L.len() - 1) {
        let (t, b) = (L[i], L[i + 1]);
        for h in t..b {
            if S[h][w] == '1' {
                cum[i] += 1;
            }
        }
    }
}

fn main() {
    input! {
        H: usize,
        W: usize,
        K: usize,
        S: [Chars; H],
    }

    let mut ans = INF;

    for state in 0..(1 << (H - 1)) {
        let mut L = vec![0];
        for d in 0..(H - 1) {
            if (state & (1 << d)) != 0 {
                L.push(d + 1);
            }
        }
        L.push(H);

        let mut cnt = L.len() - 2;
        let mut cum = vec![0; L.len() - 1];

        for w in 0..W {
            add(&mut cum, w, &L, &S);
            if cum.iter().all(|&c| c <= K) {
                continue;
            }

            cnt += 1;
            cum = vec![0; L.len() - 1];
            add(&mut cum, w, &L, &S);
            if cum.iter().all(|&c| c <= K) {
                continue;
            }
            cnt = INF;
            break;
        }

        ans = min(ans, cnt);
    }

    println!("{}", ans);
}
