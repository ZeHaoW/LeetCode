class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**0.5)**2 == N
        return any(is_square(c-a**2) for a in range(int(c**.5) + 1))

if __name__ == '__main__':
    print Solution().judgeSquareSum(17)