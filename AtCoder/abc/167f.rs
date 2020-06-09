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
        S: [String; N],
    }

    let mut A = vec![];
    for s in &S {
        let (mut cum, mut mi): (i64, i64) = (0, 0);
        for t in s.chars() {
            if t == '(' {
                cum += 1;
            } else {
                cum -= 1;
            }
            mi = min(mi, cum);
        }
        A.push((-mi, cum - mi));
    }

    let mut P: Vec<(i64, i64)> = A.iter().filter(|(l, r)| *l <= *r).cloned().collect();
    let mut N: Vec<(i64, i64)> = A.iter().filter(|(l, r)| *l > *r).cloned().collect();

    P.sort_by(|l, r| l.0.cmp(&r.0));
    N.sort_by(|l, r| l.1.cmp(&r.1));
    N.reverse();

    let mut M: i64 = 0;

    for (l, r) in &P {
        M -= l;
        if M < 0 {
            println!("No");
            return;
        }
        M += r;
    }
    for (l, r) in &N {
        M -= l;
        if M < 0 {
            println!("No");
            return;
        }
        M += r;
    }

    if M == 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
