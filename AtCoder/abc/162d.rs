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
use std::f64::consts::*;

const MOD: i64 = 1000000007;
const INF: usize = std::usize::MAX / 4;

fn main() {
    input! {
        N: usize,
        S: Chars,
    }

    let R = S.iter().filter(|&&s| s == 'R').count();
    let G = S.iter().filter(|&&s| s == 'G').count();
    let B = S.iter().filter(|&&s| s == 'B').count();

    let mut ans = R * G * B;

    for i in 0..N {
        for k in i+1..N {
            let j2 = i + k;
            if j2 % 2 == 1 {
                continue;
            }

            let (si, sj, sk) = (S[i], S[j2 / 2], S[k]);

            if si != sj && sj != sk && sk != si {
                ans -= 1;
            }
        }
    }

    println!("{}", ans);
}
