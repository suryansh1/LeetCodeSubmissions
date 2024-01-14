class Solution:


    def search(self, nums: List[int], target: int) -> int:
        
        # insert_index = bisect.bisect_left(nums, target)

        # return -1 if (insert_index == len(nums) or nums[insert_index] != target) else insert_index

        
        low, high = 0, len(nums) - 1

        while low <= high :
            mid = (low + high)//2

            if target == nums[mid] : return mid

            elif target < nums[mid] : high = mid - 1

            else : low = mid + 1

        return -1