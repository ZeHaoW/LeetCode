# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import bisect
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect.bisect(C(), -1, 1, n)

if __name__ == '__main__':
    Solution().guessNumber(6)
