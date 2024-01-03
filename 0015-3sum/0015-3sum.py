class Solution:

    def threeSum2pointers(self, nums: List[int]) -> List[List[int]]:

        size = len(nums)
        # List of dictionaries
        # [{1:2, 3:4}, {1:2, 5:3}]
        # dicts = []

        myDict = {}

        # Dict to store triplets to return
        answer = {}

        answerSet = set()

        size = len(nums)

        for i, num in enumerate(nums):

            target = 0 - num

            myDict = {}

            # We need to search for indices which sum to target in nums[i:]
            # find j,k in nums[i:] such that nums[j] + nums[k] = target

            for j in range(i+1, size) :

                # if target - nums[j] not in dicts[i] :

                if target - nums[j] not in myDict :

                   myDict[nums[j]] = j

                elif myDict[target - nums[j]] != j: 
                    
                    k = myDict[target - nums[j]]

                    answerSet.add(tuple(sorted([nums[i], nums[j], nums[k]])))

                    # key = str(sorted([nums[i], nums[j], nums[k]]))

                    # if key not in answer :

                    #     answer[key] = [nums[i], nums[j], nums[k]]

   
        return answerSet



    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        return self.threeSum2pointers(nums)