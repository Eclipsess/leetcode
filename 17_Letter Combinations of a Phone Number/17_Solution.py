class Solution(object):
    dic = {}
    dic['0']=""
    dic['1']=""  
    dic['2']="abc"
    dic['3']="def"  
    dic['4']="ghi"  
    dic['5']="jkl"  
    dic['6']="mno"  
    dic['7']="pqrs"  
    dic['8']="tuv"  
    dic['9']="wxyz"
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        self.res = []
        tmp = [''] * len(digits)
        return self.func(0, digits, tmp)
    def func(self, index, digits, tmp):
        if index >= len(digits):
            self.res.append(''.join(tmp))
            return 
        for letter in self.dic[digits[index]]:
            #print 'letter',letter
            tmp[index]=letter
            self.func(index+1, digits, tmp)
        return self.res

digits = '23'
a = Solution()
print a.letterCombinations(digits)

