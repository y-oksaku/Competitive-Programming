#![allow(unused_imports)]
#![allow(unused_macros)]
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_assignments)]
use std::collections::{BTreeMap, BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};
use std::cmp::{max, min, Ordering};

const MOD: u64 = 1000000007;

fn main() {
    let mut cin = Input::new();

    let mut N: usize = 0;
    cin = cin >> &mut N;

    N %= 10;
    if N == 2 || N == 4 || N == 5 || N == 7 || N == 9 {
        println!("hon");
    }
    if N == 0 || N == 1 || N == 6 || N == 8 {
        println!("pon");
    }
    if N == 3 {
        println!("bon");
    }
}

struct Input {
    data: Vec<String>,
}

impl Input {
    pub fn new() -> Input {
        Input{data: Vec::new()}
    }

    fn read(&mut self) {
        let mut line: String = String::new();
        std::io::stdin().read_line(&mut line).unwrap();
        self.data = line.split_whitespace().rev().map(|s| s.parse::<String>().unwrap()).collect::<Vec<_>>();
    }

    pub fn get<T: core::str::FromStr>(&mut self) -> T {
        if self.data.len() == 0 {
            self.read();
        }
        return self.data.pop().unwrap().parse::<T>().ok().unwrap();
    }
}

impl<T: core::str::FromStr> std::ops::Shr<&mut T> for Input {
    type Output = Input;

    fn shr(mut self, rhs: &mut T) -> Input {
        *rhs = self.get::<T>();
        return self;
    }
}
