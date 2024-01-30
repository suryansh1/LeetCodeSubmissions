class MovingAverage:

    def __init__(self, size: int):

        self.window_size = size

        self.window = deque()
        # self.window = []        

    def next(self, val: int) -> float:
        
        if len(self.window) == self.window_size:
            self.window.popleft()            

        self.window.append(val)

        if len(self.window) < self.window_size :

            return sum(self.window)/len(self.window)

        
        return sum(self.window)/self.window_size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)