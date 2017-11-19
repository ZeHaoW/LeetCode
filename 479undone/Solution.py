class Solution(object):
    def largestPalindrome(self, n):
    	if n == 1 return 9
        maxnum = str((10*n-1)*(10*n-1))
        while True:
	        if maxnum == maxnum[::-1]:
	        	break
	        else:
	        	firsthalf = maxnum[0:len(maxnum)/2]
	        	secondhalf = maxnum[len(maxnum)/2:len(maxnum)] if len(maxnum)%2 == 0 else maxnum[len(maxnum)/2+1:len(maxnum)]
	        	if int(firsthalf[::-1]) > int(secondhalf):
	        		maxnum = str(int(firsthalf)　- 1) + str(int(firsthalf)　- 1)[::-1]
	        		break
	        	else:
	        		maxnum = firsthalf +　firsthalf[::-1]
	        		break

	   　while !self.isProduct(int(maxnum), n):
	    	firsthalf = maxnum[0:len(maxnum)/2]
	    	maxnum = str(int(firsthalf) - 1)+ reversed(str(int(firsthalf) - 1))

	    return int(maxnum)%1337


	def isProduct(self, pro, n):
		i = 10*n-1
		while i > pro/i:
			if pro%i == 0:
				return True
			i-=1
		return False
