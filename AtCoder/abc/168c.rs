#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_assignments)]
use proconio::input;
use std::collections::*;
use std::cmp::*;
use std::f64::consts::*;

const MOD: u64 = 1000000007;

fn main() {
    input! {
        A: f64,
        B: f64,
        H: f64,
        M: f64
    };

    let thetaH = (H / 12. + M / 60. / 12.) * PI * 2.;
    let thetaM = M / 60. * PI * 2.;

    let (hX, hY) = (thetaH.cos() * A, thetaH.sin() * A);
    let (mX, mY) = (thetaM.cos() * B, thetaM.sin() * B);

    let (dx, dy) = (hX - mX, hY - mY);

    println!("{}", (dx * dx + dy * dy).sqrt());
}