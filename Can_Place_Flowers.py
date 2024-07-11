import math
import copy
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        if n == 0:
            return True
        for i in flowerbed:
            if i == 1:
                count+=1
        maxCount = math.ceil(len(flowerbed)/2.0)
        if n > (maxCount-count):
            return False
        copyArr = copy.deepcopy(flowerbed)
        for i in range(len(copyArr)):
            if copyArr[i] == 0 and (i == 0 or copyArr[i-1] == 0) and (i == len(copyArr)-1 or copyArr[i+1] == 0):
                copyArr[i] = 1
                n-=1
            if n == 0:
                return True
        return False
