class Solution(object):
	def isPowerOfThree(self, n):
		n = float(n)
		while n > 1:
			n = n/3
		return n == 1