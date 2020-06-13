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
        mut B: [Usize1; N],
    }

    let mut ans = vec![];
    while B.len() > 0 {
        let mut isDeleted = false;
        for i in (0..B.len()).rev() {
            if B[i] == i {
                B.remove(i);
                ans.push(i + 1);
                isDeleted = true;
                break;
            }
        }
        if !isDeleted {
            println!("-1");
            return;
        }
    }

    for &a in ans.iter().rev() {
        println!("{}", a);
    }
}
