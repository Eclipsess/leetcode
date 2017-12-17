class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        strx = str(x)
        strx_ = strx[::-1]
        if strx == strx_:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(12321)
