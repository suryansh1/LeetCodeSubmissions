class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        c = collections.Counter(nums)
        return any(val > 1 for k,val in c.items())