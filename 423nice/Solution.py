class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        if 'z' in s:
        	num = s.count('z')
        	s = s.replace('z', '').replace('e', '', num).replace('r', '', num).replace('o', '', num)
        	while num!=0:
        		res.append(0)
        		num-=1

        if 'w' in s:
        	num = s.count('w')
        	s = s.replace('w', '').replace('t', '', num).replace('o', '', num)
        	while num!=0:
        		res.append(2)
        		num-=1

        if 'u' in s:
        	num = s.count('u')
        	s = s.replace('u', '').replace('f', '', num).replace('o', '', num).replace('r', '', num)
        	while num != 0:
        		res.append(4)
        		num-=1

        if 'x' in s:
        	num = s.count('x')
        	s = s.replace('x', '').replace('s', '', num).replace('i', '',  num)
        	while num != 0:
        		res.append(6)
        		num-=1

        if 'g' in s:
        	num = s.count('g')
        	s = s.replace('g', '').replace('e', '', num).replace('i', '', num).replace('h', '', num).replace('t', '', num)
        	while num != 0:
        		res.append(8)
        		num-=1

        if 'o' in s:
        	num = s.count('o')
        	s = s.replace('o', '').replace('e', '', num).replace('n', '', num)
        	while num != 0:
        		res.append(1)
        		num-=1
        if 't' in s:
        	num = s.count('t')
        	s = s.replace('t', '').replace('e', '', 2*num).replace('r', '', num).replace('h', '', num)
        	while num != 0:
        		res.append(3)
        		num-=1

        if 'f' in s:
        	num = s.count('f')
        	s = s.replace('f', '').replace('e', '', num).replace('i', '', num).replace('v', '', num)
        	while num != 0:
        		res.append(5)
        		num-=1
        if 's' in s:
        	num = s.count('s')
        	s = s.replace('s', '').replace('e', '', 2*num).replace('v', '', num).replace('n', '', num)
        	while num != 0:
        		res.append(7)
        		num-=1
        if 'i' in s:
        	num = s.count('i')
        	s = s.replace('i', '').replace('n', '', 2*num).replace('e', '', num)
        	while num != 0:
        		res.append(9)
        		num-=1

        return ''.join(map(str, sorted(res)))


#别人的代码
class Solution(object):
    def originalDigits(self, s):
        d = collections.Counter(s)
        res = []
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():
            res.append(x[0] * d[x[-1]])
            for c in x:
                d[c] -= d[x[-1]]
        return ''.join(sorted(res))