class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        anagram_arr = [0] * 26  # Initialize with zeros

        for i in range(len(s)):
            anagram_arr[ord(s[i]) - ord('a')] += 1
            anagram_arr[ord(t[i]) - ord('a')] -= 1

        for count in anagram_arr:
            if count != 0:
                return False
        return True
