class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        results = []
        start = 0

        if 0 in nums == False:
            for i in nums:
                product = product * i
            for i in nums:
                results.append(product/i)
        elif nums.count(0) > 1:
            for i in nums:
                results.append(0)  
        else:    
            results = [1] * len(nums)
            for i in range(len(nums)):
                results[i] = results[i] * product
                product = product * nums[i]
            product = 1
            for i in range(len(nums)-1,-1,-1):
                results[i] = results[i] * product
                product = product * nums[i]
            
        return results
