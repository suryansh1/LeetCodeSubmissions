class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        indexOfLastZero = 0

        for i, val in enumerate(nums):
            if val != 0:
                
                if indexOfLastZero == i:
                    indexOfLastZero+=1
                
                else:
                    nums[indexOfLastZero] = val
                    indexOfLastZero +=1

        # for i in range(indexOfLastZero, len(nums)): nums[i] = 0

        for i, val in enumerate(nums[indexOfLastZero:]):
            # if not val:
            nums[indexOfLastZero + i] = 0

        return nums

        ## Moving zeros like below doesn't work
        # because when swapping first zero with last element
        # does not preserve order

        # l, r = 0, len(nums) - 1

        # while (l < r):

        #     if nums[l] != 0:
        #         l+=1

        #     if nums[r] == 0:
        #         r-=1

        #     if l >= r : break

        #     nums[l], nums[r] = nums[r], nums[l]

        #     print(l, r, nums)

        # return nums



