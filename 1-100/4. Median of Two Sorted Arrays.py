class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        index = (length - 1) // 2
        if length % 2:
            return nums[index]
        else:
            return (nums[index] + nums[index + 1]) / 2.0