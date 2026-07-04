class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Brute Force approach:
        use the sorted form of words to find anagrams.
        Time Complexity: O(n * klogk) where n = len(nums), k = avg len of string
        Space Complexity: O(n)
        '''

        # anagrams = defaultdict(list)

        # for word in strs:
        #     anagrams[tuple(sorted(word))].append(word)
        
        # return list(anagrams.values())

        '''
        Efficient approach: 
        use a word_count arr and utilise ascii values of chars
        '''

        anagrams = defaultdict(list)

        for word in strs:
            count_arr = [0] * 26
            for ch in word:
                count_arr[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(count_arr)].append(word)

        return list(anagrams.values())
















