class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 9
        k = 1
        while n > count:
            n -= count
            count = 9*10**k*(k+1)
            k += 1
        if n%k == 0:
            return (10**(k-1)+n/k-1) % 10
        else:
            return int(str(10**(k-1)+n/k)[n%k-1])