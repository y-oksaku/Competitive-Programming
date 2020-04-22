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

var N: Int = 0
cin >>> N

var ans: Int = 10000

for _ in 0..<N {
    var a: Int = 0
    cin >>> a

    var cnt: Int = 0
    while a > 0 && a % 2 == 0 {
        cnt += 1
        a /= 2
    }

    ans = min(ans, cnt)
}

print(ans)
