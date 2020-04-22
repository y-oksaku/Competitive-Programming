import Foundation
infix operator >>> : MultiplicationPrecedence

class Input {
    var inputs : [String] = [];

    func read() {
        self.inputs = readLine()!.components(separatedBy: " ")
        self.inputs.reverse()
    }

    func pop() -> (String) {
        if self.inputs.count == 0 {
            self.read()
        }
        return self.inputs.popLast()!
    }

    static func >>> (cin : Input, right : inout Int) -> (Input) {
        right = Int(cin.pop())!
        return cin
    }
    static func >>> (cin : Input, right : inout String) -> (Input) {
        right = cin.pop()
        return cin
    }
}
let cin = Input()

var (N, A, B): (Int, Int, Int) = (0, 0, 0)
cin >>> N >>> A >>> B

var ans: Int = 0

func digitSum(_ n: Int) -> Int {
    var (n, ret): (Int, Int) = (n, 0)
    while n > 0 {
        ret += n % 10
        n /= 10
    }
    return ret
}

for i in 1...N {
    let d: Int = digitSum(i)
    if A <= d && d <= B {
        ans += i
    }
}

print(ans)
