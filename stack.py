class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token == '+':
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                total = (b - a)
                stack.append(total)
            elif token == '*':
                total = stack.pop() * stack.pop()
                stack.append(total)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                total = int(b / a)
                stack.append(int(total))
            else:
                stack.append(int(token))

        return stack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
