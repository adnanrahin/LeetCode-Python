class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
                elif char == ')':
                    if stack.pop() != '(':
                        return False

                elif char == '}':
                    if stack.pop() != '{':
                        return False

                elif char == ']':
                    if stack.pop() != '[':
                        return False

        return len(stack) == 0


print(Solution().isValid('(){}[]'))
