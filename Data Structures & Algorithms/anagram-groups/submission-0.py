class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)
        val = []

        for word in strs:

            sorted_word = tuple(sorted(word))
            group[sorted_word].append(word)

        for value in group.values():
            val.append(value)
        
        return val

            
