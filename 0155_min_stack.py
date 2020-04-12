class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self._stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if len(self._stack) > 0:
            if self._stack[-1] == self.min:
                if len(self._stack) == 1:
                    self.min = float('inf')
                else:
                    self.min = min(self._stack[:-1])
            del self._stack[-1]

    def top(self) -> int:
        if len(self._stack) > 0:
            return self._stack[-1]

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(5)
    obj.push(4)
    obj.pop()
    assert obj._stack == [5]
    param_3 = obj.top()
    assert param_3 == 5
    param_4 = obj.getMin()
    assert param_4 == 5
