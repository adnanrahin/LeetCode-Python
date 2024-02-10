class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix_length = 0
        prefix_str = ""
        shortest_strings = self.get_shortest_strings(strs)

        for i in range(len(shortest_strings)):
            for str in strs:
                if str[i] != shortest_strings[i]:
                    return prefix_str
            prefix_str += shortest_strings[i]
        return prefix_str

    def get_shortest_strings(self, strs):
        count = len(strs[0])
        shortest_str = strs[0]
        for str in strs:
            if len(str) < count:
                count = len(str)
                shortest_str = str
        return shortest_str


print(Solution().longestCommonPrefix(["flower", "flow", "flight", "f"]))
