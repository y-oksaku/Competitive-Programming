class BIT:
    """
    1-indexed
    """
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def add(self, index, value=1):
        while index <= self.size:
            self.data[index] += value
            index += index & (-index)

    def sum(self, index):
        """
        右端含める
        """
        ret = 0
        while index:
            ret += self.data[index]
            index -= index & (-index)
        return ret

    def search(self, val):
        """
        x_1 + ... x_i >= val を満たす最小のi
        """
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)  # 一番上の長さ

        while step:
            if i + step <= self.size and s + self.data[i + step] < val:
                i += step
                s += self.data[i]
            step //= 2
        return i + 1
