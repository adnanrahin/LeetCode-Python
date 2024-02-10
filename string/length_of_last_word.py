class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        space = False
        for i in range(len(s) - 1, -1, -1):
            if s[i].isspace():
                space = True
            elif not s[i].isspace() and space:
                space = False
                count = 1
            else:
                count += 1
        return count


print(Solution().lengthOfLastWord('Hello World'))
