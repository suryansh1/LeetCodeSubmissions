from collections import deque

class MinStack:

    def __init__(self):
        self.data = deque()
        self.isEmpty = True

    def push(self, val: int) -> None:

        if self.isEmpty :
            self.data.append([val, val])
            self.isEmpty = False
            return

        if val < self.data[-1][1]:
            self.data.append([val, val])

        else :
            self.data.append([val, self.data[-1][1]])
                 

    def pop(self) -> None:
        
        self.data.pop()

        if len(self.data) == 0 : self.isEmpty = True

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()