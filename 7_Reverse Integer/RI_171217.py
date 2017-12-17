class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = -1 * int( str(-x) [::-1])
        else:
            y = int(str(x)[::-1])
        if y > 2147483647 or y < -2147483647:
            y = 0
        return  y

if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
