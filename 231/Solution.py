class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n is 1:
        	return True
        n = str(bin(n))[2:]
        if n[0] is not '1':
        	return False
        for i in range(len(n))[1:]:
        	if n[i] is not '0':
        		return False
        return True