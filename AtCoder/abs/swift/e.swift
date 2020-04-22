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


var (A, B, C, X): (Int, Int, Int, Int) = (0, 0, 0, 0)
cin >>> A >>> B >>> C >>> X

var ans: Int = 0
for a in 0...A {
    for c in 0...C {
        var b: Int = X - a * 500 - c * 50

        if b % 100 != 0 {
            continue
        }

        b /= 100

        if 0 <= b && b <= B {
            ans += 1
        }
    }
}

print(ans)
