class Solution(object):
    def reverseWords(self, s):
        strs = s.split()
        str = ""
        for i in range(len(strs) - 1, -1, -1):
            if i != 0:
                str += (strs[i] + " ")
            else:
                str += (strs[i])
        return str

    def reverseWords(self, s):
        strs = s.split()
        strs.reverse()
        return " ".join(strs)


print(Solution().reverseWords("a good   example  "))
