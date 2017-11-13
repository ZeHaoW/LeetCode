class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = 1
        while x/num>=10:
        	num*=10

        while num>0:
        	right = x%10
        	left = x/num
        	if left != right:
        		return False
        	x = x%num/10
        	num = num/100
        return True