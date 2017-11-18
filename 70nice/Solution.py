class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
        	return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


        # genius solution
        a = b = 1
        for _ in range(n):
        	a, b = b, a+b
        return a

if __name__ == '__main__':
	print Solution().climbStairs(35)

	# 看看人家是怎么写斐波那契数列的，别用递归，贼慢！！！！！