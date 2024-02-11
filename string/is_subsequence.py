class Solution(object):
    def isSubsequence(self, s, t):
        ptr = 0
        count = 0
        for i in range(len(s)):
            for j in range(ptr, len(t)):
                if s[i] == t[j]:
                    count += 1
                    ptr = j + 1
                    break
        return count == len(s)

print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
print(Solution().isSubsequence("aaaaaa", "bbaaaa"))