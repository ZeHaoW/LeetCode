class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        i = 2
        while i <= num/i:
            if num % i == 0:
                sum += i+num/i
            i+=2
        return sum == num
