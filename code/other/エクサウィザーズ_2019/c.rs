#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
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

const MOD: u64 = 1000000007;

// N M => let (N, M) = get!(usize, usize)
// A1 B1
// ...
// AQ BQ => let A = get!(usize, usize; Q)

fn main() {
    let (N, Q) = get!(usize, usize);
    let S = get!(String).chars().collect();
    let TD = get!(String, String; Q);

    let mut ok: isize = -1;
    let mut ng: isize = N as isize;
    while ng - ok > 1 {
        let mid: isize = (ok + ng) / 2;
        if isOkLeft(N, &S, mid, &TD) {
            ok = mid;
        } else {
            ng = mid
        }
    }
    let left: isize = ng;

    ok = N as isize;
    ng = -1 as isize;
    while ok - ng > 1 {
        let mid: isize = (ok + ng) / 2;
        if isOkRight(N, &S, mid, &TD) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    let right: isize = (N as isize) - ok;

    println!("{}", N - ((left + right) as usize));
}

fn isOkLeft(N: usize, S: &Vec<char>, mid: isize, TD: &Vec<(String, String)>) -> bool {
    let mut now: isize = mid as isize;

    for td in TD.iter() {
        if S[now as usize].to_string() == td.0 {
            if td.1 == "L" {
                now -= 1;
            } else {
                now += 1;
            }
        }

        if now < 0 {
            return true;
        }

        if (now as usize) >= N {
            return false;
        }
    }

    false
}

fn isOkRight(N: usize, S: &Vec<char>, mid: isize, TD: &Vec<(String, String)>) -> bool {
    let mut now: isize = mid as isize;

    for td in TD.iter() {
        if S[now as usize].to_string() == td.0 {
            if td.1 == "L" {
                now -= 1;
            } else {
                now += 1;
            }
        }

        if now < 0 {
            return false;
        }

        if (now as usize) >= N {
            return true;
        }
    }

    false
}