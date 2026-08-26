class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1. using a hash or a set store the numbers that are seen
        #2. iterate though the array and if the num is in seen return True
        #3. if not in seen return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        return False

        #Time Complexity O(N)
        #Space Complexity O(N)