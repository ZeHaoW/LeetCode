# 算法思想：从0开始一步步生成最终的数列，得出最大的值
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )

# 我的写法(Time Limit exceed)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.func(nums, len(nums))


    def func(self, nums, k):
            if k == 0: return 0
            if k == 1: return nums[0]
            if k == 2: return max(nums[0], nums[1])
            return max(self.func(nums, k-2) + nums[k-1], self.func(nums, k-1))


# 大神的写法，巧用平行赋值，26ms
class Solution(object):
    def rob(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max((last + i), now)
        return now

# 由此可见，同一种算法思想，同一种语言，不同的写法也能导致运行时间的天壤之别，长见识了