```
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
```
import math
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
