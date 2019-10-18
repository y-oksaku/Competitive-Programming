#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
use std::str::FromStr;
use std::cmp::PartialEq;

macro_rules! input {
    (source = $s:expr, $($r:tt)*) => {
        let mut iter = $s.split_whitespace();
        let mut next = || { iter.next().unwrap() };
        input_inner!{next, $($r)*}
    };
    ($($r:tt)*) => {
        let stdin = std::io::stdin();
        let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock()));
        let mut next = move || -> String{
            bytes
                .by_ref()
                .map(|r|r.unwrap() as char)
                .skip_while(|c|c.is_whitespace())
                .take_while(|c|!c.is_whitespace())
                .collect()
        };
        input_inner!{next, $($r)*}
    };
}

macro_rules! input_inner {
    ($next:expr) => {};
    ($next:expr, ) => {};

    ($next:expr, $var:ident : $t:tt $($r:tt)*) => {
        let $var = read_value!($next, $t);
        input_inner!{$next $($r)*}
    };
}

macro_rules! read_value {
    ($next:expr, ( $($t:tt),* )) => {
        ( $(read_value!($next, $t)),* )
    };

    ($next:expr, [ $t:tt ; $len:expr ]) => {
        (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>()
    };

    ($next:expr, chars) => {
        read_value!($next, String).chars().collect::<Vec<char>>()
    };

    ($next:expr, usize1) => {
        read_value!($next, usize) - 1
    };

    ($next:expr, $t:ty) => {
        $next().parse::<$t>().expect("Parse error")
    };
}

// N M
// input! {
//     N: i32,
//     M: i32,
// }

// N
// a1, ..., aN
// input! {
//     N: i32,
//     A: [i32, N],
// }

// H W
// a11 ... a1W
// ...
// aH1 ... aHW
// input! {
//     H: i32,
//     W: i32,
//     A: [[i32, W], H],
// }

// S
// input! {
//     S: chars,
// }

fn main() {
    input! {
        N: usize,
        S: chars,
    };

    let mut black = Vec::new();
    black.push(0);

    for (i, s) in S.iter().enumerate() {
        black.push(0);
        black[i + 1] = black[i];
        if *s == '#' {
            black[i + 1] += 1;
        }
    }

    let mut ans = N;
    for i in 0..N + 1 {
        let white = (N - i) - (black[N] - black[i]);
        ans = std::cmp::min(ans, black[i] + white);
    }

    println!("{}", ans);
}
