class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0
        return ans
