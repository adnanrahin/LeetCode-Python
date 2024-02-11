class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        word_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = []
            word_map[sorted_word].append(word)

        for key in word_map.keys():
            result.append(word_map[key])

        return result

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))