class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        index = bisect.bisect_left(nums, target)        
        
        if index == len(nums) : return -1

        if nums[index] == target : return index

        return -1