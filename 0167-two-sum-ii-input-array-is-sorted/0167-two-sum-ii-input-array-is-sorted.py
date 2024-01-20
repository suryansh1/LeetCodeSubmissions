class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        size = len(numbers)

        for i, num in enumerate(numbers):

            x = target - num

            index2 = bisect.bisect_left(numbers[i+1:], x)

            # print(i, num, index2, index2 + i + 1)

            if index2 + i + 1 == size : index2 -= 1
            
            if numbers[index2+i+1] == x : return i+1, i+index2+2
