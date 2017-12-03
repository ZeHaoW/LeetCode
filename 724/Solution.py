class Solution(object):
    def pivotIndex(self, nums):
        left_sum, right_sum = 0, sum(nums[1:])
        if left_sum == right_sum:
            return 0
        res = 1
        while res < len(nums)-1:
            left_sum += nums[res-1]
            right_sum -= nums[res]
            if left_sum == right_sum:
                return res
            res += 1
        return -1