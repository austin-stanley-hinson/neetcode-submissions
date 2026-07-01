class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            word_count = [0]*26
            for ch in word:
                word_count[ord(ch) - ord('a')] += 1 
            
            if tuple(word_count) not in anagrams: 
                anagrams[tuple(word_count)] = []
            
            anagrams[tuple(word_count)].append(word)

        return list(anagrams.values())
            

