class Solution(object):
    # 我的解法
    def reverse(self, x):
        if x > 2**31-1 or x < -(2**31-1):
            return 0
        strnum = str(x)
        if x <0:
            strnum = strnum[1:]
        res = strnum[::-1]
        if res[0] == 0 :
            if int(res[1:]) > 2**31-1:
                return 0
            else:
                return int('-' + res[1:]) if x < 0 else int(res[1:])
        if int(res) > 2**31-1:
            return 0
        else:
            return int('-' + res) if x < 0 else int(res)

    # genuis solution
    def reverse1(self, x):
        # s是x的符号
        s = cmp(x, 0)
        # ``符号相当于str()
        r = int(`s*x`[::-1])
        # 巧妙的处理了溢出
        return s*r*(r<2**31)