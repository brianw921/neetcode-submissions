class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. put all the numbers in a hash key: numbers, value: count
        #2. initate a bucket of arrays and store the numbers in the array based on count
        #3. iterate through the array freq in reverse order and push it in to another array
        #4. once the length of the array reaches k return result

        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        #Time Complexity is O(n)
        #Space Complexity is O(n)