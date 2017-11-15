class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = ''
        for i in range(len(nums)-1):
        	if nums[i+1] >= nums[i]:s += '1'
        	else:s += '0'
        if s.count('0') == 0:return True
        if s.count('0') > 1:return False
        index = s.index('0')+1
        if index == 1 or index == len(nums)-1:return True
        if nums[index+1] >= nums[index-1] or nums[index-2] <= nums[index]:return True
        return False
