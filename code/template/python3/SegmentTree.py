INF = float('inf')

class SegmentTree:
    def __init__(self, size):
        self._size = (1 << size.bit_length())
        self._data = [INF] * (self._size * 2)

    def update(self, index, value):
        index += self._size - 1
        self._data[index] = value
        while index > 0:
            index = (index - 1) // 2
            self._data[index] = min(self._data[index * 2 + 1], self._data[index * 2 + 2])

    def __query(self, qLeft, qRight, node, left, right):
        if right <= qLeft or qRight <= left:
            return INF
        if qLeft <= left and right <= qRight:
            return self._data[node]

        leftVal = self.__query(qLeft, qRight, node * 2 + 1, left, (left + right) // 2)
        rightVal = self.__query(qLeft, qRight, node * 2 + 2, (left + right) // 2, right)
        return min(leftVal, rightVal)

    # [left, right)
    def query(self, left, right):
        return self.__query(left, right, 0, 0, self._size)