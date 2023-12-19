class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums))
        
#         mySet = set()
        
#         for num in nums:
            
#             if num in mySet: return True
            
#             mySet.add(num)
            
#         return False