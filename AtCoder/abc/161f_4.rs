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

fn divisors(N: u64) -> Vec<u64> {
    let mut ret = vec![];

    let mut d = 1;
    while d * d <= N {
        if N % d == 0 {
            ret.push(d);
            let m = N / d;
            if m != d {
                ret.push(m);
            }
        }
        d += 1;
    }

    return ret;
}

fn main() {
    input! {
        N: u64,
    }

    let mut V = HashSet::new();
    for d in divisors(N) {
        if d == 1 {
            continue;
        }
        let mut M = N;
        while M % d == 0 {
            M /= d;
        }
        M %= d;
        if M == 1 {
            V.insert(d);
        }
    }
    for d in divisors(N - 1) {
        if d == 1 {
            continue;
        }
        let mut M = N;
        while M % d == 0 {
            M /= d;
        }
        M %= d;
        if M == 1 {
            V.insert(d);
        }
    }

    println!("{}", V.len());
}
