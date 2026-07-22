class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        #Time complexity is O(n log k)
        # n is the number of elements in the input list nums
        # k is the number of top frequent elements to return
        #Space complexity is O(n)
