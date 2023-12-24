class Solution:

    def productExceptSelfExponent(self, nums: List[int]) -> List[int]:


        zeros_index = []
        non_zeros_index = []

        for i, num in enumerate(nums):

            if num == 0 : zeros_index.append(i)

            else : non_zeros_index.append(i)

        if len(zeros_index) > 1 : return [0]*len(nums)

        if len(zeros_index) == 1 :

            return_list = [0]*len(nums)

            return_list[zeros_index[0]] = 1

            for i in non_zeros_index : 

                return_list[zeros_index[0]] *= nums[i]

            return return_list

        return_list = [1]*len(nums)

        product = 1

        for num in nums : product*=num

        for i, num in enumerate(nums):
            return_list[i] = int(product * pow(num, -1))

        return return_list

    def productExceptSelfPrefixSuffix(self, nums: List[int]) -> List[int]:

        prefix, suffix, answer = [1]*len(nums), [1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        # print(prefix, suffix)
        for i, num in enumerate(nums):
            answer[i] = prefix[i] * suffix[i]

        return answer




    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # return self.productExceptSelfExponent(nums)
        return self.productExceptSelfPrefixSuffix(nums)