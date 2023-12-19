class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}
        
        for num in nums:
            
            if num not in myDict:
                myDict[num] = 1
                
            else :
                myDict[num] += 1
                
                
        ret = []
        
        for i in range(k):
            
            key = max(myDict, key=myDict.get)
            
            ret.append(key)
            
            del(myDict[key])
            
        return ret
