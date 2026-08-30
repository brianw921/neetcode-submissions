class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. create an array with buckets
        #2. create a hash and store the count of each number 
        #3. iterate through the hash and place them in the array based on index
        #4. in reverse order iterate through the array of buckets, and return the result after k time
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        result = []

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

            
        

        