class Solution(object):

    def twoSumBruteForce(self, nums, target):
        index1 = index2 = 0
        size = len(nums)
        
        for index1 in range(size):

            for index2 in range(index1+1, size):

                if nums[index1] + nums[index2] == target:
                    return index1, index2

    def twoSumDictionary(self, nums, target):
        
        myDict = {}

        for index in range(len(nums)):
            
            myDict[nums[index]] = index

        for index1 in range(len(nums)):

            if (target - nums[index1]) in myDict:

                index2 = myDict[target - nums[index1]]

                if index1 != index2:
                    return index1, index2

    def twoSumDictOptimized(self, nums, target):
        
        myDict = {}

        for index1, num in enumerate(nums):

            if target - num in myDict:

                index2 = myDict[target - num]

                # if index1 != index2:
                return index1, index2

            myDict[num] = index1


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # return self.twoSumBruteForce(nums, target)
        return self.twoSumDictionary(nums, target)
        # return self.twoSumDictOptimized(nums, target)
            
        