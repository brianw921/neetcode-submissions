class Solution:

    def encode(self, strs: List[str]) -> str:
        #1. create an array that stores the len of string special char, and the word
        words = []
        for s in strs:
            words.append(str(len(s)))
            words.append("#")
            words.append(s)
        return "".join(words)

    def decode(self, s: str) -> List[str]:
        #1. have an i pointer to keep track of the index of the char, 
        #2. have a j pointer to keep track of the next word
        #3. have an array to store the result
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result
