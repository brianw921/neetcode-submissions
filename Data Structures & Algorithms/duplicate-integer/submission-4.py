class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1. use a set to store the numbers
        #2. iterate through the array and check if the number is in the set
        #3. if number is in set return True
        #4. if number is not in set return False

        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False

        #1. Time Complexity is O(N)
        #2. Space Complexity is O(N)