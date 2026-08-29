class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. iterate through the array 
        #2. for each word itialize an array with 0 * 26 chars
        #3. for each char take the ascii value of each char and add that index by 1
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(word)
        return list(result.values())
            
        #Time compleixty O(m * n)
        #Space complexity (m) auxliury space O(m* n) total space

        
