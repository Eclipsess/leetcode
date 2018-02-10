class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp = '('
        res = []
        return self.func(res, temp, 1, 2*n)
    
    def func(self, res, temp, k, n):
        
        if temp.count(')') > n/2 or temp.count('(') > n/2 or temp.count(')') > temp.count('('):
            return 
        if k == n :
            res.append(temp)
        else:
            self.func(res, temp + '(', k+1, n)
            self.func(res, temp + ')', k+1, n)
        return res

