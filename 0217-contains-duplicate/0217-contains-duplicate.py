class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        c = collections.Counter(nums)
        return any(c[k] > 1 for k in c.keys())