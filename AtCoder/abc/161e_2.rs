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
        N: usize,
        K: usize,
        C: usize,
        S: Chars,
    }

    let mut L = vec![0; N + 1];
    let mut R = vec![0; N + 1];

    let mut now = 1;
    while now <= N {
        if S[now - 1] == 'o' {
            L[now] += 1;
            now += C + 1;
        } else {
            now += 1;
        }
    }
    for i in 0..N {
        L[i + 1] += L[i];
    }

    now = 1;
    while now <= N {
        if S[N - now] == 'o' {
            R[N - now] += 1;
            now += C + 1;
        } else {
            now += 1;
        }
    }
    for i in (0..N).rev() {
        R[i] += R[i + 1];
    }

    for i in 1..N+1 {
        if S[i - 1] == 'o' && L[i] + R[i] == K && L[i] != L[i - 1] && R[i] != R[i - 1] {
            println!("{}", i);
        }
    }
}
