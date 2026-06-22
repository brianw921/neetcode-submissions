class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1. use a hashset to store the numbers
        #2. itrate through the set and check if the numbers are in the array
        #3. if the numbers are in the hashset, return True
        #4. if numbers are not in the hashset, add the number to the hashset
        #5. return False

        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False 

        #Time complexity is O(N)
        #Space Complexity is O(N)
