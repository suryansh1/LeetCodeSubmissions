class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i, val in enumerate(nums[:-1]):

            # print(nums)
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0


        # return sorted(nums, key=lambda x: x == 0)

        indexOfLastZero = 0

        for i, val in enumerate(nums):
            if val != 0:
                
                if indexOfLastZero == i:
                    indexOfLastZero+=1
                
                else:
                    nums[indexOfLastZero] = val
                    indexOfLastZero +=1

        for i in range(indexOfLastZero, len(nums)): nums[i] = 0

        return nums


