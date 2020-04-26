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

fn main() {
    let mut cin = Input::new();

    let (mut a, mut b, mut c) = (0, 0, 0);
    let mut s = String::new();
    cin = cin >> &mut a >> &mut b >> &mut c >> &mut s;

    println!("{} {} {} {}", a, b, c, s);
}
