class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. store the numbers using a hash
        #2. convert it in to a heap
        #3. push the numbers in to the heap
        #4. when it's more than k, pop from the heap

        count = Counter(nums)
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

        #Time Copmlexity is o(n log k)
        #Space complexity is o(n)