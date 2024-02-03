class Solution:

    def binarySearch(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high :

            mid = low + (high - low)//2

            if target == nums[mid] : return mid

            elif target < nums[mid] : high = mid - 1

            else : low = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:

        return self.binarySearch(nums, target)
        
        index = bisect.bisect_left(nums, target)        
        
        if index == len(nums) : return -1

        if nums[index] == target : return index

        return -1