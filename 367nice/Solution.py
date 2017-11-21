class Solution(object):
    # 我的方法
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:return False
        i = 2
        while i < num/i:
            i += 1
        if i > num/i:return False
        return False if num%i != 0 else True

    # 利用一个完全平方数等于1+3+5+7+...
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    # 利用类似二分法的方式来逼近
    def isPerfectSquare(self, num):
        start, high = 1, num
        while start <= high:
            mid = (start + high) >> 1
            if mid*mid == num:
                return True
            elif mid*mid < num:
                start = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == '__main__':
    print Solution().isPerfectSquare(35)