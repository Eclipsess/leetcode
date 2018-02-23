class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        flag = 0
        for i in range(1,nums_len)[::-1]:
            if nums[i-1] < nums[i]:
                flag = i
                #nums[i-1],nums[i] = nums[i],nums[i-1]
                for i in range(flag, nums_len)[::-1]:
                    if nums[i] > nums[flag - 1] or i == flag:
                        nums[i],nums[flag-1] = nums[flag-1],nums[i]
                        break
                break
        #print nums
        r = nums_len - 1
        while(flag < r):
            #print flag
            #print nums
            nums[flag],nums[r] = nums[r], nums[flag]
            flag += 1
            r -= 1