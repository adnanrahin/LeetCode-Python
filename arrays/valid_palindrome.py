class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.is_alpha(s[left]):
                left += 1
            elif not self.is_alpha(s[right]):
                right -= 1

            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

    def is_alpha(self, char):
        return (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9')


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("A man, a plan, a canal: Pnama"))
print(Solution().isPalindrome("0P"))
