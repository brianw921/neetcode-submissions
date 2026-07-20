class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. create 2 hash to store the chars
        #2. iterate through each hash and compare the values of each hash
        #3. if the keys are not the same, return False
        #4. return True

        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i] ,0)
        
        for c, n in hashS.items():
            if hashT.get(c, 0) != n:
                return False
        return True

        #Time Complexity O(N)
        #Space Complexity O(N)