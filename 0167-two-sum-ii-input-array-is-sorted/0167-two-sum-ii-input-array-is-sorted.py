class Solution:

    def twoSum2pointers(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while (left <= right):

            if numbers[left] + numbers[right] == target :
                return [left+1, right+1]

            if target < numbers[left] + numbers[right] : 
                right -= 1

            # elif target > numbers[left] :
            else : 
                left += 1

        return [0,0]

    def twoSumDict(self, numbers: List[int], target: int) -> List[int]:

        hashtable = {}
        
        for i,val in enumerate(numbers,start=1):
                      
            if (target - val) in hashtable :
                                
                return hashtable[target-val], i
            
            hashtable[val] = i

    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:

        size = len(numbers)

        for i, num in enumerate(numbers):

            x = target - num

            index2 = bisect.bisect_left(numbers[i+1:], x)

            if index2 + i + 1 == size : index2 -= 1

            if numbers[index2+i+1] == x : return i+1, i+index2+2


    def twoSum(self, numbers: List[int], target: int) -> List[int]:

            # return self.twoSum2pointers(numbers, target)
            # return self.twoSumBinarySearch(numbers, target)
            return self.twoSumDict(numbers, target)
