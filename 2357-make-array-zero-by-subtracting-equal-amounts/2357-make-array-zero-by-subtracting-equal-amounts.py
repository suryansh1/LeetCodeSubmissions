class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        mySet = set()
        
        for num in nums :
            if num >0 and num not in mySet :
                mySet.add(num)
                
        return len(mySet)
        
        
        
############## Slow method by Performing Operations #############        
#         x = 101
        
#         operations = 0
        
#         while (1):
            
#             x = 101
            
#             # Finding min and assigning to x
#             for num in nums :

#                 if num > 0 :
#                     if num < x : 
#                         x = num 
                        
#             if x == 101 : return operations
                  
            
#             flag = 0
            
#             # Subtracting x from each element                    
#             for i, num in enumerate(nums):

#                 if num > 0:
#                     nums[i]-=x
                    
#                     if nums[i]!=0 : 
#                         flag = 1
                        
#             operations +=1
            
#             if not flag : return operations
                            
            