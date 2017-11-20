class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:return True
        if num == 0:return False
        if num & 1 == 0 or num % 3 == 0 or num % 5 == 0:
            while num != 1:
                if num & 1 == 0:
                    num /= 2
                elif num % 3 == 0:
                    num /= 3
                elif num % 5 == 0:
                    num /= 5
                else:return False
            return True
        else: return False