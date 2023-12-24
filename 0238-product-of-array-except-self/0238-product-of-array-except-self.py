class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
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

        

