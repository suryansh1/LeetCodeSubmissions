# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        # Start from index 0

        # expand search window 2x
        # if target < ArrayReader.get(i)

            # target is between index 2^i-1 and 2 ^ i
            # binary search with low = 2^i-1 and high = 2^i

        # else i += 1

        i = 1

        upperBound = reader.get(i)

        while (target > upperBound):
            
            i *= 2

            upperBound = reader.get(i)

            if upperBound == pow(2, 31) - 1 :

                break

        # handle cases where target is less than lowest val 

        if i == 0 :
            
            if reader.get(0) == target : return 0
            else : return -1

        # and target > highest val

        low, high = 0, i

        while(low <= high) :

            mid = low + (high - low)//2

            midVal = reader.get(mid)

            if midVal == target :

                return mid

            elif target < midVal : high = mid - 1

            else : low = mid + 1

        return -1 



        