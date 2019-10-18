#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
use std::collections::{BTreeMap, BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};
use std::cmp::{max, min, Ordering};

macro_rules! get {
    ($t:ty) => {
        {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            line.trim().parse::<$t>().unwrap()
        }
    };
    ($($t:ty),*) => {
        {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            (
                $(iter.next().unwrap().parse::<$t>().unwrap(),)*
            )
        }
    };
    ($t:ty; $n:expr) => {
        (0..$n).map(|_|
            get!($t)
        ).collect::<Vec<_>>()
    };
    ($($t:ty),*; $n:expr) => {
        (0..$n).map(|_|
            get!($($t),*)
        ).collect::<Vec<_>>()
    };
    ($t:ty ;;) => {
        {
            let mut line: String = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            line.split_whitespace()
                .map(|t| t.parse::<$t>().unwrap())
                .collect::<Vec<_>>()
        }
    };
    ($t:ty ;; $n:expr) => {
        (0..$n).map(|_| get!($t ;;)).collect::<Vec<_>>()
    };
}

// N M => let (N, M) = get!(usize, usize)
// A1 B1
// ...
// AQ BQ => let A = get!(usize, usize; Q)

const MOD: u64 = 1000000007;

fn main() {
    let (K, A, B) = get!(usize, usize, usize);

    // 1ターンで1枚増やす
    // A+2ターンでB枚増やす
    let mut ans: usize = 1;
    let mut turn = 0;

    while turn < K {
        if ans < A || turn >= K - 1 {
            ans += 1;
        } else {
            let change = ans - A + B;
            let noChange = ans + 2;
            ans = max(change, noChange);
            turn += 1;
        }
        turn += 1;
    }

    println!("{}", ans);
}
