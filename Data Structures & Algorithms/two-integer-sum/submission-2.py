class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. use a hash to store the number and its index
        #2. iterate through the array and calculate the difference
        #3. as you iterate check if the difference is in the set
        #4. if the difference is in the array, return the index

        numbers = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numbers:
                return [numbers[diff], i]
            numbers[n] = i
        #Time complexity O(N)
        #Space Complexity O(N)
        