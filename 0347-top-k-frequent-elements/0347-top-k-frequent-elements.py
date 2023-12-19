from collections import Counter

class Solution:
    
    def topKFrequentDictDelete(self, nums: List[int], k: int) -> List[int]:
    
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
            
            # Deletion in dict is O(n), as elements need to be shifted          
            del(myDict[key])
            
        return ret
        
    def topKFrequentDictSort(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}
        
        for num in nums:
            
            if num not in myDict:
                myDict[num] = 1
                
            else :
                myDict[num] += 1
                
        return sorted(myDict, key=myDict.get, reverse=True)[:k]

    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        
        return [key for key, val in counter.most_common(k)]

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        
        import heapq

        myDict = {}
        
        for num in nums:
            
            if num not in myDict:
                myDict[num] = 1
                
            else :
                myDict[num] += 1
                
        return heapq.nlargest(k, myDict, key=myDict.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # return self.topKFrequentDictDelete(nums, k)
        
        # return self.topKFrequentDictSort(nums, k)
        
        # return self.topKFrequentCounter(nums, k)
    
        return self.topKFrequentHeap(nums, k)