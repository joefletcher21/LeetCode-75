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
        elif nums.count(1) + nums.count(-1) == len(nums):
            
        else:    
            while start < len(nums):
                for i in range(len(nums)):
                    if start is not i:
                        product = product * nums[i]
                results.append(product)
                product = 1
                start += 1
        return results
