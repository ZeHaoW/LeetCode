class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            flag = 1
            ss = str(num)
            if '0' in ss:continue
            for i in ss:
                if num % int(i) != 0:
                    flag = 0
                    break
            if flag == 1:
                res.append(num)
        return res

if __name__ == '__main__':
    print Solution().selfDividingNumbers(1, 22)