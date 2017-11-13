from itertools import combinations
class Solution(object):
	def readBinaryWatch(self, num):
		res = []
		for i in combinations(range(10), num):
			h, m = 0, 0
			for c in i:
				if c < 4:
					h = h | 1<<c
				else:
					m = m | 1<<(c-4)
			if h < 12 and m < 60:
				res.append(str(h) + ':' + str(m).zfill(2))
		return res