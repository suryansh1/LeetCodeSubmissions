class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        insert_index = bisect.bisect_left(nums, target)

        return -1 if (insert_index == len(nums) or nums[insert_index] != target) else insert_index

        # return insert_index if nums[insert_index] == target else -1