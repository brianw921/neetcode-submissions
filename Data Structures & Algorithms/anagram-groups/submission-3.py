class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. use a hash to store all the instances of the anagram
        #2. iterate through each word and create an array with size 26 
        #3. take the ascii value of each word and put it in the array
        
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(word)
        return list(result.values())

        #Time complexity is O(n * k)
        #Space complexity is O(n * k) ig given axiulry space or O(N*M) total space