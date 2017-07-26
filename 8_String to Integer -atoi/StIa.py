import numpy as np

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # ！！！！最开始没有想到这种情况
        if str == '':              
            return 0
        # 控制正负
        positive = 1                
        #str = '   a-1 23'
        lenstr = len(str)
        # 需要初始化sum和k
        sum = 0                      
        k = 0

        # 如果为空格就舍去，直到出现有字符的一项
        for i in range(lenstr):
            if str[i] != ' ':        
                k = i
                break
        str = str[k:]

        # 判断如果第一个符号是+或-，则从第二个字符开始取数字部分
        if str[0] == '-':             
            positive = -1;
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        #print (str)
        for i in str:
            # ord函数将字符转化成ascii的值，比如ord('0')=48
            if (ord(i) >= ord('0') ) and (ord(i) <= ord('9')):                    
                sum = sum * 10 + (ord(i) - ord('0'))
                #提交时没有考虑到下面的情况
                if positive ==1 and sum >= 2147483647:
                    return 2147483647
                if positive == -1 and sum >= 2147483648:
                    return -2147483648
            else:
                break
        sum *= positive
        return sum

# f = Solution()
# str = '             -012a3'
# print(f.myAtoi(str))
