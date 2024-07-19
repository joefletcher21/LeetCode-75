class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxTotal = currTotal = sum(nums[:k])
        if len(nums) > k:    
            for i in range(len(nums)-k):
                currTotal += nums[k+i] - nums[i]
                maxTotal = max(currTotal,maxTotal)
        return maxTotal/k
