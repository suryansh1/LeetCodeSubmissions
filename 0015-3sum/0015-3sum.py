class Solution:

    def threeSum2pointers(self, nums: List[int]) -> List[List[int]]:

        size = len(nums)

        answerSet = set()

        answer = {}

        for i, num in enumerate(nums):

            target = 0 - num

            myDict = {}

            # We need to search for indices which sum to target in nums[i:]
            # find j,k in nums[i:] such that nums[j] + nums[k] = target

            for j in range(i+1, size) :

                if target - nums[j] not in myDict :

                   myDict[nums[j]] = j

                elif myDict[target - nums[j]] != j: 
                    
                    k = myDict[target - nums[j]]

                    # answerSet.add(tuple(sorted([nums[i], nums[j], nums[k]])))

                    key = tuple(sorted([nums[i], nums[j], nums[k]]))

                    if key not in answer :

                        answer[key] = [nums[i], nums[j], nums[k]]

   
        return answer.values()



    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        return self.threeSum2pointers(nums)