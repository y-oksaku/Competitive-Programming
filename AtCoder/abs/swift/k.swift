import Foundation
infix operator >>> : MultiplicationPrecedence
extension String {
    func substring(_ r: CountableRange<Int>) -> String {

        let length = self.count
        let fromIndex = (r.startIndex > 0) ? self.index(self.startIndex, offsetBy: r.startIndex) : self.startIndex
        let toIndex = (length > r.endIndex) ? self.index(self.startIndex, offsetBy: r.endIndex) : self.endIndex

        if fromIndex >= self.startIndex && toIndex <= self.endIndex {
            return String(self[fromIndex..<toIndex])
        }

        return String(self)
    }

    func substring(_ r: CountableClosedRange<Int>) -> String {

        let from = r.lowerBound
        let to = r.upperBound

        return self.substring(from..<(to+1))
    }

    func substring(_ r: CountablePartialRangeFrom<Int>) -> String {

        let from = r.lowerBound
        let to = self.count

        return self.substring(from..<to)
    }

    func substring(_ r: PartialRangeThrough<Int>) -> String {

        let from = 0
        let to = r.upperBound

        return self.substring(from..<to)
    }
}

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

func isOk() -> Bool {
    var N : Int = 0
    cin >>> N

    var T = [Int](repeating: 0, count: N)
    var X = [Int](repeating: 0, count: N)
    var Y = [Int](repeating: 0, count: N)

    for i in 0..<N {
        cin >>> T[i] >>> X[i] >>> Y[i]
    }

    var (time, x, y) : (Int, Int, Int) = (0, 0, 0)
    for i in 0..<N {
        let dt : Int = T[i] - time
        let dx : Int = X[i] - x
        let dy : Int = Y[i] - y

        let dist : Int = abs(dx) + abs(dy)
        if dt < dist {
            return false
        }

        if dist % 2 != dt % 2 {
            return false
        }

        time = T[i]
        x = X[i]
        y = Y[i]
    }
    return true
}

print(isOk() ? "Yes" : "No")
