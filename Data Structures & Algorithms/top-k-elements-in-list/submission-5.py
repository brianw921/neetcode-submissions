class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. put the numbers in to a hash by count
        #2. iterate through the array backwards and put it in to result
        #3. once it reaches k return result
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)
        result = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

        #Time Complexity is o(n)
        #Space Complexity is o(n)