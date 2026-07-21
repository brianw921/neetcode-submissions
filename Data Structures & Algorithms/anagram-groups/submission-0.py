class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. Create a count array with size 26 and all zeros
        #2. For each char in the string, increment the count at the corresponding index
        #3. Conver the count array to a tuple and use it as a key
        #4. Append the string to the list associated with this key

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())

        #Time Complexity O(N)
        #Space Complexity O(N)
