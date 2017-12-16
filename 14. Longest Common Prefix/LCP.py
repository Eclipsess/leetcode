class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        minLen = min([len(s) for s in strs])
        if minLen == 0:
        	return ""
        q=0
        for i in range(minLen):
            q = i
            k = strs[0][i]
            for j in strs:
                if k == j[i]:
                	continue
                elif i == 0:
                    return ""
                else:
                    return strs[0][:i]
        return strs[0][:q+1]

s = Solution()
ss = s.longestCommonPrefix(['aa','ab'])
print ss
