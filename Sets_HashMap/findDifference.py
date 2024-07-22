class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = dict()
        num2 = dict()
        size = max(len(nums1), len(nums2))
        for i in range(size):
            if len(nums1) > i and nums1[i] not in nums2:
                num1[nums1[i]] = 1
            if len(nums2) > i and nums2[i] not in nums1:
                num2[nums2[i]] = 1

        return list(num1.keys()), list(num2.keys())
