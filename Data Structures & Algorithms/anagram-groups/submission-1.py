class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Brute Force approach:
        use the sorted form of words to find anagrams.
        '''

        anagrams = defaultdict(list)

        for word in strs:
            anagrams[tuple(sorted(word))].append(word)
        
        return list(anagrams.values())