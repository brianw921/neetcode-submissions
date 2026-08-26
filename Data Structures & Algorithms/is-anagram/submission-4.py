class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS = {}
        charT = {}

        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i], 0)
            charT[t[i]] = 1 + charT.get(t[i], 0)
        
        for char in charS:
            if charS[char] != charT.get(char, 0):
                return False
        return True

        #Time Complexity o(n)
        #Space Complexity o(1) becuase the alphabet is limited to 26 chars