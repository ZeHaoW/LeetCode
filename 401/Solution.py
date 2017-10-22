class Solution(object):
    def readBinaryWatch(self, num):
        from itertools import combinations
        
        res = []
        for c in combinations(range(10), num):
            # c is a list indicating which bit should be 1
            h, m = 0, 0
      
            for p in c:
                if p < 4:
                    h = h | 1 << p # bit for hour
                else:
                    m = m | 1 << (p - 4) # bit for minuts
            
            if h < 12 and m < 60:
                res.append(str(h) + ":" + str(m).zfill(2))
        
        print res
if __name__ == '__main__':
	Solution().readBinaryWatch(8)