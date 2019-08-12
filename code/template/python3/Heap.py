import heapq
class Heapq:
    def __init__(self, que=[], asc=True):
        if not asc:
            que = [-a for a in que]
        self.__que = que
        heapq.heapify(self.__que)
        self.__sign = 1 if asc else -1

    def pop(self):
        return heapq.heappop(self.__que) * self.__sign

    def push(self, value):
        heapq.heappush(self.__que, value * self.__sign)

    def pushpop(self, value):
        return heapq.heappushpop(self.__que, value * self.__sign) * self.__sign

    def top(self):
        return self.__que[0] * self.__sign

