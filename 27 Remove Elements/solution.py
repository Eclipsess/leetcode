class Solution(object):
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
    
    def removeElement(self, nums, val):  
        if nums == []:
            return None
        len_ = len(nums)
        i=0
        while(i < len_):
            if nums[i] == val:
                del nums[i]
                len_ -= 1
                i -= 1
            i += 1
                # k = i + 1
                # while (k < len(nums) and nums[k] == val):
                #     k += 1
                # dnum = k - i
                # for j in range(k, len(nums)):
                #     nums[j - dnum] = nums[j]
        return len(nums)