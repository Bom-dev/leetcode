class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = []
        num = nums[0]
        final.append(num)
        for i in range(len(nums)-1):
            num += nums[i+1]
            final.append(num)
        return final
