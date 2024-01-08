class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        mySet = {}

        for num in nums :

            if num not in mySet: mySet[num] = 1

        i = 0

        for val in mySet:

            nums[i] = val

            i+=1

        return len(mySet)
