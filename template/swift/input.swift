import Foundation
infix operator >>>: MultiplicationPrecedence
protocol Initializable {
    init?(_ description: String)
}
extension Int: Initializable {}
extension String: Initializable {}

class Input {
    var inputs: [String] = [];

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

    @discardableResult
    static func >>><T: Initializable> (cin: Input, right: inout T) -> (Input) {
        right = T.init(cin.pop())!
        return cin
    }

    @discardableResult
    static func >>><T: Initializable> (cin: Input, right: inout [T]) -> (Input) {
        for i in 0..<right.count {
            right[i] = T.init(cin.pop())!
        }
        return cin
    }
}
let cin = Input()