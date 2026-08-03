class Solution:

    def encode(self, strs: List[str]) -> str:
        #1. create an array to store the string
        #2. append the length of the array
        #3. append a special char
        #4. append the string
        #5. join the string
        words = []
        for string in strs:
            words.append(str(len(string)))
            words.append("#")
            words.append(string)
        return "".join(words)


    def decode(self, s: str) -> List[str]:
        #5#Hello5#World
        #1. create an array to return the result
        #2. have an i counter to keep track of the index of each char
        #3. have a j counter to keep track of the next number
        #4. once we get the index between i and j, splice it and append the char
        #5. set the i counter to j
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

