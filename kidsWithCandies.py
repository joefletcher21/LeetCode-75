class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currentMax = candies[0]
        result = []
        for i in candies:
            if i > currentMax:
                currentMax = i
        for i in candies:
            result.append((i + extraCandies) >= currentMax)
        return result
