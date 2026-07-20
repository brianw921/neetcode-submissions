class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. create a frequency array of size 26 initialized to 0
        #2. iterate through both strings
            # increment the count at index corresponding to s[i]
            # decreament the count at index corresponding to t[i]
        #3. After processing both strings, scan through the count array, and if 
            # any value is not 0 return false 
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True

        #Time complexity is O(n + m)
        #Space complexity is (n)