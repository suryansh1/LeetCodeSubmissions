from collections import Counter

class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        
        # counter = Counter(nums)

        # return counter.most_common(1)[0][0]

        count = 0

        majority_element = nums[0]

        for i, num in enumerate(nums):

            if num == majority_element:

                count +=1

            else :

                count -=1

                if count == 0 : 
                    majority_element = num
                    count = 1

        return majority_element
    