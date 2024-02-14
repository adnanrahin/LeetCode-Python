class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = dict()
        count = 0
        global_count = 0
        for i in range(len(s)):
            if s[i] in char_dict:
                count = max(count, char_dict[s[i]])
            global_count = max(i + 1 - count, global_count)
            char_dict[s[i]] = i + 1

        return global_count