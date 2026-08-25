class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1. use a set to store numbers
        #2. iterate though the array and if number - 1 is in the set, increase the counter by 1
        #3. add the number to the set
        #4. take the max between the counter or the set
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # Time Complexity is O(n)
        # Space Complexity is o (N)
                