class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # left, right = 0, len(numbers) - 1

        # while (left <= right):

        #     if numbers[left] + numbers[right] == target :
        #         return [left+1, right+1]

        #     if target < numbers[left] + numbers[right] : 
        #         right -= 1

        #     # elif target > numbers[left] :
        #     else : 
        #         left += 1

        # return [0,0]

        hashtable = {}
        
        for i,val in enumerate(numbers,start=1):
                      
            if (target - val) in hashtable :
                
                # if hashtable[target-val] != i:
                
                return hashtable[target-val], i
            
            hashtable[val] = i