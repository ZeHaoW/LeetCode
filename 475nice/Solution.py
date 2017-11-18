class Solution(object):

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        res, i = 0, 0
        for house in houses:
            while i < len(heaters) - 1 and heaters[i+1] + heaters[i] < house*2:
                i += 1
            res = max(res, abs(house - heaters[i]))
        return res


        该算法的思想是，寻找距离每个house最近的一个heater，计算他们之间的距离，然后从这些距离中选择一个最大值。第13行，很聪明
