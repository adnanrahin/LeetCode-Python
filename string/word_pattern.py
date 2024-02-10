class Solution(object):
    def wordPattern(self, pattern, s):
        p_map = {}
        s = s.split()
        str_map = {}
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            str_map[s[i]] = pattern[i]
            p_map[pattern[i]] = s[i]

        for i in range(len(s)):
            if p_map[pattern[i]] != s[i] or str_map[s[i]] != pattern[i]:
                return False
        return True


print(Solution().wordPattern("abba",  "dog cat cat dog"))