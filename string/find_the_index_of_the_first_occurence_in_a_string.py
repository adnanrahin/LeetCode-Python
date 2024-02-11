class Solution(object):
    def strStr(self, haystack, needle):
        piTable = self.piTable(haystack, needle)
        for i in range(len(needle), len(piTable)):
            if piTable[i] == len(needle):
                return i - (2 * len(needle))

        return -1

    def piTable(self, text, pattern):
        str = pattern + "#" + text
        piTable = [0] * len(str)
        i = 0
        j = 1
        while j < len(str):

            if str[i] == str[j]:
                piTable[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                piTable[j] = 0
                j += 1
            else:
                i = piTable[i - 1]

        return piTable


print(Solution().piTable("asaxdfaxej", "axe"))
