# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        frontindex = 1
        while frontindex < n:
            if isBadVersion((frontindex + n)/2):
                n = (frontindex + n)/2
            else:
                frontindex = (frontindex + n)/2 + 1
        return frontindex