class Solution:

    def maxSlidingWindowQueue(self, nums: List[int], k: int) -> List[int]:
        
        result = []

        queue = deque()

        for i, num in enumerate(nums[:k]):

            while queue and num > nums[queue[-1]] : 
                queue.pop()

            queue.append(i)

        result.append(nums[queue[0]])

        left = 0

        for right in range(k, len(nums)):

            left += 1

            if queue and queue[0] == right - k :
                queue.popleft()

            while queue and nums[right] >= nums[queue[-1]]:

                queue.pop()

            queue.append(right)

            result.append(nums[queue[0]])

        return result


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        return self.maxSlidingWindowQueue(nums, k)

        result = []

        max_window = nums[0]

        max_index = 0

        for i, num in enumerate(nums[:k]):

            if num >= max_window : 
                max_index, max_window = i, num

        result.append(max_window)

        left = 0

        for right in range(k, len(nums)):

            left += 1

            if max_index < left :
                # Scan the whole window from left to right
                
                max_index, max_window = left, nums[left]

                for j, num in enumerate(nums[left:right + 1]):

                    if num > max_window :

                        max_index, max_window = left + j, num
          
            else : 
                # Update max_window with nums[right]
                if nums[right] > max_window :

                    max_index, max_window = right, nums[right]
            
            result.append(max_window)

        return result

        #  max_index, max_window, left, right, j, nums[j],nums[left], nums[right], result
        #   1           3           1   3                   3           -3          [3]
        #   1           3                                                           [3,3]
        #   1           3           2     4                 -1          5
        #   2           -1                      2   5
        #   4           5           2       4                                       [3,3,5]