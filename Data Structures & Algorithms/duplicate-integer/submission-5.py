class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1. use a set to keep track of the numbers
        #2. iterate through the array
        #3. if seen return True, add the number to the array
        #4. return false

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

        #Time complexity is O(N)
        #Space complexity is O(N)