class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                continue
            if len(stack) == 0: return False
            if i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[' or i == '}' and stack[-1] == '{':
                stack.pop()
                continue
            else: 
                return False
        return True if len(stack) == 0 else False

