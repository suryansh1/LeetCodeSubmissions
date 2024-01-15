class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Using built in Counter
        counter = Counter(nums)

        # return [pair[0] for pair in counter.most_common(k)]

        # Using dictionary

        # # 1. Loop through nums and generate a mapping of num:count O(n)

        # # LOOP 2 - 4 k times

        # # 2. Obtain the element in dictionary with max count O(n)

        # # 3. Add it to ret list O(1)

        # # 4. Delete it from dictionary O(1)

        # # Total time complexity O(n*k), and if k == n, O(n^2)

        # Using HEAP

        heap = []
        for num, freq in counter.items():

            heapq.heappush(heap, (-freq, num))

            # if len(heap) > k:
                # heapq.heappop(heap)

         # The heap is a maxheap 

        result = [heapq.heappop(heap)[1] for i in range(k)]
        # result = [element for _, element in heap]
        return result