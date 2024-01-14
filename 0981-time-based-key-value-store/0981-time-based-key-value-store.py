from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        
        self.data = {} 
        # key : [list of values with timestamp]
        
        # key : {timestamp : value, timestamp2 : value2}

        # key : [timestamp : value, timestamp2 : value2]

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.data:

            self.data[key] = SortedDict()

        self.data[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.data : return ""

        # timestamps = list(self.data[key].keys())

        index = bisect.bisect_right(self.data[key].keys(), timestamp)

        print(index, self.data[key])

        if index == 0 :

            return ""

        return self.data[key].peekitem(index-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)