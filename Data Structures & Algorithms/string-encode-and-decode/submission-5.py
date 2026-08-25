class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for s in strs:
            words.append(str(len(s)))
            words.append("#")
            words.append(s)
        return "".join(words)

    def decode(self, s: str) -> List[str]:
        # // 5#Hello5#World
        
        #1. use a i counter to keep track of the index of each char
        #2. use a j index to keep track of the next word
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
            
            
