class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] != nums[i]:
                cur += 1
                nums[cur],nums[i] = nums[i], nums[cur]
        return cur + 1