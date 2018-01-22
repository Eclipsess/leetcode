class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 == 1 or len(s) == 0 :
            return False
        for i in s:
            if i not in [')',']','}']:
                stack.append(i)
            elif len(stack) == 0:          #s = '))'
                return False
            elif i == ')' and stack.pop() == '(':
                continue
            elif i == ']' and stack.pop() == '[':
                continue
            elif i == '}' and stack.pop() == '{':
                continue
            else:
                return False
        if len(stack) == 0:    ## s = '(('
            return True
        else:
            return False