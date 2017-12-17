class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        ressort = []
        for i in range(len(nums)):
            # [0,0,0][-1] = 0
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while(l < r):
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    num3 = [nums[i], nums[l], nums[r]]
                    # if sorted(num3) not in ressort:
                    #     ressort.append(sorted(num3))
                    res.append(num3)
                    while(l < r and nums[l+1] == nums[l] ):
                        l += 1
                    while(r > l and nums[r-1] == nums[r]):
                        r -= 1
                    l += 1
                    r -= 1
        return res

s = Solution()
print s.thressSum([1,1,1])
