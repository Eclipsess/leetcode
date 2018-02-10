class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = res = 0;
        usedChar = {};
        for i,v in enumerate(s):
            if v in usedChar and start <= usedChar[v]:    #如果已经使用的字符在start之前或=可以忽略
                start = usedChar[v] + 1;
            else:
                res = max(res,i - start +1)
            usedChar[v] = i;
        return res;

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start  = 0
        reslen = 0
        usedChar = {}
        for i,c in enumerate(s):
            if c in usedChar and usedChar[c] >= start:
                reslen = max(reslen, i - start)
                start = usedChar[c] + 1
            usedChar[c] = i
        return max(reslen, len(s) - start)
            