class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1. create a set for the nums
        #2. initialize a variable with 0 to keep track of the longest
        #3. iterate through the numSet and if the number -1 is not in the numSet, start the count
        #4. so while the number above it is in the numset increase the count by 1
        #5. take the max between the longest, and the count

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        #Time Complexity O(N)
        #Space Complexity O(N)
                
                

