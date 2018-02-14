class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle == '':
            return 0
        if needle == '':
            return 0
        if haystack == '':
            return -1
        
        next1 = self.getNext(needle)
        i = 0
        j = 0
        while(i < len(haystack)):
            if (j == -1 or haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                j = next1[j]
            if (j == len(needle)): 
                return i - j
        return -1
    def getNext(self, needle):
        next1 = [0]*len(needle)
        leng = len(needle)
        next1[0] = -1
        k = -1
        i = 0
        while(i < leng - 1):
            if (k == -1) or (needle[k] == needle[i]):
                i += 1
                k += 1
                next1[i] = k
            else:
                k = next1[k]
        return next1