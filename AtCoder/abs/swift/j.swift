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


var S: String = ""
cin >>> S
S = String(S.reversed())

let words: [String] = ["dream", "dreamer", "erase", "eraser"]
var revWords: [String] = []

for w in words {
    revWords.append(String(w.reversed()))
}

var t: String = ""
for s in S {
    t.append(s)
    if revWords.contains(t) {
        t = ""
    }
}
print(t.count == 0 ? "YES" : "NO")
