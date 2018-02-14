class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if dividend == 0:
            return 0

        FLAG = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            FLAG = -1

        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while(dividend >= divisor):
            times = 1
            sum = 0
            while(sum < dividend):
                times = times *2
                sum = times * divisor
            dividend -= times / 2 * divisor
            res += times / 2
        if res >= MAX_INT:
            if FLAG == -1 :
                return FLAG*MAX_INT - 1
            else:
                return FLAG*MAX_INT
        return FLAG*res
        