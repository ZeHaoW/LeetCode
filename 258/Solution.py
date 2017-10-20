class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
        	tmp = 0
        	while num > 0:
        		tmp += num%10
        		num = num/10
        	num = tmp
        return num