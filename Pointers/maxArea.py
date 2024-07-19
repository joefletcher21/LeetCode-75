class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height)-1
        start = 0
        maxArea = 0

        if max(height) == 1:
            maxArea = end
        while(start < end):
            currentArea = min(height[start], height[end]) * (end-start)
            print(start,end,currentArea, maxArea)
            maxArea= max(currentArea,maxArea)
            
            if height[start] < height[end]:
                start+=1
            else:
                end -=1
        return maxArea
