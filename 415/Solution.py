import itertools
class Solution(object):
    def addStrings(self, num1, num2):
        iteror = itertools.izip_longest(num1[::-1], num2[::-2], fillvalue='0')
        res, bit = [], 0
        for i in iteror:
            sumBit = int(i[0]) + int(i[1]) + bit
            res.insert(0, sumBit%10)
            bit = sumBit/10
        return ('1' if bit else '') + ''.join(res)



















        minlength, maxlength = min(len(num1), len(num2)), max(len(num1), len(num2))
        num = num1 if len(num1) > len(num2) else num2 
        res = []
        bit = 0
        for i in range(1, minlength+1):
            bitSum = int(num1[-i]) + int(num2[-i]) + bit
            res.insert(0, str(bitSum%10))
            bit = bitSum/10
        for i in range(minlength+1, maxlength+1):
            bitSum = int(num[-i]) + bit
            res.insert(0, str(bitSum%10))
            bit = bitSum/10
        if bit != 0:
            res.insert(0, str(bit))
        return ''.join(res)