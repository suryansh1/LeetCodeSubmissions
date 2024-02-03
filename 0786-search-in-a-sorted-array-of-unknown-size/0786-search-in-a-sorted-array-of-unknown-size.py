# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        # Start from index 0

        if reader.get(0) == target : return 0

        i = 1

        upperBound = reader.get(i)

        while (upperBound < target):
            
            i *= 2

            upperBound = reader.get(i)

        low, high = i//2, i

        while(low <= high) :

            mid = low + (high - low)//2

            midVal = reader.get(mid)

            if midVal == target :

                return mid

            elif target < midVal : high = mid - 1

            else : low = mid + 1

        return -1 



        