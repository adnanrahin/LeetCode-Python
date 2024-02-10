class Solution(object):
    def isIsomorphic(self, s, t):
        t_map = {}
        s_map = {}
        for i in (range(len(s))):
            t_map[t[i]] = s[i]
            s_map[s[i]] = t[i]

        for i in (range(len(s))):
            if s_map[s[i]] != t[i] or t_map[t[i]] != s[i]:
                return False

        return True

print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))