class Solution(object):
    def isValid(self, s):
        bracket = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char not in bracket and not stack:
                return False
            elif char in bracket:
                stack.append(char)
            elif bracket[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
a = Solution()
print(a.isValid(s="(])"))
