class Solution:
    
    def containsNearbyDuplicates2dDict (self, nums: List[int], k: int) -> bool:
        
        myDict = {}
        
        for i, num in enumerate(nums) :
            
            if num not in myDict :
                myDict[num] = [i]
                
            else : 
                
                if i - myDict[num][-1] <= k : return True
                
                myDict[num].append(i)
                
        return False
        
    def containsNearbyDuplicatesSetK (self, nums: List[int], k: int) -> bool:
        
        mySet = set()
        
        for i, num in enumerate(nums):
            
            if num in mySet :
                return True
            
            mySet.add(num)
            
            if len(mySet) > k:
                mySet.remove(nums[i-k])
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        return self.containsNearbyDuplicatesSetK(nums, k)
    
    
        
        
        