class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1. create an array with 1s
        #2. have a tracker for the prefix and the post fix
        #3. iterate through the array and set the array prefix and postfix and then multiply the prefix and postfix by the number
        #4. do it in reverse order
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

        #Time Complexity O(n + m)
        #Space Complexity is O(N)