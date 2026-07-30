class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. store the numbers in a hash with their frequencey
        #2. intiate an array of arrays to store the numbers
        #3. sort the numbers in to the index of the array based on count
        #4. iterate through the array in reverse order
        #5. once k == 2, return the array

        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        result = []
        print(freq)
        for i in range(len(freq) - 1, 0, - 1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            