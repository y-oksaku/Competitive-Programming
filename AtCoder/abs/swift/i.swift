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

func sol() -> () {
    var (N, Y): (Int, Int) = (0, 0)
    cin >>> N >>> Y

    for man in 0...(Y / 10000) {
        for gosen in 0...(Y / 5000) {
            let sen: Int = (Y - man * 10000 - gosen * 5000) / 1000

            if sen < 0 {
                break
            }

            if sen + gosen + man == N {
                print(man, gosen, sen)
                return
            }
        }
    }
    print("-1 -1 -1")
    return
}

sol()
