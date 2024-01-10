class Solution:

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:

        for i, num1 in enumerate(nums):

            for j, num2 in enumerate(nums[i+1:]):

                if num1 + num2 == target: return (i, i+j+1)

    def twoSumHashTable(self, nums: List[int], target: int) -> List[int]:

        myDict = {}

        for i, num in enumerate(nums) :
            myDict[num] = i

        for i, num in enumerate(nums) :

            if (target - num) in myDict:

                if myDict[target - num] != i : 
                    
                    return i, myDict[target - num]
    
    def twoSumSinglePassHashTable(self, nums: List[int], target: int) -> List[int]:

        myDict = {}

        for i, num in enumerate(nums):

            if (target - num) in myDict :

                return i, myDict[target - num]

            else : myDict[num] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # return self.twoSumBruteForce(nums, target)

        # return self.twoSumHashTable(nums, target)

        # return self.twoSumSinglePassHashTable(nums, target)

        myDict = {}

        for i,num in enumerate(nums) :

            if target - num in myDict :

                return i, myDict[target - num]

            else : myDict[num] = i