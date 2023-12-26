class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # c = collections.Counter(nums)
        
        return collections.Counter(nums).most_common(1)[0][1] > 1
        # return any(val > 1 for k,val in c.items())