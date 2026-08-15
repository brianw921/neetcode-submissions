class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. store all the numbers in a hash with it's count
        #2. create an array with 7 buckets
        #3. sort the numbers based on count in the array
        #4. reverse through the array and return the number up to k

        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)

        result = []

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result