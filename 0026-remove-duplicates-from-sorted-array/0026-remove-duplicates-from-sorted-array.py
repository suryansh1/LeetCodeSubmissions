class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ####### EXTRA SPACE #####
        # result = []
        # for i, val in enumerate(nums):

        #     if result == [] :
        #         result.append(val)
        #         continue

        #     if val > result[-1] : 
        #         result.append(val)

        # for i, val in enumerate(result):
        #     nums[i] = val

        # return len(result)

        ##### TWO POINTERS #####

        ptr1, ptr2 = 0, 1

        size = len(nums)
        
        while(ptr2 < size):

            while nums[ptr2] == nums[ptr1]:
                ptr2 +=1
                
                if ptr2 >= size : return ptr1 + 1

            ptr1 += 1

            nums[ptr1] = nums[ptr2]

            ptr2 += 1

        return ptr1 + 1
