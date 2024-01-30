class MovingAverage:

    def __init__(self, size: int):

        self.window_size = size

        self.window = deque()

        self.curSum = 0

        self.curAvg = 0

    def next(self, val: int) -> float:            

        self.window.append(val)

        if len(self.window) <= self.window_size :

            self.curSum += val
            self.curAvg = self.curSum/len(self.window)

            return self.curAvg
        
        diff = val - self.window.popleft() 
        # self.curSum += diff
        self.curAvg += diff/self.window_size

        return self.curAvg




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)