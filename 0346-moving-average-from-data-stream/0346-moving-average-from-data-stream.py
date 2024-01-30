class MovingAverage:

    def __init__(self, size: int):

        self.window_size = size

        self.window = deque()

        self.curSum = 0

        self.curAvg = 0

        # self.window = []        

    def next(self, val: int) -> float:
        
        # if len(self.window) == self.window_size:
        #     diff = val - self.window.popleft()            

        self.window.append(val)

        if len(self.window) <= self.window_size :

            self.curSum += val
            self.curAvg = self.curSum/len(self.window)

            return self.curAvg
            # return sum(self.window)/len(self.window)
        
        diff = val - self.window.popleft() 
        self.curSum += diff
        self.curAvg += diff/self.window_size

        return self.curAvg

        # return sum(self.window)/self.window_size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)