class Solution(object):
    # 最普通的做法
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 :return False
        while num != 1:
            if num % 4 != 0:
                return False
            num /= 4
            print num
        return True

    # 不依赖循环和递归的写法1
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and (num-1) % 3 == 0


    # 不依赖循环和递归的写法2
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and num & 0x55555555 != 0