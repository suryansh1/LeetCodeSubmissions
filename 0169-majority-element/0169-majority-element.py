from collections import Counter

class Solution:

    def majorityElementHashMap(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        return counter.most_common(1)[0][0]


    def majorityElementBoyerMoore(self, nums: List[int]) -> int:

        candidate = nums[0]

        count = 0

        for num in nums :

            if candidate == num :
                count +=1
            
            else :
                count -= 1

                if not count : 
                    candidate = num

                    count = 1

        return candidate

    def majorityElement(self, nums: List[int]) -> int:
        
        # return self.majorityElementHashMap(nums)

        return self.majorityElementBoyerMoore(nums)
