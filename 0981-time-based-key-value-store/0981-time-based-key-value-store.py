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

        # index = bisect.bisect_left(timestamps, timestamp)

        index = self.data[key].bisect_right(timestamp)

        print(index-1, self.data[key])

        if index == 0 : return ""

            # if timestamp < timestamps[0] : return ""
        
        # if index == len(timestamps) : 
            
        #     index -= 1

        # if timestamp < timestamps[index] :

        #     index -= 1


        # print(index, timestamp, timestamps, self.data[key])

        # return self.data[key][timestamps[index]]

        return self.data[key].peekitem(index-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)